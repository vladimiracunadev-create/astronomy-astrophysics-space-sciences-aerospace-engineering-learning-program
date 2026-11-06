#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C15: funciones de dos variables, cortes y curvas de nivel.

Datos (PUBLICADOS): (GM)_Tierra nominal = 3.986004e5 km3/s2, R_sol nominal =
6.957e8 m, T_eff sol nominal = 5772 K, L_sol nominal = 3.828e26 W (IAU 2015 B3,
arXiv:1510.07674); sigma = 5.670374419e-8 W m-2 K-4 (CODATA 2022, NIST);
GM_Luna = 4.90e3 km3/s2 y distancia 384 400 km (NASA/NSSDC, ficha lunar).
Modelos: Parte A: Phi(x, y) = -GM_T/r1 - GM_L/r2 en el plano de la línea
Tierra-Luna (sin rotación ni Sol; Tierra en (0,0), Luna en (d,0)).
Parte B: L(R, T) = 4 pi R^2 sigma T^4 (cuerpo negro esférico).
Supuestos: cuerpos puntuales; radiación de cuerpo negro. Validez: lejos de los
cuerpos (r > radio) en A; estrellas esféricas en B.
Tolerancias: curvas de nivel R = sqrt(L/4 pi sigma)/T^2 exactas a 1e-12;
L(R_N, T_N) frente a L_N: se informa la diferencia (las constantes difieren).
"""
from __future__ import annotations
import math, platform, sys

GE, GL, D = 3.986004e5, 4.90e3, 384_400.0
SIGMA = 5.670374419e-8
R_SOL, T_SOL, L_SOL = 6.957e8, 5772.0, 3.828e26


def phi(x, y):
    r1 = math.hypot(x, y)
    r2 = math.hypot(x - D, y)
    return -GE / r1 - GL / r2


def luminosidad(R, T):
    return 4 * math.pi * R * R * SIGMA * T**4


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print("PARTE A: Phi(x, y) [km2/s2]")
    xs = D / (1 + math.sqrt(GL / GE))
    p0 = phi(xs, 0.0)
    print(f"Punto de atracción igual sobre el eje: x* = {xs:.1f} km;  Phi(x*, 0) = {p0:.4f}")
    print("  corte a lo largo de x (y = 0):")
    for dx in (-20000, -5000, 0, 5000, 20000):
        v = phi(xs + dx, 0.0)
        print(f"    x* {dx:+7d} km: Phi = {v:.4f}  ({'<' if v < p0 else '=' if v == p0 else '>'} Phi(x*,0))")
        if dx:
            prueba(v < p0, "máximo a lo largo de x")
    print("  corte a lo largo de y (x = x*):")
    for dy in (0, 5000, 20000, 50000):
        v = phi(xs, dy)
        print(f"    y = {dy:6d} km: Phi = {v:.4f}")
        if dy:
            prueba(v > p0, "mínimo a lo largo de y")
    print("  -> máximo en un corte y mínimo en el otro: PUNTO DE SILLA")
    # simetría respecto a y
    prueba(abs(phi(1e5, 3e4) - phi(1e5, -3e4)) < 1e-12, "simetría y -> -y")
    # Phi -> -GM/r lejos de ambos cuerpos
    lejos = phi(1e8, 0.0)
    print(f"  Phi(1e8 km, 0) = {lejos:.6e};  -(GM_T+GM_L)/r = {-(GE+GL)/1e8:.6e}")
    prueba(abs(lejos / (-(GE + GL) / 1e8) - 1) < 5e-3, "campo lejano ~ masa total")

    print("\nPARTE B: L(R, T) = 4 pi R^2 sigma T^4")
    L_calc = luminosidad(R_SOL, T_SOL)
    print(f"L(R_sol^N, T_sol^N) = {L_calc:.5e} W;  L_sol^N = {L_SOL:.3e} W;  dif. relativa = {L_calc/L_SOL-1:+.2e}")
    prueba(abs(L_calc / L_SOL - 1) < 5e-3, "L(R, T) coherente con la nominal")
    print("  Curva de nivel L = L_N (radio R en función de T):")
    k = math.sqrt(L_SOL / (4 * math.pi * SIGMA))
    for T in (2886.0, 5772.0, 11544.0, 23088.0):
        R = k / T**2
        prueba(abs(luminosidad(R, T) / L_SOL - 1) < 1e-12, "punto sobre la curva de nivel")
        print(f"    T = {T:8.0f} K -> R = {R:.4e} m = {R/R_SOL:.4f} R_sol")
    prueba(abs((k / 11544.0**2) / (k / 5772.0**2) - 0.25) < 1e-12, "T x2 -> R /4")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
