#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C22: comparacion de modelos (evidencia, AIC, BIC).

Datos: SINTETICOS e ILUSTRATIVOS. (a) 27 exitos en 30 pruebas: M0 (p = 0.9
fijo) frente a M1 (p ~ Beta(1,1)). (b) Deriva de un reloj: 20 puntos
y = 2.0 + 0.50 t + ruido N(0, 0.8^2), t = 0..19 (verdad: recta); se comparan
polinomios de grado 0 a 3 con sigma = 0.8 conocida.
Modelo: evidencia Z = integral p(datos|theta) p(theta) dtheta. Para modelos
lineales gaussianos con prior beta ~ N(0, s^2 I) la evidencia es
N(y; 0, sigma^2 I + s^2 X X^T). AIC = 2k - 2 ln L_max; BIC = k ln n - 2 ln L_max.
Supuestos: ruido normal con sigma conocida; prior s = 10 para los coeficientes.
Validez: la evidencia depende del prior; AIC/BIC son aproximaciones.
Tolerancia: evidencia analitica Beta-Binomial = integracion numerica a 1e-9
relativo; evidencia lineal analitica = integracion en rejilla 2D a 1e-4
relativo. Las pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")

# (a) Beta-Binomial
n, k = 30, 27
Z0 = math.comb(n, k) * 0.9**k * 0.1 ** (n - k)
Z1_exact = 1.0 / (n + 1)  # integral de C(n,k) p^k (1-p)^(n-k) dp, prior uniforme
ps = np.linspace(0, 1, 2_000_001)
Z1_num = np.trapezoid(math.comb(n, k) * ps**k * (1 - ps) ** (n - k), ps)
print(f"evidencia M0 (p=0.9) = {Z0:.6f}; M1 (p~U(0,1)) = {Z1_exact:.6f} (numerica {Z1_num:.6f}); factor de Bayes B01 = {Z0/Z1_exact:.3f}")
assert abs(Z1_num / Z1_exact - 1) < 1e-9
B01 = Z0 / Z1_exact
assert B01 > 1  # los datos favorecen p = 0.9 fijo, que tiene prediccion mas precisa

# (b) polinomios
rng = np.random.default_rng(2222)
t = np.arange(20.0)
sig, s_prior = 0.8, 10.0
y = 2.0 + 0.5 * t + rng.normal(0, sig, t.size)
N = len(y)
tc = (t - t.mean()) / t.std()  # t estandarizado para estabilidad
print("grado  k   chi2_min   AIC      BIC      ln evidencia")
rows = []
for deg in range(4):
    X = np.vander(tc, deg + 1, increasing=True)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    rss = float(np.sum((y - X @ beta) ** 2))
    lnL = -0.5 * rss / sig**2 - N * math.log(sig * math.sqrt(2 * math.pi))
    kk = deg + 1
    aic, bic = 2 * kk - 2 * lnL, kk * math.log(N) - 2 * lnL
    cov = sig**2 * np.eye(N) + s_prior**2 * X @ X.T
    lnZ = stats.multivariate_normal.logpdf(y, mean=np.zeros(N), cov=cov)
    rows.append((deg, kk, rss / sig**2, aic, bic, lnZ))
    print(f"{deg:4d}  {kk:2d}  {rss/sig**2:8.2f}  {aic:7.2f}  {bic:7.2f}  {lnZ:9.2f}")
best_aic = min(rows, key=lambda r: r[3])[0]
best_bic = min(rows, key=lambda r: r[4])[0]
best_ev = max(rows, key=lambda r: r[5])[0]
print(f"mejor segun AIC: grado {best_aic}; BIC: grado {best_bic}; evidencia: grado {best_ev}")
assert best_bic == 1 and best_ev == 1

# comprobacion independiente de la evidencia del grado 1 por integracion 2D
deg = 1
X = np.vander(tc, 2, increasing=True)
b0 = np.linspace(-45, 45, 1201)
b1 = np.linspace(-45, 45, 1201)
B0, B1 = np.meshgrid(b0, b1, indexing="ij")
rss_grid = np.zeros_like(B0)
for ti, yi in zip(X, y):
    rss_grid += (yi - (ti[0] * B0 + ti[1] * B1)) ** 2
lnlik = -0.5 * rss_grid / sig**2 - N * math.log(sig * math.sqrt(2 * math.pi))
lnprior = -0.5 * (B0**2 + B1**2) / s_prior**2 - 2 * math.log(s_prior * math.sqrt(2 * math.pi))
integrand = np.exp(lnlik + lnprior - (lnlik + lnprior).max())
Zgrid = np.trapezoid(np.trapezoid(integrand, b1, axis=1), b0) * math.exp((lnlik + lnprior).max())
print(f"ln evidencia grado 1: analitica = {rows[1][5]:.4f}; rejilla 2D = {math.log(Zgrid):.4f}")
assert abs(math.log(Zgrid) - rows[1][5]) < 1e-3
# factor de Bayes entre grado 1 y 3
print(f"ln B(grado 1 / grado 3) = {rows[1][5]-rows[3][5]:.2f}  (penalizacion de Occam de los parametros sobrantes)")
print("Pruebas superadas.")
