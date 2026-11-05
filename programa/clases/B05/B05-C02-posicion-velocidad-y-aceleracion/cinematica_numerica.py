#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C02: velocidad y aceleración a partir de posiciones.

Datos: SINTÉTICOS, generados con la órbita circular del satélite ideal
(r = 6 378 137 m + 400 000 m; GM = 3,9860e14 m³/s², NASA NSSDC Earth Fact Sheet).
Modelo: posición en el plano x-y, marco inercial centrado en la Tierra, ejes fijos.
Supuestos: órbita circular uniforme, sin perturbaciones. Dominio de validez: pasos
de tiempo pequeños frente al período. Tolerancia: error relativo < 1e-5 en
velocidad y < 1e-3 en aceleración con paso de 1 s.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
R = 6_378_137.0 + 400_000.0
W = math.sqrt(GM / R**3)            # velocidad angular [rad/s]

def pos(t: float) -> tuple[float, float]:
    return R * math.cos(W * t), R * math.sin(W * t)

def vel_num(t: float, dt: float) -> tuple[float, float]:
    (x1, y1), (x0, y0) = pos(t + dt), pos(t - dt)
    return (x1 - x0) / (2 * dt), (y1 - y0) / (2 * dt)

def acc_num(t: float, dt: float) -> tuple[float, float]:
    (x1, y1), (x, y), (x0, y0) = pos(t + dt), pos(t), pos(t - dt)
    return (x1 - 2 * x + x0) / dt**2, (y1 - 2 * y + y0) / dt**2

def main() -> int:
    t, dt = 1234.5, 1.0
    vx, vy = vel_num(t, dt)
    ax, ay = acc_num(t, dt)
    v, a = math.hypot(vx, vy), math.hypot(ax, ay)
    v_ana, a_ana = W * R, W**2 * R
    assert abs(v - v_ana) / v_ana < 1e-5, (v, v_ana)
    assert abs(a - a_ana) / a_ana < 1e-3, (a, a_ana)
    # perpendicularidad v·r = 0 y a antiparalela a r
    x, y = pos(t)
    assert abs(vx * x + vy * y) / (v * R) < 1e-5
    assert abs((ax * x + ay * y) / (a * R) + 1.0) < 1e-3
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"w = {W:.6e} rad/s; T = {2*math.pi/W:.1f} s")
    print(f"v numerica = {v:.3f} m/s; analitica W*R = {v_ana:.3f} m/s")
    print(f"a numerica = {a:.4f} m/s^2; analitica W^2*R = {a_ana:.4f} m/s^2")
    for dt in (0.01, 1.0, 100.0, 1000.0):
        ax, ay = acc_num(t, dt)
        print(f"  dt = {dt:8.2f} s -> |a| = {math.hypot(ax, ay):.6f} m/s^2 (error rel. {abs(math.hypot(ax, ay)-a_ana)/a_ana:.2e})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
