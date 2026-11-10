#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C22: energia para sobrevivir a la noche lunar (unos 14 dias) con bateria, pila de combustible o generador radioisotopico (SINTETICO).

Datos consultados (2026-11-10): periodo sinodico de la Luna 29.53 dias y temperatura ecuatorial de 95 K de noche a 390 K de dia (NASA/NSSDC, Moon Fact Sheet);
energia especifica de celdas Li-ion comerciales de 150 a 270 Wh/kg y de paquetes de 91 a 250 Wh/kg (capitulo de potencia del estado del arte de la NASA);
MMRTG: 110 W electricos al inicio y 2.8 W/kg (hoja tecnica de la NASA/DOE); constante de Faraday F = 96485.33212 C/mol (NIST, CODATA 2022).
NO CONSULTADOS (manual, ilustrativos): masas molares H2 y O2.
ILUSTRATIVOS (sinteticos): noche = mitad del periodo sinodico (ecuador, sin latitud ni libracion ni eclipses de la Tierra), carga de supervivencia de 20 W y otra de 100 W, profundidad de descarga de la bateria 0.8,
eficiencia de descarga 0.95, paquete de 150 Wh/kg, pila a 0.75 V con 100 W/kg y factor 1.5 de tanques sobre los reactivos, generador radioisotopico solo si su potencia electrica cubre la carga.
Modelo: E = P t_noche; masa de bateria = E / (DoD eta_d rho); masa de pila = P / rho_p + 1.5 (m_H2 + m_O2); masa del RTG = P_RTG / 2.8 W/kg con P_RTG = 110 W (una unidad, o el entero superior de unidades).
Segunda via: energia de la noche por integracion numerica de una carga con un perfil constante frente a P t; masa de reactivos por carga de Faraday.
Tolerancia: energia por integral frente a P t < 1e-9 relativo; masa de reactivos por energia frente a por carga < 1e-9 relativo.
"""
from __future__ import annotations
import math, platform

SINODICO_D, F = 29.53, 96485.33212
T_NOCHE_H = SINODICO_D / 2.0 * 24.0
DOD, ETA_D, RHO_BAT = 0.8, 0.95, 150.0
V_OP, RHO_P, FACTOR = 0.75, 100.0, 1.5
M_H2, M_O2 = 2.01588e-3, 31.998e-3
P_RTG, W_KG_RTG = 110.0, 2.8


def energia_integral(p, horas, n=100000):
    h = horas / n
    return sum(p * h for _ in range(n))


def masa_bateria(e_wh, rho=RHO_BAT):
    return e_wh / (DOD * ETA_D * rho)


def reactivos_kg(e_wh):
    n = e_wh * 3600.0 / (V_OP * 2.0 * F)
    return n * M_H2 + 0.5 * n * M_O2, n * M_H2


def reactivos_por_carga(p, horas):
    q = (p / V_OP) * horas * 3600.0
    return q / (2.0 * F) * M_H2


def masa_pila(p, horas):
    e = p * horas
    mr, _ = reactivos_kg(e)
    return p / RHO_P + FACTOR * mr


def masa_rtg(p):
    unidades = math.ceil(p / P_RTG)
    return unidades * P_RTG / W_KG_RTG, unidades


def resultados():
    r = dict(t_noche_h=T_NOCHE_H, t_noche_d=T_NOCHE_H / 24.0)
    for p in (20.0, 100.0, 300.0):
        k = int(p)
        e = p * T_NOCHE_H
        r[f"E{k}"] = e
        r[f"E{k}_kWh"] = e / 1000.0
        r[f"mb250_{k}"] = masa_bateria(e, 250.0)
        r[f"mb{k}"] = masa_bateria(e)
        r[f"mp{k}"] = masa_pila(p, T_NOCHE_H)
        m, u = masa_rtg(p)
        r[f"mr{k}"], r[f"ur{k}"] = m, u
        r[f"mejor{k}"] = min((("bateria", r[f"mb{k}"]), ("pila", r[f"mp{k}"]), ("RTG", m)), key=lambda x: x[1])[0]
    r["dif_E"] = abs(energia_integral(20.0, T_NOCHE_H) - 20.0 * T_NOCHE_H) / (20.0 * T_NOCHE_H)
    mr, mh2 = reactivos_kg(20.0 * T_NOCHE_H)
    r["dif_react"] = abs(mh2 - reactivos_por_carga(20.0, T_NOCHE_H)) / mh2
    r["m_h2_20"], r["m_react_20"] = mh2, mr
    # eclipse orbital de referencia (B86-C13): 38.26 Wh
    r["E_ecl"] = 64.8 * 2125.6 / 3600.0
    r["ratio_noche_eclipse"] = r["E20"] / r["E_ecl"]
    # potencia a partir de la cual el RTG gana a la bateria (P*t / (dod eta rho) = unidades*110/2.8 con 1 unidad)
    r["P_cruce_rtg"] = P_RTG / W_KG_RTG * DOD * ETA_D * RHO_BAT / T_NOCHE_H
    r["sa_horas"] = T_NOCHE_H
    r["E50"] = 50.0 * T_NOCHE_H
    r["cap20"] = r["E20"] / (DOD * ETA_D)
    r["T_noche_K"], r["T_dia_K"] = 95.0, 390.0
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Noche lunar (mitad del periodo sinodico de 29.53 d, ecuador): {r['t_noche_d']:.3f} d = {r['t_noche_h']:.1f} h ; temperatura ecuatorial nocturna 95 K, diurna 390 K")
    print(f"Referencia: un eclipse orbital de 600 km pide {r['E_ecl']:.1f} Wh ; la noche lunar con 20 W pide {r['E20']:.0f} Wh ({r['ratio_noche_eclipse']:.0f} veces)")
    print(" P [W]   E [kWh]   bateria 150 Wh/kg [kg]   bateria 250 Wh/kg [kg]   pila H2/O2 [kg]   RTG [kg] (unidades)   mejor")
    for k in (20, 100, 300):
        print(f" {k:5d}  {r[f'E{k}_kWh']:8.2f}  {r[f'mb{k}']:22.1f}  {r[f'mb250_{k}']:22.1f}  {r[f'mp{k}']:15.1f}  {r[f'mr{k}']:8.1f} ({r[f'ur{k}']})   {r[f'mejor{k}']}")
    print(f"Energia por integral frente a P t (20 W): diferencia relativa = {r['dif_E']:.1e} ; H2 por energia frente a H2 por carga: {r['dif_react']:.1e}")
    print(f"Reactivos de la pila para 20 W en la noche: {r['m_react_20']:.2f} kg (H2: {r['m_h2_20']:.3f} kg)")
    print(f"Potencia de la carga a partir de la cual un RTG de 110 W pesa menos que la bateria de 150 Wh/kg = {r['P_cruce_rtg']:.1f} W")
    assert r["dif_E"] < 1e-9 and r["dif_react"] < 1e-9
    assert r["mb20"] > 0 and r["mr20"] > 0 and r["ur20"] == 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
