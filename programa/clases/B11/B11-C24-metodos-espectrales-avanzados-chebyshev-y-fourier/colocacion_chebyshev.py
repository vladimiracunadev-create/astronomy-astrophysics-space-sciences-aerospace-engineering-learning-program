#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C24: colocación de Chebyshev frente a Fourier y diferencias finitas.

Datos SINTÉTICOS: problema de contorno u'' = exp(4x) en [-1, 1], u(-1) = u(1) = 0,
con solución exacta u = (exp(4x) - x sinh 4 - cosh 4)/16; función no periódica
f = exp(x) para la derivada. No hay datos de misión.
Modelo: matriz de diferenciación de Chebyshev D en los nodos x_j = cos(pi j / N):
D_ij = (c_i/c_j) / (x_i - x_j) (i != j), D_ii = -sum_{j != i} D_ij, con c_0 = c_N = 2
y c_j = 1 en el resto, multiplicado por (-1)^j. La ecuación se coloca en los nodos
interiores usando D^2 y las condiciones de contorno se imponen quitando las filas y
columnas de los extremos.
Referencias independientes: soluciones exactas; diferencias finitas centrales de
segundo orden (DLMF 3.4.6 / 3.4.22) en malla uniforme del mismo número de puntos.
Supuestos: solución suave (analítica) en el intervalo. Validez: N moderado (el
condicionamiento de D^2 crece como N^4).
Tolerancia: D exacta (< 1e-9) para x^k con k <= N; error de la colocación < 1e-11
con N = 24; la diferencia finita con 25 puntos debe tener un error al menos 1e5
veces mayor; la derivada de Fourier de una función no periódica no converge
(error > 0.1); el radio espectral de D^2 debe crecer ~ 16 veces al duplicar N.
"""
import math, platform
import numpy as np


def cheb(N):
    x = np.cos(np.pi * np.arange(N + 1) / N)
    c = np.ones(N + 1); c[0] = c[-1] = 2.0
    c = c * (-1.0) ** np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    dX = X - X.T
    D = np.outer(c, 1.0 / c) / (dX + np.eye(N + 1))
    D = D - np.diag(D.sum(axis=1))
    return D, x


print(f"Python {platform.python_version()}; NumPy {np.__version__}")
# 1) exactitud de D en polinomios
D, x = cheb(16)
err_pol = max(np.max(np.abs(D @ x**k - (k * x ** (k - 1) if k > 0 else 0 * x))) for k in range(0, 17))
print(f"1) N=16: error máximo de D sobre x^k, k = 0..16: {err_pol:.2e}")
assert err_pol < 1e-9

# 2) BVP u'' = exp(4x)
exacta = lambda t: (np.exp(4 * t) - t * math.sinh(4) - math.cosh(4)) / 16
print("2) u'' = exp(4x), u(±1) = 0: error máximo en los nodos")
errc = {}
for N in (4, 8, 12, 16, 24, 32):
    D, x = cheb(N)
    D2 = (D @ D)[1:-1, 1:-1]
    u = np.zeros(N + 1)
    u[1:-1] = np.linalg.solve(D2, np.exp(4 * x[1:-1]))
    errc[N] = float(np.max(np.abs(u - exacta(x))))
    print(f"   Chebyshev N={N:2d}: {errc[N]:.3e}", end="")
    # diferencias finitas con N+1 puntos uniformes
    h = 2.0 / N
    xs = -1 + h * np.arange(N + 1)
    A = (np.diag(-2 * np.ones(N - 1)) + np.diag(np.ones(N - 2), 1) + np.diag(np.ones(N - 2), -1)) / h**2
    ufd = np.zeros(N + 1)
    ufd[1:-1] = np.linalg.solve(A, np.exp(4 * xs[1:-1]))
    efd = float(np.max(np.abs(ufd - exacta(xs))))
    print(f"   | diferencias finitas: {efd:.3e}")
    if N == 24:
        efd24 = efd
assert errc[24] < 1e-11 and efd24 > 1e5 * errc[24]

# 3) Fourier sobre una función no periódica
print("3) derivada de exp(x) en [-1, 1] (no periódica): Chebyshev frente a Fourier en malla uniforme")
for N in (16, 32, 64):
    D, x = cheb(N)
    e_ch = np.max(np.abs(D @ np.exp(x) - np.exp(x)))
    xu = np.linspace(-1, 1, N, endpoint=False)
    k = np.fft.fftfreq(N, d=2.0 / N) * 2 * np.pi
    k[N // 2] = 0.0
    dF = np.real(np.fft.ifft(1j * k * np.fft.fft(np.exp(xu))))
    e_f = np.max(np.abs(dF - np.exp(xu)))
    print(f"   N={N:2d}: Chebyshev {e_ch:.2e} | Fourier {e_f:.2e}")
    if N == 64:
        assert e_f > 0.1 and e_ch < 1e-9

# 4) radio espectral de D^2 interior
print("4) radio espectral de D^2 (nodos interiores):")
rho = {}
for N in (8, 16, 32, 64):
    D, x = cheb(N)
    rho[N] = float(np.max(np.abs(np.linalg.eigvals((D @ D)[1:-1, 1:-1]))))
    print(f"   N={N:2d}: rho = {rho[N]:.4e} ; rho/N^4 = {rho[N]/N**4:.4f}")
r1, r2 = rho[32] / rho[16], rho[64] / rho[32]
print(f"   razones al duplicar N: {r1:.2f}, {r2:.2f} (se espera ~16)")
assert 13 < r2 < 17
print("Pruebas superadas.")
