#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C11: métodos simplécticos (Störmer-Verlet / leapfrog) frente a RK4.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Órbita circular a 400 km de altitud
(ILUSTRATIVA) y órbita elíptica ILUSTRATIVA a = 26 560 km, e = 0.30.
Modelo: dos cuerpos; hamiltoniano H = v^2/2 - GM/r (por unidad de masa).
Métodos: leapfrog kick-drift-kick (1 evaluación de fuerza por paso, orden 2,
simpléctico y reversible) y Euler simpléctico (orden 1); RK4 (4 evaluaciones).
Medida: error relativo de la energía; reversibilidad (avanzar N pasos,
invertir la velocidad, avanzar N pasos); error de posición.
Supuestos: sin perturbaciones; doble precisión. Validez: n h << 1.
Tolerancia/pruebas: (1) leapfrog es reversible a 1e-4 m (ruido de redondeo) tras 1000 pasos; RK4 no lo es;
(2) el error de energía del leapfrog queda acotado (el máximo sobre todos los
pasos de 1000 vueltas es < 1.5 veces el máximo de las primeras 10 vueltas); (3) a igual costo y también con 4 veces el costo, el error máximo de RK4 en
1000 vueltas supera al del leapfrog, y la deriva de RK4 es sistemática.
"""
import math, platform

GM, RE = 3.986004e14, 6.3781e6


def acc(x, y):
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3


def leapfrog(s, h):
    x, y, vx, vy = s
    ax, ay = acc(x, y)
    vx += 0.5 * h * ax; vy += 0.5 * h * ay            # impulso medio
    x += h * vx; y += h * vy                          # deriva
    ax, ay = acc(x, y)
    vx += 0.5 * h * ax; vy += 0.5 * h * ay            # impulso medio
    return (x, y, vx, vy)


def euler_simplectico(s, h):
    x, y, vx, vy = s
    ax, ay = acc(x, y)
    vx += h * ax; vy += h * ay
    return (x + h * vx, y + h * vy, vx, vy)


def F(s):
    x, y, vx, vy = s
    ax, ay = acc(x, y)
    return (vx, vy, ax, ay)


def rk4(s, h):
    c = lambda k, q: tuple(si + h * q * ki for si, ki in zip(s, k))
    k1 = F(s); k2 = F(c(k1, .5)); k3 = F(c(k2, .5)); k4 = F(c(k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def eps(s):
    return 0.5 * (s[2] ** 2 + s[3] ** 2) - GM / math.hypot(s[0], s[1])


def corrida(paso, s, h, N, vueltas, marcas):
    e0 = eps(s)
    maxe, out = 0.0, {}
    for v in range(1, vueltas + 1):
        for _ in range(N):
            s = paso(s, h)
            maxe = max(maxe, abs((eps(s) - e0) / abs(e0)))      # máximo sobre TODOS los pasos
        if v in marcas:
            out[v] = ((eps(s) - e0) / abs(e0), maxe)
    return s, out


print(f"Python {platform.python_version()}")
a = RE + 400e3
T = 2 * math.pi * math.sqrt(a**3 / GM)
s0 = (a, 0.0, 0.0, math.sqrt(GM / a))
print(f"a = {a/1e3:.1f} km; T = {T:.1f} s")

# (1) reversibilidad
h = T / 100
s = s0
for _ in range(1000):
    s = leapfrog(s, h)
s = (s[0], s[1], -s[2], -s[3])
for _ in range(1000):
    s = leapfrog(s, h)
err_rev = math.hypot(s[0] - s0[0], s[1] - s0[1])
s = s0
for _ in range(1000):
    s = rk4(s, h)
s = (s[0], s[1], -s[2], -s[3])
for _ in range(1000):
    s = rk4(s, h)
err_rev_rk4 = math.hypot(s[0] - s0[0], s[1] - s0[1])
print(f"reversibilidad tras 1000 pasos: leapfrog {err_rev:.3e} m ; RK4 {err_rev_rk4:.3e} m")
assert err_rev < 1e-4 and err_rev_rk4 > 1e3 * err_rev

# (2) y (3): energía en 1000 vueltas, circular, a igual costo (100 evaluaciones de fuerza por vuelta)
print("\nÓrbita circular, 1000 vueltas, 100 evaluaciones de la fuerza por vuelta:")
_, lf = corrida(leapfrog, s0, T / 100, 100, 1000, {10, 100, 1000})
_, es = corrida(euler_simplectico, s0, T / 100, 100, 1000, {10, 100, 1000})
_, rk = corrida(rk4, s0, T / 25, 25, 1000, {10, 100, 1000})
_, rk4x = corrida(rk4, s0, T / 100, 100, 1000, {10, 100, 1000})
for nombre, d in (("leapfrog (h=T/100)", lf), ("Euler simpléctico (h=T/100)", es), ("RK4 (h=T/25), mismo costo", rk), ("RK4 (h=T/100), 4x el costo", rk4x)):
    for v in (10, 100, 1000):
        print(f"  {nombre:28s} vuelta {v:4d}: d(eps)/|eps0| = {d[v][0]:+.3e}   máximo hasta ahí = {d[v][1]:.3e}")
assert lf[1000][1] < 1.5 * lf[10][1]
assert rk[1000][1] > 100 * lf[1000][1]
assert abs(rk4x[1000][0]) > abs(rk4x[100][0]) > abs(rk4x[10][0])       # RK4 deriva de forma sistemática
assert rk4x[1000][1] > lf[1000][1]

# error de posición (error de FASE) del leapfrog: crece linealmente con las vueltas
print("\nError de posición del leapfrog frente a la solución exacta (circular, h = T/100):")
perr = {}
for L in (1, 10, 100, 1000):
    sl, _ = corrida(leapfrog, s0, T / 100, 100, L, {L})
    perr[L] = math.hypot(sl[0] - a, sl[1]) / 1e3
    print(f"  tras {L:4d} vueltas: {perr[L]:10.3f} km")
assert abs(perr[10] / perr[1] - 10) < 0.5
sr, _ = corrida(rk4, s0, T / 25, 25, 1000, {1000})
print(f"  RK4 (h = T/25) tras 1000 vueltas: {math.hypot(sr[0]-a, sr[1])/1e3:.3e} km (órbita destruida)")

# órbita elíptica
aE, eE = 26_560e3, 0.30
sE = (aE * (1 - eE), 0.0, 0.0, math.sqrt(GM * (1 + eE) / (aE * (1 - eE))))
TE = 2 * math.pi * math.sqrt(aE**3 / GM)
_, lfe = corrida(leapfrog, sE, TE / 400, 400, 100, {10, 100})
_, rke = corrida(rk4, sE, TE / 100, 100, 100, {10, 100})
print("\nÓrbita elíptica ilustrativa (e = 0.30), 100 vueltas, 400 evaluaciones de fuerza por vuelta:")
print(f"  leapfrog: máximo |d eps|/|eps0| = {lfe[100][1]:.3e}, tras 100 vueltas {lfe[100][0]:+.3e}")
print(f"  RK4     : máximo |d eps|/|eps0| = {rke[100][1]:.3e}, tras 100 vueltas {rke[100][0]:+.3e}")
print("Pruebas superadas.")
