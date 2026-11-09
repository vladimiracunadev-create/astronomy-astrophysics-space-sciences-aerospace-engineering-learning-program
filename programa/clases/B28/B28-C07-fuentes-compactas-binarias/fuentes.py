#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C07: frecuencia de ultima orbita, alcance de deteccion y numero esperado de eventos de binarias compactas.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Contexto: GWTC-1 reporta tres fusiones de
agujeros negros en O1 y la primera de estrellas de neutrones en O2 (arXiv:1811.12907, resumen); GW150914 tuvo una relacion
senal-ruido de 24 (arXiv:1602.03837, resumen). Las masas, la tasa de fusiones (1e-6 por Mpc^3 por anio), el alcance de
referencia y el umbral son ILUSTRATIVOS (sinteticos).
Modelo: frecuencia gravitacional en la ultima orbita circular estable: f_ISCO = c^3/(6^(3/2) pi G M), comprobada con la
tercera ley de Kepler a r = 6 G M/c^2; relacion senal-ruido proporcional a 1/d (alcance d_h = d_ref rho_ref/rho_umbral);
con una orientacion aleatoria la senal se reduce por g = (1 + cos^2 i)/2 y el volumen efectivo por <g^3> = 0.342857...;
numero de eventos N = R V T.
Supuestos: sensibilidad plana, tasa constante, sin evolucion cosmologica. Validez: Universo local.
Tolerancia: 1e-12 entre f_ISCO por dos vias; 3 % entre el MC y 1/8 (cociente de volumenes) y entre el MC y <g^3>.
"""
from __future__ import annotations
import math
import platform
import random
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G


def f_isco(m_kg):
    return C ** 3 / (6 ** 1.5 * math.pi * G * m_kg)


def f_isco_kepler(m_kg):
    r = 6 * G * m_kg / C ** 2
    f_orb = math.sqrt(G * m_kg / r ** 3) / (2 * math.pi)
    return 2 * f_orb


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'M total [Msol]':>14} {'f_ISCO [Hz]':>12} {'(Kepler) [Hz]':>14}")
    for mt in (2.74, 10.0, 65.0, 200.0):
        a, b = f_isco(mt * M_SOL), f_isco_kepler(mt * M_SOL)
        assert abs(a / b - 1) < 1e-12, "f_ISCO por dos vias"
        print(f"{mt:14.2f} {a:12.2f} {b:14.2f}")
    # alcance y eventos
    d_ref, rho_ref, rho_umbral = 100.0, 24.0, 8.0         # Mpc (ilustrativo), SNR de GW150914 (S), umbral ilustrativo
    d_h = d_ref * rho_ref / rho_umbral
    print(f"alcance (ilustrativo): d_h = d_ref rho_ref/rho_umbral = {d_ref} x {rho_ref}/{rho_umbral} = {d_h:.1f} Mpc")
    tasa, anio = 1e-6, 1.0
    for dh in (50.0, 100.0, 200.0, 400.0):
        v = 4 / 3 * math.pi * dh ** 3
        print(f"alcance {dh:6.1f} Mpc: volumen = {v:.4e} Mpc3 ; eventos por anio con R = 1e-6 Mpc-3 anio-1: {tasa * v * anio:10.2f}")
    # Monte Carlo: fraccion de fuentes uniformes en una esfera de radio 2R que caen dentro de R
    rng = random.Random(20261109)
    n = 200000
    dentro = sum(1 for _ in range(n) if (rng.random()) ** (1 / 3) * 2.0 <= 1.0)
    frac = dentro / n
    print(f"MC: fraccion dentro de R en una esfera de 2R = {frac:.4f} (esperado 1/8 = 0.1250)")
    assert abs(frac / 0.125 - 1) < 0.03
    # orientacion
    suma = 0
    nn = 200000
    for _ in range(nn):
        x = rng.random()
        g = (1 + x * x) / 2
        suma += g ** 3
    g3 = suma / nn
    ana = (1 / 8) * (1 + 3 / 3 + 3 / 5 + 1 / 7)
    print(f"MC: <g^3> = {g3:.4f} ; analitico = {ana:.6f}")
    assert abs(g3 / ana - 1) < 0.03
    print(f"eventos por anio a 100 Mpc con orientacion aleatoria: {tasa * 4 / 3 * math.pi * 100 ** 3 * ana:.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
