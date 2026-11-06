#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C04: esperanza, varianza y propiedades.

Datos: SINTETICOS. Dos medidas de distancia (en m) de una sonda con errores
independientes de desviacion tipica 3.0 m y 4.0 m (ILUSTRATIVO).
Modelo: X = numero de computadores operativos (C02); errores normales de
media cero. E[aX+b] = aE[X]+b; Var(X+Y) = Var X + Var Y si independientes;
desigualdad de Chebyshev.
Supuestos: independencia, varianzas finitas. Validez: ilustrativo.
Tolerancia: pruebas exactas con fracciones; simulacion con |dif| < 0.15 m^2
en la varianza de la suma (N = 1 000 000, semilla fija). Detienen la
ejecucion si fallan.
"""
import platform
from fractions import Fraction
from math import comb

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
p = Fraction(9, 10)
pmf = {k: comb(3, k) * p**k * (1 - p) ** (3 - k) for k in range(4)}
EX = sum(k * v for k, v in pmf.items())
EX2 = sum(k * k * v for k, v in pmf.items())
VX = EX2 - EX**2
print(f"E[X] = {EX} = {float(EX)}   Var(X) = {VX} = {float(VX)}")
assert EX == 3 * p and VX == 3 * p * (1 - p)  # binomial: np, np(1-p)
EY = sum((2 * k + 1) * v for k, v in pmf.items())
VY = sum((2 * k + 1 - EY) ** 2 * v for k, v in pmf.items())
assert EY == 2 * EX + 1 and VY == 4 * VX
print(f"Y=2X+1: E={float(EY)}  Var={float(VY):.4f}")

s1, s2 = 3.0, 4.0
sigma_suma = (s1**2 + s2**2) ** 0.5
print(f"sigma de la suma = {sigma_suma} m (Pitagoras de las desviaciones)")
assert sigma_suma == 5.0
rng = np.random.default_rng(99)
N = 1_000_000
e1, e2 = rng.normal(0, s1, N), rng.normal(0, s2, N)
v = np.var(e1 + e2)
print(f"varianza simulada de la suma = {v:.3f} m^2 (exacta 25)")
assert abs(v - 25) < 0.15
n = 9
m = rng.normal(0, 3.0, (200_000, n)).mean(axis=1)
print(f"desviacion de la media de {n} medidas = {m.std():.4f} (exacta {3.0/3:.4f})")
assert abs(m.std() - 1.0) < 0.01

x = rng.exponential(1.0, N)
for k in (2, 3):
    fr = np.mean(abs(x - 1.0) >= k)
    print(f"Chebyshev k={k}: frecuencia {fr:.4f} <= cota {1/k**2:.4f}")
    assert fr <= 1 / k**2
print("Pruebas superadas.")
