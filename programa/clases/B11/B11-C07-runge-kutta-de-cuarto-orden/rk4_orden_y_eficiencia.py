#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C07: Runge-Kutta de cuarto orden (RK4) y eficiencia.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Altitud 400 km: dato ILUSTRATIVO.
Modelo: (a) y' = -y; (b) y' = t^3 (solución polinómica de grado 4);
(c) dos cuerpos, órbita circular exacta.
Método: RK4 clásico con 4 evaluaciones por paso (DLMF 3.7(v), ec. 3.7.18-3.7.19:
error local O(h^5)):
k1 = F(s), k2 = F(s + h k1/2), k3 = F(s + h k2/2), k4 = F(s + h k3),
s' = s + h (k1 + 2 k2 + 2 k3 + k4)/6.
Supuestos: doble precisión; sin perturbaciones.
Tolerancia: orden observado en (a) en [3.9, 4.15]; en (b) RK4 reproduce la
solución exacta en un solo paso (error < 1e-12); en (c) razón de errores
en [15, 20]; a igual costo RK4 supera a Euler y Heun por varios órdenes.
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


def comb(s, h, k, c):
    return tuple(si + h * c * ki for si, ki in zip(s, k))


def paso_euler(f, t, s, h):
    return comb(s, h, f(t, s), 1.0)


def paso_heun(f, t, s, h):
    k1 = f(t, s); k2 = f(t + h, comb(s, h, k1, 1.0))
    return tuple(si + 0.5 * h * (p + q) for si, p, q in zip(s, k1, k2))


def paso_rk4(f, t, s, h):
    k1 = f(t, s)
    k2 = f(t + h / 2, comb(s, h, k1, 0.5))
    k3 = f(t + h / 2, comb(s, h, k2, 0.5))
    k4 = f(t + h, comb(s, h, k3, 1.0))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def integrar(paso, f, s, h, N):
    t = 0.0
    for _ in range(N):
        s = paso(f, t, s, h)
        t += h
    return s


def exacta(t):
    return (a * math.cos(n * t), a * math.sin(n * t), -a * n * math.sin(n * t), a * n * math.cos(n * t))


FO = lambda t, s: F(s)
print(f"Python {platform.python_version()}")

errs = []
for N in (20, 40, 80, 160):
    y = integrar(paso_rk4, lambda t, s: (-s[0],), (1.0,), 2.0 / N, N)[0]
    errs.append(abs(y - math.exp(-2.0)))
    print(f"(a) RK4 N={N:3d}  error={errs[-1]:.4e}")
ordenes = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
print("    orden observado:", " ".join(f"{p:.3f}" for p in ordenes))
assert all(3.9 < p < 4.15 for p in ordenes)

y4 = integrar(paso_rk4, lambda t, s: (t**3,), (0.0,), 2.0, 1)[0]
print(f"(b) y' = t^3, un solo paso h=2: {y4:.15f} (exacto 4)")
assert abs(y4 - 4.0) < 1e-12

s0 = exacta(0.0); ex = exacta(T)
perr = []
for N in (100, 200, 400, 800):
    sN = integrar(paso_rk4, FO, s0, T / N, N)
    perr.append(math.hypot(sN[0] - ex[0], sN[1] - ex[1]))
    print(f"(c) RK4 N={N:4d}  error de posicion = {perr[-1]:.4e} m")
razones = [perr[i] / perr[i + 1] for i in range(3)]
print("    razones de error:", " ".join(f"{q:.2f}" for q in razones))
assert all(15 < q < 20 for q in razones)

print("Costo igual: 800 evaluaciones de F")
res = {}
for nombre, paso, ev in (("Euler", paso_euler, 1), ("Heun", paso_heun, 2), ("RK4", paso_rk4, 4)):
    N = 800 // ev
    sN = integrar(paso, FO, s0, T / N, N)
    res[nombre] = math.hypot(sN[0] - ex[0], sN[1] - ex[1])
    print(f"   {nombre:5s} N={N:4d}  error = {res[nombre]:.4e} m")
assert res["RK4"] < res["Heun"] / 100 < res["Euler"] / 1e4
print("Pruebas superadas.")
