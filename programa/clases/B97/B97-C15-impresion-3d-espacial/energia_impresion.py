#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C15: energia y tiempo de una impresion 3D por sinterizado de regolito.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos ni consultados): temperatura inicial 300 K, temperatura de sinterizado 1400 K, calor especifico
cp(T) = 840 (1 + 0.0004 (T - 300)) J/(kg K), fraccion fundida 0.30 con calor latente 3.0e5 J/kg, potencia util de 1.0 kW con acoplamiento 0.30,
densidad impresa 1700 kg/m3, muro de 4.0 m x 1.0 m x 0.25 m, capa de 10 mm. Ninguno es una propiedad real de un regolito ni de una maquina.
Modelo: energia por kg E = integral cp dT + f L; tasa de masa = eta P / E; tiempo = masa / tasa; capas = altura / espesor de capa.
Segunda via: la integral de cp(T) por regla del trapecio (20000 tramos) frente a la forma cerrada; tolerancia relativa 1e-9.
Unidades SI. Sin perdidas por radiacion ni conduccion, sin tiempos de recarga de material ni de desplazamiento.
"""
from __future__ import annotations
import math, platform

T0, T1, CP0, K, FUND, LAT = 300.0, 1400.0, 840.0, 0.0004, 0.30, 3.0e5            # ILUSTRATIVOS
P_UTIL, ETA, RHO, LX, LY, LZ, CAPA = 1000.0, 0.30, 1700.0, 4.0, 0.25, 1.0, 0.010


def cp(t):
    return CP0 * (1 + K * (t - T0))


def entalpia_cerrada():
    return CP0 * ((T1 - T0) + 0.5 * K * (T1 - T0) ** 2)


def entalpia_trapecio(n=20000):
    h = (T1 - T0) / n
    return sum(0.5 * (cp(T0 + i * h) + cp(T0 + (i + 1) * h)) * h for i in range(n))


def calc():
    sens = entalpia_cerrada()
    e_kg = sens + FUND * LAT
    vol = LX * LY * LZ
    masa = RHO * vol
    energia = masa * e_kg
    tasa = ETA * P_UTIL / e_kg
    t = masa / tasa
    capas = round(LZ / CAPA)
    t_capa = t / capas
    return dict(sens=sens, e_kg=e_kg, e_kwh_kg=e_kg / 3.6e6, vol=vol, masa=masa, energia=energia, energia_kwh=energia / 3.6e6, tasa=tasa, tasa_kg_h=tasa * 3600,
                t_s=t, t_h=t / 3600, capas=capas, t_capa_min=t_capa / 60, dif=abs(entalpia_trapecio() - sens) / sens,
                frac_lat=FUND * LAT / e_kg, e_cte=CP0 * (T1 - T0) + FUND * LAT, dif_cp=(sens - CP0 * (T1 - T0)) / sens)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Muro ILUSTRATIVO {LX} x {LY} x {LZ} m = {r['vol']:.2f} m3; densidad impresa {RHO:.0f} kg/m3 -> masa = {r['masa']:.0f} kg; {r['capas']} capas de {CAPA*1000:.0f} mm")
    print(f"Calor sensible = {r['sens']/1e3:.1f} kJ/kg; latente = {FUND*LAT/1e3:.1f} kJ/kg; energia especifica = {r['e_kg']/1e3:.1f} kJ/kg ({r['e_kwh_kg']:.3f} kWh/kg)")
    print(f"Energia total = {r['energia']/1e9:.3f} GJ ({r['energia_kwh']:.0f} kWh); tasa de deposicion = {r['tasa_kg_h']:.2f} kg/h con {P_UTIL:.0f} W utiles y acoplamiento {ETA}")
    print(f"Tiempo de impresion = {r['t_h']:.1f} h ({r['t_capa_min']:.1f} min por capa)")
    print(f"Con cp constante la energia especifica seria {r['e_cte']/1e3:.1f} kJ/kg; el cp variable aporta {100*r['dif_cp']:.1f} % del calor sensible")
    print(f"Diferencia relativa entre la integral de cp cerrada y por trapecios = {r['dif']:.2e}")
    assert r["dif"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
