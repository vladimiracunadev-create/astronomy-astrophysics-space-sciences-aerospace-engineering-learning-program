#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C03: umbral del H-, escalado de Kramers y media de Rosseland.

Datos: h, c, e (NIST CODATA 2022), consultados 2026-11-09. La afinidad electronica del H- (0.7542 eV) es un valor estandar NO consultado; la ley kappa_nu = kappa_0 nu^-3 es ILUSTRATIVA (sintetica).
Modelo: umbral del H-: lambda = hc/chi; escalado de Kramers kappa ~ rho T^-3.5; media de Rosseland para kappa_nu = kappa_0 nu^-3: con x = h nu/(kT), 1/kappa_R es proporcional a
Int x^7 e^x/(e^x - 1)^2 dx / Int x^4 e^x/(e^x - 1)^2 dx = Gamma(8) zeta(7)/(Gamma(5) zeta(4)), calculado por Simpson y por la serie de zeta.
Supuestos: opacidad de prueba, ETL. Validez: ilustrativa.
Tolerancia: integrales numericas frente a las analiticas a 1e-5.
"""
from __future__ import annotations
import math, platform, sys
H, C, E = 6.62607015e-34, 299792458.0, 1.602176634e-19

def zeta(s, n=200000):
    return sum(k ** -s for k in range(1, n)) + n ** (1 - s) / (s - 1)

def simpson(f, a, b, n=200000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    chi = 0.7542
    print(f"umbral del H-: lambda = hc/chi = {H * C / (chi * E) * 1e6:.4f} um (chi = {chi} eV, valor estandar no consultado)")
    print(f"escalado de Kramers: kappa(2 rho, T)/kappa(rho, T) = 2 ; kappa(rho, 2T)/kappa(rho, T) = {2 ** -3.5:.5f}")
    g = lambda x, p: x ** p * math.exp(x) / (math.exp(x) - 1) ** 2
    num = simpson(lambda x: g(x, 7), 1e-6, 80.0)
    den = simpson(lambda x: g(x, 4), 1e-6, 80.0)
    ana_n = math.gamma(8) * zeta(7)
    ana_d = math.gamma(5) * zeta(4)
    print(f"Int x^7 e^x/(e^x - 1)^2 dx: numerica = {num:.6f} ; Gamma(8) zeta(7) = {ana_n:.6f}")
    print(f"Int x^4 e^x/(e^x - 1)^2 dx: numerica = {den:.6f} ; Gamma(5) zeta(4) = {ana_d:.6f}")
    assert abs(num / ana_n - 1) < 1e-5 and abs(den / ana_d - 1) < 1e-5
    print(f"cociente = {num / den:.4f}: 1/kappa_R = {num / den:.2f} (kT/h)^3/kappa_0")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
