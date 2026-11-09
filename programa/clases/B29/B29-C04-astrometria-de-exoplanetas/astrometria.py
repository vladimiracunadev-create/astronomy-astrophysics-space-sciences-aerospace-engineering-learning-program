#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C04: firma astrometrica de un planeta y ajuste de posicion, movimiento propio, paralaje y orbita.

Datos: GM_sol, GM_J, GM_E (IAU 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09; 1 pc = 648000/pi au. Los semiejes de Jupiter (5.2012 au, de
la tercera ley con P = 4332.59 d) y la Tierra (1 au), las distancias, el ruido (0.05 mas), el numero y el calendario de observaciones son ILUSTRATIVOS.
Modelo: firma astrometrica alpha = (Mp/Ms)(a/d) (en radianes con a y d en la misma unidad); modelo en una coordenada
x(t) = x0 + mu t + varpi cos(2 pi t/P_tierra) + A cos(2 pi t/P) + B sen(2 pi t/P); ajuste lineal; covarianza sigma^2 (X^T X)^-1;
comparacion de las desviaciones Monte Carlo (semilla fija) con la raiz de la diagonal de la covarianza.
Supuestos: una coordenada, periodos conocidos, ruido blanco. Validez: orientativa.
Tolerancia: 6 % entre la desviacion Monte Carlo y la raiz de la covarianza para los parametros del planeta.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

GM_SOL, GM_J, GM_E = 1.3271244e20, 1.2668653e17, 3.986004e14
AU = 1.49597870700e11
PC_AU = 648000 / math.pi
MAS_RAD = math.pi / (180 * 3600 * 1000)


def semieje_au(p_dias):
    return (GM_SOL * (p_dias * 86400 / (2 * math.pi)) ** 2) ** (1 / 3) / AU


def firma_mas(gm_p, a_au, d_pc):
    return gm_p / GM_SOL * a_au / (d_pc * PC_AU) / MAS_RAD


def inversa(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        pv = a[i][i]
        a[i] = [x / pv for x in a[i]]
        for r in range(n):
            if r != i:
                f = a[r][i]
                a[r] = [a[r][c] - f * a[i][c] for c in range(2 * n)]
    return [row[n:] for row in a]


def ajustar(X, y):
    n = len(X[0])
    A = [[sum(x[i] * x[j] for x in X) for j in range(n)] for i in range(n)]
    B = [sum(x[i] * v for x, v in zip(X, y)) for i in range(n)]
    Ai = inversa(A)
    return [sum(Ai[i][j] * B[j] for j in range(n)) for i in range(n)], Ai


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a_j = semieje_au(4332.59)
    print(f"semieje de Jupiter (tercera ley) = {a_j:.4f} au")
    print(f"{'planeta':<9} {'a [au]':>8} {'d [pc]':>7} {'firma [mas]':>12} {'firma [uas]':>12}")
    for nombre, gmp, a in (("Jupiter", GM_J, a_j), ("Tierra", GM_E, 1.0)):
        for d in (10.0, 100.0):
            f = firma_mas(gmp, a, d)
            print(f"{nombre:<9} {a:8.4f} {d:7.1f} {f:12.4e} {f * 1000:12.4f}")
    # ajuste
    rng = random.Random(20261109)
    p_pl, p_t = 600.0, 365.25
    sig, n = 0.05, 80
    ts = sorted(rng.uniform(0, 1800) for _ in range(n))
    x0, mu, varpi, A, B = 1.0, 0.3 / 365.25, 100.0, 0.4, -0.3
    X = [[1.0, t, math.cos(2 * math.pi * t / p_t), math.cos(2 * math.pi * t / p_pl), math.sin(2 * math.pi * t / p_pl)] for t in ts]
    cov = inversa([[sum(x[i] * x[j] for x in X) for j in range(5)] for i in range(5)])
    sig_teo = [sig * math.sqrt(cov[i][i]) for i in range(5)]
    res = []
    for _ in range(3000):
        y = [x0 + mu * t + varpi * x[2] + A * x[3] + B * x[4] + rng.gauss(0, sig) for x, t in zip(X, ts)]
        coef, _ = ajustar(X, y)
        res.append(coef)
    nombres = ["x0 [mas]", "mu [mas/d]", "paralaje [mas]", "A [mas]", "B [mas]"]
    verd = [x0, mu, varpi, A, B]
    print(f"{'parametro':<15} {'verdadero':>11} {'media MC':>11} {'sigma MC':>10} {'sigma teorico':>14}")
    for i in range(5):
        col = [r[i] for r in res]
        m, s = statistics.mean(col), statistics.pstdev(col)
        print(f"{nombres[i]:<15} {verd[i]:11.5f} {m:11.5f} {s:10.5f} {sig_teo[i]:14.5f}")
        assert abs(s / sig_teo[i] - 1) < 0.06, nombres[i]
    amp = math.hypot(A, B)
    print(f"amplitud orbital verdadera = {amp:.3f} mas ; error de A = {sig_teo[3]:.4f} mas -> significancia de la orbita ~ {amp / sig_teo[3]:.1f} sigma")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
