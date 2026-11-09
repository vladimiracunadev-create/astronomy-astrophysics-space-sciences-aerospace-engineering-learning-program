#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C04: masa de gas molecular desde el CO y extincion por polvo.

Datos: X_CO = 2e20 cm^-2 (K km/s)^-1 (+-30 %), valor recomendado para el disco de la Via Lactea
(Bolatto, Wolfire y Leroy 2013, arXiv:1301.3498, resumen consultado 2026-11-09);
N_H = 2,21e21 A_V cm^-2 mag^-1 (+-0,09e21) (Guver y Ozel 2009, arXiv:0903.2057, resumen
consultado 2026-11-09). Constantes: m_p (NIST, CODATA 2022); GM_sol (IAU 2015 B3);
1 pc = 3,0856776e16 m (conversion). La nube (W_CO, area, A_V) es SINTETICA.
Modelo: N(H2) = X_CO W_CO; masa M = N(H2) mu_H2 m_H A con mu_H2 = 2,72 (2 H por molecula x 1,36
por el helio, valor ILUSTRATIVO); extincion A = -2,5 log10(F/F0); tau = A / (2,5 log10 e).
Supuestos: X_CO constante y CO opticamente grueso en la escala de la nube; A_V uniforme.
Validez: orden de magnitud (X_CO tiene +-30 % en el disco y varia con la metalicidad).
Tolerancias: 1e-9 en identidades.
"""
from __future__ import annotations
import math
import platform
import sys

MP = 1.67262192595e-27
MSOL = 1.3271244e20 / 6.67430e-11
PC = 3.0856776e16
X_CO = 2.0e20
NH_POR_AV = 2.21e21
MU_H2 = 2.72


def masa_gas(w_co_kms_k, area_pc2, x=X_CO, mu=MU_H2):
    """Masa (Msol) de gas molecular con helio, desde W_CO (K km/s) sobre un area (pc^2)."""
    n_h2_cm2 = x * w_co_kms_k
    kg_por_cm2 = n_h2_cm2 * mu * MP
    area_cm2 = area_pc2 * (PC * 100.0) ** 2
    return kg_por_cm2 * area_cm2 / MSOL


def alfa_co(x=X_CO, mu=MU_H2):
    """Msol por (K km/s pc^2)."""
    return masa_gas(1.0, 1.0, x, mu)


def extincion_de_flujo(razon):
    return -2.5 * math.log10(razon)


def transmision(a_mag):
    return 10 ** (-0.4 * a_mag)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: via independiente de alfa_CO en gramos por cm^2 -> Msol/pc^2
    g_cm2 = X_CO * MU_H2 * MP * 1e3
    msol_pc2 = g_cm2 * (PC * 100.0) ** 2 / (MSOL * 1e3)
    assert abs(msol_pc2 / alfa_co() - 1) < 1e-9
    # Prueba 2: ida y vuelta flujo <-> magnitudes
    for a in (0.0, 1.0, 5.0, 12.5):
        assert abs(extincion_de_flujo(transmision(a)) - a) < 1e-9
    # Prueba 3: A = 1 mag -> tau = 0,921 (identidad 2,5 log10 e = 1,0857)
    assert abs(1.0 / (2.5 * math.log10(math.e)) - 0.9210340372) < 1e-9
    # Prueba 4: proporcionalidad de la masa con W_CO y area
    assert abs(masa_gas(20.0, 300.0) / masa_gas(10.0, 600.0) - 1) < 1e-12
    w, area = 10.0, 400.0  # nube SINTETICA
    m = masa_gas(w, area)
    n_h2 = X_CO * w
    av = n_h2 * 2 / NH_POR_AV
    print(f"alfa_CO = {alfa_co():.2f} Msol / (K km/s pc^2)")
    print(f"nube sintetica: W_CO = {w} K km/s, A = {area} pc^2 -> N(H2) = {n_h2:.2e} cm^-2")
    print(f"M = {m:.3e} Msol ; A_V = {av:.1f} mag ; transmision en V = {transmision(av):.2e}")
    print(f"tau_V = {av / (2.5 * math.log10(math.e)):.1f}")
    print(f"con X_CO +-30 %: M entre {masa_gas(w, area, 0.7 * X_CO):.3e} y {masa_gas(w, area, 1.3 * X_CO):.3e} Msol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
