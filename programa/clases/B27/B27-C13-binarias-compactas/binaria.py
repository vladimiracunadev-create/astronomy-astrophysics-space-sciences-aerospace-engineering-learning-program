#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C13: perdida de energia por ondas gravitacionales y tiempo hasta la fusion de una binaria compacta.

Datos: G, c (NIST CODATA 2022), GM_sol (IAU 2015 B3), consultados 2026-11-09. PSR J0348+0432: masas 2.01 y 0.172 Msol,
periodo orbital 2.46 h (Antoniadis et al., arXiv:1304.6875, resumen). GW170817: masa total 2.74 Msol, distancia 40 Mpc
(LIGO/Virgo, arXiv:1710.05832, resumen); las masas iguales de 1.37 Msol y las frecuencias de partida son ILUSTRATIVAS.
Modelo (Peters): orbita circular, da/dt = -(64/5) G^3 m1 m2 (m1+m2)/(c^5 a^3) ... con a^3 -> a^3 en el denominador
(da/dt = -K/a^3), T = a^4/(4K) = (5/256) c^5 a^4/(G^3 m1 m2 M), P_GW = (32/5) G^4 m1^2 m2^2 M/(c^5 a^5);
orbita excentrica: Peters (1964), T(a0, e0) por integracion en e con a(e) = a0 g(e)/g(e0).
Supuestos: orden de cuadrupolo, sin efectos post-newtonianos, sin espines. Validez: lejos de la fusion.
Tolerancia: 1e-6 entre RK4 y a(t) analitico; 1e-9 entre las dos formas de T en f_GW; 1e-4 del limite e -> 0.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0


def k_peters(m1, m2):
    return 64 / 5 * G ** 3 * m1 * m2 * (m1 + m2) / C ** 5


def t_fusion(a, m1, m2):
    return a ** 4 / (4 * k_peters(m1, m2))


def p_gw(a, m1, m2):
    return 32 / 5 * G ** 4 * m1 ** 2 * m2 ** 2 * (m1 + m2) / (C ** 5 * a ** 5)


def semieje(m_tot, periodo):
    return (G * m_tot * periodo ** 2 / (4 * math.pi ** 2)) ** (1 / 3)


def rk4_a(n=20000, tau_fin=0.9):
    """y = a/a0 en tau = t/T: y' = -1/(4 y^3)."""
    f = lambda y: -1 / (4 * y ** 3)
    y, h = 1.0, tau_fin / n
    for _ in range(n):
        k1 = f(y); k2 = f(y + 0.5 * h * k1); k3 = f(y + 0.5 * h * k2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def g_e(e):
    return e ** (12 / 19) / (1 - e * e) * (1 + 121 / 304 * e * e) ** (870 / 2299)


def t_excentrica(a0, e0, m1, m2, n=20000):
    """T = Int_0^e0 de/|de/dt| con a(e) = a0 g(e)/g(e0)."""
    k = G ** 3 * m1 * m2 * (m1 + m2) / C ** 5
    def integrando(e):
        if e <= 0:
            return 0.0
        a = a0 * g_e(e) / g_e(e0)
        edot = 304 / 15 * e * k / (a ** 4 * (1 - e * e) ** 2.5) * (1 + 121 / 304 * e * e)
        return 1 / edot
    h = e0 / n
    s = integrando(0) + integrando(e0)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * integrando(i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) integracion numerica de a(t)
    y = rk4_a()
    ana = (1 - 0.9) ** 0.25
    assert abs(y / ana - 1) < 1e-6, "RK4 frente a a(t) = a0 (1 - t/T)^(1/4)"
    print(f"RK4: a(0.9 T)/a0 = {y:.8f} ; analitico (0.1)^(1/4) = {ana:.8f}")
    # 2) PSR J0348+0432 (circular)
    m1, m2, Pb = 2.01 * M_SOL, 0.172 * M_SOL, 2.46 * 3600.0
    a = semieje(m1 + m2, Pb)
    t = t_fusion(a, m1, m2)
    print(f"J0348+0432: a = {a / 1e9:.4f} Gm ({a / 6.957e8:.3f} R_sol) ; P_GW = {p_gw(a, m1, m2):.4e} W ; T_fusion = {t / YR / 1e6:.1f} Ma")
    # 3) GW170817: dos formas de T desde f_GW
    mt = 2.74
    m = mt / 2 * M_SOL
    mc = (m * m) ** 0.6 / (2 * m) ** 0.2
    print(f"GW170817 (masas iguales 1.37 Msol): masa de chirrido = {mc / M_SOL:.4f} Msol")
    for f in (10.0, 30.0, 100.0):
        a_f = (G * 2 * m / (math.pi * f) ** 2) ** (1 / 3)
        t_a = t_fusion(a_f, m, m)
        t_c = 5 / 256 * (math.pi * f) ** (-8 / 3) * (G * mc / C ** 3) ** (-5 / 3)
        assert abs(t_a / t_c - 1) < 1e-9, "T desde a y desde la masa de chirrido"
        print(f"f_GW = {f:5.1f} Hz: a = {a_f / 1e3:8.2f} km ; T_fusion = {t_a:9.3f} s")
    # 4) excentricidad: limite e0 -> 0 y e0 = 0.6
    a0, mm = 1.0e9, 1.4 * M_SOL
    t_c = t_fusion(a0, mm, mm)
    r_peq = t_excentrica(a0, 1e-3, mm, mm) / t_c
    assert abs(r_peq - 1) < 1e-4, "limite circular"
    print(f"T(e0 = 1e-3)/T_circular = {r_peq:.6f}")
    for e0 in (0.1, 0.3, 0.6, 0.9):
        print(f"e0 = {e0:3.1f}: T/T_circular = {t_excentrica(a0, e0, mm, mm) / t_c:8.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
