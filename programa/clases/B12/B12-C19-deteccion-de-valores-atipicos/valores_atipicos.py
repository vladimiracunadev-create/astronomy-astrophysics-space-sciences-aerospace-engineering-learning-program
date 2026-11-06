#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C19: deteccion de valores atipicos.

Datos: SINTETICOS. 10 lecturas de distancia (m) ~ N(150, 3^2) con semilla
1919, a las que se les agrega un atipico de +15 m (ILUSTRATIVO); caso de
enmascaramiento con dos atipicos; caso bivariado con correlacion 0.8.
Modelo: estadistico de Grubbs G = max|x - media|/s con valor critico
G_c = (N-1)/sqrt(N) * sqrt(t^2/(N-2+t^2)), t = t_{alfa/(2N), N-2}
(NIST/SEMATECH e-Handbook 1.3.5.17.1); puntaje z modificado con MAD
(M = 0.6745 (x - mediana)/MAD, umbral convencional 3.5); distancia de
Mahalanobis al cuadrado frente a chi^2 con 2 gl.
Supuestos: datos limpios normales; para Grubbs, un solo atipico.
Validez: Grubbs no detecta bien dos atipicos (enmascaramiento).
Tolerancia: la tasa de falsos positivos de Grubbs bajo H0 entre 0.040 y
0.052 (R = 200 000); Mahalanobis exacto frente a chi^2. Las pruebas
detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")


def grubbs_crit(N, alpha=0.05):
    t = stats.t.ppf(1 - alpha / (2 * N), N - 2)
    return (N - 1) / math.sqrt(N) * math.sqrt(t**2 / (N - 2 + t**2))


def G(x):
    return np.max(np.abs(x - x.mean())) / x.std(ddof=1)


def mod_z(x):
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    return 0.6745 * (x - med) / mad


rng = np.random.default_rng(1919)
x = rng.normal(150.0, 3.0, 10)
xo = x.copy()
xo[3] += 15.0
print("lecturas:", np.round(xo, 2).tolist())
Gc = grubbs_crit(10)
print(f"G_critico (N=10, alfa=0.05, bilateral) = {Gc:.4f}")
print(f"G sin atipico = {G(x):.4f}; G con atipico = {G(xo):.4f}; marca el indice {int(np.argmax(np.abs(xo - xo.mean())))}")
assert G(xo) > Gc
print("puntaje z modificado (|M| > 3.5):", np.round(mod_z(xo), 2).tolist())
assert np.argmax(np.abs(mod_z(xo))) == 3 and abs(mod_z(xo)[3]) > 3.5

# falsos positivos de Grubbs bajo H0
R = 200_000
d = rng.normal(0, 1, (R, 10))
g = np.max(np.abs(d - d.mean(axis=1, keepdims=True)), axis=1) / d.std(axis=1, ddof=1)
fp = float(np.mean(g > Gc))
print(f"tasa de falsos positivos de Grubbs bajo H0 = {fp:.4f} (nominal 0.05)")
assert 0.040 <= fp <= 0.052

# enmascaramiento: dos atipicos
xm = x.copy()
xm[2] += 15.0
xm[7] += 16.0
print(f"dos atipicos: G = {G(xm):.4f} (critico {Gc:.4f}) -> {'detecta' if G(xm) > Gc else 'NO detecta'}; |M|>3.5 marca {int(np.sum(np.abs(mod_z(xm)) > 3.5))} puntos")
assert G(xm) < Gc and np.sum(np.abs(mod_z(xm)) > 3.5) == 2

# Mahalanobis bivariado
P = np.array([[9.0, 9.6], [9.6, 16.0]])
Pi = np.linalg.inv(P)
e = np.array([3.0, -4.0])
d2 = float(e @ Pi @ e)
print(f"punto (3, -4): |x|/sx = 1.00, |y|/sy = 1.00 (normal por separado) pero d^2 = {d2:.2f} > chi2(0.99; 2) = {stats.chi2.ppf(0.99, 2):.2f}")
assert d2 > stats.chi2.ppf(0.99, 2)
assert abs(stats.chi2.sf(d2, 2) - math.exp(-d2 / 2)) < 1e-12
print("Pruebas superadas.")
