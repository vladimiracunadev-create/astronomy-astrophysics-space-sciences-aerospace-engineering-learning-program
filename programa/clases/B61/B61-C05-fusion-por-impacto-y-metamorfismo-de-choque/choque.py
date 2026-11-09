#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C05: presion de choque por acoplamiento de impedancias y volumen de fusion.

Datos: ILUSTRATIVOS/SINTETICOS. Hugoniot lineal Us = C + s up con rho0 = 2860 kg/m3, C = 2600 m/s, s = 1.6
  (tipo roca basaltica; valores de ejemplo, NO consultados). Umbrales de metamorfismo (orden de magnitud, de
  resumenes de busqueda sobre Stoffler y Langenhorst, consultados 2026-11-09, originales no leidos):
  PDF en cuarzo > ~10 GPa, vidrio diaplectico/maskelynita ~30-40 GPa, fusion de roca > ~60 GPa.
  Atenuacion P ~ (r/a)^-n con n = 2 (ILUSTRATIVO; el exponente real depende de la presion y el material).
Modelo (SI): impacto plano de proyectil y blanco del mismo material a velocidad U: up = U/2 en cada lado,
  P = rho0 (C + s up) up. Dos vias: formula cerrada y bisecion sobre la condicion de continuidad de presion y
  velocidad de particula entre materiales DISTINTOS (proyectil con rho0, C, s propios) para el caso general.
  Radio de fusion r_m = a (P0/60 GPa)^(1/n); razon de volumen fundido/proyectil = (r_m/a)^3 (esfera, sobreestima
  porque ignora la energia necesaria y el calor latente).
Tolerancias: cierre de presion entre las dos vias 1e-9 relativo; continuidad de presion 1e-9.
"""
from __future__ import annotations
import math, platform

RHO, C, S = 2860.0, 2600.0, 1.6


def presion(rho, c, s, up):
    return rho * (c + s * up) * up


def mismo_material(U):
    return presion(RHO, C, S, U / 2)


def general(U, rho_p, c_p, s_p):
    """up en el blanco por biseccion: P_blanco(up_t) = P_proy(U - up_t)."""
    lo, hi = 0.0, U
    for _ in range(300):
        mid = (lo + hi) / 2
        f = presion(RHO, C, S, mid) - presion(rho_p, c_p, s_p, U - mid)
        if f > 0:
            hi = mid
        else:
            lo = mid
    up = (lo + hi) / 2
    return presion(RHO, C, S, up), up


def clasificar(P):
    g = P / 1e9
    if g > 60:
        return "fusion de roca"
    if g >= 30:
        return "vidrio diaplectico / maskelynita"
    if g >= 10:
        return "PDF en cuarzo / deformacion de choque"
    return "por debajo de ~10 GPa"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Material de ejemplo (ILUSTRATIVO): rho0=2860 kg/m3, C=2600 m/s, s=1.6")
    print(f"{'U [km/s]':>9} {'P cerrada [GPa]':>16} {'P biseccion [GPa]':>18} {'dif rel':>10}  clase")
    for U in (3000.0, 5000.0, 8000.0, 12000.0, 17000.0, 20000.0):
        p1 = mismo_material(U)
        p2, up = general(U, RHO, C, S)
        print(f"{U/1000:9.1f} {p1/1e9:16.3f} {p2/1e9:18.3f} {abs(p2/p1-1):10.2e}  {clasificar(p1)}")
        assert abs(p2 / p1 - 1) < 1e-9
    # proyectil de hierro-tipo (ILUSTRATIVO) contra roca
    pP, upP = general(17000.0, 7850.0, 3570.0, 1.92)
    print(f"Proyectil denso (rho 7850, C 3570, s 1.92 ILUSTRATIVOS) a 17 km/s: P={pP/1e9:.1f} GPa, up_blanco={upP:.0f} m/s")
    # continuidad
    p_t = presion(RHO, C, S, upP)
    p_p = presion(7850.0, 3570.0, 1.92, 17000.0 - upP)
    print(f"Continuidad de presion: blanco {p_t/1e9:.6f} GPa ; proyectil {p_p/1e9:.6f} GPa")
    assert abs(p_t / p_p - 1) < 1e-9
    # volumen fundido
    P0 = mismo_material(17000.0) / 1e9
    for n in (1.5, 2.0, 3.0):
        rm = (P0 / 60.0) ** (1 / n)
        print(f"n={n}: radio de fusion = {rm:.3f} a ; volumen fundido/proyectil = {rm**3:.2f} (cota superior ilustrativa)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
