#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C16: derivada espectral con la transformada rápida de Fourier.

Datos SINTÉTICOS: señal periódica f(x) = exp(sin x) en [0, 2 pi) (una temperatura
normalizada a lo largo de una órbita o de una vuelta de giro del vehículo); señal no
suave de comparación: onda diente de sierra. Difusividad nominal alpha = 0.1 (en
unidades del problema normalizado) para la ecuación del calor periódica.
Modelo: f'(x) = sum_k i k f_k e^{ikx}; la derivada espectral multiplica los
coeficientes de Fourier por i k (se anula el modo de Nyquist en la derivada
primera). La ecuación u_t = alpha u_xx periódica se integra en el tiempo de forma
exacta por modo: u_k(t) = u_k(0) exp(-alpha k^2 t).
Referencia independiente: derivada analítica f' = cos x exp(sin x) y
diferencia central de 3 puntos (DLMF 3.4.6).
Supuestos: función periódica y muestreada en malla uniforme. Validez: debe
estar bien resuelta (decae su espectro) en N puntos.
Tolerancia: error espectral < 1e-12 para N = 32 en la señal suave; la diferencia
central debe tener orden 2 (razón en [3.5, 4.5]); el error espectral de la
señal no suave NO debe converger (error de orden 1 lejos del salto).
"""
import math, platform
import numpy as np


def derivada_espectral(f_vals):
    N = len(f_vals)
    k = np.fft.fftfreq(N, d=1.0 / N)
    k[N // 2] = 0.0 if N % 2 == 0 else k[N // 2]          # modo de Nyquist
    return np.real(np.fft.ifft(1j * k * np.fft.fft(f_vals)))


def derivada_central(f_vals, h):
    return (np.roll(f_vals, -1) - np.roll(f_vals, 1)) / (2 * h)


print(f"Python {platform.python_version()}; NumPy {np.__version__}")
f = lambda x: np.exp(np.sin(x))
df = lambda x: np.cos(x) * np.exp(np.sin(x))
print("señal suave exp(sin x): error máximo de la derivada")
e_esp, e_fd = {}, {}
for N in (4, 8, 12, 16, 24, 32, 64):
    x = 2 * np.pi * np.arange(N) / N
    e_esp[N] = float(np.max(np.abs(derivada_espectral(f(x)) - df(x))))
    e_fd[N] = float(np.max(np.abs(derivada_central(f(x), 2 * np.pi / N) - df(x))))
    print(f"  N={N:3d}: espectral = {e_esp[N]:.3e} | diferencia central = {e_fd[N]:.3e}")
assert e_esp[32] < 1e-12
razones = [e_fd[16] / e_fd[32], e_fd[32] / e_fd[64]]
print("  razones de la diferencia central:", " ".join(f"{q:.3f}" for q in razones))
assert all(3.5 < q < 4.5 for q in razones)
# cuántos puntos necesita la diferencia central para 1e-12
print(f"  la diferencia central en N=64 sigue en {e_fd[64]:.2e}; espectral logra <1e-12 con N=24 -> {e_esp[24]:.2e}")

# aliasing: sin(5x) muestreada con N = 8 aparece como sin(-3x) = -sin(3x)
N = 8
x = 2 * np.pi * np.arange(N) / N
alias = np.max(np.abs(np.sin(5 * x) + np.sin(3 * x)))
print(f"aliasing: sin(5x) muestreada con N=8 coincide con -sin(3x) (diferencia {alias:.1e})")
assert alias < 1e-12

# señal no suave: diente de sierra
print("diente de sierra (no suave), error en puntos lejos del salto:")
E = {}
for N in (32, 64, 128, 256):
    x = 2 * np.pi * np.arange(N) / N
    s = (x - np.pi) / np.pi                     # pendiente 1/pi, salto en x = 0
    ds = derivada_espectral(s)
    lejos = (x > 1.0) & (x < 2 * np.pi - 1.0)
    E[N] = float(np.max(np.abs(ds[lejos] - 1 / np.pi)))
    print(f"  N={N:3d}: error = {E[N]:.3e} (oscilaciones de Gibbs; máx|ds| = {np.max(np.abs(ds)):.2f})")
assert E[256] > 0.1 and E[256] >= 0.9 * E[32]   # no converge: el error sigue siendo O(1)
assert E[256] > 1e5 * e_esp[32]

# ecuación del calor periódica, exacta por modo
alpha, tf, N = 0.1, 2.0, 32
x = 2 * np.pi * np.arange(N) / N
u0 = np.sin(x) + 0.5 * np.sin(3 * x)
k = np.fft.fftfreq(N, d=1.0 / N)
u = np.real(np.fft.ifft(np.fft.fft(u0) * np.exp(-alpha * k**2 * tf)))
uex = np.exp(-alpha * tf) * np.sin(x) + 0.5 * np.exp(-9 * alpha * tf) * np.sin(3 * x)
err = float(np.max(np.abs(u - uex)))
print(f"calor periódico (alpha={alpha}, t={tf}): error máximo = {err:.2e}; u(pi/2) = {u[N//4]:.6f} (exacto {uex[N//4]:.6f})")
assert err < 1e-14
print("Pruebas superadas.")
