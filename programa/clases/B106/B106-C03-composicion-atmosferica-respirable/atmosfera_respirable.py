#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C03: presion parcial inspirada de oxigeno y comparacion de atmosferas de cabina.

Datos CONSULTADOS (OCHMO-TB-003, resumen de NASA-STD-3001 vol. 2 rev. D): PIO2 = (PB - PH2O) x FiO2 con PH2O = 47 mmHg;
normoxia PIO2 = 149 mmHg (intervalo de 145 a 155 mmHg en TB-002); diluyente >= 30 %; presion total entre 34.5 kPa (5.0 psia) y 103 kPa (15.0 psia);
presion mas baja con 100 % de O2: 3.8 psia; con 30 % de diluyente: 5.0 psia; ISS tipica: 14.7 psia con 21 % de O2.
Las atmosferas de 8 psia/32 % y 56.5 kPa/34 % se citan en TB-003 como casos estudiados; aqui se usan SOLO como ejemplos de calculo.
Todo lo demas es aritmetica propia. Sin aleatoriedad ni datos medidos.
Verificacion: reproduce 149.7 mmHg al nivel del mar, 3.8 psia y 5.0 psia.
"""
from __future__ import annotations
import platform
import numpy as np

KPA_MMHG, PSI_KPA, PH2O = 7.50062, 6.894757, 47.0


def pio2(p_kpa, fio2):
    return (p_kpa * KPA_MMHG - PH2O) * fio2


def p_min_kpa(fio2, objetivo=149.0):
    return (PH2O + objetivo / fio2) / KPA_MMHG


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: aritmetica propia con umbrales consultados (OCHMO-TB-002/003); los casos de cabina son ejemplos de calculo, no mediciones")
    R = {}
    R["nivel_mar"] = pio2(101.325, 0.21)
    print(f"Control: nivel del mar (101.325 kPa, 21 % O2): PIO2 = {R['nivel_mar']:.1f} mmHg (consultado: 149.7)")
    assert abs(R["nivel_mar"] - 149.7) < 0.3
    p100 = p_min_kpa(1.0)
    p70 = p_min_kpa(0.70)
    R["p100_psia"], R["p70_psia"], R["p70_kpa"] = p100 / PSI_KPA, p70 / PSI_KPA, p70
    print(f"Presion minima para PIO2 = 149 mmHg: con 100 % de O2 {p100:.2f} kPa = {p100/PSI_KPA:.2f} psia (consultado 3.8); con 70 % de O2 (30 % de diluyente) {p70:.2f} kPa = {p70/PSI_KPA:.2f} psia (consultado 5.0)")
    assert abs(p100 / PSI_KPA - 3.8) < 0.05 and abs(p70 / PSI_KPA - 5.0) < 0.05
    cab = [("ISS tipica (14.7 psia)", 101.325, 0.21), ("Reducida 10.2 psia", 70.3, 0.265), ("8 psia / 32 %", 8.0 * PSI_KPA, 0.32),
           ("56.5 kPa / 34 %", 56.5, 0.34), ("Minima con 30 % de N2", p70, 0.70), ("Pura a 4.3 psia", 4.3 * PSI_KPA, 1.0)]
    print("Atmosfera                  P [kPa]  O2 [%]  diluyente [%]  PIO2 [mmHg]  normoxia  diluyente>=30%  P en 34.5-103 kPa")
    for nombre, p, f in cab:
        pi = pio2(p, f)
        nor = 145 <= pi <= 155
        dil = (1 - f) >= 0.30 - 1e-9
        rng = 34.5 < p <= 103
        print(f"{nombre:26s} {p:7.1f}  {100*f:6.1f}  {100*(1-f):12.1f}  {pi:11.1f}   {'si' if nor else 'no':>7}   {'si' if dil else 'no':>13}   {'si' if rng else 'no':>12}")
    R["pi_8"] = pio2(8.0 * PSI_KPA, 0.32)
    R["pi_565"] = pio2(56.5, 0.34)
    R["pi_43"] = pio2(4.3 * PSI_KPA, 1.0)
    # O2 por m3 de cabina
    print("Masa de O2 por m3 de cabina (gas ideal, 293.15 K): ")
    for nombre, p, f in cab[:4]:
        m = p * 1e3 * f * 0.0320 / (8.314462 * 293.15)
        print(f"   {nombre:26s} {m:6.3f} kg/m3")
    R["m_iss"] = 101325 * 0.21 * 0.032 / (8.314462 * 293.15)
    R["m_8"] = 8.0 * PSI_KPA * 1e3 * 0.32 * 0.032 / (8.314462 * 293.15)
    assert pio2(70.3, 0.265) < 145 < pio2(101.325, 0.21)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
