#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C05: amplitud, energia y efecto de una onda gravitacional de una binaria compacta.

Datos: G, c (NIST CODATA 2022), GM_sol (IAU 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09. Contexto: GW150914 tuvo un
pico de deformacion de 1.0e-21 y barrio de 35 a 250 Hz (arXiv:1602.03837, resumen); GW170817 estuvo a 40 Mpc con masa total
2.74 Msol (arXiv:1710.05833, resumen). Las masas iguales de 1.37 Msol, las frecuencias y la longitud de 4 km son
ILUSTRATIVAS (sinteticas), salvo donde se cita.
Modelo (orden de cuadrupolo, orbita circular, vista de frente): amplitud h = 4 (G Mc)^(5/3) (pi f)^(2/3)/(c^4 d);
flujo de energia F = (c^3/(16 pi G)) <hdot_+^2 + hdot_x^2> = (pi c^3/(4 G)) f^2 h^2 (promedio sobre un ciclo);
desplazamiento relativo de una barra de longitud L: dL = h L/2.
Comprobacion independiente: la potencia total radiada por la formula de Peters (P_GW) es 2/5 de 4 pi d^2 F, porque F es el flujo de frente
y el flujo promediado sobre todos los angulos vale 2/5 del de frente.
Supuestos: orbita circular, vista de frente, sin efectos post-newtonianos. Validez: lejos de la fusion.
Tolerancia: 1e-9 entre P_GW (Peters) y (2/5) 4 pi d^2 F.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
AU = 1.49597870700e11
MPC = 1e6 * 648000 / math.pi * AU


def masa_chirrido(m1, m2):
    return (m1 * m2) ** 0.6 / (m1 + m2) ** 0.2


def amplitud(mc, f, d):
    return 4 * (G * mc) ** (5 / 3) * (math.pi * f) ** (2 / 3) / (C ** 4 * d)


def flujo(f, h):
    return math.pi * C ** 3 / (4 * G) * f ** 2 * h ** 2


def p_peters(m1, m2, f):
    m = m1 + m2
    a = (G * m / (math.pi * f) ** 2) ** (1 / 3)         # f_GW = 2 f_orb
    return 32 / 5 * G ** 4 * m1 ** 2 * m2 ** 2 * m / (C ** 5 * a ** 5)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 1.37 * M_SOL
    mc = masa_chirrido(m, m)
    d = 40 * MPC
    print(f"GW170817 ilustrativa: masas iguales de 1.37 Msol, M_c = {mc / M_SOL:.4f} Msol, d = 40 Mpc = {d:.4e} m")
    print(f"{'f_GW [Hz]':>10} {'h':>12} {'dL en 4 km [m]':>16} {'F [W/m2]':>12} {'P_GW [W]':>12} {'P/(4 pi d2 F)':>14}")
    for f in (30.0, 100.0, 400.0):
        h = amplitud(mc, f, d)
        fl = flujo(f, h)
        p = p_peters(m, m, f)
        r = p / (4 * math.pi * d ** 2 * fl)
        assert abs(r - 0.4) < 1e-9, f"potencia (Peters) frente a flujo, f={f}"
        print(f"{f:10.1f} {h:12.4e} {h * 4000 / 2:16.4e} {fl:12.4e} {p:12.4e} {r:14.9f}")
    # escala con la distancia y con la masa de chirrido
    h40, h80 = amplitud(mc, 100.0, 40 * MPC), amplitud(mc, 100.0, 80 * MPC)
    print(f"h(80 Mpc)/h(40 Mpc) = {h80 / h40:.4f} (esperado 0.5)")
    h2 = amplitud(2 * mc, 100.0, 40 * MPC)
    print(f"h(2 M_c)/h(M_c) = {h2 / h40:.4f} (esperado 2^(5/3) = {2 ** (5 / 3):.4f})")
    assert abs(h80 / h40 - 0.5) < 1e-12 and abs(h2 / h40 - 2 ** (5 / 3)) < 1e-12
    # distancia a la que h = 1e-21 (valor de pico citado de GW150914) para M_c de GW170817 a 100 Hz
    d_eq = 4 * (G * mc) ** (5 / 3) * (math.pi * 100.0) ** (2 / 3) / (C ** 4 * 1e-21)
    print(f"distancia para h = 1e-21 con M_c = {mc / M_SOL:.4f} Msol a 100 Hz: {d_eq / MPC:.3f} Mpc")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
