#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C12: montura ecuatorial: velocidad sidérea, periodo del tornillo sin fin y error periodico.

Datos: ILUSTRATIVOS (corona de 144 dientes, amplitud del error periodico 10", escala de imagen 1,0"/pixel). Duracion del ano tropico 365,2422 dias y del dia solar medio 86400 s (definicion del segundo del SI,
no consultados otros datos). Constantes: 1 vuelta = 1296000" (definicion).
Modelo: dia sideral = 86400 T/(T + 1) con T el ano tropico en dias; velocidad sidérea = 1296000"/dia sideral; periodo del tornillo T_w = dia sideral/N_dientes;
error periodico e(t) = A sin(2 pi t/T_w + phi); deriva en una exposicion de duracion tau: maximo sobre la fase de |e(t0 + tau) - e(t0)| = 2 A sin(pi tau/T_w) para tau <= T_w/2.
Verificacion independiente: barrido numerico de la fase inicial (3600 pasos) frente a la formula.
Supuestos: error periodico sinusoidal puro, sin deriva lenta, montura perfectamente alineada. Validez: ilustrativa.
Tolerancia: maximo numerico frente a formula, 1e-4 relativo; velocidad sidérea 15,0411"/s +- 1e-4.
"""
from __future__ import annotations
import math, platform

TROP = 365.2422; DIA = 86400.0
N_DIENTES = 144; A_PE = 10.0

def calc():
    r = {}
    dia_sid = DIA * TROP / (TROP + 1)
    r["dia_sideral_s"] = dia_sid
    r["vel_sidera"] = 1296000.0 / dia_sid
    r["vel_solar"] = 1296000.0 / DIA
    r["dif_vel"] = r["vel_sidera"] - r["vel_solar"]
    r["deriva_60s_arcsec"] = r["dif_vel"] * 60
    Tw = dia_sid / N_DIENTES
    r["T_gusano_s"] = Tw
    r["max_vel_pe"] = 2 * math.pi * A_PE / Tw
    filas = []
    for tau in (30.0, 60.0, 120.0, 240.0):
        mx = 0.0
        for k in range(3600):
            ph = 2 * math.pi * k / 3600
            d = abs(A_PE * math.sin(2 * math.pi * tau / Tw + ph) - A_PE * math.sin(ph))
            if d > mx:
                mx = d
        filas.append((tau, mx, 2 * A_PE * math.sin(math.pi * tau / Tw)))
    r["filas"] = filas
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k in ("dia_sideral_s", "vel_sidera", "vel_solar", "dif_vel", "deriva_60s_arcsec", "T_gusano_s", "max_vel_pe"):
        print(f"{k} = {r[k]:.6g}")
    print("exposicion (s) | deriva maxima numerica (arcsec) | formula (arcsec)")
    for t, a, b in r["filas"]:
        print(f"{t:.0f} | {a:.4f} | {b:.4f}")
    assert abs(r["vel_sidera"] - 15.0411) < 1e-4
    for t, a, b in r["filas"]:
        assert abs(a - b) / b < 1e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
