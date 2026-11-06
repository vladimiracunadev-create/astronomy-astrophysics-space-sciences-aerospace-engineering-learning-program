#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C08: intervalos de confianza y cobertura.

Datos: SINTETICOS. 10 mediciones de una distancia verdadera de 150.0 m con
ruido normal de sigma = 3.0 m (ILUSTRATIVO), semilla 8.
Modelo: intervalo t para la media, ybar +/- t_{1-a/2, n-1} s/sqrt(n).
Supuestos: datos independientes y aproximadamente normales.
Validez: n pequeno solo con normalidad razonable.
Tolerancia: el cuantil t se comprueba contra una integracion numerica
independiente de la densidad t (error < 1e-6); la cobertura simulada del
intervalo t debe estar en [0.945, 0.955] (R = 100 000). Detienen la ejecucion.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
rng = np.random.default_rng(8)
y = rng.normal(150.0, 3.0, 10)
n = len(y)
yb, s = y.mean(), y.std(ddof=1)
t = stats.t.ppf(0.975, n - 1)
print(f"media = {yb:.3f} m  s = {s:.3f} m  t(0.975, 9) = {t:.4f}")
lo, hi = yb - t * s / math.sqrt(n), yb + t * s / math.sqrt(n)
print(f"IC 95 % = [{lo:.3f}, {hi:.3f}] m  (semiancho {t*s/math.sqrt(n):.3f} m)")

# comprobacion independiente del cuantil t: integral de la densidad t (Simpson)
def dens_t(x, nu):
    c = math.gamma((nu + 1) / 2) / (math.sqrt(nu * math.pi) * math.gamma(nu / 2))
    return c * (1 + x * x / nu) ** (-(nu + 1) / 2)

m = 200_000
h = 2 * t / m
xs = [-t + i * h for i in range(m + 1)]
integral = h / 3 * (dens_t(xs[0], 9) + dens_t(xs[-1], 9)
                     + 4 * sum(dens_t(xs[i], 9) for i in range(1, m, 2))
                     + 2 * sum(dens_t(xs[i], 9) for i in range(2, m, 2)))
print(f"integral de la densidad t entre +-t = {integral:.6f}")
assert abs(integral - 0.95) < 1e-6

# cobertura
R = 100_000
d = rng.normal(150.0, 3.0, (R, n))
mm, ss = d.mean(axis=1), d.std(axis=1, ddof=1)
cov_t = np.mean(np.abs(mm - 150.0) <= t * ss / math.sqrt(n))
cov_z = np.mean(np.abs(mm - 150.0) <= 1.96 * ss / math.sqrt(n))
cov_known = np.mean(np.abs(mm - 150.0) <= 1.96 * 3.0 / math.sqrt(n))
print(f"cobertura intervalo t = {cov_t:.4f}; con 1.96 y s estimada = {cov_z:.4f}; sigma conocida = {cov_known:.4f}")
assert 0.945 <= cov_t <= 0.955 and 0.945 <= cov_known <= 0.955
assert cov_z < 0.94  # usar 1.96 con n = 10 subcubre

# anchura frente a n (semiancho esperado ~ t s / sqrt(n))
for nn in (4, 10, 40, 160):
    tt = stats.t.ppf(0.975, nn - 1)
    print(f"n={nn:4d}  t={tt:.3f}  semiancho para s=3 m: {tt*3/math.sqrt(nn):.3f} m")
print("Pruebas superadas.")
