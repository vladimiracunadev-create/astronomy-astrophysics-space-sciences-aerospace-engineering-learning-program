#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C09: el ECLSS como un conjunto de lazos con fracciones de cierre.

Consultado: el ECLSS agrupa recuperacion de agua, revitalizacion del aire y generacion de oxigeno (pagina del ECLSS); O2 de 0.771 kg/dia y agua de bebida minima de
2.5 L/dia por persona; recuperacion de agua de ~90 % (consultadas, ver C01 y C06). ILUSTRATIVOS: demanda de agua de 10 kg/dia por persona, masa de hardware de cada
arquitectura y fraccion de CO2 reducida (0.588, de C05). Modelo de flujos diarios para 4 personas, 180 dias.
Arquitecturas: A = todo almacenado; B = agua reciclada al 90 % y O2 por electrolisis (el H2 se ventila); C = B mas reactor Sabatier.
Verificacion: la reposicion de agua de B incluye el agua electrolizada; C devuelve parte; el balance de masa de O2 se conserva (O2 producido = O2 consumido).
"""
from __future__ import annotations
import platform
import numpy as np

CREW, DIAS = 4, 180
O2_P, W_P = 0.771, 10.0
M_H2O, M_O2 = 0.018015, 0.0320


def reposicion(arq, r=0.9, f_sab=0.588):
    o2 = CREW * O2_P
    agua_el = 2 * o2 / M_O2 * M_H2O  # agua electrolizada por dia (kg)
    w = CREW * W_P
    if arq == "A":
        return dict(o2=o2, agua=w)
    agua = (1 - r) * w + agua_el
    if arq == "B":
        return dict(o2=0.0, agua=agua)
    n_co2 = CREW * 0.85 * (O2_P / M_O2)
    n_red = min(n_co2, 2 * o2 / M_O2 / 4)
    return dict(o2=0.0, agua=agua - 2 * n_red * M_H2O)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: modelo de flujos con demanda y masas de hardware ILUSTRATIVAS; cifras de O2 y ~90 % de agua consultadas")
    R = {}
    hw = {"A": 0.0, "B": 600.0, "C": 900.0}
    print(f"{CREW} personas, {DIAS} dias. Reposicion diaria [kg/dia] y total con hardware [kg]:")
    print("  arq   O2 almacenado  agua repuesta   total reposicion [kg]   hardware [kg]   total con hardware [kg]")
    tot = {}
    for a in "ABC":
        r = reposicion(a)
        rep = (r["o2"] + r["agua"]) * DIAS
        tot[a] = rep + hw[a]
        print(f"   {a}      {r['o2']:9.3f}    {r['agua']:11.3f}   {rep:16.0f}   {hw[a]:14.0f}   {tot[a]:18.0f}")
        R[a] = r
    R["tot"] = tot
    R["ahorro_BA"] = 1 - tot["B"] / tot["A"]
    R["ahorro_CB"] = tot["B"] - tot["C"]
    # sensibilidad de B a la recuperacion de agua
    print("Sensibilidad de la reposicion de B a la recuperacion de agua r:")
    for r in (0.8, 0.9, 0.95):
        x = reposicion("B", r)["agua"]
        print(f"   r = {r:.2f}: agua repuesta {x:.2f} kg/dia")
    R["dB_dr"] = (reposicion("B", 0.95)["agua"] - reposicion("B", 0.9)["agua"]) / 0.05
    # balance de O2: la electrolisis produce lo que consume la tripulacion
    prod = 2 * CREW * O2_P / M_O2 / 2 * M_O2
    print(f"Control: O2 producido {prod:.3f} kg/dia frente a O2 consumido {CREW*O2_P:.3f} kg/dia")
    assert abs(prod - CREW * O2_P) < 1e-12
    assert tot["B"] < tot["A"] and tot["C"] < tot["B"] and R["dB_dr"] < 0
    be = hw["B"] / ((reposicion("A")["o2"] + reposicion("A")["agua"]) - (reposicion("B")["agua"]))
    R["be_B"] = be
    print(f"Punto de equilibrio de B frente a A: {be:.1f} dias")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
