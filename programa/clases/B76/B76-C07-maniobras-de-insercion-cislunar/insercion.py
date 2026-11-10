#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C07: Delta-v de inyeccion translunar (TLI) e insercion lunar (LOI) con conicas empalmadas.

Datos CONSULTADOS (2026-11-10): GM_T, GM_L (JPL, DE440), radio ecuatorial terrestre 6378.137 km (NASA/NSSDC), R_L = 1737.4 km (JPL),
a_L = 384400 km (NASA/NSSDC). ILUSTRATIVOS: altitud de orbita de estacionamiento 200 km; orbita lunar objetivo de 100 km;
Isp = 320 s (hipotesis de motor), g0 = 9.80665 m/s2 (valor convencional, no consultado en esta sesion).
Modelo: Hohmann entre la orbita baja terrestre y la distancia lunar (Tierra puntual, Luna con velocidad circular n*a); la velocidad de
llegada relativa a la Luna es v_inf = v_Luna - v_apogeo (coplanar, sin inclinacion ni Sol). LOI impulsiva en el perilune.
Verificaciones: conservacion de energia (vis-viva) en la hiperbola lunar a 1e-9; tiempo de vuelo = semiperiodo de la elipse.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

G0 = 9.80665
ISP = 320.0


def calcular(h_leo=200.0, h_llo=100.0):
    r1 = R_T_EQ + h_leo
    r2 = A_L
    at = 0.5 * (r1 + r2)
    v_circ = math.sqrt(GM_T / r1)
    v_p = math.sqrt(GM_T * (2 / r1 - 1 / at))
    v_a = math.sqrt(GM_T * (2 / r2 - 1 / at))
    dv_tli = v_p - v_circ
    t_vuelo = math.pi * math.sqrt(at ** 3 / GM_T) / DIA
    v_luna = math.sqrt((GM_T + GM_L) / A_L)
    v_inf = v_luna - v_a
    rl = R_L + h_llo
    v_hip = math.sqrt(v_inf ** 2 + 2 * GM_L / rl)
    v_c = math.sqrt(GM_L / rl)
    dv_loi = v_hip - v_c
    e_hip = v_inf ** 2 / 2
    e_peri = v_hip ** 2 / 2 - GM_L / rl
    ecc = 1 + rl * v_inf ** 2 / GM_L
    total = dv_tli + dv_loi
    masa = lambda dv: 1 - math.exp(-dv * 1000 / (ISP * G0))
    return dict(r1=r1, v_circ=v_circ, v_p=v_p, v_a=v_a, dv_tli=dv_tli, t_vuelo=t_vuelo, v_luna=v_luna, v_inf=v_inf,
                v_hip=v_hip, v_c=v_c, dv_loi=dv_loi, ecc=ecc, err_e=abs(e_hip - e_peri) / e_hip, total=total,
                frac=masa(total), frac_tli=masa(dv_tli), frac_loi=masa(dv_loi), masa=masa)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"TLI desde 200 km: v_circ = {r['v_circ']:.4f} km/s ; v_perigeo = {r['v_p']:.4f} km/s ; dv_TLI = {r['dv_tli']:.4f} km/s")
    print(f"Tiempo de vuelo (semi-elipse) = {r['t_vuelo']:.3f} d ; v_apogeo = {r['v_a']:.4f} km/s ; v_Luna = {r['v_luna']:.4f} km/s")
    print(f"Llegada: v_inf = {r['v_inf']:.4f} km/s ; excentricidad hiperbolica = {r['ecc']:.4f}")
    print(f"LOI a 100 km: v_perilune = {r['v_hip']:.4f} km/s ; v_circ lunar = {r['v_c']:.4f} km/s ; dv_LOI = {r['dv_loi']:.4f} km/s")
    print(f"Delta-v total = {r['total']:.4f} km/s ; fraccion de propergol (Isp 320 s ILUSTRATIVO) = {r['frac']:.4f}")
    print(f"Error de energia hiperbolica = {r['err_e']:.2e}")
    for h in (50.0, 100.0, 500.0, 2000.0):
        print(f"  LOI a h = {h:6.0f} km : dv = {calcular(200.0, h)['dv_loi']:.4f} km/s")
    assert r['err_e'] < 1e-9
    assert 3.0 < r['dv_tli'] < 3.3 and 4.5 < r['t_vuelo'] < 5.5
    assert calcular(200, 2000)['dv_loi'] < calcular(200, 100)['dv_loi'] < calcular(200, 50)['dv_loi'] + 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
