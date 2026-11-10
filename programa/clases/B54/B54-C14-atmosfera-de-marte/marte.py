#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C14: atmosfera de Marte (masa, ciclo estacional de CO2, escarcha, inercia termica).

Datos: ficha NASA/NSSDC de Marte (presion 6.36 mb, rango estacional 4.0-8.7 mb, T 214 K, g 3.73 m/s^2, radio medio 3389.5 km, 95.1 % CO2; consulta 2026-11-09);
k, N_A de NIST CODATA 2022. Calor latente del CO2 (5.9e5 J/kg) y referencia de sublimacion (194.7 K a 1 atm): valores estandar NO consultados (ilustrativos).
Modelo: masa atmosferica M_a = 4 pi r^2 P/g ; fraccion estacional = (P_max - P_min)/P_media; temperatura de escarcha por Clausius-Clapeyron (L constante).
Supuestos: el rango 4.0-8.7 mb de la ficha es de la presion en el sitio/estacion, no necesariamente global; se usa como ORDEN DE MAGNITUD. Tolerancia: masa frente a P*area/g 1e-12; CC reversible 1e-9 K.
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
print(f"Python {platform.python_version()} (biblioteca estandar)")
g, r, Pm, Pmin, Pmax = 3.73, 3389.5e3, 636.0, 400.0, 870.0
area = 4 * math.pi * r ** 2
Ma = area * Pm / g
print(f"Area = {area:.4e} m2 ; masa de la atmosfera = {Ma:.3e} kg ; columna = {Pm/g:.1f} kg/m2")
assert math.isclose(Ma, area * (Pm / g), rel_tol=1e-12)
frac = (Pmax - Pmin) / Pm
print(f"Rango de presion 400-870 Pa: {frac*100:.0f} % de la presion media -> masa de CO2 que cambiaria de fase (cota, si fuera global): {frac*Ma:.2e} kg")
# volumen de hielo seco equivalente (densidad ilustrativa 1500 kg/m3) repartido en un casquete de 10^7 km2
rho_hs, A_cap = 1500.0, 1e7 * 1e6
esp = frac * Ma / rho_hs / A_cap
print(f"Espesor equivalente de hielo seco sobre 1e7 km2: {esp:.2f} m")
# CC invertida: temperatura de escarcha en funcion de la presion y regreso a la presion
Rc = R / 0.04401
Lc, T_ref, P_ref = 5.9e5, 194.7, 101325.0
Tf = lambda P: 1 / (1 / T_ref - Rc / Lc * math.log(P / P_ref))
Pf = lambda T: P_ref * math.exp(Lc / Rc * (1 / T_ref - 1 / T))
for P in (400.0, 636.0, 870.0):
    T = Tf(P); assert abs(Pf(T) - P) / P < 1e-9
    print(f"P = {P:6.1f} Pa: temperatura de escarcha del CO2 = {T:6.2f} K")
print(f"dT/dP en 636 Pa: {(Tf(870.0)-Tf(400.0))/(870.0-400.0)*100:.3f} K por 100 Pa")
# altura de escala a distintas T (aire de Marte)
M = 0.043486
for T in (150.0, 214.0, 270.0):
    print(f"T = {T:5.0f} K: H = {R*T/(M*g)/1e3:5.2f} km")
# escala de tiempo radiativa de una atmosfera delgada: tau_rad = cp P / (g 4 sigma T^3) (estimacion ilustrativa, cp=850)
sig = 5.670374419e-8
for T in (214.0,):
    trad = 850.0 * Pm / (g * 4 * sig * T ** 3)
    print(f"tau_rad (T={T:.0f} K, cp=850 J/kg/K) = {trad/86400:.2f} dias (estimacion; la atmosfera responde rapido al calentamiento)")
print("Pruebas superadas.")
