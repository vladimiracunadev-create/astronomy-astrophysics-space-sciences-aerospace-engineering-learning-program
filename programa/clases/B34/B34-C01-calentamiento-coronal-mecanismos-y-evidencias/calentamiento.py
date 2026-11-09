#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C01: balance de energia de un bucle coronal y calentamiento por eventos pequenos.

Datos: ninguna constante fisica externa. La conductividad de Spitzer (kappa_0 = 1e-11 W m^-1 K^-7/2, ordenes de magnitud, valor estandar NO consultado), la longitud del bucle (1e8 m), la temperatura (2e6 K),
la densidad (1e15 m^-3), la perdida radiativa (Lambda = 3e-23 erg cm^3/s convertida a SI), los indices de la ley de energias (1.8, 2.0, 2.2) y los limites de energia (1e17 y 1e25 J... ver codigo) son ILUSTRATIVOS (sinteticos).
Modelo: (1) flujo conductivo F_c = (2/7) kappa_0 T^(7/2)/L y perdida radiativa por area de base L_r = n^2 Lambda L/2... (comparacion de ordenes de magnitud); (2) energia total liberada por una
poblacion de eventos con dN/dE ~ E^-alpha entre E_min y E_max: Int E dN = A (E_max^(2 - alpha) - E_min^(2 - alpha))/(2 - alpha) frente a la integral numerica; el integrando domina en los eventos pequenos
si alpha > 2 y en los grandes si alpha < 2.
Supuestos: bucle uniforme y estacionario; ley de potencias. Validez: ordenes de magnitud.
Tolerancia: integral numerica frente a la analitica a 1e-6.
"""
from __future__ import annotations
import math, platform, sys
KAPPA0 = 1e-11

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    t, l, n = 2e6, 1e8, 1e15
    fc = 2 / 7 * KAPPA0 * t ** 3.5 / l
    lam = 3e-23 * 1e-7 * 1e-6          # erg cm^3 s^-1 -> J m^3 s^-1
    prad = n * n * lam                 # W/m^3
    lr = prad * l / 2                  # W/m^2 sobre la mitad del bucle (flujo por area de base)
    print(f"T = {t:.1e} K, L = {l:.0e} m, n = {n:.0e} m-3 (ilustrativos)")
    print(f"flujo conductivo F_c = (2/7) kappa_0 T^(7/2)/L = {fc:.1f} W/m2 ; perdida radiativa por area de base = {lr:.1f} W/m2 ; cociente = {fc / lr:.2f}")
    emin, emax = 1e17, 1e25
    print(f"{'alpha':>6} {'energia total analitica [u.a.]':>32} {'numerica':>14} {'fraccion de eventos pequenos (E < 1e21)':>40}")
    for a in (1.8, 2.0, 2.2):
        # dN/dE = E^-a
        if abs(a - 2.0) < 1e-9:
            ana = math.log(emax / emin)
            ana_peq = math.log(1e21 / emin)
        else:
            ana = (emax ** (2 - a) - emin ** (2 - a)) / (2 - a)
            ana_peq = (1e21 ** (2 - a) - emin ** (2 - a)) / (2 - a)
        n_int = 200000
        h = (math.log(emax) - math.log(emin)) / n_int
        num = 0.0
        num_peq = 0.0
        for i in range(n_int):
            le = math.log(emin) + (i + 0.5) * h
            e = math.exp(le)
            f = e ** (1 - a) * e * h        # E dN = E * E^-a * E dlnE
            num += f
            if e < 1e21:
                num_peq += f
        print(f"{a:6.1f} {ana:32.6e} {num:14.6e} {ana_peq / ana:40.4f}")
        assert abs(num / ana - 1) < 1e-6
        assert abs(num_peq / ana_peq - 1) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
