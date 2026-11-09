#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C10: perfil de temperatura y luminosidad de un disco de acrecion delgado (tipo Shakura-Sunyaev).

Datos: G, c, sigma_SB, sigma_T, m_p, k_B, h (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09.
Masa 10 Msol, r_in = 6 GM/c^2 y fraccion de Eddington 0.1: valores ILUSTRATIVOS (sinteticos).
Modelo: disco delgado y estacionario, cada cara emite como cuerpo negro: sigma T^4 = 3 G M Mdot/(8 pi r^3) (1 - sqrt(r_in/r)).
Luminosidad total L = Int 2 (2 pi r) sigma T^4 dr = G M Mdot/(2 r_in); temperatura maxima en r = (49/36) r_in.
Eddington: L_Edd = 4 pi G M m_p c/sigma_T; Mdot = L/(eta c^2) con eta = G M/(2 r_in c^2) = 1/12 para r_in = 6 GM/c^2 (pseudo-newtoniano).
Supuestos: disco geometricamente delgado, sin torque en r_in, newtoniano. Validez: orientativa, no relativista.
Tolerancia: 1e-8 entre la integral de Simpson y GMMdot/(2 r_in); 1e-6 en la posicion del maximo.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
SIG, SIG_T, M_P = 5.670374419e-8, 6.6524587051e-29, 1.67262192595e-27
KB, H = 1.380649e-23, 6.62607015e-34
GM_SOL = 1.3271244e20


def temperatura(r, r_in, gm, mdot):
    return (3 * gm * mdot / (8 * math.pi * SIG * r ** 3) * (1 - math.sqrt(r_in / r))) ** 0.25


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 10.0
    gm = m * GM_SOL
    r_g = gm / C ** 2
    r_in = 6 * r_g
    l_edd = 4 * math.pi * gm * M_P * C / SIG_T          # gm = G M
    eta = 1 / 12   # GM/(2 r_in c^2) con r_in = 6 r_g
    l = 0.1 * l_edd
    mdot = l / (eta * C ** 2)
    print(f"L_Edd(10 Msol) = {l_edd:.4e} W ; L = 0.1 L_Edd = {l:.4e} W ; Mdot = {mdot:.4e} kg/s = {mdot * 365.25 * 86400 / (GM_SOL / G):.3e} Msol/anio")
    # luminosidad por cuadratura en x = r_in/r
    f = lambda x: 3 * gm * mdot / (2 * r_in) * (1 - math.sqrt(x))
    l_num = simpson(f, 0.0, 1.0, 100000)
    l_ana = gm * mdot / (2 * r_in)
    # el integrando 1 - sqrt(x) no es suave en 0: Simpson con sustitucion x = s^2
    g = lambda s: 3 * gm * mdot / (2 * r_in) * (1 - s) * 2 * s
    l_num = simpson(g, 0.0, 1.0, 2000)
    assert abs(l_num / l_ana - 1) < 1e-8, "luminosidad del disco"
    print(f"L por cuadratura = {l_num:.4e} W ; G M Mdot/(2 r_in) = {l_ana:.4e} W ; L/(Mdot c^2) = {l_num / (mdot * C ** 2):.6f}")
    # maximo de T
    a, b = 1.0001 * r_in, 3 * r_in
    gr = (math.sqrt(5) - 1) / 2
    c_, d_ = b - gr * (b - a), a + gr * (b - a)
    for _ in range(200):
        if temperatura(c_, r_in, gm, mdot) > temperatura(d_, r_in, gm, mdot):
            b = d_
        else:
            a = c_
        c_, d_ = b - gr * (b - a), a + gr * (b - a)
    r_max = 0.5 * (a + b)
    assert abs(r_max / r_in - 49 / 36) < 1e-6, "posicion del maximo"
    t_max = temperatura(r_max, r_in, gm, mdot)
    print(f"maximo de T en r = {r_max / r_in:.6f} r_in (49/36 = {49 / 36:.6f}) ; T_max = {t_max:.4e} K ; h nu pico ~ {2.82 * KB * t_max / 1.602176634e-19 / 1e3:.2f} keV")
    print(f"{'r/r_in':>8} {'T [K]':>12}")
    for x in (1.2, 49 / 36, 2.0, 5.0, 20.0, 100.0):
        print(f"{x:8.3f} {temperatura(x * r_in, r_in, gm, mdot):12.4e}")
    # ley T ~ r^(-3/4) lejos del borde interno
    t1, t2 = temperatura(1e3 * r_in, r_in, gm, mdot), temperatura(1e4 * r_in, r_in, gm, mdot)
    pend = math.log(t2 / t1) / math.log(10)
    print(f"pendiente de T lejos del borde: {pend:.4f} (esperada -0.75)")
    assert abs(pend + 0.75) < 0.005
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
