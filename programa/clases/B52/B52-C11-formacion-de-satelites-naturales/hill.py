#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C11: satelites galileanos dentro de la esfera de Hill de Jupiter y estabilidad de orbitas en el problema de Hill.

Datos consultados el 2026-11-09: semiejes de los satelites (1e3 km) de la ficha jovian de la NASA/NSSDC (Io 421.8, Europa 671.1,
Ganimedes 1070.4, Calisto 1882.7); distancia de Jupiter al Sol 778.5e6 km de la ficha de planetas de la NASA/NSSDC (rotulada «Distance from Sun»);
(GM)_sol y (GM)_J nominales de la IAU 2015 (Resolucion B3); G de NIST (CODATA 2022). Las fichas no dan incertidumbres.
Via 2 (SIMULACION, no observacion): problema de Hill planar en unidades R_H = 1, Omega = 1:
x'' = 2 y' + 3x - 3x/r^3 ; y'' = -2 x' - 3y/r^3. Orbita circular inicial prograda/retrograda de radio rho, integrada con RK4 (h = 0.002) hasta t = 100;
se declara escape si r > 2. Umbral por biseccion sobre una malla (el borde es fractal: el umbral es el mayor rho de la malla que sobrevive antes del primer escape).
Los umbrales publicados (~0.5 R_H prograda, ~0.7 R_H retrograda) NO se consultaron; se informan solo los de esta simulacion.
Tolerancias: R_H frente a una segunda via (formula con masas) 1e-12; los umbrales numericos se reportan sin tolerancia analitica.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
GM_SOL, GM_J = 1.3271244e20, 1.2668653e17
A_J = 778.5e9
SAT = [("Io", 421.8e6), ("Europa", 671.1e6), ("Ganimedes", 1070.4e6), ("Calisto", 1882.7e6)]


def radio_hill():
    return A_J * (GM_J / (3.0 * GM_SOL)) ** (1.0 / 3.0)


def radio_hill_masas():
    ms, mj = GM_SOL / G, GM_J / G
    return A_J * (mj / (3.0 * ms)) ** (1.0 / 3.0)


def deriv(s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, 2 * vy + 3 * x - 3 * x / r3, -2 * vx - 3 * y / r3)


def sobrevive(rho, signo, t_fin=100.0, h=0.002):
    s = (rho, 0.0, 0.0, signo * math.sqrt(3.0 / rho) - rho)
    for _ in range(int(t_fin / h)):
        k1 = deriv(s)
        k2 = deriv(tuple(a + 0.5 * h * b for a, b in zip(s, k1)))
        k3 = deriv(tuple(a + 0.5 * h * b for a, b in zip(s, k2)))
        k4 = deriv(tuple(a + h * b for a, b in zip(s, k3)))
        s = tuple(a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4))
        if s[0] * s[0] + s[1] * s[1] > 4.0:
            return False
    return True


def umbral(signo):
    malla = [0.30 + 0.025 * i for i in range(0, 41)]  # 0.30 .. 1.30
    ult = malla[0]
    for rho in malla:
        if sobrevive(rho, signo):
            ult = rho
        else:
            return ult, rho
    return ult, None


def calcular():
    rh = radio_hill()
    filas = [(n, a, a / rh) for n, a in SAT]
    up = umbral(+1.0)
    ur = umbral(-1.0)
    return dict(rh=rh, rh2=radio_hill_masas(), filas=filas, up=up, ur=ur)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Radio de Hill de Jupiter = {r['rh'] / 1e9:.3f} millones de km (formula con (GM)) ; con masas = {r['rh2'] / 1e9:.3f} ; dif. rel. = {abs(r['rh'] / r['rh2'] - 1):.1e}")
    print(f"{'satelite':>10} {'a [1e3 km]':>11} {'a / R_H':>9}")
    for n, a, f in r["filas"]:
        print(f"{n:>10} {a / 1e6:11.1f} {f:9.4f}")
    print("SIMULACION (problema de Hill planar, no observacion):")
    print(f"  orbita prograda: sobrevive hasta rho = {r['up'][0]:.3f} R_H ; primer escape en la malla en rho = {r['up'][1]}")
    print(f"  orbita retrograda: sobrevive hasta rho = {r['ur'][0]:.3f} R_H ; primer escape en la malla en rho = {r['ur'][1]}")
    assert abs(r["rh"] / r["rh2"] - 1) < 1e-12 and all(f < 0.1 for _, _, f in r["filas"])
    assert r["up"][0] >= 0.30 and (r["ur"][1] is None or r["ur"][0] >= r["up"][0])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
