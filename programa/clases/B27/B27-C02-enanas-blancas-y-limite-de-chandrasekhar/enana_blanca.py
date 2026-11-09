#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C02: relacion masa-radio de enanas blancas con la ecuacion de estado degenerada exacta.

Datos (NIST CODATA 2022 e IAU 2015 B3, consultados 2026-11-09): h, c, m_e, m_u, G; GM_sol (arXiv:1510.07674).
mu_e = 2 (carbono/oxigeno) y las densidades centrales (1e7 a 1e13 kg/m3): valores ILUSTRATIVOS (sinteticos).
Modelo: equilibrio hidrostatico newtoniano dP/dr = -G m rho/r^2, dm/dr = 4 pi r^2 rho, con P(rho) de B27-C01
(gas de Fermi a T = 0) y dP/drho = (m c^2/(3 mu_e m_u)) x^2/sqrt(1+x^2). Integracion con RK4 en r desde el centro
hasta rho = 1e3 kg/m3 (superficie numerica). Limites esperados: x << 1 -> politropo n = 3/2, R ~ M^(-1/3);
rho_c -> infinito -> masa limite del politropo n = 3 (B24-C18), 1.4563 Msol para mu_e = 2.
Supuestos: relatividad general despreciable (r_s/R ~ 1e-3), T = 0, composicion uniforme, sin correcciones de Coulomb.
Validez: 1e7 <= rho_c <= 1e13 kg/m3. Tolerancia: 1e-6 de dP/drho frente a la derivada numerica; pendiente -1/3
con 0.02; M(rho_c = 1e13) a menos de 2.5 % del limite.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, ME, MU, G = 6.62607015e-34, 299792458.0, 9.1093837139e-31, 1.66053906892e-27, 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL, R_SOL = GM_SOL / G, 6.957e8
MC = ME * C
MU_E = 2.0


def x_de_rho(rho):
    n = rho / (MU_E * MU)
    return (3 * n * H ** 3 / (8 * math.pi)) ** (1 / 3) / MC


def presion(x):
    return math.pi * ME ** 4 * C ** 5 / (3 * H ** 3) * (x * (2 * x * x - 3) * math.sqrt(1 + x * x) + 3 * math.asinh(x))


def dp_drho(rho):
    x = x_de_rho(rho)
    return ME * C ** 2 / (3 * MU_E * MU) * x * x / math.sqrt(1 + x * x)


def estructura(rho_c, n=6000, rho_sup=1e3):
    """Devuelve (M, R) integrando con RK4 en r hasta que rho < rho_sup."""
    r_est = math.sqrt(dp_drho(rho_c) / (G * rho_c)) * 3.0        # escala de longitud para el paso
    h = r_est / 400
    r, rho, m = h, rho_c, 4 / 3 * math.pi * h ** 3 * rho_c

    def f(r, rho, m):
        if rho <= 0:
            return 0.0, 0.0
        return -G * m * rho / (r * r * dp_drho(rho)), 4 * math.pi * r * r * rho

    pasos = 0
    while rho > rho_sup and pasos < 200000:
        k1 = f(r, rho, m)
        k2 = f(r + h / 2, rho + h / 2 * k1[0], m + h / 2 * k1[1])
        k3 = f(r + h / 2, rho + h / 2 * k2[0], m + h / 2 * k2[1])
        k4 = f(r + h, rho + h * k3[0], m + h * k3[1])
        rho += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        m += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        r += h
        pasos += 1
        if rho < 0.05 * rho_c:
            h = r_est / 400 * 2        # cerca de la superficie el paso puede ser algo mayor
    return m, r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for rho in (1e8, 1e10, 1e12):
        d = 1e-5 * rho
        num = (presion(x_de_rho(rho + d)) - presion(x_de_rho(rho - d))) / (2 * d)
        assert abs(num / dp_drho(rho) - 1) < 1e-6, "dP/drho"
    print(f"{'rho_c [kg/m3]':>14} {'M [Msol]':>10} {'R [km]':>9} {'R [R_sol]':>10}")
    res = []
    for rho_c in (1e6, 3e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13):
        M, R = estructura(rho_c)
        res.append((rho_c, M / M_SOL, R))
        print(f"{rho_c:14.0e} {M / M_SOL:10.4f} {R / 1e3:9.0f} {R / R_SOL:10.5f}")
    # pendiente en el regimen no relativista
    (_, m1, r1), (_, m2, r2) = res[0], res[1]
    pend = (math.log(r2) - math.log(r1)) / (math.log(m2) - math.log(m1))
    print(f"pendiente d lnR/d lnM (rho_c 1e6 -> 3e6) = {pend:.3f} (politropo n = 3/2: -1/3)")
    assert abs(pend + 1 / 3) < 0.02, "pendiente no relativista"
    masas = [m for _, m, _ in res]
    assert all(b > a for a, b in zip(masas, masas[1:])), "la masa debe crecer con rho_c"
    assert 1.4563 * 0.975 < masas[-1] < 1.4563, "M(1e13) debe acercarse al limite desde abajo"
    print(f"M(rho_c = 1e13) = {masas[-1]:.4f} Msol ; limite del politropo n = 3 = 1.4563 Msol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
