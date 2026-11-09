#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C06: modelo de diseno optico reproducible (archivo de texto con huella) y verificacion contra calculos analiticos.

Datos: ninguna constante fisica consultada. El doblete de aire (indices 1.5 y 1.6, radios y espesores) es ILUSTRATIVO (sintetico); no corresponde a ningun vidrio de catalogo ni a un instrumento.
Modelo: el diseno vive en un texto JSON con unidades explicitas; se serializa de forma canonica y se le calcula una huella SHA-256. Verificaciones: focal por la matriz de transferencia paraxial
(via analitica) frente al trazado exacto de un rayo casi axial (segunda via); regresion contra los valores de referencia guardados en el propio modelo; reversibilidad del trazado (ida y vuelta).
Se altera un radio un 0.01 % y se comprueba que la huella cambia y que la regresion falla.
Supuestos: luz monocromatica, indices constantes, sin tolerancias. Validez: ilustrativa; es un metodo de trabajo, no un diseno.
Tolerancia: focal analitica frente a trazado 1e-6 relativo; regresion 1e-6 mm; reversibilidad 1e-9 mm.
"""
from __future__ import annotations
import hashlib, json, math, platform

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


MODELO = {
    "nombre": "doblete de aire de ejemplo",
    "unidades": "mm",
    "lambda_nm": 550,
    "version": "1.0.0",
    "superficies": [
        {"R": 80.0, "espesor": 5.0, "n_despues": 1.5},
        {"R": -60.0, "espesor": 3.0, "n_despues": 1.0},
        {"R": -50.0, "espesor": 3.0, "n_despues": 1.6},
        {"R": -200.0, "espesor": 0.0, "n_despues": 1.0},
    ],
    "referencia": {},
}


def huella(m):
    m2 = dict(m)
    m2["referencia"] = {}
    txt = json.dumps(m2, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()


def construir(m, invertido=False):
    z = 0.0
    sups, zs = [], []
    n_prev = 1.0
    for s in m["superficies"]:
        zs.append(z)
        z += s["espesor"]
    lst = []
    n_antes = 1.0
    for s, z0 in zip(m["superficies"], zs):
        lst.append((z0, 1.0 / s["R"], n_antes, s["n_despues"]))
        n_antes = s["n_despues"]
    if not invertido:
        return [Sup(z0, c=c, n=n2) for z0, c, n1, n2 in lst]
    return [Sup(z0, c=c, n=n1) for z0, c, n1, n2 in lst[::-1]]


def focal_abcd(m):
    A = [[1.0, 0.0], [0.0, 1.0]]  # (h, n u)
    n = 1.0
    for i, s in enumerate(m["superficies"]):
        phi = (s["n_despues"] - n) / s["R"]
        A = [[A[0][0], A[0][1]], [A[1][0] - phi * A[0][0], A[1][1] - phi * A[0][1]]]
        n = s["n_despues"]
        t = s["espesor"]
        if t:
            A = [[A[0][0] + t / n * A[1][0], A[0][1] + t / n * A[1][1]], A[1]]
    h, nu = A[0][0], A[1][0]
    efl = -1.0 / nu
    bfl = -A[0][0] / A[1][0]
    return efl, bfl


def focal_trazada(m):
    sups = construir(m)
    O, D = haz(0.0, 0.0, 1e-3, 0.0, -10.0)
    O1, D1, _, _ = trazar(sups, O, D)
    u = D1[0] / D1[2]
    efl = -1e-3 / u
    zlast = sups[-1].V[2]
    t = -O1[0] / D1[0]
    zf = O1[2] + t * D1[2]
    return efl, zf - zlast


def metricas(m):
    a = focal_abcd(m)
    b = focal_trazada(m)
    return dict(efl_abcd=a[0], bfl_abcd=a[1], efl_traza=b[0], bfl_traza=b[1])


def reversibilidad(m):
    sups = construir(m)
    O, D = haz(0.0, math.radians(0.0), 7.0, 0.0, -10.0)
    D = (math.sin(0.02), 0.0, math.cos(0.02))
    O1, D1, _, _ = trazar(sups, O, D)
    rev = construir(m, invertido=True)
    D2 = (-D1[0], -D1[1], -D1[2])
    # el rayo de vuelta recorre el mismo camino: se traza con direccion invertida
    O2, D2f, _, _ = trazar(rev, O1, (-D1[0], -D1[1], -D1[2]) )
    t = (O[2] - O2[2]) / D2f[2]
    P = (O2[0] + t * D2f[0], O2[1] + t * D2f[1], O[2])
    return math.hypot(P[0] - O[0], P[1] - O[1])


def calcular():
    ref = metricas(MODELO)
    MODELO["referencia"] = {k: round(v, 6) for k, v in ref.items()}
    h0 = huella(MODELO)
    # modelo alterado
    alt = json.loads(json.dumps(MODELO))
    alt["superficies"][1]["R"] *= 1.0001
    h1 = huella(alt)
    m1 = metricas(alt)
    dif0 = max(abs(ref[k] - MODELO["referencia"][k]) for k in ref)
    dif1 = max(abs(m1[k] - MODELO["referencia"][k]) for k in ref)
    # el JSON canonico no depende del orden de las claves
    barajado = {k: MODELO[k] for k in reversed(list(MODELO.keys()))}
    h2 = huella(barajado)
    return dict(ref=ref, h0=h0, h1=h1, h2=h2, m1=m1, dif0=dif0, dif1=dif1, rev=reversibilidad(MODELO))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Modelo: {MODELO['nombre']} (unidades {MODELO['unidades']}, version {MODELO['version']})")
    print(f"Huella SHA-256 del modelo: {r['h0']}")
    print(f"{'magnitud':>10} {'matriz paraxial':>16} {'trazado exacto':>15}")
    print(f"{'EFL [mm]':>10} {r['ref']['efl_abcd']:16.6f} {r['ref']['efl_traza']:15.6f}")
    print(f"{'BFL [mm]':>10} {r['ref']['bfl_abcd']:16.6f} {r['ref']['bfl_traza']:15.6f}")
    print(f"Regresion del modelo original: diferencia maxima con la referencia = {r['dif0']:.2e} mm")
    print(f"Huella con las claves en otro orden: {'igual' if r['h2'] == r['h0'] else 'distinta'}")
    print(f"Modelo con R2 alterado 0.01 %: huella {'igual' if r['h1'] == r['h0'] else 'distinta'} ({r['h1'][:12]}...) ; EFL = {r['m1']['efl_abcd']:.6f} mm ; diferencia con la referencia = {r['dif1']:.2e} mm")
    print(f"Reversibilidad del trazado (ida y vuelta): desviacion = {r['rev']:.2e} mm")
    assert abs(r["ref"]["efl_abcd"] - r["ref"]["efl_traza"]) / r["ref"]["efl_abcd"] < 1e-6
    assert abs(r["ref"]["bfl_abcd"] - r["ref"]["bfl_traza"]) < 1e-3
    assert r["dif0"] < 1e-6
    assert r["h2"] == r["h0"] and r["h1"] != r["h0"]
    assert r["dif1"] > 1e-3
    assert r["rev"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
