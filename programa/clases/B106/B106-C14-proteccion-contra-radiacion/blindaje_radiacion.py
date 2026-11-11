#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C14: alcance de protones en un blindaje y fraccion detenida de un espectro SINTETICO.

NO calcula dosis ni riesgo. Modelo de manual NO consultado: regla de Bragg-Kleeman R = a E^p con a = 0.0022 g/cm2/MeV^p y p = 1.77 para agua (R en g/cm2, E en MeV),
valida de forma aproximada entre ~10 y ~250 MeV (el laboratorio rechaza energias mayores). El programa PSTAR del NIST calcula tablas de alcance de protones (solo se consulto su pagina
de presentacion, sin tablas); el valor de ~7.7 g/cm2 a 100 MeV es de manual y no se consulto. Espectro SINTETICO de una tormenta de protones: dN/dE proporcional a E^-gamma entre 10 y 1000 MeV con
gamma = 2.5 (inventado). Densidades ILUSTRATIVAS: agua 1.0 g/cm3, regolito 1.5 g/cm3. Radio del habitat de 2 m. No incluye particulas secundarias, nucleos pesados ni rayos cosmicos galacticos.
Verificacion: E_min(R(E)) = E; la fraccion detenida crece con el espesor.
"""
from __future__ import annotations
import platform
import numpy as np

A, P, GAMMA, ELO, EHI = 0.0022, 1.77, 2.5, 10.0, 1000.0


def alcance(E):
    return A * E ** P


def e_min(x):
    return (x / A) ** (1 / P)


def frac_detenida(E):
    g = 1 - GAMMA
    return (ELO ** g - E ** g) / (ELO ** g - EHI ** g)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: espectro SINTETICO e inventado; regla de Bragg-Kleeman de manual NO consultada; NO es una dosis ni una evaluacion de riesgo")
    R = {}
    r100 = alcance(100.0)
    R["r100"] = r100
    print(f"Alcance de un proton de 100 MeV en agua: {r100:.2f} g/cm2 (valor de tablas de manual, no consultado: ~7.7)")
    assert abs(r100 / 7.7 - 1) < 0.03
    for E in (10.0, 30.0, 100.0, 200.0):
        assert abs(e_min(alcance(E)) - E) < 1e-9
    print("   espesor [g/cm2]   energia minima [MeV]   fraccion del espectro sintetico detenida   masa de una esfera de r = 2 m [kg]")
    filas = {}
    for x in (1.0, 5.0, 10.0, 20.0, 30.0):
        E = e_min(x)
        f = frac_detenida(E)
        m = 4 * np.pi * 2.0 ** 2 * x * 10.0  # g/cm2 -> kg/m2 = x*10
        filas[x] = (E, f, m)
        print(f"   {x:13.0f}   {E:18.1f}   {f:36.4f}   {m:30.0f}")
    R["E10"], R["f10"], R["m10"], R["f1"], R["f30"], R["E30"] = filas[10.0][0], filas[10.0][1], filas[10.0][2], filas[1.0][1], filas[30.0][1], filas[30.0][0]
    assert filas[30.0][1] > filas[10.0][1] > filas[1.0][1]
    print("Regolito (1.5 g/cm3), cubierta sobre el habitat: espesor equivalente y limite del modelo")
    for h in (0.5, 1.0, 2.0, 3.0):
        x = h * 100.0 * 1.5
        E = e_min(x)
        txt = f"E_min = {E:.0f} MeV" if E <= 250 else f"E_min = {E:.0f} MeV (FUERA del rango de validez, solo orientativo)"
        print(f"   {h:3.1f} m -> {x:6.0f} g/cm2: {txt}")
    R["x_1m"], R["E_1m"] = 150.0, e_min(150.0)
    # por que no es una simple exponencial: ejemplo de comparacion con atenuacion exponencial ingenua
    lam = 20.0
    print(f"Aviso: una atenuacion exponencial ingenua exp(-x/{lam:.0f}) daria {np.exp(-30/lam):.3f} a 30 g/cm2; no representa la fisica de las secundarias y NO se usa en este laboratorio")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
