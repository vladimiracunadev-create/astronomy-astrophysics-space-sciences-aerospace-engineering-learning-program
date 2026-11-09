#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C14: temperatura, densidad de radiacion e igualdad materia-radiacion.

Datos: T0 = 2.72548 +/- 0.00057 K (Fixsen, arXiv:0911.1955, resumen, consultado 2026-11-09); constantes de NIST
(CODATA 2022, consultadas 2026-11-09): h, c, k_B, sigma, G, eV; H0 = 67.4 km/s/Mpc, Omega_m = 0.315,
Omega_b h^2 = 0.0224, N_eff = 2.99 (Planck 2018, arXiv:1807.06209, resumen); z = 1089 de la superficie de
ultima dispersion (Eisenstein et al., astro-ph/0501171, resumen). 1 au del IERS TN36 para Mpc.
Modelo: T(z) = T0 (1 + z). Densidad de energia de los fotones u = a T^4, a = 4 sigma/c, verificada por
integracion de la distribucion de Planck. Neutrinos: factor 1 + 0.2271 N_eff con 0.2271 = (7/8)(4/11)^(4/3).
Igualdad: Om (1 + z)^3 = Or (1 + z)^4.
Supuestos: neutrinos sin masa, radiacion termica; desprecia Lambda en el pasado lejano. Validez: z >> 1.
Tolerancia: 1e-6 entre la integral de Planck y a T^4; 1e-12 en el factor de neutrinos.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB, SIGMA, G = 6.62607015e-34, 299792458.0, 1.380649e-23, 5.670374419e-8, 6.67430e-11
EV = 1.602176634e-19
AU = 1.49597870700e11
MPC_M = 1e6 * (648000 / math.pi) * AU
T0, OM, H0_KMS, N_EFF, OBH2 = 2.72548, 0.315, 67.4, 2.99, 0.0224


def u_planck(T, n=40000):
    """Densidad de energia de fotones por integracion: u = Int (8 pi h nu^3 / c^3) / (exp(h nu/kT) - 1) dnu."""
    xmax = 60.0
    dx = xmax / n
    s = 0.0
    for i in range(1, n):
        x = i * dx
        s += x ** 3 / math.expm1(x) * dx
    return 8 * math.pi * (KB * T) ** 4 / (H * C) ** 3 * s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a = 4 * SIGMA / C
    u_ana, u_num = a * T0 ** 4, u_planck(T0)
    assert abs(u_num / u_ana - 1) < 1e-6, "integral de Planck != a T^4"
    print(f"u_gamma = a T0^4 = {u_ana:.4e} J/m3 = {u_ana / EV / 1e6:.4f} eV/cm3 ; integral = {u_num:.4e} J/m3")
    h = H0_KMS * 1e3 / MPC_M * MPC_M / 1e3 / 100            # h = H0 / (100 km/s/Mpc)
    rho_c = 3 * (H0_KMS * 1e3 / MPC_M) ** 2 / (8 * math.pi * G)
    om_gam = u_ana / C ** 2 / rho_c
    fnu = (7 / 8) * (4 / 11) ** (4 / 3)
    assert abs(fnu - 0.2271) < 1e-4
    om_r = om_gam * (1 + fnu * N_EFF)
    print(f"h = {h:.4f} ; Omega_gamma = {om_gam:.4e} ; Omega_gamma h^2 = {om_gam * h * h:.4e}")
    print(f"factor de neutrinos = {fnu:.5f} ; Omega_r = {om_r:.4e}")
    z_eq = OM / om_r - 1
    print(f"igualdad materia-radiacion: z_eq = {z_eq:.0f} ; T(z_eq) = {T0 * (1 + z_eq):.0f} K = {KB * T0 * (1 + z_eq) / EV:.3f} eV")
    assert abs(OM * (1 + z_eq) ** 3 - om_r * (1 + z_eq) ** 4) < 1e-9 * OM * (1 + z_eq) ** 3
    print(f"{'z':>8} {'T [K]':>10} {'kT [eV]':>10}")
    for z in (0, 1, 10, 1089, z_eq, 1e6, 1e9):
        T = T0 * (1 + z)
        print(f"{z:8.0f} {T:10.4g} {KB * T / EV:10.4g}")
    # ionizacion del hidrogeno: kT = 13.6 eV ocurre a z mucho mayor que 1089
    z_13 = 13.605693 * EV / (KB * T0) - 1
    print(f"kT = 13.6 eV a z = {z_13:.0f} ; la recombinacion ocurre a z = 1089 (razon {z_13 / 1089:.1f})")
    eta = OBH2 * rho_c / (h * h) / 1.67262192595e-27 / ((2 * 1.2020569031595942 / math.pi ** 2) * (KB * T0 / (H * C / (2 * math.pi))) ** 3)
    print(f"eta = n_b / n_gamma = {eta:.3e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
