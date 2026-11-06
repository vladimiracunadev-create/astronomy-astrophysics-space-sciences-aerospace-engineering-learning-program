#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C05: FFT de base 2 (dividir y combinar) y su coste.

Datos: SINTÉTICOS (ruido gaussiano con semilla fija y señales exactas).
Modelo: X[k] = E[k] + W^k O[k] y X[k+N/2] = E[k] - W^k O[k], con
W = exp(-2 pi i/N), E y O las DFT de las muestras pares e impares
(esquema de Cooley y Tukey, descrito en la documentación de NumPy como origen
de la FFT moderna). El coste se mide CONTANDO mariposas: (N/2) log2 N.
Supuestos: N potencia de 2 en la implementación propia; NumPy admite otros N.
Validez: orden de magnitud del coste, no tiempos absolutos (dependen del
equipo). Tolerancia: 1e-9 entre FFT propia, DFT directa y numpy.fft.fft;
los conteos deben coincidir exactamente con la fórmula.
"""
import platform
import sys
import time

import numpy as np

CUENTA = [0]


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def fft_rec(x):
    N = len(x)
    if N == 1:
        return x.astype(complex)
    E = fft_rec(x[0::2])
    O = fft_rec(x[1::2])
    W = np.exp(-2j * np.pi * np.arange(N // 2) / N)
    T = W * O
    CUENTA[0] += N // 2          # una mariposa por cada k
    return np.concatenate([E + T, E - T])


def dft(x):
    N = len(x)
    n = np.arange(N)
    return np.exp(-2j * np.pi * np.outer(n, n) / N) @ x


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15005)

# Pruebas exactas
x = rng.standard_normal(256)
d1 = np.max(np.abs(fft_rec(x) - dft(x)))
d2 = np.max(np.abs(fft_rec(x) - np.fft.fft(x)))
print(f"FFT propia vs DFT directa (N=256): {d1:.2e}; vs numpy: {d2:.2e}")
prueba(d1 < 1e-9 and d2 < 1e-9, "FFT propia")
imp = np.zeros(64)
imp[0] = 1
prueba(np.allclose(fft_rec(imp), np.ones(64)), "impulso -> espectro plano")
prueba(abs(fft_rec(np.ones(64))[0] - 64) < 1e-12, "constante -> N en k=0")

# Conteo de mariposas
print("N        mariposas  (N/2)log2N   N^2        N^2 / mariposas")
for m in range(3, 16, 2):
    N = 2**m
    CUENTA[0] = 0
    fft_rec(rng.standard_normal(N))
    esperado = (N // 2) * m
    prueba(CUENTA[0] == esperado, f"conteo N={N}")
    print(f"{N:<8d} {CUENTA[0]:<10d} {esperado:<12d} {N*N:<10d} {N*N/CUENTA[0]:.1f}")

# Caso de la clase: 27 d a 120 s
N27 = 27 * 720
Np = 1 << (N27 - 1).bit_length()
print(f"27 d a 120 s: N = {N27}; potencia de 2 siguiente = {Np}; "
      f"N^2 = {N27**2:.3e}; (N/2)log2N con N = {Np}: {Np//2*int(np.log2(Np))}")

# Orden de los bins
print("fftfreq(8, d=1) =", np.fft.fftfreq(8, 1.0).tolist())
prueba(np.allclose(np.fft.fftfreq(8, 1.0), [0, .125, .25, .375, -.5, -.375, -.25, -.125]), "orden")

# Relleno con ceros: mismo pico, rejilla más fina
n = np.arange(N27)
senal = np.cos(2 * np.pi * 56.25 / 720.0 * n)
for N in (N27, Np):
    X = np.abs(np.fft.rfft(senal, N))
    f = np.fft.rfftfreq(N, 120.0 / 86400.0)
    print(f"  N usado = {N}: pico en {f[np.argmax(X)]:.4f} c/d, resolución de rejilla {f[1]:.5f} c/d")

# Tiempos (orientativos)
x = rng.standard_normal(2048)
t0 = time.perf_counter(); dft(x); t1 = time.perf_counter()
fft_rec(x); t2 = time.perf_counter()
np.fft.fft(x); t3 = time.perf_counter()
print(f"tiempos N=2048 (orientativos, dependen del equipo): DFT {1e3*(t1-t0):.1f} ms; "
      f"FFT propia {1e3*(t2-t1):.1f} ms; numpy {1e3*(t3-t2):.3f} ms")
print("Pruebas superadas.")
