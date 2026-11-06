#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C10: regresion lineal y no lineal.

Datos: SINTETICOS. (a) deriva de un reloj de la sonda: y = a + b t con
a = 2.0 us, b = 0.50 us/dia, ruido normal sigma = 0.8 us, t = 0..19 dias.
(b) degradacion de potencia de un panel: P = P0 exp(-k t), P0 = 100 W,
k = 0.05 /ano, ruido sigma = 1.0 W, t = 0..10 anos. Valores ILUSTRATIVOS.
Modelo: minimos cuadrados ordinarios (OLS) con matriz de diseno X;
cov(beta) = sigma^2 (X^T X)^-1; ajuste no lineal por Gauss-Newton
(scipy.optimize.curve_fit).
Supuestos: errores independientes, normales y de varianza constante.
Validez: dentro del rango de t ajustado; no extrapolar sin justificacion.
Tolerancia: recuperacion exacta sin ruido (1e-9); OLS = polyfit (1e-9);
desviaciones de los parametros frente a la teoria dentro de 3 % (R = 20 000).
Las pruebas detienen la ejecucion si fallan.
"""
import platform

import numpy as np
import scipy
from scipy.optimize import curve_fit

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
rng = np.random.default_rng(1010)

# (a) lineal
t = np.arange(20.0)
a0, b0, sig = 2.0, 0.50, 0.8
X = np.column_stack([np.ones_like(t), t])
# sin ruido: recupera exactamente
beta0 = np.linalg.solve(X.T @ X, X.T @ (a0 + b0 * t))
assert np.allclose(beta0, [a0, b0], atol=1e-9)
y = a0 + b0 * t + rng.normal(0, sig, t.size)
beta = np.linalg.solve(X.T @ X, X.T @ y)
assert np.allclose(beta, np.polyfit(t, y, 1)[::-1], atol=1e-9)
res = y - X @ beta
s2 = res @ res / (t.size - 2)
cov = s2 * np.linalg.inv(X.T @ X)
print(f"a = {beta[0]:.3f} +/- {cov[0,0]**.5:.3f} us;  b = {beta[1]:.4f} +/- {cov[1,1]**.5:.4f} us/dia;  s = {s2**.5:.3f} us")
print(f"correlacion a-b = {cov[0,1]/(cov[0,0]*cov[1,1])**.5:+.3f}")
# formula cerrada de la pendiente
b_cf = np.sum((t - t.mean()) * (y - y.mean())) / np.sum((t - t.mean()) ** 2)
assert abs(b_cf - beta[1]) < 1e-12

# cov teorica frente a simulacion
R = 20_000
ys = a0 + b0 * t + rng.normal(0, sig, (R, t.size))
bs = np.linalg.solve(X.T @ X, X.T @ ys.T).T
cov_t = sig**2 * np.linalg.inv(X.T @ X)
print(f"sd(b) simulada = {bs[:,1].std():.4f}; teorica = {cov_t[1,1]**.5:.4f}")
assert abs(bs[:, 1].std() / cov_t[1, 1] ** .5 - 1) < 0.03
assert abs(bs[:, 0].std() / cov_t[0, 0] ** .5 - 1) < 0.03

# (b) no lineal
tt = np.arange(0.0, 10.5, 1.0)
f = lambda t, P0, k: P0 * np.exp(-k * t)
p_exacto, _ = curve_fit(f, tt, f(tt, 100.0, 0.05), p0=[80, 0.1])
assert np.allclose(p_exacto, [100.0, 0.05], atol=1e-8)
yy = f(tt, 100.0, 0.05) + rng.normal(0, 1.0, tt.size)
p, pc = curve_fit(f, tt, yy, p0=[80, 0.1], sigma=np.ones_like(tt), absolute_sigma=True)
print(f"P0 = {p[0]:.2f} +/- {pc[0,0]**.5:.2f} W;  k = {p[1]:.4f} +/- {pc[1,1]**.5:.4f} /ano")
# comparacion con la linealizacion ln P = ln P0 - k t (pesos distintos)
pl = np.polyfit(tt, np.log(yy), 1)
print(f"linealizando (ln): P0 = {np.exp(pl[1]):.2f} W, k = {-pl[0]:.4f} /ano")
# R^2 y residuos
r2 = 1 - np.sum((yy - f(tt, *p)) ** 2) / np.sum((yy - yy.mean()) ** 2)
print(f"R^2 = {r2:.5f}; media de residuos = {np.mean(yy - f(tt, *p)):+.3f} W")
assert r2 > 0.98
print("Pruebas superadas.")
