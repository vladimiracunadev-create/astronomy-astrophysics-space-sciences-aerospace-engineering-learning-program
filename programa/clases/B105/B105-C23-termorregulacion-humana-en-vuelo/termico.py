#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C23: balance de calor del cuerpo en un hábitat sin conveccion natural (modelo DIDACTICO, parametros ILUSTRATIVOS).

Balance: S = M - W - E - (C + R). Metabolismo M = 100 W en reposo y 450 W en ejercicio; trabajo externo W = 50 W en ejercicio. Perdida seca C + R = h A (T_piel - T_amb) con
h = h_r + h_c; h_r = 4.5 W/(m2 K) (radiacion, valor tipico de ensenanza); conveccion natural h_c = 3.0 W/(m2 K) en la Tierra y h_c ~ 0 en microgravedad sin ventilacion
(sin flotabilidad); ventilacion forzada: h_c = 8.3 v^0.6 (v en m/s; relacion de confort termico usada como ejemplo, NO consultada aqui). Area A = 1.9 m2; T_piel = 33 C;
T_amb = 22 C. Evaporacion maxima E_max = 450 W (ILUSTRATIVA); sudor evaporado m_s = E / lambda con lambda = 2.43e6 J/kg. Acumulacion S -> dT/dt = S/(m c) con m = 75 kg y
c = 3470 J/(kg K) (calor especifico corporal de ensenanza). Todo ILUSTRATIVO. Contenido educativo: no es una pauta de seguridad termica. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

A, M_C, C_ESP, LAM = 1.9, 75.0, 3470.0, 2.43e6
HR = 4.5


def perdida_seca(hc, t_amb=22.0, t_piel=33.0):
    return (HR + hc) * A * (t_piel - t_amb)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS ILUSTRATIVOS: sin mediciones; relaciones de confort y calor especifico no consultadas")
    escenarios = {"Tierra, conveccion natural (h_c = 3.0)": 3.0, "microgravedad sin ventilacion (h_c = 0)": 0.0, "microgravedad con ventilacion 0.2 m/s": 8.3 * 0.2 ** 0.6, "microgravedad con ventilacion 0.5 m/s": 8.3 * 0.5 ** 0.6}
    print("escenario                                     h_c [W/m2K]   perdida seca a 22 C [W]   a 28 C [W]")
    for n, hc in escenarios.items():
        print(f"  {n:44s} {hc:6.2f}        {perdida_seca(hc):7.1f}                  {perdida_seca(hc, 28.0):7.1f}")
    print("Reposo (M = 100 W, W = 0): calor a disipar = 100 W")
    print("Ejercicio (M = 450 W, W = 50 W): calor a disipar = 400 W")
    print("escenario                                     seca [W]   evaporacion necesaria [W]   sudor [g/h]   S sin sudor [W]   dT/h sin sudor [C]")
    res = {}
    for n, hc in escenarios.items():
        seca = perdida_seca(hc)
        e_nec = max(0.0, 400 - seca)
        sudor = e_nec / LAM * 3600 * 1000
        s = 400 - seca
        dt_h = s * 3600 / (M_C * C_ESP)
        res[n] = (seca, e_nec, sudor, dt_h)
        print(f"  {n:44s} {seca:7.1f}    {e_nec:7.1f}                  {sudor:7.1f}      {s:7.1f}            {dt_h:6.2f}")
    # evolucion de la temperatura central en ejercicio sin evaporacion adicional ni ventilacion, 1 h
    print("Sin ventilacion en microgravedad, ejercicio de 1 h, evaporacion limitada a E_max = 450 W e igual a lo necesario (no sube T_central si E >= necesaria).")
    e_nec0 = res["microgravedad sin ventilacion (h_c = 0)"][1]
    print(f"  E necesaria = {e_nec0:.1f} W <= E_max = 450 W: la evaporacion basta si el sudor se evapora; si el sudor no se evapora (humedad alta, aire estancado), la piel se moja y el calor no sale.")
    for frac in (1.0, 0.75, 0.5, 0.25):
        s = e_nec0 * (1 - frac)
        t60 = s * 3600 / (M_C * C_ESP)
        t1 = "sin aumento" if s <= 0 else f"{M_C * C_ESP / s / 60:7.1f} min"
        print(f"  fraccion del sudor que se evapora = {frac:4.2f}: acumulacion {s:6.1f} W; aumento de T central en 1 h = {t60:5.2f} C; tiempo para +1 C = {t1}")
    assert abs(perdida_seca(3.0) - 7.5 * 1.9 * 11) < 1e-9
    assert res["microgravedad sin ventilacion (h_c = 0)"][0] < res["Tierra, conveccion natural (h_c = 3.0)"][0]
    assert res["microgravedad con ventilacion 0.5 m/s"][0] > res["microgravedad sin ventilacion (h_c = 0)"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
