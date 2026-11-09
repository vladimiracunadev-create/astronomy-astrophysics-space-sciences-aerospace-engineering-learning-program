#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C15: presupuesto de error de frente de onda de un instrumento (de la superficie al frente de onda, suma cuadratica y Strehl).

Datos: ninguna constante fisica consultada. Todos los terminos del presupuesto (errores de figura de los espejos, residuo de diseno, alineacion, termico y gravedad, pulido de media frecuencia),
el requisito de Strehl 0.80 a 1.0 micrometro y las longitudes de onda de 0.55, 1.0 y 2.2 micrometros son ILUSTRATIVOS (sinteticos); no corresponden a ningun instrumento real.
Modelo: (A) el error de superficie s se convierte en error de frente de onda: reflexion a incidencia theta, 2 s cos(theta); refraccion en una superficie con aire, (n - 1) s a incidencia normal;
ambos se comprueban con el trazador de rayos desplazando una superficie. (B) Suma cuadratica de terminos independientes y Strehl de Marechal exp(-(2 pi sigma / lambda)^2). (C) Monte Carlo con
semilla 20261109: cada termino es una combinacion aleatoria de 10 modos ortonormales de varianza unidad; la media de W^2 es la suma de varianzas. (D) Asignacion inversa: lo que queda del requisito.
Supuestos: terminos independientes, de media cero, Marechal valido (sigma pequeno). Validez: ilustrativa.
Tolerancia: factores 2 cos(theta) y (n - 1) a 1e-9 (diferencia finita con s = 1 micrometro); media de Monte Carlo dentro de 3 errores tipicos de la suma cuadratica.
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


TERMINOS = [
    ("figura del primario (superficie 18 nm RMS, factor 2)", 18.0, 2.0),
    ("figura del secundario (superficie 12 nm RMS, factor 2)", 12.0, 2.0),
    ("residuo del diseno nominal (frente de onda directo)", 10.0, 1.0),
    ("alineacion (frente de onda directo)", 22.0, 1.0),
    ("termico y gravedad (frente de onda directo)", 15.0, 1.0),
    ("pulido de media frecuencia (superficie 6 nm RMS, factor 2)", 6.0, 2.0),
]
LAMS = [550.0, 1000.0, 2200.0]
REQ_S, REQ_LAM = 0.80, 1000.0


def opd_reflexion_directa(s, th):
    """OPD respecto del frente de onda reflejado de referencia: se mide el camino hasta un plano perpendicular al rayo reflejado."""
    espejo0, espejo1 = Sup(0.0, c=0.0, espejo=True), Sup(0.0, c=0.0, espejo=True)
    mover(espejo1, dz=s)
    D = (math.sin(th), 0.0, math.cos(th))
    R = (math.sin(th), 0.0, -math.cos(th))
    res = []
    for e in (espejo0, espejo1):
        O = (0.0, 0.0, -10.0)
        o = trazar([e], O, D)
        P = o[0]
        # plano perpendicular a R que pasa por (0,0,-50)
        t = ((0.0 - P[0]) * R[0] + (-50.0 - P[2]) * R[2]) / (o[1][0] * R[0] + o[1][2] * R[2])
        res.append(o[2] + t)
    return res[1] - res[0]


def opd_refraccion(s, n):
    # placa plano-paralela: la cara trasera se desplaza s (espesor 5 + s); se mide el camino hasta z = 20
    res = []
    for ds in (0.0, s):
        a, b = Sup(0.0, c=0.0, n=n), Sup(5.0 + ds, c=0.0, n=1.0)
        O, D = (0.0, 0.0, -10.0), (0.0, 0.0, 1.0)
        o = trazar([a, b], O, D)
        t = (20.0 - o[0][2]) / o[1][2]
        res.append(o[2] + t)
    return res[1] - res[0]


def calcular():
    f2 = opd_reflexion_directa(1e-3, 0.0) / 1e-3
    th = math.radians(30.0)
    f2c = opd_reflexion_directa(1e-3, th) / 1e-3
    fr = opd_refraccion(1e-3, 1.5) / 1e-3
    w = [(nm, s * f) for nm, s, f in TERMINOS]
    tot = math.sqrt(sum(x * x for _, x in w))
    st = {lam: math.exp(-(2 * math.pi * tot / lam) ** 2) for lam in LAMS}
    sig_max = REQ_LAM / (2 * math.pi) * math.sqrt(-math.log(REQ_S))
    cumple = st[REQ_LAM] >= REQ_S
    margen = sig_max - tot
    # lo que queda para alineacion si el resto no cambia
    resto = math.sqrt(sig_max**2 - sum(x * x for nm, x in w if not nm.startswith("alineacion")))
    # Monte Carlo
    rng = random.Random(20261109)
    N, K = 20000, 10
    acc, acc2 = 0.0, 0.0
    for _ in range(N):
        q = 0.0
        coef = [0.0] * K
        for nm, x in w:
            for k in range(K):
                coef[k] += x / math.sqrt(K) * rng.gauss(0.0, 1.0)
        q = sum(c * c for c in coef)
        acc += q; acc2 += q * q
    media = acc / N
    se = math.sqrt((acc2 / N - media**2) / N)
    return dict(f2=f2, f2c=f2c, fr=fr, w=w, tot=tot, st=st, sig_max=sig_max, cumple=cumple, margen=margen, resto=resto, media=media, se=se, pred=tot**2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"A. Factores de superficie a frente de onda por trazado: reflexion normal = {r['f2']:.12f} ; reflexion a 30 grados = {r['f2c']:.12f} (2 cos = {2 * math.cos(math.radians(30.0)):.12f}) ; refraccion (n = 1.5) = {r['fr']:.12f}")
    print(f"{'termino':>62} {'frente de onda [nm RMS]':>24}")
    for nm, x in r["w"]:
        print(f"{nm:>62} {x:24.2f}")
    print(f"Total (suma cuadratica) = {r['tot']:.3f} nm RMS")
    print("Strehl de Marechal: " + " ; ".join(f"{lam:.0f} nm = {s:.4f}" for lam, s in r["st"].items()))
    print(f"Requisito: Strehl >= {REQ_S} a {REQ_LAM:.0f} nm => frente de onda <= {r['sig_max']:.2f} nm RMS ; margen = {r['margen']:.2f} nm ; cumple = {r['cumple']}")
    print(f"Si todo lo demas queda fijo, la alineacion podria llegar a {r['resto']:.2f} nm RMS")
    print(f"Monte Carlo (20 000 sistemas): media de W^2 = {r['media']:.2f} +- {r['se']:.2f} nm^2 ; suma cuadratica = {r['pred']:.2f} nm^2")
    assert abs(r["f2"] - 2.0) < 1e-9 and abs(r["f2c"] - 2 * math.cos(math.radians(30.0))) < 1e-9 and abs(r["fr"] - 0.5) < 1e-9
    assert r["cumple"] and r["margen"] > 0
    assert abs(r["media"] - r["pred"]) < 3 * r["se"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
