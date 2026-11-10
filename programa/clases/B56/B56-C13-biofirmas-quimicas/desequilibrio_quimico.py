#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C13: desequilibrio quimico CH4 + O2 como energia libre disponible.

Datos: R de NIST (CODATA 2022, consultado 2026-11-09). Composicion de la atmosfera de Marte
(CO2 95,1 %, O2 0,16 %, vapor de agua 210 ppm; presion 636 Pa): hoja de datos de la NASA/NSSDC,
consultada el 2026-11-09. NO CONSULTADOS (ILUSTRATIVOS): Delta G de formacion estandar a
298,15 K en kJ/mol: CH4(g) -50,72; CO2(g) -394,36; H2O(g) -228,57; O2 = 0. Las fracciones
molares del CH4 y la atmosfera "tipo Tierra" son SINTETICAS (un caso de ejercicio, no una
medicion).
Modelo: CH4 + 2 O2 -> CO2 + 2 H2O(g). Delta G = Delta G0 + R T ln Q, con
Q = p(CO2) p(H2O)^2 / (p(CH4) p(O2)^2), presiones en bar. La medida de desequilibrio es -Delta G
(energia por mol de CH4 que se podria liberar al llegar al equilibrio con esos reactivos).
Supuestos: gas ideal, 298,15 K, reaccion unica. Validez: ilustra la idea de desequilibrio, no
mide la biologia de ningun planeta. Tolerancia: Delta G en el equilibrio = 0 a 1e-6 kJ/mol,
trabajando con logaritmos para evitar desbordamientos.
"""
from __future__ import annotations
import math
import platform
import sys

R = 8.314462618
T = 298.15
GF = {"CH4": -50.72, "CO2": -394.36, "H2O": -228.57, "O2": 0.0}
DG0 = GF["CO2"] + 2 * GF["H2O"] - GF["CH4"] - 2 * GF["O2"]


def dg(p):
    lnq = math.log(p["CO2"]) + 2 * math.log(p["H2O"]) - math.log(p["CH4"]) - 2 * math.log(p["O2"])
    return DG0 + R * T * lnq / 1000.0


def log10_ch4_equilibrio(p):
    ln_k = -DG0 * 1000.0 / (R * T)
    lnp = math.log(p["CO2"]) + 2 * math.log(p["H2O"]) - 2 * math.log(p["O2"]) - ln_k
    return lnp / math.log(10)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Delta G0 = {DG0:.2f} kJ/mol ; log10 K = {-DG0 * 1000 / (R * T) / math.log(10):.1f}")
    # Atmosfera sintetica "tipo Tierra" (bar)
    tierra = {"O2": 0.21, "CH4": 1.8e-6, "CO2": 4.2e-4, "H2O": 1.0e-2}
    # Marte: composicion de la hoja NASA; CH4 sintetico (fraccion molar 1e-9)
    p_m = 636.0 / 1e5
    marte = {"O2": 0.0016 * p_m, "CH4": 1e-9 * p_m, "CO2": 0.951 * p_m, "H2O": 210e-6 * p_m}
    for nombre, p in (("sintetica tipo Tierra", tierra), ("Marte (hoja NASA; CH4 sintetico)", marte)):
        print(f"{nombre:34s} Delta G = {dg(p):9.2f} kJ/mol de CH4 ; log10 p(CH4) equilibrio = {log10_ch4_equilibrio(p):8.1f}")
    # Prueba: al fijar CH4 en su valor de equilibrio (1e-146 bar es representable), Delta G = 0
    p_eq = dict(tierra)
    p_eq["CH4"] = 10 ** log10_ch4_equilibrio(tierra)
    dg_eq = dg(p_eq)
    print(f"Delta G con CH4 en equilibrio = {dg_eq:.2e} kJ/mol")
    assert abs(dg_eq) < 1e-6
    # Segunda via: con todas las presiones en 1 bar, Q = 1 y Delta G = Delta G0
    unit = {"O2": 1.0, "CH4": 1.0, "CO2": 1.0, "H2O": 1.0}
    assert abs(dg(unit) - DG0) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
