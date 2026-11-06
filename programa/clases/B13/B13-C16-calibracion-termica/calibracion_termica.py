#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C16: calibracion termica de un sensor y balance de un panel.

Datos: constantes exactas del SI (h, c, k; CODATA 2022/BIPM, consultadas
2026-11-05); sigma = 2 pi^5 k^4 / (15 h^3 c^2) se calcula y se compara con el
valor 5.670374419e-8 W m-2 K-4 de CODATA. Luminosidad solar 3.828e26 W
(NASA/NSSDC, Sun Fact Sheet, 2024-05-09) y 1 au = 1.495978707e11 m (IERS TN36).
Punto triple del agua 273.16 K (NIST). Sensor: resistencia lineal SINTETICA
R(T) = 100.000 + 0.3850 (T - 273.16) ohm; segundo punto: bano de referencia de
323.15 K (SINTETICO) con u = 0.020 K; punto triple u = 0.0001 K.
Modelo 1 (calibracion de dos puntos): T = T1 + (R - R1)(T2 - T1)/(R2 - R1);
u^2(T) por propagacion de varianzas (GUM 5.1.2) en R, R1, R2, T1, T2.
Modelo 2 (balance): alpha S = eps sigma T^4 (placa que mira al Sol, cara
trasera aislada) y alpha S = 4 eps sigma T^4 (esfera isotermica); S = L/(4 pi d^2).
Supuestos: sensor lineal; equilibrio estacionario; sin albedo ni calor interno.
Tolerancia: sigma exacta a 1e-9; propagacion analitica vs Monte Carlo 3 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

H, C, K = 6.62607015e-34, 299792458.0, 1.380649e-23
SIGMA_CODATA = 5.670374419e-8
L_SOL, AU = 3.828e26, 1.495978707e11
T1, T2, UT1_, UT2_ = 273.16, 323.15, 0.0001, 0.020
UR = 0.010                       # ohm, incertidumbre de cada lectura de resistencia


def R_true(T):
    return 100.000 + 0.3850 * (T - 273.16)


def T_de_R(R, R1, R2, t1=T1, t2=T2):
    return t1 + (R - R1) * (t2 - t1) / (R2 - R1)


def u_T(R, R1, R2, ur=UR, ut1=UT1_, ut2=UT2_):
    dR = R2 - R1
    f = (R - R1) / dR
    # derivadas parciales
    c_R = (T2 - T1) / dR
    c_R1 = -(T2 - T1) / dR + (R - R1) * (T2 - T1) / dR ** 2
    c_R2 = -(R - R1) * (T2 - T1) / dR ** 2
    c_T1 = 1 - f
    c_T2 = f
    return math.sqrt((c_R * ur) ** 2 + (c_R1 * ur) ** 2 + (c_R2 * ur) ** 2 + (c_T1 * ut1) ** 2 + (c_T2 * ut2) ** 2)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    sigma = 2 * math.pi ** 5 * K ** 4 / (15 * H ** 3 * C ** 2)
    print(f"sigma calculada = {sigma:.9e} ; CODATA = {SIGMA_CODATA:.9e}")
    assert abs(sigma - SIGMA_CODATA) / SIGMA_CODATA < 1e-9
    S = L_SOL / (4 * math.pi * AU ** 2)
    print(f"irradiancia solar a 1 au = {S:.2f} W/m2")
    t_placa = (S / sigma) ** 0.25
    t_esfera = (S / (4 * sigma)) ** 0.25
    print(f"T equilibrio (alpha/eps = 1): placa {t_placa:.2f} K ; esfera {t_esfera:.2f} K")
    assert abs(sigma * t_placa ** 4 - S) < 1e-9 * S
    # sensibilidad: 1 % en alpha/eps -> 0.25 % en T
    t2 = (1.01 * S / sigma) ** 0.25
    print(f"1 % en alpha/eps -> {100*(t2/t_placa-1):.4f} % en T ({t_placa*(t2/t_placa-1):.3f} K)")
    assert abs((t2 / t_placa - 1) - 0.0025) < 1e-4
    # Calibracion sin ruido: recuperacion exacta
    R1, R2 = R_true(T1), R_true(T2)
    for T in (280.0, 300.0, 320.0, 350.0):
        assert abs(T_de_R(R_true(T), R1, R2) - T) < 1e-9
    # Incertidumbre analitica vs Monte Carlo en tres temperaturas
    rng = random.Random(16)
    print("   T (K)   u analitica (K)   u Monte Carlo (K)")
    for T in (275.0, 298.15, 323.15):
        ua = u_T(R_true(T), R1, R2)
        vals = []
        for _ in range(60000):
            r1 = R1 + rng.gauss(0, UR)
            r2 = R2 + rng.gauss(0, UR)
            r = R_true(T) + rng.gauss(0, UR)
            t1 = T1 + rng.gauss(0, UT1_)
            t2_ = T2 + rng.gauss(0, UT2_)
            vals.append(T_de_R(r, r1, r2, t1, t2_))
        m = sum(vals) / len(vals)
        sd = math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))
        print(f"{T:8.2f}   {ua:12.5f}     {sd:12.5f}")
        assert abs(sd - ua) / ua < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
