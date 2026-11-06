#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C12: inferencia bayesiana con priors conjugados.

Datos: SINTETICOS. Los conteos de C07 (4,2,3,7,3,5,1,3,4,5) en intervalos
de 10 min; tasa de falsas alarmas ILUSTRATIVA para el problema discreto.
Modelo: N_i ~ Poisson(lambda), prior Gamma(alfa, beta) (forma, tasa);
posterior Gamma(alfa + sum k, beta + n). Segundo problema: Beta-Binomial.
Supuestos: independencia, tasa constante, prior declarado.
Validez: modelo Poisson correcto. Tolerancia: la posterior por rejilla
(100 001 puntos) coincide con la analitica a menos de 1e-6 en densidad
relativa y 1e-6 en media; Bayes discreto exacto con fracciones. Las pruebas
detienen la ejecucion si fallan.
"""
import platform
from fractions import Fraction

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
k = np.array([4, 2, 3, 7, 3, 5, 1, 3, 4, 5])
n, S = len(k), int(k.sum())

# --- 1) Poisson-Gamma
for alfa, beta, nombre in ((1.0, 0.1, "debil"), (8.0, 2.0, "informativo (media 4)")):
    post = stats.gamma(a=alfa + S, scale=1 / (beta + n))
    lo, hi = post.ppf([0.025, 0.975])
    print(f"prior {nombre:22s}: posterior Gamma({alfa+S:.0f}, {beta+n:.1f}); media = {post.mean():.4f}; IC creible 95 % = [{lo:.3f}, {hi:.3f}]")

# comprobacion por rejilla (prior x verosimilitud)
alfa, beta = 1.0, 0.1
lam = np.linspace(1e-6, 15, 100_001)
logpost = stats.gamma.logpdf(lam, a=alfa, scale=1 / beta) + stats.poisson.logpmf(k[:, None], lam[None, :]).sum(axis=0)
w = np.exp(logpost - logpost.max())
dx = lam[1] - lam[0]
w /= w.sum() * dx
exacta = stats.gamma.pdf(lam, a=alfa + S, scale=1 / (beta + n))
print(f"max |rejilla - analitica| = {np.max(np.abs(w - exacta)):.2e}; media rejilla = {np.sum(lam*w)*dx:.6f} (analitica {(alfa+S)/(beta+n):.6f})")
assert np.max(np.abs(w - exacta)) < 1e-6
assert abs(np.sum(lam * w) * dx - (alfa + S) / (beta + n)) < 1e-6

# --- 2) Beta-Binomial: 27 exitos en 30 con prior Beta(1,1)
a2, b2 = 1 + 27, 1 + 3
pb = stats.beta(a2, b2)
print(f"Beta-Binomial 27/30, prior uniforme: media = {pb.mean():.4f}; IC 95 % = [{pb.ppf(0.025):.3f}, {pb.ppf(0.975):.3f}]")
assert abs(pb.mean() - 28 / 32) < 1e-12 and pb.ppf(0.975) < 1.0

# --- 3) Bayes discreto: alarma de anomalia (fracciones)
prev = Fraction(1, 1000)       # P(anomalia)
sens = Fraction(95, 100)       # P(alarma | anomalia)
fpr = Fraction(2, 100)         # P(alarma | normal)
pa = sens * prev + fpr * (1 - prev)
post_a = sens * prev / pa
print(f"P(anomalia | alarma) = {post_a} = {float(post_a):.4f}  (sensibilidad 0.95, prevalencia 0.001, falsas alarmas 0.02)")
assert post_a == Fraction(95, 95 + 1998)
print("Pruebas superadas.")
