#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C26: potencia, sesgo de significancia y poblaciones pequenas.

Datos: SINTETICOS (no son datos de personas reales). Comparacion de dos
grupos con efecto estandarizado d (diferencia de medias / sigma).
Modelo: prueba t de dos muestras con n por grupo y alfa = 0.05 bilateral;
potencia exacta con la t no central (gl = 2n - 2, no centralidad
d sqrt(n/2)). Valor predictivo positivo PPV = pot*pi/(pot*pi + alfa(1-pi)).
Supuestos: normalidad, varianzas iguales, efecto verdadero fijo.
Validez: muestras pequenas: la estimacion del efecto es muy ruidosa.
Tolerancia: potencia exacta frente a simulacion a 0.01 (R = 100 000); PPV
exacto frente a simulacion a 0.01. Detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np
import scipy
from scipy import stats

print(f"Python {platform.python_version()} - NumPy {np.__version__} - SciPy {scipy.__version__}")


def power(d, n, alpha=0.05):
    df = 2 * n - 2
    nc = d * math.sqrt(n / 2)
    tc = stats.t.ppf(1 - alpha / 2, df)
    return float(stats.nct.sf(tc, df, nc) + stats.nct.cdf(-tc, df, nc))


rng = np.random.default_rng(2626)
R = 100_000


def simula(d, n):
    x = rng.normal(0, 1, (R, n))
    y = rng.normal(d, 1, (R, n))
    diff = y.mean(axis=1) - x.mean(axis=1)
    sp = np.sqrt((x.var(axis=1, ddof=1) + y.var(axis=1, ddof=1)) / 2)
    tstat = diff / (sp * math.sqrt(2 / n))
    tc = stats.t.ppf(0.975, 2 * n - 2)
    dhat = diff / sp
    return np.abs(tstat) > tc, dhat


print("   d    n/grupo  potencia exacta  potencia simulada")
for d, n in ((0.8, 6), (0.8, 26), (0.5, 20), (0.2, 10)):
    sig, _ = simula(d, n)
    pe = power(d, n)
    print(f"{d:4.1f}  {n:6d}      {pe:6.4f}           {sig.mean():6.4f}")
    assert abs(pe - sig.mean()) < 0.01

# tamano de muestra para potencia 0.80, d = 0.8
n = 2
while power(0.8, n) < 0.80:
    n += 1
print(f"n por grupo para potencia >= 0.80 con d = 0.8: {n} (potencia {power(0.8, n):.4f})")
assert n == 26

# filtro de significancia: efecto verdadero d = 0.3, n = 10 por grupo
d_true, n = 0.3, 10
sig, dhat = simula(d_true, n)
pot = sig.mean()
exag = np.mean(np.abs(dhat[sig])) / d_true
wrong_sign = np.mean(dhat[sig] < 0)
print(f"d verdadero = {d_true}, n = {n}: potencia = {pot:.3f}; media de |d_hat| entre significativos = {np.mean(np.abs(dhat[sig])):.3f} (exageracion x{exag:.2f}); signo equivocado entre significativos = {wrong_sign:.3f}")
assert exag > 2.0 and wrong_sign > 0

# valor predictivo positivo
pi = 0.10
pot_pi = power(0.5, 20)
ppv = pot_pi * pi / (pot_pi * pi + 0.05 * (1 - pi))
nrep = 400_000
verdad = rng.random(nrep) < pi
sig_h = np.where(verdad, rng.random(nrep) < pot_pi, rng.random(nrep) < 0.05)
ppv_sim = verdad[sig_h].mean()
print(f"PPV con pi = {pi}, potencia = {pot_pi:.3f}: exacto = {ppv:.4f}; simulado = {ppv_sim:.4f}")
assert abs(ppv - ppv_sim) < 0.01
print("Pruebas superadas.")
