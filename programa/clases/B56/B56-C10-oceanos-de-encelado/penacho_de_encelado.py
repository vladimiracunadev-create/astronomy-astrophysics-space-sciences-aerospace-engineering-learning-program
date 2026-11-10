#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C10: balistica de las particulas del penacho de Encelado.

Datos consultados el 2026-11-09: NASA/NSSDC, hoja de satelites saturninos (actualizada
2025-07-22): masa 1,08e20 kg, dimensiones triaxiales 257 x 251 x 248 km (se interpretan como
semiejes; la comprobacion con la densidad de la hoja, 1610 kg/m3, lo respalda), densidad media
1610 kg/m3; pagina de Encelado de la NASA: el penacho sale a unos 400 m/s (cerca de 800 mph),
la mayor parte del material vuelve como nieve, espesor medio del hielo de 20 a 25 km y de 1 a 5 km
en el polo sur. G de NIST (CODATA 2022).
Modelo: un grano lanzado radialmente desde la superficie con rapidez v. Energia:
r_max = 1 / (1/r0 - v^2/(2 G M)) si v < v_esc. Verificacion independiente: integracion RK4 de
r'' = -G M / r^2 hasta el apogeo.
Supuestos: cuerpo esferico de radio medio geometrico, sin rotacion, sin arrastre del gas, sin
Saturno. Validez: ilustra el orden de magnitud. Tolerancia: apogeo RK4 frente a energia, 1e-6.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
M = 1.08e20
A, B, C = 257e3, 251e3, 248e3
R = (A * B * C) ** (1 / 3)


def apogeo_energia(v):
    d = 1 / R - v * v / (2 * G * M)
    return float("inf") if d <= 0 else 1 / d


def apogeo_rk4(v, dt=0.5):
    r, u = R, v
    acc = lambda x: -G * M / (x * x)
    while u > 0:
        k1r, k1u = u, acc(r)
        k2r, k2u = u + dt * k1u / 2, acc(r + dt * k1r / 2)
        k3r, k3u = u + dt * k2u / 2, acc(r + dt * k2r / 2)
        k4r, k4u = u + dt * k3u, acc(r + dt * k3r)
        r_nuevo = r + dt * (k1r + 2 * k2r + 2 * k3r + k4r) / 6
        u_nuevo = u + dt * (k1u + 2 * k2u + 2 * k3u + k4u) / 6
        if u_nuevo <= 0:  # interpolacion lineal del apogeo
            return r + (r_nuevo - r) * u / (u - u_nuevo)
        r, u = r_nuevo, u_nuevo
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rho = M / (4 / 3 * math.pi * A * B * C)
    print(f"Densidad desde los semiejes = {rho:.0f} kg/m3 (hoja: 1610)")
    assert abs(rho / 1610 - 1) < 0.01
    g = G * M / R ** 2
    ve = math.sqrt(2 * G * M / R)
    print(f"R medio = {R / 1e3:.1f} km ; g = {g:.4f} m/s2 ; v_esc = {ve:.1f} m/s")
    for v in (100.0, 200.0, 230.0):
        ae, ar = apogeo_energia(v), apogeo_rk4(v)
        assert abs(ar / ae - 1) < 1e-6
        print(f"v = {v:5.0f} m/s -> altura de apogeo: energia {(ae - R) / 1e3:7.2f} km ; RK4 {(ar - R) / 1e3:7.2f} km")
    print(f"v = 400 m/s (NASA) = {400 / ve:.2f} x v_esc -> {'escapa' if 400 > ve else 'vuelve'} (sin arrastre ni Saturno)")
    assert 400 > ve
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
