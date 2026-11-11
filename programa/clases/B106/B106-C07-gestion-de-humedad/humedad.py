#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C07: psicrometria basica de una cabina: punto de rocio, carga latente y riesgo de condensacion.

Consultado (OCHMO-TB-002): zona de salud 18-27 C y 25-75 % de humedad relativa; zona de desempeno 20-25 C y 30-60 %; el resumen cita 3.870 kg/dia por persona de
liquido por respiracion y sudor (combinado con la orina), que se usa solo como cota superior. ILUSTRATIVOS: vapor emitido de 1.5 kg/dia por persona,
cabina de 120 m3 a 101.325 kPa, temperatura de pared de 12 C y de serpentin de 7 C. Formula de Magnus para la presion de saturacion (constantes de manual,
NO consultadas): e_s = 6.112 exp(17.62 T/(243.12 + T)) hPa, valida de 0 a 60 C aprox.
Verificacion: dew point(T, 100 %) = T; la relacion de humedad a 22 C y 50 % coincide con el valor de tablas de manual (~8.3 g/kg) dentro del 3 %.
"""
from __future__ import annotations
import math
import platform
import numpy as np

P_HPA, LV = 1013.25, 2.45e6  # hPa; J/kg


def es(T):
    return 6.112 * math.exp(17.62 * T / (243.12 + T))


def rocio(T, hr):
    g = math.log(hr / 100.0 * es(T) / 6.112)
    return 243.12 * g / (17.62 - g)


def w_hum(T, hr):
    pv = hr / 100.0 * es(T)
    return 0.622 * pv / (P_HPA - pv)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: formula de Magnus (manual, NO consultada) y valores ILUSTRATIVOS de emision y de temperaturas; limites T-HR consultados")
    R = {}
    print("   T [C]  HR [%]   punto de rocio [C]   w [g/kg]")
    for T, h in ((22, 45), (22, 50), (24, 60), (26, 70)):
        print(f"   {T:5.1f}  {h:6.1f}   {rocio(T,h):16.2f}   {1000*w_hum(T,h):8.2f}")
    R["td_22_50"], R["w_22_50"] = rocio(22, 50), 1000 * w_hum(22, 50)
    assert abs(rocio(22, 100) - 22) < 1e-9 and abs(R["w_22_50"] / 8.3 - 1) < 0.03
    V, T = 120.0, 22.0
    rho = 101325.0 / (287.05 * (T + 273.15))
    m_aire = rho * V
    n_p, e_kg = 4, 1.5
    gen = n_p * e_kg / 86400.0  # kg/s
    w0, w1 = w_hum(T, 45), w_hum(T, 75)
    t_sube = (w1 - w0) * m_aire / gen / 3600.0
    R["t_sube"], R["m_aire"] = t_sube, m_aire
    print(f"Cabina {V:.0f} m3 a {T:.0f} C: {m_aire:.0f} kg de aire; {n_p} personas emiten {n_p*e_kg:.1f} kg/dia de vapor (ilustrativo)")
    print(f"Sin retirar vapor, la HR pasa de 45 % a 75 % (limite de salud) en {t_sube:.1f} h")
    q_lat = gen * LV
    R["q_lat"] = q_lat
    print(f"Carga latente: {q_lat:.0f} W; con 3.870 kg/dia por persona (cota superior consultada, ambigua) seria {n_p*3.870/86400*LV:.0f} W")
    Tw, Tc = 12.0, 7.0
    td = rocio(T, 45)
    R["td45"] = td
    print(f"Punto de rocio a {T:.0f} C y 45 %: {td:.2f} C. Pared a {Tw:.0f} C: {'condensa' if Tw < td else 'no condensa'} (margen {Tw-td:+.2f} C); serpentin a {Tc:.0f} C: {'condensa' if Tc < td else 'no condensa'}")
    w_c = w_hum(Tc, 100)
    cap = (w0 - w_c)
    flujo = 0.5  # kg/s de aire por el serpentin (ilustrativo)
    cond = flujo * cap * 86400.0 / 1.0
    R["cond"] = cond
    print(f"Serpentin saturado a {Tc:.0f} C: w = {1000*w_c:.2f} g/kg; con 0.5 kg/s de aire retira {flujo*cap*1000:.2f} g/s = {cond:.0f} kg/dia (genera {n_p*e_kg:.1f} kg/dia -> sobra capacidad)")
    assert Tc < td and cond > n_p * e_kg
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
