#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C20: Delta v de transferencia Tierra-Marte y masa de propelente de una mision conceptual.

Datos: semieje mayor de Marte 227,956e9 m (hoja de datos de Marte de la NASA/NSSDC, consultada
el 2026-11-09). NO CONSULTADOS (valores estandar recordados, ILUSTRATIVOS): GM del Sol
1,32712440018e20 m3/s2 y la UA 149 597 870 700 m (la IAU 2015 B3 consultada da los valores
nominales solares de irradiancia y luminosidad, no el GM). Orbita de la Tierra circular de 1 UA y
orbita de Marte circular de 227,956e9 m, coplanares (simplificacion). Isp de 320 s, masa seca de
1000 kg y g0 = 9,80665 m/s2 son SINTETICOS e ILUSTRATIVOS.
Modelo: transferencia de Hohmann entre orbitas circulares; los Delta v son de exceso
heliocentrico (velocidad hiperbolica de salida y de llegada), sin salida del pozo de la Tierra
ni captura en Marte. Tiempo de vuelo = pi sqrt(a^3/mu). Ecuacion del cohete:
m0/mf = exp(Delta v/(Isp g0)).
Supuestos: orbitas circulares y coplanares, impulsos instantaneos. Validez: primer orden;
una mision real requiere ventanas de lanzamiento y orbitas de aparcamiento. Tolerancia: el
tiempo de vuelo integrado con RK4 coincide con la forma cerrada a 1e-6 relativo.
"""
from __future__ import annotations
import math
import platform
import sys

MU = 1.32712440018e20
R1 = 149597870700.0
R2 = 227.956e9
G0 = 9.80665


def hohmann(r1, r2):
    a = (r1 + r2) / 2
    dv1 = math.sqrt(MU / r1) * (math.sqrt(2 * r2 / (r1 + r2)) - 1)
    dv2 = math.sqrt(MU / r2) * (1 - math.sqrt(2 * r1 / (r1 + r2)))
    t = math.pi * math.sqrt(a ** 3 / MU)
    return dv1, dv2, t


def tiempo_rk4(r1, r2, dt=3600.0):
    a = (r1 + r2) / 2
    x, y = r1, 0.0
    vx, vy = 0.0, math.sqrt(MU * (2 / r1 - 1 / a))
    acc = lambda px, py: (-MU * px / (px * px + py * py) ** 1.5, -MU * py / (px * px + py * py) ** 1.5)
    t = 0.0
    while True:
        ax, ay = acc(x, y)
        k1 = (vx, vy, ax, ay)
        a2 = acc(x + dt / 2 * k1[0], y + dt / 2 * k1[1])
        k2 = (vx + dt / 2 * k1[2], vy + dt / 2 * k1[3], a2[0], a2[1])
        a3 = acc(x + dt / 2 * k2[0], y + dt / 2 * k2[1])
        k3 = (vx + dt / 2 * k2[2], vy + dt / 2 * k2[3], a3[0], a3[1])
        a4 = acc(x + dt * k3[0], y + dt * k3[1])
        k4 = (vx + dt * k3[2], vy + dt * k3[3], a4[0], a4[1])
        nx = x + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        ny = y + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        nvx = vx + dt / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        nvy = vy + dt / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
        if ny < 0:  # cruce del eje x: apoastro
            return t + dt * y / (y - ny)
        x, y, vx, vy, t = nx, ny, nvx, nvy, t + dt


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dv1, dv2, t = hohmann(R1, R2)
    print(f"Delta v de salida = {dv1 / 1e3:.3f} km/s ; de llegada = {dv2 / 1e3:.3f} km/s ; tiempo de vuelo = {t / 86400:.1f} d")
    t_n = tiempo_rk4(R1, R2)
    print(f"Tiempo de vuelo por RK4 = {t_n / 86400:.2f} d")
    assert abs(t_n / t - 1) < 1e-6
    isp, seca = 320.0, 1000.0
    for dv in (dv1, dv1 + dv2):
        razon = math.exp(dv / (isp * G0))
        prop = seca * (razon - 1)
        print(f"Delta v = {dv / 1e3:.3f} km/s -> m0/mf = {razon:.3f} ; propelente = {prop:.0f} kg para {seca:.0f} kg secos")
    assert 2.9e3 < dv1 < 3.0e3
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
