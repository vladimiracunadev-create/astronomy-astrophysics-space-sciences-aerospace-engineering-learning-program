#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C16: razon neutron/proton y fraccion primordial de helio-4.

Datos (NIST CODATA 2022, consultados 2026-11-09): masas del neutron, proton y deuteron en u y en kg, u en MeV,
k_B. Densidad bariónica: eta = n_b/n_gamma = 6.1e-10 (calculada en B26-C15 a partir de Planck 2018,
arXiv:1807.06209, resumen). Valores ILUSTRATIVOS (sinteticos): temperatura de congelacion kT = 0.75 MeV,
vida media del neutron 880 s, tiempo del inicio de la nucleosintesis 200 s (no consultados en esta clase).
Modelo: (1) Q = (m_n - m_p) c^2; equilibrio n/p = exp(-Q/kT). (2) Desintegracion libre antes de formar
deuterio: n/p -> n/p * exp(-t/tau_n). (3) Todos los neutrones terminan en He-4: Y_p = 2 (n/p)/(1 + n/p).
(4) Energia de ligadura del deuteron B_d = (m_p + m_n - m_d) c^2 y escala del cuello de botella del
deuterio kT_D ~ B_d / ln(1/eta) (orden de magnitud).
Supuestos: congelacion instantanea, sin otros isotopos. Validez: ilustrativa del orden de magnitud de Y_p.
Tolerancia: 1e-6 entre las dos vias para Q y B_d; Y_p(n/p = 1/7) = 0.25 exacta.
"""
from __future__ import annotations
import math
import platform
import sys

U_MEV = 931.49410372
MN_U, MP_U, MD_U = 1.00866491606, 1.007276466579, 2.013553212544
MN_KG, MP_KG, MD_KG = 1.67492750056e-27, 1.67262192595e-27, 3.3435837768e-27
C, EV = 299792458.0, 1.602176634e-19
ETA = 6.1e-10
TAU_N, T_NUC, KT_FREEZE = 880.0, 200.0, 0.75


def y_p(np_ratio):
    return 2 * np_ratio / (1 + np_ratio)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    q_u = (MN_U - MP_U) * U_MEV
    q_kg = (MN_KG - MP_KG) * C ** 2 / EV / 1e6
    assert abs(q_u / q_kg - 1) < 1e-6, "Q por u y por kg"
    bd_u = (MP_U + MN_U - MD_U) * U_MEV
    bd_kg = (MP_KG + MN_KG - MD_KG) * C ** 2 / EV / 1e6
    assert abs(bd_u / bd_kg - 1) < 1e-6, "B_d por u y por kg"
    print(f"Q = (m_n - m_p) c^2 = {q_u:.5f} MeV (via u) = {q_kg:.5f} MeV (via kg)")
    print(f"B_d = (m_p + m_n - m_d) c^2 = {bd_u:.5f} MeV")
    assert abs(y_p(1 / 7) - 0.25) < 1e-15
    np_eq = math.exp(-q_u / KT_FREEZE)
    np_dec = np_eq * math.exp(-T_NUC / TAU_N)
    print(f"kT_congelacion = {KT_FREEZE} MeV (ilustrativo): n/p = exp(-Q/kT) = {np_eq:.4f} = 1/{1 / np_eq:.2f}")
    print(f"tras desintegrarse {T_NUC:.0f} s (tau = {TAU_N:.0f} s, ilustrativos): n/p = {np_dec:.4f} = 1/{1 / np_dec:.2f}")
    print(f"Y_p = 2 (n/p)/(1 + n/p) = {y_p(np_dec):.4f}  (n/p = 1/7 -> {y_p(1 / 7):.4f})")
    for kt in (0.6, 0.75, 0.9):
        x = math.exp(-q_u / kt) * math.exp(-T_NUC / TAU_N)
        print(f"  kT_cong = {kt:4.2f} MeV -> n/p = {x:.4f} -> Y_p = {y_p(x):.4f}")
    kt_d = bd_u / math.log(1 / ETA)
    print(f"cuello de botella del deuterio: kT ~ B_d / ln(1/eta) = {bd_u:.4f}/{math.log(1 / ETA):.2f} = {kt_d:.4f} MeV "
          f"= {kt_d * 1e6 / 8.617333262e-5:.3e} K (orden de magnitud)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
