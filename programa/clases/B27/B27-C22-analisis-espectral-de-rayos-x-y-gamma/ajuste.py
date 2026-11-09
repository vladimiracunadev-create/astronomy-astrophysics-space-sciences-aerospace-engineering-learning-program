#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C22: ajuste espectral con matriz de respuesta y estadistica de conteos (Cash frente a chi cuadrado).

Datos: ninguna constante fisica. Contexto: el manual de XSPEC (pagina consultada el 2026-11-09, sin las definiciones de
chi^2, C-stat, RMF ni ARF) y el telescopio Fermi-LAT (arXiv:0902.1089, resumen). La respuesta (area efectiva y matriz
de redistribucion), el espectro y el tiempo de exposicion son SINTETICOS; no se cita ninguna medicion.
Modelo: ley de potencias N(E) = K (E/3 keV)^-Gamma [fotones/cm2/s/keV], plegada con una ARF (area efectiva) y una RMF
gaussiana (sigma = 0.1 E, normalizada por columnas): mu_j = T sum_i R_ji A_i N(E_i) dE_i. Las cuentas son Poisson.
Estadistica de Cash C = 2 sum (mu - n ln mu) frente a chi^2 con varianza igual a las cuentas observadas (n; 1 si n = 0).
Minimizacion con Nelder-Mead de dos parametros (ln K, Gamma). Monte Carlo con semilla fija.
Supuestos: respuesta conocida, sin fondo; Poisson exacto (Knuth) para media <= 30 y gaussiana redondeada para media > 30. Validez: ilustrativa.
Tolerancia: 1e-9 en el plegado con respuesta identidad; |sesgo medio de Gamma| con Cash < 0.1.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

NE, NC = 15, 20
EMIN, EMAX = 1.0, 10.0
EDGES = [EMIN * (EMAX / EMIN) ** (i / NE) for i in range(NE + 1)]
EMID = [math.sqrt(EDGES[i] * EDGES[i + 1]) for i in range(NE)]
DE = [EDGES[i + 1] - EDGES[i] for i in range(NE)]
CEDGES = [EMIN * (EMAX / EMIN) ** (j / NC) for j in range(NC + 1)]
ARF = [200.0 * (e / 1.0) ** -0.3 for e in EMID]     # cm2
T_EXP = 1000.0                                       # s


def cdf(x):
    return 0.5 * math.erfc(-x / math.sqrt(2))


def construir_rmf():
    r = [[0.0] * NE for _ in range(NC)]
    for i, e in enumerate(EMID):
        s = 0.1 * e
        col = [cdf((CEDGES[j + 1] - e) / s) - cdf((CEDGES[j] - e) / s) for j in range(NC)]
        tot = sum(col)
        for j in range(NC):
            r[j][i] = col[j] / tot
    return r


RMF = construir_rmf()


def pliegue(k, gamma, rmf=RMF):
    fot = [T_EXP * ARF[i] * k * (EMID[i] / 3.0) ** -gamma * DE[i] for i in range(NE)]
    return [sum(rmf[j][i] * fot[i] for i in range(NE)) for j in range(len(rmf))]


def cash(par, n):
    lk, g = par
    mu = pliegue(math.exp(lk), g)
    return 2 * sum(m - c * math.log(max(m, 1e-300)) for m, c in zip(mu, n))


def chi2(par, n):
    lk, g = par
    mu = pliegue(math.exp(lk), g)
    return sum((c - m) ** 2 / (c if c > 0 else 1.0) for m, c in zip(mu, n))


def nelder_mead(f, x0, paso=(0.3, 0.3), iters=400):
    pts = [list(x0), [x0[0] + paso[0], x0[1]], [x0[0], x0[1] + paso[1]]]
    vals = [f(p) for p in pts]
    for _ in range(iters):
        orden = sorted(range(3), key=lambda i: vals[i])
        pts, vals = [pts[i] for i in orden], [vals[i] for i in orden]
        c = [(pts[0][k] + pts[1][k]) / 2 for k in range(2)]
        xr = [c[k] + (c[k] - pts[2][k]) for k in range(2)]
        fr = f(xr)
        if fr < vals[0]:
            xe = [c[k] + 2 * (c[k] - pts[2][k]) for k in range(2)]
            fe = f(xe)
            pts[2], vals[2] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[1]:
            pts[2], vals[2] = xr, fr
        else:
            xc = [c[k] + 0.5 * (pts[2][k] - c[k]) for k in range(2)]
            fc = f(xc)
            if fc < vals[2]:
                pts[2], vals[2] = xc, fc
            else:
                for i in (1, 2):
                    pts[i] = [pts[0][k] + 0.5 * (pts[i][k] - pts[0][k]) for k in range(2)]
                    vals[i] = f(pts[i])
    i = min(range(3), key=lambda i: vals[i])
    return pts[i], vals[i]


