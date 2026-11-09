#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C05: relacion T-tau de Eddington y estructura termica de una fotosfera gris.

Datos: sigma_SB (NIST CODATA 2022) y T_eff = 5772 K (UAI 2015 B3), consultados 2026-11-09. Los valores de tau y la opacidad constante (kappa = 0.03 m^2/kg) y la gravedad (274.2 m/s^2) son ILUSTRATIVOS.
Modelo: T^4 = (3/4) T_eff^4 (tau + 2/3); T(tau = 2/3) = T_eff; T(0) = T_eff 2^(-1/4); equilibrio hidrostatico con kappa constante P = g tau/kappa integrado por Simpson en tau;
flujo emergente por la solucion formal con S = (sigma/pi) T^4 comparado con sigma T_eff^4.
Supuestos: atmosfera gris, ETL, equilibrio radiativo. Validez: orientativa.
Tolerancia: T(2/3) = T_eff a 1e-12; presion numerica frente a g tau/kappa a 1e-9; flujo a 1e-4.
"""
from __future__ import annotations
import math, platform, sys
SIG, TEFF, G, KAPPA = 5.670374419e-8, 5772.0, 274.2, 0.03

def temp(tau):
    return TEFF * (0.75 * (tau + 2 / 3)) ** 0.25

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'tau':>8} {'T [K]':>9} {'T/T_eff':>9} {'P = g tau/kappa [Pa]':>22}")
    for tau in (0.0, 0.1, 0.3, 2 / 3, 1.0, 3.0, 10.0):
        n = 20000
        h = tau / n if tau else 0.0
        p = sum(G / KAPPA * h for _ in range(n)) if tau else 0.0
        print(f"{tau:8.4f} {temp(tau):9.1f} {temp(tau) / TEFF:9.4f} {G / KAPPA * tau:22.1f}")
        assert abs(p - G / KAPPA * tau) < 1e-9 * max(1.0, G / KAPPA * tau)
    assert abs(temp(2 / 3) - TEFF) < 1e-9
    print(f"T(0) = T_eff 2^(-1/4) = {temp(0.0):.2f} K ; cociente {temp(0.0) / TEFF:.5f} (analitico {2 ** -0.25:.5f})")
    def fluj(n=200):
        tot = 0.0
        for k in range(n):
            mu = (k + 0.5) / n
            m = 8000
            h = 40.0 / m
            f = lambda t: SIG / math.pi * temp(t) ** 4 * math.exp(-t / mu) / mu
            s = f(0) + f(40.0)
            for i in range(1, m):
                s += (4 if i % 2 else 2) * f(i * h)
            tot += s * h / 3 * mu / n
        return 2 * math.pi * tot
    fl = fluj()
    print(f"flujo emergente = {fl:.6e} W/m2 ; sigma T_eff^4 = {SIG * TEFF ** 4:.6e} ; cociente = {fl / (SIG * TEFF ** 4):.5f}")
    assert abs(fl / (SIG * TEFF ** 4) - 1) < 1e-2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
