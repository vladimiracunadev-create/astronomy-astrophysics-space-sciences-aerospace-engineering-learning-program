#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C01: problema restringido de tres cuerpos (CR3BP) Tierra-Luna en el marco sinodico.

Datos consultados (2026-11-10): GM de la Luna = 4902.800 km3/s2 y radio medio 1737.4 km (JPL SSD, DE440);
semieje mayor de la Luna 384 400 km y periodo 27.322 d (JPL SSD, elementos medios, J2000).
GM de la Tierra ~ 398 600 km3/s2: DEDUCIDO de la masa publicada en la tabla de planetas del JPL con G (CODATA 2018); aproximado.
SINTETICO (propuesto para el ejemplo, no medido): estado inicial (x, y, vx, vy) = (0.85, 0, 0, -0.40) en unidades adimensionales.
Unidades adimensionales: longitud = 384 400 km (distancia entre primarios), tiempo = 1/n con n la velocidad angular media de la Luna.
Marco: sinodico baricentrico, ejes giratorios con los primarios en (-mu, 0) y (1-mu, 0). Modelo: masa de prueba sin masa, primarios en orbita circular.
Segunda via: integracion en el marco inercial con los primarios girando, y paso del resultado al marco giratorio.
Integrador: Runge-Kutta de orden 4 con paso fijo. Tolerancias: deriva de la constante de Jacobi < 1e-8; diferencia entre vias < 1e-6 (adimensional).
"""
from __future__ import annotations
import json, math, platform, sys

GM_LUNA = 4902.800
GM_TIERRA = 398600.0
A_LUNA_KM = 384400.0
P_LUNA_D = 27.322
MU = GM_LUNA / (GM_TIERRA + GM_LUNA)


def f_rot(s, mu=MU):
    x, y, vx, vy = s
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    ax = 2 * vy + x - (1 - mu) * (x + mu) / r1**3 - mu * (x - 1 + mu) / r2**3
    ay = -2 * vx + y - (1 - mu) * y / r1**3 - mu * y / r2**3
    return [vx, vy, ax, ay]


def f_in(s, t, mu=MU):
    X, Y, VX, VY = s
    c, sn = math.cos(t), math.sin(t)
    p1 = (-mu * c, -mu * sn)
    p2 = ((1 - mu) * c, (1 - mu) * sn)
    d1 = math.hypot(X - p1[0], Y - p1[1])
    d2 = math.hypot(X - p2[0], Y - p2[1])
    ax = -(1 - mu) * (X - p1[0]) / d1**3 - mu * (X - p2[0]) / d2**3
    ay = -(1 - mu) * (Y - p1[1]) / d1**3 - mu * (Y - p2[1]) / d2**3
    return [VX, VY, ax, ay]


def rk4(f, s, t, dt, n, usa_t):
    for _ in range(n):
        if usa_t:
            k1 = f(s, t)
            k2 = f([a + 0.5 * dt * b for a, b in zip(s, k1)], t + 0.5 * dt)
            k3 = f([a + 0.5 * dt * b for a, b in zip(s, k2)], t + 0.5 * dt)
            k4 = f([a + dt * b for a, b in zip(s, k3)], t + dt)
        else:
            k1 = f(s)
            k2 = f([a + 0.5 * dt * b for a, b in zip(s, k1)])
            k3 = f([a + 0.5 * dt * b for a, b in zip(s, k2)])
            k4 = f([a + dt * b for a, b in zip(s, k3)])
        s = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]
        t += dt
    return s


def jacobi(s, mu=MU):
    x, y, vx, vy = s
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    return x * x + y * y + 2 * (1 - mu) / r1 + 2 * mu / r2 - vx * vx - vy * vy


def rot_a_inercial(s, t):
    x, y, vx, vy = s
    c, sn = math.cos(t), math.sin(t)
    return [x * c - y * sn, x * sn + y * c, (vx - y) * c - (vy + x) * sn, (vx - y) * sn + (vy + x) * c]


def inercial_a_rot(s, t):
    X, Y, VX, VY = s
    c, sn = math.cos(t), math.sin(t)
    x, y = X * c + Y * sn, -X * sn + Y * c
    ux, uy = VX * c + VY * sn, -VX * sn + VY * c
    return [x, y, ux + y, uy - x]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"mu = GM_Luna/(GM_Tierra+GM_Luna) = {MU:.8f}  (GM_Tierra aproximado)")
    s0 = [0.85, 0.0, 0.0, -0.40]
    T = 20.0
    C0 = jacobi(s0)
    dt = 1e-3
    # deriva de Jacobi a lo largo de la trayectoria
    s, dC = list(s0), 0.0
    for _ in range(int(T / dt) // 100):
        s = rk4(f_rot, s, 0.0, dt, 100, False)
        dC = max(dC, abs(jacobi(s) - C0))
    sf = s
    print(f"Estado final (T = {T} adimensional = {T * P_LUNA_D / (2 * math.pi):.2f} d): x = {sf[0]:.6f} y = {sf[1]:.6f} vx = {sf[2]:.6f} vy = {sf[3]:.6f}")
    print(f"Constante de Jacobi inicial C = {C0:.6f} ; deriva maxima |C - C0| = {dC:.2e}")
    # segunda via: marco inercial
    si = rk4(f_in, rot_a_inercial(s0, 0.0), 0.0, dt, int(T / dt), True)
    sr = inercial_a_rot(si, T)
    dpos = max(abs(a - b) for a, b in zip(sf, sr))
    print(f"Diferencia maxima entre marco sinodico e inercial en T = {dpos:.2e}")
    # orden de convergencia
    r = {}
    for h in (4e-3, 2e-3, 1e-3):
        r[h] = rk4(f_rot, list(s0), 0.0, h, int(round(T / h)), False)
    e1 = max(abs(a - b) for a, b in zip(r[4e-3], r[2e-3]))
    e2 = max(abs(a - b) for a, b in zip(r[2e-3], r[1e-3]))
    p = math.log2(e1 / e2)
    print(f"Orden de convergencia estimado de RK4 = {p:.2f}")
    # puntos de referencia: posicion de la Luna en km
    print(f"Distancia a la Luna al final = {math.hypot(sf[0] - (1 - MU), sf[1]) * A_LUNA_KM:.0f} km (unidad = {A_LUNA_KM:.0f} km)")
    assert dC < 1e-8 and dpos < 1e-6 and 3.5 < p < 4.5
    print("Pruebas superadas.")
    return {"python": platform.python_version(), "mu": MU, "C0": C0, "dC": dC, "dpos": dpos, "p": p, "x": sf[0], "y": sf[1],
            "dias": T * P_LUNA_D / (2 * math.pi), "dluna": math.hypot(sf[0] - (1 - MU), sf[1]) * A_LUNA_KM}


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
