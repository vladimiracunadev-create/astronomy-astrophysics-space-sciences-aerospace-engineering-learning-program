#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C08: balance termico de una cabina, caudal de refrigerante y area de radiador.

Consultado (OCHMO-TB-002): zona de desempeno 20-25 C y limite de salud hasta 27 C; ingesta media de 3035 kcal/dia (147 W por persona, C01).
ILUSTRATIVOS: equipos de 3000 W, radiador a 285 K con emisividad 0.85, sumideros efectivos de 200 K y de 270 K, agua con cp = 4186 J/(kg K), aire con cp = 1005 J/(kg K),
capacidad termica del conjunto aire + estructura de 2e6 J/K. Constante de Stefan-Boltzmann 5.670374e-8 W/(m2 K4) (valor de manual, NO consultado).
Verificacion: el area del radiador coincide con la formula Q/(e sigma (T^4 - Ts^4)); un sumidero mas caliente exige mas area; el tiempo a 27 C usa dT/dt = Q/C.
"""
from __future__ import annotations
import platform
import numpy as np

SIG = 5.670374e-8


def area_rad(Q, Tr, Ts, eps=0.85):
    return Q / (eps * SIG * (Tr ** 4 - Ts ** 4))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: modelo propio con potencias, emisividad y sumideros ILUSTRATIVOS; limites de temperatura consultados; sin datos de un habitat")
    R = {}
    crew = 4
    q_crew = crew * 3035 * 4184 / 86400.0
    q_eq = 3000.0
    Q = q_crew + q_eq
    R["q_crew"], R["Q"] = q_crew, Q
    print(f"Carga: tripulacion {crew} x 147 W = {q_crew:.0f} W + equipos {q_eq:.0f} W = {Q:.0f} W")
    print("Radiador a 285 K (emisividad 0.85):")
    print("   sumidero [K]   area [m2]   (con una cara; una cara que ve el sumidero)")
    for Ts in (200.0, 250.0, 270.0):
        print(f"   {Ts:9.0f}   {area_rad(Q, 285.0, Ts):9.2f}")
    R["a200"], R["a270"] = area_rad(Q, 285.0, 200.0), area_rad(Q, 285.0, 270.0)
    assert R["a270"] > R["a200"]
    a_chk = Q / (0.85 * SIG * (285.0 ** 4 - 200.0 ** 4))
    assert abs(a_chk - R["a200"]) < 1e-12
    dT = 5.0
    m_w = Q / (4186.0 * dT)
    m_a = Q / (1005.0 * dT)
    rho = 1.2
    R["m_w"], R["m_a"], R["v_a"] = m_w, m_a, m_a / rho
    print(f"Lazo de agua con salto de {dT:.0f} K: {m_w:.3f} kg/s ({m_w*60:.1f} L/min); lazo de aire con el mismo salto: {m_a:.3f} kg/s = {m_a/rho:.2f} m3/s ({m_a/rho*1000:.0f} L/s)")
    C = 2.0e6
    Tz = 22.0
    t27 = (27.0 - Tz) * C / Q / 3600.0
    R["t27"], R["rate"] = t27, Q / C * 3600.0
    print(f"Si falla el enfriamiento desde {Tz:.0f} C: sube {Q/C*3600:.2f} K/h; llega a 27 C (limite de salud consultado) en {t27:.2f} h")
    # flujo solar ilustrativo sobre el radiador: 1361 W/m2 con absortividad 0.2
    q_sol = 1361.0 * 0.2
    R["rad_neto"] = 0.85 * SIG * (285.0 ** 4 - 200.0 ** 4) - q_sol
    print(f"Radiador mirando al Sol (absortividad 0.2, 1361 W/m2): absorbe {q_sol:.0f} W/m2 y su capacidad neta cae de {0.85*SIG*(285**4-200**4):.0f} a {R['rad_neto']:.0f} W/m2")
    assert R["rad_neto"] < 0.85 * SIG * (285.0 ** 4 - 200.0 ** 4)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
