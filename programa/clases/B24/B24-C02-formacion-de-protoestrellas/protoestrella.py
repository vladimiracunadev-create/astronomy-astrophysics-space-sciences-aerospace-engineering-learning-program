#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C02: energia gravitatoria, tiempo de Kelvin-Helmholtz y luminosidad de acrecion.

Datos: G, k_B, m_p (NIST CODATA 2022, consultados 2026-11-09); GM_sol, R_sol y L_sol
nominales (IAU 2015 B3, arXiv:1510.07674). Masa, radio y tasa de acrecion de la
protoestrella de ejemplo: valores ILUSTRATIVOS (estimados), no una estrella concreta.
Modelo: esfera uniforme (energia gravitatoria Omega = -3/5 G M^2/R), teorema del virial
(mitad de la energia liberada se irradia: t_KH = |Omega|/(2 L)), luminosidad de acrecion
L_acc = G M Mdot / R (toda la energia cinetica de caida se irradia).
Supuestos: sin rotacion; una estrella real esta mas condensada que una esfera uniforme,
asi que |Omega| y t_KH reales son mayores. Validez: orden de magnitud.
Tolerancia de las pruebas: 1e-4 (relativa) en la suma de capas frente a la forma cerrada.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
R_SOL = 6.957e8
L_SOL = 3.828e26
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0
KB, MP = 1.380649e-23, 1.67262192595e-27


def omega_cerrada(M, R):
    return -0.6 * G * M * M / R


def omega_capas(M, R, n=100000):
    """Suma de la energia de ligadura de capas esfericas de densidad uniforme."""
    rho = M / (4 / 3 * math.pi * R ** 3)
    w = 0.0
    dr = R / n
    for i in range(n):
        r = (i + 0.5) * dr
        m_int = 4 / 3 * math.pi * r ** 3 * rho
        dm = 4 * math.pi * r * r * rho * dr
        w -= G * m_int * dm / r
    return w


def t_kh(M, R, L):
    return abs(omega_cerrada(M, R)) / (2 * L)


def l_acrecion(M, mdot, R):
    return G * M * mdot / R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    w_num, w_cer = omega_capas(M_SOL, R_SOL), omega_cerrada(M_SOL, R_SOL)
    assert abs(w_num / w_cer - 1) < 1e-4, "Omega por capas no coincide con -3/5 GM^2/R"
    # Virial: 2K + Omega = 0 -> T medio = G M mu m_p / (5 k R), mu = 0.6
    t_vir = G * M_SOL * 0.6 * MP / (5 * KB * R_SOL)
    n_part = M_SOL / (0.6 * MP)
    assert abs(3 * n_part * KB * t_vir / abs(w_cer) - 1) < 1e-12
    tkh = t_kh(M_SOL, R_SOL, L_SOL)
    m, r, mdot = 0.5 * M_SOL, 2.0 * R_SOL, 1e-6 * M_SOL / YR
    lacc = l_acrecion(m, mdot, r)
    cs = math.sqrt(KB * 10 / (2.33 * MP))
    mdot_shu = cs ** 3 / G
    print(f"|Omega| uniforme (Sol) = {abs(w_cer):.3e} J ; por capas = {abs(w_num):.3e} J")
    print(f"T virial medio (Sol, mu=0.6) = {t_vir:.3e} K")
    print(f"t_KH (Sol, esfera uniforme) = {tkh / YR / 1e6:.2f} Myr")
    print(f"L_acc (0.5 Msol, 2 Rsol, 1e-6 Msol/yr) = {lacc / L_SOL:.2f} Lsol")
    print(f"Mdot ~ c_s^3/G (10 K) = {mdot_shu * YR / M_SOL:.2e} Msol/yr")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
