#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C10: efecto del descentramiento del espejo secundario en un Cassegrain clasico (coma por descentramiento).

Datos: ninguna constante fisica consultada. El telescopio (primario parabolico de 400 mm de diametro y f/2, focal final de 4000 mm, secundario hiperbolico, obstruccion central de 45 mm de radio)
y la longitud de onda de 550 nm son ILUSTRATIVOS (sinteticos); no se modela ningun telescopio real.
Modelo: trazador exacto 3D; el secundario se desplaza lateralmente d; RMS del frente de onda en el eje (tras quitar pistón, inclinacion y enfoque) en funcion de d. Dos pruebas analiticas:
(1) la respuesta es lineal en d (coma) y simetrica en +-d; (2) un desplazamiento rigido de todo el telescopio no cambia nada (solo importa el descentramiento relativo).
Supuestos: luz monocromatica sobre el eje, sin otras tolerancias. Validez: ilustrativa.
Tolerancia: cociente RMS/d constante a 2 % entre 0.02 y 0.2 mm; simetria a 1e-9 relativo; invariancia al desplazamiento rigido a 1e-6 ondas.
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


LAM = 550e-6
F1, M, B = 800.0, 5.0, 200.0
D_SEC = (M * F1 - B) / (M + 1)
S0 = F1 - D_SEC
R2 = 2 * M * S0 / (M - 1)
K2 = -((M + 1) / (M - 1)) ** 2
PTS = pupila(200.0, 41, rmin=45.0)


def sistema(dx_sec=0.0, dx_total=0.0):
    p = Sup(0.0, c=-1.0 / (2 * F1), k=-1.0, espejo=True)
    s = Sup(-D_SEC, c=-1.0 / R2, k=K2, espejo=True)
    mover(s, dx=dx_sec)
    mover(p, dx=dx_total)
    mover(s, dx=dx_total)
    return [p, s]


def rms(dx_sec=0.0, campo=0.0, dx_total=0.0, quitar=("pistón", "inclinación", "enfoque")):
    pts = [(x + dx_total, y) for x, y in PTS] if dx_total else PTS
    # el desplazamiento rigido mueve tambien la onda plana: la pupila se muestrea alrededor del primario desplazado
    sups = sistema(dx_sec, dx_total)
    return frente(sups, math.radians(campo), 0.0, B, pts, -900.0, LAM, quitar=quitar)[0]


def calcular():
    ds = [0.02, 0.05, 0.1, 0.2, 0.5]
    filas = []
    for d in ds:
        a = rms(d)
        b = rms(-d)
        filas.append((d, a, b, a / d))
    nominal = rms(0.0)
    pendiente = filas[0][3]
    d_tol = 0.05 / pendiente
    rms_tol = rms(d_tol)
    inv = abs(rms(0.1, dx_total=7.0) - rms(0.1))
    # sin quitar el enfoque
    sin_enf = rms(0.2, quitar=("pistón", "inclinación"))
    # equivalente de campo: angulo del campo en el sistema nominal con el mismo RMS
    c_eq = None
    lo, hi = 0.0, 0.5
    objetivo = rms(0.1)
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if rms(0.0, campo=mid) < objetivo:
            lo = mid
        else:
            hi = mid
    c_eq = 0.5 * (lo + hi)
    return dict(filas=filas, nominal=nominal, pendiente=pendiente, d_tol=d_tol, rms_tol=rms_tol, inv=inv, sin_enf=sin_enf, c_eq=c_eq)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cassegrain clasico: d = {D_SEC:.3f} mm ; R2 = {R2:.3f} mm ; k2 = {K2:.3f} ; RMS nominal en el eje = {r['nominal']:.2e} ondas")
    print(f"{'d [mm]':>7} {'RMS(+d)':>9} {'RMS(-d)':>9} {'RMS/d [ondas/mm]':>17}")
    for d, a, b, q in r["filas"]:
        print(f"{d:7.2f} {a:9.5f} {b:9.5f} {q:17.4f}")
    print(f"Tolerancia de descentramiento para 0.05 ondas RMS (lineal) = {r['d_tol']:.4f} mm ; RMS trazado a ese valor = {r['rms_tol']:.5f} ondas")
    print(f"Desplazamiento rigido de todo el telescopio 7 mm: cambio del RMS = {r['inv']:.1e} ondas")
    print(f"Con d = 0.2 mm sin quitar el enfoque: RMS = {r['sin_enf']:.5f} ondas")
    print(f"Campo equivalente del sistema nominal con el mismo RMS que d = 0.1 mm: {r['c_eq']:.5f} grados")
    for d, a, b, q in r["filas"]:
        assert abs(a - b) / a < 1e-9
    qs = [f[3] for f in r["filas"][:4]]
    assert max(qs) / min(qs) - 1.0 < 0.02
    assert r["inv"] < 1e-6
    assert abs(r["rms_tol"] / 0.05 - 1.0) < 0.03
    assert r["nominal"] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
