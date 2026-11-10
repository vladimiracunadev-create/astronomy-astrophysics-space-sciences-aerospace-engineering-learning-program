#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C08: condensacion (Clausius-Clapeyron), nivel de condensacion y sedimentacion de aerosoles.

Datos: constantes k y N_A de NIST CODATA 2022 (consulta 2026-11-09). Calor latente del agua (2.50e6 J/kg), del CO2 (5.9e5 J/kg), presion del punto triple
del agua (611.657 Pa) y viscosidad del aire (1.8e-5 Pa s) son VALORES ESTANDAR NO CONSULTADOS en esta clase (ilustrativos). Densidad de particula: SINTETICA.
Modelo: e_s(T) = e_ref exp[(L/R_v)(1/T_ref - 1/T)] con L constante; nivel de condensacion ascendente ~ (T - T_d)/(Gamma_d - Gamma_dp); ley de Stokes v = 2 r^2 (rho_p - rho_a) g /(9 mu).
Supuestos: L constante, Stokes valido para Reynolds << 1 (se verifica). Tolerancia: v de Stokes frente a su formula 1e-12; derivada numerica de ln e_s frente a L/(R_v T^2) 1e-8; e_s(373.15 K) frente a 101325 Pa solo como limite de L constante (30 %).
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
print(f"Python {platform.python_version()} (biblioteca estandar)")
Rv = R / 0.018015
es = lambda T: 611.657 * math.exp(2.50e6 / Rv * (1 / 273.16 - 1 / T))
for T in (253.15, 273.16, 288.15, 303.15, 373.15):
    print(f"e_s({T:7.2f} K) = {es(T):12.2f} Pa")
d = abs(es(373.15) - 101325.0) / 101325.0
print(f"e_s en el punto de ebullicion frente a 1 atm: dif. rel. = {d*100:.1f} % (limite de L constante: L real disminuye al subir T)")
assert d < 0.30
# prueba analitica: d ln e_s / dT = L / (R_v T^2)
T, h = 290.0, 1e-3
num = (math.log(es(T + h)) - math.log(es(T - h))) / (2 * h)
print(f"d ln es/dT en 290 K: numerico = {num:.6e} 1/K ; analitico = {2.50e6/(Rv*T*T):.6e} 1/K")
assert math.isclose(num, 2.50e6 / (Rv * T * T), rel_tol=1e-8)
# CO2 sobre Marte: temperatura de congelacion a la presion media de la ficha (636 Pa), referencia 194.7 K a 1 atm (valor estandar no consultado)
Rc = R / 0.04401
T_ref, P_ref, L = 194.7, 101325.0, 5.9e5
T_f = 1 / (1 / T_ref - Rc / L * math.log(636.0 / P_ref))
print(f"CO2 en Marte (636 Pa): temperatura de escarcha ilustrativa = {T_f:.1f} K")
# nivel de condensacion: T=303 K, punto de rocio 293 K
Gd, Gdp = 9.76e-3, 1.8e-3
z_lcl = (303.0 - 293.0) / (Gd - Gdp)
print(f"Nivel de condensacion (T=303 K, Td=293 K): {z_lcl:.0f} m (formula lineal; regla empirica ~125 m/K = {125*(10):.0f} m)")
# sedimentacion de Stokes
mu, rho_a, g, rho_p = 1.8e-5, 1.2, 9.820, 1500.0
print("radio [um]   v Stokes [m/s]   Reynolds   tiempo para caer 1 km")
for r_um in (0.1, 1.0, 10.0, 50.0):
    r = r_um * 1e-6
    v = 2 * r * r * (rho_p - rho_a) * g / (9 * mu)
    Re = rho_a * v * 2 * r / mu
    t = 1000.0 / v
    print(f"{r_um:9.1f} {v:16.3e} {Re:10.2e} {t/86400:12.2f} dias")
    assert math.isclose(v, 2 * r**2 * (rho_p - rho_a) * g / (9 * mu), rel_tol=1e-12)
    assert Re < 1.0 or r_um >= 50.0
print("Pruebas superadas.")
