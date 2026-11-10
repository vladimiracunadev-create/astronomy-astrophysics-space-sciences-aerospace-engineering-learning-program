#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C04: parametro gravitacional mu = GM, su precision frente a G y M, y conversion de unidades.

Datos consultados (2026-11-10): G = 6.67430e-11 m3/(kg s2), incertidumbre estandar 0.00015e-11 (NIST, CODATA 2022);
(GM)sol = 1.3271244e20 y (GM)Tierra = 3.986004e14 m3/s2 (nominales IAU 2015 B3, exactos por definicion);
fichas NASA/NSSDC: masas Tierra 5.9722e24, Marte 0.64169e24, Luna 0.07346e24 kg; radios medios 6371.000, 3389.5, 1737.4 km.
Sistema: SI. mu del Sol y la Tierra son nominales; mu de Marte y la Luna se CALCULAN aqui como G*M con la masa de la ficha
(su precision real es peor que la de los valores determinados por seguimiento de naves, que NO se consultaron).
Segunda via: la velocidad circular rasante v = sqrt(mu/R) se calcula con mu nominal y con G*M; deben coincidir en la precision de G.
Tolerancias: conversion km3/s2 <-> m3/s2 exacta (1e-15); GM(Tierra)/(G*M ficha) dentro de 1e-3.
"""
from __future__ import annotations
import math, platform

G, G_U = 6.67430e-11, 0.00015e-11
MU_SOL, MU_T = 1.3271244e20, 3.986004e14
M = {"Tierra": 5.9722e24, "Marte": 0.64169e24, "Luna": 0.07346e24}
RAD = {"Tierra": 6371.000e3, "Marte": 3389.5e3, "Luna": 1737.4e3}


def calcular():
    R = {}
    R["g_rel"] = G_U / G
    R["mu_gm"] = {k: G * v for k, v in M.items()}
    for k in M:
        R["mu_" + k] = R["mu_gm"][k]
    R["mu_t_dif"] = (G * M["Tierra"] - MU_T) / MU_T
    R["mu_rel_u"] = R["g_rel"]  # incertidumbre relativa de G*M si M es exacta
    R["m_de_mu"] = MU_T / G
    R["m_u"] = R["m_de_mu"] * R["g_rel"]
    R["razon_sol_tierra"] = MU_SOL / MU_T
    R["mu_t_km"] = MU_T / 1e9
    R["mu_t_vuelta"] = R["mu_t_km"] * 1e9
    R["conv_err"] = abs(R["mu_t_vuelta"] - MU_T) / MU_T
    v = {}
    for k in M:
        mu = R["mu_gm"][k]
        v[k] = math.sqrt(mu / RAD[k])
    R["v_rasante"] = v
    R["v_rasante_t_nominal"] = math.sqrt(MU_T / RAD["Tierra"])
    R["v_dif"] = abs(v["Tierra"] - R["v_rasante_t_nominal"]) / R["v_rasante_t_nominal"]
    # el error de v por G: v ~ sqrt(G M) => mitad de la incertidumbre relativa de G (si M es exacta)
    for k in M:
        R["v_" + k] = v[k]
    R["v_u_rel"] = 0.5 * R["g_rel"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"Incertidumbre relativa de G (CODATA 2022) = {R['g_rel']:.2e}")
    print("mu = G*M con la masa de la ficha NASA/NSSDC [m3/s2] (derivado):")
    for k, v in R["mu_gm"].items():
        print(f"  {k:7s} {v:.6e}   (km3/s2: {v / 1e9:.4f})")
    print(f"  (GM)Tierra nominal IAU = {MU_T:.6e} ; G*M_ficha frente al nominal = {R['mu_t_dif']:+.2e}")
    print(f"M = mu/G (Tierra) = {R['m_de_mu']:.5e} kg ; incertidumbre por G = {R['m_u']:.2e} kg")
    print(f"(GM)sol/(GM)Tierra = {R['razon_sol_tierra']:.1f}")
    print(f"Conversion km3/s2 <-> m3/s2: ida y vuelta error relativo = {R['conv_err']:.1e}")
    print("Velocidad circular rasante sqrt(mu/R) con G*M [km/s]:")
    for k, v in R["v_rasante"].items():
        print(f"  {k:7s} {v / 1e3:.4f}")
    print(f"  Tierra con mu nominal = {R['v_rasante_t_nominal'] / 1e3:.4f} km/s ; diferencia relativa = {R['v_dif']:.2e} ; incertidumbre por G = {R['v_u_rel']:.1e}")
    assert abs(R["mu_t_dif"]) < 1e-3
    assert R["conv_err"] < 1e-15
    assert R["v_dif"] < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
