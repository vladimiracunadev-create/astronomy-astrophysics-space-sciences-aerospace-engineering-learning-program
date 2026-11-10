#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C05: gradiente adiabatico seco y criterio de estabilidad convectiva.

Datos: g de las fichas NASA/NSSDC (consulta 2026-11-09). Calores especificos cp (aire ~1004, CO2 ~850 J/kg/K a baja T, H2/He ~12000 J/kg/K) son
VALORES ILUSTRATIVOS no consultados; para CO2 a alta T real, cp es mayor y el gradiente menor. Perfiles ambientales de prueba: SINTETICOS.
Modelo: Gamma_ad = g / cp ; T(P) = T0 (P/P0)^(R/(M cp)) (adiabata seca). Criterio: capa inestable si -dT/dz > Gamma_ad.
Supuestos: gas ideal, sin condensacion. Tolerancia: integracion numerica frente a la adiabata analitica 1e-6 relativo.
"""
import math, platform
R = 1.380649e-23 * 6.02214076e23
G = {"Tierra": (9.820, 1004.0, 0.028967), "Venus": (8.87, 850.0, 0.043449), "Marte": (3.73, 850.0, 0.043486), "Jupiter": (24.79, 12000.0, 0.002219)}
print(f"Python {platform.python_version()} (biblioteca estandar)")
print("planeta   Gamma_ad [K/km]   kappa = R/(M cp)")
for n, (g, cp, M) in G.items():
    print(f"{n:8s} {g/cp*1e3:14.2f} {R/(M*cp):15.4f}")
# integracion de dT/dP = kappa T / P frente a la formula cerrada (Tierra, 1000 hPa -> 500 hPa)
g, cp, M = G["Tierra"]; kappa = R / (M * cp)
T0, P0, P1 = 300.0, 100000.0, 50000.0
n = 20000; h = (P1 - P0) / n; P, T = P0, T0
f = lambda P, T: kappa * T / P
for _ in range(n):
    k1 = f(P, T); k2 = f(P + h/2, T + h*k1/2); k3 = f(P + h/2, T + h*k2/2); k4 = f(P + h, T + h*k3)
    T += h*(k1 + 2*k2 + 2*k3 + k4)/6; P += h
ex = T0 * (P1 / P0) ** kappa
print(f"Tierra, 100 -> 50 kPa desde 300 K: RK4 = {T:.5f} K ; analitica = {ex:.5f} K")
assert abs(T - ex) / ex < 1e-6
# criterio de estabilidad con perfiles sinteticos
Gam = g / cp * 1e3
for nombre, lapse in [("capa estable (inversion -3 K/km)", 3.0), ("capa neutra (9.8 K/km)", Gam), ("capa inestable (11 K/km)", 11.0)]:
    est = "estable" if lapse < Gam - 1e-9 else ("neutra" if abs(lapse - Gam) < 1e-9 else "inestable")
    print(f"{nombre:36s} gradiente ambiental {lapse:5.2f} K/km frente a {Gam:.2f}: {est}")
# frecuencia de Brunt-Vaisala N^2 = g/T (Gamma_ad - Gamma) con T=280 K
for lapse in (6.5, 3.0, 0.0):
    N2 = g / 280.0 * (Gam - lapse) / 1e3
    print(f"gradiente {lapse:4.1f} K/km: N^2 = {N2:.3e} s^-2 ; periodo de flotabilidad = {2*math.pi/math.sqrt(N2)/60:.1f} min")
# altura convectiva de una capa limite: enfriamiento adiabatico de T0 a T0 - 30 K
print(f"Una parcela de la Tierra que sube 3 km se enfria {Gam*3:.1f} K (seca); en Marte {G['Marte'][0]/G['Marte'][1]*1e3*3:.1f} K")
print("Pruebas superadas.")
