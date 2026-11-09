#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C06: balance energetico de la fusion 4 p -> He-4.

Datos (NIST CODATA 2022, consultados 2026-11-09): masa del proton y de la particula alfa en kg
y en u; masa del electron; c; equivalente en MeV de la unidad de masa atomica. GM_sol, L_sol
nominales (IAU 2015 B3). Fraccion de nucleo que se quema y fraccion de hidrogeno: valores
ILUSTRATIVOS (estimados).
Modelo: Q = 4 m_p + 4 m_e - (m_alpha + 2 m_e) en energia (atomos de H -> atomo de He-4):
incluye la aniquilacion de los dos positrones y NO descuenta los neutrinos. Tiempo nuclear
t = f X M epsilon c^2 / L.
Supuestos: luminosidad constante; todo el Q sale como luz (los neutrinos se llevan una fraccion
pequeña no calculada aqui). Validez: orden de magnitud. Tolerancia: 1e-9 entre la via en kg y la via en u.
"""
from __future__ import annotations
import platform
import sys

C = 299792458.0
MP_KG, MA_KG, ME_KG = 1.67262192595e-27, 6.6446573450e-27, 9.1093837139e-31
MP_U, MA_U, ME_U = 1.007276466579, 4.001506179129, 5.485799090e-4
U_MEV = 931.49410372
EV = 1.602176634e-19
GM_SOL, L_SOL, G = 1.3271244e20, 3.828e26, 6.67430e-11
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0


def q_kg_mev():
    dm = 4 * MP_KG + 4 * ME_KG - (MA_KG + 2 * ME_KG)
    return dm * C * C / EV / 1e6, dm / (4 * MP_KG + 4 * ME_KG)


def q_u_mev():
    dm = 4 * MP_U + 4 * ME_U - (MA_U + 2 * ME_U)
    return dm * U_MEV, dm / (4 * MP_U + 4 * ME_U)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    qk, ek = q_kg_mev()
    qu, eu = q_u_mev()
    assert abs(qk / qu - 1) < 1e-6, "Q por kg y por u no coinciden"
    assert abs(ek / eu - 1) < 1e-6
    eps_c2 = ek * C * C
    mdot = L_SOL / eps_c2
    f, X = 0.1, 0.7
    t_nuc = f * X * M_SOL * eps_c2 / L_SOL
    print(f"Q (via kg) = {qk:.4f} MeV ; Q (via u) = {qu:.4f} MeV")
    print(f"fraccion de masa convertida epsilon = {ek:.5f}")
    print(f"energia por kg de H = {eps_c2:.4e} J/kg")
    print(f"H consumido por el Sol = {mdot:.3e} kg/s")
    print(f"t_nuc (f={f}, X={X}) = {t_nuc / YR / 1e9:.2f} Gyr ; con f=0.1 y X=1: {f * M_SOL * eps_c2 / L_SOL / YR / 1e9:.2f} Gyr")
    assert 0.0070 < ek < 0.0073
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
