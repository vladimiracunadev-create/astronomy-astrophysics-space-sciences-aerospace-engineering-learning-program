#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C05: inversion de un cociente de lineas sensible a la densidad y propagacion del error.

Datos: ninguna constante fisica. El cociente R(n) = R_bajo + (R_alto - R_bajo) n/(n + n_c) (modelo de dos niveles de juguete) con R_bajo = 0.2, R_alto = 1.2 y n_c = 1e15 m^-3, el error relativo
del cociente (5 %), las densidades verdaderas y la semilla fija son ILUSTRATIVOS (sinteticos); no corresponden a ningun par de lineas real.
Modelo: inversion analitica n = n_c (R - R_bajo)/(R_alto - R); propagacion lineal sigma_n = |dn/dR| sigma_R con dn/dR = n_c (R_alto - R_bajo)/(R_alto - R)^2; Monte Carlo (20 000) del cociente
con error gaussiano y reinversion; sensibilidad que se pierde cerca de la saturacion R -> R_alto.
Supuestos: cociente de prueba monotono; errores gaussianos independientes. Validez: ilustrativa.
Tolerancia: sigma_n de Monte Carlo frente a la lineal dentro del 5 % para n/n_c entre 0.3 y 2.
"""
from __future__ import annotations
import math, platform, random, sys
RB, RA, NC = 0.2, 1.2, 1e15

def ratio(n):
    return RB + (RA - RB) * n / (n + NC)

def inv(r):
    return NC * (r - RB) / (RA - r)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    print(f"{'n verdadera [m-3]':>18} {'R':>7} {'n invertida':>12} {'sigma_n lineal':>15} {'sigma_n MC':>11} {'sigma_n/n lineal':>17} {'MC/lineal':>10}")
    for x in (0.1, 0.3, 1.0, 3.0, 10.0):
        n = x * NC
        r = ratio(n)
        assert abs(inv(r) / n - 1) < 1e-12
        sr = 0.05 * r
        lin = NC * (RA - RB) / (RA - r) ** 2 * sr
        ests = []
        for _ in range(20000):
            rr = rng.gauss(r, sr)
            if rr < RA - 1e-3:
                ests.append(inv(rr))
        m = sum(ests) / len(ests)
        sd = math.sqrt(sum((e - m) ** 2 for e in ests) / (len(ests) - 1))
        print(f"{n:18.2e} {r:7.4f} {inv(r):12.3e} {lin:15.3e} {sd:11.3e} {lin / n:17.3f} {sd / lin:10.3f}")
        if 0.3 <= x <= 2:
            assert abs(sd / lin - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
