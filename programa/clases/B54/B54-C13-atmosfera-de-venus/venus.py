#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C13: atmosfera de Venus (adiabata, escala de altura, gas ideal y masa).

Datos: ficha NASA/NSSDC de Venus (presion 92 bar, T 737 K, H 15.9 km, g 8.87 m/s^2, radio 6051.8 km, 96.5 % CO2 y 3.5 % N2; consulta 2026-11-09); k, N_A de NIST CODATA 2022.
cp(CO2) = 1100 J/(kg K) es un valor ILUSTRATIVO no consultado (a T alta, cp del CO2 no es constante: el resultado es una estimacion).
Modelo: adiabata seca T(P) = T0 (P/P0)^kappa ; altura por integracion hidrostatica con gas ideal; masa de la atmosfera = 4 pi r^2 P0 / g.
Supuestos: CO2 ideal con kappa constante (a 92 bar y 737 K la desviacion real es importante), sin nubes. Tolerancia: RK4 frente a analitica 1e-9; H calculada frente a la ficha 1 %.
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
M = 0.965 * 0.044009 + 0.035 * 0.028014
g, T0, P0, r, Hf = 8.87, 737.0, 92e5, 6051.8e3, 15.9
cp = 1100.0
kappa = R / (M * cp)
print(f"Python {platform.python_version()} (biblioteca estandar)")
print(f"M = {M*1e3:.3f} g/mol ; kappa = R/(M cp) = {kappa:.4f} ; Gamma_ad = g/cp = {g/cp*1e3:.2f} K/km")
H = R * T0 / (M * g) / 1e3
print(f"H(737 K) = {H:.2f} km (ficha {Hf} km, dif. {abs(H-Hf)/Hf*100:.2f} %)")
assert abs(H - Hf) / Hf < 0.01
# integracion hidrostatica con adiabata: dz = -(R T / (M g)) dP / P  -> altura en funcion de P
def altura(Pf, n=200000):
    P = P0; z = 0.0; T = T0
    lnP0, lnP1 = math.log(P0), math.log(Pf); h = (lnP1 - lnP0) / n
    f = lambda lp: -(R * T0 * math.exp(kappa * (lp - lnP0)) / (M * g))
    for i in range(n):
        lp = lnP0 + i * h
        z += h * (f(lp) + 4 * f(lp + h / 2) + f(lp + h)) / 6
    return z
print("P [bar]   T adiabatica [K]   z numerica [km]   z analitica [km]")
for Pb in (92.0, 50.0, 10.0, 1.0, 0.1):
    Pf = Pb * 1e5
    T = T0 * (Pf / P0) ** kappa
    z_num = altura(Pf) / 1e3
    z_an = (cp * T0 / g) * (1 - (Pf / P0) ** kappa) / 1e3
    print(f"{Pb:7.1f} {T:17.1f} {z_num:15.2f} {z_an:16.2f}")
    assert abs(z_num - z_an) < 1e-6 * max(1.0, z_an) + 1e-6
rho = P0 * M / (R * T0)
print(f"rho(superficie, gas ideal) = {rho:.2f} kg/m3 (ficha ~65)")
mass = 4 * math.pi * r ** 2 * P0 / g
print(f"Masa de la atmosfera = 4 pi r^2 P0/g = {mass:.3e} kg ; relativa a la terrestre (5.1e18 kg, valor ilustrativo no consultado): {mass/5.1e18:.0f}")
print(f"Altura isoterma ln(92) H = {H*math.log(92):.1f} km (cota: la adiabata es mas fria con la altura)")
print("Pruebas superadas.")
