#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C03: escalado Arrhenius de las tasas metabolicas hacia temperaturas bajo cero.

Datos: SINTETICOS. Se toma como parametro ilustrativo la energia de activacion de unos 110 kJ que Price y Sowers 2004
(resumen consultado el 2026-11-09, Europe PMC) senalan como comun a crecimiento, mantenimiento y supervivencia, y la
razon aproximada 10^6 : 10^3 : 1 entre esas tres categorias. Las tasas absolutas aqui son propuestas, NO medidas.
Constantes: R = 8.314462618 J/(mol K) (CODATA 2022, NIST, consultado 2026-11-09).
Modelo: k(T) = k_ref exp(-Ea/R (1/T - 1/T_ref)), T en kelvin, T_ref = 298.15 K (25 C). Q10(T) = k(T+10)/k(T).
Se comprueba (1) que el ajuste de Arrhenius de datos sinteticos con ruido recupere Ea; (2) que Q10 coincida con la
forma cerrada exp(Ea/R (1/T - 1/(T+10))); (3) el calculo de tiempo de renovacion con una segunda via (producto de factores
por tramos de 5 K).
Supuestos: Arrhenius valido en todo el intervalo (hipotesis fuerte: la membrana y las proteinas reales se desvian); agua
liquida disponible (salmuera en vetas); sin congelacion intracelular. Validez: ilustrativa.
Tolerancias: Ea recuperada a 2 %; Q10 a 1e-12 relativo; producto por tramos a 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, random

R = 8.314462618
EA = 110e3          # J/mol (valor del resumen de Price y Sowers 2004, usado como parametro)
TREF = 298.15


def k_rel(Tc, Ea=EA):
    T = Tc + 273.15
    return math.exp(-Ea / R * (1 / T - 1 / TREF))


def q10(Tc, Ea=EA):
    return math.exp(Ea / R * (1 / (Tc + 273.15) - 1 / (Tc + 283.15)))


def ajuste(xs, ys):
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n
    m = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    return m, my - m * mx


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Ea (parametro) = {EA / 1000:.0f} kJ/mol ; T_ref = {TREF} K")
    print(f"{'T [C]':>7} {'k/k(25C)':>12} {'Q10':>7} {'factor de lentitud':>20}")
    for Tc in (25, 4, 0, -10, -20, -40):
        print(f"{Tc:7d} {k_rel(Tc):12.3e} {q10(Tc):7.2f} {1 / k_rel(Tc):20.3e}")
    # ajuste con ruido
    rng = random.Random(20261109)
    temps = [-40, -30, -20, -10, 0, 5, 10, 15, 20, 25]
    ys = [math.log(k_rel(t)) + rng.gauss(0, 0.05) for t in temps]
    xs = [1.0 / (t + 273.15) for t in temps]
    m, b = ajuste(xs, ys)
    Ea_fit = -m * R
    print(f"Ea recuperada de datos sinteticos con ruido (sigma ln k = 0.05): {Ea_fit / 1000:.1f} kJ/mol")
    assert abs(Ea_fit - EA) / EA < 0.02
    # Q10 vs forma cerrada por diferencia
    for Tc in (-40, -10, 5, 25):
        q_num = k_rel(Tc + 10) / k_rel(Tc)
        assert abs(q_num - q10(Tc)) / q10(Tc) < 1e-12
    # categorias (razon 10^6 : 10^3 : 1 del resumen) y renovacion de carbono
    print("Categorias (razon 1e6 : 1e3 : 1 segun el resumen consultado): crecimiento / mantenimiento / supervivencia")
    t_ren_25 = 1.0 / 24.0 / 365.25    # a 25 C, tiempo de renovacion de 1 h -> en anios (SINTETICO, supuesto del ejemplo)
    for Tc in (25, 0, -20, -40):
        for nombre, fac in (("crecimiento", 1.0), ("mantenimiento", 1e-3), ("supervivencia", 1e-6)):
            t = t_ren_25 / (k_rel(Tc) * fac)
            print(f"  {Tc:4d} C {nombre:>14}: renovacion = {t:10.3e} anios")
    # segunda via: producto por tramos de 5 K desde 25 C hasta -40 C
    factor = 1.0
    T = 25.0
    while T > -40.0 + 1e-9:
        factor *= k_rel(T - 5) / k_rel(T)
        T -= 5
    assert abs(factor - k_rel(-40.0)) / k_rel(-40.0) < 1e-9
    print(f"Producto de factores por tramos de 5 K = {factor:.3e} ; directo = {k_rel(-40):.3e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
