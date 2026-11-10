#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C34: recubrimientos termo-opticos (temperatura de equilibrio) y espesor de anodizado por la ley de Faraday.

Constantes: sigma_SB = 5,670374419e-8 W/(m2 K4) y F = 96485,33212 C/mol (valores del SI/CODATA 2018; no consultados en esta sesion).
DATOS ILUSTRATIVOS (no consultados): constante solar S = 1361 W/m2 (valor tipico a 1 UA); absortividad solar alfa y emisividad infrarroja epsilon al comienzo de vida:
  pintura blanca 0,25/0,88; pintura negra 0,95/0,90; aluminio pulido 0,20/0,05; aluminio anodizado 0,35/0,80; oro 0,30/0,03; reflector solar optico (OSR, vidrio plateado) 0,08/0,80.
Modelo: placa plana con la cara delantera al Sol (incidencia normal) y la trasera aislada; equilibrio alfa S = epsilon sigma T^4 -> T = (alfa S/(epsilon sigma))^(1/4).
Degradacion ILUSTRATIVA: alfa aumenta en +0,10 al final de vida (por UV y radiacion).
Anodizado: Al -> 1/2 Al2O3 por 3 electrones; masa de oxido por mol de carga = 50,98 g/(3 F); espesor = eta j t M_ox/(3 F rho_ox) con densidad de oxido ILUSTRATIVA 3000 kg/m3,
eficiencia eta = 0,8 y densidad de corriente j = 150 A/m2 (1,5 A/dm2). Segunda via de la temperatura: balance de potencia neto = 0 a la T calculada (|residuo| < 1e-9 W/m2).
"""
from __future__ import annotations
import math, platform

SIGMA = 5.670374419e-8
F = 96485.33212
S = 1361.0
REC = {"Pintura blanca": (0.25, 0.88), "Pintura negra": (0.95, 0.90), "Aluminio pulido": (0.20, 0.05),
       "Aluminio anodizado": (0.35, 0.80), "Oro": (0.30, 0.03), "OSR (vidrio plateado)": (0.08, 0.80)}


def temp(al, ep, s=S):
    return (al * s / (ep * SIGMA)) ** 0.25


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Placa de una cara al Sol, trasera aislada, S = 1361 W/m2 (ILUSTRATIVO); alfa y epsilon ILUSTRATIVOS")
    print(f"{'recubrimiento':24s} {'alfa':>5s} {'eps':>5s} {'alfa/eps':>9s} {'T inicio [K]':>13s} {'T inicio [C]':>13s} {'T fin de vida [C]':>18s}")
    rmax = 0.0
    for n, (al, ep) in REC.items():
        T = temp(al, ep)
        res = abs(al * S - ep * SIGMA * T ** 4)
        rmax = max(rmax, res)
        Tf = temp(al + 0.10, ep)
        print(f"{n:24s} {al:5.2f} {ep:5.2f} {al / ep:9.3f} {T:13.2f} {T - 273.15:13.2f} {Tf - 273.15:18.2f}")
    print(f"Residuo maximo del balance de potencia = {rmax:.1e} W/m2")
    print("Sensibilidad: aumento de temperatura por +0,10 de absortividad (K):")
    for n, (al, ep) in REC.items():
        print(f"  {n:24s} +{temp(al + 0.10, ep) - temp(al, ep):6.2f} K")
    print("Anodizado: espesor de oxido segun la carga (eta = 0,8; rho_ox = 3000 kg/m3, ILUSTRATIVO)")
    j = 150.0
    for minutos in (10, 20, 30, 60):
        q = j * minutos * 60.0
        masa = 0.8 * q / (3 * F) * 50.98e-3  # kg/m2
        esp = masa / 3000.0
        print(f"  j = {j:.0f} A/m2, {minutos:2d} min: carga = {q:9.0f} C/m2 ; oxido = {masa * 1e3:6.2f} g/m2 ; espesor = {esp * 1e6:6.2f} um")
    # Efecto de absortividad vs espesor? (no modelado): se avisa
    assert rmax < 1e-9
    assert temp(0.25, 0.88) < temp(0.95, 0.90)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
