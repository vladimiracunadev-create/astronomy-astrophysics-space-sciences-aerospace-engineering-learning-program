#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C02: escalas sinodicas, unidades adimensionales y resonancia 9:2 de una NRHO.

Datos CONSULTADOS (2026-11-10): periodo sideral lunar 27.3217 d y sinodico 29.53 d (NASA/NSSDC, ficha de la Luna);
a = 384400 km; GM (JPL, DE440). Resonancia 9:2, periodo medio 6.56 d, apolune medio 71100 km y perilune medio 3366 km:
Davis, Khoury, Howell y Sweeney, NASA NTRS 20200000733 (consultado con PyMuPDF, 2026-11-10; fecha de publicacion no consultada).
NO CONSULTADO en esta sesion: el periodo sideral terrestre 365.256 d (valor estandar usado para la comprobacion).
Modelo: P_sin = 1/(1/P_sid - 1/P_Tierra). Unidad de longitud a; de tiempo 1/n; de velocidad a*n.
Tolerancias: P_sin calculado frente a 29.53 d < 0.05 d; ida y vuelta de unidades < 1e-12 relativa.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

P_ANIO = 365.256  # d, valor estandar (NO CONSULTADO)


def a_adim(km_, dias_):
    return km_ / A_L, dias_ * DIA / T_U


def de_adim(l, t):
    return l * A_L, t * T_U / DIA


def calcular():
    p_sin = 1.0 / (1.0 / P_SID - 1.0 / P_ANIO)
    t_nrho = 2 * P_SIN / 9
    l, t = a_adim(71100.0, 6.56)
    l2, t2 = de_adim(l, t)
    return dict(p_sin=p_sin, n_dia=2 * math.pi / P_SID, w_sin=2 * math.pi / P_SIN, t_nrho=t_nrho,
                err_sin=abs(p_sin - P_SIN), apo=l, t=t, rt=max(abs(l2 - 71100.0) / 71100.0, abs(t2 - 6.56) / 6.56),
                t_u=T_U / DIA, v_u=A_L * N_L, rev=2 * P_SIN / 6.56)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Periodo sinodico calculado = {r['p_sin']:.4f} d ; consultado = {P_SIN} d ; diferencia = {r['err_sin']:.4f} d")
    print(f"Movimiento medio sideral = {r['n_dia']:.5f} rad/d ; sinodico = {r['w_sin']:.5f} rad/d")
    print(f"Unidades: longitud = {A_L:.0f} km ; tiempo = {r['t_u']:.4f} d ; velocidad = {r['v_u']:.5f} km/s")
    print(f"Resonancia 9:2: 2*P_sin/9 = {r['t_nrho']:.4f} d (periodo medio publicado 6.56 d)")
    print(f"Revoluciones de 6.56 d en dos meses sinodicos = {r['rev']:.3f}")
    print(f"NRHO publicada en unidades adimensionales: apolune = {r['apo']:.5f} ; periodo = {r['t']:.5f}")
    print(f"Error de ida y vuelta de unidades = {r['rt']:.2e}")
    assert r['err_sin'] < 0.05
    assert abs(r['t_nrho'] - 6.56) < 0.02
    assert r['rt'] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
