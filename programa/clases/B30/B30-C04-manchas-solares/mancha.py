#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C04: equilibrio de presiones, contraste y flujo magnetico de una mancha solar.

Datos: mu_0 y sigma_SB (NIST CODATA 2022); R_sol, T_eff,sol = 5772 K y S_sol = 1361 W/m2 (IAU 2015 B3), consultados 2026-11-09. El campo de la mancha (0.3 T),
su temperatura (4000 K en la umbra, 5400 K en la penumbra), el radio (10 Mm), la presion fotosferica (1e5 Pa) y los 1000 millonesimos de hemisferio de area total
son ILUSTRATIVOS (sinteticos); no se simula ninguna mancha concreta.
Modelo: equilibrio de presiones horizontal P_gas,fuera = P_gas,dentro + B^2/(2 mu_0); contraste bolometrico (T/T_eff)^4 con la ley de Stefan-Boltzmann; flujo magnetico
Phi = B pi r^2; area en millonesimos de hemisferio (MSH) = A/(2 pi R_sol^2) x 1e6; deficit de irradiancia dS/S = (area proyectada/(pi R^2)) (1 - contraste).
Supuestos: campo uniforme vertical, simetria circular. Validez: orden de magnitud.
Tolerancia: la conversion de area a MSH y de vuelta con 1e-12; contraste de la fotosfera = 1 a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

MU0, SIG = 1.25663706127e-6, 5.670374419e-8
R_SOL, T_SOL, S_SOL = 6.957e8, 5772.0, 1361.0


def a_msh(area):
    return area / (2 * math.pi * R_SOL ** 2) * 1e6


def de_msh(msh):
    return msh * 1e-6 * 2 * math.pi * R_SOL ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    b, r = 0.3, 1.0e7
    p_mag = b ** 2 / (2 * MU0)
    p_fuera = 1.0e5
    print(f"presion magnetica B^2/(2 mu_0) con B = {b} T: {p_mag:.4e} Pa ; presion gas fuera (ilustrativa) = {p_fuera:.1e} Pa ; presion gas dentro = {p_fuera - p_mag:.4e} Pa ({(p_fuera - p_mag) / p_fuera * 100:.1f} % de la de fuera)")
    area = math.pi * r ** 2
    phi = b * area
    msh = a_msh(area)
    assert abs(de_msh(msh) / area - 1) < 1e-12
    print(f"mancha de r = 10 Mm: area = {area:.4e} m2 = {msh:.1f} millonesimos de hemisferio ; flujo magnetico = {phi:.4e} Wb = {phi * 1e8:.3e} Mx")
    print(f"{'region':<10} {'T [K]':>7} {'contraste (T/T_eff)^4':>22} {'flujo [W/m2]':>13}")
    for nombre, t in (("fotosfera", T_SOL), ("penumbra", 5400.0), ("umbra", 4000.0)):
        c = (t / T_SOL) ** 4
        print(f"{nombre:<10} {t:7.0f} {c:22.4f} {SIG * t ** 4:13.4e}")
    assert abs((T_SOL / T_SOL) ** 4 - 1) < 1e-12
    # deficit de irradiancia con 1000 MSH
    total_msh = 1000.0
    a_total = de_msh(total_msh)
    frac_proy = a_total / (math.pi * R_SOL ** 2) * 0.5      # proyeccion media sobre el disco (aprox. 1/2 por escorzo)
    c_umbra = (4000.0 / T_SOL) ** 4
    ds = frac_proy * (1 - c_umbra)
    print(f"1000 MSH de umbra: area = {a_total:.3e} m2 ; fraccion del disco proyectada (factor 1/2 ilustrativo) = {frac_proy * 100:.4f} % ; deficit de irradiancia = {ds * 100:.4f} % = {ds * S_SOL:.3f} W/m2")
    # sensibilidad: campo para equilibrar completamente la presion
    b_max = math.sqrt(2 * MU0 * p_fuera)
    print(f"campo que anula la presion de gas en un entorno de {p_fuera:.0e} Pa: B = {b_max:.3f} T")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
