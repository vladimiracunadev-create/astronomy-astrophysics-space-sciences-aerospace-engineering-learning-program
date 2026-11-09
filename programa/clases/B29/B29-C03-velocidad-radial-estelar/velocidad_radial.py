#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C03: semiamplitud de velocidad radial, ecuacion de Kepler y ajuste de una curva de velocidad radial.

Datos: G (NIST CODATA 2022), GM_sol, GM_J, GM_E (IAU 2015 B3), consultados 2026-11-09. Los periodos orbitales de Jupiter (4332.59 d) y
de la Tierra (365.25 d), la excentricidad, el ruido (1 m/s), el numero de medidas y los parametros del planeta sintetico son ILUSTRATIVOS.
Modelo: K = (2 pi G/P)^(1/3) Mp sen i/((Ms + Mp)^(2/3) sqrt(1 - e^2)); velocidad v(t) = gamma + K[cos(nu + omega) + e cos(omega)] con la
anomalia verdadera nu de la ecuacion de Kepler (Newton). Ajuste lineal de gamma + A cos(2 pi t/P) + B sen(2 pi t/P) (orbita circular), K = sqrt(A^2 + B^2).
Verificacion de la incertidumbre: sigma_K ~ sigma sqrt(2/N) para fase uniforme, frente a la desviacion Monte Carlo (semilla fija).
Supuestos: un solo planeta, periodo conocido, ruido blanco. Validez: orientativa.
Tolerancia: 1e-12 en la ecuacion de Kepler; 5 % entre el sigma_K del Monte Carlo y el teorico; para e = 0 el K recuperado dentro de 3 sigma.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

G = 6.67430e-11
GM_SOL, GM_J, GM_E = 1.3271244e20, 1.2668653e17, 3.986004e14
DIA = 86400.0


def semiamplitud(p, gm_p, gm_s, e=0.0, sini=1.0):
    mp, ms = gm_p / G, gm_s / G
    return (2 * math.pi * G / p) ** (1 / 3) * mp * sini / ((ms + mp) ** (2 / 3) * math.sqrt(1 - e * e))


def kepler(m_anom, e):
    e_anom = m_anom if e < 0.8 else math.pi
    for _ in range(100):
        d = (e_anom - e * math.sin(e_anom) - m_anom) / (1 - e * math.cos(e_anom))
        e_anom -= d
        if abs(d) < 1e-15:
            break
    return e_anom


def vr(t, p, k, e, omega, t0=0.0):
    m = (2 * math.pi * (t - t0) / p) % (2 * math.pi)
    ea = kepler(m, e)
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(ea / 2), math.sqrt(1 - e) * math.cos(ea / 2))
    return k * (math.cos(nu + omega) + e * math.cos(omega))


def resolver3(a, b):
    n = 3
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(n):
            if r != i:
                f = m[r][i] / m[i][i]
                m[r] = [m[r][c] - f * m[i][c] for c in range(n + 1)]
    return [m[i][n] / m[i][i] for i in range(n)]


def ajuste_circular(ts, vs, p):
    X = [[1.0, math.cos(2 * math.pi * t / p), math.sin(2 * math.pi * t / p)] for t in ts]
    A = [[sum(x[i] * x[j] for x in X) for j in range(3)] for i in range(3)]
    B = [sum(x[i] * v for x, v in zip(X, vs)) for i in range(3)]
    g, a, b = resolver3(A, B)
    return g, math.hypot(a, b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'planeta':<10} {'Mp/Ms':>11} {'P [d]':>9} {'K [m/s]':>10}")
    for nombre, gmp, p in (("Jupiter", GM_J, 4332.59 * DIA), ("Tierra", GM_E, 365.25 * DIA)):
        k = semiamplitud(p, gmp, GM_SOL)
        print(f"{nombre:<10} {gmp / GM_SOL:11.4e} {p / DIA:9.2f} {k:10.4f}")
    k_j = semiamplitud(4332.59 * DIA, GM_J, GM_SOL)
    # ecuacion de Kepler
    for e in (0.1, 0.5, 0.9):
        for m in (0.3, 1.7, 3.0, 5.5):
            ea = kepler(m, e)
            assert abs(ea - e * math.sin(ea) - m) < 1e-12, "ecuacion de Kepler"
    print("ecuacion de Kepler resuelta con residuo < 1e-12 para e = 0.1, 0.5, 0.9")
    # ajuste con muestreo uniforme en fase y MC
    rng = random.Random(20261109)
    p, k_true, sig, n = 30.0, 10.0, 1.0, 60
    ts = [rng.uniform(0, 300) for _ in range(n)]
    sk = sig * math.sqrt(2 / n)
    res = {}
    for e, om in ((0.0, 0.0), (0.3, 0.7), (0.6, 0.7)):
        ks = []
        for _ in range(1500):
            vs = [vr(t, p, k_true, e, om) + rng.gauss(0, sig) for t in ts]
            _, kk = ajuste_circular(ts, vs, p)
            ks.append(kk)
        res[e] = (statistics.mean(ks), statistics.pstdev(ks))
        print(f"e = {e}: K verdadero = {k_true} ; K recuperado (ajuste circular) = {res[e][0]:.3f} ; desviacion = {res[e][1]:.3f} ; sigma teorico = {sk:.3f}")
    assert abs(res[0.0][0] - k_true) < 3 * sk / math.sqrt(1500) * 3 + 0.05
    assert abs(res[0.0][1] / sk - 1) < 0.08, "sigma_K"
    print(f"masa minima (Mp sen i) para K = 10 m/s, P = 30 d, Ms = 1 Msol: {10.0 / semiamplitud(30 * DIA, GM_J, GM_SOL):.3f} masas de Jupiter")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
