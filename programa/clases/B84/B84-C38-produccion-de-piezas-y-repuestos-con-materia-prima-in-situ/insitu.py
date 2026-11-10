#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C38: produccion de repuestos con materia prima in situ: balance de masa y energia, tiempo, repeticiones por defectos y punto de equilibrio frente al transporte.

DATOS ILUSTRATIVOS (ordenes de magnitud inventados para el ejercicio, NO consultados): repuesto de hierro/acero de 2,0 kg; fraccion masica de hierro extraible del regolito f = 0,08;
rendimiento de extraccion eta = 0,50; perdida por soporte/viruta en la impresion 20 % (rendimiento de la pieza 0,80); energia especifica de extraccion 15 kWh/kg de hierro y de
impresion 8 kWh/kg de pieza; potencia disponible 2,0 kW; probabilidad de pieza defectuosa tras inspeccion p_d = 0,15 (cada intento independiente);
masa de la planta de produccion in situ 400 kg y masa de transporte desde la Tierra igual a la masa del repuesto; tiempo de reaprovisionamiento desde la Tierra 180 dias.
Segunda via: numero esperado de intentos hasta una pieza buena = 1/(1 - p_d) (geometrica) frente a Monte Carlo (20000 repeticiones, semilla 84038).
Tolerancia: Monte Carlo dentro del 2 % de la teoria.
"""
from __future__ import annotations
import math, platform, random

M_PIEZA = 2.0
F_FE, ETA, REND = 0.08, 0.50, 0.80
E_EXT, E_IMP = 15.0, 8.0
POT = 2.0
PD = 0.15
M_PLANTA = 400.0
DIAS_TIERRA = 180.0


def por_pieza(f=F_FE):
    hierro = M_PIEZA / REND
    regolito = hierro / (f * ETA)
    energia = hierro * E_EXT + M_PIEZA * E_IMP
    return hierro, regolito, energia


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    hierro, reg, e = por_pieza()
    print("Repuesto de 2,0 kg (todos los datos ILUSTRATIVOS)")
    print(f"Hierro necesario = {hierro:.2f} kg (rendimiento de pieza {REND}) ; regolito procesado = {reg:.1f} kg (f = {F_FE}, eta = {ETA}) ; escoria/residuo = {reg - hierro:.1f} kg")
    print(f"Energia por intento = {e:.1f} kWh ({hierro * E_EXT:.1f} extraccion + {M_PIEZA * E_IMP:.1f} impresion) ; tiempo a {POT:.1f} kW = {e / POT:.1f} h = {e / POT / 24:.2f} dias")
    rng = random.Random(84038)
    n = 20000
    tot = 0
    for _ in range(n):
        k = 1
        while rng.random() < PD:
            k += 1
        tot += k
    teo = 1 / (1 - PD)
    print(f"Intentos hasta una pieza buena: teorica = {teo:.4f} ; Monte Carlo = {tot / n:.4f} (dif {abs(tot / n - teo) / teo * 100:.2f} %)")
    assert abs(tot / n - teo) / teo < 0.02
    print(f"Por pieza buena: regolito = {reg * teo:.1f} kg ; energia = {e * teo:.1f} kWh ; tiempo = {e * teo / POT:.1f} h = {e * teo / POT / 24:.2f} dias (frente a {DIAS_TIERRA:.0f} dias desde la Tierra)")
    print("Sensibilidad a la fraccion de hierro extraible (regolito por pieza buena, kg):")
    for f in (0.04, 0.08, 0.12, 0.15):
        _, r, _ = por_pieza(f)
        print(f"  f = {f:.2f}: {r * teo:7.1f} kg de regolito por pieza buena")
    nstar = M_PLANTA / M_PIEZA
    print(f"Punto de equilibrio en masa transportada: la planta de {M_PLANTA:.0f} kg se compensa tras {nstar:.0f} repuestos de {M_PIEZA:.0f} kg (si se ignoran consumibles y repuestos de la propia planta)")
    print("Masa transportada acumulada segun el numero de repuestos necesarios (Tierra frente a planta):")
    for nn in (10, 50, 100, 200, 500):
        print(f"  {nn:4d} repuestos: Tierra = {nn * M_PIEZA:6.0f} kg ; planta = {M_PLANTA:5.0f} kg -> {'la planta ahorra masa' if nn * M_PIEZA > M_PLANTA else ('masa igual' if nn * M_PIEZA == M_PLANTA else 'el transporte es menor')}")
    assert abs(nstar - 200) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
