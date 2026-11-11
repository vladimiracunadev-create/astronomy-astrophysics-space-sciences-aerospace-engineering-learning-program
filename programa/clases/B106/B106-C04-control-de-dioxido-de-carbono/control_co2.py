#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C04: balance de CO2 de una cabina bien mezclada, con y sin depurador.

Datos CONSULTADOS (OCHMO-TB-004 y TB-002): ppCO2 medio de 1 h < 3 mmHg; dolores de cabeza descritos entre 2.8 y 4.5 mmHg; 0.5 % de CO2 = 3.8 mmHg;
CO2 exhalado con RQ 0.85 (C01). Modelo PROPIO: cabina de 100 m3 a 293.15 K y 101.325 kPa con 4 personas que exhalan 0.9013 kg/dia cada una;
depurador que procesa un caudal Q con eficiencia eta (VALORES ILUSTRATIVOS); mezcla perfecta; sin fugas ni aporte de otros gases.
Verificacion: la integracion numerica coincide con la solucion analitica; sin depurador la subida es lineal; el estado estacionario es G/(eta Q n_molar).
"""
from __future__ import annotations
import math
import platform
import numpy as np

RG, M_CO2 = 8.314462, 0.04401
V, T, P = 100.0, 293.15, 101325.0
PMM = P / 133.322  # mmHg de la cabina


def sim(g_mol_s, k, x0, t_end, dt=10.0):
    """x = fraccion molar; dx/dt = g/n - k x ; k = eta Q / V."""
    n_tot = P * V / (RG * T)
    x, t, tr = x0, 0.0, []
    while t <= t_end + 1e-9:
        tr.append((t, x * PMM))
        x += dt * (g_mol_s / n_tot - k * x)
        t += dt
    return tr


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: modelo propio con caudal y eficiencia ILUSTRATIVOS; umbrales de ppCO2 consultados (OCHMO-TB-004); sin datos de un habitat real")
    R = {}
    n_tot = P * V / (RG * T)
    g1 = 0.9013 / M_CO2 / 86400.0
    crew = 4
    g = crew * g1
    print(f"Cabina {V:.0f} m3: {n_tot:.0f} mol de gas; {crew} personas generan {g*1e3:.4f} mmol/s de CO2 ({crew*0.9013:.2f} kg/dia)")
    dpp = g / n_tot * PMM * 3600
    R["dpp_h"] = dpp
    print(f"Sin depurador: ppCO2 sube {dpp:.3f} mmHg por hora (lineal); 0.5 % de CO2 equivale a {0.005*PMM:.2f} mmHg (consultado 3.8)")
    print("Con depurador (eficiencia eta, caudal Q): estacionario ppCO2_ss = G / (eta Q) en mmHg")
    print("   Q [L/s]   eta   ppCO2_ss [mmHg]   cumple < 3 mmHg")
    ss = {}
    for Q, eta in ((5, 0.7), (10, 0.7), (10, 0.9), (20, 0.7)):
        k = eta * Q * 1e-3 / V
        x_ss = (g / n_tot) / k
        ss[(Q, eta)] = x_ss * PMM
        print(f"   {Q:6.0f}   {eta:4.2f}   {x_ss*PMM:12.3f}        {'si' if x_ss*PMM < 3 else 'no'}")
    R["ss_10"] = ss[(10, 0.7)]
    R["ss_5"] = ss[(5, 0.7)]
    k = 0.7 * 10e-3 / V
    tr = sim(g, k, 0.0, 6 * 3600, dt=10.0)
    x_an = (g / n_tot) / k * (1 - math.exp(-k * 6 * 3600)) * PMM
    R["err"] = abs(tr[-1][1] - x_an)
    print(f"Control: ppCO2 a las 6 h por integracion {tr[-1][1]:.4f} mmHg frente a {x_an:.4f} mmHg analitico (diferencia {R['err']:.1e})")
    assert abs(tr[-1][1] - x_an) < 5e-3
    # falla del depurador a partir del estacionario
    y0 = ss[(10, 0.7)]
    t3 = (3.0 - y0) / dpp
    t45 = (4.5 - y0) / dpp
    R["t3"], R["t45"], R["y0"] = t3, t45, y0
    print(f"Falla del depurador desde el estacionario ({y0:.2f} mmHg): llega a 3 mmHg en {t3:.2f} h y a 4.5 mmHg en {t45:.2f} h")
    for crew2 in (4, 6):
        yss = crew2 * g1 / n_tot / k * PMM
        print(f"Con Q = 10 L/s y eta = 0.7, {crew2} personas: ppCO2_ss = {yss:.2f} mmHg")
    R["ss6"] = 6 * g1 / n_tot / k * PMM
    assert ss[(10, 0.9)] < ss[(10, 0.7)] < ss[(5, 0.7)] and t45 > t3 > 0
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
