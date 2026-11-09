#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C01: solucion formal de la transferencia radiativa y oscurecimiento del limbo.

Datos: sigma_SB (NIST CODATA 2022) y T_eff = 5772 K (UAI 2015 B3), consultados 2026-11-09. Las funciones fuente de prueba (lineal, exponencial) son ILUSTRATIVAS (sinteticas).
Modelo: atmosfera plano-paralela; I(0, mu) = Int_0^inf S(tau) exp(-tau/mu) dtau/mu por Simpson; para S = a + b tau el resultado exacto es a + b mu (Eddington-Barbier);
S(tau) = a e^(-tau) + b: I = a/(1 + mu) + b; atmosfera gris de Eddington S = (sigma/pi)(3/4) T_eff^4 (tau + 2/3) con oscurecimiento I(mu)/I(1) = (2/3 + mu)/(5/3) y flujo F = sigma T_eff^4.
Supuestos: ETL, dispersion nula, plano-paralela. Validez: ideal.
Tolerancia: Simpson frente a la forma cerrada a 1e-8; flujo emergente frente a sigma T_eff^4 a 1e-4.
"""
from __future__ import annotations
import math, platform, sys
SIG, TEFF = 5.670374419e-8, 5772.0

def emergente(s, mu, tmax=60.0, n=60000):
    h = tmax / n
    f = lambda t: s(t) * math.exp(-t / mu) / mu
    tot = f(0) + f(tmax)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(i * h)
    return tot * h / 3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a, b = 0.4, 0.6
    print(f"{'mu':>5} {'I numerica (S lineal)':>22} {'a + b mu':>10} {'I (S = a e^-t + b)':>20} {'a/(1+mu) + b':>13}")
    for mu in (1.0, 0.6, 0.2):
        i1 = emergente(lambda t: a + b * t, mu)
        i2 = emergente(lambda t: a * math.exp(-t) + b, mu)
        print(f"{mu:5.1f} {i1:22.8f} {a + b * mu:10.8f} {i2:20.8f} {a / (1 + mu) + b:13.8f}")
        assert abs(i1 - (a + b * mu)) < 1e-8 and abs(i2 - (a / (1 + mu) + b)) < 1e-8
    c = SIG / math.pi * 0.75 * TEFF ** 4
    s = lambda t: c * (t + 2 / 3)
    i1 = emergente(s, 1.0)
    print(f"{'mu':>5} {'I(mu)/I(1) numerico':>20} {'(2/3 + mu)/(5/3)':>18}")
    for mu in (1.0, 0.6, 0.2):
        r = emergente(s, mu) / i1
        print(f"{mu:5.1f} {r:20.8f} {(2 / 3 + mu) / (5 / 3):18.8f}")
        assert abs(r - (2 / 3 + mu) / (5 / 3)) < 1e-8
    n = 200
    flujo = 0.0
    for k in range(n):
        mu = (k + 0.5) / n
        flujo += emergente(s, mu, n=6000) * mu / n
    flujo *= 2 * math.pi
    print(f"flujo emergente = {flujo:.6e} W/m2 ; sigma T_eff^4 = {SIG * TEFF ** 4:.6e} W/m2 ; cociente = {flujo / (SIG * TEFF ** 4):.6f}")
    assert abs(flujo / (SIG * TEFF ** 4) - 1) < 1e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
