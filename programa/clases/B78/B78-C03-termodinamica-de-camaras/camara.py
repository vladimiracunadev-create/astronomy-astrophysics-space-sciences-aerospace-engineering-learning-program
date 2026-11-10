#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C03: termodinamica de camara y tobera isentropica.

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K) y g0 = 9.80665 m/s2 (NIST CODATA).
ILUSTRATIVO (sintetico, no de un motor real): temperatura de camara Tc = 3500 K, presion de camara pc = 7.0 MPa,
razon de calores especificos gamma = 1.2, masa molar de los gases M = 22 g/mol (y 10 g/mol en la comparacion).
Modelo: gas ideal calorificamente perfecto, flujo unidimensional isentropico, tobera adaptada (pe = presion de diseno), sin perdidas.
Formula: Ve = sqrt(2 gamma/(gamma-1) (R Tc/M) [1 - (pe/pc)^((gamma-1)/gamma)]).
Segunda via: balance de energia Ve^2/2 = cp (Tc - Te) con Te = Tc (pe/pc)^((gamma-1)/gamma) y cp = gamma R/((gamma-1) M).
Tolerancia: ambas vias coinciden a 1e-12 relativa; velocidad caracteristica c* dentro de 1e-12 frente a su forma alternativa.
"""
from __future__ import annotations
import math, platform

R = 8.314462618  # J/(mol K), NIST
G0 = 9.80665


def ve_formula(tc, pc_pe, gamma, m):
    return math.sqrt(2 * gamma / (gamma - 1) * R * tc / m * (1 - pc_pe ** (-(gamma - 1) / gamma)))


def ve_energia(tc, pc_pe, gamma, m):
    cp = gamma * R / ((gamma - 1) * m)
    te = tc * pc_pe ** (-(gamma - 1) / gamma)
    return math.sqrt(2 * cp * (tc - te)), te


def cstar(tc, gamma, m):
    cap_gamma = math.sqrt(gamma) * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return math.sqrt(R * tc / m) / cap_gamma, cap_gamma


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    tc, pc, gamma, m = 3500.0, 7.0e6, 1.2, 0.022
    print(f"Camara ILUSTRATIVA: Tc = {tc:.0f} K, pc = {pc/1e6:.1f} MPa, gamma = {gamma}, M = {m*1e3:.0f} g/mol")
    print(" pc/pe     Te [K]   Ve [m/s]   Isp_ve [s]  (Ve/g0)")
    for razon in (10.0, 50.0, 100.0, 500.0, 1000.0):
        v1 = ve_formula(tc, razon, gamma, m)
        v2, te = ve_energia(tc, razon, gamma, m)
        assert abs(v1 - v2) / v1 < 1e-12
        print(f" {razon:>6.0f} {te:>9.1f} {v1:>11.1f} {v1/G0:>11.1f}")
    cs, cg = cstar(tc, gamma, m)
    cs2 = math.sqrt(R * tc / m) * (1 / math.sqrt(gamma)) * ((gamma + 1) / 2) ** ((gamma + 1) / (2 * (gamma - 1)))
    assert abs(cs - cs2) / cs < 1e-12
    print(f"Velocidad caracteristica c* = {cs:.1f} m/s (Gamma = {cg:.4f})")
    print("Efecto de la masa molar a pc/pe = 100 y Tc = 3500 K:")
    for mm in (10.0, 16.0, 22.0, 30.0):
        v = ve_formula(tc, 100.0, gamma, mm * 1e-3)
        print(f"  M = {mm:>4.0f} g/mol -> Ve = {v:>7.1f} m/s")
    v10, v40 = ve_formula(tc, 100.0, gamma, 0.010), ve_formula(tc, 100.0, gamma, 0.040)
    assert abs(v10 / v40 - 2.0) < 1e-12  # Ve ~ 1/sqrt(M)
    print(f"Cociente Ve(M=10)/Ve(M=40) = {v10/v40:.6f} (esperado 2 por Ve ~ M^-1/2)")
    print("Efecto de la temperatura de camara (pc/pe = 100, M = 22 g/mol):")
    for t in (2500.0, 3000.0, 3500.0):
        print(f"  Tc = {t:>5.0f} K -> Ve = {ve_formula(t, 100.0, gamma, m):>7.1f} m/s")
    lim = math.sqrt(2 * gamma / (gamma - 1) * R * tc / m)
    print(f"Cota de expansion infinita (pe -> 0): Ve_max = {lim:.1f} m/s ; Ve(pc/pe = 1000) / Ve_max = {ve_formula(tc,1000.0,gamma,m)/lim:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
