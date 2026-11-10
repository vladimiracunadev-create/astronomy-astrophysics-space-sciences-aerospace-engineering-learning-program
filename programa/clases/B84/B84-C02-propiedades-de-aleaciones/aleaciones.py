#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C02: curva de Ramberg-Osgood, limite elastico al 0,2 % e indices especificos de cuatro aleaciones.

DATOS ILUSTRATIVOS (valores tipicos redondeados; NO consultados en una fuente concreta y NO son valores de diseno certificados):
  aleacion        E [GPa]  rho [kg/m3]  sigma_0.2 [MPa]  n (Ramberg-Osgood)
  Al 6061-T6        69        2700          275              20
  Ti-6Al-4V        114        4430          880              25
  Inconel 718      200        8190         1030              15
  Acero 304 recoc. 193        8000          215               7
Modelo: eps = sigma/E + 0,002 (sigma/sigma_0.2)^n  (Ramberg-Osgood). Segunda via: interseccion numerica de la curva con la recta
sigma = E (eps - 0,002) (definicion del limite elastico al 0,2 % de deformacion plastica) y energia por integracion numerica.
Unidades: SI (Pa, kg, m). Tolerancias: limite al 0,2 % recuperado con error relativo < 1e-9; energia numerica vs analitica < 1e-6.
"""
from __future__ import annotations
import math, platform

ALEACIONES = {  # E [Pa], rho, sigma02 [Pa], n
    "Al 6061-T6": (69e9, 2700.0, 275e6, 20.0),
    "Ti-6Al-4V": (114e9, 4430.0, 880e6, 25.0),
    "Inconel 718": (200e9, 8190.0, 1030e6, 15.0),
    "Acero 304": (193e9, 8000.0, 215e6, 7.0),
}


def deformacion(sig, E, s02, n):
    return sig / E + 0.002 * (sig / s02) ** n


def limite_offset(E, s02, n):
    """Raiz de eps(sig) - sig/E = 0,002 por biseccion: la plastica a sigma debe ser 0,002."""
    lo, hi = 0.1 * s02, 3.0 * s02
    f = lambda s: deformacion(s, E, s02, n) - s / E - 0.002
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def energia_numerica(E, s02, n, sig_max, pasos=200000):
    """Integral de eps d(sigma) (complementaria) con regla del trapecio."""
    h = sig_max / pasos
    s = 0.0
    for i in range(pasos):
        a, b = i * h, (i + 1) * h
        s += 0.5 * (deformacion(a, E, s02, n) + deformacion(b, E, s02, n)) * h
    return s


def energia_analitica(E, s02, n, sig_max):
    return sig_max ** 2 / (2 * E) + 0.002 * s02 / (n + 1) * (sig_max / s02) ** (n + 1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Aleaciones con datos ILUSTRATIVOS (valores tipicos, no consultados)")
    print(f"{'aleacion':12s} {'E/rho':>9s} {'s02/rho':>9s} {'E^1/3/rho':>12s} {'resil. [kJ/m3]':>15s}   (E/rho en MN m/kg; s02/rho en kN m/kg; E^1/3/rho en GPa^1/3 por Mg/m3)")
    filas = {}
    for nom, (E, rho, s02, n) in ALEACIONES.items():
        er = E / rho / 1e6
        sr = s02 / rho / 1e3
        idx = (E / 1e9) ** (1 / 3) / (rho / 1e3)  # indice de panel rigido: GPa^(1/3) / (Mg/m3)
        res = s02 ** 2 / (2 * E) / 1e3
        filas[nom] = (er, sr, idx, res)
        print(f"{nom:12s} {er:9.2f} {sr:9.1f} {idx:12.3f} {res:15.1f}")
    print("Limite elastico al 0,2 % (biseccion) frente al dato de entrada:")
    emax = 0.0
    for nom, (E, rho, s02, n) in ALEACIONES.items():
        s = limite_offset(E, s02, n)
        err = abs(s - s02) / s02
        emax = max(emax, err)
        eps = deformacion(s02, E, s02, n)
        print(f"  {nom:12s} sigma = {s / 1e6:8.3f} MPa  eps total = {eps * 100:.4f} %  error relativo = {err:.1e}")
    print("Energia complementaria hasta sigma_0.2 (trapecio frente a formula cerrada):")
    ee = 0.0
    for nom, (E, rho, s02, n) in ALEACIONES.items():
        a = energia_numerica(E, s02, n, s02)
        b = energia_analitica(E, s02, n, s02)
        ee = max(ee, abs(a - b) / b)
        print(f"  {nom:12s} numerica = {a / 1e3:9.3f} kJ/m3  analitica = {b / 1e3:9.3f} kJ/m3")
    # Mejor aleacion segun cada indice
    for k, nombre in ((0, "rigidez especifica E/rho"), (1, "resistencia especifica s02/rho"), (2, "panel rigido E^(1/3)/rho")):
        mejor = max(filas, key=lambda x: filas[x][k])
        print(f"Mejor por {nombre}: {mejor}")
    assert emax < 1e-9, emax
    assert ee < 1e-6, ee
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
