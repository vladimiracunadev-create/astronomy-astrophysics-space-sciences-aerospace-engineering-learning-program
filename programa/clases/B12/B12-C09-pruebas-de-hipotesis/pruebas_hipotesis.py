#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C09: pruebas de hipotesis, error tipo I y potencia.

Datos: (a) OBSERVADOS/ESTIMADOS publicados: H0 = 67.4 +/- 0.5 km/s/Mpc
(Planck 2018, arXiv:1807.06209) y H0 = 73.04 +/- 1.04 km/s/Mpc (Riess et al.,
arXiv:2112.04510), consultados el 2026-11-05. (b) SINTETICOS para las
simulaciones (media 0, sigma 1; efecto delta = 1 m con sigma = 3 m, n = 25).
Modelo: prueba z de la diferencia de dos estimaciones independientes y
normales; prueba t de una muestra; potencia de la prueba z bilateral.
Supuestos: normalidad y independencia de las dos estimaciones (aproximacion
didactica; no es un analisis cosmologico).
Validez: solo la aritmetica de la prueba, no la interpretacion fisica tension.
Tolerancia: tasa de error tipo I en [0.046, 0.054]; potencia simulada a menos
de 0.01 de la teorica (R = 200 000, semilla fija). Detienen la ejecucion.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")

# (a) tension de Hubble (aritmetica)
h1, s1 = 67.4, 0.5
h2, s2 = 73.04, 1.04
se = math.hypot(s1, s2)
z = (h2 - h1) / se
p = math.erfc(abs(z) / math.sqrt(2))
print(f"diferencia = {h2-h1:.2f}; error tipico de la diferencia = {se:.4f}; z = {z:.3f}; p bilateral = {p:.2e}")
assert abs(z - 4.887) < 0.01
assert abs(p - 2 * stats.norm.sf(z)) < 1e-12  # comprobacion independiente

# (b) error tipo I de la prueba t de una muestra, H0 verdadera
rng = np.random.default_rng(909)
R, n = 200_000, 10
x = rng.normal(0.0, 1.0, (R, n))
tstat = x.mean(axis=1) / (x.std(axis=1, ddof=1) / math.sqrt(n))
tc = stats.t.ppf(0.975, n - 1)
alpha_hat = float(np.mean(np.abs(tstat) > tc))
print(f"error tipo I simulado = {alpha_hat:.4f} (nominal 0.05, n = {n}, tcrit = {tc:.4f})")
assert 0.046 <= alpha_hat <= 0.054

# (c) potencia de la prueba z bilateral
delta, sigma, n2 = 1.0, 3.0, 25
ncp = delta * math.sqrt(n2) / sigma
power = stats.norm.sf(1.96 - ncp) + stats.norm.cdf(-1.96 - ncp)
y = rng.normal(delta, sigma, (R, n2)).mean(axis=1)
zs = y / (sigma / math.sqrt(n2))
power_sim = float(np.mean(np.abs(zs) > 1.96))
print(f"potencia teorica = {power:.4f}; simulada = {power_sim:.4f} (delta={delta} m, sigma={sigma} m, n={n2})")
assert abs(power - power_sim) < 0.01
# tamano de muestra para potencia 0.80
n80 = ((1.96 + stats.norm.ppf(0.80)) * sigma / delta) ** 2
print(f"n para potencia 0.80 (aprox. normal) = {n80:.1f} -> {math.ceil(n80)}")

# (d) pruebas multiples: 20 pruebas independientes con H0 verdadera
k = 20
fwe = 1 - 0.95**k
sim = float(np.mean((rng.random((R, k)) < 0.05).any(axis=1)))
print(f"P(al menos un falso positivo en {k} pruebas) = {fwe:.4f}; simulada = {sim:.4f}; con Bonferroni (alpha/k): {1 - (1 - 0.05/k)**k:.4f}")
assert abs(fwe - sim) < 0.01
print("Pruebas superadas.")
