#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C06: lazo de agua con fraccion de recuperacion y masa lanzada.

Consultado (NASA, pagina del ECLSS, y OCHMO-TB-002): el ECLSS recicla cerca del 90 % del agua de la estacion; el agua minima para beber es 2.5 L/dia por persona;
el procesador de orina con salmuera permite recuperar mas del 90 %. ILUSTRATIVOS (inventados para el ejercicio): demanda total de 10 kg/dia por persona
(bebida + higiene + preparacion de alimentos), masa del sistema M_sys = 300 + 2000 r^2 kg, recuperaciones de etapa de 0.75 y 0.65.
Verificacion: la simulacion dia a dia coincide con la formula (1 - r) D T; el punto de equilibrio iguala los dos totales; la recuperacion en serie suma r1 + (1-r1) r2.
"""
from __future__ import annotations
import math
import platform
import numpy as np

CREW, D_P = 4, 10.0
D = CREW * D_P  # kg/dia


def msys(r):
    return 300.0 + 2000.0 * r * r if r > 0 else 0.0


def total(r, T):
    return (1 - r) * D * T + msys(r)


def simular(r, T):
    reposicion = 0.0
    for _ in range(int(T)):
        reciclada = r * D
        reposicion += D - reciclada
    return reposicion


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: demanda y masa del sistema ILUSTRATIVAS; la cifra de ~90 % de recuperacion es la consultada (pagina del ECLSS)")
    R = {}
    print(f"Demanda: {CREW} personas x {D_P:.0f} kg/dia = {D:.0f} kg/dia (de ellos {CREW*2.5:.0f} kg/dia de bebida minima consultada)")
    print("  r      reposicion [kg/dia]   total 30 d [kg]   total 180 d [kg]   total 900 d [kg]")
    for r in (0.0, 0.5, 0.8, 0.9, 0.95, 0.98):
        print(f"  {r:4.2f}   {(1-r)*D:14.2f}   {total(r,30):16.0f}   {total(r,180):15.0f}   {total(r,900):16.0f}")
    R["rep90"] = (1 - 0.9) * D
    R["t180_0"], R["t180_90"], R["t900_90"], R["t900_0"] = total(0, 180), total(0.9, 180), total(0.9, 900), total(0, 900)
    be = msys(0.9) / (0.9 * D)
    R["be"] = be
    print(f"Punto de equilibrio con r = 0.9: M_sys/(r D) = {be:.1f} dias (a partir de ahi el lazo ahorra masa lanzada)")
    assert abs(total(0.9, be) - total(0, be)) < 1e-6
    sim = simular(0.9, 180)
    print(f"Control: simulacion dia a dia de 180 dias con r = 0.9 -> {sim:.1f} kg frente a {(1-0.9)*D*180:.1f} kg por formula")
    assert abs(sim - 0.1 * D * 180) < 1e-9
    r1, r2 = 0.75, 0.65
    rt = r1 + (1 - r1) * r2
    R["rt"] = rt
    print(f"Etapas en serie: la primera recupera {r1}, la salmuera pasa a una segunda que recupera {r2} -> r total = {rt:.4f}")
    n = math.log(0.01) / math.log(0.9)
    R["ciclos"] = n
    print(f"Ciclos de reciclaje para que quede 1 % del agua original con r = 0.9: {n:.1f} (el agua se reutiliza ~{1/(1-0.9):.0f} veces)")
    assert abs(rt - 0.9125) < 1e-12
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
