#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C16: estequiometria de la serpentinizacion (produccion de H2) y energia disponible de la metanogenesis, con una roca SINTETICA.

Datos: pesos atomicos estandar del NIST (consultados el 2026-11-09): Mg 24.305 (punto medio de [24.304, 24.307]), Si 28.085 (punto medio de [28.084, 28.086]), Fe 55.845; O 15.9994 y H 1.00794 (de masas
isotopicas y abundancias NIST). La roca (40 % de olivino con Fo90 en masa; 2/3 del Fe(II) oxidado) y la variacion de energia libre estandar de la metanogenesis (-130 kJ/mol) son SINTETICAS/ILUSTRATIVAS.
Constante de los gases R = k_B N_A = 8.314462618... J mol-1 K-1 (valores exactos del SI 2019). Waite et al. (2017) y Hsu et al. (2015) se consultaron solo por resumenes truncados.
Modelo: reaccion 3 Fe2SiO4 + 2 H2O -> 2 Fe3O4 + 3 SiO2 + 2 H2 (se comprueba el balance de atomos). Por cada Fe(II) oxidado se forma 1/2 H2 (si el Fe(II) pasa a Fe(III)).
Energia: CO2 + 4 H2 -> CH4 + 2 H2O ; DeltaG = DeltaG0 + R T ln Q con Q = a(CH4) / (a(CO2) a(H2)^4) (agua con actividad 1).
Supuestos: sistema cerrado, equilibrio de las fases solidas, actividades iguales a concentraciones (mol/kg). Validez: ilustrativa.
Tolerancia: balance de atomos exacto; H2 por dos caminos de calculo a 1e-12 relativo; DeltaG en estado estandar igual a DeltaG0 a 1e-9.
"""
from __future__ import annotations
import math, platform

H, O, MG, SI, FE = 1.00794, 15.9994, 24.305, 28.085, 55.845
R = 1.380649e-23 * 6.02214076e23
M_FA = 2 * FE + SI + 4 * O
M_FO = 2 * MG + SI + 4 * O
M_H2 = 2 * H

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # balance de atomos
    reac = {"Fe": 3 * 2, "Si": 3 * 1, "O": 3 * 4 + 2 * 1, "H": 2 * 2}
    prod = {"Fe": 2 * 3, "Si": 3 * 1, "O": 2 * 4 + 3 * 2, "H": 2 * 2}
    print("A. Balance de atomos de 3 Fe2SiO4 + 2 H2O -> 2 Fe3O4 + 3 SiO2 + 2 H2")
    print("elemento   reactivos   productos")
    for e in ("Fe", "Si", "O", "H"):
        print(f"{e:>8}   {reac[e]:9d}   {prod[e]:9d}")
        assert reac[e] == prod[e]
    print(f"B. Masas molares [g/mol]: Fe2SiO4 {M_FA:.3f} ; Mg2SiO4 {M_FO:.3f} ; H2 {M_H2:.5f}")
    # H2 por kg de fayalita
    mol_fa = 1000.0 / M_FA
    h2_1 = mol_fa * 2.0 / 3.0
    # segundo camino: Fe(II) -> Fe(III), 1/2 H2 por Fe oxidado, 2/3 del Fe(II) se oxida (en magnetita 2 de 3 Fe son Fe3+)
    fe_oxid = mol_fa * 2.0 * (2.0 / 3.0)
    h2_2 = fe_oxid * 0.5
    print(f"C. H2 por kg de fayalita pura: {h2_1:.4f} mol = {h2_1 * M_H2:.3f} g (segundo camino {h2_2:.4f} mol)")
    assert abs(h2_1 - h2_2) / h2_1 < 1e-12
    # roca sintetica: 40 % olivino Fo90
    x_fo = 0.90
    m_oliv = 400.0   # g de olivino por kg de roca
    mm_ol = x_fo * M_FO + (1 - x_fo) * M_FA
    mol_ol = m_oliv / mm_ol
    mol_fe = mol_ol * 2 * (1 - x_fo)
    f_ox = 2.0 / 3.0
    h2_roca = mol_fe * f_ox * 0.5
    print(f"D. Roca SINTETICA (40 % olivino Fo90): masa molar del olivino = {mm_ol:.3f} g/mol ; Fe(II) = {mol_fe:.4f} mol/kg ; H2 maximo = {h2_roca:.4f} mol/kg = {h2_roca * M_H2:.3f} g/kg")
    print("E. H2 maximo por kg de roca segun la fraccion de olivino y el contenido de Fe (SINTETICO)")
    print("fraccion olivino   Fo#   H2 [mol/kg]")
    for fo_ol in (0.2, 0.4, 0.6):
        for fo in (0.95, 0.90, 0.80):
            mm = fo * M_FO + (1 - fo) * M_FA
            mol = 1000.0 * fo_ol / mm
            h = mol * 2 * (1 - fo) * f_ox * 0.5
            print(f"{fo_ol:15.1f}   {100 * fo:3.0f}   {h:9.4f}")
    # energia
    dG0 = -130.0e3     # J/mol ILUSTRATIVO
    T = 300.0
    print("F. Energia libre de CO2 + 4 H2 -> CH4 + 2 H2O (DeltaG0 = -130 kJ/mol ILUSTRATIVO, T = 300 K, actividades en mol/kg)")
    print("a(H2) [mol/kg]   DeltaG [kJ/mol]")
    a_co2, a_ch4 = 1.0e-3, 1.0e-4
    dg_std = dG0 + R * T * math.log(1.0 / 1.0)
    assert abs(dg_std - dG0) < 1e-9
    prev = None
    for a_h2 in (1e-8, 1e-6, 1e-4, 1e-3, 1e-2):
        Q = a_ch4 / (a_co2 * a_h2 ** 4)
        dg = dG0 + R * T * math.log(Q)
        print(f"{a_h2:12.0e}      {dg / 1e3:9.3f}")
        if prev is not None:
            assert dg < prev
        prev = dg
    # H2 de equilibrio: DeltaG = 0
    a_eq = (a_ch4 / (a_co2 * math.exp(-dG0 / (R * T)))) ** 0.25
    print(f"G. H2 de equilibrio (DeltaG = 0) con CO2 = 1e-3 y CH4 = 1e-4 mol/kg: a(H2) = {a_eq:.3e} mol/kg")
    q_eq = a_ch4 / (a_co2 * a_eq ** 4)
    assert abs(dG0 + R * T * math.log(q_eq)) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
