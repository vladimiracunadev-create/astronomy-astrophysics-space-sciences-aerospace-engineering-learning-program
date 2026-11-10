#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C07: energia libre de la metanogenesis con concentraciones variables.

Datos: R y N_A de NIST (CODATA 2022, consultados 2026-11-09). NO CONSULTADOS (tabla de libro
recordada por el autor, ILUSTRATIVOS): Delta G de formacion estandar a 298,15 K en kJ/mol:
CH4(g) -50,72; CO2(g) -394,36; H2O(l) -237,13; H2 = 0. Las presiones parciales, la
temperatura y la potencia de mantenimiento de una celula (1e-19 W) son SINTETICAS e
ILUSTRATIVAS; no describen ningun ambiente real.
Modelo: 4 H2 + CO2 -> CH4 + 2 H2O(l). Delta G = Delta G0 + R T ln Q, con
Q = p(CH4)/(p(H2)^4 p(CO2)) en bar (actividad del agua = 1).
Supuestos: gas ideal, 298,15 K, sin correccion de pH ni de fuerza ionica.
Validez: ilustracion de la dependencia con la concentracion. Tolerancia: la presion de H2
de equilibrio hallada por biseccion coincide con la forma cerrada a 1e-9 relativo.
"""
from __future__ import annotations
import math
import platform
import sys

R = 8.314462618
T = 298.15
GF = {"CH4": -50.72, "CO2": -394.36, "H2O": -237.13, "H2": 0.0}
DG0 = (GF["CH4"] + 2 * GF["H2O"]) - (4 * GF["H2"] + GF["CO2"])  # kJ/mol


def dg(p_h2, p_co2=1e-3, p_ch4=1e-3):
    q = p_ch4 / (p_h2 ** 4 * p_co2)
    return DG0 + R * T * math.log(q) / 1000.0


def p_h2_equilibrio_cerrada(p_co2=1e-3, p_ch4=1e-3):
    k = math.exp(-DG0 * 1000.0 / (R * T))
    return (p_ch4 / (p_co2 * k)) ** 0.25


def p_h2_equilibrio_biseccion(p_co2=1e-3, p_ch4=1e-3):
    lo, hi = 1e-30, 1e5
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if dg(mid, p_co2, p_ch4) > 0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Delta G0 = {DG0:.2f} kJ/mol de CH4 (T = {T} K)")
    pe_c, pe_b = p_h2_equilibrio_cerrada(), p_h2_equilibrio_biseccion()
    assert abs(pe_c / pe_b - 1) < 1e-9
    assert abs(dg(pe_c)) < 1e-6
    print(f"p(H2) de equilibrio = {pe_c:.3e} bar ; Delta G ahi = {dg(pe_c):.2e} kJ/mol")
    for p in (1e-2, 1e-4, 1e-6, 1e-8):
        print(f"p(H2) = {p:7.0e} bar -> Delta G = {dg(p):8.2f} kJ/mol de CH4")
    # Presupuesto por celula: potencia de mantenimiento ilustrativa
    pot = 1e-19  # W
    dg_pt = -dg(1e-4)  # kJ/mol aprovechables en el caso p(H2) = 1e-4 bar
    mol_s = pot / (dg_pt * 1000.0)
    print(f"Con {dg_pt:.1f} kJ/mol, mantener 1e-19 W exige {mol_s * 6.02214076e23:.0f} moleculas de CH4 por segundo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
