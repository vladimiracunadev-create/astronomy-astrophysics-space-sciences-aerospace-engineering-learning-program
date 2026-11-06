#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C03: binomial, Poisson, exponencial y normal.

Datos: SINTETICOS. Detector con tasa media de 4.0 eventos por intervalo de
10 min (lambda = 4.0, ILUSTRATIVO).
Modelo: N ~ Poisson(lambda); tiempo entre eventos T ~ Exponencial(tasa 0.4/min);
ruido de medicion normal.
Supuestos: eventos independientes y de tasa constante (proceso de Poisson).
Validez: tasa constante; fuera de eso (rafagas) el modelo falla.
Tolerancia: pruebas exactas en coma flotante a 1e-12; frente a simulacion,
|diferencia| < 3e-3 con N = 1 000 000 y semilla fija. Las pruebas detienen
la ejecucion si fallan.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
lam = 4.0
pois = lambda k: math.exp(-lam) * lam**k / math.factorial(k)
print(f"P(N=0)={pois(0):.6f}  P(N=4)={pois(4):.6f}  P(N>=8)={1-sum(pois(k) for k in range(8)):.6f}")
assert abs(sum(pois(k) for k in range(100)) - 1) < 1e-12
mean = sum(k * pois(k) for k in range(100))
var = sum((k - mean) ** 2 * pois(k) for k in range(100))
assert abs(mean - lam) < 1e-12 and abs(var - lam) < 1e-12

# Poisson como limite de la binomial
n, p = 1000, lam / 1000
binom = lambda k: math.comb(n, k) * p**k * (1 - p) ** (n - k)
print(f"Binomial(1000, 0.004) P(4) = {binom(4):.6f} frente a Poisson {pois(4):.6f}")
assert abs(binom(4) - pois(4)) < 1e-3

# exponencial: P(T > t) = exp(-r t); sin memoria
r = 0.4
S = lambda t: math.exp(-r * t)
assert abs(S(5 + 3) / S(5) - S(3)) < 1e-12
print(f"P(T>3 min) = {S(3):.6f}")

# normal: fracciones dentro de k sigma via erf
for k in (1, 2, 3):
    print(f"P(|Z|<{k}) = {math.erf(k / math.sqrt(2)):.6f}")
assert abs(math.erf(1 / math.sqrt(2)) - 0.682689492137086) < 1e-12

rng = np.random.default_rng(7)
N = 1_000_000
s = rng.poisson(lam, N)
print(f"simulacion Poisson: P(N=4)={np.mean(s==4):.5f}  media={s.mean():.4f}  var={s.var():.4f}")
assert abs(np.mean(s == 4) - pois(4)) < 3e-3
t = rng.exponential(1 / r, N)
print(f"simulacion exponencial: P(T>3)={np.mean(t>3):.5f} frente a {S(3):.5f}")
assert abs(np.mean(t > 3) - S(3)) < 3e-3
z = rng.standard_normal(N)
print(f"simulacion normal: P(|Z|<2)={np.mean(abs(z)<2):.5f}")
assert abs(np.mean(abs(z) < 2) - math.erf(2 / math.sqrt(2))) < 3e-3
print("Pruebas superadas.")
