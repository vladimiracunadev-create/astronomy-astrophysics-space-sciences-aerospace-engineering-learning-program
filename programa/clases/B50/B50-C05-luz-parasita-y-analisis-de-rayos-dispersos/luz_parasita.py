#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B50-C05: luz parasita (fantasmas de Fresnel en una lente y dispersion lambertiana en un tubo con deflector).

Datos: ninguna constante fisica consultada. La lente (biconvexa, n = 1.5, radios de 100 mm, espesor de 4 mm), las reflectividades de 0.04 (sin recubrir) y 0.01 (recubierta, valor
ilustrativo) y el tubo (radio 60 mm, largo 300 mm, deflector de 30 mm de radio interior) son ILUSTRATIVOS (sinteticos); no se modela ningun instrumento real.
Modelo: (1) reflectividad de Fresnel a incidencia casi normal por la formula cerrada y por las amplitudes rs y rp; razon de potencia del fantasma de doble reflexion R1 R2.
(2) Posicion y tamano del fantasma: trazado exacto (reflexiones internas con los mismos objetos de superficie) frente a la matriz de transferencia paraxial (n u' = n u - h phi, phi = -2n/R en la reflexion).
(3) Factor de vista de un parche lambertiano de la pared al disco detector: cuadratura determinista frente a Monte Carlo con semilla 20261109, sin y con deflector.
Supuestos: sin polarizacion detallada, sin dispersion, parche pequeno, pared absorbente despues del primer rebote. Validez: ilustrativa.
Tolerancia: Fresnel 1e-4; foco del fantasma 1e-3 mm; factor de vista Monte Carlo frente a cuadratura < 0.003 (absoluto).
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
LAM = 550e-6


def fresnel_normal(n):
    return ((n - 1.0) / (n + 1.0)) ** 2


def fresnel_amplitudes(n, th):
    ci = math.cos(th)
    st = math.sin(th) / n
    ct = math.sqrt(1.0 - st * st)
    rs = (ci - n * ct) / (ci + n * ct)
    rp = (n * ci - ct) / (n * ci + ct)
    return 0.5 * (rs * rs + rp * rp)


def fantasma_paraxial(r1, r2, t, n):
    """Cruce con el eje del rayo paraxial tras: refraccion 1, reflexion en 2, reflexion en 1, refraccion 2 (altura inicial 1)."""
    # estado (h, nu) en z = 0; superficies con vertice en z1 = 0, z2 = t
    h, nu = 1.0, 0.0
    phi1 = (n - 1.0) / r1
    nu = nu - h * phi1                       # refraccion en 1
    h = h + (nu / n) * t                      # hasta 2
    nu = nu - h * (-2.0 * n / r2)             # reflexion en 2 (medio n)
    h = h + (nu / n) * t                      # de vuelta a 1 (espacio desplegado: se sigue avanzando)
    nu = nu - h * (2.0 * n / r1)              # reflexion en 1: en el espacio desplegado el radio cambia de signo
    h = h + (nu / n) * (t)                    # de nuevo hacia 2
    nu = nu - h * (1.0 - n) / r2              # refraccion en 2 al aire
    z = t - h / nu                            # cruce con el eje tras la superficie 2 real (en z = t, hacia +z)
    return z, h, nu


def fantasma_trazado(h0, r1, r2, t, n):
    s1 = Sup(0.0, c=1.0 / r1, n=n)
    s2 = Sup(t, c=1.0 / r2, n=1.0)
    s1b = Sup(0.0, c=1.0 / r1, espejo=True)
    s2m = Sup(t, c=1.0 / r2, espejo=True)
    s2e = Sup(t, c=1.0 / r2, n=1.0)
    # el medio tras el primer vertice es el vidrio; la salida final por la superficie 2 vuelve al aire
    ss = [s1, s2m, s1b, s2e]
    ss[0].n = n
    O, D = haz(0.0, 0.0, h0, 0.0, -10.0)
    # n efectivo: las reflexiones no cambian el medio
    r = trazar(ss, O, D)
    return r


def calcular():
    r1, r2, t, n = 100.0, -100.0, 4.0, N_G
    R0 = fresnel_normal(n)
    R_ang = fresnel_amplitudes(n, 1e-6)
    ghost_sin = R0 * R0
    ghost_rec = 0.01 * 0.01
    # fantasma
    zp, _, _ = fantasma_paraxial(r1, r2, t, n)
    O1, D1, _, _ = fantasma_trazado(1e-4, r1, r2, t, n)
    tt = -O1[0] / D1[0]
    zt = O1[2] + tt * D1[2]
    # imagen real
    lente = [Sup(0.0, c=1.0 / r1, n=n), Sup(t, c=1.0 / r2, n=1.0)]
    O, D = haz(0.0, 0.0, 1e-4, 0.0, -10.0)
    Oi, Di, _, _ = trazar(lente, O, D)
    z_img = Oi[2] + (-Oi[0] / Di[0]) * Di[2]
    a = 1.0
    Og, Dg, _, _ = fantasma_trazado(a, r1, r2, t, n)
    xg, _ = a_plano(Og, Dg, z_img)
    radio_fantasma = abs(xg[0])
    Og10, Dg10, _, _ = fantasma_trazado(10.0, r1, r2, t, n)
    radio10 = abs(a_plano(Og10, Dg10, z_img)[0][0])
    # paraxial: altura del fantasma en el plano de imagen (lineal en h0)
    zgp, hh, nu = fantasma_paraxial(r1, r2, t, n)
    h_plano = abs((hh + (nu * 1.0) * (z_img - t)) * a)
    # factor de vista
    a_tubo, L, b_def, z_def = 60.0, 300.0, 30.0, 150.0
    def f_cuad(con_def):
        nr, nf = 300, 300
        tot = 0.0
        for i in range(nr):
            r = a_tubo * (i + 0.5) / nr
            for j in range(nf):
                ph = 2 * math.pi * (j + 0.5) / nf
                qx, qy = r * math.cos(ph), r * math.sin(ph)
                vx, vy, vz = qx - a_tubo, qy, L
                d2 = vx * vx + vy * vy + vz * vz
                d = math.sqrt(d2)
                c1 = -vx / d
                c2 = vz / d
                if c1 <= 0:
                    continue
                if con_def:
                    s = z_def / L
                    rb = math.hypot(a_tubo + s * vx, s * vy)
                    if rb >= b_def:
                        continue
                tot += c1 * c2 / (math.pi * d2) * (a_tubo * (a_tubo / nr) * (2 * math.pi / nf)) * (r / a_tubo)
        return tot
    def f_mc(con_def, N=400000):
        rng = random.Random(20261109)
        ok = 0
        for _ in range(N):
            u1, u2 = rng.random(), rng.random()
            st = math.sqrt(u1)
            ct = math.sqrt(1.0 - u1)
            ph = 2 * math.pi * u2
            # base local: n1 = (-1, 0, 0), e1 = (0, 1, 0), e2 = (0, 0, 1)
            dx, dy, dz = -ct, st * math.cos(ph), st * math.sin(ph)
            if dz <= 0:
                continue
            s = L / dz
            qx, qy = a_tubo + s * dx, s * dy
            if math.hypot(qx, qy) > a_tubo:
                continue
            if con_def:
                sb = z_def / dz
                if math.hypot(a_tubo + sb * dx, sb * dy) >= b_def:
                    continue
            ok += 1
        return ok / N
    return dict(R0=R0, R_ang=R_ang, ghost_sin=ghost_sin, ghost_rec=ghost_rec, zp=zp, zt=zt, z_img=z_img, radio=radio_fantasma, hp=h_plano, radio10=radio10,
                F=(f_cuad(False), f_mc(False), f_cuad(True), f_mc(True)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Fresnel a incidencia normal, n = 1.5: formula cerrada = {r['R0']:.6f} ; por amplitudes rs y rp a 1e-6 rad = {r['R_ang']:.6f}")
    print(f"Fantasma de doble reflexion (razon de potencia R1 R2): sin recubrir = {r['ghost_sin']:.2e} ; con R = 0.01 = {r['ghost_rec']:.2e}")
    print(f"Foco del fantasma: matriz paraxial z = {r['zp']:.5f} mm ; trazado exacto z = {r['zt']:.5f} mm ; imagen real z = {r['z_img']:.4f} mm")
    print(f"Radio del fantasma en el plano de imagen (h = 1 mm): trazado = {r['radio']:.4f} mm ; paraxial = {r['hp']:.4f} mm")
    print(f"Mismo fantasma con h = 10 mm (aberracion esferica del fantasma): radio = {r['radio10']:.4f} mm")
    print(f"Factor de vista parche-detector sin deflector: cuadratura = {r['F'][0]:.5f} ; Monte Carlo = {r['F'][1]:.5f}")
    print(f"Factor de vista con deflector de 30 mm a 150 mm: cuadratura = {r['F'][2]:.5f} ; Monte Carlo = {r['F'][3]:.5f}")
    print(f"Reduccion por el deflector = {r['F'][0] / r['F'][2]:.2f} veces")
    assert abs(r["R0"] - r["R_ang"]) < 1e-4
    assert abs(r["zp"] - r["zt"]) < 1e-3
    assert abs(r["radio"] - r["hp"]) / r["hp"] < 0.01
    assert abs(r["F"][0] - r["F"][1]) < 0.003 and abs(r["F"][2] - r["F"][3]) < 0.003
    assert r["F"][2] < r["F"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
