#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C17: escenario de incendio en una cabina cerrada: calor, presion, oxigeno consumido, CO2 producido y tiempo de deteccion.

Consultado (Yang et al. 2018, Fire Safety Journal 98, ficha del NIST): ninguno de los dos detectores espaciales evaluados identifico todos los tipos de humo y los detectores de proxima
generacion deben probarse con humo de materiales espaciales. Valores de manual NO consultados: calor de combustion de la celulosa de 16 MJ/kg, formula C6H10O5 (162.14 g/mol),
cv del aire de 718 J/(kg K). ILUSTRATIVOS: combustible de 0.5 kg, cabina rigida de 100 m3 a 293.15 K y 101.325 kPa, 30 % del calor absorbido por las paredes en el caso moderado,
caudal de ventilacion de 0.6 m3/s, tasa de humo de 2 mg/s y umbral de alarma de 1 mg/m3, distancia al detector de 10 m a 0.2 m/s.
Verificacion: conservacion de masa de la reaccion C6H10O5 + 6 O2 -> 6 CO2 + 5 H2O; la subida de presion es la de un gas ideal a volumen constante.
"""
from __future__ import annotations
import math
import platform
import numpy as np

M_FUEL, M_O2, M_CO2, M_H2O = 162.14, 31.998, 44.01, 18.015
HC, CV, V, T0, P0 = 16e6, 718.0, 100.0, 293.15, 101325.0
RG = 8.314462


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: valores de manual NO consultados e ILUSTRATIVOS; la limitacion de los detectores es el resultado CONSULTADO de Yang et al. (2018); ningun incendio real")
    R = {}
    ent = 6 * M_O2 + M_FUEL
    sal = 6 * M_CO2 + 5 * M_H2O
    print(f"Control de masa: C6H10O5 + 6 O2 -> 6 CO2 + 5 H2O : entran {ent:.3f} g/mol, salen {sal:.3f} g/mol (diferencia {ent-sal:+.3f})")
    assert abs(ent - sal) < 0.05
    o2_kg = 6 * M_O2 / M_FUEL
    co2_kg = 6 * M_CO2 / M_FUEL
    R.update(o2_kg=o2_kg, co2_kg=co2_kg)
    print(f"Por kg de combustible: consume {o2_kg:.3f} kg de O2, produce {co2_kg:.3f} kg de CO2 y {5*M_H2O/M_FUEL:.3f} kg de H2O")
    m_aire = P0 * V * 0.02897 / (RG * T0)
    n_gas = P0 * V / (RG * T0)
    m_o2_cab = 0.21 * n_gas * M_O2 / 1000
    print(f"Cabina: {m_aire:.1f} kg de aire, {n_gas:.0f} mol, {m_o2_cab:.2f} kg de O2")
    print("   combustible [kg]   Q [MJ]   dT sin perdidas [K]   dP [kPa]   dT con 30 % a paredes [K]   O2 consumido [%]   dppCO2 [mmHg]")
    for mf in (0.05, 0.5):
        Q = mf * HC
        dT = Q / (m_aire * CV)
        dP = P0 * dT / T0
        dT_m = 0.7 * dT
        o2c = mf * o2_kg / m_o2_cab * 100
        dpp = mf * co2_kg / (M_CO2 / 1000) / n_gas * 760.0
        print(f"   {mf:15.2f}   {Q/1e6:6.1f}   {dT:19.1f}   {dP/1e3:8.1f}   {dT_m:24.1f}   {o2c:15.2f}   {dpp:12.2f}")
        R[mf] = dict(Q=Q, dT=dT, dP=dP / 1e3, dT_m=dT_m, o2c=o2c, dpp=dpp)
    assert R[0.5]["dpp"] > 3.0 and R[0.5]["o2c"] < 5.0
    m_dot, c_thr = 2.0, 1.0
    Q_v = 0.6
    tau = V / Q_v
    t_alarm = -tau * math.log(1 - c_thr * Q_v / m_dot)
    t_trans = 10.0 / 0.2
    R.update(tau=tau, t_alarm=t_alarm, t_trans=t_trans)
    print(f"Deteccion (humo de mezcla perfecta, {m_dot} mg/s, umbral {c_thr} mg/m3): con {Q_v} m3/s, tau = {tau:.0f} s y la alarma llega en {t_alarm:.0f} s; el transporte de 10 m a 0.2 m/s suma {t_trans:.0f} s")
    print("   caudal de ventilacion [m3/s]   concentracion maxima [mg/m3]   tiempo de alarma [s]")
    previo = 0.0
    for Q in (0.1, 0.3, 0.6, 1.5, 2.5):
        cmax = m_dot / Q
        if cmax > c_thr:
            ta = -(V / Q) * math.log(1 - c_thr * Q / m_dot)
            print(f"   {Q:26.1f}   {cmax:28.2f}   {ta:18.0f}")
            assert ta > previo - 1e-9 or Q == 0.1
            previo = ta
        else:
            print(f"   {Q:26.1f}   {cmax:28.2f}   {'nunca (diluido bajo el umbral)':>18}")
    R["q_max"] = m_dot / c_thr
    R["ta_01"] = -(V / 0.1) * math.log(1 - c_thr * 0.1 / m_dot)
    print(f"Con esta tasa de humo, ventilar a mas de {R['q_max']:.1f} m3/s diluye el humo por debajo del umbral y la alarma no suena")
    assert t_alarm > 0 and R["ta_01"] < t_alarm
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
