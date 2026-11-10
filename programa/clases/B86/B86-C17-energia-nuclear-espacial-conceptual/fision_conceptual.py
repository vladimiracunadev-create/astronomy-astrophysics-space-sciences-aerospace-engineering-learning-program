#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C17: dimensionamiento CONCEPTUAL de la conversion y del radiador de un sistema de fision de superficie (orden de magnitud).

Datos consultados (2026-11-10): constante de Stefan-Boltzmann sigma = 5.670374419e-8 W m-2 K-4 (NIST, CODATA 2022); la pagina de energia nuclear de la NASA para naves pequenas dice que
el mercado aun no estimula fuentes nucleares miniaturizadas (capitulo de potencia). La pagina de Fission Surface Power de la NASA NO se pudo abrir (redirecciones): ninguna cifra de ese programa se usa.
ILUSTRATIVOS (sinteticos, no medidos, no de un diseno real): potencia electrica 40 kW, temperatura de entrada del ciclo T_h = 900 K, fraccion de Carnot 0.5, radiador isotermo de emisividad 0.85,
densidad de area del radiador 5 kg/m2, sin entorno (sumidero a 0 K, cota conservadora favorable).
Modelo: eta = f (1 - T_c/T_h); Q_th = P_e / eta; Q_rej = Q_th - P_e; A = Q_rej / (eps sigma T_c^4).
Segunda via: la T_c que minimiza A se busca con seccion aurea y con barrido; para f = 1 se compara con el optimo analitico T_c/T_h = 3/4.
Tolerancia: seccion aurea frente a barrido < 0.5 K; para f = 1 el optimo numerico frente a 0.75 < 1e-6.
"""
from __future__ import annotations
import math, platform

SIGMA = 5.670374419e-8
PE, TH, F_CARNOT, EPS, RHO_A = 40.0e3, 900.0, 0.5, 0.85, 5.0


def eta(tc, th=TH, f=F_CARNOT):
    return f * (1.0 - tc / th)


def area(tc, th=TH, f=F_CARNOT, pe=PE):
    e = eta(tc, th, f)
    return pe * (1.0 / e - 1.0) / (EPS * SIGMA * tc ** 4)


def aurea(fun, a, b):
    g = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(300):
        if fun(c) < fun(d):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return 0.5 * (a + b)


def resultados():
    r = {}
    tc_opt = aurea(lambda t: area(t), 300.0, 890.0)
    barrido = min((300.0 + 0.1 * k for k in range(5901)), key=area)
    r["Tc_opt"], r["Tc_barr"], r["dTc"] = tc_opt, barrido, abs(tc_opt - barrido)
    r["eta_opt"] = eta(tc_opt)
    r["A_opt"] = area(tc_opt)
    r["Qth"] = PE / r["eta_opt"]
    r["Qrej"] = r["Qth"] - PE
    r["m_rad"] = r["A_opt"] * RHO_A
    r["Carnot_opt"] = 1.0 - tc_opt / TH
    # f = 1: optimo analitico 3/4
    t1 = aurea(lambda t: area(t, TH, 1.0), 300.0, 890.0)
    r["x_f1"] = t1 / TH
    r["dx_f1"] = abs(r["x_f1"] - 0.75)
    # comparacion con el diseno a Tc = 400, 500, 600 K
    for tc in (400.0, 500.0, 600.0, 700.0):
        k = int(tc)
        r[f"eta{k}"], r[f"A{k}"], r[f"m{k}"] = eta(tc), area(tc), area(tc) * RHO_A
    # sensibilidad a Th
    for th in (800.0, 1100.0):
        k = int(th)
        t = aurea(lambda x: area(x, th), 300.0, th - 10.0)
        r[f"Tc_th{k}"], r[f"A_th{k}"] = t, area(t, th)
    r["x_opt"] = tc_opt / TH
    r["A_opt_m2"] = r["A_opt"]
    r["Pe_kW"] = PE / 1e3
    r["eta_opt_pct"] = r["eta_opt"] * 100.0
    r["Qrej_kW"] = r["Qrej"] / 1e3
    r["Qth_kW"] = r["Qth"] / 1e3
    for k in (400, 500, 600, 700):
        r[f"eta{k}_pct"] = r[f"eta{k}"] * 100.0
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Sistema CONCEPTUAL (ilustrativo): P_e = {PE/1e3:.0f} kW ; T_h = {TH:.0f} K ; f = {F_CARNOT} ; eps = {EPS} ; densidad de area = {RHO_A} kg/m2")
    print(f"Radiador de area minima: T_c = {r['Tc_opt']:.2f} K (barrido {r['Tc_barr']:.1f} K ; dif {r['dTc']:.2f} K) ; T_c/T_h = {r['x_opt']:.4f}")
    print(f"  eta = {r['eta_opt']*100:.2f} % ; Q_th = {r['Qth']/1e3:.1f} kW ; Q_rechazado = {r['Qrej']/1e3:.1f} kW ; A = {r['A_opt']:.1f} m2 ; masa del radiador = {r['m_rad']:.0f} kg")
    print(" T_c [K]   eta [%]   A [m2]   masa radiador [kg]")
    for k in (400, 500, 600, 700):
        print(f" {k:6d}   {r[f'eta{k}']*100:7.2f}   {r[f'A{k}']:7.1f}   {r[f'm{k}']:10.0f}")
    print(f"Con f = 1 (Carnot ideal): T_c/T_h optimo = {r['x_f1']:.6f} (analitico 0.75 ; dif {r['dx_f1']:.1e})")
    print(f"Sensibilidad a T_h: 800 K -> T_c = {r['Tc_th800']:.1f} K, A = {r['A_th800']:.1f} m2 ; 1100 K -> T_c = {r['Tc_th1100']:.1f} K, A = {r['A_th1100']:.1f} m2")
    assert r["dTc"] < 0.5
    assert r["dx_f1"] < 1e-6
    assert r["A_opt"] <= min(r["A400"], r["A500"], r["A600"], r["A700"]) + 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
