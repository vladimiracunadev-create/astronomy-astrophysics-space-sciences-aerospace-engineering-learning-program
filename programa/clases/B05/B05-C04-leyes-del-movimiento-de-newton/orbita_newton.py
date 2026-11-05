#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C04: segunda ley de Newton integrada paso a paso.

Datos: GM = 3,9860e14 m³/s² y R = 6 378 137 m (NASA NSSDC Earth Fact Sheet);
altura 400 km (SINTÉTICA, satélite ideal). Modelo: F = m a con solo la gravedad
puntual de la Tierra, marco inercial geocéntrico, 2D. Integradores: Euler
explícito y velocity-Verlet. Supuestos: masa puntual, sin atmósfera, sin
achatamiento. Dominio de validez: una a pocas órbitas. Tolerancia: tras una
órbita, Verlet vuelve al punto de partida a menos de 1e-3 de r con 600 pasos.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
R0 = 6_378_137.0 + 400_000.0

def acc(x: float, y: float) -> tuple[float, float]:
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3

def correr(metodo: str, n: int) -> tuple[float, float, float]:
    v0 = math.sqrt(GM / R0)
    T = 2 * math.pi * math.sqrt(R0**3 / GM)
    dt = T / n
    x, y, vx, vy = R0, 0.0, 0.0, v0
    ax, ay = acc(x, y)
    for _ in range(n):
        if metodo == "euler":
            x, y = x + vx * dt, y + vy * dt
            vx, vy = vx + ax * dt, vy + ay * dt
            ax, ay = acc(x, y)
        else:  # velocity-Verlet
            vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
            x += vx * dt; y += vy * dt
            ax, ay = acc(x, y)
            vx += 0.5 * ax * dt; vy += 0.5 * ay * dt
    err = math.hypot(x - R0, y) / R0
    return err, math.hypot(x, y), math.hypot(vx, vy)

def main() -> int:
    err_v, r_v, v_v = correr("verlet", 600)
    assert err_v < 1e-3, err_v
    # F = m a: con m = 1000 kg la fuerza gravitatoria en t=0 vale m*GM/r²
    m = 1000.0
    F = m * GM / R0**2
    assert abs(F - m * math.hypot(*acc(R0, 0.0))) < 1e-6
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Fuerza gravitatoria sobre 1000 kg a 400 km: {F:.1f} N (peso en superficie con g_n: {m*9.80665:.1f} N)")
    for met, n in (("euler", 600), ("euler", 6000), ("verlet", 600)):
        err, r, v = correr(met, n)
        print(f"{met:7s} n={n:5d}: error de cierre = {err:.2e} (rel. a r); r_final = {r:.0f} m; v_final = {v:.2f} m/s")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
