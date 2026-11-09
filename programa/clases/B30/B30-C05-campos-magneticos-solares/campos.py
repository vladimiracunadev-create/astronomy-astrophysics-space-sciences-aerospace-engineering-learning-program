#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C05: beta del plasma, velocidad de Alfven y conservacion del flujo en las capas solares.

Datos: k_B, mu_0 y masa del proton m_p (NIST CODATA 2022), consultados 2026-11-09. Las densidades (1e23, 1e19, 1e15 m^-3), temperaturas (5772, 1e4, 1.5e6 K) y campos
(0.15, 0.01, 0.001 T) de la fotosfera, la cromosfera y la corona, y las secciones del tubo de flujo son ILUSTRATIVOS (sinteticos).
Modelo: beta = 2 mu_0 n k_B T/B^2 (hidrogeno completamente ionizado: presion total 2 n k T con n pares electron-proton -> aqui se usa n k T para n particulas totales y se indica);
densidad de masa rho = n m_p; velocidad de Alfven v_A = B/sqrt(mu_0 rho); conservacion del flujo B1 A1 = B2 A2; energia magnetica por volumen B^2/(2 mu_0).
Supuestos: plasma de hidrogeno, capas homogeneas. Validez: orden de magnitud.
Tolerancia: v_A por dos vias (B/sqrt(mu_0 rho) y sqrt(2 w_B/rho)) a 1e-12; B2 = B1 A1/A2 a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

KB, MU0, MP = 1.380649e-23, 1.25663706127e-6, 1.67262192595e-27


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    capas = (("fotosfera", 1e23, 5772.0, 0.15), ("cromosfera", 1e19, 1e4, 0.01), ("corona", 1e15, 1.5e6, 1e-3))
    print(f"{'capa (ilustrativa)':<18} {'n [m-3]':>9} {'T [K]':>9} {'B [T]':>8} {'p = n k T [Pa]':>15} {'p_mag [Pa]':>11} {'beta':>9} {'v_A [km/s]':>11}")
    for nombre, n, t, b in capas:
        p = n * KB * t
        pm = b ** 2 / (2 * MU0)
        beta = p / pm
        rho = n * MP
        va = b / math.sqrt(MU0 * rho)
        va2 = math.sqrt(2 * pm / rho)
        assert abs(va / va2 - 1) < 1e-12
        print(f"{nombre:<18} {n:9.1e} {t:9.4g} {b:8.3g} {p:15.4e} {pm:11.4e} {beta:9.4f} {va / 1e3:11.1f}")
    # conservacion del flujo: tubo que se expande entre la fotosfera y la corona
    b1, a1 = 0.15, math.pi * 1e5 ** 2         # radio 100 km
    for f in (10, 100, 1e4):
        a2 = a1 * f
        b2 = b1 * a1 / a2
        assert abs(b2 * a2 / (b1 * a1) - 1) < 1e-12
        print(f"tubo con area x{f:g}: B = {b2:.3e} T (B ~ 1/A)")
    # energia magnetica en un volumen coronal
    w = (1e-2) ** 2 / (2 * MU0)
    print(f"densidad de energia magnetica con B = 0.01 T: {w:.2f} J/m3 ; en (1e7 m)^3 = {w * 1e21:.3e} J = {w * 1e21 * 1e7:.3e} erg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
