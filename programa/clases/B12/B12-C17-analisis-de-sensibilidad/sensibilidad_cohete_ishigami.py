#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C17: analisis de sensibilidad local y global.

Datos: SINTETICOS e ILUSTRATIVOS. Ecuacion del cohete: dv = ve ln(m0/mf)
con ve = 3000 m/s, m0 = 1000 kg, mf = 600 kg, y desviaciones tipicas
relativas de 2 % (ve), 0.5 % (m0) y 0.5 % (mf). Banco de pruebas global:
funcion de Ishigami (a = 7, b = 0.1) con indices de Sobol analiticos.
Modelo: sensibilidades locales (derivadas), elasticidades, contribucion a la
varianza y estimadores de Monte Carlo de Saltelli (1.er orden) y Jansen
(total) por muestras "pick-freeze".
Supuestos: entradas independientes; Ishigami con entradas U(-pi, pi).
Validez: los indices de Sobol miden varianza, no cola ni riesgo.
Tolerancia: derivadas por diferencias centrales a 1e-6 relativo; indices de
Sobol Monte Carlo (N = 400 000) a 0.01 de los analiticos; semilla fija. Las
pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")

# --- sensibilidad local de la ecuacion del cohete
ve, m0, mf = 3000.0, 1000.0, 600.0
f = lambda ve, m0, mf: ve * math.log(m0 / mf)
dv = f(ve, m0, mf)
d_ve, d_m0, d_mf = math.log(m0 / mf), ve / m0, -ve / mf
print(f"dv = {dv:.3f} m/s;  d/dve = {d_ve:.5f};  d/dm0 = {d_m0:.4f} (m/s)/kg;  d/dmf = {d_mf:.4f} (m/s)/kg")


def cdiff(i, x, rel=1e-5):
    h = x[i] * rel
    xp, xm = list(x), list(x)
    xp[i] += h
    xm[i] -= h
    return (f(*xp) - f(*xm)) / (2 * h)


for i, d in enumerate((d_ve, d_m0, d_mf)):
    n = cdiff(i, [ve, m0, mf])
    assert abs(n - d) / abs(d) < 1e-6
el = [d_ve * ve / dv, d_m0 * m0 / dv, d_mf * mf / dv]
print("elasticidades (cambio relativo de dv por cambio relativo de cada entrada):", " ".join(f"{e:+.4f}" for e in el))
assert abs(el[0] - 1) < 1e-12 and abs(el[1] + el[2]) < 1e-12

u = np.array([0.02 * ve, 0.005 * m0, 0.005 * mf])
c = np.array([d_ve, d_m0, d_mf])
contrib = (c * u) ** 2
uc = math.sqrt(contrib.sum())
print(f"u(dv) = {uc:.2f} m/s; fraccion de la varianza: ve {contrib[0]/contrib.sum():.3f}, m0 {contrib[1]/contrib.sum():.3f}, mf {contrib[2]/contrib.sum():.3f}")
rng0 = np.random.default_rng(1718)
Xs = rng0.normal([ve, m0, mf], u, (1_000_000, 3))
dvs = Xs[:, 0] * np.log(Xs[:, 1] / Xs[:, 2])
print(f"Monte Carlo (M = 1e6): u(dv) = {dvs.std():.2f} m/s (GUM {uc:.2f})")
assert abs(dvs.std() / uc - 1) < 0.01 and contrib[0] / contrib.sum() > 0.6

# --- Sobol global con Ishigami
a, b = 7.0, 0.1
ish = lambda x: np.sin(x[:, 0]) + a * np.sin(x[:, 1]) ** 2 + b * x[:, 2] ** 4 * np.sin(x[:, 0])
V = a**2 / 8 + b * math.pi**4 / 5 + b**2 * math.pi**8 / 18 + 0.5
V1 = 0.5 * (1 + b * math.pi**4 / 5) ** 2
V2 = a**2 / 8
V13 = 8 * b**2 * math.pi**8 / 225
S1_t, S2_t, S3_t = V1 / V, V2 / V, 0.0
ST1_t, ST2_t, ST3_t = (V1 + V13) / V, V2 / V, V13 / V
print(f"Ishigami analitico: S1={S1_t:.4f} S2={S2_t:.4f} S3={S3_t:.4f};  ST1={ST1_t:.4f} ST2={ST2_t:.4f} ST3={ST3_t:.4f}")

rng = np.random.default_rng(1717)
N = 400_000
A = rng.uniform(-math.pi, math.pi, (N, 3))
B = rng.uniform(-math.pi, math.pi, (N, 3))
yA, yB = ish(A), ish(B)
var = np.var(np.concatenate([yA, yB]))
S1, ST = [], []
for i in range(3):
    ABi = A.copy()
    ABi[:, i] = B[:, i]
    yAB = ish(ABi)
    S1.append(np.mean(yB * (yAB - yA)) / var)           # Saltelli 2010
    ST.append(0.5 * np.mean((yA - yAB) ** 2) / var)     # Jansen
print("Sobol Monte Carlo:  S1 = " + " ".join(f"{s:.4f}" for s in S1) + "   ST = " + " ".join(f"{s:.4f}" for s in ST))
for est, ex in zip(S1 + ST, (S1_t, S2_t, S3_t, ST1_t, ST2_t, ST3_t)):
    assert abs(est - ex) < 0.01, (est, ex)
print(f"S3 = 0 pero ST3 = {ST[2]:.3f}: x3 actua solo por interaccion con x1")
print("Pruebas superadas.")
