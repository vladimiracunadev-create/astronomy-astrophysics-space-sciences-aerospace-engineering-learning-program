#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C05: inversion de un modelo de dos capas con masa y momento de inercia, no unicidad y restriccion adicional.

Datos consultados (NASA/GSFC NSSDC, Fact Sheets, consulta 2026-11-09): densidad media y I/(M R^2) de la Tierra (5513 kg/m^3; 0.3308; actualizada 2024-11-15),
de Marte (3934 kg/m^3; 0.366; 2025-05-19) y de la Luna (3344 kg/m^3; 0.394; 2024-01-11). Las hojas no dan incertidumbre del momento de inercia: aqui se asume ILUSTRATIVAMENTE 0.001.
Dato SINTETICO: radio relativo del nucleo x = 0.546 +/- 0.010 que sustituye a una restriccion sismica o de otra clase (no es una medida).
Modelo: dos capas homogeneas (manto rho_m, nucleo rho_c, radio relativo x = r_c / R). rho_medio = rho_m + (rho_c - rho_m) x^3 ;
I/(M R^2) = (2/5) [rho_m + (rho_c - rho_m) x^5] / rho_medio. Para x dado el sistema es lineal y se resuelve en forma cerrada. Propagacion: lineal (derivada numerica) y Monte Carlo (semilla 20261109).
Supuestos: capas homogeneas, esfericidad, sin rotacion ni marea. Validez: ilustrativa; no es un modelo de la Tierra, Marte ni la Luna.
Tolerancia: reconstruccion de los datos directos < 1e-12 relativo; propagacion lineal frente a Monte Carlo < 10 % en las desviaciones.
"""
from __future__ import annotations
import math, platform, random

def resolver(rho_med, C, x):
    delta = rho_med * (1.0 - 2.5 * C) / (x**3 * (1.0 - x * x))
    rho_m = rho_med - delta * x**3
    return rho_m, rho_m + delta

def directo(rho_m, rho_c, x):
    rho_med = rho_m + (rho_c - rho_m) * x**3
    C = 0.4 * (rho_m + (rho_c - rho_m) * x**5) / rho_med
    return rho_med, C

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    cuerpos = {"Tierra": (5513.0, 0.3308), "Marte": (3934.0, 0.366), "Luna": (3344.0, 0.394)}
    maxrec = 0.0
    for nombre, (rm, C) in cuerpos.items():
        print(f"\n{nombre}: densidad media = {rm:.0f} kg/m^3 ; I/(MR^2) = {C}")
        print("  x = rc/R   rho_manto [kg/m^3]   rho_nucleo [kg/m^3]   fisico?")
        for x in (0.2, 0.3, 0.4, 0.5, 0.546, 0.6, 0.7):
            rho_m, rho_c = resolver(rm, C, x)
            rm2, C2 = directo(rho_m, rho_c, x)
            maxrec = max(maxrec, abs(rm2 - rm) / rm, abs(C2 - C) / C)
            ok = "si" if (rho_m > 0 and rho_c > rho_m) else "no"
            print(f"  {x:7.3f} {rho_m:18.1f} {rho_c:20.1f}   {ok}")
    # restriccion adicional y propagacion
    rm, C = cuerpos["Tierra"]
    x0, sx, sC = 0.546, 0.010, 0.001
    def f(C_, x_):
        return resolver(rm, C_, x_)
    m0, c0 = f(C, x0)
    h = 1e-6
    dm_dx, dc_dx = [(a - b) / (2 * h) for a, b in zip(f(C, x0 + h), f(C, x0 - h))]
    dm_dC, dc_dC = [(a - b) / (2 * h) for a, b in zip(f(C + h, x0), f(C - h, x0))]
    sm_lin = math.hypot(dm_dx * sx, dm_dC * sC)
    sc_lin = math.hypot(dc_dx * sx, dc_dC * sC)
    rng = random.Random(20261109)
    N = 20000
    ms, cs = [], []
    for _ in range(N):
        a, b = f(rng.gauss(C, sC), rng.gauss(x0, sx))
        ms.append(a); cs.append(b)
    mm, mc = sum(ms) / N, sum(cs) / N
    sm_mc = math.sqrt(sum((a - mm) ** 2 for a in ms) / (N - 1))
    sc_mc = math.sqrt(sum((a - mc) ** 2 for a in cs) / (N - 1))
    print(f"\nTierra con x = {x0} +/- {sx} (sintetico) y sigma(I/MR^2) = {sC} (ilustrativo):")
    print(f"  rho_manto = {m0:.1f} kg/m^3 ; sigma lineal = {sm_lin:.1f} ; sigma Monte Carlo (N = {N}) = {sm_mc:.1f}")
    print(f"  rho_nucleo = {c0:.1f} kg/m^3 ; sigma lineal = {sc_lin:.1f} ; sigma Monte Carlo (N = {N}) = {sc_mc:.1f}")
    print(f"  Contribucion de cada dato a sigma(rho_nucleo): por x = {abs(dc_dx*sx):.1f} ; por I/MR^2 = {abs(dc_dC*sC):.1f} kg/m^3")
    print(f"Maxima discrepancia al reconstruir los datos = {maxrec:.2e}")
    assert maxrec < 1e-12 and abs(sm_lin - sm_mc) / sm_mc < 0.1 and abs(sc_lin - sc_mc) / sc_mc < 0.1
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
