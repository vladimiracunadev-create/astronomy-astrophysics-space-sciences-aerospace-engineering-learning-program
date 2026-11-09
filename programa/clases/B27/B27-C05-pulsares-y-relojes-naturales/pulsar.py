#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C05: campo, edad y energia de frenado de un pulsar, y funcion de masa de un pulsar binario.

Datos (NIST CODATA 2022 e IAU 2015 B3, consultados 2026-11-09): mu_0, c, G, GM_sol. Pulsar de ejemplo
(P = 0.033 s, dP/dt = 4.2e-13, I = 1e38 kg m2, R = 1e4 m): valores ILUSTRATIVOS (sinteticos). Pulsar binario:
masas 2.01 y 0.172 Msol y periodo orbital 2.46 h (Antoniadis et al., arXiv:1304.6875, resumen, consultado
2026-11-09); inclinacion de 90 grados (ILUSTRATIVA).
Modelo: dipolo magnetico en rotacion en el vacio: potencia radiada P_rad = (8 pi/3) B^2 R^6 w^4/(mu_0 c^3) (B en el
ecuador), igualada a la perdida de energia rotacional I w |dw/dt|, con w = 2 pi/P y dw/dt = -2 pi Pdot/P^2:
B = sqrt(3 mu_0 c^3 I P Pdot/(32 pi^3 R^6)). Edad caracteristica tau = P/(2 Pdot). Funcion de masa de un binario:
f = 4 pi^2 (a1 sin i)^3/(G P_b^2) = (m2 sin i)^3/(m1 + m2)^2.
Supuestos: dipolo en el vacio, indice de frenado n = 3, momento de inercia fijo. Validez: ilustrativa.
Tolerancia: 5 % frente a la formula usual B = 3.2e15 sqrt(P Pdot) T; 1e-9 en la funcion de masa.
"""
from __future__ import annotations
import math
import platform
import sys

MU0, C, G = 1.25663706127e-6, 299792458.0, 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
I_NS, R_NS = 1e38, 1e4
YR = 365.25 * 86400.0


def campo(P, Pdot, I=I_NS, R=R_NS):
    return math.sqrt(3 * MU0 * C ** 3 * I * P * Pdot / (32 * math.pi ** 3 * R ** 6))


def edad(P, Pdot):
    return P / (2 * Pdot)


def edot_frenado(P, Pdot, I=I_NS):
    w = 2 * math.pi / P
    wd = -2 * math.pi * Pdot / P ** 2
    return -I * w * wd


def edot_dipolo(B, P, R=R_NS):
    w = 2 * math.pi / P
    return 8 * math.pi / 3 * B ** 2 * R ** 6 * w ** 4 / (MU0 * C ** 3)


def funcion_masa(m1, m2, sini=1.0):
    return (m2 * sini) ** 3 / (m1 + m2) ** 2


def a1_sini(f, Pb):
    return (f * M_SOL * G * Pb ** 2 / (4 * math.pi ** 2)) ** (1 / 3)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    P, Pd = 0.033, 4.2e-13
    B = campo(P, Pd)
    coef = B / math.sqrt(P * Pd)
    assert abs(coef / 3.2e15 - 1) < 0.05, "coeficiente fuera del 5 % de 3.2e15 T"
    e1, e2 = edot_frenado(P, Pd), edot_dipolo(B, P)
    assert abs(e1 / e2 - 1) < 1e-9, "balance de energia"
    print(f"B = {B:.3e} T (coeficiente {coef:.3e} T) ; edad caracteristica = {edad(P, Pd) / YR:.0f} anios")
    print(f"Edot (frenado) = {e1:.3e} W ; Edot (dipolo) = {e2:.3e} W")
    print(f"energia rotacional = {0.5 * I_NS * (2 * math.pi / P) ** 2:.3e} J")
    # indice de frenado n = 3: tiempo de vida con P(t)^2 = P0^2 + 2 P Pdot t
    P0, t = 0.033, 1000 * YR
    P1 = math.sqrt(P0 ** 2 + 2 * P0 * Pd * t)
    print(f"tras 1000 anios (Pdot constante): P = {P1:.5f} s")
    # pulsar binario
    m1, m2, Pb = 2.01, 0.172, 2.46 * 3600.0
    f = funcion_masa(m1, m2)
    a = a1_sini(f, Pb)
    print(f"funcion de masa f = {f:.5e} Msol ; a1 sen i = {a / 1e3:.0f} km = {a / C:.4f} s-luz")
    # inversion: dado f, m1 e i recuperar m2 por biseccion
    lo, hi = 1e-6, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if funcion_masa(m1, mid) < f:
            lo = mid
        else:
            hi = mid
    assert abs(0.5 * (lo + hi) / m2 - 1) < 1e-9, "inversion de la funcion de masa"
    print(f"inversion: m2 = {0.5 * (lo + hi):.6f} Msol (dado f, m1 = {m1}, i = 90 grados)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
