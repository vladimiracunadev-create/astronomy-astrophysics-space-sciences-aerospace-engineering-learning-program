#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C10: deriva de la energía y del momento angular en integraciones largas.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Órbita circular a 400 km de altitud
(ILUSTRATIVA) y órbita elíptica ILUSTRATIVA a = 26 560 km, e = 0.30.
Modelo: dos cuerpos. Cantidades conservadas: energía específica
eps = v^2/2 - GM/r y momento angular específico h = x vy - y vx.
Métodos: Euler (orden 1), Heun (2), RK4 (4), paso fijo.
Medida: error relativo (q - q0)/|q0| tras 1, 10 y 100 vueltas.
Supuestos: sin perturbaciones. Validez: pasos con n h << 1.
Tolerancia/pruebas: (1) la energía exacta de la solución analítica se conserva
a 1e-12; (2) la deriva de energía de RK4 tras 100 vueltas baja con h^5 (razón entre
N=100 y N=200 en [25, 40]; la amortiguación por paso del oscilador lineal es
O(h^6) y hay N ~ 1/h pasos por vuelta); (3) Euler duplica o más el radio en pocas vueltas; (4) la deriva de
RK4 es sistemática (energía decreciente y momento angular casi constante).
"""
import math, platform

GM, RE = 3.986004e14, 6.3781e6


def F(t, s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -GM * x / r3, -GM * y / r3)


def c(s, h, k, q):
    return tuple(si + h * q * ki for si, ki in zip(s, k))


def euler(s, h):
    return c(s, h, F(0, s), 1.0)


def heun(s, h):
    k1 = F(0, s); k2 = F(0, c(s, h, k1, 1.0))
    return tuple(si + 0.5 * h * (p + q) for si, p, q in zip(s, k1, k2))


def rk4(s, h):
    k1 = F(0, s); k2 = F(0, c(s, h, k1, .5)); k3 = F(0, c(s, h, k2, .5)); k4 = F(0, c(s, h, k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def eps(s):
    return 0.5 * (s[2] ** 2 + s[3] ** 2) - GM / math.hypot(s[0], s[1])


def hmom(s):
    return s[0] * s[3] - s[1] * s[2]


def inicial(a, e):
    return (a * (1 - e), 0.0, 0.0, math.sqrt(GM * (1 + e) / (a * (1 - e))))


def propagar(paso, s, a, N, vueltas, marcas):
    T = 2 * math.pi * math.sqrt(a**3 / GM)
    h = T / N
    e0, h0 = eps(s), hmom(s)
    out = {}
    for v in range(1, vueltas + 1):
        for _ in range(N):
            s = paso(s, h)
        if v in marcas:
            out[v] = ((eps(s) - e0) / abs(e0), (hmom(s) - h0) / abs(h0), math.hypot(s[0], s[1]))
    return s, out


print(f"Python {platform.python_version()}")
aL = RE + 400e3
sL = inicial(aL, 0.0)
# prueba 1: la energía de la solución analítica es constante
n = math.sqrt(GM / aL**3)
ex = lambda t: (aL * math.cos(n * t), aL * math.sin(n * t), -aL * n * math.sin(n * t), aL * n * math.cos(n * t))
assert all(abs(eps(ex(t)) - eps(ex(0))) / abs(eps(ex(0))) < 1e-12 for t in (0, 777.7, 2500.1, 5000.0))
print(f"eps0 = {eps(sL):.6e} J/kg ; h0 = {hmom(sL):.6e} m2/s ; T = {2*math.pi/n:.1f} s")

print("\nÓrbita circular de 400 km, N = 200 pasos por vuelta, error relativo de la energía:")
resultados = {}
for nombre, paso, vueltas in (("Euler", euler, 5), ("Heun", heun, 100), ("RK4", rk4, 100)):
    _, out = propagar(paso, sL, aL, 200, vueltas, {1, min(10, vueltas), vueltas})
    resultados[nombre] = out
    for v, (de, dh, r) in sorted(out.items()):
        print(f"  {nombre:5s} vuelta {v:3d}: d(eps)/|eps0| = {de:+.3e}   d(h)/h0 = {dh:+.3e}   r/a = {r/aL:.6f}")

assert resultados["Euler"][5][2] > 2 * aL * 0.99 or resultados["Euler"][5][2] > 1.5 * aL
print("\nRK4, deriva tras 100 vueltas según el paso (N pasos por vuelta):")
deriva = {}
for N in (100, 200):
    _, out = propagar(rk4, sL, aL, N, 100, {100})
    deriva[N] = out[100][0]
    print(f"  N={N}: d(eps)/|eps0| = {out[100][0]:+.4e}   d(h)/h0 = {out[100][1]:+.3e}")
razon = deriva[100] / deriva[200]
print(f"  razón de derivas N=100/N=200 = {razon:.2f} (se espera 32 si la deriva por vuelta escala como h^5)")
assert 25 < razon < 40
assert deriva[200] < 0                                   # RK4 disipa energía en esta órbita
assert abs(resultados["RK4"][100][1]) < abs(resultados["RK4"][100][0])   # el momento angular deriva menos que la energía

# órbita elíptica
aE, eE = 26_560e3, 0.30
sE = inicial(aE, eE)
print("\nÓrbita elíptica ilustrativa (a = 26 560 km, e = 0.30), RK4, N = 400:")
_, outE = propagar(rk4, sE, aE, 400, 100, {1, 10, 100})
for v, (de, dh, r) in sorted(outE.items()):
    print(f"  vuelta {v:3d}: d(eps)/|eps0| = {de:+.3e}   d(h)/h0 = {dh:+.3e}")
assert abs(outE[100][0]) < 1e-3
print("Pruebas superadas.")
