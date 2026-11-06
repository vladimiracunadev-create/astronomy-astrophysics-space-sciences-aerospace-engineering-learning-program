#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C07: estimacion de parametros (maxima verosimilitud).

Datos: SINTETICOS. Conteos de un detector en 10 intervalos, generados con
lambda verdadero = 4.0 (ILUSTRATIVO) y semilla 5.
Modelo: N_i ~ Poisson(lambda) independientes; log-verosimilitud
l(lambda) = sum(k_i ln lambda - lambda - ln k_i!). Estimador de maxima
verosimilitud (MLE) = media muestral; cota de Cramer-Rao Var >= lambda/n.
Para una normal, la varianza MLE (divisor n) tiene sesgo -sigma^2/n.
Supuestos: independencia, tasa constante. Validez: modelo correcto.
Tolerancia: MLE por rejilla = media a menos de 1e-3; pruebas exactas con
fracciones para el sesgo; simulacion: varianza del MLE de Poisson dentro de
3 % de lambda/n. Las pruebas detienen la ejecucion si fallan.
"""
import itertools
import math
import platform
from fractions import Fraction

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
rng = np.random.default_rng(5)
k = rng.poisson(4.0, 10)
print("conteos:", k.tolist(), " suma =", int(k.sum()))

lg = np.array([math.lgamma(v + 1) for v in k])
ll = lambda lam: float(np.sum(k * math.log(lam) - lam - lg))
grid = np.linspace(1.0, 8.0, 70001)
best = grid[np.argmax([ll(g) for g in grid])]
print(f"lambda_MLE por rejilla = {best:.4f}; media muestral = {k.mean():.4f}")
assert abs(best - k.mean()) < 1e-3
se = math.sqrt(k.mean() / len(k))
print(f"error tipico estimado sqrt(lambda_hat/n) = {se:.4f}")

# --- sesgo exacto de la varianza: poblacion {0,1} equiprobable, n = 2 con reemplazo
vals = [0, 1]
n = 2
mle, ins = [], []
for s in itertools.product(vals, repeat=n):
    m = Fraction(sum(s), n)
    ss = sum((Fraction(x) - m) ** 2 for x in s)
    mle.append(ss / n)
    ins.append(ss / (n - 1))
E_mle = sum(mle) / len(mle)
E_ins = sum(ins) / len(ins)
print(f"sigma^2 = 1/4; E[divisor n] = {E_mle}; E[divisor n-1] = {E_ins}")
assert E_ins == Fraction(1, 4) and E_mle == Fraction(1, 4) * Fraction(n - 1, n)

# --- simulacion: varianza del MLE de Poisson vs cota de Cramer-Rao
n, lam, R = 10, 4.0, 200_000
est = rng.poisson(lam, (R, n)).mean(axis=1)
print(f"Var(MLE) simulada = {est.var():.4f}; lambda/n = {lam/n:.4f}")
assert abs(est.var() - lam / n) / (lam / n) < 0.03
print(f"sesgo del MLE = {est.mean() - lam:+.4f} (insesgado)")

# --- normal, n = 5: sesgo de la varianza con divisor n
x = rng.normal(0, 3.0, (R, 5))
v_n = x.var(axis=1, ddof=0).mean()
v_n1 = x.var(axis=1, ddof=1).mean()
print(f"normal sigma^2 = 9: E[divisor n] = {v_n:.3f} (teorica 7.2); E[divisor n-1] = {v_n1:.3f}")
assert abs(v_n - 7.2) < 0.08 and abs(v_n1 - 9.0) < 0.08
print("Pruebas superadas.")
