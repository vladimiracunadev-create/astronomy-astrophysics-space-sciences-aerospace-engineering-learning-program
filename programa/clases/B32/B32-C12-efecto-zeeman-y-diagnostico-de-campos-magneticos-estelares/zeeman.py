#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C12: desdoblamiento Zeeman, comparacion con el ancho Doppler y aproximacion de campo debil de la polarizacion circular.

Datos: e, m_e, c, k_B, u y mu_B/h = 1.399 624 491 71e10 Hz/T (NIST CODATA 2022), consultados 2026-11-09. La linea (525 nm, g_eff = 1.5, hierro de 55.845 u como valor estandar NO consultado),
la temperatura (5772 K, UAI 2015 B3), los campos (0.01 a 0.5 T) y el perfil gaussiano de la linea (ancho 4 pm) son ILUSTRATIVOS (sinteticos).
Modelo: Delta lambda_B = g (e/(4 pi m_e)) lambda^2 B/c; comparacion con Delta lambda_D = (lambda/c) sqrt(2kT/m); polarizacion circular V = [I(lambda + Dl) - I(lambda - Dl)]/2 de una linea gaussiana
frente a la aproximacion de campo debil V = Dl dI/dlambda.
Supuestos: triplete normal efectivo, linea gaussiana, perfil I simetrico. Validez: campo debil Delta lambda_B << ancho de la linea.
Tolerancia: coeficiente e/(4 pi m_e) frente a mu_B/h a 1e-9; error de la aproximacion de campo debil menor del 2 % para Delta lambda_B < 0.2 ancho.
"""
from __future__ import annotations
import math, platform, sys
E, ME, C, KB, U, MUB_H = 1.602176634e-19, 9.1093837139e-31, 299792458.0, 1.380649e-23, 1.66053906892e-27, 1.39962449171e10

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    k = E / (4 * math.pi * ME)
    print(f"e/(4 pi m_e) = {k:.6e} Hz/T ; mu_B/h (NIST) = {MUB_H:.6e} Hz/T ; cociente = {k / MUB_H:.10f}")
    assert abs(k / MUB_H - 1) < 1e-9
    lam, g = 525e-9, 1.5
    vth = math.sqrt(2 * KB * 5772 / (55.845 * U))
    dld = lam / C * vth
    print(f"Delta lambda_D (Fe, 5772 K) = {dld * 1e12:.3f} pm")
    print(f"{'B [T]':>7} {'B [G]':>8} {'Delta lambda_B [pm]':>20} {'cociente a Doppler':>19}")
    for b in (0.01, 0.1, 0.3, 0.5):
        dl = g * k * b * lam ** 2 / C
        print(f"{b:7.2f} {b * 1e4:8.0f} {dl * 1e12:20.4f} {dl / dld:19.3f}")
    s = 4e-12
    I = lambda x: 1 - 0.5 * math.exp(-0.5 * (x / s) ** 2)
    dI = lambda x: 0.5 * x / s ** 2 * math.exp(-0.5 * (x / s) ** 2)
    print(f"{'B [T]':>7} {'Dl/ancho':>9} {'V exacta (x = s)':>17} {'V campo debil':>14} {'error':>8}")
    for b in (0.01, 0.05, 0.1, 0.3):
        dl = g * k * b * lam ** 2 / C
        x = s
        ve = 0.5 * (I(x + dl) - I(x - dl))
        vd = dl * dI(x)
        err = abs(ve / vd - 1)
        print(f"{b:7.2f} {dl / s:9.4f} {ve:17.6e} {vd:14.6e} {err * 100:7.3f} %")
        if dl / s < 0.2:
            assert err < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
