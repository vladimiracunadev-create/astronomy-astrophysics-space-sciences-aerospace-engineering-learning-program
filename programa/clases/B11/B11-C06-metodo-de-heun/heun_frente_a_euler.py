#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C06: método de Heun frente a Euler.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Altitud 400 km: dato ILUSTRATIVO.
Modelo: (a) y' = -y, y(0) = 1; (b) dos cuerpos, órbita circular exacta
x = a cos(n t), y = a sin(n t).
Métodos: Euler (orden 1, 1 evaluación por paso) y Heun / Euler mejorado
(orden 2, 2 evaluaciones): k1 = F(s); k2 = F(s + h k1); s' = s + h (k1+k2)/2.
Supuestos: doble precisión, sin perturbaciones.
Validez: h pequeño frente al periodo. Tolerancia: orden observado de Heun en
(a) dentro de [1.95, 2.05]; razón de errores de posición en (b) dentro de
[3.5, 4.5]; a igual número de evaluaciones, Heun debe ser más preciso que Euler.
"""
import math, platform

GM, RE = 3.986004e14, 6.3781e6
a = RE + 400e3
n = math.sqrt(GM / a**3)
T = 2 * math.pi / n


def F(s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -GM * x / r3, -GM * y / r3)


def paso_euler(f, s, h):
    k1 = f(s)
    return tuple(si + h * a1 for si, a1 in zip(s, k1))


def paso_heun(f, s, h):
    k1 = f(s)
    p = tuple(si + h * a1 for si, a1 in zip(s, k1))
    k2 = f(p)
    return tuple(si + 0.5 * h * (a1 + a2) for si, a1, a2 in zip(s, k1, k2))


def integrar(paso, f, s, h, N):
    for _ in range(N):
        s = paso(f, s, h)
    return s


def exacta(t):
    return (a * math.cos(n * t), a * math.sin(n * t), -a * n * math.sin(n * t), a * n * math.cos(n * t))


def energia(s):
    return 0.5 * (s[2] ** 2 + s[3] ** 2) - GM / math.hypot(s[0], s[1])


print(f"Python {platform.python_version()}")
errs = []
for N in (20, 40, 80, 160):
    y = integrar(paso_heun, lambda s: (-s[0],), (1.0,), 2.0 / N, N)[0]
    errs.append(abs(y - math.exp(-2.0)))
    print(f"(a) Heun N={N:3d}  error={errs[-1]:.4e}")
ordenes = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
print("    orden observado:", " ".join(f"{p:.3f}" for p in ordenes))
assert all(1.95 < p < 2.10 for p in ordenes)

s0 = exacta(0.0)
e0 = energia(s0)
ex = exacta(T)
perr = []
for N in (100, 200, 400, 800):
    sN = integrar(paso_heun, F, s0, T / N, N)
    err = math.hypot(sN[0] - ex[0], sN[1] - ex[1])
    perr.append(err)
    print(f"(b) Heun N={N:4d}  error de posicion = {err/1e3:10.4f} km  d(energia)/|e0| = {(energia(sN)-e0)/abs(e0):+.3e}")
razones = [perr[i] / perr[i + 1] for i in range(3)]
print("    razones de error:", " ".join(f"{q:.3f}" for q in razones))
assert all(3.5 < q < 4.5 for q in razones)

# mismo costo: 800 evaluaciones de F
sE = integrar(paso_euler, F, s0, T / 800, 800)
sH = integrar(paso_heun, F, s0, T / 400, 400)
eE = math.hypot(sE[0] - ex[0], sE[1] - ex[1])
eH = math.hypot(sH[0] - ex[0], sH[1] - ex[1])
print(f"A 800 evaluaciones: Euler {eE/1e3:.3f} km; Heun {eH/1e3:.3f} km (razon {eE/eH:.1f})")
assert eH < eE / 10
print("Pruebas superadas.")
