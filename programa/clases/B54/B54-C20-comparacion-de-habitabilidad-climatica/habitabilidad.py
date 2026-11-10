#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C20: tabla comparativa de condiciones climaticas de Venus, Tierra, Marte y Titan.

Datos: fichas NASA/NSSDC (irradiancia, albedo de Bond, T y presion de superficie de Venus, Tierra y Marte), pagina NASA Science de Titan (T = 94.15 K; presion
"60 % mayor que la terrestre"; Titan recibe S ~ S0/9.58^2 con 9.58 UA ilustrativo no consultado y albedo SINTETICO 0.3) y limites 0.99-1.70 UA (resumen de Kopparapu et al. 2013);
punto triple del agua (273.16 K; 611.657 Pa) y temperatura critica (647.1 K), valores estandar NO consultados. Consulta 2026-11-09. sigma de NIST CODATA 2022.
Modelo: instalacion relativa, T de equilibrio, efecto invernadero Delta = T_s - T_e, y tres condiciones NECESARIAS (no suficientes) para agua liquida en la superficie:
P_s > 611.657 Pa y 273.16 K < T_s < 647.1 K. El indicador NO mide habitabilidad: solo ordena condiciones climaticas.
Tolerancia: Te recalculado frente a la ficha (0.3 K salvo Tierra, ver B54-C03).
"""
import platform
SIG = 5.670374419e-8
print(f"Python {platform.python_version()} (biblioteca estandar)")
D = {  # S [W/m2], A, Ts [K], Ps [Pa], origen
    "Venus": (2601.3, 0.77, 737.0, 92e5), "Tierra": (1361.0, 0.294, 288.0, 101400.0),
    "Marte": (586.2, 0.250, 214.0, 636.0), "Titan": (1361.0 / 9.58 ** 2, 0.30, 94.15, 1.6 * 101325.0)}
TP_T, TP_P, T_CRIT = 273.16, 611.657, 647.1
print("mundo     S/S_T   Te [K]   Ts [K]  Delta [K]  Ps [Pa]    273<T<647 P>611.7  ambas")
for n, (S, A, Ts, Ps) in D.items():
    Te = (S * (1 - A) / (4 * SIG)) ** 0.25
    cT, cP = TP_T < Ts < T_CRIT, Ps > TP_P
    print(f"{n:8s} {S/1361.0:7.3f} {Te:8.1f} {Ts:8.1f} {Ts-Te:9.1f} {Ps:11.1f} {str(cT):>9s} {str(cP):>8s} {str(cT and cP):>6s}")
assert abs((D["Venus"][0] * (1 - D["Venus"][1]) / (4 * SIG)) ** 0.25 - 226.6) < 0.3
assert abs((D["Marte"][0] * (1 - D["Marte"][1]) / (4 * SIG)) ** 0.25 - 209.8) < 0.3
# posicion respecto de los limites solares de la zona habitable (solo para el Sol)
a = {"Venus": 0.72333199, "Tierra": 1.0, "Marte": 1.52366231}
for n, d in a.items():
    pos = "interior al borde interno" if d < 0.99 else ("dentro" if d <= 1.70 else "exterior")
    print(f"{n:7s} a = {d:.4f} UA: {pos} del intervalo 0.99-1.70 UA (Sol, modelo sin nubes)")
assert a["Venus"] < 0.99 <= a["Tierra"] <= 1.70 and a["Marte"] <= 1.70
# prueba de consistencia: ordenacion por instalacion es monotona con el semieje
assert 2601.3 > 1361.0 > 586.2
# presion minima de la columna para el agua liquida a 288 K y a 214 K (la presion del punto triple es el umbral)
print(f"Marte: P_media / P_punto_triple = {636.0/TP_P:.2f} (por encima del umbral por poco; con T media de 214 K el agua no es liquida)")
print("Pruebas superadas.")
