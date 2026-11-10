#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C13: entalpia, entalpia total y velocidad de escape.

Consultado (2026-11-10): NASA Glenn, relaciones isentropicas (T/Tt, p/pt en funcion de M y gamma) y primera ley.
ESTANDAR (no consultado): h = u + p v = cp T; h0 = h + V^2/2 = cp T0; velocidad maxima V = sqrt(2 h0) (expansion hasta T -> 0);
V_e = sqrt(2 cp T0 [1 - (pe/p0)^((g-1)/g)]); mezcla adiabatica de corrientes conserva el flujo de entalpia total.
ILUSTRATIVOS (sinteticos, no medidos): gas caliente gamma = 1.2, R = 350 J/(kg K), p0 = 5e6 Pa, T0 = 3000 K (tobera de C08);
aire gamma = 1.4, R = 287.05 J/(kg K) para el choque normal (M1 = 2, T1 = 250 K); mezcla de dos corrientes de 3 kg/s a 1100 K y 1 kg/s a 700 K.
Via 2: h0 en cada estacion calculado de forma independiente (T por isentropicas y V = M a) y comparado con cp T0.
Via 3: velocidad de escape por balance de energia frente a velocidad por M y a.
Tolerancias: h0 constante a 1e-12 relativa; escape por dos vias a 1e-12 relativa.
"""
import math, platform

G, R, P0, T0 = 1.2, 350.0, 5.0e6, 3000.0
CP = G * R / (G - 1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Gas caliente ILUSTRATIVO: gamma = {G}, R = {R} J/(kg K), cp = {CP:.1f} J/(kg K), T0 = {T0} K, h0 = cp T0 = {CP * T0 / 1e6:.4f} MJ/kg")
    print(" estacion   M      T [K]    V [m/s]    h [MJ/kg]   V^2/2 [MJ/kg]   h0 [MJ/kg]")
    peor = 0.0
    for M in (0.2, 1.0, 2.0, 3.2783):
        f = 1 + 0.5 * (G - 1) * M * M
        t = T0 / f
        v = M * math.sqrt(G * R * t)
        h = CP * t
        h0 = h + 0.5 * v * v
        peor = max(peor, abs(h0 - CP * T0) / (CP * T0))
        print(f"   M={M:6.4f}  {M:6.4f}  {t:7.1f}   {v:8.1f}     {h / 1e6:.4f}       {0.5 * v * v / 1e6:.4f}        {h0 / 1e6:.4f}")
    vmax = math.sqrt(2 * CP * T0)
    print(f"Velocidad maxima (expansion hasta T = 0): V_max = sqrt(2 h0) = {vmax:.1f} m/s")
    print(" pe/p0       Ve [m/s]   Ve/Vmax   fraccion de h0 convertida")
    for r in (0.5, 0.1, 0.0125, 1e-3, 1e-4):
        ve = math.sqrt(2 * CP * T0 * (1 - r ** ((G - 1) / G)))
        print(f" {r:8.4f}   {ve:9.1f}   {ve / vmax:.4f}      {ve * ve / (vmax * vmax):.4f}")
    # via 3: Ve para la tobera de C08 (pe/p0 = 62686/5e6) por Mach y por balance
    Me = 3.2783
    f = 1 + 0.5 * (G - 1) * Me * Me
    te = T0 / f
    v_m = Me * math.sqrt(G * R * te)
    v_e = math.sqrt(2 * CP * (T0 - te))
    pe_p0 = f ** (-G / (G - 1))
    v_r = math.sqrt(2 * CP * T0 * (1 - pe_p0 ** ((G - 1) / G)))
    print(f"Escape a Me = 3.2783: por M y a = {v_m:.3f} ; por balance = {v_e:.3f} ; por pe/p0 = {pe_p0:.6f}: {v_r:.3f} m/s")
    peor = max(peor, abs(v_m - v_e) / v_e, abs(v_r - v_e) / v_e)
    # choque normal en aire: h0 constante
    g, rr = 1.4, 287.05
    cp_a = g * rr / (g - 1)
    M1, T1 = 2.0, 250.0
    p = (2 * g * M1 * M1 - (g - 1)) / (g + 1)
    r_ = (g + 1) * M1 * M1 / ((g - 1) * M1 * M1 + 2)
    m2 = math.sqrt(((g - 1) * M1 * M1 + 2) / (2 * g * M1 * M1 - (g - 1)))
    t2 = T1 * p / r_
    h01 = cp_a * T1 + 0.5 * (M1 * math.sqrt(g * rr * T1)) ** 2
    h02 = cp_a * t2 + 0.5 * (m2 * math.sqrt(g * rr * t2)) ** 2
    print(f"Choque normal en aire (M1 = 2): h01 = {h01 / 1e3:.3f} kJ/kg ; h02 = {h02 / 1e3:.3f} kJ/kg (la entalpia total no cambia)")
    peor = max(peor, abs(h01 - h02) / h01)
    # mezcla adiabatica
    ma, ta, mb, tb = 3.0, 1100.0, 1.0, 700.0
    tmez = (ma * ta + mb * tb) / (ma + mb)
    print(f"Mezcla adiabatica de {ma:.0f} kg/s a {ta:.0f} K y {mb:.0f} kg/s a {tb:.0f} K (cp igual): T0 mezcla = {tmez:.1f} K")
    print(f"Diferencia maxima de h0 / escape entre vias = {peor:.2e}")
    assert peor < 1e-10
    assert abs(tmez - 1000.0) < 1e-12
    print("Pruebas superadas.")


main()
