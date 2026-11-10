#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C15: atmosfera de Jupiter (altura de escala, balance de energia y adiabata profunda).

Datos: ficha NASA/NSSDC de Jupiter (T a 1 bar = 165 K, H = 27 km, g = 25.92 m/s^2 a 1 bar, 89.8 % H2 y 10.2 % He por volumen, albedo de Bond 0.343,
S = 50.26 W/m^2, T_bb = 109.9 K; consulta 2026-11-09); k, N_A, sigma de NIST CODATA 2022. kappa = 2/7 (gas diatomico rigido) es SUPUESTO de la clase.
Modelo: H = R T/(M g); T_eq desde el balance solar; adiabata T = T1 (P/P1)^kappa por debajo de 1 bar.
Supuestos: H2/He ideal, sin condensados ni cambios de calor especifico con T. No se usa el flujo interno medido (no consultado). Tolerancia: H frente a la ficha 15 %; T_eq frente a T_bb 0.3 K.
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
SIG = 5.670374419e-8
M = (0.898 * 2.016 + 0.102 * 4.0026) / 1000
print(f"Python {platform.python_version()} (biblioteca estandar)")
print(f"M = {M*1e3:.3f} g/mol")
for g, tag in ((25.92, "g de la ficha (1 bar)"), (24.79, "g de GM/r^2 con masa y radio ecuatorial")):
    H = R * 165.0 / (M * g) / 1e3
    print(f"H(165 K), {tag}: {H:.2f} km (ficha 27 km; dif. {abs(H-27)/27*100:.1f} %)")
assert abs(R * 165.0 / (M * 25.92) / 1e3 - 27.0) / 27.0 < 0.15
S, A = 50.26, 0.343
Te = (S * (1 - A) / (4 * SIG)) ** 0.25
print(f"T_eq solar = {Te:.2f} K (ficha 109.9 K); T a 1 bar = 165 K -> exceso {165.0-Te:.1f} K")
assert abs(Te - 109.9) < 0.3
print(f"Flujo solar absorbido promedio = {S*(1-A)/4:.3f} W/m2 ; sigma T(1 bar)^4 = {SIG*165.0**4:.1f} W/m2 (no es el flujo emergente)")
kappa = 2 / 7
print("P [bar]   T adiabatica [K]   z bajo 1 bar [km]")
Cp = 3.5 * R / M   # J/kg/K para kappa = 2/7
g = 25.92
for P in (1.0, 2.0, 5.0, 10.0, 20.0):
    T = 165.0 * P ** kappa
    z = Cp * (T - 165.0) / g / 1e3     # altura equivalente: dz = cp dT/g
    print(f"{P:7.1f} {T:17.1f} {z:17.1f}")
# integracion RK4 de dT/dlnP = kappa T hasta 10 bar frente a la formula
lnP, T, n = 0.0, 165.0, 10000
h = math.log(10.0) / n
f = lambda lp, T: kappa * T
for _ in range(n):
    k1 = f(lnP, T); k2 = f(lnP + h/2, T + h*k1/2); k3 = f(lnP + h/2, T + h*k2/2); k4 = f(lnP + h, T + h*k3)
    T += h*(k1 + 2*k2 + 2*k3 + k4)/6; lnP += h
ex = 165.0 * 10.0 ** kappa
print(f"A 10 bar: RK4 = {T:.4f} K ; analitica = {ex:.4f} K")
assert abs(T - ex) / ex < 1e-9
print(f"Gradiente adiabatico en 1 bar: g/cp = {g/Cp*1e3:.2f} K/km (cp = {Cp:.0f} J/kg/K)")
print("Pruebas superadas.")
