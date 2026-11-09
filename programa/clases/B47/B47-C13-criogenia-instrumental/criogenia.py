#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C13: criogenia instrumental, escudos radiativos, conduccion por soportes y vida de un criogeno.

Datos: constante de Stefan-Boltzmann 5,670374419e-8 W m-2 K-4 de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09).
ILUSTRATIVOS (no son valores de ningun instrumento): T_caliente 290 K, T_fria 40 K, emisividad 0,02 en todas las superficies, area 0,2 m2, 4 soportes de 2 mm2 y 0,2 m,
conductividad k = 0,005 T W m-1 K-1 (lineal en T), 50 kg de criogeno con calor latente 2,09e4 J/kg (valor de uso general, no consultado aqui).
Modelo: (1) flujo entre N escudos q = sigma (Th^4 - Tc^4) / ((N + 1)(2/eps - 1)); las temperaturas de los escudos se obtienen iterando el balance T_i^4 = (T_{i-1}^4 + T_{i+1}^4)/2
(Gauss-Seidel) y se contrastan con la solucion lineal T_i^4 = Th^4 - i (Th^4 - Tc^4)/(N + 1); (2) conduccion Q = (A/L) integral k dT por trapecios frente a (A/L) a (Th^2 - Tc^2)/2;
(3) vida del criogeno = m L / Q_total.
Supuestos: superficies grises difusas paralelas y grandes, sin fugas por cables ni perdidas en costuras, regimen estacionario. Validez: ilustrativa.
Tolerancia: temperaturas de los escudos, 1e-6 relativo; conduccion numerica, 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

SIGMA = 5.670374419e-8
TH, TC, EPS, AREA = 290.0, 40.0, 0.02, 0.2
A_K = 0.005
STRUT_A, STRUT_L, N_STRUT = 2e-6, 0.2, 4
M_CRIO, L_CRIO = 50.0, 2.09e4


def flujo(n):
    return SIGMA * (TH ** 4 - TC ** 4) / ((n + 1) * (2 / EPS - 1))


def temps_gs(n, iters=20000):
    t4 = [TH ** 4 - i * (TH ** 4 - TC ** 4) / (n + 1) * 0.0 for i in range(n + 2)]
    for i in range(1, n + 1):
        t4[i] = TH ** 4 * 0.5
    t4[0], t4[-1] = TH ** 4, TC ** 4
    for _ in range(iters):
        for i in range(1, n + 1):
            t4[i] = 0.5 * (t4[i - 1] + t4[i + 1])
    return [x ** 0.25 for x in t4]


def temps_analitico(n):
    return [(TH ** 4 - i * (TH ** 4 - TC ** 4) / (n + 1)) ** 0.25 for i in range(n + 2)]


def conduccion_num(n=100000):
    h = (TH - TC) / n
    s = 0.0
    for i in range(n + 1):
        t = TC + i * h
        s += (0.5 if i in (0, n) else 1.0) * A_K * t
    return STRUT_A / STRUT_L * s * h


def calc():
    r = {"q": {n: flujo(n) for n in (0, 1, 3, 10)}}
    r["temps"] = (temps_gs(3), temps_analitico(3))
    r["cond_num"] = conduccion_num()
    r["cond_an"] = STRUT_A / STRUT_L * A_K * (TH ** 2 - TC ** 2) / 2
    r["cond_total"] = N_STRUT * r["cond_an"]
    r["vida"] = {}
    for n in (0, 10, 40):
        qt = flujo(n) * AREA + r["cond_total"]
        r["vida"][n] = (qt, M_CRIO * L_CRIO / qt / 86400 / 365.25)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for n, q in r["q"].items():
        print(f"N = {n:2d} escudos: q = {q:.4f} W/m2 (cociente con N = 0: {q/r['q'][0]:.4f} = 1/(N+1))")
    gs, an = r["temps"]
    print("temperaturas con 3 escudos [K]:")
    for i, (a, b) in enumerate(zip(gs, an)):
        print(f"  superficie {i}: Gauss-Seidel = {a:.6f} ; analitica = {b:.6f}")
        assert abs(a - b) / b < 1e-6
    print(f"conduccion por soporte: numerica = {r['cond_num']*1e3:.6f} mW ; analitica = {r['cond_an']*1e3:.6f} mW ; 4 soportes = {r['cond_total']*1e3:.4f} mW")
    assert abs(r["cond_num"] - r["cond_an"]) / r["cond_an"] < 1e-6
    for n, (qt, y) in r["vida"].items():
        print(f"N = {n:2d}: carga total = {qt*1e3:.3f} mW ; vida del criogeno = {y:.3f} anios")
    for n in (1, 3, 10):
        assert abs(r["q"][n] * (n + 1) - r["q"][0]) < 1e-12
    assert r["vida"][40][1] > r["vida"][10][1] > r["vida"][0][1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
