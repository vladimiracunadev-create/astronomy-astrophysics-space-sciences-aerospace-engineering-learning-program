#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C16: tamano de una gigante roja y crecimiento del nucleo de helio por quemado en capa.

Datos: sigma (NIST CODATA 2022); GM_sol, R_sol, L_sol, T_ef,sol nominales (IAU 2015 B3);
epsilon c^2 = 6.3978e14 J/kg (B24-C06). La gigante (M, L, T_ef) y X son valores ILUSTRATIVOS
(sinteticos): M = 1.3 Msol, L = 100 Lsol, T_ef = 4500 K, X = 0.7. El periodo de espaciado
de modos de gravedad medido en gigantes por Kepler (50 s frente a 100-300 s) se cita en la
clase (Bedding et al. 2011, resumen), no se calcula aqui.
Modelo: R = sqrt(L/(4 pi sigma)) / T^2; g = GM/R^2; densidad media; crecimiento del nucleo
dMc/dt = L / (X epsilon c^2) con L constante (quemado de H en capa), integrado con RK4 y
comparado con la solucion lineal exacta.
Supuestos: L constante durante el intervalo; toda la luminosidad viene de la capa. Validez:
orden de magnitud. Tolerancia: 1e-12 en el viaje de ida y vuelta L -> R -> L; 1e-9 en RK4.
"""
from __future__ import annotations
import math
import platform
import sys

SIGMA = 5.670374419e-8
G = 6.67430e-11
GM_SOL, R_SOL, L_SOL, T_SOL = 1.3271244e20, 6.957e8, 3.828e26, 5772.0
M_SOL = GM_SOL / G
EPS_C2 = 6.3978e14
YR = 365.25 * 86400.0


def radio(L, T):
    return math.sqrt(L / (4 * math.pi * SIGMA)) / T ** 2


def nucleo_rk4(m0, L, X, t, n=500):
    f = lambda m: L / (X * EPS_C2)
    h, m = t / n, m0
    for _ in range(n):
        k1 = f(m); k2 = f(m + h * k1 / 2); k3 = f(m + h * k2 / 2); k4 = f(m + h * k3)
        m += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    M, L, T, X = 1.3 * M_SOL, 100 * L_SOL, 4500.0, 0.7
    R = radio(L, T)
    assert abs(4 * math.pi * R * R * SIGMA * T ** 4 / L - 1) < 1e-12, "ida y vuelta L-R-L"
    g = G * M / R ** 2
    g_sol = GM_SOL / R_SOL ** 2
    rho = M / (4 / 3 * math.pi * R ** 3)
    rho_sol = M_SOL / (4 / 3 * math.pi * R_SOL ** 3)
    print(f"R = {R / R_SOL:.2f} R_sol ; g = {g:.2f} m/s2 (Sol {g_sol:.1f}) ; log g(cgs) = {math.log10(g * 100):.2f}")
    print(f"densidad media = {rho:.3f} kg/m3 = {rho / rho_sol:.2e} rho_sol")
    t_dyn = math.sqrt(R ** 3 / (G * M)) / 86400.0
    print(f"tiempo dinamico = {t_dyn:.2f} d")
    dmc_dt = L / (X * EPS_C2)
    t = 7.0e7 * YR
    mc = nucleo_rk4(0.0, L, X, t)
    assert abs(mc / (dmc_dt * t) - 1) < 1e-9, "RK4 != solucion lineal"
    print(f"dMc/dt = {dmc_dt:.3e} kg/s = {dmc_dt * YR / M_SOL:.2e} Msol/yr")
    print(f"crecimiento del nucleo en 70 Myr = {mc / M_SOL:.3f} Msol")
    print(f"tiempo para anadir 0.1 Msol = {0.1 * M_SOL / dmc_dt / YR / 1e6:.0f} Myr")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
