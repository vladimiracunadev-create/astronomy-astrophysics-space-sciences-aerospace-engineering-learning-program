#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C01: presion de un gas de electrones degenerado, de lo no relativista a lo ultrarrelativista.

Datos (NIST CODATA 2022, consultados 2026-11-09): h, c, masa del electron, unidad de masa atomica m_u.
Densidades de ejemplo (1e6 a 1e12 kg/m3) y mu_e = 2: valores ILUSTRATIVOS (sinteticos).
Modelo: temperatura cero, estados llenos hasta p_F = m c x. n_e = (8 pi/(3 h^3)) p_F^3. Presion exacta
P = (8 pi/(3 h^3)) Int_0^pF p^3 v dp con v = p c^2/sqrt(p^2 c^2 + m^2 c^4), comparada con la forma cerrada
P = (pi m^4 c^5/(3 h^3)) [x(2x^2 - 3) sqrt(1+x^2) + 3 asinh x]. Limites: x << 1, P = (8 pi m^4 c^5/(15 h^3)) x^5
(no relativista); x >> 1, P = (2 pi m^4 c^5/(3 h^3)) x^4 (ultrarrelativista).
Supuestos: gas ideal de Fermi, sin interacciones, T = 0. Validez: gas completamente ionizado (rho >~ 1e5 kg/m3).
Tolerancia: 1e-8 entre cuadratura y forma cerrada; 1 % en los limites a x = 1e-2 y 1e2 (error ~ x^2 o 1/x^2).
"""
from __future__ import annotations
import math
import platform
import sys

H, C, ME, MU = 6.62607015e-34, 299792458.0, 9.1093837139e-31, 1.66053906892e-27
MC = ME * C


def x_de_rho(rho, mu_e=2.0):
    n = rho / (mu_e * MU)
    return (3 * n * H ** 3 / (8 * math.pi)) ** (1 / 3) / MC, n


def p_cerrada(x):
    return math.pi * ME ** 4 * C ** 5 / (3 * H ** 3) * (x * (2 * x * x - 3) * math.sqrt(1 + x * x) + 3 * math.asinh(x))


def p_cuadratura(x, n=20000):
    pf = MC * x
    def f(p):
        return p ** 3 * p * C ** 2 / math.sqrt(p * p * C * C + (ME * C * C) ** 2)
    h = pf / n
    s = f(0) + f(pf)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return 8 * math.pi / (3 * H ** 3) * s * h / 3


def p_nr(x):
    return 8 * math.pi * ME ** 4 * C ** 5 / (15 * H ** 3) * x ** 5


def p_ur(x):
    return 2 * math.pi * ME ** 4 * C ** 5 / (3 * H ** 3) * x ** 4


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for x in (0.01, 0.1, 1.0, 10.0, 100.0):
        a, b = p_cerrada(x), p_cuadratura(x)
        assert abs(a / b - 1) < 1e-8, f"x = {x}: cuadratura != forma cerrada"
    assert abs(p_cerrada(0.01) / p_nr(0.01) - 1) < 0.01, "limite no relativista"
    assert abs(p_cerrada(100.0) / p_ur(100.0) - 1) < 0.01, "limite ultrarrelativista"
    n_cruce = 8 * math.pi * MC ** 3 / (3 * H ** 3)
    print(f"n_e en x = 1 : {n_cruce:.3e} m^-3 -> rho (mu_e = 2) = {n_cruce * 2 * MU:.3e} kg/m3")
    print(f"{'rho [kg/m3]':>12} {'x':>10} {'P exacta [Pa]':>15} {'P_NR/P':>9} {'P_UR/P':>9} {'E_F [keV]':>10}")
    for rho in (1e6, 1e8, 1e9, 1e10, 1e12):
        x, n = x_de_rho(rho)
        P = p_cerrada(x)
        ef = (math.sqrt(1 + x * x) - 1) * ME * C ** 2 / 1.602176634e-19 / 1e3
        print(f"{rho:12.0e} {x:10.4f} {P:15.4e} {p_nr(x) / P:9.3f} {p_ur(x) / P:9.3f} {ef:10.2f}")
    print("la presion no depende de la temperatura (T = 0): solo de n_e y de m_e")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
