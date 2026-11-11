#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C12: dimensionado de un cultivo con luz artificial (fotones, area, O2, CO2 y electricidad).

TODOS los parametros del cultivo son ILUSTRATIVOS (inventados para el ejercicio; no proceden de ninguna fuente consultada): PPFD 300 umol/(m2 s), fotoperiodo de 16 h,
eficiencia de las lamparas de 2.5 umol/J, eficiencia de uso de la luz de 1.5 g de biomasa seca por mol de fotones, fraccion comestible de 0.45, 3.8 kcal por g de
comestible seco. Consultado de C01: 3035 kcal/dia, 0.771 kg de O2 y 0.901 kg de CO2 por persona y dia. Biomasa como CH2O (30.03 g/mol): 1 mol de CO2 fijado libera 1 mol de O2.
Verificacion: la estequiometria CH2O conserva la masa (44.01 + 18.015 -> 30.03 + 32.00 con agua); el area necesaria escala con la cantidad.
"""
from __future__ import annotations
import platform
import numpy as np

PPFD, HORAS, EFIC, LUE, COM, KC = 300.0, 16.0, 2.5, 1.5, 0.45, 3.8
M_CH2O, M_O2, M_CO2 = 30.026, 31.998, 44.01


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: TODOS los parametros del cultivo son ILUSTRATIVOS; demanda por persona de C01 (consultada/calculada)")
    R = {}
    dli = PPFD * 1e-6 * HORAS * 3600.0
    w_luz = PPFD / EFIC
    w_med = w_luz * HORAS / 24.0
    R["dli"], R["w_med"] = dli, w_med
    print(f"Luz: PPFD {PPFD:.0f} umol/(m2 s) x {HORAS:.0f} h = {dli:.2f} mol/(m2 dia); potencia electrica {w_luz:.0f} W/m2 encendida, {w_med:.0f} W/m2 en promedio")
    bio = dli * LUE
    comest = bio * COM
    kcal_m2 = comest * KC
    o2_m2 = bio / M_CH2O * M_O2
    co2_m2 = bio / M_CH2O * M_CO2
    R.update(bio=bio, kcal_m2=kcal_m2, o2_m2=o2_m2, co2_m2=co2_m2)
    print(f"Por m2 y dia: biomasa seca {bio:.1f} g; comestible {comest:.1f} g = {kcal_m2:.0f} kcal; O2 liberado {o2_m2:.1f} g; CO2 fijado {co2_m2:.1f} g")
    a_kcal = 3035.0 / kcal_m2
    a_o2 = 771.0 / o2_m2
    a_co2 = 901.0 / co2_m2
    R.update(a_kcal=a_kcal, a_o2=a_o2, a_co2=a_co2)
    print("Area de cultivo por persona para cubrir cada necesidad por separado:")
    print(f"   100 % de las kcal: {a_kcal:.1f} m2 ({a_kcal*w_med/1000:.2f} kW promedio); todo el O2: {a_o2:.1f} m2; todo el CO2: {a_co2:.1f} m2")
    print("   fraccion de las kcal   area [m2/persona]   potencia [kW/persona]   O2 liberado [g/dia]")
    for f in (0.05, 0.25, 0.5, 1.0):
        a = f * a_kcal
        print(f"   {f:18.2f}   {a:15.1f}   {a*w_med/1000:19.2f}   {a*o2_m2:17.0f}")
    R["a25"] = 0.25 * a_kcal
    R["p100"] = a_kcal * w_med / 1000
    cons = M_CH2O + M_O2 - M_CO2 - 18.015
    print(f"Control de masa de CO2 + H2O -> CH2O + O2: {M_CO2 + 18.015:.3f} g/mol entran, {M_CH2O + M_O2:.3f} g/mol salen (diferencia {cons:.3f})")
    assert abs(cons) < 0.01
    assert a_kcal > a_o2
    R["o2_pers_frac"] = (a_kcal * o2_m2) / 771.0
    print(f"Si se cultivara el area que da el 100 % de las kcal, el O2 liberado seria {R['o2_pers_frac']:.2f} veces el consumo de una persona")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
