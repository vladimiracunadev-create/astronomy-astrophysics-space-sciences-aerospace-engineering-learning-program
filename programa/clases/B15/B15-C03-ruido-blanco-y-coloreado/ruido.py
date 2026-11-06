#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C03: ruido blanco, AR(1) y paseo aleatorio.

Datos: SINTÉTICOS, semilla fija. Modelos: blanco w[n]~N(0,s^2);
AR(1) x[n]=phi x[n-1]+w[n] (r_1 teórico = phi); paseo aleatorio = suma
acumulada de w (espectro ~ 1/f^2). Para ruido blanco la desviación estándar de
la media de N datos es s/sqrt(N).
Supuestos: gaussiano, estacionario (salvo el paseo). Validez: N grande.
Tolerancias: 3 sigma estadísticos en cada prueba.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def r1(x):
    m = x.mean()
    return float(np.sum((x[:-1] - m) * (x[1:] - m)) / np.sum((x - m) ** 2))


def pendiente_psd(x):
    P = np.abs(np.fft.rfft(x - x.mean())) ** 2
    f = np.fft.rfftfreq(x.size)[1:]
    P = P[1:]
    sel = (f > 0.001) & (f < 0.2)
    return float(np.polyfit(np.log10(f[sel]), np.log10(P[sel]), 1)[0])


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
N, s = 4096, 1.0
rng = np.random.default_rng(15003)
w = s * rng.standard_normal(N)
phi = 0.9
a = np.zeros(N)
for n in range(1, N):
    a[n] = phi * a[n - 1] + w[n]
rw = np.cumsum(w)
for nom, x in [("blanco", w), ("AR(1) phi=0.9", a), ("paseo aleatorio", rw)]:
    print(f"{nom:16s} r_1 = {r1(x):+.3f}; pendiente del espectro = {pendiente_psd(x):+.2f}")
tol = 3 / np.sqrt(N)
prueba(abs(r1(w)) < tol, "r1 del ruido blanco ~ 0")
prueba(abs(r1(a) - phi) < 0.05, "r1 del AR(1) ~ phi")
prueba(abs(pendiente_psd(w)) < 0.3, "espectro blanco plano")
prueba(abs(pendiente_psd(rw) + 2) < 0.3, "espectro del paseo ~ -2")
# desviación de la media: 400 realizaciones de 256 datos
M, L = 400, 256
bl = rng.standard_normal((M, L))
mb = bl.mean(axis=1).std(ddof=1)
ar = np.zeros((M, L))
ww = rng.standard_normal((M, L))
for n in range(1, L):
    ar[:, n] = phi * ar[:, n - 1] + ww[:, n]
ma = ar.mean(axis=1).std(ddof=1)
teo = np.sqrt(1 / (1 - phi**2)) * np.sqrt((1 + phi) / (1 - phi)) / np.sqrt(L)
print(f"sigma(media, N={L}): blanco {mb:.4f} (teoría {1/np.sqrt(L):.4f}); AR(1) {ma:.4f} (teoría aprox. {teo:.4f})")
prueba(abs(mb - 1 / np.sqrt(L)) < 0.15 / np.sqrt(L), "sigma de la media, ruido blanco")
prueba(ma > 3 * mb, "el ruido rojo promedia peor")
print("Pruebas superadas.")
