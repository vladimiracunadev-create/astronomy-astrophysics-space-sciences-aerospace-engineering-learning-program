#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C06: Clausius-Clapeyron y decision de fase del agua.

Datos: R de NIST (CODATA 2022, consultado 2026-11-09); presion en Marte 636 Pa y temperatura
media 214 K de la hoja de datos de Marte de la NASA (NSSDC, actualizada 2025-05-19, consultada
el 2026-11-09). NO CONSULTADOS (valores de libro recordados por el autor, ILUSTRATIVOS):
punto triple del agua (273,16 K; 611,657 Pa), calores latentes de vaporizacion (2,50e6 J/kg) y
de sublimacion (2,83e6 J/kg), masa molar 0,018015 kg/mol, punto de ebullicion normal 373,15 K,
y para el metano L = 8,19 kJ/mol con T_eb = 111,7 K. Los otros ambientes son SINTETICOS.
Modelo: ln(P/P0) = -(L M / R)(1/T - 1/T0), calor latente constante. La fase liquida exige
P >= P_triple y T_fusion <= T <= T_ebullicion(P); T_fusion = 273,16 K - 7,4e-8 K/Pa (P - P_triple) para P <= 2e8 Pa
(pendiente de la fusion del hielo Ih, valor de libro NO CONSULTADO, ilustrativo); ignora solutos.
Validez: orden de magnitud; error de unos pocos K lejos del punto triple. Tolerancia: la
integracion RK4 de la ecuacion diferencial coincide con la forma cerrada a 1e-6 relativo; el
punto de ebullicion normal calculado desde el punto triple difiere < 2 % de 373,15 K
(el calor latente no es constante: error esperado de unos 5 K).
"""
from __future__ import annotations
import math
import platform
import sys

R = 8.314462618
M_AGUA = 0.018015
TT, PT = 273.16, 611.657
LV, LS = 2.50e6, 2.83e6


def presion_vap(T, L=LV, T0=TT, P0=PT, M=M_AGUA):
    return P0 * math.exp(-(L * M / R) * (1.0 / T - 1.0 / T0))


def presion_vap_rk4(T, L=LV, T0=TT, P0=PT, M=M_AGUA, n=4000):
    f = lambda t, p: p * L * M / (R * t * t)
    h = (T - T0) / n
    t, p = T0, P0
    for _ in range(n):
        k1 = f(t, p)
        k2 = f(t + h / 2, p + h * k1 / 2)
        k3 = f(t + h / 2, p + h * k2 / 2)
        k4 = f(t + h, p + h * k3)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return p


def t_ebullicion(P, L=LV, T0=TT, P0=PT, M=M_AGUA):
    return 1.0 / (1.0 / T0 - (R / (L * M)) * math.log(P / P0))


def fase(T, P):
    if P < PT:
        return "hielo/vapor (sin liquido)" if T < TT else "vapor"
    tf = TT - 7.4e-8 * (min(P, 2.0e8) - PT)
    if T < tf:
        return "hielo"
    return "liquido" if T <= t_ebullicion(P) else "vapor"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    Tb = t_ebullicion(101325.0)
    print(f"T_ebullicion(101325 Pa) desde el punto triple = {Tb:.1f} K (referencia ilustrativa 373,15 K)")
    assert abs(Tb - 373.15) / 373.15 < 0.02
    p_c, p_n = presion_vap(300.0), presion_vap_rk4(300.0)
    print(f"P_vap(300 K): cerrada = {p_c:.1f} Pa ; RK4 = {p_n:.1f} Pa")
    assert abs(p_c - p_n) / p_c < 1e-6
    casos = [
        ("Marte, media (NASA)", 214.0, 636.0),
        ("Marte, tarde calida sintetica", 290.0, 636.0),
        ("Tierra, nivel del mar sintetico", 288.0, 101325.0),
        ("Fondo de oceano de Europa sintetico", 272.0, 1.0e8),
        ("Titan, superficie sintetica", 94.0, 1.5e5),
    ]
    for nombre, T, P in casos:
        print(f"{nombre:36s} T={T:6.1f} K P={P:11.1f} Pa -> {fase(T, P)}")
    assert fase(214.0, 636.0).startswith("hielo") and fase(288.0, 101325.0) == "liquido"
    # Solvente alternativo: metano con T_eb = 111,7 K a 1 atm
    LM = 8190.0 / 0.01604
    p94 = presion_vap(94.0, L=LM, T0=111.7, P0=101325.0, M=0.01604)
    print(f"Metano: presion de vapor a 94 K ~ {p94 / 1e5:.2f} bar (ilustrativo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
