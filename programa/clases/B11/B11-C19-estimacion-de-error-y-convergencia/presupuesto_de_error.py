#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C19: estimación de error, convergencia y presupuesto de error.

Datos: (a) f = sin x en x = 1 (derivada exacta cos 1); (b)-(d) órbita circular a 400 km
de altitud (ILUSTRATIVA) con GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial
6.3781e6 m (valores nominales IAU 2015, Res. B3). La incertidumbre relativa de GM
de 1e-8 es un valor SINTÉTICO de ejemplo para el presupuesto.
Modelo: (a) diferencias hacia adelante y centrales con paso h: error de truncamiento
O(h) u O(h^2) más error de redondeo ~ eps/h; (b) RK4 de paso fijo con solución exacta
circular; (c) autoconvergencia sin conocer la solución exacta; (d) efecto sobre la
posición de una incertidumbre en GM.
Supuestos: doble precisión (eps = 2.22e-16). Validez: órbita de dos cuerpos.
Tolerancia: el paso óptimo de la diferencia hacia adelante debe estar a un factor 10
de sqrt(eps) y el de la central a un factor 10 de eps^(1/3); el error estimado por
Richardson debe estar a un factor 2 del error verdadero; el orden por
autoconvergencia, en [3.5, 4.5]; el efecto de la incertidumbre de GM (con el estado inicial
medido fijo) debe coincidir con 4*pi*a*delta a 5 %.
"""
import math, platform, sys

eps = sys.float_info.epsilon
print(f"Python {platform.python_version()}; eps = {eps:.3e}")

# (a) curva en V
ex = math.cos(1.0)
best_f = min(((abs((math.sin(1 + h) - math.sin(1)) / h - ex), h) for h in [10 ** (-k / 4) for k in range(4, 65)]))
best_c = min(((abs((math.sin(1 + h) - math.sin(1 - h)) / (2 * h) - ex), h) for h in [10 ** (-k / 4) for k in range(4, 65)]))
print("(a) derivada de sin x en x = 1: error frente a h")
for h in (1e-1, 1e-3, 1e-5, 1e-8, 1e-11, 1e-14):
    ef = abs((math.sin(1 + h) - math.sin(1)) / h - ex)
    ec = abs((math.sin(1 + h) - math.sin(1 - h)) / (2 * h) - ex)
    print(f"    h = {h:.0e}: hacia adelante {ef:.3e} | central {ec:.3e}")
print(f"    mínimo hacia adelante: {best_f[0]:.2e} en h = {best_f[1]:.1e} (teoría sqrt(eps) = {math.sqrt(eps):.1e})")
print(f"    mínimo central       : {best_c[0]:.2e} en h = {best_c[1]:.1e} (teoría eps^(1/3) = {eps ** (1/3):.1e})")
assert 0.1 < best_f[1] / math.sqrt(eps) < 10 and 0.1 < best_c[1] / eps ** (1 / 3) < 10

# órbita
GM, RE = 3.986004e14, 6.3781e6
a = RE + 400e3
n0 = math.sqrt(GM / a**3)
T = 2 * math.pi / n0


def F(s, gm=GM):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -gm * x / r3, -gm * y / r3)


def rk4(s, h, gm=GM):
    c = lambda k, q: tuple(si + h * q * ki for si, ki in zip(s, k))
    k1 = F(s, gm); k2 = F(c(k1, .5), gm); k3 = F(c(k2, .5), gm); k4 = F(c(k3, 1.), gm)
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def vuelta(N, gm=GM):
    s = (a, 0.0, 0.0, a * n0)
    h = T / N
    for _ in range(N):
        s = rk4(s, h, gm)
    return s


dist = lambda p, q: math.hypot(p[0] - q[0], p[1] - q[1])
s_ex = (a, 0.0)
print("(b) Richardson (RK4, p = 4): error estimado frente a verdadero tras 1 vuelta")
sN = {N: vuelta(N) for N in (50, 100, 200, 400)}
for N in (50, 100, 200):
    est = dist(sN[N], sN[2 * N]) / (2**4 - 1)            # error estimado de la solución con 2N
    ver = dist(sN[2 * N], s_ex)
    print(f"    N={N:3d}->{2*N:3d}: estimado = {est:.4e} m ; verdadero = {ver:.4e} m ; razón = {est/ver:.2f}")
    if N >= 100:
        assert 0.5 < est / ver < 2.0

# (c) autoconvergencia
d1, d2 = dist(sN[100], sN[200]), dist(sN[200], sN[400])
p_obs = math.log2(d1 / d2)
print(f"(c) autoconvergencia sin solución exacta: orden observado = {p_obs:.3f} (diferencias {d1:.3e} y {d2:.3e} m)")
assert 3.5 < p_obs < 4.5

# (d) presupuesto de error
delta = 1e-8
s_pert = vuelta(200, GM * (1 + delta))
s_nom = vuelta(200)
efecto = dist(s_pert, s_nom)
teor = 4 * math.pi * a * delta     # estado inicial fijo: a' = a(1-delta), T' = T(1-2 delta)
trunc = dist(s_nom, s_ex)
print("(d) presupuesto de error de una vuelta (N=200):")
print(f"    truncamiento del integrador       = {trunc:.3e} m")
print(f"    incertidumbre de GM (1e-8 relativo) = {efecto:.3e} m (estimación 4*pi*a*delta = {teor:.3e} m)")
print(f"    redondeo (eps * a * pasos)         ~ {eps * a * 200:.1e} m")
assert abs(efecto - teor) / teor < 0.05
print("Pruebas superadas.")
