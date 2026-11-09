#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C02: ecuaciones de Boltzmann y de Saha para el hidrogeno.

Datos: h, k_B, m_e, e y la energia de Rydberg R_inf h c = 13.605 693 122 990 eV (NIST CODATA 2022), consultados 2026-11-09. La densidad total de hidrogeno (1e23 m^-3)
y las temperaturas (4000 a 20000 K) son ILUSTRATIVAS (sinteticas).
Modelo: Boltzmann n_2/n_1 = (g_2/g_1) exp(-DeltaE/kT) con g_n = 2 n^2 y DeltaE = (3/4) Ryd; Saha n_II n_e/n_I = (2 pi m_e k T/h^2)^(3/2) exp(-chi/kT) (2 g_II/g_I = 1 para el hidrogeno);
fraccion ionizada x de x^2/(1 - x) = S(T)/n_tot resuelta de forma cerrada y por biseccion.
Supuestos: ETL, hidrogeno puro, sin descenso del potencial de ionizacion. Validez: orientativa; las desviaciones no ETL no se calculan.
Tolerancia: solucion cerrada y biseccion a 1e-10; limites x -> 0 y x -> 1.
"""
from __future__ import annotations
import math, platform, sys
H, KB, ME, E = 6.62607015e-34, 1.380649e-23, 9.1093837139e-31, 1.602176634e-19
RYD = 13.605693122990

def saha(t, chi=RYD):
    return (2 * math.pi * ME * KB * t / H ** 2) ** 1.5 * math.exp(-chi * E / (KB * t))

def frac(t, ntot=1e23):
    s = saha(t) / ntot
    return (-s + math.sqrt(s * s + 4 * s)) / 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    de = 0.75 * RYD
    print(f"DeltaE(1 -> 2) = {de:.4f} eV ; lambda Lyman alfa = {1239.841984 / de:.2f} nm")
    print(f"{'T [K]':>7} {'n2/n1 (Boltzmann)':>19}")
    for t in (4000, 5772, 10000, 20000):
        print(f"{t:7d} {4 * math.exp(-de * E / (KB * t)):19.4e}")
    print(f"{'T [K]':>7} {'S(T) [m-3]':>12} {'x cerrada':>11} {'x biseccion':>12}")
    for t in (4000, 6000, 8000, 10000, 12000, 20000):
        s = saha(t) / 1e23
        x = frac(t)
        lo, hi = 0.0, 1.0
        for _ in range(200):
            m = 0.5 * (lo + hi)
            if m * m / (1 - m) < s:
                lo = m
            else:
                hi = m
        xb = 0.5 * (lo + hi)
        print(f"{t:7d} {saha(t):12.4e} {x:11.6f} {xb:12.6f}")
        assert abs(x - xb) < 1e-10
    assert frac(3000) < 1e-6 and frac(1e5) > 0.999
    lo, hi = 3000.0, 20000.0
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if frac(m) < 0.5:
            lo = m
        else:
            hi = m
    print(f"temperatura de ionizacion del 50 % con n_tot = 1e23 m-3: {0.5 * (lo + hi):.1f} K")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
