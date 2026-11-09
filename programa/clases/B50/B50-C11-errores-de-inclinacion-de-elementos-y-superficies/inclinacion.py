#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C11: inclinacion de espejos (espejo plano a 2 alpha) y punto de pivote libre de coma del secundario de un Cassegrain.

Datos: ninguna constante fisica consultada. El Cassegrain (primario parabolico de 400 mm y f/2, focal final de 4000 mm, obstruccion de 45 mm de radio), la inclinacion de 0.5 mrad y la longitud de
onda de 550 nm son ILUSTRATIVOS (sinteticos); no se modela ningun telescopio real.
Modelo: (1) espejo plano inclinado alpha: el rayo reflejado gira 2 alpha (exacto). (2) Inclinacion del secundario alrededor de un punto del eje: equivale a inclinar alrededor del vertice y descentrar
el vertice delta = alpha (z_V - z_P). Coeficiente de coma firmado c = coeficiente de x (x^2 + y^2) del ajuste del frente de onda (ondas por mm^3 de pupila). El pivote libre de coma se halla de dos formas:
barrido con secante sobre el trazado y prediccion lineal a partir de la coma por inclinacion en el vertice y por descentramiento.
Supuestos: luz monocromatica sobre el eje, inclinaciones pequenas. Validez: ilustrativa.
Tolerancia: 2 alpha a 1e-12; pivote por las dos vias dentro de 0.5 mm; el RMS en el pivote libre de coma es menos de un decimo del RMS con pivote en el vertice.
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
ZV = -D_SEC
ALFA = 5e-4


def sistema(dx_sec=0.0, alfa=0.0, pivote=None):
    p = Sup(0.0, c=-1.0 / (2 * F1), k=-1.0, espejo=True)
    s = Sup(ZV, c=-1.0 / R2, k=K2, espejo=True)
    if alfa:
        girar(s, 0.0, alfa, pivote_z=pivote)
    mover(s, dx=dx_sec)
    return [p, s]


def metricas(sups):
    rms, W, XY, Pc, res = frente(sups, 0.0, 0.0, B, PTS, -900.0, LAM, quitar=("pistón", "inclinación", "enfoque"))
    filas = []
    sc = 200.0
    for (x, y) in XY:
        x, y = x / sc, y / sc
        filas.append([1.0, x, y, x * x + y * y, x * (x * x + y * y), y * (x * x + y * y)])
    co = ajuste_mc(filas, W)
    return rms, co[4], Pc[0]


def deflexion_plano(alfa):
    s = Sup(0.0, c=0.0, espejo=True)
    girar(s, 0.0, alfa)
    O, D = (0.0, 0.0, -10.0), (0.0, 0.0, 1.0)
    r = trazar([s], O, D)
    return math.atan2(r[1][0], -r[1][2]) if r[1][2] < 0 else math.atan2(r[1][0], r[1][2])


def calcular():
    defl = []
    for a in (1e-4, 1e-3, 1e-2):
        d = deflexion_plano(a)
        defl.append((a, d, abs(d) - 2 * a))
    # coma por descentramiento (ondas por mm de descentramiento, firmada)
    r_d, c_d, _ = metricas(sistema(dx_sec=0.1))
    c_por_mm = c_d / 0.1
    # inclinacion en el vertice
    r_v, c_v, x_v = metricas(sistema(alfa=ALFA, pivote=None))
    # pivotes
    zc_curv = ZV + (-R2)
    tabla = []
    for zp in (ZV, ZV - 200.0, zc_curv, ZV + 200.0, 0.0):
        r_p, c_p, x_p = metricas(sistema(alfa=ALFA, pivote=zp))
        tabla.append((zp, c_p, r_p, x_p))
    # secante para el pivote libre de coma
    def coef(zp):
        return metricas(sistema(alfa=ALFA, pivote=zp))[1]
    z0, z1 = ZV, ZV + 300.0
    f0, f1 = coef(z0), coef(z1)
    for _ in range(8):
        z2 = z1 - f1 * (z1 - z0) / (f1 - f0)
        z0, f0, z1, f1 = z1, f1, z2, coef(z2)
    z_sec = z1
    # prediccion lineal: delta = alfa (zV - zP), coma = c_v + delta * c_por_mm = 0
    # el signo de delta se toma del trazado (se contrasta con la secante)
    z_pred = ZV - (-c_v / c_por_mm) / ALFA
    r_lib, c_lib, _ = metricas(sistema(alfa=ALFA, pivote=z_sec))
    return dict(defl=defl, c_por_mm=c_por_mm, r_v=r_v, c_v=c_v, tabla=tabla, z_sec=z_sec, z_pred=z_pred, r_lib=r_lib, c_lib=c_lib)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Espejo plano inclinado: giro del rayo reflejado")
    for a, d, e in r["defl"]:
        print(f"  alpha = {a:.0e} rad ; giro = {abs(d):.12f} rad ; 2 alpha = {2 * a:.12f} ; diferencia = {e:.1e}")
    print(f"Coma por descentramiento del secundario: {r['c_por_mm']:.4f} ondas por mm de descentramiento (coeficiente de x r^2, pupila normalizada)")
    print(f"Inclinacion alpha = {ALFA} rad del secundario alrededor de su vertice (z = {ZV:.2f} mm): RMS = {r['r_v']:.5f} ondas ; coeficiente de coma = {r['c_v']:.5f}")
    print(f"{'pivote z [mm]':>14} {'coef. coma':>11} {'RMS [ondas]':>12} {'desplaz. imagen [mm]':>21}")
    for zp, c, rr, xp in r["tabla"]:
        print(f"{zp:14.2f} {c:11.5f} {rr:12.5f} {xp:21.4f}")
    print(f"Pivote libre de coma: secante sobre el trazado z = {r['z_sec']:.3f} mm ; prediccion lineal z = {r['z_pred']:.3f} mm")
    print(f"En el pivote libre de coma: coeficiente = {r['c_lib']:.2e} ; RMS = {r['r_lib']:.5f} ondas (vertice: {r['r_v']:.5f})")
    for a, d, e in r["defl"]:
        assert abs(e) < 1e-12
    assert abs(r["z_sec"] - r["z_pred"]) < 0.5
    assert r["r_lib"] < r["r_v"] / 10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
