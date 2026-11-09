#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C02: frecuencia de plasma, retardo por dispersion y perdida en espacio libre.

Datos: e, m_e, epsilon_0, c y pi de NIST CODATA 2022 (consultada 2026-11-09). La densidad electronica (0,03 cm^-3), la medida de dispersion
(DM = 100 pc cm^-3) y las frecuencias son ILUSTRATIVAS.
Modelo: f_p = sqrt(n e^2 / (4 pi^2 eps0 m)); retardo de grupo t(f) = L/c * (1 - fp^2/f^2)^(-1/2) integrado numericamente sobre una columna
uniforme, frente a la formula de primer orden dt = K DM / f^2 con K = e^2/(8 pi^2 eps0 m c). Perdida en espacio libre FSPL = (4 pi d/lambda)^2.
Supuestos: plasma frio uniforme sin campo magnetico; f >> f_p. Validez: orientativa.
Tolerancia: retardo exacto frente a primer orden dentro del 0,1 % a 1 GHz; K frente a 4,149 ms GHz^2 cm^3/pc dentro del 0,1 %.
"""
from __future__ import annotations
import math, platform
E, ME, EPS0, C = 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12, 299792458.0
PC = 3.0856775814913673e16

def fp(n_cm3):
    return math.sqrt(n_cm3 * 1e6 * E ** 2 / (4 * math.pi ** 2 * EPS0 * ME))

def retardo_exacto(f, n_cm3, L_pc):
    r = fp(n_cm3) / f
    return L_pc * PC / C * (1 / math.sqrt(1 - r * r) - 1)

def calc():
    Kd = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME * C)       # m^2 s^-1 ... por columna en m^-2
    K_ms = Kd * 1e6 * PC * 1e3 / 1e18                 # ms GHz^2 cm^3 pc^-1 (1 pc cm^-3 = 1e6*PC m^-2)
    n, L = 0.03, 100 / 0.03
    f1 = 1e9
    ex = retardo_exacto(f1, n, L)
    apx = Kd * (n * 1e6 * L * PC) / f1 ** 2
    filas = []
    for f in (0.4e9, 1e9, 1.4e9, 5e9):
        filas.append((f, Kd * (n * 1e6 * L * PC) / f ** 2, retardo_exacto(f, n, L)))
    lam = C / 1.4e9
    fspl = 20 * math.log10(4 * math.pi * 1000e3 / lam)
    return dict(fp=fp(0.03), fp_ion=fp(1e5), K=K_ms, ex=ex, apx=apx, filas=filas, fspl=fspl)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"f_p(0.03 cm^-3) = {r['fp']/1e3:.3f} kHz ; f_p(1e5 cm^-3) = {r['fp_ion']/1e6:.3f} MHz")
    print(f"K = {r['K']:.4f} ms GHz^2 cm^3 pc^-1")
    print(f"{'f [GHz]':>8} {'primer orden [ms]':>18} {'exacto [ms]':>12}")
    for f, a, b in r["filas"]:
        print(f"{f/1e9:8.1f} {a*1e3:18.4f} {b*1e3:12.4f}")
    print(f"FSPL a 1.4 GHz y 1000 km = {r['fspl']:.2f} dB")
    assert abs(r["K"] / 4.149 - 1) < 1e-3
    assert abs(r["ex"] / r["apx"] - 1) < 1e-3
    assert abs(r["fp"] / (8.98e3 * math.sqrt(0.03)) - 1) < 2e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
