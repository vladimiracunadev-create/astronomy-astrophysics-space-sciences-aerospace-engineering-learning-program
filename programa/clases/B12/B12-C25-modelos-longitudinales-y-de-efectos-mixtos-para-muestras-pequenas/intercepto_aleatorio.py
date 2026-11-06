#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C25: modelo de intercepto aleatorio con muestras pequenas.

Datos: SINTETICOS (no son datos de personas reales). 6 unidades (sujetos
simulados) con 4 mediciones cada una: y_ij = b0 + b1 t_j + u_i + e_ij,
b0 = 10, b1 = 0.5 por visita, u_i ~ N(0, 2^2), e_ij ~ N(0, 1^2); t = 0..3.
Modelo: estimadores de varianza por ANOVA para el diseno balanceado
(MS_entre, MS_dentro): sigma_e^2 = MSW; sigma_u^2 = (MSB - MSW)/n_t (si >= 0);
ICC = sigma_u^2/(sigma_u^2 + sigma_e^2). Nivel medio: IC con t de m - 1
grados de libertad sobre las medias por unidad; IC ingenuo: ignora el
agrupamiento (todas las observaciones independientes).
Supuestos: balanceado, errores normales, intercepto aleatorio.
Validez: datos faltantes o pendientes aleatorias exigen un modelo mixto
completo (REML); aqui solo el caso balanceado.
Tolerancia: componentes de varianza con m = 4000 unidades a 5 % de lo
verdadero; error tipico exacto del nivel medio frente a simulacion a 3 %;
cobertura del IC correcto en [0.94, 0.96] y del ingenuo < 0.85 (R = 20 000).
Detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")
rng = np.random.default_rng(2525)
b0, b1, su, se = 10.0, 0.5, 2.0, 1.0
nt = 4
t = np.arange(nt, dtype=float)


def simula(m, rng):
    u = rng.normal(0, su, (m, 1))
    e = rng.normal(0, se, (m, nt))
    return b0 + b1 * t[None, :] + u + e


def componentes(Y):
    m = Y.shape[0]
    # se quita el efecto de la visita (medias por columna)
    R = Y - Y.mean(axis=0, keepdims=True)
    unit_mean = R.mean(axis=1)
    SSB = nt * np.sum(unit_mean**2)
    SSW = np.sum((R - unit_mean[:, None]) ** 2)
    MSB = SSB / (m - 1)
    MSW = SSW / ((m - 1) * (nt - 1))
    s2u = max((MSB - MSW) / nt, 0.0)
    return MSW, s2u


# recuperacion de componentes con muchas unidades
MSW, s2u = componentes(simula(4000, rng))
icc = s2u / (s2u + MSW)
print(f"m = 4000: sigma_e^2 = {MSW:.3f} (verdad 1); sigma_u^2 = {s2u:.3f} (verdad 4); ICC = {icc:.3f} (verdad {su**2/(su**2+se**2):.3f})")
assert abs(MSW - 1) < 0.05 and abs(s2u - 4) < 0.2

# muestra pequena: 6 unidades
m = 6
Y = simula(m, rng)
MSW6, s2u6 = componentes(Y)
print(f"m = 6: sigma_e^2 = {MSW6:.3f}; sigma_u^2 = {s2u6:.3f}; ICC = {s2u6/(s2u6+MSW6):.3f}")

# error tipico del nivel medio: teorico vs ingenuo
N = m * nt
se_true = math.sqrt(su**2 / m + se**2 / N)
se_naive = math.sqrt((su**2 + se**2) / N)
print(f"error tipico del nivel medio: verdadero = {se_true:.4f}; ingenuo (ignora agrupamiento) = {se_naive:.4f}")
R_ = 20_000
means = np.array([simula(m, rng).mean() for _ in range(R_)])
print(f"simulado = {means.std():.4f}")
assert abs(means.std() / se_true - 1) < 0.03

# cobertura
cov_ok = cov_nv = 0
tcrit5 = stats.t.ppf(0.975, m - 1)
tcrit23 = stats.t.ppf(0.975, N - 1)
target = b0 + b1 * t.mean()
for _ in range(R_):
    Yr = simula(m, rng)
    um = Yr.mean(axis=1)
    c = Yr.mean()
    half_ok = tcrit5 * um.std(ddof=1) / math.sqrt(m)
    half_nv = tcrit23 * Yr.std(ddof=1) / math.sqrt(N)
    cov_ok += abs(c - target) <= half_ok
    cov_nv += abs(c - target) <= half_nv
cov_ok, cov_nv = cov_ok / R_, cov_nv / R_
print(f"cobertura del IC 95 % del nivel medio: correcto (t con {m-1} gl sobre medias por unidad) = {cov_ok:.4f}; ingenuo = {cov_nv:.4f}")
assert 0.94 <= cov_ok <= 0.96 and cov_nv < 0.85

# pendiente: efecto dentro de la unidad -> el ingenuo SOBREestima el error
sxx = m * np.sum((t - t.mean()) ** 2)
se_b1_true = se / math.sqrt(sxx)
se_b1_naive = math.sqrt(su**2 + se**2) / math.sqrt(sxx)
print(f"error tipico de la pendiente: verdadero = {se_b1_true:.4f}; ingenuo = {se_b1_naive:.4f} (el ingenuo es {se_b1_naive/se_b1_true:.2f} veces mayor)")
slopes = []
for _ in range(R_):
    Yr = simula(m, rng)
    slopes.append(np.sum((t - t.mean())[None, :] * (Yr - Yr.mean())) / sxx)
print(f"simulado = {np.std(slopes):.4f}")
assert abs(np.std(slopes) / se_b1_true - 1) < 0.03
print("Pruebas superadas.")
