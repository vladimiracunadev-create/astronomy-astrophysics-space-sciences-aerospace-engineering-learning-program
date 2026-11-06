#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C02: variables aleatorias discreta y continua.

Datos: SINTETICOS. (a) X = numero de computadores que funcionan de 3
(p = 0.9, ILUSTRATIVO). (b) Y = error de una medicion de distancia, uniforme
en [-2, 2] m (ILUSTRATIVO).
Modelo: (a) pmf binomial B(3, 0.9); (b) densidad uniforme f(y) = 1/4.
Supuestos: independencia en (a); error sin sesgo en (b).
Validez: solo ilustracion de definiciones. Tolerancia: pruebas exactas con
fracciones; para la simulacion |frecuencia - probabilidad| < 2e-3 con
N = 1 000 000 y semilla fija. Las pruebas detienen la ejecucion si fallan.
"""
import platform
from fractions import Fraction
from math import comb

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
p = Fraction(9, 10)
pmf = {k: comb(3, k) * p**k * (1 - p) ** (3 - k) for k in range(4)}
for k, v in pmf.items():
    print(f"P(X={k}) = {float(v):.6f}")
assert sum(pmf.values()) == 1
cdf = {k: sum(pmf[j] for j in range(k + 1)) for k in range(4)}
print("F(0..3) =", " ".join(f"{float(cdf[k]):.6f}" for k in range(4)))
assert cdf[3] == 1
assert pmf[2] + pmf[3] == Fraction(972, 1000)  # coincide con C01
assert 1 - cdf[1] == pmf[2] + pmf[3]  # P(X>=2) = 1 - F(1)

# continua: F(y) = (y + 2)/4 en [-2, 2]
F = lambda y: min(max((y + 2) / 4, 0.0), 1.0)
print(f"P(-1 < Y <= 0.5) = {F(0.5) - F(-1):.4f}")
assert abs((F(0.5) - F(-1)) - 0.375) < 1e-12
print(f"P(Y = 0) = 0 (un punto); mediana = {-2 + 4 * 0.5}; cuantil 0.95 = {-2 + 4 * 0.95}")

rng = np.random.default_rng(2024)
N = 1_000_000
y = rng.uniform(-2, 2, N)
frec = np.mean((y > -1) & (y <= 0.5))
print(f"frecuencia simulada: {frec:.5f}")
assert abs(frec - 0.375) < 2e-3
x = rng.binomial(3, 0.9, N)
print(f"P(X=2) simulada {np.mean(x==2):.5f} frente a exacta {float(pmf[2]):.5f}")
assert abs(np.mean(x == 2) - float(pmf[2])) < 2e-3
print("Pruebas superadas.")
