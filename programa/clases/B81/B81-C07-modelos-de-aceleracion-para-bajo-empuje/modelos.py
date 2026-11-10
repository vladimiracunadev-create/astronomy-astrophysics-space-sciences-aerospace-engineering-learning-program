#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C07: tres modelos de aceleracion de bajo empuje para una transferencia circular heliocentrica coplanar.

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y UA = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10); g0 = 9,80665 m/s^2 (convencional, no consultado).
Orbitas circulares de 1,0 UA a 1,5 UA (radio final ILUSTRATIVO, no un planeta concreto). Empuje tangencial.
Parametros ILUSTRATIVOS (sinteticos): aceleracion inicial a0 = 2e-4 m/s^2 a 1 UA, masa inicial 1000 kg, Isp 3000 s.
Modelos: (A) aceleracion constante a0; (B) empuje constante T = m0 a0 con masa decreciente (mdot = T/(g0 Isp)); (C) potencia solar: aceleracion a0 (1 UA/r)^2 con masa constante.
Promediado tangencial: da/dt = 2 a_t sqrt(a^3/mu) con a = radio de la orbita casi circular; dv ideal = |v0 - v1|.
Analiticos: (A) t = dv/a0; (B) t = (m0/mdot)(1 - exp(-dv/ve)), ve = g0 Isp. Para (C) no hay cierre simple; segunda via: integracion con DOP853 de la ecuacion en velocidad
dv/dt = a0 (1UA/r)^2 con r(v) circular, r = mu/v^2.
Tolerancias: A y B numericos frente a analiticos < 1e-6 relativo; C por dos integraciones < 1e-6 relativo.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp

MU = 132712440041.279419
AU = 149597870.7
G0 = 9.80665
A0, M0, ISP = 2e-4, 1000.0, 3000.0   # m/s^2, kg, s


def tiempo(modelo):
    r0, r1 = AU, 1.5 * AU
    mu = MU * 1e9  # m^3/s^2
    a0m, a1m = r0 * 1e3, r1 * 1e3

    def f(t, y):
        a, m = y
        r_ua = a / (AU * 1e3)
        if modelo == "A":
            at = A0
        elif modelo == "B":
            at = A0 * M0 / m
        else:
            at = A0 / r_ua**2
        mdot = -(A0 * M0) / (G0 * ISP) if modelo == "B" else 0.0
        return [2 * at * math.sqrt(a**3 / mu), mdot]

    ev = lambda t, y: y[0] - a1m
    ev.terminal = True
    s = solve_ivp(f, (0, 3e9), [a0m, M0], method="DOP853", rtol=1e-12, atol=1e-6, events=ev)
    return s.t_events[0][0], s.y_events[0][0][1]


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    v0 = math.sqrt(MU / AU) * 1e3
    v1 = math.sqrt(MU / (1.5 * AU)) * 1e3
    dv = v0 - v1
    print(f"Orbitas circulares 1,0 -> 1,5 UA ; v0 = {v0:.2f} m/s, v1 = {v1:.2f} m/s ; dv ideal = {dv:.2f} m/s")
    print(f"Parametros ILUSTRATIVOS: a0 = {A0:.1e} m/s^2 a 1 UA, m0 = {M0:.0f} kg, Isp = {ISP:.0f} s")
    ve = G0 * ISP
    mdot = A0 * M0 / ve
    tA, mA = tiempo("A"); tB, mB = tiempo("B"); tC, mC = tiempo("C")
    tA_an = dv / A0
    tB_an = (M0 / mdot) * (1 - math.exp(-dv / ve))
    print(" modelo                 tiempo [d]   analitico [d]   dif. relativa   masa final [kg]")
    print(f" A aceleracion const.   {tA/86400:10.3f}   {tA_an/86400:12.3f}   {abs(tA-tA_an)/tA_an:12.2e}   {M0:8.1f}")
    print(f" B empuje const.        {tB/86400:10.3f}   {tB_an/86400:12.3f}   {abs(tB-tB_an)/tB_an:12.2e}   {mB:8.1f}")
    # segunda via de C: dv/dt = A0 (1/r_ua)^2, r = mu/v^2
    def fv(t, y):
        v = y[0]
        r_ua = (MU * 1e9 / v**2) / (AU * 1e3)
        return [-A0 / r_ua**2]
    ev = lambda t, y: y[0] - v1
    ev.terminal = True
    s = solve_ivp(fv, (0, 3e9), [v0], method="DOP853", rtol=1e-12, atol=1e-9, events=ev)
    tC2 = s.t_events[0][0]
    print(f" C potencia solar 1/r^2 {tC/86400:10.3f}   (2a via {tC2/86400:.3f})   {abs(tC-tC2)/tC2:12.2e}   {M0:8.1f}")
    print(f"Propelente consumido en B = {M0 - mB:.2f} kg ; con la ecuacion del cohete: {M0*(1-math.exp(-dv/ve)):.2f} kg")
    print(f"Cociente t_C/t_A = {tC/tA:.3f} ; t_B/t_A = {tB/tA:.3f}")
    assert abs(tA - tA_an) / tA_an < 1e-6 and abs(tB - tB_an) / tB_an < 1e-6 and abs(tC - tC2) / tC2 < 1e-6
    assert abs((M0 - mB) - M0 * (1 - math.exp(-dv / ve))) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
