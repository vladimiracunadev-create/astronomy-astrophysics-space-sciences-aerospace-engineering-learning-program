#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C03: sistemas catadioptricos (placa de Schmidt y menisco concentrico tipo Maksutov) con un espejo esferico.

Datos: ninguna constante fisica consultada. El espejo (R = 2000 mm, abertura de 200 mm, f/5), el indice 1.5 del corrector y la longitud de onda de 550 nm son ILUSTRATIVOS (sinteticos);
no se modela ningun telescopio real.
Modelo: trazador exacto 3D. (1) Espejo esferico con el diafragma en el espejo y en el centro de curvatura: RMS de frente de onda (sin enfoque) frente al campo.
(2) Placa de Schmidt delgada modelada como perfil de espesor s(r) = a r^4 (+ b r^2) con desviacion -(n-1) grad s; a se obtiene por minimos cuadrados y se compara con la teoria de tercer orden
a = 1/(8 (n-1) R^2 f). (3) Menisco con superficies concentricas en el centro de curvatura (concavo hacia el cielo, radio frontal de 500 mm): barrido del espesor.
Supuestos: luz monocromatica, placa delgada sin dispersion, abanico completo de pupila. Validez: ilustrativa.
Tolerancia: coeficiente de la placa a 6 % de la teoria; reduccion del RMS en el eje > 20 veces; menisco con un minimo interior del barrido.
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
RM, ZM = -2000.0, 0.0
N_G = 1.5
RAD = 100.0


def rms_espejo(ax, z0, nq=("pistón", "inclinación", "enfoque"), placa=None, extra=None):
    s = [Sup(ZM, c=1.0 / RM, espejo=True)]
    if extra:
        s = extra + s
    pts = pupila(RAD, 33)
    r = frente(s, ax, 0.0, -1000.0, pts, z0, LAM, quitar=nq, placa=placa)
    return r[0]


