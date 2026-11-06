#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C04: transformada discreta de Fourier (DFT) directa.

Datos: SINTÉTICOS. Definición: X[k] = sum_{n=0}^{N-1} x[n] exp(-2 pi i k n/N).
Se implementa por la suma directa (O(N^2)) y se contrasta con (a) el resultado
analítico de un coseno con k0 entero: X[k0] = X[N-k0] = N/2; (b) la identidad
de Parseval: sum|x|^2 = (1/N) sum|X|^2; (c) el teorema de convolución
circular; (d) numpy.fft.fft como referencia independiente.
Supuestos: señal periódica con periodo N (implícito en la DFT).
Tolerancia: 1e-9 relativa.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def dft(x):
    N = len(x)
    n = np.arange(N)
    W = np.exp(-2j * np.pi * np.outer(n, n) / N)
    return W @ x


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
N, k0 = 64, 5
n = np.arange(N)
x = np.cos(2 * np.pi * k0 * n / N)
X = dft(x)
print(f"|X[{k0}]| = {abs(X[k0]):.6f}, |X[{N-k0}]| = {abs(X[N-k0]):.6f} (analítico {N/2})")
prueba(abs(abs(X[k0]) - N / 2) < 1e-9 and abs(abs(X[N - k0]) - N / 2) < 1e-9, "coseno")
resto = np.delete(np.abs(X), [k0, N - k0]).max()
print(f"máximo en los otros bins = {resto:.2e}")
prueba(resto < 1e-9, "fuga nula con k0 entero")
rng = np.random.default_rng(15004)
y = rng.standard_normal(N)
Y = dft(y)
e1, e2 = np.sum(y**2), np.sum(abs(Y)**2) / N
print(f"Parseval: sum|y|^2 = {e1:.9f}; (1/N) sum|Y|^2 = {e2:.9f}")
prueba(abs(e1 - e2) < 1e-9 * e1, "Parseval")
h = rng.standard_normal(N)
conv = np.array([sum(y[m] * h[(i - m) % N] for m in range(N)) for i in range(N)])
via = np.real(np.fft.ifft(dft(y) * dft(h)))
d = np.max(np.abs(conv - via))
print(f"convolución circular directa vs producto de DFT: diferencia máxima {d:.2e}")
prueba(d < 1e-9, "teorema de convolución")
dif = np.max(np.abs(Y - np.fft.fft(y)))
print(f"DFT directa vs numpy.fft.fft: {dif:.2e}")
prueba(dif < 1e-9, "contra numpy")
# fuga: k0 no entero
x2 = np.cos(2 * np.pi * 5.5 * n / N)
X2 = np.abs(dft(x2))
print(f"k0 = 5,5: |X[5]| = {X2[5]:.3f}, |X[6]| = {X2[6]:.3f}, |X[20]| = {X2[20]:.3f} (fuga)")
print("Pruebas superadas.")
