#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C06: campo critico cuantico, energia ciclotronica y energia magnetica.

Datos (NIST CODATA 2022, consultados 2026-11-09): masa del electron, c, e, hbar, magneton de Bohr en eV/T, mu_0.
Campo de ejemplo de un magnetar (1e11 T = 1e15 G), radio 1e4 m, radio y campo del progenitor (1e7 m, 1e3 T):
valores ILUSTRATIVOS (sinteticos); Kaspi y Beloborodov (arXiv:1703.00068, resumen, consultado 2026-11-09)
describen unos 30 magnetares conocidos con un campo ultrafuerte sin dar cifras en el resumen.
Modelo: campo critico B_Q = m_e^2 c^2/(e hbar). Energia ciclotronica del electron hbar w_c = hbar e B/m_e = 2 mu_B B.
Niveles de Landau relativistas: E_n = m c^2 (sqrt(1 + 2 n B/B_Q) - 1). Energia magnetica U = B^2/(2 mu_0) V.
Flujo congelado: B R^2 = const.
Supuestos: campo uniforme, electron libre en el campo. Validez: ilustrativa.
Tolerancia: 1e-9 entre las dos vias de la energia ciclotronica; 1e-6 entre E_1 y hbar w_c a B = 1e-6 B_Q.
"""
from __future__ import annotations
import math
import platform
import sys

ME, C, E, HBAR = 9.1093837139e-31, 299792458.0, 1.602176634e-19, 1.054571817e-34
MUB_EV = 5.7883817982e-5       # eV/T
MU0 = 1.25663706127e-6


def b_critico():
    return ME ** 2 * C ** 2 / (E * HBAR)


def e_ciclotron_ev(B):
    return HBAR * E * B / ME / E               # hbar w_c / e  en eV


def landau_ev(n, B):
    return ME * C ** 2 / E * (math.sqrt(1 + 2 * n * B / b_critico()) - 1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    bq = b_critico()
    print(f"B_Q = m_e^2 c^2/(e hbar) = {bq:.4e} T = {bq * 1e4:.3e} G")
    for B in (1e8, 1e10, 1e11):
        a, b = e_ciclotron_ev(B), 2 * MUB_EV * B
        assert abs(a / b - 1) < 1e-9, "dos vias de la energia ciclotronica"
        print(f"B = {B:.0e} T ({B / bq:8.3g} B_Q): hbar w_c = {a / 1e3:12.4g} keV (via e hbar B/m = via 2 mu_B B)")
    b_peq = 1e-6 * bq
    assert abs(landau_ev(1, b_peq) / e_ciclotron_ev(b_peq) - 1) < 1e-6, "limite no relativista de Landau"
    print(f"Landau n = 1 a B = B_Q: E_1 = {landau_ev(1, bq) / 1e3:.2f} keV (m c^2 (sqrt(3) - 1) = {0.51099895e6 * (math.sqrt(3) - 1) / 1e3:.2f} keV)")
    B, R = 1e11, 1e4
    U = B ** 2 / (2 * MU0) * 4 / 3 * math.pi * R ** 3
    print(f"energia magnetica (B = 1e11 T, R = 1e4 m, uniforme) = {U:.3e} J")
    Bp, Rp = 1e3, 1e7
    B_ns = Bp * (Rp / R) ** 2
    assert abs(B_ns * R ** 2 / (Bp * Rp ** 2) - 1) < 1e-12
    print(f"flujo congelado: 1e3 T con R = 1e7 m -> {B_ns:.2e} T con R = 1e4 m")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
