#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C10: densidad, gravedad superficial y velocidad de escape; propagacion de incertidumbres de masa y radio.

Datos: G (NIST CODATA 2022), GM_E, GM_J, R_E(ecuatorial), R_J(ecuatorial) (IAU 2015 B3), consultados 2026-11-09. Contexto: Weiss y Marcy estudian la relacion
masa-radio de 65 exoplanetas menores que 4 radios terrestres y hallan una densidad maxima de 7.6 g/cc a 1.4 radios terrestres (arXiv:1312.0936, resumen);
Chen y Kipping presentan un modelo probabilistico de masa y radio condicionado a 316 objetos (arXiv:1603.08614, resumen), consultados 2026-11-09. Las
masas y radios del planeta sintetico (5 +/- 1 M_E, 1.5 +/- 0.1 R_E) son ILUSTRATIVOS.
Modelo: rho = 3 M/(4 pi R^3); g = G M/R^2; v_esc = sqrt(2 G M/R). Propagacion lineal: (sigma_rho/rho)^2 = (sigma_M/M)^2 + (3 sigma_R/R)^2; comparada con un
Monte Carlo (semilla fija) con masa y radio gaussianos independientes.
Supuestos: planeta esferico, errores gaussianos independientes. Validez: errores relativos pequenos.
Tolerancia: la desviacion Monte Carlo de rho dentro del 10 % de la lineal con errores grandes y del 2 % con errores pequenos; densidad de la Tierra y de Jupiter a partir de GM y R con 1e-12 de consistencia.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

G = 6.67430e-11
GM_E, GM_J = 3.986004e14, 1.2668653e17
R_E, R_J = 6.3781e6, 7.1492e7
M_E, M_J = GM_E / G, GM_J / G


def densidad(m, r):
    return 3 * m / (4 * math.pi * r ** 3)


def gravedad(m, r):
    return G * m / r ** 2


def v_escape(m, r):
    return math.sqrt(2 * G * m / r)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"M_E = {M_E:.4e} kg ; M_J = {M_J:.4e} kg ; M_J/M_E = {M_J / M_E:.3f}")
    print(f"{'objeto':<22} {'M [M_E]':>9} {'R [R_E]':>8} {'rho [g/cc]':>11} {'g [m/s2]':>9} {'v_esc [km/s]':>13}")
    cuerpos = (("Tierra", M_E, R_E), ("Jupiter", M_J, R_J), ("sintetico 1.4 R_E", 4.0 * M_E, 1.4 * R_E), ("sintetico 4 R_E", 15.0 * M_E, 4.0 * R_E))
    for nombre, m, r in cuerpos:
        print(f"{nombre:<22} {m / M_E:9.3f} {r / R_E:8.3f} {densidad(m, r) / 1000:11.3f} {gravedad(m, r):9.3f} {v_escape(m, r) / 1e3:13.3f}")
    # consistencia: rho(Tierra) = 3 GM/(4 pi G R^3)
    assert abs(densidad(M_E, R_E) / (3 * GM_E / (4 * math.pi * G * R_E ** 3)) - 1) < 1e-12
    # propagacion de incertidumbres
    m0, sm, r0, sr = 5.0 * M_E, 1.0 * M_E, 1.5 * R_E, 0.1 * R_E
    rho0 = densidad(m0, r0)
    lin = rho0 * math.sqrt((sm / m0) ** 2 + (3 * sr / r0) ** 2)
    rng = random.Random(20261109)
    muestras = [densidad(rng.gauss(m0, sm), rng.gauss(r0, sr)) for _ in range(200000)]
    mc_m, mc_s = statistics.mean(muestras), statistics.pstdev(muestras)
    print(f"planeta sintetico: M = 5 +/- 1 M_E, R = 1.5 +/- 0.1 R_E -> rho central = {rho0 / 1000:.3f} g/cc")
    print(f"propagacion lineal: sigma_rho = {lin / 1000:.3f} g/cc ({lin / rho0 * 100:.1f} %) ; Monte Carlo: media = {mc_m / 1000:.3f}, sigma = {mc_s / 1000:.3f} g/cc ({mc_s / mc_m * 100:.1f} %)")
    assert abs(mc_s / lin - 1) < 0.10, "propagacion lineal frente a Monte Carlo (errores grandes)"
    # caso de errores pequenos: la propagacion lineal es buena
    m1, s1, r1, s1r = 5.0 * M_E, 0.25 * M_E, 1.5 * R_E, 0.03 * R_E
    lin1 = densidad(m1, r1) * math.sqrt((s1 / m1) ** 2 + (3 * s1r / r1) ** 2)
    mu1 = [densidad(rng.gauss(m1, s1), rng.gauss(r1, s1r)) for _ in range(200000)]
    print(f"errores pequenos (5 % en masa, 2 % en radio): lineal = {lin1 / 1000:.4f} g/cc ; Monte Carlo = {statistics.pstdev(mu1) / 1000:.4f} g/cc ; cociente = {statistics.pstdev(mu1) / lin1:.4f}")
    assert abs(statistics.pstdev(mu1) / lin1 - 1) < 0.02, "propagacion lineal con errores pequenos"
    # contribucion de cada fuente
    fm, fr = sm / m0, 3 * sr / r0
    print(f"contribuciones al error relativo de rho: masa {fm * 100:.1f} % ; radio (x3) {fr * 100:.1f} %")
    # sesgo de la media por la no linealidad
    print(f"media Monte Carlo / valor central = {mc_m / rho0:.4f}")
    # precision necesaria
    for ms_rel in (0.20, 0.10, 0.05):
        print(f"con error de masa {ms_rel * 100:.0f} % y de radio 3 %: sigma_rho/rho = {math.sqrt(ms_rel ** 2 + (3 * 0.03) ** 2) * 100:.1f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
