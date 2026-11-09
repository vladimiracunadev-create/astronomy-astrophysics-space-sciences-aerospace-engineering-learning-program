#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C01: trazado exacto de rayos y aberracion esferica de orden superior en una lente simple.

Datos: ninguna constante fisica consultada. La lente (biconvexa, n = 1.5, radios de 100 mm, espesor de 5 mm) y la longitud de onda de 550 nm son ILUSTRATIVAS (sinteticas);
no se modela ninguna lente real.
Modelo: trazador 3D exacto (ley de Snell vectorial) para superficies conicas; aberracion esferica longitudinal LSA(h) de una superficie esferica unica contrastada con la solucion cerrada
meridional; en la lente, ajuste LSA = a h^2 + b h^4 y fraccion de orden superior; cociente de RMS de frente de onda (foco paraxial / mejor foco), que para W040 puro vale 4 exacto.
Supuestos: luz monocromatica, indice constante, objeto en el infinito sobre el eje. Validez: ilustrativa, no sustituye a un programa de diseno.
Tolerancia: trazador frente a solucion cerrada < 1e-9 mm; cociente de RMS = 4 con 3 % para una apertura pequena.
"""
from __future__ import annotations
import math, platform

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


LAM = 550e-6  # mm


def lsa_cerrada(R, n, h):
    """Cruce con el eje de un rayo paralelo de altura h en una superficie esferica (centro en +R), solucion meridional."""
    s_i = h / R
    i = math.asin(s_i)
    ip = math.asin(s_i / n)
    zs = R - R * math.cos(i)
    return zs + h / math.tan(i - ip)


def cruce_eje(R, n, h):
    s = Sup(0.0, c=1.0 / R, n=n)
    O, D = haz(0.0, 0.0, h, 0.0, -10.0)
    O1, D1, _, _ = trazar([s], O, D)
    t = -O1[0] / D1[0]
    return O1[2] + t * D1[2]


def calcular():
    R, n = 50.0, 1.5
    f_par = lsa_cerrada(R, n, 1e-6)
    filas = []
    err = 0.0
    for h in (2.0, 4.0, 6.0, 8.0, 10.0):
        zc = lsa_cerrada(R, n, h)
        zt = cruce_eje(R, n, h)
        err = max(err, abs(zc - zt))
        filas.append((h, zc, zt, zc - f_par))
    # lente biconvexa
    r1, r2, tc = 100.0, -100.0, 5.0
    lente = [Sup(0.0, c=1 / r1, n=n), Sup(tc, c=1 / r2, n=1.0)]
    def cruce_lente(h):
        O, D = haz(0.0, 0.0, h, 0.0, -10.0)
        O1, D1, _, _ = trazar(lente, O, D)
        t = -O1[0] / D1[0]
        return O1[2] + t * D1[2]
    zp = cruce_lente(1e-4)
    hs = [1.0 + 1.0 * k for k in range(0, 18)]  # 1..18 mm
    lsa = [cruce_lente(h) - zp for h in hs]
    # ajuste LSA = a h^2 + b h^4
    a, b = ajuste_mc([[h**2, h**4] for h in hs], lsa)
    h_max = hs[-1]
    frac4 = b * h_max**4 / (a * h_max**2 + b * h_max**4)
    # frente de onda en el foco paraxial y en el mejor foco (apertura pequena y grande)
    res = {}
    for nombre, Ra in (("pequena", 3.0), ("grande", 18.0)):
        pts = pupila(Ra, 41)
        r_par = frente(lente, 0.0, 0.0, zp, pts, -10.0, LAM, quitar=("pistón", "inclinación"))[0]
        r_mej = frente(lente, 0.0, 0.0, zp, pts, -10.0, LAM, quitar=("pistón", "inclinación", "enfoque"))[0]
        res[nombre] = (Ra, r_par, r_mej, r_par / r_mej)
    return dict(f_par=f_par, filas=filas, err=err, zp=zp, a=a, b=b, h_max=h_max, frac4=frac4, lsa_max=lsa[-1], res=res)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Superficie unica R = 50 mm, n = 1.5: cruce paraxial = {r['f_par']:.6f} mm")
    print(f"{'h [mm]':>7} {'cruce cerrado [mm]':>19} {'cruce trazado [mm]':>19} {'LSA [mm]':>10}")
    for h, zc, zt, l in r["filas"]:
        print(f"{h:7.1f} {zc:19.9f} {zt:19.9f} {l:10.5f}")
    print(f"Diferencia maxima trazado - cerrada = {r['err']:.2e} mm")
    print(f"Lente biconvexa: foco paraxial z = {r['zp']:.4f} mm")
    print(f"Ajuste LSA = a h^2 + b h^4: a = {r['a']:.6e} mm^-1 ; b = {r['b']:.6e} mm^-3")
    print(f"Con h = {r['h_max']:.1f} mm: LSA = {r['lsa_max']:.4f} mm ; fraccion de orden h^4 = {r['frac4']:.4f}")
    for nombre, (Ra, rp, rm, q) in r["res"].items():
        print(f"Apertura {nombre} (radio {Ra:.1f} mm): RMS foco paraxial = {rp:.4f} ondas ; mejor foco = {rm:.4f} ondas ; cociente = {q:.3f}")
    assert r["err"] < 1e-9
    assert abs(r["res"]["pequena"][3] - 4.0) < 0.12
    assert abs(r["res"]["grande"][3] - 4.0) > abs(r["res"]["pequena"][3] - 4.0)
    assert r["b"] != 0 and r["frac4"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
