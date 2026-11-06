#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C05: covarianza y correlacion.

Datos: SINTETICOS. Errores de posicion (sigma 3.0 m) y de velocidad
(sigma 4.0 mm/s) de un filtro de navegacion con correlacion rho = 0.8
(ILUSTRATIVO). Caso exacto: X uniforme discreta en {-2,-1,0,1,2}, Y = X^2.
Modelo: Cov(X,Y) = E[XY] - E[X]E[Y]; Var(X+Y) = Var X + Var Y + 2 Cov(X,Y);
varianza del promedio de n medidas con correlacion comun rho:
sigma^2 (1 + (n-1) rho) / n.
Supuestos: normalidad conjunta para la simulacion; varianzas finitas.
Validez: relaciones lineales; r = 0 no implica independencia.
Tolerancia: pruebas exactas con fracciones; en simulacion |r - rho| < 3e-3 y
|Var - exacta|/exacta < 1.5 % (N = 1 000 000, semilla fija). Detienen la
ejecucion si fallan.
"""
import platform
from fractions import Fraction

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")

# --- caso exacto: dependencia sin correlacion
xs = [-2, -1, 0, 1, 2]
p = Fraction(1, 5)
EX = sum(x * p for x in xs)
EY = sum(x * x * p for x in xs)
EXY = sum(x * x * x * p for x in xs)
cov = EXY - EX * EY
print(f"Y = X^2: E[X]={EX}, E[Y]={EY}, E[XY]={EXY}, Cov={cov}")
assert cov == 0  # no correlacionadas ...
# ... pero Y esta determinada por X: P(Y=4 | X=2) = 1 frente a P(Y=4) = 2/5
assert Fraction(1) != sum(p for x in xs if x * x == 4)
print("Cov = 0 pero Y depende de X (P(Y=4|X=2)=1 frente a P(Y=4)=2/5)")

# --- binarias: covarianza exacta de dos indicadores dependientes
# A = 'al menos 2 funcionan' (0.972), B = 'el computador 1 funciona' (0.9), P(A y B)=0.891 (C01)
pA, pB = Fraction(972, 1000), Fraction(9, 10)
pAB = Fraction(891, 1000)
cov_ind = pAB - pA * pB
print(f"Cov(1_A,1_B) = {cov_ind} = {float(cov_ind):.4f}")
assert cov_ind == Fraction(81, 5000)
r_ind = float(cov_ind) / (float(pA * (1 - pA) * pB * (1 - pB))) ** 0.5
print(f"correlacion de los indicadores = {r_ind:.4f}")
assert abs(r_ind - 0.3273) < 1e-3

# --- simulacion gaussiana correlacionada
rho, s1, s2 = 0.8, 3.0, 4.0
rng = np.random.default_rng(31)
N = 1_000_000
z = rng.standard_normal((N, 2))
x = s1 * z[:, 0]
y = s2 * (rho * z[:, 0] + np.sqrt(1 - rho**2) * z[:, 1])
r = np.corrcoef(x, y)[0, 1]
c = np.cov(x, y)[0, 1]
print(f"r simulada = {r:.4f} (rho = {rho});  Cov = {c:.3f} (exacta {rho*s1*s2:.3f})")
assert abs(r - rho) < 3e-3
v_exacta = s1**2 + s2**2 + 2 * rho * s1 * s2
v = np.var(x + y)
print(f"Var(X+Y) = {v:.2f} (exacta {v_exacta:.2f}); sin covarianza seria {s1**2 + s2**2:.2f}")
assert abs(v - v_exacta) / v_exacta < 0.015

# --- promedio de n medidas con correlacion comun
n = 9
rho_c = 0.5
cov_m = np.full((n, n), rho_c * 9.0)
np.fill_diagonal(cov_m, 9.0)
m = rng.multivariate_normal(np.zeros(n), cov_m, 200_000).mean(axis=1)
exacta = 9.0 * (1 + (n - 1) * rho_c) / n
print(f"Var(promedio de 9, rho=0.5) = {m.var():.3f} (exacta {exacta:.3f}; independientes: {9.0/n:.3f})")
assert abs(m.var() - exacta) / exacta < 0.02
print(f"limite n->infinito: sigma^2 * rho = {9.0 * rho_c:.1f} m^2")

# Cauchy-Schwarz: |r| <= 1
assert abs(r) <= 1
print("Pruebas superadas.")
