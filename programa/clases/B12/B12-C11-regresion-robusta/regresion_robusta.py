#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C11: regresion robusta frente a valores atipicos.

Datos: SINTETICOS. Residuo de rango (m) frente al tiempo: y = 5.0 + 0.40 t
con ruido normal sigma = 0.3 m, t = 0..19 s, y 3 valores atipicos grandes
(-9, +8, +10 m) en t = 1, 17, 19 (ILUSTRATIVO).
Modelo: OLS, mediana de pendientes por pares (Theil-Sen) y M-estimador de
Huber por minimos cuadrados reponderados iterativos (IRLS) con constante
k = 1.345 s (s = MAD/0.6745).
Supuestos: ruido simetrico, minoria de atipicos.
Validez: hasta ~29 % de contaminacion (Theil-Sen); Huber con atipicos en y.
Tolerancia: sin atipicos OLS = Huber con k grande (1e-9); con atipicos el
error de pendiente de Theil-Sen y Huber < 0.04 frente a OLS > 0.3; la
eficiencia relativa de la mediana frente a la media en datos normales
= sqrt(pi/2) = 1.2533 dentro de 0.02 (R = 100 000). Detienen la ejecucion.
"""
import itertools
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
rng = np.random.default_rng(1111)
t = np.arange(20.0)
a0, b0 = 5.0, 0.40
y_limpio = a0 + b0 * t + rng.normal(0, 0.3, t.size)
y = y_limpio.copy()
for i, d in zip((1, 17, 19), (-9.0, 8.0, 10.0)):
    y[i] += d
X = np.column_stack([np.ones_like(t), t])


def ols(X, y):
    return np.linalg.solve(X.T @ X, X.T @ y)


def huber(X, y, k=1.345, it=100):
    b = ols(X, y)
    for _ in range(it):
        r = y - X @ b
        s = np.median(np.abs(r - np.median(r))) / 0.6745
        s = max(s, 1e-12)
        u = np.abs(r) / s
        w = np.where(u <= k, 1.0, k / u)
        W = np.diag(w)
        b_new = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
        if np.max(np.abs(b_new - b)) < 1e-12:
            b = b_new
            break
        b = b_new
    return b


def theil_sen(t, y):
    sl = [(y[j] - y[i]) / (t[j] - t[i]) for i, j in itertools.combinations(range(len(t)), 2)]
    b = float(np.median(sl))
    return np.array([float(np.median(y - b * t)), b])


# limpio: Huber con k enorme == OLS
assert np.allclose(huber(X, y_limpio, k=1e9), ols(X, y_limpio), atol=1e-9)
print(f"verdad: a = {a0}, b = {b0}")
for nombre, datos in (("sin atipicos", y_limpio), ("con atipicos", y)):
    bo, bh, bt = ols(X, datos), huber(X, datos), theil_sen(t, datos)
    print(f"{nombre:13s} OLS b={bo[1]:.4f} a={bo[0]:.3f} | Huber b={bh[1]:.4f} a={bh[0]:.3f} | Theil-Sen b={bt[1]:.4f} a={bt[0]:.3f}")
bo, bh, bt = ols(X, y), huber(X, y), theil_sen(t, y)
assert abs(bo[1] - b0) > 0.3  # OLS arrastrada por los atipicos
assert abs(bh[1] - b0) < 0.04 and abs(bt[1] - b0) < 0.04  # robustos cerca de la verdad

# media frente a mediana con 20 % de contaminacion
z = rng.normal(0, 1, 1000)
z[:200] += 50.0
print(f"contaminacion 20 % (+50): media = {z.mean():.2f}; mediana = {np.median(z):.3f}; punto de ruptura de la mediana = 50 %")
assert z.mean() > 5 and abs(np.median(z)) < 1.0

# eficiencia de la mediana (normal): Var(mediana)/Var(media) -> pi/2
R, n = 100_000, 101
d = rng.normal(0, 1, (R, n))
ratio = np.median(d, axis=1).std() / d.mean(axis=1).std()
print(f"sd(mediana)/sd(media) = {ratio:.4f} (teorico sqrt(pi/2) = {math.sqrt(math.pi/2):.4f})")
assert abs(ratio - math.sqrt(math.pi / 2)) < 0.02
print("Pruebas superadas.")
