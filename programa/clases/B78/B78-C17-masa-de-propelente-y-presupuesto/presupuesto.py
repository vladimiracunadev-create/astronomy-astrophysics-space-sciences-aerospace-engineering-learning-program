#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C17: presupuesto de masa de una mision con propulsion quimica o electrica (acoplamiento propelente-planta de potencia).

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); rangos de Isp de la NASA SSVI (Tabla 4-1): bipropelentes/monopropelentes alternativos 150-310 s;
Hall 200-1920 s; gridded ion 500-3000 s.
ILUSTRATIVOS (sinteticos, no de una mision): masa de bus + carga util 400 kg; fraccion de tanques 10 % (quimica) y 8 % (electrica) de la masa de propelente;
margen de Delta-v 10 %; residuo no utilizable 2 % del propelente; Isp quimico 300 s; Isp electrico 2500 s; eficiencia 0.6; masa especifica de la planta de potencia 25 kg/kW;
tiempo de empuje 200 dias (electrico); Delta-v nominal 2000 m/s.
Modelo: m_f = bus + k m_p + (planta) ; m_p = (1+residuo)(m_f)(exp(dv_margen/Ve) - 1) ; P = m_p Ve^2/(2 eta t) ; planta = alpha P. Acoplamiento resuelto por iteracion de punto fijo.
Segunda via: biseccion sobre m_p del residuo de la ecuacion acoplada.
Tolerancia: punto fijo y biseccion coinciden a 1e-9 relativa.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
BUS = 400.0
RESIDUO, MARGEN = 0.02, 0.10


def residuo_ec(mp, ve, k, dv, alpha=0.0, eta=0.6, t=1.0):
    p = mp * ve ** 2 / (2 * eta * t) if alpha else 0.0
    mf = BUS + k * mp + alpha * p
    return mp - (1 + RESIDUO) * mf * (math.exp(dv * (1 + MARGEN) / ve) - 1)


def resolver_punto_fijo(ve, k, dv, alpha=0.0, eta=0.6, t=1.0):
    mp = 0.0
    for _ in range(100000):
        p = mp * ve ** 2 / (2 * eta * t) if alpha else 0.0
        mf = BUS + k * mp + alpha * p
        nuevo = (1 + RESIDUO) * mf * (math.exp(dv * (1 + MARGEN) / ve) - 1)
        if abs(nuevo - mp) < 1e-13 * max(1.0, nuevo):
            return nuevo
        mp = nuevo
    raise RuntimeError("sin convergencia")


def resolver_biseccion(ve, k, dv, alpha=0.0, eta=0.6, t=1.0):
    lo, hi = 0.0, 1e6
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if residuo_ec(mid, ve, k, dv, alpha, eta, t) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def caso(nombre, isp, k, dv, alpha=0.0, t=1.0):
    ve = isp * G0
    a = resolver_punto_fijo(ve, k, dv, alpha, 0.6, t)
    b = resolver_biseccion(ve, k, dv, alpha, 0.6, t)
    assert abs(a - b) / a < 1e-9, (a, b)
    p = a * ve ** 2 / (2 * 0.6 * t) if alpha else 0.0
    planta = alpha * p
    tanques = k * a
    total = BUS + tanques + planta + a
    return a, p, planta, tanques, total


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    t = 200 * 86400.0
    print(f"Mision ILUSTRATIVA: bus + carga util {BUS:.0f} kg ; margen de dv {MARGEN*100:.0f} % ; residuo {RESIDUO*100:.0f} % ; dv nominal 2000 m/s")
    print(" opcion      Isp [s]  m_prop [kg]  P [kW]  planta [kg]  tanques [kg]  masa total [kg]  prop/total")
    filas = {}
    for nombre, isp, k, alpha, tt in (("quimica", 300.0, 0.10, 0.0, 1.0), ("electrica", 2500.0, 0.08, 25.0 / 1000, t)):
        a, p, planta, tanques, total = caso(nombre, isp, k, 2000.0, alpha, tt)
        filas[nombre] = total
        print(f" {nombre:<10} {isp:>7.0f} {a:>12.2f} {p/1e3:>7.2f} {planta:>12.2f} {tanques:>13.2f} {total:>16.2f} {a/total:>11.3f}")
    print("Masa total frente al delta-v nominal (quimica / electrica):")
    menor = True
    for dv in (500.0, 1000.0, 2000.0, 3000.0, 4000.0, 6000.0):
        q = caso("q", 300.0, 0.10, dv)[4]
        e = caso("e", 2500.0, 0.08, dv, 25.0 / 1000, t)[4]
        menor = menor and e < q
        print(f"  dv = {dv:>5.0f} m/s -> {q:>9.1f} kg / {e:>9.1f} kg ; cociente quimica/electrica = {q/e:.2f}")
    print(f"Con estos parametros ILUSTRATIVOS la electrica pesa menos en todos los dv de la tabla: {menor} (no incluye tiempo de maniobra ni costo)")
    # sensibilidad al margen: sin margen ni residuo
    print("Sensibilidad del propelente quimico (dv nominal 2000 m/s):")
    for etiqueta, mar, res in (("con margen 10 % y residuo 2 %", 0.10, 0.02), ("sin margen ni residuo", 0.0, 0.0)):
        globals()["MARGEN"], globals()["RESIDUO"] = mar, res
        print(f"  {etiqueta}: m_prop = {resolver_punto_fijo(300.0*G0, 0.10, 2000.0):.2f} kg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
