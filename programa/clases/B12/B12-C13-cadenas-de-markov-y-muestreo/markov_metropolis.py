#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C13: cadenas de Markov y muestreo de Metropolis.

Datos: SINTETICOS. (a) Enlace de comunicaciones con dos estados, Bueno (0) y
Malo (1): P(B->M) = 0.10, P(M->B) = 0.40 por paso de 1 min (ILUSTRATIVO).
(b) Posterior Gamma(38, 10.1) de la tasa del detector de la clase C12
(prior Gamma(1, 0.1), conteos sinteticos con suma 37 en 10 intervalos).
Modelo: (a) cadena de Markov homogenea; distribucion estacionaria
pi = (q/(p+q), p/(p+q)). (b) Metropolis con propuesta normal simetrica.
Supuestos: cadena irreducible y aperiodica; propuesta simetrica.
Validez: tras el calentamiento; la diagnostica de convergencia es de C23.
Tolerancia: pi teorica = vector propio = iteracion de potencias (1e-12);
frecuencia simulada a 5e-3; media y varianza de la posterior a 1 % y 6 %
(N = 400 000, calentamiento 5 000, semilla fija). Detienen la ejecucion.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")

# (a) cadena de dos estados
p, q = 0.10, 0.40
P = np.array([[1 - p, p], [q, 1 - q]])
pi_teo = np.array([q / (p + q), p / (p + q)])
w, v = np.linalg.eig(P.T)
pi_eig = np.real(v[:, np.argmin(np.abs(w - 1))])
pi_eig /= pi_eig.sum()
Pn = np.linalg.matrix_power(P, 60)
print(f"pi teorica = {pi_teo}; vector propio = {np.round(pi_eig, 6)}; P^60 filas = {np.round(Pn[0], 6)} {np.round(Pn[1], 6)}")
assert np.allclose(pi_teo, pi_eig, atol=1e-12) and np.allclose(Pn, pi_teo, atol=1e-9)
assert np.allclose(pi_teo @ P, pi_teo, atol=1e-12)
# segundo valor propio y velocidad de mezcla
lam2 = 1 - p - q
print(f"segundo valor propio = {lam2:.2f}: el error cae como {abs(lam2)}^n")

rng = np.random.default_rng(1313)
n = 1_000_000
u = rng.random(n)
s = np.zeros(n, dtype=int)
for i in range(1, n):
    s[i] = (u[i] < p) if s[i - 1] == 0 else (u[i] >= q)
frac_malo = s.mean()
print(f"fraccion simulada en estado Malo = {frac_malo:.4f} (teorica {pi_teo[1]:.4f})")
assert abs(frac_malo - pi_teo[1]) < 5e-3

# balance detallado de Metropolis en un objetivo discreto de 3 estados
obj = np.array([0.2, 0.5, 0.3])
T = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        if i != j:
            T[i, j] = (1 / 2) * min(1.0, obj[j] / obj[i])  # propuesta uniforme entre los otros 2
    T[i, i] = 1 - T[i].sum()
assert np.allclose(obj @ T, obj, atol=1e-12)
print("balance detallado de Metropolis: pi T = pi (3 estados) verificado")

# (b) Metropolis sobre la posterior Gamma(38, 10.1)
a_post, b_post = 38.0, 10.1
logp = lambda x: (a_post - 1) * math.log(x) - b_post * x if x > 0 else -math.inf
N, burn, step = 400_000, 5_000, 0.8
x = 8.0  # inicio deliberadamente lejos
chain = np.empty(N)
acc = 0
lp = logp(x)
z = rng.standard_normal(N)
ul = np.log(rng.random(N))
for i in range(N):
    y = x + step * z[i]
    lpy = logp(y)
    if ul[i] < lpy - lp:
        x, lp = y, lpy
        acc += 1
    chain[i] = x
c = chain[burn:]
print(f"tasa de aceptacion = {acc/N:.3f}; media = {c.mean():.4f} (exacta {a_post/b_post:.4f}); var = {c.var():.4f} (exacta {a_post/b_post**2:.4f})")
assert abs(c.mean() / (a_post / b_post) - 1) < 0.01
assert abs(c.var() / (a_post / b_post**2) - 1) < 0.06
lo, hi = np.percentile(c, [2.5, 97.5])
ex = stats.gamma.ppf([0.025, 0.975], a=a_post, scale=1 / b_post)
print(f"IC 95 % MCMC = [{lo:.3f}, {hi:.3f}]; exacto = [{ex[0]:.3f}, {ex[1]:.3f}]")
print(f"primeros 5 valores de la cadena: {np.round(chain[:5], 3)}")
print("Pruebas superadas.")
