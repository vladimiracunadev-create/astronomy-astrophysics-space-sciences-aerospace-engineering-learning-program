#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C06: distribuciones de Bose-Einstein y Fermi-Dirac, constantes del cuerpo negro y energia de Fermi.

Datos: h, c, k_B, hbar, m_e, e y los valores publicados de la constante de Stefan-Boltzmann (5.670374419e-8 W m^-2 K^-4) y de la constante de desplazamiento de Wien (2.897771955e-3 m K)
(NIST CODATA 2022), consultados 2026-11-09. Las densidades de electrones (8.5e28 m^-3 de tipo metalico y 1e36 m^-3 de tipo enana blanca) son ILUSTRATIVAS (sinteticas).
Modelo: ocupaciones n_BE = 1/(e^x - 1), n_FD = 1/(e^x + 1), n_MB = e^-x con x = (E - mu)/(k T); integral de Planck Int x^3/(e^x - 1) dx = pi^4/15 por Simpson; sigma = 2 pi^5 k^4/(15 h^3 c^2)
y b = h c/(x_W k) con x_W raiz de x = 5 (1 - e^-x) por biseccion; energia de Fermi E_F = hbar^2 (3 pi^2 n)^(2/3)/(2 m) y su cociente con m c^2 (parametro relativista p_F/(m c)).
Supuestos: gas ideal de fermiones o bosones, T = 0 para la energia de Fermi. Validez: ver cada caso.
Tolerancia: Planck a 1e-9; sigma y b frente a NIST a 1e-8; FD(x) + FD(-x) = 1 a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB, E, ME = 6.62607015e-34, 299792458.0, 1.380649e-23, 1.602176634e-19, 9.1093837139e-31
HBAR = H / (2 * math.pi)
SIGMA_NIST, WIEN_NIST = 5.670374419e-8, 2.897771955e-3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'x':>6} {'BE':>12} {'FD':>12} {'MB':>12} {'BE/MB':>8} {'FD/MB':>8}")
    for x in (0.1, 0.5, 1.0, 3.0, 10.0):
        be, fd, mb = 1 / (math.exp(x) - 1), 1 / (math.exp(x) + 1), math.exp(-x)
        print(f"{x:6.1f} {be:12.6f} {fd:12.6f} {mb:12.6f} {be / mb:8.4f} {fd / mb:8.4f}")
        assert abs(1 / (math.exp(-x) + 1) + fd - 1) < 1e-12
    assert abs(1 / (math.exp(0) + 1) - 0.5) < 1e-15
    # integral de Planck
    n = 200000
    a, b = 1e-9, 60.0
    h = (b - a) / n
    f = lambda x: x ** 3 / math.expm1(x)
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    ip = s * h / 3
    print(f"Int x^3/(e^x - 1) dx = {ip:.9f} ; pi^4/15 = {math.pi ** 4 / 15:.9f}")
    assert abs(ip / (math.pi ** 4 / 15) - 1) < 1e-8
    sigma = 2 * math.pi ** 5 * KB ** 4 / (15 * H ** 3 * C ** 2)
    print(f"sigma = 2 pi^5 k^4/(15 h^3 c^2) = {sigma:.9e} W m^-2 K^-4 ; NIST = {SIGMA_NIST:.9e} ; cociente = {sigma / SIGMA_NIST:.10f}")
    assert abs(sigma / SIGMA_NIST - 1) < 1e-8
    lo, hi = 1.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid - 5 * (1 - math.exp(-mid)) < 0:
            lo = mid
        else:
            hi = mid
    xw = 0.5 * (lo + hi)
    wien = H * C / (xw * KB)
    print(f"x_W = {xw:.9f} ; b = h c/(x_W k) = {wien:.9e} m K ; NIST = {WIEN_NIST:.9e} ; cociente = {wien / WIEN_NIST:.10f}")
    assert abs(wien / WIEN_NIST - 1) < 1e-8
    # energia de Fermi
    print(f"{'n [m-3] (ilustrativo)':>22} {'E_F [eV]':>10} {'T_F [K]':>11} {'p_F/(m c)':>10} {'regimen':>14}")
    for n_e in (8.5e28, 1e36):
        pf = HBAR * (3 * math.pi ** 2 * n_e) ** (1 / 3)
        ef = pf ** 2 / (2 * ME)
        x = pf / (ME * C)
        print(f"{n_e:22.2e} {ef / E:10.4f} {ef / KB:11.4e} {x:10.4f} {('no relativista' if x < 0.3 else 'relativista'):>14}")
    ef_cu = HBAR ** 2 * (3 * math.pi ** 2 * 8.5e28) ** (2 / 3) / (2 * ME) / E
    assert 6.5 < ef_cu < 7.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
