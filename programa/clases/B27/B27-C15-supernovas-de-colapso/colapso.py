#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C15: balance de energia y escala de tiempo del colapso de un nucleo estelar.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Nucleo de 1.4 Msol con radio inicial
1500 km y final 12 km (Riley et al., arXiv:1912.05702, resumen, para el radio final de ~12.7 km de una estrella de neutrones
de 1.34 Msol); la energia cinetica de 1e44 J y la fraccion de neutrinos son ILUSTRATIVAS (sinteticas).
Modelo: esfera uniforme; energia de ligadura gravitatoria E = (3/5) G M^2 / R; caida libre desde el reposo:
t = sqrt(R0^3/(2GM)) [ sqrt(x(1-x)) + arccos sqrt(x) ], x = r/R0; tiempo de caida libre global (pi/2) sqrt(R0^3/(2GM)) =
sqrt(3 pi/(32 G rho)).
Supuestos: esfera uniforme, caida libre sin presion, sin rotacion. Validez: fase inicial del colapso.
Tolerancia: 1e-5 entre la integracion RK4 y el tiempo analitico.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20


def t_analitico(x, gm, r0):
    return math.sqrt(r0 ** 3 / (2 * gm)) * (math.sqrt(x * (1 - x)) + math.acos(math.sqrt(x)))


def t_rk4(x_fin, gm, r0):
    r, v, t = r0, 0.0, 0.0
    f = lambda rr, vv: (vv, -gm / rr ** 2)
    while r > x_fin * r0:
        h = min(0.002 * math.sqrt(r ** 3 / gm), 1e-3)
        h = 0.002 * math.sqrt(r ** 3 / gm)
        k1 = f(r, v)
        k2 = f(r + 0.5 * h * k1[0], v + 0.5 * h * k1[1])
        k3 = f(r + 0.5 * h * k2[0], v + 0.5 * h * k2[1])
        k4 = f(r + h * k3[0], v + h * k3[1])
        rn = r + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        vn = v + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if rn <= x_fin * r0:
            # interpolacion lineal del cruce
            frac = (r - x_fin * r0) / (r - rn)
            return t + frac * h
        r, v, t = rn, vn, t + h
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 1.4 * GM_SOL / G
    gm = G * m
    r0, rf = 1.5e6, 1.2e4
    e_i = 0.6 * G * m * m / r0
    e_f = 0.6 * G * m * m / rf
    de = e_f - e_i
    print(f"M = {m / (GM_SOL / G):.2f} Msol ; E_grav(R=1500 km) = {e_i:.4e} J ; E_grav(R=12 km) = {e_f:.4e} J ; energia liberada = {de:.4e} J")
    print(f"energia liberada = {de / (m * C ** 2) * 100:.2f} % de M c^2 ; en erg: {de * 1e7:.3e}")
    ek = 1e44
    print(f"si la energia cinetica de la explosion es 1e44 J, fraccion = {ek / de * 100:.3f} % ; resto (neutrinos y otros) = {100 - ek / de * 100:.2f} %")
    rho = 3 * m / (4 * math.pi * r0 ** 3)
    t_ff = math.sqrt(3 * math.pi / (32 * G * rho))
    t_ff2 = math.pi / 2 * math.sqrt(r0 ** 3 / (2 * gm))
    assert abs(t_ff / t_ff2 - 1) < 1e-12, "dos formas del tiempo de caida libre"
    print(f"rho_0 = {rho:.4e} kg/m3 ; t_ff = {t_ff * 1e3:.2f} ms")
    print(f"{'x = r/R0':>9} {'t analitico [ms]':>17} {'t RK4 [ms]':>12}")
    for x in (0.5, 0.1, 0.01):
        ta = t_analitico(x, gm, r0)
        tn = t_rk4(x, gm, r0)
        assert abs(tn / ta - 1) < 1e-5, f"RK4 x={x}"
        print(f"{x:9.3f} {ta * 1e3:17.4f} {tn * 1e3:12.4f}")
    print(f"velocidad de caida libre en r = {rf / 1e3:.0f} km: {math.sqrt(2 * gm * (1 / rf - 1 / r0)) / C:.3f} c (newtoniano, no valido cerca de c)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
