#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C14: probabilidad de colision en el plano del encuentro y maniobra de evasion con HCW.

Datos SINTETICOS (ninguno proviene de un catalogo ni de un conjunction data message real): distancia de fallo nominal 120 m a lo largo del eje x del
plano del encuentro, covarianza combinada diagonal sigma_x = 80 m y sigma_y = 40 m, radio duro combinado HBR = 10 m, orbita circular de 400 km
(GM_T = 398600.435507 km3/s2, JPL DE440, consultado el 2026-11-10; radio ecuatorial 6378.137 km, NASA/NSSDC). Umbral de aceptacion 1e-6
(ILUSTRATIVO del autor; no es un criterio operativo consultado). Semilla 76014, 400000 muestras.
Modelo: encuentro corto (velocidad relativa alta y recta), Pc = integral de la gaussiana 2D sobre el disco de radio HBR.
Tres vias: (1) cuadratura polar 400x400; (2) aproximacion de primer orden: area del disco (pi HBR^2) por la densidad gaussiana en el centro; (3) Monte Carlo. Evasion: impulso a lo largo de la trayectoria
medio periodo antes del encuentro; desplazamiento radial = 4 dv / n (HCW), verificado con hcw().
Tolerancias: cuadratura frente a Monte Carlo < 5 % relativa; aproximacion frente a cuadratura < 2 %.
"""
from __future__ import annotations
import math, os, platform, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

SX, SY, HBR = 80.0, 40.0, 10.0
R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)
P = 2 * math.pi / N


def pdf(x, y, mx, my):
    return math.exp(-0.5 * (((x - mx) / SX) ** 2 + ((y - my) / SY) ** 2)) / (2 * math.pi * SX * SY)


def pc_cuadratura(mx, my=0.0, nr=400, nt=400):
    s = 0.0
    dr = HBR / nr
    for i in range(nr):
        r = (i + 0.5) * dr
        for j in range(nt):
            th = (j + 0.5) * 2 * math.pi / nt
            s += pdf(r * math.cos(th), r * math.sin(th), mx, my) * r * dr * (2 * math.pi / nt)
    return s


def pc_aprox(mx, my=0.0):
    return math.pi * HBR ** 2 * pdf(0.0, 0.0, mx, my)


def pc_mc(mx, n=400000, semilla=76014):
    rng = random.Random(semilla)
    k = 0
    for _ in range(n):
        x = rng.gauss(mx, SX)
        y = rng.gauss(0.0, SY)
        if x * x + y * y <= HBR * HBR:
            k += 1
    return k / n, k


def calcular():
    pc = pc_cuadratura(120.0)
    pa = pc_aprox(120.0)
    pm, k = pc_mc(120.0)
    # evasion: buscar el fallo mx que da Pc <= 1e-6 (aproximacion calibrada con la cuadratura)
    lo, hi = 120.0, 2000.0
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if pc_aprox(m) > 1e-6:
            lo = m
        else:
            hi = m
    mx_obj = hi
    dx = mx_obj - 120.0
    dv = dx * N / 4          # impulso a lo largo de la trayectoria medio periodo antes: x = 4 dv / n
    x_hcw = hcw(N, 0.5 * P, (0, 0, 0, 0, dv, 0))[0]
    pc_nuevo = pc_cuadratura(mx_obj, 200, 200)
    return dict(pc=pc, pa=pa, pm=pm, k=k, mx_obj=mx_obj, dx=dx, dv=dv, x_hcw=x_hcw, pc_nuevo=pc_nuevo,
                tabla=[(m, pc_aprox(m)) for m in (0.0, 60.0, 120.0, 240.0, 400.0)])


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar) ; semilla 76014 ; datos SINTETICOS")
    print(f"Encuentro: fallo nominal 120 m, sigma = ({SX:.0f}, {SY:.0f}) m, HBR = {HBR:.0f} m")
    print(f"Pc cuadratura polar = {r['pc']:.4e} ; aproximacion de primer orden = {r['pa']:.4e} ; Monte Carlo = {r['pm']:.4e} ({r['k']} impactos de 400000)")
    print(" fallo [m]   Pc (aprox.)")
    for m, p in r['tabla']:
        print(f"{m:8.0f}   {p:.3e}")
    print(f"Fallo necesario para Pc <= 1e-6 (ILUSTRATIVO) = {r['mx_obj']:.1f} m ; desplazamiento adicional = {r['dx']:.1f} m")
    print(f"Impulso a lo largo de la trayectoria medio periodo antes: dv = {r['dv'] * 1000:.2f} mm/s ; desplazamiento HCW = {r['x_hcw']:.1f} m")
    print(f"Pc tras la maniobra (cuadratura) = {r['pc_nuevo']:.3e}")
    assert abs(r['pc'] - r['pm']) / r['pc'] < 0.05
    assert abs(r['pa'] - r['pc']) / r['pc'] < 0.02
    assert abs(r['x_hcw'] - r['dx']) < 1e-6
    assert r['pc_nuevo'] < 1.1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
