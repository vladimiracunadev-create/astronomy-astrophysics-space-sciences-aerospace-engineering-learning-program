#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C11: Clausius-Clapeyron y regiones de fase de agua y CO2.

Datos PUBLICADOS: SI Brochure 9.ª ed. (T del punto triple del agua = 273,16 K,
valor histórico); NIST Chemistry WebBook: agua, presión del punto triple 0,0061 bar,
ebullición normal 373,17 +- 0,04 K, T_c 647 +- 2 K, P_c 220,64 bar, Delta_vap H
(298 K) = 44,004 kJ/mol DERIVADO de Delta_f H; CO2: punto triple 216,58 K y 5,185 bar,
crítico 304,18 K y 73,80 bar, Delta_sub H = 26,1 kJ/mol (25,2-27,2 según fuente).
NASA NSSDC: Marte 636 Pa y 214 K; Venus 92 bar y 737 K; Tierra 101 400 Pa y 288 K.
Modelo: ln(P/P_tp) = -(Delta H/R)(1/T - 1/T_tp), Delta H constante. Supuestos: gas
ideal, vapor sin volumen del condensado. Dominio de validez: cerca del punto triple;
la hipótesis de Delta H constante falla lejos de él. Tolerancias: ebullición del
agua dentro de 3 K de 373,17 K; sublimación del CO2 a 1 atm dentro de 193-196 K
(intervalo de consistencia que cubre el rango de Delta H publicado).
"""

from __future__ import annotations

import math
import sys

R = 8.314462618
ATM = 101_325.0

AGUA = {"Ttp": 273.16, "Ptp": 610.0, "dHvap": 44_004.0, "Tc": 647.0, "Pc": 220.64e5}
CO2 = {"Ttp": 216.58, "Ptp": 5.185e5, "dHsub": 26_100.0, "Tc": 304.18, "Pc": 73.80e5}


def presion_cc(T: float, Ttp: float, Ptp: float, dH: float) -> float:
    return Ptp * math.exp(-dH / R * (1 / T - 1 / Ttp))


def temperatura_cc(P: float, Ttp: float, Ptp: float, dH: float) -> float:
    return 1 / (1 / Ttp - R * math.log(P / Ptp) / dH)


def region_agua(P: float, T: float) -> str:
    a = AGUA
    if T > a["Tc"]:
        return "vapor o fluido supercrítico (T > T_c)"
    if P < a["Ptp"]:
        return "sólido o vapor (P < P del punto triple: no hay líquido)"
    if T < a["Ttp"]:
        return "sólido (T < T del punto triple)"
    return "líquido" if T < temperatura_cc(P, a["Ttp"], a["Ptp"], a["dHvap"]) else "vapor"


def region_co2(P: float, T: float) -> str:
    c = CO2
    if T > c["Tc"] and P > c["Pc"]:
        return "fluido supercrítico"
    if P < c["Ptp"]:
        t_sub = temperatura_cc(P, c["Ttp"], c["Ptp"], c["dHsub"])
        return "sólido" if T < t_sub else "gas"
    return "sólido, líquido o gas según la T (requiere la curva de vaporización)"


def pruebas() -> None:
    a, c = AGUA, CO2
    # la curva pasa por el punto triple por construcción
    assert abs(presion_cc(a["Ttp"], a["Ttp"], a["Ptp"], a["dHvap"]) - a["Ptp"]) < 1e-9
    # ida y vuelta P -> T -> P
    t = temperatura_cc(5000.0, c["Ttp"], c["Ptp"], c["dHsub"])
    assert abs(presion_cc(t, c["Ttp"], c["Ptp"], c["dHsub"]) - 5000.0) < 1e-6
    # ebullición del agua a 1 atm: predicción frente a 373,17 K (+- 3 K)
    tb = temperatura_cc(ATM, a["Ttp"], a["Ptp"], a["dHvap"])
    assert abs(tb - 373.17) < 3.0, tb
    # sublimación del CO2 a 1 atm: 193-196 K para el rango de Delta H publicado
    for dh in (25_200.0, 26_100.0, 27_200.0):
        assert 193.0 < temperatura_cc(ATM, c["Ttp"], c["Ptp"], dh) < 196.0
    # regiones
    assert region_agua(101_400.0, 288.0) == "líquido"
    assert region_agua(101_400.0, 400.0) == "vapor"
    assert region_agua(636.0, 214.0).startswith("sólido")
    assert region_co2(92e5, 737.0) == "fluido supercrítico"
    assert region_co2(636.0, 214.0) == "gas" and region_co2(636.0, 140.0) == "sólido"


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    a, c = AGUA, CO2
    tb = temperatura_cc(ATM, a["Ttp"], a["Ptp"], a["dHvap"])
    print(f"Agua: ebullición a 1 atm predicha = {tb:.2f} K (NIST: 373.17 +- 0.04 K ; diferencia {tb - 373.17:+.2f} K)")
    for dh in (25_200.0, 26_100.0, 27_200.0):
        print(f"CO2 (Delta_sub H = {dh / 1000:.1f} kJ/mol): sublimación a 1 atm = "
              f"{temperatura_cc(ATM, c['Ttp'], c['Ptp'], dh):.1f} K ; punto de escarcha a 636 Pa = "
              f"{temperatura_cc(636.0, c['Ttp'], c['Ptp'], dh):.1f} K")
    for nombre, P, T in (("Marte (media)", 636.0, 214.0), ("Marte, casquete polar de invierno (ilustrativo)", 636.0, 140.0),
                         ("Tierra", 101_400.0, 288.0), ("Venus", 92e5, 737.0)):
        print(f"{nombre}: agua -> {region_agua(P, T)} ; CO2 -> {region_co2(P, T)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
