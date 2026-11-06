#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C19: reconstrucción de una serie con un hueco.

Datos: SINTÉTICOS, semilla fija. Serie de N = 256 muestras, suma de dos
oscilaciones periódicas en la ventana (bins 5 y 12 de la DFT):
    s[n] = cos(2 pi 5 n/N + 0.3) + 0.5 cos(2 pi 12 n/N - 1.1);
hueco de 20 muestras consecutivas (n = 100..119).
Métodos: (a) interpolación lineal; (b) ajuste por mínimos cuadrados de un
modelo de dos senoides de frecuencias conocidas; (c) extrapolación de banda
limitada de Gerchberg-Papoulis (alternar: imponer los datos, filtrar a la banda).
Referencias analíticas: (1) para A cos(w t) con datos en t = -a y t = +a, la
interpolación lineal da A cos(w a) en t = 0 y el error es A (1 - cos(w a));
(2) sin ruido y con el modelo correcto, el ajuste es exacto;
(3) con ruido sigma, el error en los puntos con datos del ajuste de p parámetros
tiene varianza media sigma^2 p/N_datos.
Supuestos: señal de banda limitada o de modelo conocido; ruido blanco.
Tolerancias: 1e-12 en (1); 1e-9 en (2); 15 % en (3).
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15019)
N = 256
n = np.arange(N)
s = np.cos(2 * np.pi * 5 * n / N + 0.3) + 0.5 * np.cos(2 * np.pi * 12 * n / N - 1.1)
hueco = (n >= 100) & (n < 120)
datos = ~hueco


def rmse(a, b, m):
    return float(np.sqrt(np.mean((a[m] - b[m]) ** 2)))


def interp_lineal(y):
    return np.interp(n, n[datos], y[datos])


def ajuste(y, bins=(5, 12)):
    cols = [np.ones(N)]
    for k in bins:
        cols += [np.cos(2 * np.pi * k * n / N), np.sin(2 * np.pi * k * n / N)]
    A = np.vstack(cols).T
    c, *_ = np.linalg.lstsq(A[datos], y[datos], rcond=None)
    return A @ c, A.shape[1]


def gerchberg_papoulis(y, kmax, it):
    x = np.where(datos, y, 0.0)
    hist = {}
    for i in range(1, it + 1):
        X = np.fft.rfft(x)
        X[kmax + 1:] = 0
        f = np.fft.irfft(X, N)
        x = np.where(datos, y, f)
        if i in (10, 100, 1000, it):
            hist[i] = x.copy()
    return x, hist


# (1) Interpolación lineal sobre un seno
a, w, A = 10.0, 0.2, 1.0
t = np.array([-a, 0.0, a])
y = A * np.cos(w * t)
mid = np.interp(0.0, [-a, a], [y[0], y[2]])
print(f"(1) interpolación lineal de A cos(w t) con a = {a}, w = {w}: error en t=0 = {abs(y[1]-mid):.6f} (A(1-cos(w a)) = {A*(1-np.cos(w*a)):.6f})")
prueba(abs(abs(y[1] - mid) - A * (1 - np.cos(w * a))) < 1e-12, "error de interpolación analítico")

# (2) Sin ruido
lin = interp_lineal(s)
mod, p = ajuste(s)
print(f"(2) sin ruido, error RMS en el hueco (20 muestras): interpolación lineal {rmse(lin, s, hueco):.4f}; "
      f"ajuste del modelo {rmse(mod, s, hueco):.2e}")
prueba(rmse(mod, s, hueco) < 1e-9, "ajuste exacto sin ruido")

gp, hist = gerchberg_papoulis(s, 14, 5000)
print("    Gerchberg-Papoulis (banda hasta el bin 14), error RMS en el hueco: "
      + ", ".join(f"{k} it.: {rmse(v, s, hueco):.2e}" for k, v in hist.items()))
prueba(rmse(gp, s, hueco) < 0.05 * rmse(lin, s, hueco), "G-P mejora a la lineal")

# (3) Con ruido
sg = 0.1
reps = 300
e_lin, e_mod, e_gp, e_dat = [], [], [], []
for _ in range(reps):
    y = s + sg * rng.standard_normal(N)
    e_lin.append(interp_lineal(y)[hueco] - s[hueco])
    m_, p = ajuste(y)
    e_mod.append(m_[hueco] - s[hueco])
    e_dat.append(m_[datos] - s[datos])
    g_, _ = gerchberg_papoulis(y, 14, 300)
    e_gp.append(g_[hueco] - s[hueco])
r = lambda e: float(np.sqrt(np.mean(np.concatenate(e) ** 2)))
teo = sg * np.sqrt(p / datos.sum())
print(f"(3) con ruido sigma = {sg}: RMS en el hueco: lineal {r(e_lin):.4f}; modelo {r(e_mod):.4f}; G-P (300 it.) {r(e_gp):.4f}")
print(f"    RMS del ajuste en los puntos con datos: {r(e_dat):.4f} (teoría sigma sqrt(p/N_datos) = {teo:.4f})")
prueba(abs(r(e_dat) / teo - 1) < 0.15, "varianza del ajuste en los datos")
prueba(r(e_mod) < r(e_lin), "el modelo reconstruye mejor que la interpolación lineal")

# (4) Modelo equivocado: una frecuencia olvidada
mod1, _ = ajuste(s, bins=(5,))
print(f"(4) con el modelo incompleto (solo bin 5), sin ruido: error RMS en el hueco {rmse(mod1, s, hueco):.3f}; en los datos {rmse(mod1, s, datos):.3f}")
prueba(rmse(mod1, s, hueco) > 0.1, "un modelo incompleto reconstruye mal")
print("Pruebas superadas.")
