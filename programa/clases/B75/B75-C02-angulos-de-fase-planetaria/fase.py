#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C02: angulo de fase de salida (adelanto del destino) y periodo sinodico.

Datos consultados (2026-11-10): periodos siderales de las fichas NASA/NSSDC (Venus 224.701 d, Tierra 365.256 d, Marte 686.980 d, Jupiter 4332.589 d)
y semiejes de las mismas fichas. GM_sol = 1.32712440e11 km3/s2 (valor estandar, no consultado en la pagina).
Modelo: orbitas circulares y coplanares; angulo de fase de salida phi = 180 - 360 * TOF / P_destino (grados, positivo si el destino va por delante).
Pruebas: (1) periodo sinodico por 1/(1/P1 - 1/P2) frente al tiempo en que la separacion angular acumula 360 grados (muestreo; tol. 1e-2 d);
(2) el destino, movido durante el TOF, llega al afelio a 180 grados de la salida (tol. 1e-9 grados).
"""
import math, platform
MU = 1.32712440e11
A = {"Venus": 108.210e6, "Tierra": 149.598e6, "Marte": 227.956e6, "Jupiter": 778.479e6}
P = {"Venus": 224.701, "Tierra": 365.256, "Marte": 686.980, "Jupiter": 4332.589}


def tof_d(r1, r2):
    return math.pi * math.sqrt((0.5 * (r1 + r2)) ** 3 / MU) / 86400


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(" destino   TOF [d]   fase de salida [grados]   P_sinodico [d]   P_sinodico [anios]")
    for dest in ("Venus", "Marte", "Jupiter"):
        t = tof_d(A["Tierra"], A[dest])
        phi = 180.0 - 360.0 * t / P[dest]
        syn = 1.0 / abs(1.0 / P["Tierra"] - 1.0 / P[dest])
        print(f"{dest:8s} {t:8.2f} {phi:18.3f} {syn:19.2f} {syn/365.256:14.3f}")
        lead = phi + 360.0 * t / P[dest]
        assert abs(lead - 180.0) < 1e-9
    dt = 0.01; t = 0.0
    wE, wM = 360.0 / P["Tierra"], 360.0 / P["Marte"]
    sep = 0.0
    while sep < 360.0:
        t += dt; sep = (wE - wM) * t
    syn = 1.0 / (1.0 / P["Tierra"] - 1.0 / P["Marte"])
    print(f"Marte: periodo sinodico por formula = {syn:.4f} d ; por muestreo de la separacion = {t:.4f} d")
    assert abs(t - syn) < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