def calcular():
    campos = [0.0, 0.5, 1.0, 2.0]
    A = {}
    for a in campos:
        ax = math.radians(a)
        A[a] = (rms_espejo(ax, -50.0), rms_espejo(ax, -2000.0))
    # placa de Schmidt: W(a,b) lineal; diferencias finitas sobre los mismos rayos
    def placa_fn(a, b):
        def f(x, y):
            r2 = x * x + y * y
            s = a * r2 * r2 + b * r2
            g = (N_G - 1.0) * (4 * a * r2 + 2 * b)
            return (N_G - 1.0) * s, -g * x, -g * y
        return f
    pts = pupila(RAD, 33)
    def W(a, b):
        r = frente([Sup(ZM, c=1.0 / RM, espejo=True)], 0.0, 0.0, -1000.0, pts, -2000.0, LAM, quitar=("pistón",), placa=placa_fn(a, b))
        return r[1], r[2]
    # los frentes con "inclinacion" removida: se trabaja con W sin ajuste de enfoque para estimar a por minimos cuadrados
    W0, XY = W(0.0, 0.0)
    da, db = 1e-11, 1e-8
    Wa = [(x - y) / da for x, y in zip(W(da, 0.0)[0], W0)]
    Wb = [(x - y) / db for x, y in zip(W(0.0, db)[0], W0)]
    # minimizar |W0 + a Wa + b Wb + c0 + c1 x + c2 y| con b=0 y a libre
    filas_a = [[wa, 1.0, x, y] for wa, (x, y) in zip(Wa, XY)]
    sol_a = ajuste_mc(filas_a, [-w for w in W0])
    a_fit = sol_a[0]
    a_teo = abs(1.0 / (8.0 * (N_G - 1.0) * RM**2 * (-RM / 2.0)))
    # con enfoque libre (b libre)
    filas_ab = [[wa, wb, 1.0, x, y] for wa, wb, (x, y) in zip(Wa, Wb, XY)]
    sol_ab = ajuste_mc(filas_ab, [-w for w in W0])
    rms_sin = frente([Sup(ZM, c=1.0 / RM, espejo=True)], 0.0, 0.0, -1000.0, pts, -2000.0, LAM, quitar=("pistón", "inclinación"))[0]
    rms_con = frente([Sup(ZM, c=1.0 / RM, espejo=True)], 0.0, 0.0, -1000.0, pts, -2000.0, LAM, quitar=("pistón", "inclinación"), placa=placa_fn(a_fit, 0.0))[0]
    rms_con_b = frente([Sup(ZM, c=1.0 / RM, espejo=True)], 0.0, 0.0, -1000.0, pts, -2000.0, LAM, quitar=("pistón", "inclinación", "enfoque"), placa=placa_fn(sol_ab[0], sol_ab[1]))[0]
    campo_placa = {}
    for a in (0.0, 1.0, 2.0):
        ax = math.radians(a)
        campo_placa[a] = frente([Sup(ZM, c=1.0 / RM, espejo=True)], ax, 0.0, -1000.0, pts, -2000.0, LAM, quitar=("pistón", "inclinación", "enfoque"), placa=placa_fn(sol_ab[0], sol_ab[1]))[0]
    # menisco concentrico en el centro de curvatura C (z = -2000), concavo hacia el cielo: vertices a rho1 y rho1 + t de C
    rho1 = 500.0
    def menisco(t):
        return [Sup(-2000.0 + rho1, c=-1.0 / rho1, n=N_G), Sup(-2000.0 + rho1 + t, c=-1.0 / (rho1 + t), n=1.0)] if t > 0 else []
    barrido = []
    for t in [0, 5, 10, 15, 20, 25, 30, 40, 50, 60]:
        rms = frente(menisco(t) + [Sup(ZM, c=1.0 / RM, espejo=True)], 0.0, 0.0, -1000.0, pts, -1600.0, LAM, quitar=("pistón", "inclinación", "enfoque"))[0]
        barrido.append((t, rms))
    tmin, rmin = min(barrido, key=lambda x: x[1])
    camp_men = {}
    for a in (0.0, 1.0, 2.0):
        camp_men[a] = frente(menisco(tmin) + [Sup(ZM, c=1.0 / RM, espejo=True)], math.radians(a), 0.0, -1000.0, pts, -1600.0, LAM, quitar=("pistón", "inclinación", "enfoque"))[0]
    return dict(A=A, a_fit=a_fit, a_teo=a_teo, ab=sol_ab[:2], rms_sin=rms_sin, rms_con=rms_con, rms_con_b=rms_con_b, campo_placa=campo_placa, barrido=barrido, tmin=tmin, rmin=rmin, camp_men=camp_men)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("RMS de frente de onda sin enfoque del espejo esferico (R = 2000 mm, f/5) [ondas de 550 nm]")
    print(f"{'campo [grados]':>14} {'diafragma en espejo':>20} {'diafragma en C':>16}")
    for a, (m, c) in r["A"].items():
        print(f"{a:14.1f} {m:20.4f} {c:16.4f}")
    print(f"Placa de Schmidt (b = 0): a ajustado = {r['a_fit']:.4e} mm^-3 ; teoria de tercer orden = {r['a_teo']:.4e} mm^-3 ; cociente = {r['a_fit'] / r['a_teo']:.4f}")
    print(f"RMS en el eje en el foco paraxial: sin placa = {r['rms_sin']:.3f} ondas ; con placa = {r['rms_con']:.4f} ondas")
    print(f"Placa con enfoque libre: a = {r['ab'][0]:.4e} ; b = {r['ab'][1]:.4e} ; RMS sin enfoque = {r['rms_con_b']:.5f} ondas")
    print("RMS con la placa optima segun el campo: " + " ; ".join(f"{a:.0f} grados = {v:.5f}" for a, v in r["campo_placa"].items()))
    print(f"{'espesor [mm]':>12} {'RMS [ondas]':>12}")
    for t, v in r["barrido"]:
        print(f"{t:12.0f} {v:12.4f}")
    print(f"Menisco: minimo en t = {r['tmin']} mm con RMS = {r['rmin']:.4f} ondas")
    print("RMS del menisco segun el campo: " + " ; ".join(f"{a:.0f} grados = {v:.4f}" for a, v in r["camp_men"].items()))
    assert r["A"][2.0][1] < r["A"][2.0][0] / 5
    assert abs(r["a_fit"] / r["a_teo"] - 1.0) < 0.06
    assert r["rms_con"] < r["rms_sin"] / 20
    assert 0 < r["tmin"] < 60 and r["rmin"] < r["barrido"][0][1] / 3
    assert r["camp_men"][2.0] < 2.0 * r["camp_men"][0.0] + 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
