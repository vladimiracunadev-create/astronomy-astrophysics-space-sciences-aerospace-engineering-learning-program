#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C13: analisis Monte Carlo de tolerancias de un Cassegrain clasico (distribucion del RMS del frente de onda y rendimiento).

Datos: ninguna constante fisica consultada. El telescopio (primario parabolico de 400 mm y f/2, focal final de 4000 mm, obstruccion de 45 mm de radio), las tolerancias (uniformes +-) y la
longitud de onda de 550 nm son ILUSTRATIVOS (sinteticos); no se modela ningun telescopio real.
Modelo: cinco errores independientes y uniformes (descentramientos x e y del secundario, inclinacion del secundario, error de espaciado y error de conica del primario). Se calcula con el trazador
exacto el vector de frente de onda por unidad de cada error (diferencias centrales) y la matriz de Gram G; la media de W^2 es suma sigma_i^2 G_ii (los terminos cruzados se anulan en media).
Monte Carlo con semilla 20261109: 600 sistemas trazados con todos los errores a la vez; se compara (1) cada W^2 trazado con la superposicion lineal, (2) la media de W^2 con la prediccion (en errores
tipicos de la media) y (3) el rendimiento P(RMS <= 0.04 ondas) con el del modelo lineal con 200 000 ensayos.
Supuestos: errores independientes, de media cero, sin otras tolerancias; se quitan pistón, inclinacion y enfoque (compensables). Validez: ilustrativa.
Tolerancia: superposicion lineal a 3 %; media de W^2 dentro de 3 errores tipicos; rendimiento dentro de 3 errores binomiales.
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


LAM = 550e-6
F1, M, B = 800.0, 5.0, 200.0
D_SEC = (M * F1 - B) / (M + 1)
S0 = F1 - D_SEC
R2 = 2 * M * S0 / (M - 1)
K2 = -((M + 1) / (M - 1)) ** 2
PTS = pupila(200.0, 21, rmin=45.0)
NOMBRES = ["descentramiento x del secundario [mm]", "descentramiento y del secundario [mm]", "inclinacion del secundario [rad]", "espaciado del secundario [mm]", "error de conica del primario"]
TOL = [0.03, 0.03, 3e-4, 0.05, 0.002]   # semiancho de la distribucion uniforme (ilustrativo)
H = [0.01, 0.01, 1e-4, 0.02, 1e-3]
OBJ = 0.04


def sistema(p):
    dx, dy, tilt, dz, dk = p
    pr = Sup(0.0, c=-1.0 / (2 * F1), k=-1.0 + dk, espejo=True)
    s = Sup(-D_SEC, c=-1.0 / R2, k=K2, espejo=True)
    if tilt:
        girar(s, 0.0, tilt)
    mover(s, dx=dx, dy=dy, dz=dz)
    return [pr, s]


def vec(p):
    r = frente(sistema(p), 0.0, 0.0, B, PTS, -900.0, LAM, quitar=("pistón", "inclinación", "enfoque"))
    return r[0], r[4]


def calcular():
    n = len(NOMBRES)
    w = []
    for i in range(n):
        pp, pm = [0.0] * n, [0.0] * n
        pp[i], pm[i] = H[i], -H[i]
        a, b = vec(pp)[1], vec(pm)[1]
        w.append([(x - y) / (2 * H[i]) for x, y in zip(a, b)])
    m = len(w[0])
    G = [[sum(a * b for a, b in zip(w[i], w[j])) / m for j in range(n)] for i in range(n)]
    contrib = [(TOL[i] ** 2 / 3.0) * G[i][i] for i in range(n)]
    pred_w2 = sum(contrib)
    rng = random.Random(20261109)
    N = 600
    w2_traza, w2_lin = [], []
    for _ in range(N):
        p = [rng.uniform(-t, t) for t in TOL]
        rms, _res = vec(p)
        w2_traza.append(rms * rms)
        w2_lin.append(sum(p[i] * p[j] * G[i][j] for i in range(n) for j in range(n)))
    dev = max(abs(a - b) / max(b, 1e-12) for a, b in zip(w2_traza, w2_lin) if b > 0.1 * pred_w2)
    media = sum(w2_traza) / N
    var = sum((x - media) ** 2 for x in w2_traza) / (N - 1)
    se = math.sqrt(var / N)
    rend_mc = sum(1 for x in w2_traza if math.sqrt(x) <= OBJ) / N
    # modelo lineal con muchos ensayos
    L = 200000
    ok = 0
    for _ in range(L):
        p = [rng.uniform(-t, t) for t in TOL]
        if sum(p[i] * p[j] * G[i][j] for i in range(n) for j in range(n)) <= OBJ * OBJ:
            ok += 1
    rend_lin = ok / L
    se_b = math.sqrt(rend_lin * (1 - rend_lin) / N)
    srt = sorted(math.sqrt(x) for x in w2_traza)
    pct = [srt[int(q * (N - 1))] for q in (0.05, 0.5, 0.95, 0.99)]
    return dict(G=G, contrib=contrib, pred=pred_w2, media=media, se=se, dev=dev, rend_mc=rend_mc, rend_lin=rend_lin, se_b=se_b, pct=pct, N=N)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'error':>40} {'tolerancia +-':>14} {'ondas por unidad':>15} {'aporte a W^2':>13}")
    for nm, t, g, c in zip(NOMBRES, TOL, [r['G'][i][i] for i in range(5)], r["contrib"]):
        print(f"{nm:>40} {t:14.4g} {math.sqrt(g):15.4g} {c:13.3e}")
    print(f"Prediccion: media de W^2 = {r['pred']:.4e} ondas^2 (RMS tipico {math.sqrt(r['pred']):.5f})")
    print(f"Monte Carlo ({r['N']} sistemas): media de W^2 = {r['media']:.4e} +- {r['se']:.1e} ; diferencia = {(r['media'] - r['pred']) / r['se']:+.2f} errores tipicos")
    print(f"Desviacion maxima del W^2 trazado frente a la superposicion lineal = {100 * r['dev']:.2f} %")
    print("Percentiles del RMS (5, 50, 95, 99 %): " + " ; ".join(f"{x:.5f}" for x in r["pct"]) + " ondas")
    print(f"Rendimiento P(RMS <= {OBJ} ondas): Monte Carlo trazado = {r['rend_mc']:.4f} ; modelo lineal (200 000) = {r['rend_lin']:.4f}")
    assert abs(r["media"] - r["pred"]) < 3 * r["se"]
    assert r["dev"] < 0.03
    assert abs(r["rend_mc"] - r["rend_lin"]) < 3 * r["se_b"] + 1e-9
    assert 0.3 < r["rend_lin"] < 0.99
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
