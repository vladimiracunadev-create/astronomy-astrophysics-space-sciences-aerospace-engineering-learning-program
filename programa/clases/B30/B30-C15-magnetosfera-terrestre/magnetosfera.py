#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C15: dipolo terrestre, distancia a la magnetopausa y radio geosincrono.

Datos: mu_0 y m_p (NIST CODATA 2022); GM_E y R_E ecuatorial (IAU 2015 B3), consultados 2026-11-09. El campo ecuatorial superficial B_0 = 3.12e-5 T, la rotacion terrestre
7.2921150e-5 rad/s (valor estandar, no consultado) y las condiciones del viento solar (n = 5e6 m^-3, v = 400 km/s y sus variaciones) son ILUSTRATIVOS (sinteticos).
Modelo: campo dipolar B(r, lat) = B_0 (R_E/r)^3 sqrt(1 + 3 sen^2 lat); linea de campo r = L R_E cos^2 lat; magnetopausa por equilibrio de presiones
rho v^2 = (2 B_0 (R_E/r)^3)^2/(2 mu_0) (factor 2 del dipolo comprimido), resuelta por biseccion y comparada con la forma cerrada r/R_E = [2 B_0^2/(mu_0 rho v^2)]^(1/6);
radio geosincrono (GM_E/Omega^2)^(1/3).
Supuestos: dipolo centrado y alineado, magnetopausa sub-solar, sin presion del plasma magnetosferico. Validez: orientativa.
Tolerancia: biseccion frente a la forma cerrada dentro de 1e-9 relativo; radio geosincrono y altitud por dos vias a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

MU0, MP = 1.25663706127e-6, 1.67262192595e-27
GM_E, R_E = 3.986004e14, 6.3781e6
B0, OMEGA = 3.12e-5, 7.2921150e-5


def campo(r, lat):
    return B0 * (R_E / r) ** 3 * math.sqrt(1 + 3 * math.sin(lat) ** 2)


def r_mp_cerrada(n, v):
    rho = n * MP
    return (2 * B0 ** 2 / (MU0 * rho * v ** 2)) ** (1 / 6)


def r_mp_biseccion(n, v):
    rho = n * MP
    lo, hi = 1.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        b = 2 * B0 * mid ** -3
        if b * b / (2 * MU0) > rho * v * v:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'L':>5} {'B ecuatorial [nT]':>18} {'lat en superficie [deg]':>24} {'B superficie [nT]':>18}")
    for l in (2.0, 4.0, 6.6, 10.0):
        beq = campo(l * R_E, 0.0)
        lat = math.acos(math.sqrt(1 / l))
        bs = campo(R_E, lat)
        # la linea r = L R_E cos^2 lat corta r = R_E cuando cos^2 lat = 1/L
        print(f"{l:5.1f} {beq * 1e9:18.1f} {math.degrees(lat):24.2f} {bs * 1e9:18.0f}")
    print(f"campo en el ecuador superficial B_0 = {B0 * 1e9:.0f} nT ; en el polo (lat = 90) = {campo(R_E, math.pi / 2) * 1e9:.0f} nT (el doble)")
    assert abs(campo(R_E, math.pi / 2) / B0 - 2) < 1e-12
    # magnetopausa
    n0, v0 = 5e6, 4e5
    rho = n0 * MP
    print(f"viento solar ilustrativo: n = {n0:.0e} m-3, v = {v0 / 1e3:.0f} km/s -> presion dinamica rho v^2 = {rho * v0 ** 2 * 1e9:.3f} nPa")
    print(f"{'n [m-3]':>9} {'v [km/s]':>9} {'P_din [nPa]':>12} {'r_mp [R_E] biseccion':>21} {'cerrada':>9}")
    for n, v in ((5e6, 3e5), (5e6, 4e5), (5e6, 6e5), (5e6, 8e5), (2e7, 4e5), (2e7, 8e5), (5e7, 1e6)):
        rb, rc = r_mp_biseccion(n, v), r_mp_cerrada(n, v)
        assert abs(rb / rc - 1) < 1e-9
        print(f"{n:9.0e} {v / 1e3:9.0f} {n * MP * v * v * 1e9:12.3f} {rb:21.3f} {rc:9.3f}")
    # exponente 1/6
    r1, r2 = r_mp_cerrada(5e6, 4e5), r_mp_cerrada(5e6 * 64, 4e5)
    print(f"presion dinamica x64 -> r_mp /{r1 / r2:.4f} (esperado 64^(1/6) = {64 ** (1 / 6):.4f})")
    assert abs(r1 / r2 - 2) < 1e-9
    # orbita geosincrona
    rg = (GM_E / OMEGA ** 2) ** (1 / 3)
    t = 2 * math.pi / OMEGA
    rg2 = (GM_E * t ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    assert abs(rg / rg2 - 1) < 1e-12
    print(f"radio geosincrono: {rg / 1e3:.1f} km = {rg / R_E:.3f} R_E ; altitud = {(rg - R_E) / 1e3:.1f} km ; periodo = {t:.1f} s")
    print(f"campo dipolar ilustrativo en el ecuador geosincrono: {campo(rg, 0.0) * 1e9:.1f} nT")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
