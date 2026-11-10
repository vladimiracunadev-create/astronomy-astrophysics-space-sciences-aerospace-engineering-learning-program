#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C06: sublimacion en vacio (ley de Langmuir) y camino libre medio.

Constantes: k_B = 1,380649e-23 J/K y N_A = 6,02214076e23 1/mol (valores exactos del SI 2019; no consultados en esta sesion); R = k_B N_A.
DATOS ILUSTRATIVOS (ordenes de magnitud, NO consultados, no de diseno): para cada metal, una temperatura T1 a la que la presion de vapor
es 1 Pa, la entalpia de sublimacion H y la masa molar M y la densidad rho.
  metal   T1 [K]   H [kJ/mol]   M [g/mol]   rho [kg/m3]
  Cd       457       112          112,4        8650
  Zn       540       130           65,4        7140
  Mg       600       147           24,3        1740
  Al      1190       326           27,0        2700
  Ti      1710       470           47,9        4500
Modelo: P(T) = 1 Pa exp(-H/R (1/T - 1/T1)); flujo de Langmuir J = P sqrt(M/(2 pi R T)) [kg/(m2 s)] (coeficiente de acomodacion = 1,
sin reflexion: cota superior); perdida de espesor por ano = J t / rho.
Segunda via: flujo molecular P/sqrt(2 pi m k_B T) multiplicado por la masa molecular m = M/N_A (otra expresion de la misma magnitud). Tolerancia relativa < 1e-12.
Camino libre medio de N2 (d = 3,7e-10 m, ilustrativo): lambda = k_B T / (sqrt(2) pi d2 P).
"""
from __future__ import annotations
import math, platform

KB, NA = 1.380649e-23, 6.02214076e23
R = KB * NA
AN = 365.25 * 86400.0
METALES = {"Cd": (457.0, 112e3, 112.4e-3, 8650.0), "Zn": (540.0, 130e3, 65.4e-3, 7140.0),
           "Mg": (600.0, 147e3, 24.3e-3, 1740.0), "Al": (1190.0, 326e3, 27.0e-3, 2700.0),
           "Ti": (1710.0, 470e3, 47.9e-3, 4500.0)}


def presion(T, T1, H):
    return math.exp(-H / R * (1 / T - 1 / T1))


def flujo(P, M, T):
    return P * math.sqrt(M / (2 * math.pi * R * T))


def flujo_b(P, M, T):
    m = M / NA
    return m * P / math.sqrt(2 * math.pi * m * KB * T)  # masa por flujo molecular P/sqrt(2 pi m k T)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Perdida de espesor por sublimacion al ano [micrometros] (datos ILUSTRATIVOS, cota superior):")
    temps = (300.0, 400.0, 500.0)
    print(f"{'metal':6s}" + "".join(f"{'T=' + str(int(t)) + ' K':>14s}" for t in temps))
    dmax = 0.0
    res = {}
    for n, (T1, H, M, rho) in METALES.items():
        fila = []
        for T in temps:
            P = presion(T, T1, H)
            j1, j2 = flujo(P, M, T), flujo_b(P, M, T)
            dmax = max(dmax, abs(j1 - j2) / j1)
            e = j1 * AN / rho * 1e6
            fila.append(e)
        res[n] = fila
        print(f"{n:6s}" + "".join(f"{e:14.3e}" for e in fila))
    print(f"Diferencia relativa maxima entre las dos expresiones del flujo = {dmax:.1e}")
    print("Presion de vapor a 300 K [Pa]: " + ", ".join(f"{n} {presion(300.0, v[0], v[1]):.2e}" for n, v in METALES.items()))
    print("Camino libre medio de N2 a 300 K:")
    for P in (1e5, 1e-2, 1e-5, 1e-8):
        lam = KB * 300.0 / (math.sqrt(2) * math.pi * (3.7e-10) ** 2 * P)
        print(f"  P = {P:8.0e} Pa  lambda = {lam:10.3e} m")
    # Criterio ilustrativo: perdida < 1 micrometro en 10 anos a 300 K
    print("Clasificacion ILUSTRATIVA (perdida < 1 um en 10 anos a 300 K):")
    for n in METALES:
        e10 = res[n][0] * 10
        print(f"  {n}: {e10:.2e} um en 10 anos -> {'apto sin proteccion' if e10 < 1 else 'NO apto sin proteccion'}")
    assert dmax < 1e-12
    assert res["Cd"][0] > 1.0 and res["Al"][0] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
