#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C04: presion, densidad y ley de gas ideal en tres atmosferas.

Datos: presion superficial, T, masa molar derivada de la composicion y densidad superficial de las fichas NASA/NSSDC (consulta 2026-11-09);
k y N_A de NIST CODATA 2022. Masas molares: valores estandar redondeados, no consultados en esta clase.
Modelo: rho = P M / (R T) (gas ideal); atmosfera isoterma P(z) = P0 exp(-z/H) con H = R T/(M g).
Supuestos: gas ideal (en Venus, a 92 bar y 737 K, es una aproximacion que se cuantifica). Validez: capa baja y bien mezclada.
Tolerancia: rho calculada frente a la ficha, 5 %; integracion RK4 frente a la exponencial, 1e-8 relativo.
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
D = {  # P0 [Pa], T [K], M [kg/mol], g [m/s2], rho ficha [kg/m3]
    "Tierra": (101400.0, 288.0, 0.028967, 9.820, 1.217),
    "Venus": (92e5, 737.0, 0.043449, 8.87, 65.0),
    "Marte": (636.0, 214.0, 0.043486, 3.73, 0.016)}
print(f"Python {platform.python_version()} (biblioteca estandar)")
print("planeta   rho calc [kg/m3]   rho ficha   dif.    H [km]   Z=P/(rho R T / M) implicito")
for n, (P0, T, M, g, rf) in D.items():
    rho = P0 * M / (R * T)
    d = abs(rho - rf) / rf
    H = R * T / (M * g) / 1e3
    assert d < 0.05, (n, rho, rf)
    print(f"{n:8s} {rho:14.4f} {rf:12.4f} {d*100:6.1f} % {H:9.2f}")
# integracion hidrostatica RK4 isoterma frente a exponencial
P0, T, M, g, _ = D["Marte"]
H = R * T / (M * g)
f = lambda z, P: -P / H
n_, z_fin = 4000, 30000.0
h, z, P = z_fin / n_, 0.0, P0
for _ in range(n_):
    k1 = f(z, P); k2 = f(z + h/2, P + h*k1/2); k3 = f(z + h/2, P + h*k2/2); k4 = f(z + h, P + h*k3)
    P += h*(k1 + 2*k2 + 2*k3 + k4)/6; z += h
ex = P0 * math.exp(-z_fin / H)
print(f"Marte a 30 km: RK4 = {P:.6f} Pa ; analitica = {ex:.6f} Pa ; dif. rel. = {abs(P-ex)/ex:.1e}")
assert abs(P - ex) / ex < 1e-8
# peso de la columna: P0 = masa de columna * g
for n, (P0, T, M, g, _) in D.items():
    print(f"{n:8s} masa de columna = P0/g = {P0/g:12.1f} kg/m2")
# altura a la que P cae a 1/e y a 1/1000
Pk = D["Tierra"]
print(f"Tierra: P = P0/e a {R*Pk[1]/(Pk[2]*Pk[3])/1e3:.2f} km ; P = P0/1000 a {R*Pk[1]/(Pk[2]*Pk[3])*math.log(1000)/1e3:.1f} km (isoterma)")
print("Pruebas superadas.")
