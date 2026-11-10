#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C15: pila de combustible H2/O2 frente a bateria Li-ion para una necesidad de energia SINTETICA.

Datos consultados (2026-11-10): constante de Faraday F = 96485.33212... C/mol (NIST, CODATA 2022); energia especifica de baterias Li-ion comerciales de 150 a 270 Wh/kg y de
paquetes de 91 a 250 Wh/kg, y la mencion de pilas de combustible como tecnologia de herencia espacial que aun no se ha miniaturizado (capitulo de potencia del estado del arte de la NASA).
NO CONSULTADOS (valores de manual, ilustrativos): Delta G = -237.1 kJ/mol y Delta H = -285.8 kJ/mol del agua liquida, masas molares H2 = 2.01588 y O2 = 31.998 g/mol.
ILUSTRATIVOS (sinteticos): tension de operacion de celda 0.75 V, potencia de 500 W, potencia especifica de la pila 100 W/kg, factor de tanques y balance de planta 1.5 sobre la masa de reactivos,
bateria de 150 Wh/kg a nivel de paquete.
Modelo: E0 = -Delta G/(2 F); eficiencia respecto del poder calorifico superior eta = V/(-Delta H/(2F)); m_H2 = E M/(V 2 F) y m_O2 = m_H2 M_O2/(2 M_H2);
masa del sistema m_fc = P/rho_p + 1.5 (m_H2 + m_O2); masa de bateria m_b = E/rho_E; cruce m_fc = m_b.
Segunda via: masa de H2 por integracion de la corriente (I = P/V, Q = I t, n = Q/(2F)) y balance de masa del agua formada (m_H2O = m_H2 + m_O2).
Tolerancia: masa por energia frente a masa por carga < 1e-9 relativo; balance de masa del agua < 1e-4 (limitado por el redondeo de las masas molares).
"""
from __future__ import annotations
import math, platform

F = 96485.33212
DG, DH = -237.1e3, -285.8e3                 # J/mol (ilustrativos)
M_H2, M_O2, M_H2O = 2.01588e-3, 31.998e-3, 18.01528e-3   # kg/mol
V_OP, P, RHO_P, FACTOR, RHO_BAT = 0.75, 500.0, 100.0, 1.5, 150.0


def reactivos(e_wh):
    e_j = e_wh * 3600.0
    n_h2 = e_j / (V_OP * 2.0 * F)
    return n_h2 * M_H2, 0.5 * n_h2 * M_O2, n_h2 * M_H2O


def reactivos_por_carga(e_wh):
    t = e_wh * 3600.0 / P
    i = P / V_OP
    q = i * t
    n_h2 = q / (2.0 * F)
    return n_h2 * M_H2


def masa_fc(e_wh):
    h2, o2, _ = reactivos(e_wh)
    return P / RHO_P + FACTOR * (h2 + o2)


def masa_bat(e_wh):
    return e_wh / RHO_BAT


def cruce():
    # masa_fc - masa_bat es lineal en E: biseccion
    lo, hi = 1.0, 1e6
    for _ in range(300):
        m = 0.5 * (lo + hi)
        if masa_fc(m) > masa_bat(m):
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def resultados():
    e0 = -DG / (2.0 * F)
    etn = -DH / (2.0 * F)
    r = dict(E0=e0, E_tn=etn, eta_HHV=V_OP / etn, eta_G=V_OP / e0, eta_pct=V_OP / etn * 100.0, eta_G_pct=V_OP / e0 * 100.0)
    h2, o2, w = reactivos(1000.0)
    r["h2_kWh_g"], r["o2_kWh_g"], r["agua_kWh_g"] = h2 * 1e3, o2 * 1e3, w * 1e3
    r["reac_kWh"] = (h2 + o2) * 1e3
    r["bal_masa"] = abs(w - (h2 + o2)) / w
    r["dif_carga"] = abs(reactivos_por_carga(1000.0) - h2) / h2
    r["Ecruce"] = cruce()
    for e in (500.0, 2000.0, 10000.0):
        k = int(e)
        r[f"mfc{k}"], r[f"mb{k}"] = masa_fc(e), masa_bat(e)
    r["pila_kg"] = P / RHO_P
    r["pend_fc"] = FACTOR * r["reac_kWh"] / 1000.0       # kg por Wh
    r["horas_10kWh"] = 10000.0 / P
    r["horas_cruce"] = r["Ecruce"] / P
    r["n_mol"] = 3.6e6 / (V_OP * 2.0 * F)
    r["pend_fc_kg"] = r["pend_fc"]
    r["bat_kg_kWh"] = 1000.0 / RHO_BAT
    r["h2_070"] = 3.6e6 / (0.70 * 2.0 * F) * M_H2 * 1e3
    r["mfc4000"] = masa_fc(4000.0)
    r["Ecruce2_kWh"] = 10.0 / (1.0 / RHO_BAT - r["pend_fc"] / 1000.0) / 1000.0
    r["Ecruce3_kWh"] = (P / RHO_P) / (1.0 / RHO_BAT - 2.0 * r["pend_fc"] / 1000.0) / 1000.0
    r["Ecruce_kWh"] = r["Ecruce"] / 1000.0
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Tension reversible E0 = {r['E0']:.4f} V ; tension termoneutra = {r['E_tn']:.4f} V (valores de manual NO consultados, ilustrativos)")
    print(f"Celda sintetica a {V_OP} V: eficiencia sobre HHV = {r['eta_pct']:.1f} % ; sobre Delta G = {r['eta_G_pct']:.1f} %")
    print(f"Reactivos por kWh a {V_OP} V: H2 = {r['h2_kWh_g']:.2f} g ; O2 = {r['o2_kWh_g']:.2f} g ; agua formada = {r['agua_kWh_g']:.2f} g")
    print(f"Balance de masa del agua: diferencia relativa = {r['bal_masa']:.1e} ; H2 por integral de la corriente: diferencia relativa = {r['dif_carga']:.1e}")
    print(f"Pila de {P:.0f} W a {RHO_P:.0f} W/kg = {r['pila_kg']:.2f} kg ; reactivos con tanques = {r['pend_fc']:.3f} kg/kWh ; bateria a {RHO_BAT:.0f} Wh/kg = {1000/RHO_BAT:.3f} kg/kWh")
    print(" E [Wh]   t a 500 W [h]   m pila [kg]   m bateria [kg]")
    for e in (500, 2000, 10000):
        print(f" {e:6d}   {e/P:12.1f}   {r[f'mfc{e}']:11.3f}   {r[f'mb{e}']:13.3f}")
    print(f"Energia de cruce (la pila pesa menos que la bateria por encima de) = {r['Ecruce']:.1f} Wh = {r['Ecruce_kWh']:.3f} kWh")
    assert r["bal_masa"] < 1e-4 and r["dif_carga"] < 1e-9   # las masas molares redondeadas no cierran el agua mejor que 1e-4
    assert r["mfc500"] > r["mb500"] and r["mfc10000"] < r["mb10000"]
    assert abs(masa_fc(r["Ecruce"]) - masa_bat(r["Ecruce"])) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
