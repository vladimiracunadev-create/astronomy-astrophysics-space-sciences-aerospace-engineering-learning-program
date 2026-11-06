#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C01: serie temporal discreta, tendencia y autocorrelación.

Datos: SINTÉTICOS. Curva de luz ficticia muestreada cada 120 s (cadencia
nominal de 2 min de los objetivos de TESS, MAST) durante 7 d, con modulación
rotacional (P = 2,5 d, amplitud 2e-3), tendencia lineal (-1e-4 por día) y
ruido gaussiano (sigma = 5e-4), semilla fija. Hueco de 12 h por descarga.
Modelo: x[n] = x(t0 + n*dt); autocorrelación muestral
r_k = sum (x_n-m)(x_{n+k}-m) / sum (x_n-m)^2 (NIST e-Handbook 1.3.5.12).
Supuestos: muestreo equiespaciado salvo el hueco; ruido blanco.
Validez: lags k << N. Tolerancia: 0,01 en r_k analítico; 1e-12 en el ajuste
lineal exacto.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def acf(x, k):
    m = x.mean()
    return float(np.sum((x[:-k] - m) * (x[k:] - m)) / np.sum((x - m) ** 2))


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())

# --- Prueba 1: seno puro, 20 periodos de 100 muestras: r_k = (1-k/N) cos(2 pi k/100)
N0, P0 = 2000, 100
s = np.sin(2 * np.pi * np.arange(N0) / P0)
for k, esperado in [(100, 0.95), (50, -0.975), (25, 0.0)]:
    r = acf(s, k)
    print(f"  prueba seno: r_{k} = {r:+.4f} (analítico {esperado:+.4f})")
    prueba(abs(r - esperado) < 0.01, f"acf del seno en k={k}")

# --- Prueba 2: el ajuste lineal recupera una recta exacta
t = np.arange(100.0)
c = np.polyfit(t, 3.0 - 0.5 * t, 1)
prueba(abs(c[0] + 0.5) < 1e-12 and abs(c[1] - 3.0) < 1e-12, "ajuste lineal exacto")

# --- Curva sintética
dt = 120.0                      # s
n = 7 * 86400 // 120            # 5040 muestras
tt = np.arange(n) * dt          # s desde t0
td = tt / 86400.0               # d
rng = np.random.default_rng(15001)
x = 1 + 2e-3 * np.sin(2 * np.pi * td / 2.5) - 1e-4 * td + 5e-4 * rng.standard_normal(n)
hueco = (td >= 3.0) & (td < 3.5)
td_g, x_g = td[~hueco], x[~hueco]
print(f"muestras: {n}, con hueco: {x_g.size}, faltan {n - x_g.size} ({100*(n-x_g.size)/n:.1f} %)")
print(f"frecuencia de muestreo = {1/dt*1e3:.3f} mHz = {86400/dt:.0f} muestras/día; Nyquist = {43200/dt:.0f} ciclos/día")
print(f"media = {x.mean():.6f}; desviación estándar = {x.std(ddof=1):.6f}")
pend, orig = np.polyfit(td_g, x_g, 1)
print(f"tendencia ajustada: {pend*1e4:+.3f}e-4 por día (real -1.000e-4); orden en origen {orig:.6f}")
xd = x - (pend * td + orig)
print(f"desviación estándar tras quitar tendencia = {xd.std(ddof=1):.6f}")
k = int(2.5 * 86400 / dt)
print(f"r_k en medio periodo (k={k//2}) = {acf(xd, k//2):+.3f};  en un periodo (k={k}) = {acf(xd, k):+.3f}")
print("Pruebas superadas.")
