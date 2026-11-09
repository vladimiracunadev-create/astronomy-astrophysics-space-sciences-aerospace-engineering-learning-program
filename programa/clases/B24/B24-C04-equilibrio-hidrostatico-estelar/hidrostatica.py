#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C04: equilibrio hidrostatico de una estrella de densidad uniforme.

Datos: G, k_B, m_p (NIST CODATA 2022, consultados 2026-11-09); GM_sol y R_sol nominales
(IAU 2015 B3); presion y temperatura centrales del Sol segun el modelo de la NASA Sun Fact
Sheet (actualizada 2024-05-09): 2.477e11 bar y 1.571e7 K (valores de MODELO, no medidos).
Modelo: dP/dr = -G m(r) rho / r^2 con rho uniforme; solucion cerrada
P(r) = (3 G M^2 / (8 pi R^4)) (1 - r^2/R^2). T virial media = G M mu m_p /(5 k R).
Supuestos: densidad uniforme (el Sol real esta muy condensado). Validez: cota inferior de
P_c y orden de magnitud de T. Tolerancia: 1e-6 relativa entre integracion RK4 y forma cerrada.
"""
from __future__ import annotations
import math
import platform
import sys

G, KB, MP = 6.67430e-11, 1.380649e-23, 1.67262192595e-27
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
M_SOL = GM_SOL / G
BAR = 1e5


def p_central_cerrada(M, R):
    return 3 * G * M * M / (8 * math.pi * R ** 4)


def p_central_rk4(M, R, n=2000):
    """Integra dP/dr desde la superficie (P=0) hasta el centro con RK4."""
    rho = M / (4 / 3 * math.pi * R ** 3)

    def f(r):
        return -G * (4 / 3 * math.pi * r ** 3 * rho) * rho / (r * r) if r > 0 else 0.0

    h = -R / n
    r, p = R, 0.0
    for _ in range(n):
        k1 = f(r)
        k2 = f(r + h / 2)
        k3 = f(r + h / 2)
        k4 = f(r + h)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        r += h
    return p


def t_virial(M, R, mu=0.6):
    return G * M * mu * MP / (5 * KB * R)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    pc_c, pc_n = p_central_cerrada(M_SOL, R_SOL), p_central_rk4(M_SOL, R_SOL)
    assert abs(pc_n / pc_c - 1) < 1e-6, "RK4 no reproduce la solucion cerrada"
    assert abs(p_central_cerrada(2 * M_SOL, R_SOL) / pc_c - 4) < 1e-12
    assert abs(p_central_cerrada(M_SOL, 2 * R_SOL) / pc_c - 1 / 16) < 1e-12
    pc_mod = 2.477e11 * BAR
    tv = t_virial(M_SOL, R_SOL)
    print(f"P_c uniforme (cerrada) = {pc_c:.4e} Pa ; RK4 = {pc_n:.4e} Pa")
    print(f"P_c modelo NASA = {pc_mod:.4e} Pa ; cociente modelo/uniforme = {pc_mod / pc_c:.0f}")
    print(f"T virial media = {tv:.3e} K ; T central modelo NASA = 1.571e+07 K ; cociente = {1.571e7 / tv:.1f}")
    t_dyn = math.sqrt(R_SOL ** 3 / GM_SOL)
    rho_m = M_SOL / (4 / 3 * math.pi * R_SOL ** 3)
    t_ff = math.sqrt(3 * math.pi / (32 * G * rho_m))
    assert abs(t_ff / t_dyn - math.pi / math.sqrt(8)) < 1e-12, "t_ff/t_dyn = pi/sqrt(8) para esfera uniforme"
    a_rad = 4 * 5.670374419e-8 / 299792458.0
    p_rad = a_rad * (1.571e7) ** 4 / 3
    print(f"t_dyn = {t_dyn:.0f} s = {t_dyn / 60:.1f} min ; t_ff medio = {t_ff / 60:.1f} min ; g = {GM_SOL / R_SOL ** 2:.1f} m/s2")
    print(f"P_rad centro = {p_rad:.3e} Pa ; fraccion del modelo = {p_rad / pc_mod:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
