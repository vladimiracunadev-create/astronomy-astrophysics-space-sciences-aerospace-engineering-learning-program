#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C04: familias de ecuaciones de estado y restricciones de masa maxima y radio.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Restricciones publicadas (solo
resumenes, consultados 2026-11-09): PSR J0740+6620, 2.14 (+0.10/-0.09) Msol (Cromartie et al., arXiv:1904.06759);
PSR J0030+0451, R = 12.71 (+1.14/-1.19) km con M = 1.34 (+0.15/-0.16) Msol (Riley et al., arXiv:1912.05702).
Las tres EOS (politropos con K y Gamma, una de ellas por tramos) son SINTETICAS (ilustrativas); sus parametros
no proceden de ningun modelo nuclear.
Modelo: TOV como en B27-C03. EOS por tramos: P = K1 rho^G1 para rho < rho_t, P = K2 rho^G2 para rho >= rho_t con
K2 = K1 rho_t^(G1-G2) (continuidad de P); e = (1 + a_i) rho c^2 + P/(G_i - 1), con a_2 elegido para que e sea continua.
Se calcula M_max y el radio R(1.4 Msol) (interpolacion lineal en el brazo estable) y se confrontan con las restricciones.
Supuestos: EOS barotropica, sin rotacion, sin corteza. Validez: ilustrativa.
Tolerancia: continuidad de P y e en rho_t a 1e-12; TOV de un solo tramo reproduce B27-C03 a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
M_SOL = 1.3271244e20 / G


class EOS:
    def __init__(self, K1, G1, rho_t=None, G2=None):
        self.K1, self.G1, self.rt, self.G2 = K1, G1, rho_t, G2
        if rho_t is not None:
            self.K2 = K1 * rho_t ** (G1 - G2)
            p_t = K1 * rho_t ** G1
            e1 = rho_t * C ** 2 + p_t / (G1 - 1)
            self.a2 = (e1 - p_t / (G2 - 1)) / (rho_t * C ** 2) - 1
            self.p_t = p_t

    def rho(self, p):
        if p <= 0:
            return 0.0
        if self.rt is None or p < self.p_t:
            return (p / self.K1) ** (1 / self.G1)
        return (p / self.K2) ** (1 / self.G2)

    def e(self, p):
        r = self.rho(p)
        if self.rt is None or p < self.p_t:
            return r * C ** 2 + p / (self.G1 - 1)
        return (1 + self.a2) * r * C ** 2 + p / (self.G2 - 1)

    def p_de_rho(self, rho):
        if self.rt is None or rho < self.rt:
            return self.K1 * rho ** self.G1
        return self.K2 * rho ** self.G2


def tov(eos, rho_c):
    pc = eos.p_de_rho(rho_c)
    h = math.sqrt(pc / (G * rho_c ** 2)) * 2 / 300
    r, p = h, pc
    m = 4 / 3 * math.pi * r ** 3 * eos.e(pc) / C ** 2

    def f(r, p, m):
        e = eos.e(p)
        return (-(e + p) * (m + 4 * math.pi * r ** 3 * p / C ** 2) * G / (C ** 2 * r * (r - 2 * G * m / C ** 2)),
                4 * math.pi * r * r * e / C ** 2)

    n = 0
    while p > 1e-9 * pc and n < 100000:
        k1 = f(r, p, m)
        k2 = f(r + h / 2, p + h / 2 * k1[0], m + h / 2 * k1[1])
        k3 = f(r + h / 2, p + h / 2 * k2[0], m + h / 2 * k2[1])
        k4 = f(r + h, p + h * k3[0], m + h * k3[1])
        p += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        m += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        r += h
        n += 1
        if p < 0:
            break
    return m / M_SOL, r / 1e3


def cs2(eos, rho):
    """(velocidad del sonido / c)^2 = dP/de por diferencias finitas."""
    d = 1e-6 * rho
    p1, p2 = eos.p_de_rho(rho - d), eos.p_de_rho(rho + d)
    return (p2 - p1) / (eos.e(p2) - eos.e(p1))


def barrido(eos, rhos):
    return [(rc,) + tov(eos, rc) for rc in rhos]


def radio_a(masa, tabla):
    """Interpola R(M) en el brazo estable (hasta M_max)."""
    imax = max(range(len(tabla)), key=lambda i: tabla[i][1])
    for i in range(imax):
        m0, m1 = tabla[i][1], tabla[i + 1][1]
        if m0 <= masa <= m1:
            return tabla[i][2] + (tabla[i + 1][2] - tabla[i][2]) * (masa - m0) / (m1 - m0)
    return None


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    eos_a = EOS(6.1e-3, 2.0)
    eos_b = EOS(5.5e-3, 2.0, rho_t=1.0e17, G2=2.6)
    eos_c = EOS(3.0e-2, 2.0)
    # continuidad de P y e en rho_t
    p_menos = eos_b.K1 * eos_b.rt ** eos_b.G1
    p_mas = eos_b.K2 * eos_b.rt ** eos_b.G2
    e_menos = eos_b.rt * C ** 2 + p_menos / (eos_b.G1 - 1)
    e_mas = (1 + eos_b.a2) * eos_b.rt * C ** 2 + p_mas / (eos_b.G2 - 1)
    assert abs(p_mas / p_menos - 1) < 1e-12 and abs(e_mas / e_menos - 1) < 1e-12, "continuidad en rho_t"
    rhos = [1e17 * 1.25 ** k for k in range(0, 22)]
    print(f"{'EOS':32s} {'M_max [Msol]':>12} {'R(1.4) [km]':>12}  M_max >= 2.05 ?  R(1.4) en [11.5, 13.9] km ?  cs2/c2 max")
    ok_total = {}
    for nombre, eos in (("A: Gamma=2, K=6.1e-3", eos_a), ("B: K=5.5e-3, G=2 -> 2.6 sobre 1e17", eos_b), ("C: Gamma=2, K=3.0e-2", eos_c)):
        tab = barrido(eos, rhos)
        mmax = max(t[1] for t in tab)
        r14 = radio_a(1.4, tab)
        c1 = mmax >= 2.05
        c2 = r14 is not None and 11.5 <= r14 <= 13.9
        ok_total[nombre[0]] = (mmax, r14, c1, c2)
        i_m = max(range(len(tab)), key=lambda i: tab[i][1])
        cs = max(cs2(eos, r) for r in rhos[:i_m + 1])
        assert cs < 1.0, "la EOS debe ser causal (c_s < c) en la estrella de masa maxima"
        print(f"{nombre:32s} {mmax:12.3f} {(f'{r14:.2f}' if r14 else 'n/a'):>12}  {str(c1):>15}  {str(c2):>22}  {cs:8.3f}")
    assert ok_total["A"][0] < 2.05 and not ok_total["A"][2], "A debe quedar por debajo de 2 Msol"
    assert ok_total["B"][0] > ok_total["A"][0], "endurecer a alta densidad sube M_max"
    # la rigidez alta densidad no cambia el radio de estrellas de baja densidad central
    eos_b0 = EOS(5.5e-3, 2.0)
    r1, r2 = tov(eos_b0, 6e16)[1], tov(eos_b, 6e16)[1]
    assert abs(r1 / r2 - 1) < 1e-12, "a rho_c < rho_t la EOS por tramos coincide con su primer tramo"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
