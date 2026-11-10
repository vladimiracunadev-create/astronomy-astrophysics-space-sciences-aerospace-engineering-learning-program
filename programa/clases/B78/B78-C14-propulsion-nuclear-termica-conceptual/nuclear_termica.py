#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C14: Isp de un cohete termico (propulsion nuclear termica) como balance de energia y masa molar. Solo conceptual.

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K), g0 = 9.80665 m/s2 (NIST CODATA);
Kirk (2004, NASA/MSFC, NTRS 20050215304): el hidrogeno calentado en el nucleo de un reactor da impulsos especificos por encima de 900 s,
casi el doble que los motores LOX/LH2 del transbordador;
resumenes de resultados de busqueda (fuente secundaria, sin verificar contra el informe primario): pruebas en tierra de NERVA/Rover de 825-850 s.
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): masa molar del H2 = 2.016 g/mol, gamma = 1.40 constante (se ignora la disociacion),
masa molar del metano 16.04 g/mol (comparacion), razon de presiones pc/pe = 1000.
ILUSTRATIVOS: temperaturas del gas 2300-3000 K, potencia termica 1000 MW y eficiencia termica 0.90 para la razon empuje/potencia (SIN diseno de reactor).
Modelo: gas ideal de cp constante, expansion isentropica, calentamiento sin perdidas; F = 2 eta P/Ve.
Segunda via: Isp a partir de ve = sqrt(2 cp (T - Te)) con Te de la isentropica, y el escalamiento Ve ~ sqrt(T/M).
Tolerancia: las dos vias de Ve coinciden a 1e-12; el cociente de escalamiento a 1e-12.
"""
from __future__ import annotations
import math, platform

R, G0 = 8.314462618, 9.80665
GAMMA, RZ = 1.40, 1000.0
M_H2, M_CH4 = 2.016e-3, 16.04e-3


def ve_formula(t, m, g=GAMMA, rz=RZ):
    return math.sqrt(2 * g / (g - 1) * R * t / m * (1 - rz ** (-(g - 1) / g)))


def ve_energia(t, m, g=GAMMA, rz=RZ):
    cp = g * R / ((g - 1) * m)
    te = t * rz ** (-(g - 1) / g)
    return math.sqrt(2 * cp * (t - te))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Cohete termico de H2 (gas ideal, gamma = 1.40, SIN disociacion; ILUSTRATIVO)")
    print("  T [K]    Ve [m/s]   Isp [s]")
    for t in (2300.0, 2700.0, 3000.0):
        v1, v2 = ve_formula(t, M_H2), ve_energia(t, M_H2)
        assert abs(v1 - v2) / v1 < 1e-12
        print(f" {t:>6.0f} {v1:>11.0f} {v1/G0:>9.1f}")
    r = ve_formula(2700.0, M_H2) / ve_formula(2700.0, M_CH4)
    assert abs(r - math.sqrt(M_CH4 / M_H2)) < 1e-12
    print(f"A igual T, Ve(H2)/Ve(CH4) = {r:.4f} = sqrt(M_CH4/M_H2) (la masa molar baja del hidrogeno es la clave)")
    v27 = ve_formula(2700.0, M_H2)
    print(f"Contraste con lo consultado: modelo a 2700 K = {v27/G0:.0f} s ; NERVA (secundaria) 825-850 s ; Kirk (2004): > 900 s")
    print(f"  El modelo cae {'dentro' if 825 <= v27/G0 <= 850 else 'fuera'} del rango 825-850 s: la coincidencia depende de los parametros ilustrativos")
    # Temperatura necesaria para 900 s en este modelo
    v900 = 900.0 * G0
    t900 = v900 ** 2 / (2 * GAMMA / (GAMMA - 1) * R / M_H2 * (1 - RZ ** (-(GAMMA - 1) / GAMMA)))
    print(f"En este modelo, 900 s piden T = {t900:.0f} K (sin disociacion)")
    # Empuje por potencia termica (conceptual)
    p, eta = 1000e6, 0.90
    f = 2 * eta * p / v27
    print(f"Con P = {p/1e6:.0f} MW termicos y eta = {eta} (ILUSTRATIVOS): F = 2 eta P/Ve = {f/1e3:.0f} kN ; mdot = {f/v27:.1f} kg/s")
    # Fraccion de propelente para un delta-v frente a quimico
    print("Fraccion de propelente 1 - exp(-dv/Ve) (comparacion, Ve quimico = 450 s ILUSTRATIVO):")
    for dv in (3000.0, 5000.0, 8000.0):
        fq = 1 - math.exp(-dv / (450.0 * G0))
        fn = 1 - math.exp(-dv / v27)
        print(f"  dv = {dv:>5.0f} m/s -> quimico {fq:.3f} ; termico {fn:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
