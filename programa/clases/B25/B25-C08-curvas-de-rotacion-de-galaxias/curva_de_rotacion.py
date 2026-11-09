#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C08: curva de rotacion de un disco exponencial y halo necesario.

Datos: G (NIST, CODATA 2022, 2026-11-09); Sigma_0 = 890 Msol/pc2 y R_d = 2,6 kpc derivados en C01 de
Bland-Hawthorn y Gerhard (2016, arXiv:1602.07702, texto del PDF consultado 2026-11-09);
Theta0 = 238 km/s y R0 = 8,2 kpc de la misma fuente (observados). El radio del nucleo del halo
(5 kpc) es ILUSTRATIVO.
Modelo: (a) disco exponencial delgado de Freeman, v^2 = 4 pi G Sigma_0 R_d y^2 [I0 K0 - I1 K1], y = R/(2 R_d),
con funciones de Bessel calculadas por cuadratura propia; (b) halo pseudo-isotermo
v^2 = v_inf^2 [1 - (r_c/R) arctan(R/r_c)].
Supuestos: disco sin bulbo, barra ni gas; halo esferico; v_inf elegido para que el total sea Theta0 en R0.
Validez: orden de magnitud; la fraccion de disco depende de Sigma_0 y R_d. Tolerancias: 1e-9 (Bessel
frente a valores tabulados y al wronskiano), 2e-2 (limite kepleriano a 100 R_d).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
M_SOL = 1.3271244e20 / G
PC = 3.0856776e16
KPC = 1e3 * PC


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def bessel_i(n, x):
    return simpson(lambda t: math.exp(x * math.cos(t)) * math.cos(n * t), 0.0, math.pi) / math.pi


def bessel_k(n, x):
    tmax = math.acosh(1 + 80.0 / x) if x < 80 else 1.0
    return simpson(lambda t: math.exp(-x * math.cosh(t)) * math.cosh(n * t), 0.0, tmax, 8000)


def v2_disco(R, sig0_msol_pc2, rd_kpc):
    """(m/s)^2 de un disco exponencial en R (kpc)."""
    y = R / (2 * rd_kpc)
    sig0 = sig0_msol_pc2 * M_SOL / PC ** 2  # kg/m2
    rd = rd_kpc * KPC
    return 4 * math.pi * G * sig0 * rd * y * y * (bessel_i(0, y) * bessel_k(0, y) - bessel_i(1, y) * bessel_k(1, y))


def v2_halo(R, vinf, rc):
    return vinf ** 2 * (1 - rc / R * math.atan(R / rc))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: valores tabulados de Bessel en x = 1
    assert abs(bessel_i(0, 1.0) - 1.2660658777520082) < 1e-9
    assert abs(bessel_i(1, 1.0) - 0.5651591039924851) < 1e-9
    assert abs(bessel_k(0, 1.0) - 0.42102443824070834) < 1e-9
    assert abs(bessel_k(1, 1.0) - 0.6019072301972346) < 1e-9
    # Prueba 2: wronskiano I0 K1 + I1 K0 = 1/x
    for x in (0.3, 1.0, 4.0):
        assert abs(bessel_i(0, x) * bessel_k(1, x) + bessel_i(1, x) * bessel_k(0, x) - 1 / x) < 1e-9
    sig0, rd, R0, theta = 890.0, 2.6, 8.2, 238e3
    # Prueba 3: limite kepleriano lejos del disco, v^2 -> G M / R con M = 2 pi Sigma_0 R_d^2
    M = 2 * math.pi * (sig0 * M_SOL / PC ** 2) * (rd * KPC) ** 2
    R = 100 * rd
    assert abs(v2_disco(R, sig0, rd) * R * KPC / (G * M) - 1) < 2e-2
    v_d = math.sqrt(v2_disco(R0, sig0, rd))
    # maximo del disco
    mejor = max((v2_disco(0.05 * rd * i, sig0, rd), 0.05 * i) for i in range(10, 200))
    v_inf = math.sqrt((theta ** 2 - v_d ** 2) / (1 - 5.0 / R0 * math.atan(R0 / 5.0)))
    print(f"M_disco = {M / M_SOL:.3e} Msol ; v_disco(R0) = {v_d / 1e3:.1f} km/s ({v_d / theta:.2f} de Theta0)")
    print(f"maximo del disco: {math.sqrt(mejor[0]) / 1e3:.1f} km/s en R = {mejor[1]:.2f} R_d")
    print(f"halo necesario (r_c = 5 kpc): v_inf = {v_inf / 1e3:.0f} km/s ; fraccion de v^2 del halo en R0 = {1 - (v_d / theta) ** 2:.2f}")
    for r in (2.0, 5.0, 8.2, 15.0, 30.0):
        vt = math.sqrt(v2_disco(r, sig0, rd) + v2_halo(r, v_inf, 5.0))
        print(f"R = {r:5.1f} kpc: disco {math.sqrt(v2_disco(r, sig0, rd)) / 1e3:6.1f} ; halo {math.sqrt(v2_halo(r, v_inf, 5.0)) / 1e3:6.1f} ; total {vt / 1e3:6.1f} km/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
