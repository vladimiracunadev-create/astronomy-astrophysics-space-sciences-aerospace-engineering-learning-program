#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C08: enfriamiento de primer orden de un detector y su efecto en la corriente oscura.

Datos: k_B en eV/K de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). Capacidad termica (200 J/K), conductancia (0,5 W/K), potencia de enfriamiento (30 W),
temperatura ambiente (293 K) y parametros de la ley oscura son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: C dT/dt = -G (T - Ta) - Q; solucion analitica T(t) = T_inf + (Ta - T_inf) exp(-t/tau), con T_inf = Ta - Q/G y tau = C/G; integracion numerica de Euler (paso pequeno) y de Runge-Kutta 4.
Supuestos: una sola masa termica, Q constante hasta el limite del enfriador. Validez: ilustrativa.
Tolerancia: RK4 frente a la solucion analitica a 1e-6 K; Euler a 0,05 K.
"""
from __future__ import annotations
import math, platform, sys

KB_EV = 8.617333262e-5
C_, G, Q, TA = 200.0, 0.5, 30.0, 293.0
EA, T0 = 0.60, 293.0

def dark(t):
    return (t / T0) ** 1.5 * math.exp(-EA / KB_EV * (1 / t - 1 / T0))

def f(T):
    return (-G * (T - TA) - Q) / C_

def exacta(t):
    tinf = TA - Q / G
    return tinf + (TA - tinf) * math.exp(-t * G / C_)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    tau = C_ / G
    print(f"constante de tiempo tau = {tau:.1f} s ; temperatura limite = {TA - Q/G:.1f} K")
    dt = 0.5
    Te = Tr = TA
    print(f"{'t [s]':>7} {'exacta [K]':>11} {'Euler [K]':>10} {'RK4 [K]':>10} {'D/D(293 K)':>11}")
    t = 0.0
    marcas = {200, 400, 800, 1600, 3200}
    maxe = maxr = 0.0
    while t < 3200 - 1e-9:
        Te += dt * f(Te)
        k1 = f(Tr); k2 = f(Tr + 0.5 * dt * k1); k3 = f(Tr + 0.5 * dt * k2); k4 = f(Tr + dt * k3)
        Tr += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
        maxe = max(maxe, abs(Te - exacta(t)))
        maxr = max(maxr, abs(Tr - exacta(t)))
        if round(t) in marcas and abs(t - round(t)) < 1e-9:
            print(f"{t:7.0f} {exacta(t):11.4f} {Te:10.4f} {Tr:10.4f} {dark(Tr):11.5f}")
            marcas.discard(round(t))
    print(f"error maximo: Euler {maxe:.5f} K ; RK4 {maxr:.2e} K")
    assert maxr < 1e-6 and maxe < 0.05
    t90 = -tau * math.log(0.1)
    print(f"tiempo para recorrer el 90 % del descenso: {t90:.0f} s")
    assert abs(exacta(t90) - (TA - 0.9 * Q / G)) < 1e-9
    assert dark(exacta(3200)) < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
