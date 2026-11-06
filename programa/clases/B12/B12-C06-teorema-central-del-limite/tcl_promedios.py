#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C06: teorema central del limite con promedios.

Datos: SINTETICOS. Errores uniformes en [0, 1] (media 1/2, varianza 1/12) y,
como contraejemplo, errores de Cauchy (sin media ni varianza).
Modelo: media de n variables independientes de igual distribucion.
Supuestos: independencia, varianza finita (solo para el caso uniforme).
Validez: n moderado a grande; para colas pesadas el teorema no se aplica.
Tolerancia: pruebas exactas por formula (Irwin-Hall n=2); desviacion de la
media = sigma/sqrt(n) dentro de 1 %; distancia maxima entre la acumulada
empirica y la normal (Kolmogorov-Smirnov) decreciente con n y menor que 0.01
para n = 30 con 200 000 repeticiones; semilla fija. Detienen la ejecucion.
"""
import platform

import numpy as np
from scipy.special import ndtr

import scipy

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
rng = np.random.default_rng(2025)
R = 200_000
sigma = (1 / 12) ** 0.5

# prueba exacta: la suma de 2 uniformes tiene P(S <= 0.5) = 0.5**2 / 2 = 0.125
s2 = rng.random((1_000_000, 2)).sum(axis=1)
print(f"P(U1+U2 <= 0.5) simulada = {np.mean(s2 <= 0.5):.4f} (exacta 0.1250)")
assert abs(np.mean(s2 <= 0.5) - 0.125) < 2e-3

print("  n   desv.media  sigma/sqrt(n)  asimetria  KS vs normal")
ks_prev = 1.0
for n in (1, 2, 5, 30):
    m = rng.random((R, n)).mean(axis=1)
    sd = m.std()
    z = np.sort((m - 0.5) / (sigma / n**0.5))
    emp = np.arange(1, R + 1) / R
    ks = float(np.max(np.abs(emp - ndtr(z))))
    sk = float(np.mean(((m - m.mean()) / sd) ** 3))
    print(f"{n:3d}   {sd:.5f}     {sigma/n**0.5:.5f}     {sk:+.4f}     {ks:.4f}")
    assert abs(sd - sigma / n**0.5) / (sigma / n**0.5) < 0.01
    assert ks < ks_prev + 1e-3
    ks_prev = ks
assert ks < 0.01

# contraejemplo: la media de n Cauchy tiene la misma dispersion que una sola
c1 = rng.standard_cauchy(R)
c100 = rng.standard_cauchy((R, 100)).mean(axis=1)
iqr = lambda a: float(np.subtract(*np.percentile(a, [75, 25])))
print(f"Cauchy: IQR de 1 dato = {iqr(c1):.3f}; IQR de la media de 100 = {iqr(c100):.3f} (no baja)")
assert abs(iqr(c100) - iqr(c1)) / iqr(c1) < 0.05
print("Pruebas superadas.")
