#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C08: convolución discreta y respuesta impulsional.

Datos: SINTÉTICOS. Sensor térmico ficticio de primer orden (constante de
tiempo tau = 30 s) muestreado cada 1 s ante un cambio brusco de temperatura
de 300 K a 250 K (entrada en escalón).
Modelo: y[n] = sum_m h[m] x[n-m] con h[n] = a (1-a)^n, a = 1 - exp(-dt/tau).
Referencia analítica: para un escalón de amplitud DT, la respuesta del sistema
continuo es DT (1 - exp(-t/tau)); la discreta coincide en t = (n+1) dt.
Otras referencias: numpy.convolve y el teorema de convolución con FFT con
relleno de ceros a N+M-1 (la circular sin relleno se desvía).
Supuestos: sistema lineal e invariante. Validez: sensor lineal, sin saturación.
Tolerancias: 1e-12 en la respuesta analítica, 1e-9 entre métodos.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def conv_directa(x, h):
    N, M = len(x), len(h)
    y = np.zeros(N + M - 1)
    for n in range(N):
        for m in range(M):
            y[n + m] += x[n] * h[m]
    return y


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15008)

# (1) Ejemplo mínimo a mano
x = np.array([1.0, 2.0, 3.0])
h = np.array([1.0, 0.0, -1.0])
y = conv_directa(x, h)
print("(1) [1,2,3] * [1,0,-1] =", y.tolist())
prueba(np.allclose(y, [1, 2, 2, -2, -3]), "convolución a mano")

# (2) Propiedades
a, b, c = rng.standard_normal(20), rng.standard_normal(7), rng.standard_normal(5)
prueba(np.allclose(np.convolve(a, b), np.convolve(b, a)), "conmutativa")
prueba(np.allclose(np.convolve(np.convolve(a, b), c), np.convolve(a, np.convolve(b, c))), "asociativa")
prueba(np.allclose(np.convolve(a, b + 0), conv_directa(a, b)), "directa = numpy")
prueba(len(np.convolve(a, b)) == 20 + 7 - 1, "longitud N+M-1")
print("(2) conmutativa, asociativa y longitud N+M-1: verificadas")

# (3) Teorema de convolución con y sin relleno
N, M = 64, 9
x = rng.standard_normal(N)
h = rng.standard_normal(M)
lineal = np.convolve(x, h)
L = N + M - 1
via = np.real(np.fft.ifft(np.fft.fft(x, L) * np.fft.fft(h, L)))
circ = np.real(np.fft.ifft(np.fft.fft(x, N) * np.fft.fft(h, N)))
err_pad = np.max(np.abs(lineal - via))
err_circ = np.max(np.abs(lineal[:N] - circ))
print(f"(3) FFT con relleno a N+M-1: error {err_pad:.1e}; circular sin relleno: error {err_circ:.2f}")
prueba(err_pad < 1e-9, "convolución por FFT con relleno")
prueba(err_circ > 0.1, "la circular sin relleno se desvía")

# (4) Sensor térmico: respuesta al escalón contra la analítica
tau, dt, T0, T1 = 30.0, 1.0, 300.0, 250.0
a_ = 1 - np.exp(-dt / tau)
Nt = 400
n = np.arange(Nt)
h = a_ * (1 - a_) ** n
u = np.ones(Nt)                                     # escalón unitario
y = np.convolve(h, u)[:Nt]
teo = 1 - np.exp(-(n + 1) * dt / tau)
d = np.max(np.abs(y - teo))
print(f"(4) sensor tau = {tau:.0f} s: respuesta al escalón vs analítica, diferencia máx. = {d:.1e}")
prueba(d < 1e-12, "respuesta analítica del sensor")
print(f"    área de h = {h.sum():.6f} (ganancia en continua = 1)")
T = T0 + (T1 - T0) * y
for t in (1, 30, 60, 138):
    print(f"    t = {t:3d} s: lectura {T[t-1]:.2f} K (cambio real {T1-T0:.0f} K; fracción {y[t-1]:.3f})")
t99 = np.argmax(y >= 0.99) + 1
print(f"    el 99 % del salto se alcanza en {t99} s (teoría tau ln 100 = {tau*np.log(100):.1f} s)")

# (5) Linealidad e invariancia
x1, x2 = rng.standard_normal(100), rng.standard_normal(100)
y_suma = np.convolve(h, 2 * x1 + 3 * x2)
y_comb = 2 * np.convolve(h, x1) + 3 * np.convolve(h, x2)
despl = np.concatenate([np.zeros(10), x1])
y_despl = np.convolve(h, despl)
y_base = np.concatenate([np.zeros(10), np.convolve(h, x1)])
prueba(np.allclose(y_suma, y_comb) and np.allclose(y_despl, y_base), "linealidad e invariancia")
print("(5) linealidad y invariancia en el tiempo: verificadas")
print("Pruebas superadas.")
