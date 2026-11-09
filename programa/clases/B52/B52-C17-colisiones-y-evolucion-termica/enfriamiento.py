#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C17: calentamiento por impacto y enfriamiento por conduccion de un cuerpo esferico.

Sin constantes fisicas consultadas. Datos ILUSTRATIVOS (sinteticos): radio R = 50 km, difusividad termica kappa = 1e-6 m^2/s, calor especifico 1000 J/(kg K),
velocidad de impacto 5 km/s con fraccion de energia termalizada 0.1, temperatura inicial uniforme T0 (el resultado se da en unidades de T0).
Sistema de referencia: esfera con simetria radial, borde a temperatura 0 (espacio frio), sin fuentes internas; SI.
Via 1: serie analitica T(0,t)/T0 = 2 sum (-1)^(n+1) exp(-n^2 pi^2 kappa t / R^2) y temperatura media volumetrica.
Via 2: diferencias finitas en u = r T (ecuacion del calor 1D) con Crank-Nicolson y solucion tridiagonal (N = 400, dt = tau/2000).
Tolerancias: temperatura central y media numericas frente a la serie 1e-3 relativo (para t >= 0.1 tau).
"""
from __future__ import annotations
import math, platform

R, KAPPA, CP, V_IMP, ETA = 50e3, 1e-6, 1000.0, 5e3, 0.1
TAU = R ** 2 / (math.pi ** 2 * KAPPA)


def serie_centro(t, nterm=200):
    return 2.0 * sum((-1) ** (n + 1) * math.exp(-n * n * math.pi ** 2 * KAPPA * t / R ** 2) for n in range(1, nterm))


def serie_media(t, nterm=200):
    # media volumetrica: 6 sum exp(-n^2 pi^2 kappa t / R^2) / (n^2 pi^2)
    return 6.0 * sum(math.exp(-n * n * math.pi ** 2 * KAPPA * t / R ** 2) / (n * n * math.pi ** 2) for n in range(1, nterm))


def thomas(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def numerico(tiempos, N=400):
    dr = R / N
    dt = TAU / 2000.0
    k = KAPPA * dt / dr ** 2
    u = [(i * dr) * 1.0 for i in range(N + 1)]  # u = r T con T = 1
    u[N] = 0.0
    t, res = 0.0, {}
    objetivos = sorted(tiempos)
    j = 0
    while j < len(objetivos):
        m = N - 1
        a = [-k / 2] * m; b = [1 + k] * m; c = [-k / 2] * m
        d = [u[i] + k / 2 * (u[i - 1] - 2 * u[i] + u[i + 1]) for i in range(1, N)]
        sol = thomas(a, b, c, d)
        u = [0.0] + sol + [0.0]
        t += dt
        while j < len(objetivos) and t >= objetivos[j] - 1e-9 * dt:
            centro = u[1] / dr  # T(0) ~ u'(0)
            media = sum(u[i] * (i * dr) * dr for i in range(1, N)) * 3.0 / R ** 3
            res[objetivos[j]] = (centro, media)
            j += 1
    return res


def calcular():
    tiempos = [0.1 * TAU, 0.5 * TAU, 1.0 * TAU, 2.0 * TAU]
    num = numerico(tiempos)
    filas = [(t / TAU, serie_centro(t), num[t][0], serie_media(t), num[t][1]) for t in tiempos]
    dT = ETA * 0.5 * V_IMP ** 2 / CP
    return dict(filas=filas, tau=TAU, dT=dT, e_cin=0.5 * V_IMP ** 2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cuerpo ilustrativo: R = {R / 1e3:.0f} km, kappa = {KAPPA:.0e} m^2/s ; escala tau = R^2/(pi^2 kappa) = {r['tau']:.3e} s = {r['tau'] / (365.25 * 86400) / 1e6:.2f} Ma")
    print(f"Impacto a {V_IMP / 1e3:.0f} km/s, fraccion termalizada {ETA}: energia cinetica especifica = {r['e_cin']:.3e} J/kg ; Delta T = {r['dT']:.0f} K")
    print(f"{'t/tau':>6} {'T(0)/T0 serie':>14} {'T(0)/T0 CN':>12} {'<T>/T0 serie':>13} {'<T>/T0 CN':>11}")
    for x, cs, cn, ms, mn in r["filas"]:
        print(f"{x:6.2f} {cs:14.6f} {cn:12.6f} {ms:13.6f} {mn:11.6f}")
    for x, cs, cn, ms, mn in r["filas"]:
        assert abs(cn / cs - 1) < 1e-3 and abs(mn / ms - 1) < 1e-3, (x, cs, cn, ms, mn)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