def poisson(lam, rng):
    if lam > 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # comprobacion del plegado con respuesta identidad
    ident = [[1.0 if j == i else 0.0 for i in range(NE)] for j in range(NE)]
    mu_id = pliegue(0.0005, 2.0, ident)
    for i in range(NE):
        esp = T_EXP * ARF[i] * 0.0005 * (EMID[i] / 3.0) ** -2.0 * DE[i]
        assert abs(mu_id[i] / esp - 1) < 1e-9, "plegado con respuesta identidad"
    # conservacion: columnas de la RMF suman 1
    assert all(abs(sum(RMF[j][i] for j in range(NC)) - 1) < 1e-12 for i in range(NE))
    # prueba del minimizador con una funcion cuadratica conocida
    xm, fm = nelder_mead(lambda p: (p[0] - 1.5) ** 2 + 3 * (p[1] + 0.5) ** 2 + 2.0, [0.0, 0.0])
    assert abs(xm[0] - 1.5) < 1e-6 and abs(xm[1] + 0.5) < 1e-6 and abs(fm - 2.0) < 1e-9, "Nelder-Mead"
    print("plegado con respuesta identidad: correcto ; columnas de la RMF suman 1 ; Nelder-Mead recupera el minimo de una cuadratica")
    k0, g0 = 0.0005, 2.0
    mu = pliegue(k0, g0)
    print(f"cuentas esperadas totales = {sum(mu):.1f} en {NC} canales ({EMIN}-{EMAX} keV, exposicion {T_EXP:.0f} s)")
    p0, _ = nelder_mead(lambda p: cash(p, mu), [math.log(k0), 1.5])
    assert abs(p0[1] - g0) < 1e-3 and abs(math.exp(p0[0]) / k0 - 1) < 1e-3, "recuperacion sin ruido"
    print(f"ajuste sin ruido (n = mu): Gamma = {p0[1]:.5f} ; K = {math.exp(p0[0]):.5f}")
    rng = random.Random(20261109)
    nrep = 100
    g_c, g_x = [], []
    for _ in range(nrep):
        n = [poisson(m, rng) for m in mu]
        pc, _ = nelder_mead(lambda p: cash(p, n), [math.log(k0), 1.5])
        px, _ = nelder_mead(lambda p: chi2(p, n), [math.log(k0), 1.5])
        g_c.append(pc[1])
        g_x.append(px[1])
    for nombre, gs in (("Cash", g_c), ("chi2 con varianza = cuentas", g_x)):
        print(f"{nombre}: Gamma medio = {statistics.mean(gs):.4f} (sesgo {statistics.mean(gs) - g0:+.4f}) ; desviacion = {statistics.pstdev(gs):.4f}")
    assert abs(statistics.mean(g_c) - g0) < 0.1, "sesgo con Cash"
    # cuentas mas bajas: exposicion 10 veces menor
    globals()["T_EXP"] = 100.0

    mu2 = pliegue(k0, g0)
    print(f"exposicion reducida a {T_EXP:.0f} s: cuentas esperadas = {sum(mu2):.1f}")
    g_c2, g_x2 = [], []
    for _ in range(nrep):
        n = [poisson(m, rng) for m in mu2]
        pc, _ = nelder_mead(lambda p: cash(p, n), [math.log(k0), 1.5])
        px, _ = nelder_mead(lambda p: chi2(p, n), [math.log(k0), 1.5])
        g_c2.append(pc[1])
        g_x2.append(px[1])
    for nombre, gs in (("Cash", g_c2), ("chi2 con varianza = cuentas", g_x2)):
        print(f"{nombre}: Gamma medio = {statistics.mean(gs):.4f} (sesgo {statistics.mean(gs) - g0:+.4f}) ; desviacion = {statistics.pstdev(gs):.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
