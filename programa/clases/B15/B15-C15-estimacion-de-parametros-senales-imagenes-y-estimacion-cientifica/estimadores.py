#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C15: estimadores, sesgo, varianza y cota de Cramér-Rao.

Datos: SINTÉTICOS, semilla fija (simulación de Monte Carlo con verdad conocida).
Referencias analíticas:
 (1) media de N datos N(mu, s^2): sin sesgo, desviación s/sqrt(N) = cota CR;
 (2) varianza con divisor N: E = (N-1)/N s^2; con N-1: E = s^2;
     ECM(divisor N) = (2N-1) s^4/N^2 < ECM(divisor N-1) = 2 s^4/(N-1);
 (3) tasa de Poisson: MLE = media muestral, información de Fisher N/lambda,
     cota lambda/N;
 (4) centroide de N fotones con perfil gaussiano de sigma_p: MLE = media de las
     posiciones, desviación sigma_p/sqrt(N) (cota CR);
 (5) tasa de una exponencial: MLE = 1/media; E[MLE] = lambda N/(N-1) (sesgo
     grande con N pequeño).
Supuestos: datos independientes e idénticamente distribuidos.
Tolerancias: 3 desviaciones del propio Monte Carlo.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15015)
M = 200000

# (1) Media gaussiana
N, mu, s = 25, 10.0, 3.0
x = rng.normal(mu, s, (M, N))
med = x.mean(1)
print(f"(1) media (N={N}): sesgo {med.mean()-mu:+.5f}; desviación {med.std():.5f} (cota CR s/sqrt(N) = {s/np.sqrt(N):.5f})")
prueba(abs(med.mean() - mu) < 4 * s / np.sqrt(N * M) and abs(med.std() / (s / np.sqrt(N)) - 1) < 0.01, "media")

# (2) Varianza con divisor N y N-1
N = 5
x = rng.normal(0, s, (M, N))
vN, vN1 = x.var(1, ddof=0), x.var(1, ddof=1)
ecmN = np.mean((vN - s**2) ** 2)
ecmN1 = np.mean((vN1 - s**2) ** 2)
print(f"(2) N={N}: E[var/N] = {vN.mean():.4f} (teoría {(N-1)/N*s**2:.4f}); E[var/(N-1)] = {vN1.mean():.4f} (teoría {s**2:.4f})")
print(f"    ECM divisor N = {ecmN:.3f} (teoría {(2*N-1)*s**4/N**2:.3f}); ECM divisor N-1 = {ecmN1:.3f} (teoría {2*s**4/(N-1):.3f})")
prueba(abs(vN.mean() / ((N - 1) / N * s**2) - 1) < 0.01 and abs(vN1.mean() / s**2 - 1) < 0.01, "sesgos de la varianza")
prueba(ecmN < ecmN1 and abs(ecmN / ((2 * N - 1) * s**4 / N**2) - 1) < 0.02, "ECM de la varianza")

# (3) Poisson
lam, N = 4.0, 50
k = rng.poisson(lam, (M // 4, N))
lh = k.mean(1)
grid = np.linspace(2, 6, 4001)
d = k[0]
ll = np.array([np.sum(d * np.log(g) - g) for g in grid])
print(f"(3) Poisson: MLE numérico de una muestra = {grid[np.argmax(ll)]:.4f}, media muestral = {d.mean():.4f}")
print(f"    desviación del MLE = {lh.std():.4f} (cota CR sqrt(lambda/N) = {np.sqrt(lam/N):.4f})")
prueba(abs(grid[np.argmax(ll)] - d.mean()) < 2e-3 and abs(lh.std() / np.sqrt(lam / N) - 1) < 0.02, "Poisson")

# (4) Centroide de fotones
N, sp = 100, 2.0
pos = rng.normal(7.3, sp, (M // 4, N))
c = pos.mean(1)
print(f"(4) centroide de {N} fotones, sigma_p = {sp}: desviación {c.std():.4f} (cota CR sigma_p/sqrt(N) = {sp/np.sqrt(N):.4f})")
prueba(abs(c.std() / (sp / np.sqrt(N)) - 1) < 0.02, "centroide")

# (5) Exponencial
lam, N = 2.0, 5
t = rng.exponential(1 / lam, (M, N))
ml = 1 / t.mean(1)
print(f"(5) tasa exponencial, N={N}: E[MLE] = {ml.mean():.3f} (teoría lambda N/(N-1) = {lam*N/(N-1):.3f}); sesgo {100*(ml.mean()/lam-1):.0f} %")
prueba(abs(ml.mean() / (lam * N / (N - 1)) - 1) < 0.02, "sesgo del MLE exponencial")
print("Pruebas superadas.")
