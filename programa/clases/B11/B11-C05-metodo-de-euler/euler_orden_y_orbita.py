#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C05: método de Euler, orden de convergencia y órbita circular.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Altitud 400 km: dato ILUSTRATIVO.
Modelo: (a) y' = -y, y(0) = 1, solución exacta exp(-t); (b) dos cuerpos
s' = F(s) con s = (x, y, vx, vy) y órbita circular exacta
x = a cos(n t), y = a sin(n t).
Método: Euler explícito s_{k+1} = s_k + h F(s_k), orden global 1.
Supuestos: aritmética de doble precisión; sin perturbaciones.
Validez: h pequeño frente al periodo. Tolerancia: orden observado en (a)
dentro de [0.95, 1.05]; razón de errores de posición al dividir h entre 2
dentro de [1.7, 2.3] (orden 1) en (b). Las pruebas detienen la ejecución.
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


def euler(f, s, h, nsteps):
    for _ in range(nsteps):
        d = f(s)
        s = tuple(si + h * di for si, di in zip(s, d))
    return s


def exacta(t):
    return (a * math.cos(n * t), a * math.sin(n * t), -a * n * math.sin(n * t), a * n * math.cos(n * t))


def energia(s):
    x, y, vx, vy = s
    return 0.5 * (vx * vx + vy * vy) - GM / math.hypot(x, y)


print(f"Python {platform.python_version()}")
# (a) orden en y' = -y hasta t = 2
errs = []
for N in (20, 40, 80, 160):
    y = euler(lambda s: (-s[0],), (1.0,), 2.0 / N, N)[0]
    errs.append(abs(y - math.exp(-2.0)))
    print(f"(a) N={N:4d}  h={2.0/N:.5f}  error={errs[-1]:.4e}")
ordenes = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
print("    orden observado:", " ".join(f"{p:.3f}" for p in ordenes))
assert all(0.95 < p < 1.05 for p in ordenes)

# (b) una vuelta de órbita circular
s0 = exacta(0.0)
e0 = energia(s0)
perr = []
for N in (200, 400, 800, 1600):
    sN = euler(F, s0, T / N, N)
    ex = exacta(T)
    err = math.hypot(sN[0] - ex[0], sN[1] - ex[1])
    perr.append(err)
    print(f"(b) N={N:5d}  h={T/N:8.3f} s  error de posicion = {err/1e3:10.3f} km  "
          f"r/a = {math.hypot(sN[0], sN[1])/a:.5f}  d(energia)/|e0| = {(energia(sN)-e0)/abs(e0):+.3e}")
razones = [perr[i] / perr[i + 1] for i in range(3)]
print("    razones de error:", " ".join(f"{q:.3f}" for q in razones))
assert all(1.7 < q < 2.3 for q in razones)
assert energia(euler(F, s0, T / 400, 400)) > e0          # Euler hace crecer la energía en esta órbita
print("Pruebas superadas.")
