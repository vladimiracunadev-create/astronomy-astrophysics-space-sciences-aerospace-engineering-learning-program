#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C09: constante de estructura fina, razon entre fuerza electrica y gravitatoria y alcance de Yukawa.

Datos: e, epsilon_0, h, c, G, m_p, m_e, el radio de Bohr (5.291 772 105 44e-11 m), la longitud de onda de Compton (2.426 310 235 38e-12 m), la constante de estructura fina (7.297 352 5643e-3)
y hbar c = 197.326 980 4 MeV fm (NIST CODATA 2022, tabla allascii.txt), consultados 2026-11-09. Las masas del mediador (1 eV, 1 MeV, 100 MeV, 80 GeV) son ILUSTRATIVAS (sinteticas).
Modelo: alpha = e^2/(4 pi epsilon_0 hbar c); razon de fuerzas de Coulomb y de Newton entre dos protones e^2/(4 pi epsilon_0 G m_p^2) (independiente de la distancia); radio de Bohr
a_0 = hbar/(m_e c alpha) y longitud de onda de Compton h/(m_e c); alcance de Yukawa hbar/(m c) = hbar c/(m c^2) del potencial V(r) ~ exp(-r/lambda)/r.
Supuestos: interacciones aisladas, particulas puntuales. Validez: comparaciones de orden de magnitud.
Tolerancia: alpha, a_0 y la longitud de Compton frente a NIST a 1e-8; el cociente Coulomb/Yukawa a r = lambda igual a e a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

E, EPS0, H, C = 1.602176634e-19, 8.8541878188e-12, 6.62607015e-34, 299792458.0
G, MP, ME = 6.67430e-11, 1.67262192595e-27, 9.1093837139e-31
HBAR = H / (2 * math.pi)
ALPHA_NIST, A0_NIST, LC_NIST, HBARC = 7.2973525643e-3, 5.29177210544e-11, 2.42631023538e-12, 197.3269804


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    alpha = E ** 2 / (4 * math.pi * EPS0 * HBAR * C)
    print(f"alpha = e^2/(4 pi eps0 hbar c) = {alpha:.10e} ; NIST = {ALPHA_NIST:.10e} ; 1/alpha = {1 / alpha:.6f} ; cociente = {alpha / ALPHA_NIST:.10f}")
    assert abs(alpha / ALPHA_NIST - 1) < 1e-8
    a0 = HBAR / (ME * C * alpha)
    lc = H / (ME * C)
    print(f"radio de Bohr hbar/(m_e c alpha) = {a0:.9e} m ; NIST = {A0_NIST:.9e} ; cociente = {a0 / A0_NIST:.9f}")
    print(f"longitud de onda de Compton h/(m_e c) = {lc:.9e} m ; NIST = {LC_NIST:.9e} ; cociente = {lc / LC_NIST:.9f}")
    assert abs(a0 / A0_NIST - 1) < 1e-8 and abs(lc / LC_NIST - 1) < 1e-8
    # razon de fuerzas
    r = E ** 2 / (4 * math.pi * EPS0 * G * MP ** 2)
    re = E ** 2 / (4 * math.pi * EPS0 * G * ME * MP)
    print(f"razon Coulomb/Newton entre dos protones = {r:.4e} ; entre electron y proton = {re:.4e} (independientes de la distancia)")
    for d in (1e-15, 1e-10, 1.0):
        fc = E ** 2 / (4 * math.pi * EPS0 * d ** 2)
        fg = G * MP ** 2 / d ** 2
        assert abs(fc / fg / r - 1) < 1e-12
    # Yukawa
    print(f"{'mc^2':<10} {'alcance hbar c/(m c^2)':>24}")
    for nombre, mc2 in (("1 eV", 1e-6), ("1 MeV", 1.0), ("100 MeV", 100.0), ("80 GeV", 8e4)):
        lam_fm = HBARC / mc2
        print(f"{nombre:<10} {lam_fm:20.4e} fm = {lam_fm * 1e-15:.4e} m")
    lam = 1.0
    print(f"{'r/lambda':>9} {'V_Yukawa/V_Coulomb = exp(-r/lambda)':>38}")
    for x in (0.5, 1.0, 2.0, 5.0, 10.0):
        print(f"{x:9.1f} {math.exp(-x):38.6e}")
    assert abs(math.exp(-1.0) * math.e - 1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
