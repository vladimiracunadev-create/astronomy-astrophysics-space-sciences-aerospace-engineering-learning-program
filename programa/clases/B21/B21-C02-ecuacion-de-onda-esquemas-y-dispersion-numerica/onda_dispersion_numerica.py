#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B21-C02: ecuación de onda 1D, esquema salto de rana y dispersión numérica.

Datos: SINTETICOS (pulso gaussiano y modos senoidales). Para dar escala física
se usa un bucle ILUSTRATIVO de longitud L = 100 Mm con velocidad de onda
c = 1000 km/s (no es una medición de ningún bucle real).
Modelo: u_tt = c^2 u_xx en un dominio periódico de longitud L.
Método: u^{n+1}_i = 2 u^n_i - u^{n-1}_i + nu^2 (u^n_{i+1} - 2 u^n_i + u^n_{i-1}),
nu = c dt / dx (número de Courant); primer paso u^1 = u^0 + nu^2/2 * delta2(u^0).
Relación de dispersión discreta (derivada en la clase): sin(w dt/2) = nu sin(k dx/2).
Supuestos: coeficiente c constante; periodico; doble precisión.
Validez: nu <= 1 (condición CFL de estabilidad).
Tolerancias (las pruebas detienen la ejecución si fallan): el modo senoidal
simulado coincide con la solución discreta exacta cos(w_num t) a 1e-11;
la frecuencia medida coincide con la relación de dispersión a 1e-10 (relativo);
con nu = 1 el pulso se propaga sin error a 1e-12; el factor de amplificación
del modo de Nyquist con nu = 1.05 coincide con la predicción a 1e-6 (relativo).
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()}  NumPy {np.__version__}")

L_MM, C_KMS = 100.0, 1000.0  # ILUSTRATIVO
L_UNIDAD = 1.0  # trabajamos en x/L; c = 1 -> tiempo en unidades de L/c
T_CRUCE = L_MM * 1e3 / C_KMS  # s, tiempo de cruce de L
print(f"Escala ilustrativa: L/c = {T_CRUCE:.0f} s")


def omega_num(k, dx, dt, c=1.0):
    nu = c * dt / dx
    return 2.0 / dt * math.asin(nu * math.sin(k * dx / 2.0))


def paso(u_prev, u, nu):
    return 2 * u - u_prev + nu**2 * (np.roll(u, -1) - 2 * u + np.roll(u, 1))


def evolucion_modo(N, m, nu, nsteps):
    dx = 1.0 / N
    dt = nu * dx
    x = np.arange(N) * dx
    k = 2 * math.pi * m
    u0 = np.sin(k * x)
    u1 = u0 + 0.5 * nu**2 * (np.roll(u0, -1) - 2 * u0 + np.roll(u0, 1))
    a = [1.0, 2.0 / N * float(np.sum(u1 * np.sin(k * x)))]
    up, uc = u0, u1
    for _ in range(nsteps - 1):
        un = paso(up, uc, nu)
        up, uc = uc, un
        a.append(2.0 / N * float(np.sum(uc * np.sin(k * x))))
    return np.array(a), dx, dt, k


# (a) modos: frecuencia numérica frente a relación de dispersión y a la exacta
print("(a) modo sin(k x), nu = 0.5, N = 200; w_num / w = c_fase_num / c")
N, nu = 200, 0.5
for m in (1, 5, 10, 20, 40):
    nsteps = int(0.2 * N / nu / m) + 1  # menos de un cuarto de periodo
    a, dx, dt, k = evolucion_modo(N, m, nu, nsteps)
    w_teo = omega_num(k, dx, dt)
    t = dt * np.arange(a.size)
    assert np.max(np.abs(a - np.cos(w_teo * t))) < 1e-11, "modo discreto"
    w_med = math.acos(a[-1]) / t[-1]
    assert abs(w_med - w_teo) / w_teo < 1e-10, "dispersión"
    razon = w_teo / k  # c = 1
    print(f"    m={m:2d}  puntos por longitud de onda = {N // m:3d}  "
          f"w_num/w = {razon:.6f}  error de fase relativo = {razon - 1:+.3e}")

# (b) pulso: nu = 1 exacto; nu = 0.5 dispersivo
print("(b) pulso gaussiano (ancho 0.05 L), N = 400, hasta t = 0.25 L/c")
N = 400
x = np.arange(N) / N
u0 = np.exp(-(((x - 0.5) / 0.05) ** 2))


def u_exacta(t):
    g = lambda y: np.exp(-((((y % 1.0) - 0.5) / 0.05) ** 2))
    return 0.5 * (g(x - t) + g(x + t))


for nu in (1.0, 0.5):
    dx = 1.0 / N
    dt = nu * dx
    nsteps = int(round(0.25 / dt))
    up = u0
    uc = u0 + 0.5 * nu**2 * (np.roll(u0, -1) - 2 * u0 + np.roll(u0, 1))
    for _ in range(nsteps - 1):
        up, uc = uc, paso(up, uc, nu)
    err = float(np.max(np.abs(uc - u_exacta(nsteps * dt))))
    print(f"    nu = {nu:.1f}  error max = {err:.3e}")
    if nu == 1.0:
        assert err < 1e-12, "nu=1 debe ser exacto"
    else:
        assert 1e-4 < err < 1e-1

# (c) estabilidad: modo de Nyquist
print("(c) modo de Nyquist (damero): factor de amplificación por paso")
for nu in (0.9, 1.0, 1.05):
    N = 64
    dx = 1.0 / N
    s = (-1.0) ** np.arange(N)
    up = s.copy()
    uc = s.copy()  # semilla arbitraria
    uc = up + 0.5 * nu**2 * (np.roll(up, -1) - 2 * up + np.roll(up, 1))
    amps = []
    for _ in range(60):
        un = paso(up, uc, nu)
        up, uc = uc, un
        amps.append(float(np.max(np.abs(uc))))
    # raíces de lambda^2 - (2 - 4 nu^2) lambda + 1 = 0
    b = 2 - 4 * nu**2
    disc = b * b - 4
    lam = max(abs((b + math.sqrt(disc)) / 2), abs((b - math.sqrt(disc)) / 2)) if disc > 0 else 1.0
    crec = (amps[-1] / amps[-2])
    if nu > 1:
        print(f"    nu = {nu:.2f}  |lambda| teorico = {lam:.6f}  razón medida = {crec:.6f}")
    else:
        print(f"    nu = {nu:.2f}  |lambda| teorico = {lam:.6f}  amplitud máxima en 60 pasos = {max(amps):.3f}")
    if nu > 1:
        assert abs(crec - lam) / lam < 1e-6
    else:
        assert amps[-1] < 1.0 + 1e-9

# (d) lectura física con la escala ilustrativa
print("(d) desfase de un modo tras cruzar el bucle 10 veces (nu = 0.5)")
for ppw in (10, 20, 40):
    N = 4 * ppw  # m = 4 modos -> ppw puntos por longitud de onda (ilustrativo)
    dx = 1.0 / N
    dt = 0.5 * dx
    k = 2 * math.pi * 4
    razon = omega_num(k, dx, dt) / k
    desfase_longitudes = 10 * (1 - razon) / (1.0 / 4)  # en longitudes de onda
    print(f"    {ppw:2d} puntos/long. de onda: c_num/c = {razon:.6f}  "
          f"retraso tras 10 cruces = {desfase_longitudes:.3f} longitudes de onda")
print("Pruebas superadas.")
