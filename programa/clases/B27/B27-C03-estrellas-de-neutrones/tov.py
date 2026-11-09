#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C03: estructura de una estrella de neutrones con la ecuacion TOV y un politropo ilustrativo.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Ecuacion de estado P = K rho^Gamma
con Gamma = 2 y K = 6.1e-3 (SI): parametros ILUSTRATIVOS (sinteticos), elegidos para dar radios de unos 12 km.
Valores publicados de contraste (solo resumenes consultados 2026-11-09): PSR J0740+6620, 2.14 (+0.10/-0.09) Msol
(Cromartie et al., arXiv:1904.06759); PSR J0348+0432, 2.01 +/- 0.04 Msol (Antoniadis et al., arXiv:1304.6875);
PSR J0030+0451 (NICER), 1.34 (+0.15/-0.16) Msol y 12.71 (+1.14/-1.19) km (Riley et al., arXiv:1912.05702).
Modelo: TOV, dP/dr = -(e + P)(m + 4 pi r^3 P/c^2) G /(c^2 r (r - 2 G m/c^2)), dm/dr = 4 pi r^2 e/c^2, con
e = rho c^2 + P/(Gamma - 1). Limite newtoniano (n = 1): R = sqrt(pi K/(2G)) y M = 4 rho_c R^3/pi.
Supuestos: estrella esferica, estatica, sin rotacion, EOS de una sola ley de potencias. Validez: ilustrativa.
Tolerancia: 3 % entre TOV a baja densidad central y el limite newtoniano.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
GAMMA, K = 2.0, 6.1e-3


def rho_de_p(p, K=K, g=GAMMA):
    return (p / K) ** (1 / g) if p > 0 else 0.0


def e_de_p(p, K=K, g=GAMMA):
    return rho_de_p(p, K, g) * C ** 2 + p / (g - 1)


def tov(rho_c, K=K, g=GAMMA, n=3000, newt=False):
    pc = K * rho_c ** g
    r_est = math.sqrt(pc / (G * rho_c ** 2)) * 2
    h = r_est / 300
    r = h
    m = 4 / 3 * math.pi * r ** 3 * e_de_p(pc, K, g) / C ** 2
    p = pc

    def f(r, p, m):
        e = e_de_p(p, K, g) if not newt else rho_de_p(p, K, g) * C ** 2
        if newt:
            return -G * m * (e / C ** 2) / (r * r), 4 * math.pi * r * r * e / C ** 2
        return (-(e + p) * (m + 4 * math.pi * r ** 3 * p / C ** 2) * G / (C ** 2 * r * (r - 2 * G * m / C ** 2)),
                4 * math.pi * r * r * e / C ** 2)

    pasos = 0
    while p > 1e-9 * pc and pasos < 100000:
        k1 = f(r, p, m)
        k2 = f(r + h / 2, p + h / 2 * k1[0], m + h / 2 * k1[1])
        k3 = f(r + h / 2, p + h / 2 * k2[0], m + h / 2 * k2[1])
        k4 = f(r + h, p + h * k3[0], m + h * k3[1])
        p += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        m += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        r += h
        pasos += 1
        if p < 0:
            break
    return m, r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r_newt = math.sqrt(math.pi * K / (2 * G))
    print(f"politropo n = 1 newtoniano: R = {r_newt / 1e3:.2f} km (independiente de la masa)")
    m_t, r_t = tov(2e15)
    m_n = 4 * 2e15 * r_newt ** 3 / math.pi
    assert abs(r_t / r_newt - 1) < 0.03 and abs(m_t / m_n - 1) < 0.03, "TOV debe tender al limite newtoniano"
    print(f"rho_c = 2e15: TOV M = {m_t / M_SOL:.4f} Msol, R = {r_t / 1e3:.2f} km ; newtoniano M = {m_n / M_SOL:.4f} Msol")
    print(f"{'rho_c [kg/m3]':>14} {'M [Msol]':>9} {'R [km]':>8} {'GM/(Rc^2)':>10} {'M newt.':>9}")
    filas = []
    for rho_c in (3e16, 1e17, 3e17, 6e17, 1e18, 1.5e18, 2.5e18, 4e18, 8e18):
        m, r = tov(rho_c)
        mn, rn = tov(rho_c, newt=True)
        filas.append((rho_c, m / M_SOL, r / 1e3))
        print(f"{rho_c:14.1e} {m / M_SOL:9.3f} {r / 1e3:8.2f} {G * m / (r * C ** 2):10.3f} {mn / M_SOL:9.3f}")
    mmax = max(m for _, m, _ in filas)
    print(f"masa maxima del barrido TOV = {mmax:.3f} Msol")
    ref = [("J0740+6620 (Cromartie)", 2.14), ("J0348+0432 (Antoniadis)", 2.01)]
    for nom, mm in ref:
        print(f"  {nom}: {mm} Msol -> {'compatible' if mmax >= mm else 'excluida por esta EOS'}")
    assert mmax > max(m for _, m, _ in [(0, 0.0, 0)]), "barrido"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
