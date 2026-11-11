#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C21: presiones parciales respiratorias y atmosferas de cabina (calculo; atmosferas ILUSTRATIVAS).

Ecuacion del gas alveolar: PAO2 = FiO2 (Pb - PH2O) - PaCO2 / R, con PH2O = 6.28 kPa (47 mmHg, vapor de agua a 37 grados C; valor estandar, no consultado aqui),
PaCO2 = 5.33 kPa (40 mmHg) y cociente respiratorio R = 0.8 (valores de referencia de ensenanza). Presion inspirada de O2: PIO2 = FiO2 (Pb - PH2O).
Cabinas ILUSTRATIVAS (no son especificaciones de ninguna agencia): A) 101.325 kPa, 21 % O2; B) 70.3 kPa, 26.5 % O2; C) 56.5 kPa, 34 % O2.
Altitud equivalente con la atmosfera estandar ISA: p = 101.325 (1 - 2.25577e-5 h)^5.25588 kPa (formula estandar, no consultada). CO2 ambiente: p_CO2 = ppm x 1e-6 x P_total.
Con CO2 inspirado elevado se supone PaCO2 = PaCO2_0 + 0.9 PICO2 / 1 (aproximacion didactica de la elevacion). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

PH2O, PACO2, R = 6.28, 5.33, 0.8
MMHG = 0.133322


def pio2(pb, fio2):
    return fio2 * (pb - PH2O)


def pao2(pb, fio2, paco2=PACO2, r=R):
    return fio2 * (pb - PH2O) - paco2 / r


def altitud_isa(p):
    return (1 - (p / 101.325) ** (1 / 5.25588)) / 2.25577e-5


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: constantes estandar no consultadas; cabinas ILUSTRATIVAS; sin mediciones")
    cabinas = {"A (101.325 kPa, 21 % O2)": (101.325, 0.21), "B (70.3 kPa, 26.5 % O2)": (70.3, 0.265), "C (56.5 kPa, 34 % O2)": (56.5, 0.34)}
    print("cabina                      PIO2 [kPa] [mmHg]   PAO2 [kPa] [mmHg]   O2 ambiente [kPa]   N2 ambiente [kPa]   altitud ISA equivalente [m]")
    res = {}
    for n, (pb, f) in cabinas.items():
        a, b = pio2(pb, f), pao2(pb, f)
        res[n] = (a, b)
        print(f"{n:28s} {a:6.2f} {a / MMHG:6.1f}     {b:6.2f} {b / MMHG:6.1f}       {pb * f:6.2f}            {pb * (1 - f):6.2f}            {altitud_isa(pb):7.0f}")
    print("Efecto del CO2 ambiente en la cabina A (elevacion didactica de PaCO2 = 0.9 PICO2):")
    for ppm in (400, 2000, 5000, 10000, 20000):
        pc = ppm * 1e-6 * 101.325
        pa = PACO2 + 0.9 * pc
        print(f"  {ppm:6d} ppm: p_CO2 ambiente = {pc:6.3f} kPa ({pc / MMHG:5.2f} mmHg); PaCO2 = {pa:5.2f} kPa; PAO2 = {pao2(101.325, 0.21, pa):6.2f} kPa")
    # el efecto de la ventilacion: PaCO2 inversamente proporcional a la ventilacion alveolar
    print("PaCO2 y PAO2 con ventilacion alveolar relativa v (PaCO2 = 5.33/v):")
    for v in (0.5, 0.75, 1.0, 1.5, 2.0):
        pa = PACO2 / v
        print(f"  v = {v:4.2f}: PaCO2 = {pa:5.2f} kPa; PAO2 (cabina A) = {pao2(101.325, 0.21, pa):6.2f} kPa; (cabina B) = {pao2(70.3, 0.265, pa):6.2f} kPa")
    # Gravedad y perfusion: gradiente hidrostatico en el pulmon (altura 0.24 m)
    h = 0.24
    print(f"Gradiente hidrostatico de la sangre a lo largo del pulmon (h = {h} m, rho = 1060): Tierra {1060 * 9.81 * h / 1000:.2f} kPa = {1060 * 9.81 * h * 1e-3 / MMHG:.1f} mmHg; microgravedad 0")
    assert abs(pio2(101.325, 0.21) - 19.96) < 0.01
    assert abs(pao2(101.325, 0.21) - 13.30) < 0.02
    assert abs(altitud_isa(101.325)) < 1e-6
    assert 2900 < altitud_isa(70.3) < 3100
    assert res["B (70.3 kPa, 26.5 % O2)"][1] > 0 and res["B (70.3 kPa, 26.5 % O2)"][0] > 0.8 * res["A (101.325 kPa, 21 % O2)"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
