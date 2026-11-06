#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C14: simulacion Monte Carlo y su error.

Datos: SINTETICOS. Error de posicion relativa de dos objetos en el plano de
encuentro: componentes x e y independientes, normales de media cero y
sigma = 100 m (ILUSTRATIVO). Evento: distancia de paso < R = 50 m.
Modelo: distancia ~ Rayleigh(sigma); P(d < R) = 1 - exp(-R^2/(2 sigma^2)).
Segundo problema: I = integral_0^pi sin(x) dx = 2 por media de muestras.
Supuestos: independencia, normalidad, sigma conocida.
Validez: modelo didactico; no es un analisis de colision real.
Tolerancia: error absoluto menor que 4 desviaciones del estimador teorico;
la desviacion observada de 400 replicas dentro de 15 % de la teorica
sqrt(p(1-p)/N); semilla fija. Las pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
sigma, R = 100.0, 50.0
p_exact = 1 - math.exp(-R**2 / (2 * sigma**2))
print(f"P(d < {R:.0f} m) exacta (Rayleigh) = {p_exact:.6f}")
rng = np.random.default_rng(1414)

print("       N    estimacion   error      desv. teorica sqrt(p(1-p)/N)")
for N in (10**3, 10**4, 10**5, 10**6):
    xy = rng.normal(0.0, sigma, (N, 2))
    d = np.hypot(xy[:, 0], xy[:, 1])
    p_hat = float(np.mean(d < R))
    se = math.sqrt(p_exact * (1 - p_exact) / N)
    print(f"{N:8d}    {p_hat:.6f}   {p_hat - p_exact:+.6f}   {se:.6f}")
    assert abs(p_hat - p_exact) < 4 * se

# desviacion del estimador sobre 400 replicas con N = 10 000
N, reps = 10_000, 400
est = np.array([np.mean(np.hypot(*rng.normal(0, sigma, (2, N))) < R) for _ in range(reps)])
se_t = math.sqrt(p_exact * (1 - p_exact) / N)
print(f"N={N}: desviacion observada de {reps} replicas = {est.std():.6f}; teorica = {se_t:.6f}")
assert abs(est.std() / se_t - 1) < 0.15
print(f"cada 100 veces mas muestras reducen el error 10 veces: {math.sqrt(100):.0f}x")

# integral por Monte Carlo
for N in (10**3, 10**5):
    x = rng.random(N) * math.pi
    est_i = math.pi * np.mean(np.sin(x))
    se_i = math.pi * math.sqrt(0.5 - (2 / math.pi) ** 2) / math.sqrt(N)
    print(f"integral N={N:6d}: {est_i:.5f} (exacta 2); desv. teorica {se_i:.5f}")
    assert abs(est_i - 2.0) < 4 * se_i

# numero de muestras para un error relativo del 1 % en p
n_need = (1 - p_exact) / (p_exact * 0.01**2)
print(f"muestras para error relativo de 1 % en p = {p_exact:.4f}: N = {n_need:,.0f}")
print("Pruebas superadas.")
