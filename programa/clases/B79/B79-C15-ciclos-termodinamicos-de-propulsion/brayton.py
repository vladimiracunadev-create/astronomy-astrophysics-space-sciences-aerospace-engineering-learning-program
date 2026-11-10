#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C15: ciclo de Brayton ideal y con perdidas (turbina de gas).

Consultado (2026-11-10): NASA Glenn, ciclo de Brayton de un motor de turbina: estacion 0 (corriente libre), 2 (entrada al compresor),
3 (salida del compresor), 4 (salida del quemador, a presion constante), 5 (salida de turbina), 8 (salida de tobera). La pagina NO da expresion de eficiencia.
ESTANDAR (no consultado): eta_Brayton ideal = 1 - r^(-(g-1)/g); trabajo neto ideal; relacion de presiones de trabajo maximo
r_opt = (T3/T1)^(g/(2(g-1))); rendimientos isentropicos de compresor y turbina.
ILUSTRATIVOS (sinteticos, no medidos): T1 = 288 K, T_max (salida del quemador) = 1400 K; ciclo ideal con aire frio gamma = 1.4, cp = 1004.675 J/(kg K);
ciclo con perdidas: lado frio cp = 1004.675, gamma = 1.4; lado caliente cp = 1148 J/(kg K), gamma = 1.333 (valores de texto de uso comun, no consultados);
eta_compresor = 0.85, eta_turbina = 0.88, caida de presion del quemador 4 %. Aqui estacion 1 = entrada compresor, 2 = salida compresor, 3 = salida quemador, 4 = salida turbina.
Via 2: eficiencia calculada estado a estado (q_entra, q_sale, w = q_entra - q_sale) frente a la formula cerrada y balance de trabajo compresor-turbina.
Tolerancias: ideal estado a estado frente a cerrada < 1e-12; r_opt numerico frente a analitico < 1e-3 relativa.
"""
import math, platform

T1, T3 = 288.0, 1400.0
CP_C, G_C = 1004.675, 1.4
CP_H, G_H = 1148.0, 1.333
ETA_C, ETA_T, DP_Q = 0.85, 0.88, 0.04


def ideal(r):
    k = (G_C - 1) / G_C
    t2 = T1 * r ** k
    t4 = T3 / r ** k
    q_in = CP_C * (T3 - t2)
    q_out = CP_C * (t4 - T1)
    w = q_in - q_out
    return w, w / q_in, 1 - r ** -k, (CP_C * (T3 - t4) - CP_C * (t2 - T1))


def real(r):
    kc = (G_C - 1) / G_C
    kh = (G_H - 1) / G_H
    t2 = T1 + T1 * (r ** kc - 1) / ETA_C
    w_c = CP_C * (t2 - T1)
    r_t = r * (1 - DP_Q)  # relacion de expansion de la turbina hasta la presion ambiente
    t4s = T3 / r_t ** kh
    t4 = T3 - ETA_T * (T3 - t4s)
    w_t = CP_H * (T3 - t4)
    q_in = CP_H * T3 - CP_C * t2  # entalpia del gas caliente menos la del aire que sale del compresor (se ignora la masa del combustible)
    w = w_t - w_c
    return w, w / q_in


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Ciclo ILUSTRATIVO: T1 = {T1} K, T maxima = {T3} K, aire frio gamma = {G_C}")
    print("   r    T2 [K]  T4 [K]   w ideal [kJ/kg]  eta ideal   eta cerrada   w real [kJ/kg]  eta real")
    peor = 0.0
    for r in (5.0, 10.0, 15.0, 20.0, 30.0, 40.0):
        w, eta, eta_c, w2 = ideal(r)
        peor = max(peor, abs(eta - eta_c), abs(w - w2) / w)
        k = (G_C - 1) / G_C
        wr, er = real(r)
        print(f" {r:4.0f}  {T1 * r ** k:7.1f} {T3 / r ** k:7.1f}      {w / 1e3:8.2f}       {eta:.4f}      {eta_c:.4f}       {wr / 1e3:8.2f}      {er:.4f}")
    print(f"Diferencia maxima estado a estado frente a cerrada = {peor:.2e}")
    # r de trabajo maximo
    mejor, r_mejor = -1.0, 0.0
    r = 2.0
    while r <= 80.0:
        w = ideal(r)[0]
        if w > mejor:
            mejor, r_mejor = w, r
        r += 0.01
    r_ana = (T3 / T1) ** (G_C / (2 * (G_C - 1)))
    print(f"Relacion de presiones de trabajo maximo (ideal): numerica = {r_mejor:.2f} ; analitica = {r_ana:.3f} ; w_max = {mejor / 1e3:.2f} kJ/kg ; eta en ese punto = {ideal(r_ana)[2]:.4f}")
    # r de trabajo maximo y de eficiencia maxima del ciclo real
    mw, rw = -1.0, 0.0
    me, re_ = -1.0, 0.0
    r = 2.0
    while r <= 60.0:
        wr, er = real(r)
        if wr > mw:
            mw, rw = wr, r
        if er > me:
            me, re_ = er, r
        r += 0.01
    print(f"Ciclo real: trabajo maximo {mw / 1e3:.2f} kJ/kg en r = {rw:.2f} ; eficiencia maxima {me:.4f} en r = {re_:.2f}")
    print(f"Con T3 = 1600 K el r de trabajo maximo ideal sube a {(1600.0 / T1) ** (G_C / (2 * (G_C - 1))):.2f}")
    assert peor < 1e-12
    assert abs(r_mejor - r_ana) / r_ana < 1e-3
    print("Pruebas superadas.")


main()
