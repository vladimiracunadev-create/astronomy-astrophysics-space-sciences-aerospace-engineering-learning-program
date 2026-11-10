#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C16: sensibilidad de una busqueda de radio de banda estrecha y pico de Wien.

Datos: k, h y c de NIST (CODATA 2022, consultados 2026-11-09). Contexto: el resumen de Wright
et al. (2014), arXiv:1408.1134, consultado el 2026-11-09, describe busquedas de calor residual
en el infrarrojo medio (WISE, Spitzer). Todos los parametros del receptor y del transmisor
(T_sis = 25 K, area efectiva 5000 m2, ancho de banda 1 Hz, integracion 100 s, 2 polarizaciones,
SNR umbral 10, EIRP 2e13 W) son SINTETICOS e ILUSTRATIVOS; no describen ningun instrumento
real ni ninguna senal.
Modelo: S_min = SNR (2 k T_sis / A_ef) sqrt(Delta_nu / (n_pol tau)); distancia maxima
d = sqrt(EIRP / (4 pi S_min)). Pico de Wien en longitud de onda: lambda = h c / (x k T) donde
x resuelve x = 5 (1 - exp(-x)), calculado aqui por biseccion.
Supuestos: ruido blanco, senal estrecha dentro de un canal, sin dispersion ni centelleo.
Validez: orden de magnitud. Tolerancia: la fluctuacion relativa de una media de N muestras
simulada (semilla 99) coincide con 1/sqrt(N) a 3 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

K = 1.380649e-23
H = 6.62607015e-34
C = 299792458.0
PC = 3.0857e16  # m, valor ilustrativo


def s_min(snr, t_sis, a_ef, dnu, tau, n_pol=2):
    return snr * 2 * K * t_sis / a_ef * math.sqrt(dnu / (n_pol * tau))


def alcance(eirp, s):
    return math.sqrt(eirp / (4 * math.pi * s))


def x_wien():
    lo, hi = 1.0, 10.0
    f = lambda x: x - 5 * (1 - math.exp(-x))
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def fluctuacion_relativa(N, intentos=4000, semilla=99):
    rng = random.Random(semilla)
    medias = []
    for _ in range(intentos):
        suma = 0.0
        for _ in range(N):
            re, im = rng.gauss(0, 1), rng.gauss(0, 1)
            suma += re * re + im * im
        medias.append(suma / N)
    m = sum(medias) / intentos
    var = sum((x - m) ** 2 for x in medias) / (intentos - 1)
    return math.sqrt(var) / m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    s = s_min(10, 25.0, 5000.0, 1.0, 100.0)
    d = alcance(2e13, s)
    print(f"S_min = {s:.2e} W/m2 ; alcance para EIRP 2e13 W = {d:.2e} m = {d / PC:.0f} pc")
    # La mejora al integrar 4 veces mas tiempo debe ser 2 en sensibilidad
    assert abs(s_min(10, 25.0, 5000.0, 1.0, 400.0) / s - 0.5) < 1e-12
    r1, r16 = fluctuacion_relativa(1), fluctuacion_relativa(16)
    print(f"Fluctuacion relativa de la potencia media: N=1 -> {r1:.3f} ; N=16 -> {r16:.3f} ; cociente = {r1 / r16:.2f} (esperado 4)")
    assert abs(r1 / r16 - 4) / 4 < 0.03
    x = x_wien()
    lam = H * C / (x * K * 300.0)
    print(f"x de Wien = {x:.6f} ; pico a 300 K en lambda = {lam * 1e6:.2f} micras")
    assert abs(x - 4.965114) < 1e-5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
