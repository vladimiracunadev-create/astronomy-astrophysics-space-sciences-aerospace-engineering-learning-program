#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C15: muestreo de importancia para un suceso raro.

Datos: SINTETICOS. Error normalizado de aproximacion Z ~ N(0,1) de una
maniobra; el suceso raro es Z > 4 (probabilidad exacta 3.167e-5) (ILUSTRATIVO).
Modelo: P(Z > 4) = E_q[ w(X) 1{X > 4} ], con propuesta q = N(mu_q, s_q^2) y
peso w = p/q. Para q = N(4, 1): w(x) = exp(-4x + 8).
Supuestos: el soporte de q cubre el de p·1{X>4}; pesos con varianza finita.
Validez: propuesta con colas al menos tan pesadas como la integranda.
Tolerancia: estimador de importancia dentro de 4 errores tipicos de la
exacta; reduccion de varianza frente al Monte Carlo simple mayor que 100;
propuesta mal centrada N(2,1): ESS menor que 0.5 del de la buena. Semilla
fija; las pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
p_exact = 0.5 * math.erfc(4.0 / math.sqrt(2.0))
print(f"P(Z > 4) exacta = {p_exact:.6e}")
rng = np.random.default_rng(1515)
N = 100_000

# Monte Carlo simple
z = rng.standard_normal(N)
hits = int(np.sum(z > 4))
p_mc = hits / N
se_mc = math.sqrt(p_exact * (1 - p_exact) / N)
print(f"MC simple N={N}: aciertos = {hits}; estimacion = {p_mc:.3e}; error relativo teorico = {se_mc/p_exact:.2f}")

# importancia con q = N(4, 1)
x = rng.normal(4.0, 1.0, N)
w = np.exp(-4.0 * x + 8.0)
f = w * (x > 4)
p_is = float(f.mean())
se_is = float(f.std(ddof=1) / math.sqrt(N))
print(f"IS q=N(4,1):    estimacion = {p_is:.4e} +/- {se_is:.1e}; error relativo = {abs(p_is-p_exact)/p_exact:.3%}")
assert abs(p_is - p_exact) < 4 * se_is
var_ratio = (p_exact * (1 - p_exact) / N) / se_is**2
print(f"reduccion de varianza (MC simple / IS) = {var_ratio:,.0f}")
assert var_ratio > 100
ess = float(f.sum() ** 2 / np.sum(f**2))
print(f"tamano muestral efectivo (solo pesos >0): {ess:,.0f} de {N}")

# propuesta mal centrada: N(2, 1), muy pocas muestras caen en la region de interes
x2 = rng.normal(2.0, 1.0, N)
f2 = np.exp(-2.0 * x2 + 2.0) * (x2 > 4)
ess2 = float(f2.sum() ** 2 / np.sum(f2**2)) if f2.sum() > 0 else 0.0
se2 = float(f2.std(ddof=1) / math.sqrt(N))
print(f"IS q=N(2,1): estimacion = {f2.mean():.4e} +/- {se2:.1e}; muestras en la region = {int(np.sum(x2 > 4))}; ESS = {ess2:,.0f} ({ess2/ess:.2f} del bueno)")
assert ess2 < 0.5 * ess

# propuesta correctamente ponderada para el mismo objetivo (verificacion cruzada)
mu = 3.0
x3 = rng.normal(mu, 1.0, N)
f3 = np.exp(-mu * x3 + mu**2 / 2) * (x3 > 4)
se3 = float(f3.std(ddof=1) / math.sqrt(N))
print(f"IS q=N(3,1):   estimacion = {f3.mean():.4e} +/- {se3:.1e}")
assert abs(f3.mean() - p_exact) < 4 * se3
print("Pruebas superadas.")
