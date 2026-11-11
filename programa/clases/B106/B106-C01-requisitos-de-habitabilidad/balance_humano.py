#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C01: balance de entradas y salidas de una persona y zonas de temperatura y humedad.

Datos CONSULTADOS (OCHMO-TB-002 rev. B, resumen de NASA-STD-3001 vol. 2 rev. D): consumo en reposo de 5 ml/kg/min con 75 kg;
total de 0.771 kg de O2 por persona y dia en reposo; 5.397 kg/dia para 7 personas; cociente respiratorio 0.85; ingesta media de
3035 kcal/dia; agua minima de 2.5 L/dia; zona de salud 18-27 C y 25-75 % de humedad relativa; zona de desempeno 20-25 C y 30-60 %.
Todo lo demas es calculo propio con gas ideal (R = 8.314462 J/(mol K)); no hay datos medidos de ningun habitat.
Verificacion: el O2 calculado coincide con 0.771 kg/dia (tolerancia 1 %); 7 personas = 7 x una; el calor de 3035 kcal/dia es ~147 W.
"""
from __future__ import annotations
import platform
import numpy as np

R_GAS, M_O2, M_CO2 = 8.314462, 0.0320, 0.04401
MASA, VO2_REPOSO, RQ = 75.0, 5.0e-3, 0.85  # kg; L/(kg min); adimensional


def o2_reposo_kg_dia(masa=MASA, vo2=VO2_REPOSO, T=273.15, P=101325.0):
    litros = vo2 * masa * 1440.0  # L/dia
    rho = P * M_O2 / (R_GAS * T)  # kg/m3 = g/L
    return litros * rho / 1000.0, litros


def en_zona(T, hr, zona):
    t0, t1, h0, h1 = zona
    return t0 <= T <= t1 and h0 <= hr <= h1


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: valores consultados de OCHMO-TB-002 y calculo propio; NINGUNA cifra es una medicion de un habitat real")
    R = {}
    m_o2, litros = o2_reposo_kg_dia()
    mol_o2 = m_o2 / M_O2
    m_co2 = RQ * mol_o2 * M_CO2
    R.update(o2=m_o2, litros=litros, co2=m_co2, mol_o2=mol_o2)
    print(f"O2 en reposo por persona: {litros:.0f} L/dia -> {m_o2:.4f} kg/dia (consultado: 0.771; diferencia {100*(m_o2/0.771-1):+.2f} %)")
    print(f"CO2 exhalado (RQ {RQ}): {RQ*mol_o2:.2f} mol/dia = {m_co2:.4f} kg/dia")
    assert abs(m_o2 / 0.771 - 1) < 0.01
    crew = 7
    R["o2_7"] = crew * m_o2
    print(f"Tripulacion de {crew}: O2 = {crew*m_o2:.3f} kg/dia (consultado: 5.397)")
    assert abs(crew * m_o2 / 5.397 - 1) < 0.01
    # el resumen da +0.376 kg por sesion de ejercicio, pero sus totales (1.083 - 0.771) implican 0.312
    extra_tot = 1.083 - 0.771
    R["extra"] = extra_tot
    exc_L = (45.0 - 5.0) * 1e-3 * MASA * 120.0
    exc_kg = exc_L * (101325.0 * M_O2 / (R_GAS * 273.15)) / 1000.0
    R["exc_kg"] = exc_kg
    print(f"Ejercicio (120 min a 45 ml/kg/min): calculo propio {exc_kg:.3f} kg sobre el reposo; el resumen cita 0.376 pero sus totales implican {extra_tot:.3f} -> no se reproduce con estos supuestos")
    kcal = 3035.0
    w_met = kcal * 4184.0 / 86400.0
    R["w_met"] = w_met
    print(f"Potencia metabolica media: {kcal:.0f} kcal/dia = {w_met:.1f} W por persona (se disipa como calor en la cabina)")
    assert 140 < w_met < 155
    agua_min = 2.5
    print(f"Agua minima para beber (consultada): {agua_min} L/dia por persona; tripulacion de 4 en 30 dias: {4*30*agua_min:.0f} L")
    zs, zd = (18, 27, 25, 75), (20, 25, 30, 60)
    casos = [(22, 45), (26, 70), (19, 28), (29, 40), (24, 65)]
    print("Zonas (texto del resumen, como rectangulos): salud 18-27 C / 25-75 %; desempeno 20-25 C / 30-60 %")
    print("   T [C]  HR [%]   salud  desempeno")
    ns = 0
    for T, h in casos:
        a, b = en_zona(T, h, zs), en_zona(T, h, zd)
        ns += a
        print(f"   {T:5.1f}  {h:6.1f}   {'si' if a else 'no':>5}  {'si' if b else 'no':>9}")
    R["ns"] = ns
    assert en_zona(22, 45, zd) and not en_zona(29, 40, zs)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
