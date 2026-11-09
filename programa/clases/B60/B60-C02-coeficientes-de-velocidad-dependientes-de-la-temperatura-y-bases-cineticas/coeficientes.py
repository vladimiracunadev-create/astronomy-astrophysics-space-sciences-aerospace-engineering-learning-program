#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B60-C02: coeficiente k(T) = alpha (T/300)^beta exp(-gamma/T) y su ajuste.

Datos: SINTETICOS. Los parametros (alpha, beta, gamma) de las tres reacciones de ejemplo son ILUSTRATIVOS:
no se tomaron de KIDA ni de UMIST (sus tablas no se consultaron) y no corresponden a ninguna reaccion real.
Modelo: evaluacion de la forma de Arrhenius modificada (tipo Kooij) y ajuste por minimos cuadrados lineales de
ln k = ln alpha + beta ln(T/300) - gamma/T con ruido lognormal de semilla fija (60002).
Unidades: k en cm^3 s^-1 (bimolecular), T en K, gamma en K, alpha en cm^3 s^-1.
Supuestos: ajuste valido solo en el intervalo de temperatura de los datos; se declara el error al extrapolar.
Tolerancias: sin ruido, el ajuste recupera los parametros con error relativo < 1e-9; con ruido de 5 %, ln k ajustado
dentro del intervalo con error < 6 % (media). Biblioteca estandar de Python.
"""
from __future__ import annotations
import math, platform, random


def k_kooij(T, alpha, beta, gamma):
    return alpha * (T / 300.0) ** beta * math.exp(-gamma / T)


def resolver(A, b):
    n = len(b)
    M = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][c] * x[c] for c in range(i + 1, n))) / M[i][i]
    return x


def ajustar(Ts, ks, usa_gamma=True):
    """Minimos cuadrados en ln k. Columnas: [1, ln(T/300), -1/T] (la ultima solo si usa_gamma)."""
    cols = [lambda T: 1.0, lambda T: math.log(T / 300.0)] + ([lambda T: -1.0 / T] if usa_gamma else [])
    n = len(cols)
    X = [[c(T) for c in cols] for T in Ts]
    y = [math.log(k) for k in ks]
    AtA = [[sum(X[r][i] * X[r][j] for r in range(len(Ts))) for j in range(n)] for i in range(n)]
    Aty = [sum(X[r][i] * y[r] for r in range(len(Ts))) for i in range(n)]
    p = resolver(AtA, Aty)
    return math.exp(p[0]), p[1], (p[2] if usa_gamma else 0.0)


REACCIONES = {  # ILUSTRATIVAS
    "A (sin barrera, beta<0)": (2.0e-9, -0.5, 0.0),
    "B (con barrera)": (1.0e-10, 0.0, 800.0),
    "C (mixta)": (5.0e-11, 1.2, 200.0),
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Parametros ILUSTRATIVOS (no son de KIDA ni de UMIST)")
    print("\nEvaluacion k(T) [cm3/s]:")
    print("  reaccion                    T=10 K        T=100 K       T=300 K")
    for nombre, (a, b, g) in REACCIONES.items():
        print(f"  {nombre:<22} {k_kooij(10.0, a, b, g):12.3e} {k_kooij(100.0, a, b, g):12.3e} {k_kooij(300.0, a, b, g):12.3e}")
    Ts = [100.0 + 20.0 * i for i in range(11)]  # 100-300 K
    peor = 0.0
    for nombre, (a, b, g) in REACCIONES.items():
        ks = [k_kooij(T, a, b, g) for T in Ts]
        usa = g != 0.0
        a2, b2, g2 = ajustar(Ts, ks, usa)
        peor = max(peor, abs(a2 / a - 1), abs(b2 - b) / max(1.0, abs(b)), abs(g2 - g) / max(1.0, g))
    print(f"\nAjuste sin ruido (100-300 K): maximo error relativo en los parametros = {peor:.1e}")
    rng = random.Random(60002)
    a, b, g = REACCIONES["C (mixta)"]
    ks = [k_kooij(T, a, b, g) * math.exp(rng.gauss(0, 0.05)) for T in Ts]
    a2, b2, g2 = ajustar(Ts, ks)
    print(f"\nReaccion C con ruido lognormal de 5 % (SINTETICO):")
    print(f"  verdadero   alpha = {a:.3e}  beta = {b:.3f}  gamma = {g:.1f} K")
    print(f"  ajustado    alpha = {a2:.3e}  beta = {b2:.3f}  gamma = {g2:.1f} K")
    err_in = sum(abs(k_kooij(T, a2, b2, g2) / k_kooij(T, a, b, g) - 1) for T in Ts) / len(Ts)
    print(f"  error medio dentro del intervalo = {err_in:.2%}")
    print("  extrapolacion fuera del intervalo ajustado:")
    print("    T [K]   k_verdadero      k_ajustado      cociente")
    for T in (10.0, 30.0, 60.0, 400.0):
        kt, ka = k_kooij(T, a, b, g), k_kooij(T, a2, b2, g2)
        print(f"    {T:5.0f}   {kt:12.3e}   {ka:12.3e}   {ka / kt:8.3f}")
    print("\nSin termino de barrera ajustado a la reaccion B (modelo equivocado, 100-300 K):")
    aB, bB, gB = REACCIONES["B (con barrera)"]
    ksB = [k_kooij(T, aB, bB, gB) for T in Ts]
    a3, b3, _ = ajustar(Ts, ksB, usa_gamma=False)
    for T in (30.0, 100.0, 300.0):
        print(f"  T = {T:5.0f} K: cociente ajustado/verdadero = {k_kooij(T, a3, b3, 0.0) / k_kooij(T, aB, bB, gB):.3g}")
    assert peor < 1e-9 and err_in < 0.06
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
