#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C10: corrimiento al rojo gravitacional exacto frente a campo debil.

Datos: c exacta y G (NIST CODATA 2022, consultados 2026-11-09); GM y radios nominales del Sol y de la
Tierra (IAU 2015 B3, arXiv:1510.07674, texto del PDF extraido el 2026-11-09). Enana blanca (0.6 Msol,
0.0127 Rsol, de B24-C03), estrella de neutrones (1.4 Msol, 10 km) y radio de la orbita (2.6e7 m):
valores ILUSTRATIVOS (sinteticos). Prueba con satelites Galileo: desviacion (+0.19 +/- 2.48)e-5
(Delva et al., arXiv:1812.03711, resumen, consultado 2026-11-09).
Modelo: un fotón emitido por un emisor estatico en r = R llega al infinito con 1 + z = 1/sqrt(1 - r_s/R),
r_s = 2GM/c^2. Campo debil: z ~ x + (3/2) x^2 + (5/2) x^3, con x = GM/(R c^2) (serie de la forma exacta).
Entre un suelo (R) y una orbita (r) la razon de frecuencias es sqrt((1 - r_s/R)/(1 - r_s/r)).
Supuestos: emisor estatico, metrica de Schwarzschild, sin rotacion. Validez: R > r_s (el emisor esta fuera del horizonte).
Tolerancia: 1e-6 relativa entre la forma exacta y la serie para x = 1e-3 (el error es O(x^4)).
"""
from __future__ import annotations
import math
import platform
import sys

C, G = 299792458.0, 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
GM_E, R_E = 3.986004e14, 6.3781e6


def z_exacto(gm, R):
    rs = 2 * gm / C ** 2
    return 1 / math.sqrt(1 - rs / R) - 1


def z_debil(gm, R):
    x = gm / (R * C ** 2)
    return x + 1.5 * x * x + 2.5 * x ** 3


def razon(gm, R, r):
    rs = 2 * gm / C ** 2
    return math.sqrt((1 - rs / R) / (1 - rs / r))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    cuerpos = [("Tierra", GM_E, R_E), ("Sol", GM_SOL, R_SOL),
               ("enana blanca (0.6 Msol, 0.0127 Rsol)", 0.6 * GM_SOL, 0.0127 * R_SOL),
               ("estrella de neutrones (1.4 Msol, 10 km)", 1.4 * GM_SOL, 1.0e4)]
    print(f"{'cuerpo':42s} {'GM/(R c^2)':>11s} {'z exacto':>12s} {'z debil':>12s} {'c z [km/s]':>12s}")
    for nombre, gm, R in cuerpos:
        ze, zw = z_exacto(gm, R), z_debil(gm, R)
        x = gm / (R * C ** 2)
        print(f"{nombre:42s} {x:11.3e} {ze:12.4e} {zw:12.4e} {C * ze / 1e3:12.4g}")
    # series: error O(x^4)
    gm, R = 1.0e-3 * C ** 2, 1.0
    assert abs(z_exacto(gm, R) / z_debil(gm, R) - 1) < 1e-6
    # coherencia con el tiempo propio: 1/(1+z) = sqrt(1 - rs/R)
    for _, gm, R in cuerpos:
        rs = 2 * gm / C ** 2
        assert abs(1 / (1 + z_exacto(gm, R)) - math.sqrt(1 - rs / R)) < 1e-12
    # suelo -> orbita
    r_orb = 2.6e7
    f = razon(GM_E, R_E, r_orb)
    print(f"razon de frecuencias orbita/suelo (r = {r_orb:.1e} m) = {f:.12f} ; 1 - f = {1 - f:.4e}")
    dia = 86400 * (1 - f)
    print(f"la parte gravitacional adelanta el reloj orbital en {dia * 1e6:.1f} us por dia")
    assert abs((1 - f) - GM_E * (1 / R_E - 1 / r_orb) / C ** 2) < 1e-14
    print("incertidumbre de la prueba Galileo (1 sigma) sobre el efecto: 2.48e-5")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
