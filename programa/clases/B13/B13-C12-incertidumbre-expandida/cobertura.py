#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C12: incertidumbre expandida y cobertura real.

Datos: SINTETICOS. Un telemetro mide una distancia verdadera de 1000.000 m con
ruido gaussiano sigma = 0.050 m (semilla fija).
Modelo (GUM 6.2, G.3): U = k u_c. Con sigma conocida y normalidad, el
intervalo x +/- k sigma cubre erf(k/sqrt(2)): 68.27 %, 95.45 %, 99.73 % para
k = 1, 2, 3. Con n lecturas y u = s/sqrt(n) estimada de los datos, el factor
k = 2 cubre menos que 95.45 % porque s fluctua: la cobertura sigue una t de
Student con nu = n-1 grados de libertad. Solucion exacta para nu = 2:
P(|t| < x) = x / sqrt(2 + x^2), que da P = 0.8165 para x = 2 y exige
x = 4.303 para P = 0.95.
Supuestos: ruido gaussiano independiente. Tolerancia: la cobertura simulada
coincide con la teorica dentro de 5 errores tipicos binomiales.
"""
from __future__ import annotations
import math
import platform
import random
import sys

VERDAD, SIGMA = 1000.000, 0.050


def cobertura_normal(k: float) -> float:
    return math.erf(k / math.sqrt(2.0))


def cobertura_t2(x: float) -> float:
    return x / math.sqrt(2.0 + x * x)


def simular(n, k, R, rng):
    dentro = 0
    for _ in range(R):
        x = [VERDAD + rng.gauss(0, SIGMA) for _ in range(n)]
        m = sum(x) / n
        s = math.sqrt(sum((v - m) ** 2 for v in x) / (n - 1))
        u = s / math.sqrt(n)
        if abs(m - VERDAD) <= k * u:
            dentro += 1
    return dentro / R


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(2026)
    # 1) sigma conocida
    print("k   cobertura normal (exacta)")
    for k in (1, 2, 3):
        c = cobertura_normal(k)
        print(f"{k}   {c:.4f}")
    assert abs(cobertura_normal(2) - 0.9545) < 5e-5
    R = 20000
    sim = sum(abs(rng.gauss(0, SIGMA)) <= 2 * SIGMA for _ in range(R)) / R
    err = math.sqrt(0.9545 * 0.0455 / R)
    print(f"sigma conocida, k = 2: simulada {sim:.4f}")
    assert abs(sim - cobertura_normal(2)) < 5 * err
    # 2) sigma estimada, n = 3
    teor = cobertura_t2(2.0)
    sim3 = simular(3, 2.0, 40000, rng)
    err3 = math.sqrt(teor * (1 - teor) / 40000)
    print(f"n = 3, k = 2: teorica t(nu=2) = {teor:.4f} ; simulada = {sim3:.4f}")
    assert abs(sim3 - teor) < 5 * err3
    # 3) factor necesario para 95 % con nu = 2
    x95 = math.sqrt(2 * 0.95 ** 2 / (1 - 0.95 ** 2))
    print(f"k para 95 % con nu = 2: {x95:.3f}")
    assert abs(cobertura_t2(x95) - 0.95) < 1e-12 and abs(x95 - 4.303) < 1e-3
    # 4) n grande: k = 2 se acerca a 95.45 %
    sim30 = simular(30, 2.0, 20000, rng)
    print(f"n = 30, k = 2: simulada = {sim30:.4f} (limite normal 0.9545)")
    assert abs(sim30 - 0.9545) < 0.012
    # 5) U para una serie concreta
    x = [VERDAD + rng.gauss(0, SIGMA) for _ in range(10)]
    m = sum(x) / 10
    s = math.sqrt(sum((v - m) ** 2 for v in x) / 9)
    u = s / math.sqrt(10)
    print(f"serie n = 10: media = {m:.4f} m, u = {u:.4f} m, U(k=2) = {2*u:.4f} m")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
