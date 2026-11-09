#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C10: estimador de masa de una galaxia enana y su sesgo en un caso analitico.

Datos: G (NIST, CODATA 2022, 2026-11-09). Estimador M_1/2 = 3 sigma_los^2 r_1/2 / G ~ 4 sigma_los^2 R_e / G
(Wolf et al. 2010, arXiv:0908.2995, resumen consultado 2026-11-09). La enana (sigma = 7 km/s,
R_e = 300 pc, L = 1e6 Lsol) es SINTETICA, no una galaxia observada.
Modelo de comprobacion: esfera de Plummer isotropa (C06), de la que se conocen de forma exacta
la superficie Sigma(R) = M a^2 / (pi (R^2 + a^2)^2), el radio efectivo R_e = a, el radio de media
masa 3D r_1/2 = 1,3048 a y la dispersion global sigma_los^2 = pi G M / (32 a).
Supuestos: esfericidad, isotropia, masa que sigue a la luz (solo para el caso de comprobacion).
Validez: el caso de Plummer mide el sesgo del estimador; no lo valida para galaxias reales.
Tolerancias: 1e-6 (proyeccion numerica) y 1e-9 (identidades).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
M_SOL = 1.3271244e20 / G
PC = 3.0856776e16


def rho_plummer(r, M, a):
    return 3 * M * a * a / (4 * math.pi * (r * r + a * a) ** 2.5)


def simpson(f, a, b, n=40000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def sigma_proyectada(R, M, a):
    """Sigma(R) = 2 int_0^inf rho(sqrt(R^2+u^2)) du, truncada en 300 a."""
    return 2 * simpson(lambda u: rho_plummer(math.sqrt(R * R + u * u), M, a), 0.0, 300 * a)


def masa_proyectada(R, M, a):
    return M * R * R / (R * R + a * a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    M, a = 1.0, 1.0  # unidades G = 1 para la comprobacion adimensional
    # Prueba 1: proyeccion numerica frente a la forma cerrada, en tres radios
    for R in (0.3, 1.0, 3.0):
        num = sigma_proyectada(R, M, a)
        ana = M * a * a / (math.pi * (R * R + a * a) ** 2)
        assert abs(num / ana - 1) < 1e-6, "Sigma(R) de Plummer"
    # Prueba 2: R_e = a por biseccion sobre la masa proyectada
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if masa_proyectada(mid, M, a) < 0.5 * M:
            lo = mid
        else:
            hi = mid
    re = 0.5 * (lo + hi)
    assert abs(re - a) < 1e-9
    # radio de media masa 3D
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid ** 3 / (mid * mid + a * a) ** 1.5 < 0.5:
            lo = mid
        else:
            hi = mid
    r_half = 0.5 * (lo + hi)
    # Prueba 3: sigma_los^2 global por integral de rho sigma^2 (Jeans de C06) frente a pi G M/(32 a)
    s2 = lambda r: 1.0 / (6 * math.sqrt(r * r + a * a))  # G = M = 1
    dos_k = 3 * simpson(lambda r: 4 * math.pi * r * r * rho_plummer(r, M, a) * s2(r), 0.0, 400 * a, 200000)
    sig_los2 = dos_k / 3.0 / M
    assert abs(sig_los2 / (math.pi / 32) - 1) < 1e-6
    estimado = 3 * sig_los2 * r_half
    estimado_4 = 4 * sig_los2 * re
    print(f"R_e = {re:.6f} a ; r_1/2 = {r_half:.4f} a ; r_1/2/R_e = {r_half / re:.4f} (4/3 = {4 / 3:.4f})")
    print(f"sigma_los^2 = {sig_los2:.5f} G M / a (pi/32 = {math.pi / 32:.5f})")
    print(f"M_est(3 s^2 r_1/2)/M_1/2 = {estimado / 0.5:.3f} ; M_est(4 s^2 R_e)/M_1/2 = {estimado_4 / 0.5:.3f}")
    # enana sintetica
    sigma, re_pc, lum = 7e3, 300.0, 1e6
    m12 = 4 * sigma ** 2 * re_pc * PC / G / M_SOL
    print(f"enana sintetica: M_1/2 = 4 sigma^2 R_e / G = {m12:.3e} Msol ; M/L(<r_1/2) = {m12 / (lum / 2):.0f} Msol/Lsol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
