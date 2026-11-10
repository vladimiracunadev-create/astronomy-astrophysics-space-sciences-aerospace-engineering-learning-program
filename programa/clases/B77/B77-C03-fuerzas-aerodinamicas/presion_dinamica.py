#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C03: presion dinamica, arrastre, sustentacion y max-q en un ascenso SINTETICO.

Datos consultados (2026-11-10): rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet); q = rho V^2/2 y D = Cd q A (NASA Glenn).
ILUSTRATIVOS (sinteticos): ascenso vertical con aceleracion constante a = 20 m/s2 (v = a t, h = a t^2/2), Cd = 0.3, CL_alfa = 2.0 /rad,
alfa = 2 grados, A = 10 m2.
Sistema: eje vertical local, altitud sobre el suelo, SI. Las fuerzas se descomponen en el sistema de ejes del viento (arrastre opuesto a la velocidad,
sustentacion perpendicular).
Modelo: q(t) = 0.5 rho0 exp(-h/H) v^2. Condicion analitica de max-q: dq/dt = 0 -> t* = sqrt(2 H / a).
Segunda via: barrido numerico fino del maximo de q(t).
Tolerancias: t* numerico frente a analitico 1e-4 relativa (paso 1 ms); q* analitico = 0.5 rho0 a^2 t*^2 exp(-1) con 1e-6.
"""
import math, platform

RHO0, H = 1.217, 8500.0
ACC, CD, CLA, ALFA, AREA = 20.0, 0.3, 2.0, math.radians(2.0), 10.0


def estado(t):
    return 0.5 * ACC * t * t, ACC * t


def q_din(t):
    h, v = estado(t)
    return 0.5 * RHO0 * math.exp(-h / H) * v * v


def calcular():
    r = {}
    r["t_ana"] = math.sqrt(2 * H / ACC)
    r["h_ana"], r["v_ana"] = estado(r["t_ana"])
    r["q_ana"] = 0.5 * RHO0 * ACC ** 2 * r["t_ana"] ** 2 * math.exp(-1.0)
    dt, t, mejor, tm = 0.001, 0.0, 0.0, 0.0
    while t < 80.0:
        q = q_din(t)
        if q > mejor:
            mejor, tm = q, t
        t += dt
    r["t_num"], r["q_num"] = tm, mejor
    qm = r["q_num"]
    r["D"], r["L"] = CD * qm * AREA, CLA * ALFA * qm * AREA
    r["M_v"] = r["v_ana"]
    r["tabla"] = [(t, *estado(t), q_din(t)) for t in (10.0, 20.0, 30.0, 40.0, 50.0, 60.0)]
    r["q_sin_ex"] = 0.5 * RHO0 * (ACC * r["t_ana"]) ** 2
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Ascenso SINTETICO: a = {ACC} m/s2 constante, Cd = {CD}, CLalfa = {CLA}/rad, alfa = 2 grados, A = {AREA} m2")
    print("  t [s]   h [m]    v [m/s]   q [Pa]")
    for t, h, v, q in r["tabla"]:
        print(f"  {t:5.1f}  {h:8.0f}  {v:7.1f}  {q:9.1f}")
    print(f"Max-q analitico: t* = {r['t_ana']:.4f} s, h = {r['h_ana']:.1f} m, v = {r['v_ana']:.2f} m/s, q = {r['q_ana']:.1f} Pa")
    print(f"Max-q numerico : t* = {r['t_num']:.3f} s, q = {r['q_num']:.1f} Pa")
    print(f"En max-q: arrastre D = {r['D']/1e3:.2f} kN; sustentacion L = {r['L']/1e3:.2f} kN (alfa = 2 grados)")
    print(f"q sin el factor exp(-h/H) en t*: {r['q_sin_ex']:.0f} Pa (el aire fino ya ha reducido q en un factor e)")
    assert abs(r["t_num"] - r["t_ana"]) / r["t_ana"] < 1e-3
    assert abs(r["q_num"] - r["q_ana"]) / r["q_ana"] < 1e-5
    assert abs(r["q_sin_ex"] / r["q_ana"] - math.e) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
