#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C24: conversion de unidades y indice de riesgo aditivo frente a limites de exposicion (valores ILUSTRATIVOS).

Consultado (NASA, pagina «Exposure Guidelines: SMACs & SWEGs»): los SMAC son limites de contaminantes quimicos en el aire de naves fijados por los toxicologos del JSC con el comite de toxicologia
del NRC; los SWEG son sus equivalentes para el agua; los valores oficiales estan en JSC 20584 (SMAC) y JSC 63414 (SWEG). LOS VALORES DE ESOS DOCUMENTOS NO SE CONSULTARON: la tabla de este
laboratorio usa limites INVENTADOS (ilustrativos) y concentraciones SINTETICAS, y no debe leerse como ningun SMAC. Gas ideal: C [mg/m3] = ppm M P/(R T) (1 ppm = 1.1451 mg/m3 para CO a 25 C y 101.325 kPa).
Verificacion: 1 ppm de CO a 25 C y 1 atm = 1.145 mg/m3; la conversion escala con P; el indice suma las razones C/L.
"""
from __future__ import annotations
import platform
import numpy as np

RG = 8.314462


def mg_conv(ppm, M, P=101325.0, T=298.15):
    return ppm * 1e-6 * (P / (RG * T)) * M * 1e3  # mg/m3


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: limites INVENTADOS (ilustrativos) y concentraciones SINTETICAS; los valores reales de JSC 20584 NO se consultaron; no son SMAC")
    R = {}
    c1 = mg_conv(1.0, 28.01)
    print(f"Control: 1 ppm de CO (28.01 g/mol) a 25 C y 101.325 kPa = {c1:.4f} mg/m3 (valor de manual ~1.145)")
    assert abs(c1 - 1.1451) < 0.002
    for nom, P in (("101.3 kPa", 101325.0), ("55.2 kPa (8 psia)", 55158.0), ("34.6 kPa", 34640.0)):
        print(f"   1 ppm de CO a {nom}: {mg_conv(1.0, 28.01, P):.4f} mg/m3 (la fraccion en volumen es la misma; la masa por m3 baja con P)")
    R["c1"], R["c55"] = c1, mg_conv(1.0, 28.01, 55158.0)
    assert abs(mg_conv(1.0, 28.01, 55158.0) / c1 - 55158.0 / 101325.0) < 1e-12
    # tabla sintetica: compuesto, M, concentracion medida [ppm], limite ilustrativo [ppm]
    tabla = [("compuesto A", 44.05, 0.30, 4.0), ("compuesto B", 58.08, 1.2, 10.0), ("compuesto C", 28.01, 2.0, 15.0), ("compuesto D", 78.11, 0.05, 1.0), ("compuesto E", 17.03, 1.5, 7.0), ("compuesto F", 46.07, 3.0, 30.0)]
    print("Indice de riesgo aditivo HI = suma(C_i / L_i) con limites ILUSTRATIVOS (HI < 1 aceptable en este ejercicio):")
    print("   compuesto      M [g/mol]  C [ppm]  C [mg/m3]  L [ppm]   C/L")
    hi = 0.0
    razones = []
    for nom, M, c, L in tabla:
        r = c / L
        hi += r
        razones.append(r)
        print(f"   {nom:12s}  {M:8.2f}  {c:7.2f}  {mg_conv(c, M):9.3f}  {L:7.2f}  {r:6.3f}")
    R["hi"], R["dom"] = hi, tabla[int(np.argmax(razones))][0]
    print(f"HI = {hi:.3f}; compuesto dominante: {R['dom']} ({max(razones):.3f}); {'cumple' if hi < 1 else 'NO cumple'} el ejercicio")
    assert abs(hi - sum(razones)) < 1e-12 and hi < 1
    # escenario: el compuesto E se duplica y D triplica
    t2 = [(n_, M, c * (2 if n_ == "compuesto E" else 3 if n_ == "compuesto D" else 1), L) for n_, M, c, L in tabla]
    hi2 = sum(c / L for _, _, c, L in t2)
    R["hi2"] = hi2
    print(f"Escenario: E x2 y D x3 -> HI = {hi2:.3f}; {'cumple' if hi2 < 1 else 'NO cumple'} aunque cada compuesto por separado quede bajo su limite: {all(c/L < 1 for _, _, c, L in t2)}")
    assert hi2 > hi and all(c / L < 1 for _, _, c, L in t2)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
