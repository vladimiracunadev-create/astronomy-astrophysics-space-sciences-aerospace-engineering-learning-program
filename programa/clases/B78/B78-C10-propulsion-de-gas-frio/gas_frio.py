#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C10: propulsion de gas frio (expansion isentropica y flujo estrangulado).

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K), g0 = 9.80665 m/s2 (NIST CODATA);
NASA SSVI (Tabla 4-1): gas frio 10 uN-3.6 N y 40-110 s; modulo CPOD hasta 186 N s de impulso total; ArgoMoon con propulsores de 25 mN.
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): masas molares N2 28.014, Ar 39.948, He 4.0026, Xe 131.293 g/mol;
gamma = 1.40 (N2) y 1.667 (monoatomicos); temperatura del gas 300 K; presion de camara 1.0 MPa; razon de presiones 1000 (casi vacio).
Modelo: gas ideal, flujo isentropico unidimensional, tobera adaptada a la razon de presiones, sin capa limite ni perdidas.
Segunda via: Ve a partir del numero de Mach de salida, Me^2 = 2/(gamma-1) [(pc/pe)^((gamma-1)/gamma) - 1] y Te = Tc/(1 + (gamma-1) Me^2/2), Ve = Me sqrt(gamma R Te/M).
Tolerancia: las dos vias coinciden a 1e-12 relativa.
"""
from __future__ import annotations
import math, platform

R, G0 = 8.314462618, 9.80665
GASES = {"N2": (28.014e-3, 1.40), "Ar": (39.948e-3, 1.667), "He": (4.0026e-3, 1.667), "Xe": (131.293e-3, 1.667)}
TC, PC, RZ = 300.0, 1.0e6, 1000.0


def ve_ent(m, g):
    return math.sqrt(2 * g / (g - 1) * R * TC / m * (1 - RZ ** (-(g - 1) / g)))


def ve_mach(m, g):
    me2 = 2 / (g - 1) * (RZ ** ((g - 1) / g) - 1)
    te = TC / (1 + (g - 1) * me2 / 2)
    return math.sqrt(me2) * math.sqrt(g * R * te / m), math.sqrt(me2), te


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Gas frio ILUSTRATIVO: Tc = {TC:.0f} K, pc = {PC/1e6:.1f} MPa, pc/pe = {RZ:.0f} (gases de manual no consultados)")
    print(" gas    M [g/mol]  gamma   Mach_e   Te [K]   Ve [m/s]   Isp [s]  mdot para 25 mN [mg/s]  A* [mm2]")
    for nombre, (m, g) in GASES.items():
        v1 = ve_ent(m, g)
        v2, me, te = ve_mach(m, g)
        assert abs(v1 - v2) / v1 < 1e-12
        md = 25e-3 / v1
        cap = math.sqrt(g) * (2 / (g + 1)) ** ((g + 1) / (2 * (g - 1)))
        astar = md / (PC * cap * math.sqrt(m / (R * TC)))
        print(f" {nombre:<4} {m*1e3:>10.3f} {g:>6.3f} {me:>8.2f} {te:>8.1f} {v1:>10.1f} {v1/G0:>9.1f} {md*1e6:>16.2f} {astar*1e6:>14.4f}")
    print("Impulso total de 186 N s (valor consultado del modulo CPOD) -> masa de gas ideal:")
    for nombre, (m, g) in GASES.items():
        v = ve_ent(m, g)
        print(f"  {nombre:<3}: {186.0/v:>7.3f} kg")
    v_n2 = ve_ent(*GASES["N2"])
    assert 40 <= v_n2 / G0 <= 110
    print(f"Isp del N2 = {v_n2/G0:.1f} s: dentro del rango consultado 40-110 s")
    v_he = ve_ent(*GASES["He"])
    print(f"Isp del He = {v_he/G0:.1f} s: fuera del rango consultado (modelo ideal; ver limites)")
    rho = 20e6 * GASES["N2"][0] / (R * TC)
    print(f"Densidad ideal de N2 a 20 MPa y 300 K = {rho:.0f} kg/m3 (el gas real a esa presion difiere) -> volumen para 186 N s = {186.0/v_n2/rho*1e3:.2f} L")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
