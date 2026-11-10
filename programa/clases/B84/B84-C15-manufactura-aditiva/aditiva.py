#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C15: manufactura aditiva por fusion en lecho de polvo: densidad de energia, ventana de proceso, rugosidad escalonada y tiempo.

DATOS ILUSTRATIVOS (no consultados; valores tipicos de AlSi10Mg inventados como orden de magnitud): potencia P [W], velocidad de barrido v [mm/s],
separacion entre pasadas h = 0,19 mm, espesor de capa t = 0,030 mm. Densidad de energia volumetrica E_v = P/(v h t) [J/mm3].
Ventana ILUSTRATIVA: E_v < 35 J/mm3 -> falta de fusion; 35 <= E_v <= 70 -> ventana; E_v > 70 -> exceso de energia (poros de ojo de cerradura). Los umbrales son
inventados para el ejercicio y dependen del material y del equipo.
Rugosidad escalonada: en una superficie inclinada theta grados respecto del plano de construccion (0 = horizontal), la altura de escalon es t y el perfil es un
diente de sierra de amplitud t cos(theta); Ra = t cos(theta)/4 (analitica) y se calcula tambien por integracion numerica del perfil.
Tiempo de construccion: capas = H/t; tiempo por capa = area/(h v) + 10 s de recubrimiento; pieza ILUSTRATIVA de H = 40 mm y area de capa 20 cm2 con v = 1300 mm/s.
Unidades: W, mm, s, J. Tolerancia: Ra numerica frente a analitica < 1e-3 relativa.
"""
from __future__ import annotations
import math, platform

H_SEP, T_CAPA = 0.19, 0.030


def ev(P, v):
    return P / (v * H_SEP * T_CAPA)


def clase(e):
    return "falta de fusion" if e < 35 else ("ventana" if e <= 70 else "exceso")


def ra_numerica(theta_deg, n=200000):
    th = math.radians(theta_deg)
    amp = T_CAPA * math.cos(th)
    # diente de sierra de periodo 1 con amplitud amp: y(x) = amp (x - 0,5), x en [0,1)
    s = 0.0
    for i in range(n):
        x = (i + 0.5) / n
        s += abs(amp * (x - 0.5))
    return s / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Densidad de energia E_v = P/(v h t) [J/mm3] con h = 0,19 mm y t = 0,030 mm (valores ILUSTRATIVOS)")
    vs = (600, 900, 1300, 1800)
    print("   P [W] |" + "".join(f" v={v:4d} mm/s |" for v in vs))
    for P in (150, 250, 370, 400):
        print(f"  {P:5d}  |" + "".join(f" {ev(P, v):6.1f} {clase(ev(P, v))[:6]:6s}|" for v in vs))
    print(f"Punto de referencia P = 370 W, v = 1300 mm/s: E_v = {ev(370, 1300):.2f} J/mm3 -> {clase(ev(370, 1300))}")
    # Cuantos puntos de una malla fina caen en la ventana
    n_v = 0
    n_t = 0
    for P in range(100, 421, 10):
        for v in range(400, 2001, 25):
            n_t += 1
            if clase(ev(P, v)) == "ventana":
                n_v += 1
    print(f"Malla P 100-420 W (paso 10) x v 400-2000 mm/s (paso 25): {n_v} de {n_t} puntos en la ventana ({n_v / n_t * 100:.1f} %)")
    print("Rugosidad escalonada Ra [micrometros] segun la inclinacion (t = 30 um):")
    dmax = 0.0
    for th in (0, 30, 45, 60, 80, 89):
        ra_a = T_CAPA * math.cos(math.radians(th)) / 4 * 1e3
        ra_n = ra_numerica(th) * 1e3
        dmax = max(dmax, abs(ra_n - ra_a) / ra_a)
        print(f"  theta = {th:2d} grados  Ra analitica = {ra_a:6.3f}  numerica = {ra_n:6.3f}")
    capas = 40.0 / T_CAPA
    t_capa = 2000.0 / (H_SEP * 1300) + 10.0
    print(f"Tiempo de construccion ILUSTRATIVO: {capas:.0f} capas x ({2000.0 / (H_SEP * 1300):.2f} s de barrido + 10 s de recubrimiento) = {capas * t_capa / 3600:.2f} h")
    print(f"El recubrimiento aporta {capas * 10 / 3600:.2f} h de las {capas * t_capa / 3600:.2f} h: espesor de capa 60 um -> {(40 / 0.060) * (2000.0 / (H_SEP * 1300) + 10.0) / 3600:.2f} h (sin cambiar E_v)")
    assert dmax < 1e-3
    assert clase(ev(370, 1300)) == "ventana"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
