#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C06: tubo de choque de Sod en 1D con SPH, con malla (Godunov de primer orden con HLL) y con la solucion exacta de Riemann.

Datos: ninguna constante fisica. El problema de Sod (izquierda rho=1, p=1; derecha rho=0,125, p=0,1; reposo; gamma = 1,4; t = 0,2 en [-0,5, 0,5]) es el CASO DE PRUEBA clasico, con
parametros ILUSTRATIVOS; las resoluciones y los coeficientes de viscosidad artificial son elecciones de este laboratorio. Del metodo de malla movil de Springel (2010) solo se leyo el resumen
(consultado el 2026-11-09); este laboratorio NO implementa ese metodo.
Modelo: (a) solucion exacta por iteracion de Newton para la presion de la region central; (b) malla fija con flujo HLL de primer orden; (c) SPH 1D con nucleo spline cubico, particulas de masa
igual, h = 1,2 m/rho (con rho de la iteracion previa), viscosidad artificial de Monaghan (alpha = 1, beta = 2) e integracion leapfrog con paso adaptativo.
Supuestos: gas ideal, sin gravedad ni enfriamiento, 1D. Validez: ilustrativa.
Tolerancia: el error L1 de la densidad de la malla debe disminuir al duplicar las celdas; el error L1 de SPH debe disminuir al duplicar las particulas y ser menor que 0,06, y el de la malla menor que el de SPH; masa conservada a 1e-12 y energia total a 1 %.
"""
from __future__ import annotations
import math, platform, sys

GAM = 1.4
T_FIN = 0.2

def exacta(x, t):
    rl, pl, rr, pr = 1.0, 1.0, 0.125, 0.1
    cl, cr = math.sqrt(GAM * pl / rl), math.sqrt(GAM * pr / rr)
    def f(p, r0, p0, c0):
        if p > p0:
            a = 2 / ((GAM + 1) * r0)
            b = (GAM - 1) / (GAM + 1) * p0
            return (p - p0) * math.sqrt(a / (p + b))
        return 2 * c0 / (GAM - 1) * ((p / p0) ** ((GAM - 1) / (2 * GAM)) - 1)
    p = 0.5 * (pl + pr)
    for _ in range(100):
        fv = f(p, rl, pl, cl) + f(p, rr, pr, cr)
        h = 1e-7 * p
        d = (f(p + h, rl, pl, cl) + f(p + h, rr, pr, cr) - fv) / h
        pn = p - fv / d
        if abs(pn - p) < 1e-14:
            p = pn
            break
        p = max(pn, 1e-8)
    u = 0.5 * (f(p, rr, pr, cr) - f(p, rl, pl, cl))
    # region central izquierda (rarefaccion a su derecha) y derecha (choque)
    rstar_l = rl * (p / pl) ** (1 / GAM)
    cstar_l = cl * (p / pl) ** ((GAM - 1) / (2 * GAM))
    rstar_r = rr * ((p / pr + (GAM - 1) / (GAM + 1)) / ((GAM - 1) / (GAM + 1) * p / pr + 1))
    s_shock = u * rstar_r / (rstar_r - rr)
    xs = x / t
    cabeza, cola = -cl, u - cstar_l
    if xs < cabeza:
        return rl, 0.0, pl
    if xs < cola:
        uu = 2 / (GAM + 1) * (cl + xs)
        cc = 2 / (GAM + 1) * (cl - (GAM - 1) / 2 * xs)
        rr_ = rl * (cc / cl) ** (2 / (GAM - 1))
        return rr_, uu, pl * (cc / cl) ** (2 * GAM / (GAM - 1))
    if xs < u:
        return rstar_l, u, p
    if xs < s_shock:
        return rstar_r, u, p
    return rr, 0.0, pr

def hll(ul, ur):
    def prim(U):
        r, m, e = U
        u = m / r
        p = (GAM - 1) * (e - 0.5 * r * u * u)
        return r, u, p
    def flux(U):
        r, u, p = prim(U)
        return (r * u, r * u * u + p, (U[2] + p) * u)
    rl, uL, pl = prim(ul); rr, uR, pr = prim(ur)
    cl, cr = math.sqrt(GAM * pl / rl), math.sqrt(GAM * pr / rr)
    sl, sr = min(uL - cl, uR - cr), max(uL + cl, uR + cr)
    fl, fr = flux(ul), flux(ur)
    if sl >= 0:
        return fl
    if sr <= 0:
        return fr
    return tuple((sr * a - sl * b + sl * sr * (c - d)) / (sr - sl) for a, b, c, d in zip(fl, fr, ur, ul))

def malla(n):
    dx = 1.0 / n
    xc = [-0.5 + (i + 0.5) * dx for i in range(n)]
    U = []
    for x in xc:
        r, p = (1.0, 1.0) if x < 0 else (0.125, 0.1)
        U.append([r, 0.0, p / (GAM - 1)])
    t = 0.0
    while t < T_FIN - 1e-14:
        smax = max(abs(u[1] / u[0]) + math.sqrt(GAM * (GAM - 1) * (u[2] - 0.5 * u[1] ** 2 / u[0]) / u[0]) for u in U)
        dt = min(0.4 * dx / smax, T_FIN - t)
        F = [hll(U[0], U[0])]
        F += [hll(U[i], U[i + 1]) for i in range(n - 1)]
        F.append(hll(U[-1], U[-1]))
        for i in range(n):
            for k in range(3):
                U[i][k] -= dt / dx * (F[i + 1][k] - F[i][k])
        t += dt
    rho = [u[0] for u in U]
    masa = sum(rho) * dx
    ener = sum(u[2] for u in U) * dx
    return xc, rho, masa, ener

def w_spline(q, h):
    s = 2 / (3 * h)
    if q < 1:
        return s * (1 - 1.5 * q * q + 0.75 * q ** 3)
    if q < 2:
        return s * 0.25 * (2 - q) ** 3
    return 0.0

def dw_spline(q, h):
    s = 2 / (3 * h * h)
    if q < 1:
        return s * (-3 * q + 2.25 * q * q)
    if q < 2:
        return s * (-0.75 * (2 - q) ** 2)
    return 0.0

def sph(nl, nr):
    m = 1.0 * 0.5 / nl  # masa por particula (rho_l x longitud 0,5 / nl)
    x = [-0.5 + (i + 0.5) * 0.5 / nl for i in range(nl)] + [(i + 0.5) * 0.5 / nr for i in range(nr)]
    # igual masa: el lado derecho tiene rho = 0,125 => nr = nl/8 para igual m
    n = len(x)
    v = [0.0] * n
    u = [1.0 / ((GAM - 1) * 1.0)] * nl + [0.1 / ((GAM - 1) * 0.125)] * nr
    h = [1.2 * 0.5 / nl] * nl + [1.2 * 0.5 / nr] * nr
    def dens_y_fuerzas(x, v, u, h):
        rho = [0.0] * n
        for i in range(n):
            s = 0.0
            for j in range(max(0, i - 40), min(n, i + 41)):
                s += m * w_spline(abs(x[i] - x[j]) / h[i], h[i])
            rho[i] = s
        h_nuevo = [1.2 * m / r for r in rho]
        p = [(GAM - 1) * rho[i] * u[i] for i in range(n)]
        c = [math.sqrt(GAM * p[i] / rho[i]) for i in range(n)]
        dv, du = [0.0] * n, [0.0] * n
        for i in range(n):
            for j in range(max(0, i - 40), min(n, i + 41)):
                if i == j:
                    continue
                dx = x[i] - x[j]
                hij = 0.5 * (h[i] + h[j])
                q = abs(dx) / hij
                if q >= 2:
                    continue
                dw = dw_spline(q, hij) * (1 if dx > 0 else -1)
                vij = v[i] - v[j]
                pi_ = 0.0
                if vij * dx < 0:
                    mu = hij * vij * dx / (dx * dx + 0.01 * hij * hij)
                    cb = 0.5 * (c[i] + c[j]); rb = 0.5 * (rho[i] + rho[j])
                    pi_ = (-1.0 * cb * mu + 2.0 * mu * mu) / rb
                dv[i] -= m * (p[i] / rho[i] ** 2 + p[j] / rho[j] ** 2 + pi_) * dw
                du[i] += 0.5 * m * (p[i] / rho[i] ** 2 + p[j] / rho[j] ** 2 + pi_) * vij * dw
        return rho, dv, du, h_nuevo, c
    # los bordes extremos quedan intactos en t=0,2 (la onda no llega)
    rho, a, du, h, c = dens_y_fuerzas(x, v, u, h)
    t = 0.0
    while t < T_FIN - 1e-14:
        dt = min(0.25 * min(h[i] / (c[i] + 1e-12) for i in range(n)), T_FIN - t)
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
            u[i] += 0.5 * dt * du[i]
            x[i] += dt * v[i]
        rho, a, du, h, c = dens_y_fuerzas(x, v, u, h)
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
            u[i] += 0.5 * dt * du[i]
        t += dt
    energia = sum(m * (u[i] + 0.5 * v[i] ** 2) for i in range(n))
    return x, rho, m * n, energia

def error_l1(xs, rhos):
    return sum(abs(r - exacta(x, T_FIN)[0]) for x, r in zip(xs, rhos)) / len(xs)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r, u, p = exacta(0.1, T_FIN)
    print(f"solucion exacta en x = 0,1, t = 0,2: rho = {r:.4f}, u = {u:.4f}, p = {p:.4f}")
    # cantidades de la region central
    print(f"exacta: rho en x = -0,3: {exacta(-0.3, T_FIN)[0]:.4f}; x = 0,2: {exacta(0.2, T_FIN)[0]:.4f}; x = 0,4: {exacta(0.4, T_FIN)[0]:.4f}")
    errs = {}
    for n in (100, 200, 400):
        xs, rho, masa, ener = malla(n)
        errs[n] = error_l1(xs, rho)
        print(f"malla N = {n:4d}: error L1 de rho = {errs[n]:.5f}")
    assert errs[200] < errs[100] and errs[400] < errs[200]
    xs, rho, masa, ener = malla(400)
    e_ini = (0.5 * 1.0 + 0.5 * 0.1) / (GAM - 1)
    assert abs(masa - 0.5625) < 1e-12
    assert abs(ener - e_ini) / e_ini < 0.01
    print(f"malla N = 400: masa {masa:.6f} (esperada 0.562500), energia {ener:.5f} (inicial {e_ini:.5f})")
    sel2 = [i for i, x in enumerate(xs) if abs(x) < 0.45]
    l1g = sum(abs(rho[i] - exacta(xs[i], T_FIN)[0]) for i in sel2) / len(sel2)
    e_sph = 1.0 * 0.5 / (GAM - 1) + 0.125 * 0.5 * (0.1 / 0.125) / (GAM - 1)
    errs_sph = {}
    for nl, nr in ((160, 20), (320, 40)):
        xp, rhop, masap, enerp = sph(nl, nr)
        sel = [i for i in range(len(xp)) if abs(xp[i]) < 0.45]
        mp = 0.5 / nl
        vol = [mp / exacta(xp[i], T_FIN)[0] for i in range(len(xp))]
        l1p = sum(abs(rhop[i] - exacta(xp[i], T_FIN)[0]) * vol[i] for i in sel) / sum(vol[i] for i in sel)
        errs_sph[nl] = l1p
        print(f"SPH ({len(xp)} particulas, m = {mp:.6f}): error L1 de rho = {l1p:.5f}; masa total {masap:.6f}; energia {enerp:.5f} (inicial {e_sph:.5f})")
        assert abs(masap - 0.5625) < 1e-12
        assert abs(enerp - e_sph) / e_sph < 0.01
    print(f"malla N = 400 (misma ventana): error L1 de rho = {l1g:.5f}")
    assert errs_sph[320] < errs_sph[160] < 0.12 and errs_sph[320] < 0.06
    assert l1g < errs_sph[320]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
