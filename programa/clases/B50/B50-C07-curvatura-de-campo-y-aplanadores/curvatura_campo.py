#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C07: curvatura de campo (superficie de Petzval), astigmatismo de Coddington y aplanador de campo.

Datos: ninguna constante fisica consultada. El espejo esferico (R = 2000 mm, f = 1000 mm), el aplanador (plano-concavo, n = 1.5) y la tolerancia de foco de +-2 lambda N^2 con lambda = 550 nm
y N = 5 son ILUSTRATIVOS (sinteticos); no se modela ningun telescopio real.
Modelo: trazado exacto de haces estrechos; el foco de un haz es el punto que minimiza la distancia a todos sus rayos (minimos cuadrados). (A) Espejo esferico con el diafragma en el vertice:
focos tangencial y sagital a f cos(theta) y f / cos(theta) (formula de Coddington para espejos). (B) Diafragma en el centro de curvatura C: la superficie de enfoque es una esfera de radio f centrada
en C. (C) Un aplanador delgado de potencia phi = -n / f anula la suma de Petzval; se busca el valor optimo por barrido y se compara.
Supuestos: monocromatico, haz estrecho (radio 0.3 mm) para A y 30 mm para B y C. Validez: ilustrativa.
Tolerancia: focos de Coddington a 1e-3 relativo; radio de la superficie de enfoque a 1e-3 relativo (haz estrecho); aplanador optimo a 30 % del valor teorico.
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


RM = -2000.0
F = 1000.0
LAM = 550e-6


def foco_ls(rayos):
    """Punto que minimiza la suma de cuadrados de las distancias a los rayos (O, D)."""
    A = [[0.0] * 3 for _ in range(3)]
    b = [0.0] * 3
    for O, D in rayos:
        for i in range(3):
            for j in range(3):
                m = (1.0 if i == j else 0.0) - D[i] * D[j]
                A[i][j] += m
                b[i] += m * O[j]
    return resolver(A, b)


def haz_estrecho(th, base, eje, rad, sups):
    """Rayos de un abanico (eje = 'T' tangencial en x, 'S' sagital en y) de una onda plana de campo th que pasa por 'base'."""
    D = (math.sin(th), 0.0, math.cos(th))
    e1 = (math.cos(th), 0.0, -math.sin(th))
    e2 = (0.0, 1.0, 0.0)
    out = []
    for k in range(-4, 5):
        s = rad * k / 4.0
        e = e1 if eje == "T" else e2
        O = (base[0] + s * e[0], base[1] + s * e[1], base[2] + s * e[2])
        r = trazar(sups, O, D)
        out.append((r[0], r[1]))
    return out, D


def coddington(th):
    sups = [Sup(0.0, c=1.0 / RM, espejo=True)]
    base = (-50.0 * math.sin(th), 0.0, -50.0 * math.cos(th))  # el rayo principal pasa por el vertice
    res = {}
    for eje in ("T", "S"):
        rayos, D = haz_estrecho(th, base, eje, 0.3, sups)
        Dr = trazar(sups, base, D)[1]
        P = foco_ls(rayos)
        res[eje] = math.sqrt(P[0] ** 2 + P[1] ** 2 + P[2] ** 2)
    return res


def foco_en_C(th, rad=30.0, extra=None):
    sups = [Sup(0.0, c=1.0 / RM, espejo=True)]
    if extra:
        sups = extra + sups
    C = (0.0, 0.0, -2000.0)
    # rayos de un haz circular que pasa por C (pupila en C)
    D = (math.sin(th), 0.0, math.cos(th))
    e1 = (math.cos(th), 0.0, -math.sin(th))
    rayos = []
    for (x, y) in pupila(rad, 15):
        O = (C[0] + x * e1[0], C[1] + y, C[2] + x * e1[2])
        r = trazar(sups, O, D)
        if r is not None:
            rayos.append((r[0], r[1]))
    return foco_ls(rayos)


def sum_petzval_lente(phi_l, n_l):
    return phi_l / n_l


