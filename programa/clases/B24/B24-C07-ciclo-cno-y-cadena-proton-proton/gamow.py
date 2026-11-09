#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C07: pico de Gamow y sensibilidad de la tasa de fusion a la temperatura.

Datos (NIST CODATA 2022, consultados 2026-11-09): constante de estructura fina, k_B, eV,
masa del proton en u, equivalente en MeV de la u. Temperatura central del Sol segun el modelo
de la NASA Sun Fact Sheet (2024-05-09): 1.571e7 K (valor de MODELO). La masa del nucleo de
N-14 se aproxima por 14 u (aproximacion declarada).
Modelo: tasa <sigma v> ~ T^(-3/2) Int S exp(-E/kT - sqrt(E_G/E)) dE con factor S constante;
E_G = 2 mu c^2 (pi alpha Z1 Z2)^2; pico E0 = (E_G (kT)^2 / 4)^(1/3); aproximacion del
punto de silla: <sigma v> ~ tau^2 exp(-tau), tau = 3 E0/kT, de modo que el exponente
de temperatura es nu = (tau - 2)/3.
Supuestos: factor astrofisico S constante, sin apantallamiento ni resonancias; reacciones
p+p y p+N14. Validez: orden de magnitud del exponente. Tolerancia: 1e-6 en el pico; 3 % en nu.
"""
from __future__ import annotations
import math
import platform
import sys

ALPHA = 1 / 137.035999177
KB_EV = 1.380649e-23 / 1.602176634e-19   # eV/K
U_MEV = 931.49410372
MP_MEV = 1.007276466579 * U_MEV


def e_gamow_mev(z1, z2, a1, a2):
    m1, m2 = (MP_MEV if a1 == 1 else a1 * U_MEV), (MP_MEV if a2 == 1 else a2 * U_MEV)
    mu = m1 * m2 / (m1 + m2)
    return 2 * mu * (math.pi * ALPHA * z1 * z2) ** 2


def pico_mev(eg, kt):
    return (eg * kt * kt / 4) ** (1 / 3)


def integrando(e, eg, kt):
    return math.exp(-e / kt - math.sqrt(eg / e))


def maximo_numerico(eg, kt):
    a, b = 1e-6 * kt, 60 * kt
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if integrando(c, eg, kt) > integrando(d, eg, kt):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return (a + b) / 2


def tasa(eg, T, n=20000):
    kt = KB_EV * T * 1e-6
    lo, hi = 1e-4 * kt, 80 * kt
    h = (hi - lo) / n
    s = integrando(lo, eg, kt) + integrando(hi, eg, kt)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * integrando(lo + i * h, eg, kt)
    return T ** -1.5 * s * h / 3


def nu_numerico(eg, T):
    d = 1e-3
    return (math.log(tasa(eg, T * (1 + d))) - math.log(tasa(eg, T * (1 - d)))) / (
        math.log(1 + d) - math.log(1 - d))


def nu_silla(eg, T):
    kt = KB_EV * T * 1e-6
    tau = 3 * pico_mev(eg, kt) / kt
    return (tau - 2) / 3, tau


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    T = 1.571e7
    kt = KB_EV * T * 1e-6
    print(f"kT a {T:.3e} K = {kt * 1e3:.3f} keV")
    res = {}
    for nom, z1, z2, a1, a2 in (("p+p", 1, 1, 1, 1), ("p+N14", 1, 7, 1, 14)):
        eg = e_gamow_mev(z1, z2, a1, a2)
        e0 = pico_mev(eg, kt)
        e0n = maximo_numerico(eg, kt)
        assert abs(e0n / e0 - 1) < 1e-6, "pico numerico != analitico"
        nu_s, tau = nu_silla(eg, T)
        nu_n = nu_numerico(eg, T)
        assert abs(nu_n / nu_s - 1) < 0.03, "nu numerico y de silla difieren > 3 %"
        res[nom] = nu_n
        print(f"{nom}: E_G = {eg * 1e3:.1f} keV ; E0 = {e0 * 1e3:.2f} keV (numerico {e0n * 1e3:.2f}) ; "
              f"tau = {tau:.1f} ; nu_silla = {nu_s:.2f} ; nu_numerico = {nu_n:.2f}")
    assert res["p+N14"] > 3 * res["p+p"]
    print(f"cociente de sensibilidades CNO/pp = {res['p+N14'] / res['p+p']:.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
