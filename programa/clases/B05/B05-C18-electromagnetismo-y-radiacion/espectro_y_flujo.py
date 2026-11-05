#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C18: c a partir de epsilon_0 y mu_0, energía del fotón y flujo de una fuente.

Datos PUBLICADOS: epsilon_0 = 8,854 187 8188e-12 F/m y mu_0 = 1,256 637 061 27e-6 N/A² (CODATA 2022);
c = 299 792 458 m/s y h = 6,626 070 15e-34 J s exactas, e = 1,602 176 634e-19 C (BIPM, SI);
semieje mayor lunar 384 400 km (NASA NSSDC, Moon Fact Sheet); radio ecuatorial 6378,137 km (NASA NSSDC,
Earth Fact Sheet). Potencia de la fuente (10 W), frecuencias y distancias de enlace: SINTÉTICAS.
Modelo: ondas electromagnéticas en el vacío, fuente isótropa, sin absorción. Dominio de validez: espacio
libre. Tolerancias: c calculada con epsilon_0 y mu_0 a 1e-9 relativa (la incertidumbre relativa de ambas es 1,6e-10).
"""
from __future__ import annotations
import math
import sys

EPS0 = 8.8541878188e-12
MU0 = 1.25663706127e-6
C = 299_792_458.0
H = 6.62607015e-34
E = 1.602176634e-19
A_LUNA = 3.844e8
R_T = 6_378_137.0

def energia_foton_ev(f_hz: float) -> float:
    return H * f_hz / E

def flujo_isotropo(P: float, d: float) -> float:
    return P / (4 * math.pi * d * d)

def main() -> int:
    c_calc = 1 / math.sqrt(EPS0 * MU0)
    assert abs(c_calc - C) / C < 1e-9, c_calc
    assert abs(flujo_isotropo(10.0, 2.0) * 4 - flujo_isotropo(10.0, 1.0)) < 1e-15   # ley del cuadrado inverso
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"c calculada = 1/sqrt(eps0 mu0) = {c_calc:.3f} m/s (exacta {C:.0f}); diferencia relativa {abs(c_calc-C)/C:.1e}")
    for nombre, f in (("radio 100 MHz", 100e6), ("microondas 2,2 GHz", 2.2e9), ("infrarrojo 30 THz", 30e12),
                      ("visible 545 THz", 545e12), ("ultravioleta 3e15 Hz", 3e15), ("rayos X 3e18 Hz", 3e18)):
        print(f"  {nombre:22s}: lambda = {C/f:.4e} m; energía del fotón = {energia_foton_ev(f):.4e} eV")
    print(f"Retardo de la luz Tierra–Luna (384 400 km): {A_LUNA/C:.4f} s")
    d = 400e3
    print(f"Retardo satélite (400 km, vertical): {d/C*1e3:.4f} ms")
    for d in (400e3, 4e6, A_LUNA):
        print(f"Fuente isótropa de 10 W a {d/1e3:9.0f} km: flujo = {flujo_isotropo(10.0, d):.4e} W/m²")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
