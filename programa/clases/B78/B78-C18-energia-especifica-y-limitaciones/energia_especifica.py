#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C18: energia especifica requerida por un Isp y limites de energia frente a limites de potencia.

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); Dawn (NASA/JPL): 91 mN y 3.25 mg/s (-> Veq = 28000 m/s).
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): calor de combustion H2/O2 = 241.8 kJ por mol de H2O (18.015 g/mol);
energia especifica de una bateria de iones de litio 200 Wh/kg; D-T = 3.376e14 J/kg (calculado en C16 con valores de manual).
ILUSTRATIVOS: eficiencia de conversion del calor/energia en energia cinetica del chorro eta = 0.6 (electrico) y 1.0 (cota quimica ideal).
Modelo: la energia cinetica por kg de propelente es Ve^2/2; la fuente debe aportar eps_req = Ve^2/(2 eta) por kg de propelente.
Un propulsor es ENERGETICAMENTE POSIBLE con una fuente de energia especifica eps si eps >= eps_req (cuando la energia sale del propelente).
Segunda via: Ve_max = sqrt(2 eta eps) y su inversa eps_req(Ve_max) = eps con 1e-12.
Tolerancia: ida y vuelta Ve <-> eps a 1e-12.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
EPS = {"H2/O2 quimica": 241.8e3 / 18.015e-3, "bateria Li-ion": 200 * 3600.0, "D-T (de C16)": 3.376e14}


def eps_req(ve, eta):
    return ve ** 2 / (2 * eta)


def ve_max(eps, eta):
    return math.sqrt(2 * eta * eps)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Energia especifica de las fuentes (valores de manual no consultados):")
    for n, e in EPS.items():
        print(f"  {n:<16} {e:.3e} J/kg")
    print("Cota de escape de las fuentes si la energia sale del propio propelente (eta = 1 cota quimica; 0.6 = ILUSTRATIVA):")
    for n, e in EPS.items():
        for eta in (1.0, 0.6):
            v = ve_max(e, eta)
            assert abs(eps_req(v, eta) - e) / e < 1e-12
            print(f"  {n:<16} eta = {eta:.1f}: Ve_max = {v:>11.1f} m/s ; Isp = {v/G0:>10.1f} s")
    print("Energia requerida por Isp (eta = 0.6) y comparacion con la quimica H2/O2:")
    print("  Isp [s]    eps_req [J/kg]   eps_req/eps_quimica   posible solo con energia quimica")
    for isp in (300.0, 450.0, 1000.0, 2855.2, 5000.0):
        r = eps_req(isp * G0, 0.6)
        print(f"  {isp:>7.1f} {r:>16.3e} {r/EPS['H2/O2 quimica']:>20.2f}   {'si' if r <= EPS['H2/O2 quimica'] else 'NO'}")
    ve_dawn = 0.091 / 3.25e-6
    r_dawn = eps_req(ve_dawn, 0.6)
    print(f"Dawn (F y mdot consultados): Veq = {ve_dawn:.0f} m/s -> eps_req = {r_dawn:.3e} J/kg = {r_dawn/EPS['H2/O2 quimica']:.1f} veces la quimica: la energia NO sale del propelente")
    assert r_dawn > EPS["H2/O2 quimica"]
    # limite de energia de una bateria: Ve maximo con fraccion de bateria
    print("Propulsor alimentado por BATERIA (limite de energia), eta = 0.6, fraccion de propelente 0.3 de m0:")
    for fb in (0.1, 0.3, 0.5):
        fp = 0.3
        ve2 = 2 * 0.6 * EPS["bateria Li-ion"] * fb / fp
        print(f"  fraccion de bateria {fb:.1f}: Ve = {math.sqrt(ve2):>7.1f} m/s ; Isp = {math.sqrt(ve2)/G0:>6.1f} s ; dv = {math.sqrt(ve2)*math.log(1/(1-fp)):>6.1f} m/s")
    # limite de potencia: misma energia a lo largo de un tiempo
    print("Limite de POTENCIA (P fija): F = 2 eta P/Ve, sin tope de energia si la fuente es continua (solar, reactor):")
    for ve in (10000.0, 28000.0):
        print(f"  Ve = {ve:>6.0f} m/s con P = 2 kW, eta = 0.6 -> F = {2*0.6*2000/ve*1e3:>6.1f} mN")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
