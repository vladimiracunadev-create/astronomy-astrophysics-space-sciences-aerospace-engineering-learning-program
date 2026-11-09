#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C04: telecentricidad (angulo del rayo principal) y vineteo geometrico por dos aperturas.

Datos: ninguna constante fisica consultada. La lente (biconvexa, n = 1.5, radios de 100 mm, espesor de 4 mm) y las aperturas (50 mm y 55 mm de radio, separadas 300 mm) son ILUSTRATIVAS (sinteticas).
Modelo: (1) trazador exacto: angulo de salida del rayo principal frente a la posicion del diafragma; el diafragma telecentrico esta en el foco objeto, que se halla por una segunda via
(rayo paralelo trazado desde la imagen en sentido inverso); caso analitico de lente delgada u' = theta (1 - s/f). (2) Fraccion no vineteada = area de interseccion de dos circulos (formula
analitica) frente a Monte Carlo con semilla 20261109.
Supuestos: aproximacion geometrica, campo pequeno en (1); sin transmitancia ni cos^4. Validez: ilustrativa.
Tolerancia: foco objeto por las dos vias < 1e-3 mm; fraccion analitica frente a Monte Carlo < 0.004.
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


def lente():
    return [Sup(0.0, c=1.0 / 100.0, n=N_G), Sup(4.0, c=-1.0 / 100.0, n=1.0)]


def angulo_salida(zs, theta=1e-5):
    """Angulo del rayo principal (que pasa por el centro del diafragma en z = zs) en el espacio imagen."""
    O = (0.0, 0.0, zs)
    D = (math.sin(theta), 0.0, math.cos(theta))
    r = trazar(lente(), O, D)
    return math.atan2(r[1][0], r[1][2])


def foco_objeto():
    sups = lente()[::-1]
    sups = [Sup(4.0, c=-1.0 / 100.0, n=N_G), Sup(0.0, c=1.0 / 100.0, n=1.0)]
    O = (1e-4, 0.0, 50.0)
    D = (0.0, 0.0, -1.0)
    O1, D1, _, _ = trazar(sups, O, D)
    t = -O1[0] / D1[0]
    return O1[2] + t * D1[2]


def foco_imagen():
    O, D = (1e-4, 0.0, -50.0), (0.0, 0.0, 1.0)
    O1, D1, _, _ = trazar(lente(), O, D)
    t = -O1[0] / D1[0]
    return O1[2] + t * D1[2]


def area_interseccion(r1, r2, d):
    if d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a = r1 * r1 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    b = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    c = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    return a + b - c


def calcular():
    zF = foco_objeto()
    zFi = foco_imagen()
    f_ana = 1.0 / ((N_G - 1.0) * (2.0 / 100.0 - (N_G - 1.0) * 4.0 / (N_G * 100.0 * 100.0)))
    # bisectriz: posicion del diafragma que anula el angulo de salida
    lo, hi = zF - 20.0, zF + 20.0
    flo, fhi = angulo_salida(lo), angulo_salida(hi)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fm = angulo_salida(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    z_tel = 0.5 * (lo + hi)
    tabla = []
    for dz in (-60.0, -30.0, 0.0, 30.0, 60.0):
        zs = z_tel + dz
        tabla.append((dz, angulo_salida(zs, 0.01) * 1000.0, angulo_salida(zs, 0.01) / 0.01))
    # lente delgada ideal: u' = theta (1 - s/f)
    # vineteo
    R, b, d = 50.0, 55.0, 300.0
    rng = random.Random(20261109)
    N = 200000
    filas = []
    for th in (0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35):
        desplaz = d * th
        a = area_interseccion(R, b, desplaz) / (math.pi * R * R)
        pasa = 0
        for _ in range(N):
            r = R * math.sqrt(rng.random())
            ph = 2 * math.pi * rng.random()
            x, y = r * math.cos(ph), r * math.sin(ph)
            if math.hypot(x + desplaz, y) <= b:
                pasa += 1
        filas.append((th, desplaz, a, pasa / N))
    return dict(zF=zF, z_tel=z_tel, tabla=tabla, filas=filas, zFi=zFi, f_ana=f_ana)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Foco objeto por el trazado inverso: z = {r['zF']:.5f} mm ; foco imagen: z = {r['zFi']:.5f} mm")
    print(f"Diafragma telecentrico por biseccion (angulo de salida nulo): z = {r['z_tel']:.5f} mm ; diferencia = {abs(r['z_tel'] - r['zF']):.2e} mm")
    print(f"{'z diafragma - z telec. [mm]':>28} {'angulo de salida [mrad por 0.01 rad]':>40} {'cociente':>10}")
    for dz, mr, q in r["tabla"]:
        print(f"{dz:28.1f} {mr:40.5f} {q:10.4f}")
    print(f"Focal paraxial analitica de la lente gruesa = {r['f_ana']:.4f} mm ; 60 / f = {60.0 / r['f_ana']:.4f}")
    print("Vineteo por dos aperturas (R = 50 mm, b = 55 mm, d = 300 mm)")
    print(f"{'campo [rad]':>11} {'desplaz. [mm]':>14} {'analitica':>10} {'Monte Carlo':>12}")
    for th, ds, a, mc in r["filas"]:
        print(f"{th:11.2f} {ds:14.2f} {a:10.4f} {mc:12.4f}")
    assert abs(r["z_tel"] - r["zF"]) < 1e-3
    assert abs(r["tabla"][2][2]) < 5e-4
    assert abs(r["tabla"][4][2] - 60.0 / r["f_ana"]) < 2e-3
    assert r["tabla"][0][2] * r["tabla"][4][2] < 0
    for th, ds, a, mc in r["filas"]:
        assert abs(a - mc) < 0.004
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
