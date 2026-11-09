#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C12: escalera rotacional de un rotor rigido (tipo CO) y poblaciones en ETL.

Datos: h, k y c de NIST CODATA 2022 (consultada 2026-11-09). La constante rotacional B = 57,636 GHz es un valor de referencia conocido para CO
que NO se consulto en esta clase; se usa como parametro ILUSTRATIVO. Las temperaturas de excitacion (10, 30, 100 K) son ilustrativas.
Modelo: E_J = h B J (J+1); nu(J->J-1) = 2 B J; poblacion en ETL n_J/N = (2J+1) exp(-E_J/kT)/Z, con Z sumada numericamente y comparada con
Z ~ kT/(hB) + 1/3; J de maxima poblacion frente a sqrt(kT/(2hB)) - 1/2. Efecto Doppler: delta nu / nu = v/c.
Supuestos: rotor rigido sin distorsion centrifuga, ETL, sin profundidad optica. Validez: orientativa.
Tolerancia: Z numerica frente a la aproximacion dentro del 1 % para T >= 30 K; J pico dentro de +-1 del valor analitico.
"""
from __future__ import annotations
import math, platform
H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0
B = 57.636e9

def pob(T, Jmax=60):
    w = [(2 * J + 1) * math.exp(-H * B * J * (J + 1) / (K * T)) for J in range(Jmax)]
    Z = sum(w)
    return [x / Z for x in w], Z

def calc():
    filas = []
    for T in (10.0, 30.0, 100.0):
        p, Z = pob(T)
        Jp = max(range(len(p)), key=lambda j: p[j])
        filas.append((T, Z, K * T / (H * B) + 1 / 3, Jp, math.sqrt(K * T / (2 * H * B)) - 0.5, p[:6]))
    lad = [(J, 2 * B * J / 1e9, C / (2 * B * J) * 1e3, H * B * J * (J + 1) / K) for J in range(1, 5)]
    dv = 1.0
    dnu = 2 * B * dv * 1e3 / C / 1e6
    return dict(filas=filas, lad=lad, dnu_MHz=dnu, T1=H * 2 * B / K)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'J->J-1':>7} {'nu [GHz]':>9} {'lambda [mm]':>12} {'E_J/k [K]':>10}")
    for J, nu, lam, Ek in r["lad"]:
        print(f"{J:3d}->{J-1:<2d} {nu:9.3f} {lam:12.4f} {Ek:10.2f}")
    print(f"{'T [K]':>6} {'Z numerica':>11} {'kT/hB+1/3':>10} {'J pico':>7} {'J analitico':>12}")
    for T, Z, Za, Jp, Ja, p in r["filas"]:
        print(f"{T:6.0f} {Z:11.3f} {Za:10.3f} {Jp:7d} {Ja:12.2f}  p(J=0..5) = " + " ".join(f"{x:.3f}" for x in p))
    print(f"1 km/s en la transicion 1-0 desplaza {r['dnu_MHz']:.4f} MHz ; h nu/k (1-0) = {r['T1']:.3f} K")
    for T, Z, Za, Jp, Ja, p in r["filas"][1:]:
        assert abs(Z / Za - 1) < 0.01
    for T, Z, Za, Jp, Ja, p in r["filas"]:
        assert abs(Jp - Ja) <= 1.0
    assert abs(r["lad"][0][1] - 115.272) < 0.001
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
