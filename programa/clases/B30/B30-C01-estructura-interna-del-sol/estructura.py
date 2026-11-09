#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C01: modelo politropico del Sol, temperatura central y tiempos caracteristicos.

Datos: G, k_B y la constante de masa atomica u (NIST CODATA 2022); GM_sol, R_sol, L_sol (IAU 2015 B3), consultados 2026-11-09. La masa molecular media del
nucleo (0.6), el indice politropico n = 3 y el camino libre medio de los fotones (1 cm) son ILUSTRATIVOS (no se calculan con un modelo solar real).
Modelo: ecuacion de Lane-Emden theta'' + (2/xi) theta' + theta^n = 0 integrada con RK4 hasta el primer cero xi_1; densidad central rho_c/rho_medio = xi_1/(3|theta'_1|);
temperatura central T_c = (mu u/k_B) 4 pi G rho_c alpha^2/(n + 1) con alpha = R/xi_1; estimacion virial T ~ G M mu u/(k_B R); tiempo de caida libre sqrt(3 pi/(32 G rho));
tiempo de difusion de fotones R^2/(l c); luminosidad especifica L/M.
Supuestos: politropo n = 3, gas ideal, composicion uniforme. Validez: orden de magnitud.
Tolerancia: xi_1 dentro de 1e-3 del valor tabulado 6.8968 (valor estandar, no consultado); densidad media solar por dos vias a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

G, KB, U, C = 6.67430e-11, 1.380649e-23, 1.66053906892e-27, 299792458.0
GM_SOL, R_SOL, L_SOL = 1.3271244e20, 6.957e8, 3.828e26
MU, N_POLI, L_MFP = 0.6, 3.0, 0.01


def lane_emden(n, h=1e-4):
    xi, th, dth = h, 1 - h * h / 6, -h / 3
    f = lambda x, t, d: (d, -t ** n if t > 0 else 0.0 - 2 * d / x)
    while True:
        def der(x, t, d):
            return d, -(max(t, 0.0) ** n) - 2 * d / x
        k1 = der(xi, th, dth)
        k2 = der(xi + h / 2, th + h / 2 * k1[0], dth + h / 2 * k1[1])
        k3 = der(xi + h / 2, th + h / 2 * k2[0], dth + h / 2 * k2[1])
        k4 = der(xi + h, th + h * k3[0], dth + h * k3[1])
        t_n = th + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        d_n = dth + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if t_n <= 0:
            frac = th / (th - t_n)
            return xi + frac * h, dth + frac * (d_n - dth)
        xi, th, dth = xi + h, t_n, d_n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xi1, d1 = lane_emden(N_POLI)
    assert abs(xi1 / 6.8968 - 1) < 1e-3, "primer cero de Lane-Emden"
    cociente = xi1 / (3 * abs(d1))
    print(f"politropo n = 3: xi_1 = {xi1:.4f} ; -theta'(xi_1) = {-d1:.5f} ; -xi_1^2 theta' = {xi1 ** 2 * -d1:.4f} ; rho_c/rho_medio = {cociente:.2f}")
    m = GM_SOL / G
    rho_m = 3 * m / (4 * math.pi * R_SOL ** 3)
    rho_m2 = 3 * GM_SOL / (4 * math.pi * G * R_SOL ** 3)
    assert abs(rho_m / rho_m2 - 1) < 1e-12
    rho_c = rho_m * cociente
    alpha = R_SOL / xi1
    t_c = MU * U / KB * 4 * math.pi * G * rho_c * alpha ** 2 / (N_POLI + 1)
    t_vir = G * m * MU * U / (KB * R_SOL)
    print(f"masa solar = {m:.4e} kg ; densidad media = {rho_m:.2f} kg/m3 ; densidad central (politropo) = {rho_c:.4e} kg/m3 = {rho_c / 1000:.1f} g/cc")
    print(f"temperatura central (politropo, mu = {MU}) = {t_c:.4e} K ; estimacion virial G M mu u/(k R) = {t_vir:.4e} K ; cociente = {t_c / t_vir:.3f}")
    t_ff = math.sqrt(3 * math.pi / (32 * G * rho_m))
    t_dif = R_SOL ** 2 / (L_MFP * C)
    print(f"tiempo de caida libre = {t_ff:.1f} s = {t_ff / 60:.1f} min ; tiempo de difusion de fotones (l = 1 cm) = {t_dif:.3e} s = {t_dif / 3.15576e7:.3e} anios")
    print(f"luminosidad especifica L/M = {L_SOL / m:.3e} W/kg ; energia de ligadura gravitatoria ~ (3/2)GM^2/R: tiempo de Kelvin-Helmholtz = {1.5 * G * m ** 2 / R_SOL / L_SOL / 3.15576e7:.3e} anios (con coeficiente 3/2)")
    # presion central del politropo
    k_const = 4 * math.pi * G * alpha ** 2 * rho_c ** (1 - 1 / N_POLI) / (N_POLI + 1)
    p_c = k_const * rho_c ** (1 + 1 / N_POLI)
    print(f"presion central (politropo) = {p_c:.4e} Pa ; comprobacion gas ideal: rho_c k T_c/(mu u) = {rho_c * KB * t_c / (MU * U):.4e} Pa")
    assert abs(p_c / (rho_c * KB * t_c / (MU * U)) - 1) < 1e-9, "presion central por dos vias"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
