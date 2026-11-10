#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C16: atmosfera de Titan (gravedad, altura de escala, densidad y columna).

Datos: ficha NASA/NSSDC de satelites saturnianos (Titan: radio 2575 km, masa 1345.5e20 kg, densidad media 1880 kg/m^3) y pagina NASA Science de Titan
(T de superficie -179 C = 94.15 K; ~95 % N2 y ~5 % CH4; presion "60 % mayor que la terrestre", sin valor absoluto), consulta 2026-11-09; G, k, N_A de NIST CODATA 2022.
La presion absoluta se DERIVA aqui: 1.6 veces 101325 Pa (la presion terrestre de referencia es un valor estandar no consultado) y es una ESTIMACION de la clase.
Modelo: g = GM/r^2; H = R T/(M g); rho = P M/(R T); columna = P/g. Supuestos: gas ideal, T uniforme en la baja atmosfera. Tolerancia: densidad media frente a masa/volumen, 1 %.
"""
import math, platform
G = 6.67430e-11
R = 1.380649e-23 * 6.02214076e23
m, r, rho_f = 1.3455e23, 2575.0e3, 1880.0
print(f"Python {platform.python_version()} (biblioteca estandar)")
V = 4 / 3 * math.pi * r ** 3
rho_c = m / V
print(f"Densidad media calculada = {rho_c:.1f} kg/m3 (ficha {rho_f}; dif. {abs(rho_c-rho_f)/rho_f*100:.2f} %)")
assert abs(rho_c - rho_f) / rho_f < 0.01
g = G * m / r ** 2
print(f"g = G M/r^2 = {g:.4f} m/s2 ; v_esc = {math.sqrt(2*G*m/r)/1e3:.3f} km/s")
M = 0.95 * 0.028014 + 0.05 * 0.016043
T = 94.15
P = 1.6 * 101325.0
H = R * T / (M * g) / 1e3
rho = P * M / (R * T)
print(f"M = {M*1e3:.2f} g/mol ; H = {H:.2f} km ; P (estimada) = {P:.0f} Pa ; rho(superficie) = {rho:.2f} kg/m3")
print(f"Columna P/g = {P/g:.0f} kg/m2 (Tierra: ~{101325/9.82:.0f} kg/m2, Marte {636/3.73:.0f} kg/m2)")
print(f"Razon H/radio = {H*1e3/r:.4f} (atmosfera extensa frente al cuerpo: Tierra {8.5/6371:.4f})")
# metano: mezcla 5 %: presion parcial y densidad parcial
pm = 0.05 * P
print(f"Presion parcial de metano (mezcla 5 % por volumen) = {pm:.0f} Pa ; fraccion de masa = {0.05*0.016043/M*100:.1f} %")
# balance radiativo con un albedo SINTETICO de 0.3 y S = 1361/9.58^2 (a de Saturno 9.58 UA = valor ilustrativo no consultado)
SIG = 5.670374419e-8
S = 1361.0 / 9.58 ** 2
Te = (S * (1 - 0.3) / (4 * SIG)) ** 0.25
print(f"S(Saturno) ~ {S:.2f} W/m2 (inverso del cuadrado) ; Te con albedo sintetico 0.3 = {Te:.1f} K -> Ts - Te = {T-Te:.1f} K (el valor depende del albedo sintetico)")
# prueba analitica: el cociente de alturas de escala entre dos gases en la misma atmosfera es el cociente inverso de masas
HN = R * T / (0.028014 * g); HC = R * T / (0.016043 * g)
assert math.isclose(HN / HC, 0.016043 / 0.028014, rel_tol=1e-12)
print(f"H(N2) = {HN/1e3:.2f} km ; H(CH4) = {HC/1e3:.2f} km (el metano, mas ligero, cae mas despacio con la altura si el gas se mezclara por separado)")
print("Pruebas superadas.")