def calcular():
    cod = []
    for g in (5.0, 10.0, 20.0):
        th = math.radians(g)
        r = coddington(th)
        cod.append((g, r["T"], F * math.cos(th), r["S"], F / math.cos(th)))
    sup = []
    for g in (0.0, 0.5, 1.0, 2.0):
        th = math.radians(g)
        P = foco_en_C(th)
        d = math.sqrt(P[0] ** 2 + P[1] ** 2 + (P[2] + 2000.0) ** 2)
        sup.append((g, d, P[2]))
    # profundidad de foco y campo util con detector plano
    delta = 2 * LAM * 5.0 ** 2
    th_max = math.sqrt(2.0 * delta / F)
    # aplanador: lente plano-concava delgada a 20 mm antes del foco; barrido de la focal
    def sag_sin(g):
        return foco_en_C(math.radians(g))[2]
    z0 = foco_en_C(0.0)[2]
    dz_sin = foco_en_C(math.radians(1.0))[2] - z0
    barrido = []
    for fl in (-400.0, -600.0, -900.0, -1200.0, -1500.0, -2000.0, -3000.0, -5000.0):
        R2 = -(1.5 - 1.0) * fl  # radio de la cara de salida; la luz viaja hacia -z, por lo que la curvatura en z es -1/R2
        lente = [Sup(-977.0, c=0.0, n=1.5), Sup(-980.0, c=-1.0 / R2, n=1.0)]
        za = foco_en_C(0.0, extra=lente)[2]
        zb = foco_en_C(math.radians(1.0), extra=lente)[2]
        barrido.append((fl, zb - za))
    # interpolar el cero
    fl_opt = None
    for (f1, d1), (f2, d2) in zip(barrido, barrido[1:]):
        if d1 * d2 < 0:
            fl_opt = f1 + (f2 - f1) * d1 / (d1 - d2)
            break
    fl_teo = -1.5 * F
    return dict(cod=cod, sup=sup, delta=delta, th_max=th_max, dz_sin=dz_sin, barrido=barrido, fl_opt=fl_opt, fl_teo=-1.5 * F / 1.0 * 1.0, petz=(1.0 / F, sum_petzval_lente(-1.0 / F * 1.5, 1.5)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("A. Diafragma en el vertice: focos de Coddington del espejo esferico (distancia al vertice a lo largo del rayo principal)")
    print(f"{'campo [grados]':>14} {'T trazado [mm]':>15} {'f cos(th)':>10} {'S trazado [mm]':>15} {'f/cos(th)':>10}")
    for g, t, ta, s, sa in r["cod"]:
        print(f"{g:14.1f} {t:15.4f} {ta:10.4f} {s:15.4f} {sa:10.4f}")
    print("B. Diafragma en el centro de curvatura C: distancia de C al foco")
    print(f"{'campo [grados]':>14} {'|F - C| [mm]':>14} {'z del foco [mm]':>16}")
    for g, d, z in r["sup"]:
        print(f"{g:14.1f} {d:14.4f} {z:16.4f}")
    print(f"Tolerancia de foco +-2 lambda N^2 = {r['delta']:.4f} mm ; campo maximo con detector plano = {math.degrees(r['th_max']):.3f} grados")
    print(f"Hundimiento del foco a 1 grado sin aplanador = {r['dz_sin']:.4f} mm ; analitico f theta^2 / 2 = {F * math.radians(1.0) ** 2 / 2.0:.4f} mm")
    print(f"{'focal del aplanador [mm]':>25} {'z(1 grado) - z(0) [mm]':>24}")
    for fl, dz in r["barrido"]:
        print(f"{fl:25.1f} {dz:24.4f}")
    print(f"Focal optima interpolada = {r['fl_opt']:.1f} mm ; teoria de Petzval phi = -n_lente / f ==> f_l = {r['fl_teo']:.1f} mm")
    for g, t, ta, s, sa in r["cod"]:
        assert abs(t - ta) / ta < 1e-3 and abs(s - sa) / sa < 1e-3
    for g, d, z in r["sup"]:
        assert abs(d - F) / F < 2e-3
    assert r["fl_opt"] is not None and abs(r["fl_opt"] / r["fl_teo"] - 1.0) < 0.3
    assert abs(r["petz"][0] + r["petz"][1]) < 1e-12
    assert abs(r["dz_sin"] + F * math.radians(1.0) ** 2 / 2.0) < 2e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
