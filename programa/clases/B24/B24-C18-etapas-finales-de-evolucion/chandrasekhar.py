#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C18: masa de Chandrasekhar con un politropo n = 3 y presion de Fermi ultrarrelativista.

Datos (NIST CODATA 2022, consultados 2026-11-09): h, c, G, unidad de masa atomica m_u;
GM_sol nominal (IAU 2015 B3). mu_e = 2 (carbono/oxigeno completamente ionizados) es una
hipotesis ILUSTRATIVA. R de una estrella de neutrones = 10 km y M = 1.4 Msol: valores
ILUSTRATIVOS (estimados).
Modelo: gas de electrones degenerado y ultrarrelativista, P = K rho^(4/3) con
K = (hbar c / 4) (3 pi^2)^(1/3) / (mu_e m_u)^(4/3); politropo n = 3:
M = 4 pi (K/(pi G))^(3/2) * omega_3, con omega_3 = -xi^2 theta'(xi_1).
Supuestos: temperatura cero, sin correcciones electrostaticas ni captura de electrones, sin rotacion.
Validez: masa limite aproximada. Tolerancia: 1e-6 del solver frente a n = 1 y a n = 5 analiticos;
1e-6 entre la presion de Fermi por cuadratura y la forma cerrada.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, G = 6.62607015e-34, 299792458.0, 6.67430e-11
HBAR = H / (2 * math.pi)
M_U = 1.66053906892e-27
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G


def lane_emden(n, h=1e-4, xi_max=60.0, hasta=None):
    xi = h
    th = 1 - xi * xi / 6 + n * xi ** 4 / 120
    dth = -xi / 3 + n * xi ** 3 / 30

    def f(x, y, z):
        return z, -2 * z / x - (max(y, 0.0) ** n)

    while xi < xi_max:
        if hasta is not None and xi >= hasta:
            return xi, th, dth
        k1 = f(xi, th, dth)
        k2 = f(xi + h / 2, th + h / 2 * k1[0], dth + h / 2 * k1[1])
        k3 = f(xi + h / 2, th + h / 2 * k2[0], dth + h / 2 * k2[1])
        k4 = f(xi + h, th + h * k3[0], dth + h * k3[1])
        th_n = th + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        dth_n = dth + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if th_n <= 0:
            xi1 = xi + h * th / (th - th_n)
            d1 = dth + (dth_n - dth) * (xi1 - xi) / h
            return xi1, 0.0, d1
        xi, th, dth = xi + h, th_n, dth_n
    return xi, th, dth


def presion_fermi_cerrada(n_e):
    pf = H * (3 * n_e / (8 * math.pi)) ** (1 / 3)
    return 2 * math.pi * C * pf ** 4 / (3 * H ** 3)


def presion_fermi_cuadratura(n_e, n=20000):
    """P = (1/3) Int_0^pF (p v) 2*4 pi p^2 dp / h^3 con v = c (limite ultrarrelativista)."""
    pf = H * (3 * n_e / (8 * math.pi)) ** (1 / 3)
    dp, s = pf / n, 0.0
    for i in range(n):
        p = (i + 0.5) * dp
        s += (p * C) * 8 * math.pi * p * p / H ** 3 * dp / 3
    return s


def k_ultrarrel(mu_e):
    return HBAR * C / 4 * (3 * math.pi ** 2) ** (1 / 3) / (mu_e * M_U) ** (4 / 3)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xi1_1, _, _ = lane_emden(1)
    assert abs(xi1_1 - math.pi) < 1e-6, "n=1: xi1 != pi"
    xi, th, _ = lane_emden(5, hasta=5.0)
    assert abs(th - (1 + xi * xi / 3) ** -0.5) < 1e-8, "n=5: theta != (1+xi^2/3)^(-1/2)"
    xi3, _, d3 = lane_emden(3)
    omega3 = -xi3 ** 2 * d3
    print(f"solver validado: n=1 xi1 = {xi1_1:.6f} ; n=5 theta(5) = {th:.8f}")
    print(f"n=3: xi1 = {xi3:.5f} ; omega_3 = {omega3:.5f}")
    n_e = 1.0e36
    pc, pn = presion_fermi_cerrada(n_e), presion_fermi_cuadratura(n_e)
    assert abs(pn / pc - 1) < 1e-6, "presion de Fermi: cuadratura != forma cerrada"
    rho = n_e * 2 * M_U
    assert abs(pc / (k_ultrarrel(2) * rho ** (4 / 3)) - 1) < 1e-6, "K inconsistente con la presion de Fermi"
    print(f"presion de Fermi (n_e = 1e36 m^-3): cerrada = {pc:.4e} Pa ; cuadratura = {pn:.4e} Pa ; K rho^(4/3) coincide")
    for mu_e in (2.0, 2.15):
        M = 4 * math.pi * (k_ultrarrel(mu_e) / (math.pi * G)) ** 1.5 * omega3
        print(f"mu_e = {mu_e}: M_Ch (politropo n=3) = {M / M_SOL:.4f} Msol")
    e_lig = 0.6 * (1.4 * GM_SOL) ** 2 / G / 1.0e4
    print(f"energia gravitatoria (esfera uniforme, 1.4 Msol, 10 km) = {e_lig:.2e} J = {e_lig / (1.4 * M_SOL * C ** 2):.3f} M c^2")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
