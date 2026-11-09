#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C08: distorsion geometrica (mapas de proyeccion, distorsion de una lente real trazada y calibracion polinomica).

Datos: ninguna constante fisica consultada. La lente (biconvexa, n = 1.5, radios de 100 mm, espesor de 4 mm), las posiciones del diafragma, los coeficientes verdaderos k1 = -4e-5 mm^-2 y
k2 = +3e-8 mm^-4 y el ruido de 0.005 mm son ILUSTRATIVOS (sinteticos); no se calibra ninguna camara real.
Modelo: (A) identidades de las proyecciones (tan, equidistante, estereografica, equisolida, ortografica); (B) distorsion del rayo principal de la lente trazada con el diafragma a 0, 40 y 80 mm
(trazado exacto) y su ajuste a Delta r / r = k1 r^2; (C) calibracion: rejilla de 11 x 11 estrellas con distorsion polinomica r_d = r (1 + k1 r^2 + k2 r^4) y ruido gaussiano (semilla 20261109),
ajuste lineal por minimos cuadrados de (k1, k2) con su incertidumbre, residuo y mapa inverso por iteracion de punto fijo.
Supuestos: distorsion radial pura, sin descentrado, centro conocido. Validez: ilustrativa.
Tolerancia: identidad de la estereografica con la tangente < 1e-12; coeficientes verdaderos dentro de 3 sigma; residuo cercano al ruido (10 %); inversa 1e-9 mm.
"""
from __future__ import annotations
import math, platform, random

# ---- Trazador de rayos exacto 3D para superficies conicas (biblioteca estandar) ----
def _mv(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2], M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2], M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2])

def _mtv(M, v):
    return (M[0][0]*v[0] + M[1][0]*v[1] + M[2][0]*v[2], M[0][1]*v[0] + M[1][1]*v[1] + M[2][1]*v[2], M[0][2]*v[0] + M[1][2]*v[1] + M[2][2]*v[2])

def _mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def _rot(ax, ay):
    """Rotacion: primero ax alrededor de x y luego ay alrededor de y (radianes)."""
    cx, sx, cy, sy = math.cos(ax), math.sin(ax), math.cos(ay), math.sin(ay)
    return _mm([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]], [[1, 0, 0], [0, cx, -sx], [0, sx, cx]])

class Sup:
    """Superficie conica z = c r^2 / (1 + sqrt(1 - (1+k) c^2 r^2)); vertice V, rotacion local->global R.
    n: indice tras la superficie (refraccion); espejo=True: reflexion; plano de imagen/abertura si c=0."""
    def __init__(s, z, c=0.0, k=0.0, n=1.0, espejo=False, V=None, R=None, rmax=None, rmin=0.0):
        s.c, s.k, s.n, s.espejo = c, k, n, espejo
        s.V = V if V is not None else (0.0, 0.0, z)
        s.R = R if R is not None else [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        s.rmax, s.rmin = rmax, rmin

def mover(sup, dx=0.0, dy=0.0, dz=0.0):
    sup.V = (sup.V[0] + dx, sup.V[1] + dy, sup.V[2] + dz)

def girar(sup, ax, ay, pivote_z=None):
    """Gira la superficie ax (eje x) y ay (eje y) alrededor de un punto del eje (por defecto su vertice)."""
    R = _rot(ax, ay)
    if pivote_z is not None:
        P = (0.0, 0.0, pivote_z)
        d = (sup.V[0] - P[0], sup.V[1] - P[1], sup.V[2] - P[2])
        d = _mv(R, d)
        sup.V = (P[0] + d[0], P[1] + d[1], P[2] + d[2])
    sup.R = _mm(R, sup.R)

def _cruce(sup, O, D):
    Ol = _mtv(sup.R, (O[0] - sup.V[0], O[1] - sup.V[1], O[2] - sup.V[2]))
    Dl = _mtv(sup.R, D)
    c, k1 = sup.c, 1.0 + sup.k
    A = c * (Dl[0]**2 + Dl[1]**2 + k1 * Dl[2]**2)
    B = 2 * c * (Ol[0]*Dl[0] + Ol[1]*Dl[1] + k1 * Ol[2]*Dl[2]) - 2 * Dl[2]
    C = c * (Ol[0]**2 + Ol[1]**2 + k1 * Ol[2]**2) - 2 * Ol[2]
    disc = B*B - 4*A*C
    if disc < 0:
        return None
    sq = math.sqrt(disc)
    cand = []
    if abs(A) < 1e-30:
        if B != 0:
            cand.append(-C / B)
    else:
        q = -0.5 * (B + math.copysign(sq, B if B != 0 else 1.0))
        cand.append(q / A)
        if q != 0:
            cand.append(C / q)
    if not cand:
        return None
    t = min(cand, key=lambda tt: abs(Ol[2] + tt * Dl[2]))
    Pl = (Ol[0] + t*Dl[0], Ol[1] + t*Dl[1], Ol[2] + t*Dl[2])
    Nl = (2*c*Pl[0], 2*c*Pl[1], 2*c*k1*Pl[2] - 2)
    nn = math.sqrt(Nl[0]**2 + Nl[1]**2 + Nl[2]**2)
    Nl = (Nl[0]/nn, Nl[1]/nn, Nl[2]/nn)
    P = _mv(sup.R, Pl)
    P = (P[0] + sup.V[0], P[1] + sup.V[1], P[2] + sup.V[2])
    return t, P, _mv(sup.R, Nl), math.hypot(Pl[0], Pl[1])

def trazar(sups, O, D, n0=1.0, rejilla=True):
    """Traza un rayo. Devuelve (O, D, opl, n_final) tras la ultima superficie, o None si falla/vineteo."""
    n = n0
    opl = 0.0
    for s in sups:
        r = _cruce(s, O, D)
        if r is None:
            return None
        t, P, N, rl = r
        if s.rmax is not None and (rl > s.rmax or rl < s.rmin):
            return None
        opl += n * t
        cs = D[0]*N[0] + D[1]*N[1] + D[2]*N[2]
        if cs > 0:
            N = (-N[0], -N[1], -N[2]); cs = -cs
        if s.espejo:
            D = (D[0] - 2*cs*N[0], D[1] - 2*cs*N[1], D[2] - 2*cs*N[2])
        else:
            mu = n / s.n
            kk = 1 - mu*mu*(1 - cs*cs)
            if kk < 0:
                return None
            g = -mu*cs - math.sqrt(kk)
            D = (mu*D[0] + g*N[0], mu*D[1] + g*N[1], mu*D[2] + g*N[2])
            n = s.n
        O = P
    return O, D, opl, n

def _norm(v):
    m = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return (v[0]/m, v[1]/m, v[2]/m)

def a_plano(O, D, zi):
    t = (zi - O[2]) / D[2]
    return (O[0] + t*D[0], O[1] + t*D[1], zi), t

def haz(ax, ay, x, y, z0):
    """Rayo de una onda plana de direccion (ax, ay) (radianes en x e y); (x, y) es la posicion en el plano de la onda."""
    D = (math.sin(ax), math.sin(ay) * math.cos(ax), math.cos(ax) * math.cos(ay))
    nn = math.sqrt(sum(d*d for d in D)); D = (D[0]/nn, D[1]/nn, D[2]/nn)
    e1 = (D[2], 0.0, -D[0]); m1 = math.hypot(e1[0], e1[2]); e1 = (e1[0]/m1, 0.0, e1[2]/m1)
    e2 = (D[1]*e1[2] - D[2]*e1[1], D[2]*e1[0] - D[0]*e1[2], D[0]*e1[1] - D[1]*e1[0])
    O = (x*e1[0] + y*e2[0], x*e1[1] + y*e2[1], z0 + x*e1[2] + y*e2[2])
    return O, D

def pupila(R, N, rmin=0.0):
    """Retícula cuadrada uniforme de N x N puntos dentro del anillo rmin..R (pesos iguales)."""
    pts = []
    for i in range(N):
        for j in range(N):
            x = -R + 2*R*(i + 0.5)/N
            y = -R + 2*R*(j + 0.5)/N
            if rmin <= math.hypot(x, y) <= R:
                pts.append((x, y))
    return pts

def resolver(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for cc in range(i, n + 1):
                M[r][cc] -= f * M[i][cc]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x

def ajuste_mc(filas, y):
    m = len(filas[0])
    AtA = [[sum(f[i]*f[j] for f in filas) for j in range(m)] for i in range(m)]
    Aty = [sum(f[i]*yy for f, yy in zip(filas, y)) for i in range(m)]
    return resolver(AtA, Aty)

def frente(sups, ax, ay, zi, pts, z0, lam, quitar=("pistón", "inclinación"), n0=1.0, placa=None):
    """Frente de onda (en ondas) respecto de la esfera de referencia centrada en el rayo principal sobre el plano zi.
    Devuelve (rms tras quitar terminos, lista de W en ondas, lista de (x,y) validos, punto de imagen)."""
    Oc, Dc = haz(ax, ay, 0.0, 0.0, z0)
    dsc = 0.0
    if placa is not None:
        dsc, gx, gy = placa(0.0, 0.0)
        Dc = _norm((Dc[0] + gx, Dc[1] + gy, Dc[2]))
    rc = trazar(sups, Oc, Dc, n0)
    if rc is None:
        return None
    Pc, tc = a_plano(rc[0], rc[1], zi)
    rho = tc
    oplc = rc[2] + dsc
    W, XY = [], []
    for (x, y) in pts:
        O, D = haz(ax, ay, x, y, z0)
        ds = 0.0
        if placa is not None:
            ds, gx, gy = placa(x, y)
            D = _norm((D[0] + gx, D[1] + gy, D[2]))
        r = trazar(sups, O, D, n0)
        if r is None:
            continue
        S, Dd, opl, nf = r
        opl += ds
        v = (S[0] - Pc[0], S[1] - Pc[1], S[2] - Pc[2])
        b = Dd[0]*v[0] + Dd[1]*v[1] + Dd[2]*v[2]
        cc = v[0]**2 + v[1]**2 + v[2]**2 - rho**2
        d2 = b*b - cc
        if d2 < 0:
            continue
        t1 = -b - math.sqrt(d2)
        # la esfera de referencia pasa por la ultima superficie del rayo principal (t1 = 0 para el)
        W.append((opl + nf * t1) / lam)
        XY.append((x, y))
    # referencia: rayo principal (t1 = 0)
    Wc = oplc / lam
    W = [w - Wc for w in W]
    R2 = max(x*x + y*y for x, y in XY)
    filas = []
    for x, y in XY:
        f = [1.0]
        if "inclinación" in quitar:
            f += [x, y]
        if "enfoque" in quitar:
            f += [x*x + y*y]
        filas.append(f)
    co = ajuste_mc(filas, W)
    res = [w - sum(c_ * f_ for c_, f_ in zip(co, f)) for w, f in zip(W, filas)]
    rms = math.sqrt(sum(r*r for r in res) / len(res))
    return rms, W, XY, Pc, res
# ---- fin del trazador ----


N_G = 1.5


def proyecciones(th, f=1.0):
    return dict(tan=f * math.tan(th), equi=f * th, estereo=2 * f * math.tan(th / 2), equisolida=2 * f * math.sin(th / 2), orto=f * math.sin(th))


def lente():
    return [Sup(0.0, c=1.0 / 100.0, n=N_G), Sup(4.0, c=-1.0 / 100.0, n=1.0)]


def altura_principal(th, s, z_img):
    Dx, Dz = math.sin(th), math.cos(th)
    O = (-s * math.tan(th) * 0.0, 0.0, -s)  # el rayo principal pasa por el centro del diafragma (0, 0, -s)
    r = trazar(lente(), O, (Dx, 0.0, Dz))
    P, _ = a_plano(r[0], r[1], z_img)
    return P[0]


def distorsion_lente(s):
    f_ana = 1.0 / ((N_G - 1.0) * (2.0 / 100.0 - (N_G - 1.0) * 4.0 / (N_G * 100.0 * 100.0)))
    O, D = (1e-4, 0.0, -50.0), (0.0, 0.0, 1.0)
    O1, D1, _, _ = trazar(lente(), O, D)
    z_img = O1[2] + (-O1[0] / D1[0]) * D1[2]
    filas = []
    for g in (2.0, 4.0, 6.0, 8.0, 10.0):
        th = math.radians(g)
        h = altura_principal(th, s, z_img)
        ideal = f_ana * math.tan(th)
        filas.append((g, h, ideal, (h - ideal) / ideal))
    # ajuste Delta r / r = k1 r^2 con la altura h como r
    A = [[h * h] for g, h, i, d in filas]
    y = [d for g, h, i, d in filas]
    k1 = sum(a[0] * yy for a, yy in zip(A, y)) / sum(a[0] ** 2 for a in A)
    return f_ana, z_img, filas, k1


def calcular():
    th = math.radians(10.0)
    proy = proyecciones(th)
    ident = abs(proy["estereo"] - 2 * math.tan(th / 2)) + abs(math.tan(th) - 2 * math.tan(th / 2) / (1 - math.tan(th / 2) ** 2))
    lentes = {s: distorsion_lente(s) for s in (0.0, 40.0, 80.0)}
    # calibracion
    rng = random.Random(20261109)
    k1v, k2v, sig = -4e-5, 3e-8, 0.005
    pts = []
    for i in range(-5, 6):
        for j in range(-5, 6):
            x, y = 3.0 * i, 3.0 * j
            r = math.hypot(x, y)
            if r == 0:
                continue
            f = 1 + k1v * r * r + k2v * r**4
            pts.append((x, y, x * f + rng.gauss(0, sig), y * f + rng.gauss(0, sig)))
    # ajuste lineal: (xd - x, yd - y) = (k1 r^2 + k2 r^4) (x, y)
    filas, yy = [], []
    for x, y, xd, yd in pts:
        r2 = x * x + y * y
        filas.append([x * r2, x * r2 * r2]); yy.append(xd - x)
        filas.append([y * r2, y * r2 * r2]); yy.append(yd - y)
    k1, k2 = ajuste_mc(filas, yy)
    AtA = [[sum(f[i] * f[j] for f in filas) for j in range(2)] for i in range(2)]
    det = AtA[0][0] * AtA[1][1] - AtA[0][1] ** 2
    cov = [[AtA[1][1] / det, -AtA[0][1] / det], [-AtA[0][1] / det, AtA[0][0] / det]]
    s1, s2 = sig * math.sqrt(cov[0][0]), sig * math.sqrt(cov[1][1])
    res = []
    for x, y, xd, yd in pts:
        r2 = x * x + y * y
        f = 1 + k1 * r2 + k2 * r2 * r2
        res.append(xd - x * f); res.append(yd - y * f)
    rms = math.sqrt(sum(e * e for e in res) / len(res))
    # inversa por punto fijo para un punto de la esquina
    x0, y0 = 15.0, 15.0
    f0 = 1 + k1 * (x0 * x0 + y0 * y0) + k2 * (x0 * x0 + y0 * y0) ** 2
    xd, yd = x0 * f0, y0 * f0
    xu, yu = xd, yd
    for _ in range(60):
        r2 = xu * xu + yu * yu
        f = 1 + k1 * r2 + k2 * r2 * r2
        xu, yu = xd / f, yd / f
    err_inv = math.hypot(xu - x0, yu - y0)
    desplaz = math.hypot(xd - x0, yd - y0)
    return dict(proy=proy, ident=ident, lentes=lentes, k=(k1, k2), s=(s1, s2), verdad=(k1v, k2v), rms=rms, sig=sig, err_inv=err_inv, desplaz=desplaz, n=len(pts))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("A. Proyecciones (r / f) para un campo de 10 grados")
    for k, v in r["proy"].items():
        print(f"  {k:>10}: {v:.6f}  ({100 * (v / r['proy']['tan'] - 1):+.3f} % respecto de la tangente)")
    print(f"  Identidad tan(theta) = 2 t / (1 - t^2), t = tan(theta/2): diferencia = {r['ident']:.1e}")
    print("B. Distorsion del rayo principal de la lente trazada (lente biconvexa), segun la posicion del diafragma")
    for s, (f_ana, z_img, filas, k1) in r["lentes"].items():
        print(f"  Diafragma a {s:.0f} mm ante la lente (f = {f_ana:.3f} mm, plano de imagen z = {z_img:.3f} mm): k1 ajustado = {k1:.3e} mm^-2")
        for g, h, ideal, d in filas:
            print(f"    campo {g:4.1f} grados: h = {h:9.5f} mm ; f tan = {ideal:9.5f} mm ; distorsion = {100 * d:+.4f} %")
    print(f"C. Calibracion con {r['n']} estrellas (ruido {r['sig']} mm)")
    print(f"  k1 = {r['k'][0]:.4e} +- {r['s'][0]:.1e} (verdad {r['verdad'][0]:.1e}) ; k2 = {r['k'][1]:.4e} +- {r['s'][1]:.1e} (verdad {r['verdad'][1]:.1e})")
    print(f"  Residuo RMS = {r['rms']:.5f} mm (ruido {r['sig']} mm)")
    print(f"  Esquina (15, 15) mm: desplazamiento por la distorsion = {r['desplaz']:.4f} mm ; error de la inversa = {r['err_inv']:.1e} mm")
    assert r["ident"] < 1e-12
    assert abs(r["k"][0] - r["verdad"][0]) < 3 * r["s"][0] and abs(r["k"][1] - r["verdad"][1]) < 3 * r["s"][1]
    assert abs(r["rms"] / r["sig"] - 1.0) < 0.1
    assert r["err_inv"] < 1e-9
    k_s = [v[3] for v in r["lentes"].values()]
    assert abs(k_s[0]) < abs(k_s[2])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
