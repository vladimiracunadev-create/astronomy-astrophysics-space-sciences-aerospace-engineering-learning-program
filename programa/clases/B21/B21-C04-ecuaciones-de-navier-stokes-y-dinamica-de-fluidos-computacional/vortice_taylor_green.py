#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B21-C04: Navier-Stokes incompresible por método de proyección (vórtice de Taylor-Green).

Datos: SINTETICOS y adimensionales. Campo inicial de Taylor-Green en [0, 2 pi)^2 periódico,
u = -cos x sin y, v = sin x cos y (velocidad U = 1, longitud L = 1), viscosidad
cinemática nu = 0.1 (número de Reynolds Re = U L / nu = 10), densidad 1.
Modelo: u_t + (u.grad)u = -grad p + nu lap u,  div u = 0.
Solución exacta (se verifica sustituyendo en las ecuaciones, ver clase):
u = -cos x sin y e^{-2 nu t}, v = sin x cos y e^{-2 nu t},
p = -(1/4)(cos 2x + cos 2y) e^{-4 nu t}; energía cinética E(t) = E(0) e^{-4 nu t}.
Método: diferencias centradas de segundo orden en malla colocada; Heun (RK2) con
proyección tras cada etapa; el problema de Poisson de la presión se resuelve por FFT
con el símbolo exacto del operador discreto div(grad) de estencil ancho, de modo que la
divergencia discreta central queda al nivel del redondeo.
Supuestos: periodico, malla uniforme, un solo fluido, sin turbulencia modelada.
Validez: Re moderado y solución suave (sin choques); la malla colocada puede
admitir modos de damero, que aquí no se excitan.
Tolerancias (las pruebas detienen la ejecución si fallan): divergencia discreta
< 1e-10; error de la energía frente a e^{-4 nu t} < 1e-2 relativo en N=16 (y decreciente con N);
orden espacial observado de la velocidad en [1.9, 2.1]; límite de estabilidad
difusivo de Heun dt <= h^2/(4 nu): estable al 90 % e inestable al 130 %.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()}  NumPy {np.__version__}")

NU = 0.1


def derivadas(f, h):
    fx = (np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)) / (2 * h)
    fy = (np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)) / (2 * h)
    return fx, fy


def laplaciano(f, h):
    return (np.roll(f, -1, 0) + np.roll(f, 1, 0) + np.roll(f, -1, 1) + np.roll(f, 1, 1) - 4 * f) / h**2


def preparar_proyeccion(N, h):
    k = 2 * math.pi * np.fft.fftfreq(N, d=h)
    sx = np.sin(k * h) / h
    SX, SY = np.meshgrid(sx, sx, indexing="ij")
    simbolo = -(SX**2 + SY**2)  # div(grad) de estencil ancho
    simbolo[np.abs(simbolo) < 1e-14] = 1.0
    return SX, SY, simbolo


def proyectar(u, v, h, prep):
    SX, SY, simbolo = prep
    uh, vh = np.fft.fft2(u), np.fft.fft2(v)
    div = 1j * (SX * uh + SY * vh)
    phi = div / simbolo
    phi[np.abs(simbolo) == 1.0] = 0.0
    return np.real(np.fft.ifft2(uh - 1j * SX * phi)), np.real(np.fft.ifft2(vh - 1j * SY * phi))


def rhs(u, v, h):
    ux, uy = derivadas(u, h)
    vx, vy = derivadas(v, h)
    return (-(u * ux + v * uy) + NU * laplaciano(u, h),
            -(u * vx + v * vy) + NU * laplaciano(v, h))


def paso(u, v, dt, h, prep):
    k1u, k1v = rhs(u, v, h)
    u1, v1 = proyectar(u + dt * k1u, v + dt * k1v, h, prep)
    k2u, k2v = rhs(u1, v1, h)
    return proyectar(0.5 * u + 0.5 * (u1 + dt * k2u), 0.5 * v + 0.5 * (v1 + dt * k2v), h, prep)


def divergencia_max(u, v, h):
    ux, _ = derivadas(u, h)
    _, vy = derivadas(v, h)
    return float(np.max(np.abs(ux + vy)))


def ejecutar(N, tfin, dt):
    h = 2 * math.pi / N
    x = np.arange(N) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    u, v = -np.cos(X) * np.sin(Y), np.sin(X) * np.cos(Y)
    prep = preparar_proyeccion(N, h)
    n = int(round(tfin / dt))
    for _ in range(n):
        u, v = paso(u, v, dt, h, prep)
    return X, Y, u, v, h, n * dt


# (a) exactitud frente a la solución analítica
print("(a) Taylor-Green, nu = 0.1, t = 1, dt = 0.005")
errs = []
for N in (8, 16, 32, 64):
    X, Y, u, v, h, t = ejecutar(N, 1.0, 0.005)
    ue, ve = -np.cos(X) * np.sin(Y) * math.exp(-2 * NU * t), np.sin(X) * np.cos(Y) * math.exp(-2 * NU * t)
    err = float(max(np.max(np.abs(u - ue)), np.max(np.abs(v - ve))))
    E = 0.5 * float(np.mean(u**2 + v**2))
    E0 = 0.5 * float(np.mean(np.cos(X)**2 * np.sin(Y)**2 + np.sin(X)**2 * np.cos(Y)**2))
    div = divergencia_max(u, v, h)
    errs.append(err)
    rel_E = E / E0 / math.exp(-4 * NU * t) - 1
    print(f"    N={N:3d}  error max velocidad = {err:.4e}  E/E0 = {E/E0:.6f} (exacta {math.exp(-4*NU*t):.6f})  "
          f"|div| max = {div:.1e}")
    assert div < 1e-10, "divergencia"
    if N == 16:
        assert abs(rel_E) < 1e-2
ords = [math.log2(errs[i] / errs[i + 1]) for i in range(1, 3)]
print("    orden observado (N=16->32->64):", " ".join(f"{o:.3f}" for o in ords))
assert all(1.9 <= o <= 2.1 for o in ords), "orden"

# (b) límite de estabilidad difusivo de Heun
print("(b) estabilidad difusiva, N = 32: dt_lim = h^2 / (4 nu)")
N = 32
h = 2 * math.pi / N
dt_lim = h**2 / (4 * NU)
rng = np.random.default_rng(0)
resultados = {}
for factor in (0.9, 1.3):
    x = np.arange(N) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    u = -np.cos(X) * np.sin(Y) + 1e-6 * rng.standard_normal((N, N))
    v = np.sin(X) * np.cos(Y) + 1e-6 * rng.standard_normal((N, N))
    prep = preparar_proyeccion(N, h)
    u, v = proyectar(u, v, h, prep)
    dt = factor * dt_lim
    for _ in range(300):
        u, v = paso(u, v, dt, h, prep)
        if not np.isfinite(u).all() or np.max(np.abs(u)) > 1e6:
            break
    amp = float(np.max(np.abs(u)))
    resultados[factor] = amp
    print(f"    dt = {factor:.1f} dt_lim = {dt:.5f}  max|u| tras 300 pasos = {amp:.3e}")
assert resultados[0.9] < 1.5 and resultados[1.3] > 1e3
print("Pruebas superadas.")
