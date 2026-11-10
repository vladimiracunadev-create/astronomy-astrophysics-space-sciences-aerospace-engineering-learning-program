#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C02: Euler 1D estacionario en un conducto convergente-divergente (Venturi), incompresible.

Consultado (2026-11-10): NASA Glenn, las ecuaciones de Euler son Navier-Stokes sin terminos viscosos.
ILUSTRATIVOS (sinteticos, no medidos): A(x) = A1 (1 - 0.6 sin^2(pi x/L)) con A1 = 0.010 m2 y L = 1.0 m (garganta 0.004 m2 en x = L/2);
rho = 1000 kg/m3 (agua, ilustrativo), u1 = 2.0 m/s, p1 = 200000 Pa.
Modelo: continuidad u A = u1 A1 y momento u du/dx = -(1/rho) dp/dx.
Via 1: Bernoulli, p = p1 + 0.5 rho (u1^2 - u^2).
Via 2: integracion numerica (trapecio) de dp/dx = -rho u du/dx con du/dx por diferencias centrales en 4000 intervalos.
Tolerancia: diferencia maxima entre vias dividida por max|p - p1| < 1e-5; p(L) = p1 (sin perdidas, d'Alembert 1D).
"""
import math, platform

A1, L, RHO, U1, P1 = 0.010, 1.0, 1000.0, 2.0, 200000.0
N = 4000


def area(x):
    return A1 * (1 - 0.6 * math.sin(math.pi * x / L) ** 2)


def u_de(x):
    return U1 * A1 / area(x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h = L / N
    xs = [i * h for i in range(N + 1)]
    u = [u_de(x) for x in xs]
    dudx = [(u[1] - u[0]) / h] + [(u[i + 1] - u[i - 1]) / (2 * h) for i in range(1, N)] + [(u[N] - u[N - 1]) / h]
    p_num = [P1]
    for i in range(1, N + 1):
        f0 = -RHO * u[i - 1] * dudx[i - 1]
        f1 = -RHO * u[i] * dudx[i]
        p_num.append(p_num[-1] + 0.5 * h * (f0 + f1))
    p_ber = [P1 + 0.5 * RHO * (U1 ** 2 - ui ** 2) for ui in u]
    print("Venturi ILUSTRATIVO: A1 = 0.010 m2, garganta 0.004 m2, rho = 1000 kg/m3, u1 = 2 m/s, p1 = 200000 Pa")
    print("   x [m]   A [m2]    u [m/s]   p Bernoulli [Pa]   p numerico [Pa]   pt [Pa]")
    peor = 0.0
    for k in (0, 1000, 2000, 3000, 4000):
        pt = p_ber[k] + 0.5 * RHO * u[k] ** 2
        print(f"  {xs[k]:.2f}    {area(xs[k]):.5f}   {u[k]:7.3f}    {p_ber[k]:12.2f}      {p_num[k]:12.2f}   {pt:10.2f}")
    escala = max(abs(pb - P1) for pb in p_ber)
    peor = max(abs(p_num[k] - p_ber[k]) for k in range(N + 1)) / escala
    print(f"Diferencia maxima entre vias / max|p - p1| = {peor:.2e}")
    caida = P1 - p_ber[2000]
    print(f"Caida de presion a la garganta = {caida:.1f} Pa ; recuperacion en la salida: p(L) - p1 = {p_ber[N] - P1:.3e} Pa")
    # Venturi como medidor: u1 a partir de la caida
    r = (A1 / area(0.5 * L)) ** 2 - 1
    u1_med = math.sqrt(2 * caida / (RHO * r))
    print(f"u1 inferida de la caida de presion = {u1_med:.4f} m/s (dato: {U1})")
    assert peor < 1e-5
    assert abs(p_ber[N] - P1) < 1e-6
    assert abs(u1_med - U1) < 1e-9
    print("Pruebas superadas.")


main()
