#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C11: velocidad de escape, parametro de Jeans y escape termico relativo.

Datos: G, k y N_A de NIST CODATA 2022 (consulta 2026-11-09); masas, radios y velocidades de escape de las fichas NASA/NSSDC (Tierra 11.186 km/s, Jupiter 59.5 km/s).
Temperaturas del exobase: SINTETICAS e ILUSTRATIVAS (1000 K para la Tierra, 200 K para Marte y Venus: no son datos medidos).
Modelo: v_esc = sqrt(2GM/r); lambda = G M m /(k T r) ; flujo de Jeans proporcional a (1 + lambda) exp(-lambda) / sqrt(m) para igual densidad en el exobase.
Supuestos: distribucion maxwelliana sin colisiones sobre el exobase; no se modelan escape no termico ni hidrodinamico. Tolerancia: v_esc frente a la ficha 0.2 %.
"""
import math, platform
G, K, NA = 6.67430e-11, 1.380649e-23, 6.02214076e23
print(f"Python {platform.python_version()} (biblioteca estandar)")
P = {"Tierra": (5.9722e24, 6371.0e3, 11.186), "Marte": (0.64169e24, 3389.5e3, None), "Venus": (4.8673e24, 6051.8e3, None), "Jupiter": (1898.13e24, 71492.0e3, 59.5)}
for n, (M, r, vf) in P.items():
    v = math.sqrt(2 * G * M / r) / 1e3
    s = f"{n:8s} v_esc = {v:7.3f} km/s"
    if vf:
        d = abs(v - vf) / vf
        s += f" (ficha {vf} km/s, dif. {d*100:.2f} %)"
        assert d < 0.002, (n, v)
    print(s)
mas = {"H": 1.008, "He": 4.0026, "N2": 28.014, "CO2": 44.009}
Texo = {"Tierra": 1000.0, "Marte": 200.0, "Venus": 200.0}
print("planeta  especie   lambda    exp(-lambda)      Jeans relativo a H")
for n in Texo:
    M, r, _ = P[n]
    base = None
    for esp, mm in mas.items():
        m = mm * 1e-3 / NA
        lam = G * M * m / (K * Texo[n] * r)
        w = (1 + lam) * math.exp(-lam) / math.sqrt(m)
        if base is None: base = w
        print(f"{n:8s} {esp:6s} {lam:9.2f} {math.exp(-lam):14.3e} {w/base:14.3e}")
# prueba analitica: lambda es proporcional a la masa molecular: lambda(N2)/lambda(H) = 28.014/1.008
M, r, _ = P["Tierra"]
l = {e: G * M * m * 1e-3 / NA / (K * 1000.0 * r) for e, m in mas.items()}
assert math.isclose(l["N2"] / l["H"], 28.014 / 1.008, rel_tol=1e-12)
# prueba: la energia cinetica de escape de una molecula = (lambda/ ... ): v_esc^2 m /2 = lambda k T
v = math.sqrt(2 * G * M / r)
assert math.isclose(0.5 * mas["H"] * 1e-3 / NA * v ** 2, l["H"] * K * 1000.0, rel_tol=1e-12)
print(f"Tierra (T_exo sintetica 1000 K): lambda(H) = {l['H']:.2f}, lambda(N2) = {l['N2']:.1f}")
# velocidad termica mas probable de H frente a v_esc
vth = math.sqrt(2 * K * 1000.0 / (mas["H"] * 1e-3 / NA))
print(f"v_termica(H, 1000 K) = {vth/1e3:.2f} km/s = {vth/v*100:.1f} % de v_esc")
print("Pruebas superadas.")
