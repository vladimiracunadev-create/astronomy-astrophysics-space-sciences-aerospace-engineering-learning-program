#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C05: flujo compresible isentropico de un gas ideal - propiedades estaticas/totales y error de Bernoulli.

Consultado (2026-11-10): NASA Glenn, relaciones isentropicas p/pt, T/Tt, rho/rhot en funcion de M y gamma.
ILUSTRATIVOS: aire con gamma = 1.4 y R = 287.05 J/(kg K) (valores de uso comun, no consultados); T0 = 300 K, p0 = 101325 Pa.
Via 1: formulas cerradas de la pagina de NASA Glenn.
Via 2: balance de energia cp T + V^2/2 = cp T0 con V = M sqrt(gamma R T), resuelto por iteracion de punto fijo, y p/p0 = (T/T0)^(gamma/(gamma-1)).
Via 3 (error de Bernoulli): (p0 - p)/(0.5 rho V^2) con rho local frente a su valor incompresible 1.
Tolerancias: via 2 frente a via 1 < 1e-10 relativa; expansion en serie 1 + M^2/4 + (2-gamma) M^4/24 con 1e-3 a M = 0.3.
"""
import math, platform

GAM, R, T0, P0 = 1.4, 287.05, 300.0, 101325.0
CP = GAM * R / (GAM - 1)


def cerradas(M):
    f = 1 + 0.5 * (GAM - 1) * M * M
    return f ** -1, f ** (-GAM / (GAM - 1)), f ** (-1 / (GAM - 1))


def energia(M):
    t = T0
    for _ in range(200):
        v = M * math.sqrt(GAM * R * t)
        t = T0 - v * v / (2 * CP)
    return t / T0, (t / T0) ** (GAM / (GAM - 1))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Aire ILUSTRATIVO: gamma = {GAM}, R = {R} J/(kg K), T0 = {T0} K, p0 = {P0:.0f} Pa, a0 = {math.sqrt(GAM * R * T0):.2f} m/s")
    print("   M     T/T0      p/p0      rho/rho0   V [m/s]   (p0-p)/(q)   error Bernoulli [%]")
    peor = 0.0
    for M in (0.1, 0.3, 0.5, 0.8, 1.0, 2.0):
        tt, pp, rr = cerradas(M)
        t2, p2 = energia(M)
        peor = max(peor, abs(t2 - tt) / tt, abs(p2 - pp) / pp)
        a = math.sqrt(GAM * R * T0 * tt)
        v = M * a
        rho = P0 * pp / (R * T0 * tt)
        q = 0.5 * rho * v * v
        ratio = P0 * (1 - pp) / q
        print(f" {M:4.1f}   {tt:.5f}   {pp:.5f}   {rr:.5f}   {v:8.2f}    {ratio:.5f}      {100 * (ratio - 1):7.3f}")
    print(f"Diferencia maxima entre vias (T y p) = {peor:.2e}")
    # serie para M = 0.3
    M = 0.3
    tt, pp, rr = cerradas(M)
    rho = P0 * pp / (R * T0 * tt)
    v = M * math.sqrt(GAM * R * T0 * tt)
    ratio = P0 * (1 - pp) / (0.5 * rho * v * v)
    # relacion con la presion total: p0 - p frente a 0.5 gamma p M^2
    p = P0 * pp
    ratio2 = (P0 - p) / (0.5 * GAM * p * M * M)
    serie = 1 + M * M / 4 + (2 - GAM) * M ** 4 / 24
    print(f"A M = 0.3: (p0 - p)/(0.5 gamma p M^2) = {ratio2:.6f} ; serie 1 + M^2/4 + (2-gamma) M^4/24 = {serie:.6f}")
    print(f"Variacion de densidad a M = 0.3: {100 * (1 - rr):.2f} % ; a M = 0.1: {100 * (1 - cerradas(0.1)[2]):.2f} %")
    assert peor < 1e-10
    assert abs(ratio2 - serie) < 1e-3
    assert abs(ratio - ratio2) < 1e-12
    print("Pruebas superadas.")


main()
