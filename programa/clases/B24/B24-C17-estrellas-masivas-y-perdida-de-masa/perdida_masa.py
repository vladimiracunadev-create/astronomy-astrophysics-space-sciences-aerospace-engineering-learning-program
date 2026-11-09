#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C17: factor de Eddington y masa perdida acumulada de una estrella masiva.

Datos: constantes de NIST (CODATA 2022, consultados 2026-11-09): sigma_T, G, c, m_p;
GM_sol y L_sol nominales (IAU 2015 B3); epsilon c^2 = 6.3978e14 J/kg (B24-C06). Las parejas
(M, L), la tasa de perdida de masa y los tiempos son valores ILUSTRATIVOS (sinteticos), no de
estrellas catalogadas; Smith (2014) senala que las tasas de vientos de estrellas calientes
parecen 2-3 veces menores que las de modelos anteriores (solo resumen consultado).
Modelo: Gamma = L / L_Edd con L_Edd = 4 pi G M c / kappa_es y kappa_es = sigma_T (1+X)/(2 m_p);
perdida de masa dM/dt = -k M^2 (k = Mdot0 / M0^2), con solucion exacta 1/M = 1/M0 + k t,
integrada con RK4; vida t = f X M epsilon c^2 / L.
Supuestos: opacidad de Thomson, gas ionizado, X = 0.7; Mdot proporcional a M^2 solo para ilustrar
una solucion exacta. Validez: ilustrativa. Tolerancia: 1e-9 entre RK4 y la solucion exacta.
"""
from __future__ import annotations
import platform
import sys

G, C, MP, SIGMA_T = 6.67430e-11, 299792458.0, 1.67262192595e-27, 6.6524587051e-29
GM_SOL, L_SOL = 1.3271244e20, 3.828e26
M_SOL = GM_SOL / G
EPS_C2, YR = 6.3978e14, 365.25 * 86400.0
X = 0.7


def kappa():
    return SIGMA_T * (1 + X) / (2 * MP)


def l_edd(m_sol):
    return 4 * 3.141592653589793 * G * m_sol * M_SOL * C / kappa() / L_SOL


def masa_exacta(m0, k, t):
    return 1.0 / (1.0 / m0 + k * t)


def masa_rk4(m0, k, t, n=4000):
    f = lambda m: -k * m * m
    h, m = t / n, m0
    for _ in range(n):
        k1 = f(m); k2 = f(m + h * k1 / 2); k3 = f(m + h * k2 / 2); k4 = f(m + h * k3)
        m += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"L_Edd(1 Msol) = {l_edd(1):.3e} L_sol (kappa_es = {kappa():.5f} m2/kg)")
    print(f"{'M':>5} {'L [Lsol]':>10} {'Gamma':>7} {'t_vida [Myr]':>13}")
    for m, l in ((10, 5.0e3), (20, 4.0e4), (40, 2.5e5), (80, 8.0e5)):
        gam = l / l_edd(m)
        t = 0.1 * X * m * M_SOL * EPS_C2 / (l * L_SOL) / YR / 1e6
        print(f"{m:5d} {l:10.3g} {gam:7.3f} {t:13.2f}")
        assert 0 < gam < 1
    m0, mdot0, t = 40.0, 1.0e-6, 4.0e6
    k = mdot0 / m0 ** 2
    me, mr = masa_exacta(m0, k, t), masa_rk4(m0, k, t)
    assert abs(mr / me - 1) < 1e-9, "RK4 != solucion exacta"
    print(f"M(0) = {m0} ; M(4 Myr) exacta = {me:.4f} ; RK4 = {mr:.4f} ; perdida = {m0 - me:.3f} Msol")
    print(f"comparacion: tasa constante {mdot0:.0e} Msol/yr -> perdida = {mdot0 * t:.3f} Msol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
