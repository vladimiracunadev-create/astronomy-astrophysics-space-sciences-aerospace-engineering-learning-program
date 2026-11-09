#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C10: estructura del tubo optico: flexion de un tubo y cercha tipo Serrurier con flechas iguales.

Datos: ILUSTRATIVOS (tubo de aluminio E = 69 GPa, radio 125 mm, pared 2 mm, longitud 1,0 m, masa 8 kg; masas de extremo 6 kg (cel. del primario) y 1 kg (secundario) a 0,5 m del eje de la caja central).
g = 9,80665 m/s^2 de NIST CODATA 2022, consultada el 2026-11-09. El modulo del aluminio es un valor tipico NO consultado.
Modelo: viga de Euler-Bernoulli; momento de inercia de un tubo delgado I = pi r^3 t; voladizo con carga puntual delta = P L^3/(3 E I) y con carga uniforme delta = w L^4/(8 E I).
Verificacion independiente: doble integracion numerica (regla del trapecio, 4000 pasos) de la curvatura y'' = M/(E I) con empotramiento en x = 0.
Serrurier: para que ambos extremos se flexionen lo mismo, I_b/I_a = (m_b/m_a)(L_b/L_a)^3; entonces el descentrado relativo primario-secundario es nulo.
Supuestos: pequenas deflexiones, material lineal, cada brazo de la cercha equivale a una viga en voladizo. Validez: primera estimacion, no sustituye a un modelo de elementos finitos.
Tolerancia: integracion numerica frente a formula, 1e-3 relativo.
"""
from __future__ import annotations
import math, platform

G = 9.80665; E = 69e9

def integrar(Mf, EI, L, n=4000):
    h = L / n
    th = 0.0; y = 0.0; ths = [0.0]; ys = [0.0]
    kappa = [Mf(i * h) / EI for i in range(n + 1)]
    for i in range(n):
        th += 0.5 * (kappa[i] + kappa[i + 1]) * h
        y += th * h  # aproximacion de primer orden mejorada abajo
        ths.append(th)
    # reintegracion trapezoidal de theta
    y = 0.0
    for i in range(n):
        y += 0.5 * (ths[i] + ths[i + 1]) * h
    return y

def calc():
    r = {}
    rad = 0.125; t = 0.002; L = 1.0; m = 8.0
    I = math.pi * rad ** 3 * t
    r["I_tubo_m4"] = I
    w = m * G / L
    f_u = w * L ** 4 / (8 * E * I)
    n_u = integrar(lambda x: w * (L - x) ** 2 / 2, E * I, L)
    r["flecha_uniforme_um"] = f_u * 1e6; r["flecha_uniforme_num_um"] = n_u * 1e6
    P = 6 * G
    Ia = 5e-7
    f_p = P * 0.5 ** 3 / (3 * E * Ia)
    n_p = integrar(lambda x: P * (0.5 - x), E * Ia, 0.5)
    r["flecha_a_um"] = f_p * 1e6; r["flecha_a_num_um"] = n_p * 1e6
    ma, mb, La, Lb = 6.0, 1.0, 0.5, 0.5
    fb_igual_I = mb * G * Lb ** 3 / (3 * E * Ia)
    r["flecha_b_mismo_I_um"] = fb_igual_I * 1e6
    r["descentrado_mismo_I_um"] = (f_p - fb_igual_I) * 1e6
    Ib = Ia * (mb / ma) * (Lb / La) ** 3
    fb = mb * G * Lb ** 3 / (3 * E * Ib)
    r["Ib_sobre_Ia"] = Ib / Ia; r["flecha_b_serrurier_um"] = fb * 1e6
    r["descentrado_serrurier_um"] = (f_p - fb) * 1e6
    r["rigidez_tubo_N_por_um"] = (3 * E * I / L ** 3) / 1e6
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.6g}")
    assert abs(r["flecha_uniforme_um"] - r["flecha_uniforme_num_um"]) / r["flecha_uniforme_um"] < 1e-3
    assert abs(r["flecha_a_um"] - r["flecha_a_num_um"]) / r["flecha_a_um"] < 1e-3
    assert abs(r["descentrado_serrurier_um"]) < 1e-9
    assert abs(r["Ib_sobre_Ia"] - 1 / 6) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
