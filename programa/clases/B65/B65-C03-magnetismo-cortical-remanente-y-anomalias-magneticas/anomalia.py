#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C03: anomalia magnetica de un bloque de corteza magnetizado y ajuste de su momento.

Datos consultados: mu0 = 1.25663706127e-6 N A^-2 (NIST, CODATA 2022, consulta 2026-11-09).
Datos SINTETICOS (inventados para el ejercicio, no medidos en Marte ni en la Luna): esfera de 50 km de radio, magnetizacion uniforme vertical M = 5 A/m,
altura de observacion de 150 km sobre su cima, ruido gaussiano de 2 nT con semilla 20261109.
Modelo: (1) campo de la esfera uniformemente magnetizada = campo de un dipolo m = (4/3) pi a^3 M (solucion cerrada); (2) integracion numerica por celdas cubicas
(suma de dipolos); (3) ajuste lineal por minimos cuadrados del momento a datos con ruido; (4) profundidad de Curie = (Tc - Ts)/gradiente.
Sistema de referencia: x horizontal, z hacia arriba, origen en el centro de la esfera; Bz en nT.
Supuestos: magnetizacion uniforme, sin campo inductor, sin curvatura planetaria. Validez: ilustrativa.
Tolerancia: integracion numerica frente a dipolo < 1e-3 relativo al maximo; error del ajuste < 3 sigma.
"""
from __future__ import annotations
import math, platform, random

MU0 = 1.25663706127e-6
A, M0 = 50.0e3, 5.0                 # m, A/m (sinteticos)
H_OBS = 150.0e3                      # m sobre la cima
ZC = A + H_OBS                       # altura del punto de observacion sobre el centro
SIG_NT = 2.0
SEMILLA = 20261109

def bz_dipolo(m, x, z):
    """Bz [T] de un dipolo vertical m [A m^2] en el origen, en el punto (x, z)."""
    r2 = x * x + z * z
    r = math.sqrt(r2)
    return MU0 / (4 * math.pi) * m * (3 * z * z / r2 - 1) / r**3

def bz_celdas(M, x, z, n=24):
    """Suma de dipolos de celdas cubicas cuyos centros estan dentro de la esfera."""
    d = 2 * A / n
    tot = 0.0
    nin = 0
    for i in range(n):
        xi = -A + (i + 0.5) * d
        for j in range(n):
            yj = -A + (j + 0.5) * d
            for k in range(n):
                zk = -A + (k + 0.5) * d
                if xi * xi + yj * yj + zk * zk <= A * A:
                    nin += 1
                    dx, dy, dz = x - xi, -yj, z - zk
                    r2 = dx * dx + dy * dy + dz * dz
                    r = math.sqrt(r2)
                    tot += MU0 / (4 * math.pi) * (M * d**3) * (3 * dz * dz / r2 - 1) / r**3
    return tot, nin * d**3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 4.0 / 3.0 * math.pi * A**3 * M0
    print(f"Esfera sintetica: a = {A/1e3:.0f} km, M = {M0} A/m, momento m = {m:.4e} A m^2, altura de observacion sobre el centro = {ZC/1e3:.0f} km")
    print(" x [km]   Bz dipolo [nT]   Bz celdas [nT]   dif [nT]")
    maxdif, pico = 0.0, bz_dipolo(m, 0.0, ZC) * 1e9
    for xkm in (0, 100, 200, 400):
        bd = bz_dipolo(m, xkm * 1e3, ZC) * 1e9
        bc, vol = bz_celdas(M0, xkm * 1e3, ZC)
        bc = bc * 1e9 * (4.0 / 3.0 * math.pi * A**3) / vol      # corrige la diferencia de volumen de las celdas
        maxdif = max(maxdif, abs(bd - bc))
        print(f"{xkm:6d} {bd:16.4f} {bc:16.4f} {bd-bc:10.5f}")
    print(f"Maxima diferencia / pico = {maxdif/pico:.2e}")
    # ajuste con ruido
    rng = random.Random(SEMILLA)
    xs = [(-400.0 + 20.0 * i) * 1e3 for i in range(41)]
    g = [bz_dipolo(1.0, x, ZC) * 1e9 for x in xs]            # nT por A m^2
    d = [m * gi + rng.gauss(0.0, SIG_NT) for gi in g]
    sgg = sum(gi * gi for gi in g)
    mhat = sum(gi * di for gi, di in zip(g, d)) / sgg
    sm = SIG_NT / math.sqrt(sgg)
    print(f"Ajuste lineal (41 puntos, ruido {SIG_NT} nT, semilla {SEMILLA}): m_ajustado = {mhat:.4e} A m^2 ; error estandar = {sm:.2e} ; verdadero = {m:.4e}")
    print(f"Diferencia = {(mhat-m)/sm:+.2f} sigma ; Bz pico = {pico:.3f} nT (relacion senal/ruido = {pico/SIG_NT:.1f})")
    # caida con la altura
    r1 = bz_dipolo(m, 0.0, A + 150e3) / bz_dipolo(m, 0.0, A + 400e3)
    print(f"Pico a 150 km / pico a 400 km sobre la cima = {r1:.3f} ; (z2/z1)^3 = {((A+400e3)/(A+150e3))**3:.3f}")
    # profundidad de Curie (valores ILUSTRATIVOS)
    tc, ts, grad = 853.0, 210.0, 15.0   # K, K, K/km
    print(f"Profundidad de Curie ilustrativa: ({tc:.0f} - {ts:.0f}) K / {grad:.0f} K/km = {(tc-ts)/grad:.1f} km")
    assert maxdif / pico < 1e-3 and abs(mhat - m) < 3 * sm
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
