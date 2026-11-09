#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C13: temperatura de equilibrio, flujo recibido y distancias para una temperatura dada.

Datos: sigma_SB (NIST CODATA 2022); R_sol, S_sol = 1361 W/m2, L_sol = 3.828e26 W, T_eff,sol = 5772 K (IAU 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09.
Contexto: Kopparapu y colaboradores revisan las zonas habitables de estrellas de la secuencia principal con modelos climaticos 1-D que mejoran los de Kasting y
colaboradores de 1993 (arXiv:1301.6674, resumen, consultado 2026-11-09); AQUI NO SE USAN sus limites: la clase calcula solo la temperatura de equilibrio sin efecto
invernadero. Las estrellas K y M (T = 4500 K, R = 0.7 R_sol; T = 3300 K, R = 0.3 R_sol), el albedo (0.3 e incertidumbre uniforme en [0.1, 0.6]) y el efecto invernadero
de +33 K son ILUSTRATIVOS.
Modelo: T_eq = T_* sqrt(R_*/(2 a)) [f (1 - A)]^(1/4) con f = 1 (redistribucion global); flujo S = sigma T_*^4 (R_*/a)^2; distancia para una T_eq dada:
a = (R_*/2)(T_*/T_eq)^2 sqrt(1 - A). Propagacion de la incertidumbre del albedo: linea (sigma_T = T sigma_A/(4(1-A))) frente a Monte Carlo (semilla fija).
Supuestos: planeta con albedo uniforme, sin atmosfera ni invernadero salvo el desplazamiento indicado. Validez: orientativa.
Tolerancia: S_sol calculado frente a 1361 W/m2 dentro del 0.3 %; Monte Carlo frente a linea dentro del 3 %.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

SIG = 5.670374419e-8
R_SOL, L_SOL, S_SOL, T_SOL = 6.957e8, 3.828e26, 1361.0, 5772.0
AU = 1.49597870700e11


def t_eq(ts, rs, a, albedo):
    return ts * math.sqrt(rs / (2 * a)) * (1 - albedo) ** 0.25


def flujo(ts, rs, a):
    return SIG * ts ** 4 * (rs / a) ** 2


def distancia_para_t(ts, rs, t, albedo):
    return rs / 2 * (ts / t) ** 2 * math.sqrt(1 - albedo)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    s_calc = flujo(T_SOL, R_SOL, AU)
    s_l = L_SOL / (4 * math.pi * AU ** 2)
    print(f"flujo solar a 1 au: sigma T^4 (R/a)^2 = {s_calc:.2f} W/m2 ; L/(4 pi a^2) = {s_l:.2f} ; valor nominal de la UAI = {S_SOL}")
    assert abs(s_calc / S_SOL - 1) < 0.003 and abs(s_l / S_SOL - 1) < 0.003, "flujo solar"
    t1 = t_eq(T_SOL, R_SOL, AU, 0.3)
    print(f"T_eq de un planeta a 1 au del Sol con albedo 0.3 = {t1:.2f} K ; con efecto invernadero ilustrativo de +33 K: {t1 + 33:.2f} K")
    print(f"{'a [au]':>7} {'T_eq (A = 0.3) [K]':>19} {'S [S_sol]':>10}")
    for a in (0.3, 0.5, 0.72, 1.0, 1.5, 5.2):
        print(f"{a:7.2f} {t_eq(T_SOL, R_SOL, a * AU, 0.3):19.2f} {flujo(T_SOL, R_SOL, a * AU) / S_SOL:10.3f}")
    print(f"{'estrella':<10} {'T* [K]':>7} {'R* [R_sol]':>11} {'a(T_eq = 273) [au]':>19} {'a(T_eq = 373) [au]':>19} {'a(S = S_sol) [au]':>18}")
    for nombre, ts, rs in (("Sol", T_SOL, R_SOL), ("enana K", 4500.0, 0.7 * R_SOL), ("enana M", 3300.0, 0.3 * R_SOL)):
        a273 = distancia_para_t(ts, rs, 273.0, 0.3) / AU
        a373 = distancia_para_t(ts, rs, 373.0, 0.3) / AU
        a_s = rs * math.sqrt(SIG * ts ** 4 / S_SOL) / AU
        assert abs(t_eq(ts, rs, a273 * AU, 0.3) - 273.0) < 1e-9
        print(f"{nombre:<10} {ts:7.0f} {rs / R_SOL:11.2f} {a273:19.4f} {a373:19.4f} {a_s:18.4f}")
    # incertidumbre del albedo
    rng = random.Random(20261109)
    a0 = 1.0 * AU
    muestras = [t_eq(T_SOL, R_SOL, a0, rng.uniform(0.1, 0.6)) for _ in range(200000)]
    mc_m, mc_s = statistics.mean(muestras), statistics.pstdev(muestras)
    sa = 0.5 / math.sqrt(12)
    lin = t_eq(T_SOL, R_SOL, a0, 0.35) * sa / (4 * (1 - 0.35))
    print(f"albedo uniforme en [0.1, 0.6]: T_eq media = {mc_m:.2f} K ; desviacion Monte Carlo = {mc_s:.3f} K ; lineal = {lin:.3f} K ; cociente = {mc_s / lin:.4f}")
    assert abs(mc_s / lin - 1) < 0.03, "propagacion del albedo"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
