#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C05: energia y momento relativistas, limite clasico y balances de masa-energia.

Datos (NIST CODATA 2022, consultados 2026-11-09): c exacta, masa del proton y del electron (kg y u),
equivalente en MeV de la u, electronvoltio. GM_sol nominal (IAU 2015 B3, arXiv:1510.07674) y G (NIST)
para la masa solar. Masas de GW150914 (36 + 29 -> 62 Msol y energia radiada 3.0 Msol c^2, LIGO-Virgo,
arXiv:1602.03837, resumen, consultado 2026-11-09). Velocidades del proton: SINTETICAS.
Modelo: E = gamma m c^2, p = gamma m v, E^2 = (p c)^2 + (m c^2)^2; energia cinetica K = (gamma-1) m c^2.
Aniquilacion e+ e- en reposo: dos fotones de energia m_e c^2 cada uno.
Supuestos: particulas libres, sin campos. Validez: cualquier velocidad < c.
Tolerancia: 1e-12 relativa en la relacion energia-momento; 1e-9 entre las dos vias del electron.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
EV = 1.602176634e-19
U_MEV = 931.49410372
MP_U, ME_U = 1.007276466579, 5.485799090e-4
ME_KG = 9.1093837139e-31
G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
MP_MEV = MP_U * U_MEV


def gamma(beta):
    return 1 / math.sqrt(1 - beta * beta)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"m_p c^2 = {MP_MEV:.3f} MeV")
    print(f"{'beta':>10} {'gamma':>11} {'K [MeV]':>13} {'K clasica':>13} {'K/Kcl - 1':>11}")
    for beta in (1e-3, 0.1, 0.5, 0.9, 0.99999):
        g = gamma(beta)
        E = g * MP_MEV
        pc = g * beta * MP_MEV
        assert abs((E * E - pc * pc) / MP_MEV ** 2 - 1) < 1e-9, "E^2 - p^2 c^2 != m^2 c^4"
        K, Kcl = (g - 1) * MP_MEV, 0.5 * MP_MEV * beta ** 2
        print(f"{beta:10.5f} {g:11.5f} {K:13.6g} {Kcl:13.6g} {K / Kcl - 1:11.3e}")
    # el limite clasico: K/Kcl - 1 ~ 3 beta^2 / 4
    b = 1e-3
    assert abs(((gamma(b) - 1) / (0.5 * b * b) - 1) / (0.75 * b * b) - 1) < 1e-2
    # aniquilacion e+ e-: cada foton lleva m_e c^2
    e_gamma_kg = ME_KG * C ** 2 / EV / 1e6
    e_gamma_u = ME_U * U_MEV
    assert abs(e_gamma_kg / e_gamma_u - 1) < 1e-9, "dos vias del electron"
    print(f"aniquilacion e+ e-: cada foton {e_gamma_kg:.6f} MeV (via kg) = {e_gamma_u:.6f} MeV (via u)")
    # GW150914
    m_ini, m_fin, e_rad = 36.0 + 29.0, 62.0, 3.0
    assert abs((m_ini - m_fin) - e_rad) < 1e-9, "balance de masas GW150914"
    E_J = e_rad * M_SOL * C ** 2
    print(f"GW150914: 36 + 29 - 62 = {m_ini - m_fin:.0f} Msol ; energia radiada = {E_J:.3e} J ; "
          f"fraccion de la masa inicial = {e_rad / m_ini:.4f}")
    print(f"1 Msol c^2 = {M_SOL * C ** 2:.4e} J")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
