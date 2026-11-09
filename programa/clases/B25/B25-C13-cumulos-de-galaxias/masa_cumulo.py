#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C13: masa de un cumulo de galaxias por equilibrio hidrostatico y por dispersion.

Datos: G, k_B, m_p y eV (NIST, CODATA 2022, consultados 2026-11-09). El cumulo es SINTETICO:
kT = 5 keV, beta = 2/3, r_c = 0,2 Mpc, densidad electronica central 3e-3 cm^-3, mu = 0,6 y
mu_e = 1,17 (valores tipicos ILUSTRATIVOS, no medidos).
Modelo: gas isotermo en equilibrio hidrostatico con perfil beta, rho_gas = rho_0 (1 + (r/r_c)^2)^(-3 beta/2).
M(<r) = -(kT r / (G mu m_p)) dln(rho)/dln(r) = 3 beta kT r^3 / (G mu m_p (r_c^2 + r^2)).
Esfera isoterma singular (SIS, r_c -> 0): M(<r) = 2 sigma^2 r / G con sigma^2 = kT/(mu m_p) si beta_espec = 1.
Supuestos: esfericidad, isotermia, equilibrio hidrostatico (sin presion no termica).
Validez: orden de magnitud (factor ~1,5). Tolerancias: 1e-6 (derivada y cuadratura), 1e-9 (limite SIS).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
KB = 1.380649e-23
MP = 1.67262192595e-27
EV = 1.602176634e-19
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
MPC = 3.0856776e22
MU, MU_E = 0.6, 1.17


def dens(r, beta, rc, rho0=1.0):
    return rho0 * (1 + (r / rc) ** 2) ** (-1.5 * beta)


def masa_beta(r, kT, beta, rc):
    return 3 * beta * kT * r ** 3 / (G * MU * MP * (rc * rc + r * r))


def masa_numerica(r, kT, beta, rc, h=1e-5):
    """-kT r/(G mu mp) dln rho/dln r con derivada central en ln r."""
    d = (math.log(dens(r * math.exp(h), beta, rc)) - math.log(dens(r * math.exp(-h), beta, rc))) / (2 * h)
    return -kT * r / (G * MU * MP) * d


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    kT = 5e3 * EV
    beta, rc = 2 / 3, 0.2 * MPC
    # Prueba 1: derivada numerica frente a la forma cerrada
    for r in (0.1 * MPC, 0.5 * MPC, 1.0 * MPC, 2.0 * MPC):
        assert abs(masa_numerica(r, kT, beta, rc) / masa_beta(r, kT, beta, rc) - 1) < 1e-6
    # Prueba 2: limite SIS, r_c -> 0 : 2 sigma^2 r / G
    sigma2 = kT / (MU * MP)
    r = 1.0 * MPC
    assert abs(masa_beta(r, kT, beta, 1e-9 * MPC) / (2 * sigma2 * r / G) - 1) < 1e-9
    # Prueba 3: masa de gas por cuadratura frente a la integral cerrada para beta = 2/3,
    # rho = rho0/(1+x^2): M = 4 pi rho0 rc^3 (x - atan x)
    rho0 = 3e-3 * 1e6 * MU_E * MP  # kg/m^3
    x = 5.0
    num = simpson(lambda s: 4 * math.pi * rho0 * s * s / (1 + (s / rc) ** 2), 0.0, x * rc)
    cer = 4 * math.pi * rho0 * rc ** 3 * (x - math.atan(x))
    assert abs(num / cer - 1) < 1e-8
    m1 = masa_beta(MPC, kT, beta, rc)
    mg = 4 * math.pi * rho0 * rc ** 3 * (5 - math.atan(5))
    sigma = math.sqrt(sigma2)
    print(f"sigma = sqrt(kT/(mu mp)) = {sigma / 1e3:.0f} km/s")
    print(f"M_hidrostatica(<1 Mpc) = {m1 / M_SOL:.3e} Msol ; SIS 2 sigma^2 r/G = {2 * sigma2 * MPC / G / M_SOL:.3e} Msol")
    print(f"M_gas(<1 Mpc) = {mg / M_SOL:.3e} Msol ; fraccion de gas = {mg / m1:.3f}")
    print(f"t_cruce = 1 Mpc / sigma = {MPC / sigma / 3.15576e16 :.2f} Gyr")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
