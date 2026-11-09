#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C18: calentamiento radiactivo, difusion y luminosidad pico de una kilonova.

Datos: c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Contexto: una kilonova es un transitorio termico casi isotropo
alimentado por la desintegracion radiactiva de nucleos pesados formados por captura rapida de neutrones (arXiv:1910.01617, resumen,
consultado 2026-11-09). La masa eyectada (0.03 Msol), la velocidad (0.2 c), la opacidad (10 cm^2/g), el calentamiento especifico a 1 d
(1e10 erg/g/s), el exponente (-1.3) y la fraccion termalizada (0.5) son ILUSTRATIVOS (sinteticos); el exponente no proviene de ninguna
fuente consultada.
Modelo (tipo Arnett): calentamiento Q(t) = f M eps0 (t/1 d)^-1.3; tiempo de difusion t_d = sqrt(kappa M/(4 pi c v)); luminosidad
L(t) = (2/t_d^2) exp(-(t/t_d)^2) Int_0^t Q(t') t' exp((t'/t_d)^2) dt'. Con la sustitucion u = t'^0.7 el integrando es suave.
Comprobacion independiente: regla de Arnett: en el maximo de L, L = Q.
Supuestos: opacidad gris constante, esfera homogenea en expansion homologa. Validez: ilustrativa.
Tolerancia: 1e-4 relativa en L_pico/Q(t_pico) = 1; 1e-6 entre la integral con sustitucion y por Simpson fino.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
GM_SOL, G = 1.3271244e20, 6.67430e-11
M_SOL = GM_SOL / G
DIA = 86400.0
M, V, KAPPA = 0.03 * M_SOL, 0.2 * C, 1.0           # kappa en m2/kg (10 cm2/g)
EPS0, FTERM, EXPO = 1e6, 0.5, -1.3                  # W/kg a 1 d (1e10 erg/g/s)
T_D = math.sqrt(KAPPA * M / (4 * math.pi * C * V))


def q(t):
    return FTERM * M * EPS0 * (t / DIA) ** EXPO


def integral(t, n=4000):
    """Int_0^t Q t' exp((t'/td)^2) dt' con u = t'^0.7: t'^-0.3 dt' = du/0.7 (t' = u^(1/0.7))."""
    u1 = t ** 0.7
    h = u1 / n
    f = lambda u: math.exp(((u ** (1 / 0.7)) / T_D) ** 2)
    s = f(0.0) + f(u1)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    coef = FTERM * M * EPS0 * DIA ** (-EXPO)         # Q(t') t' = coef t'^(1 + EXPO) = coef t'^-0.3
    return coef * s * h / 3 / 0.7


def integral_simpson(t, n=400000):
    a = 1e-3 * DIA
    h = (t - a) / n
    f = lambda tp: q(tp) * tp * math.exp((tp / T_D) ** 2)
    s = f(a) + f(t)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    # parte [0, a] analitica sin el factor exponencial (aprox. 1): Int Q t' dt' = coef a^0.7/0.7
    coef = FTERM * M * EPS0 * DIA ** (-EXPO)
    return s * h / 3 + coef * a ** 0.7 / 0.7


def lum(t):
    return 2 / T_D ** 2 * math.exp(-(t / T_D) ** 2) * integral(t)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"M = {M / M_SOL:.2f} Msol ; v = 0.2 c ; kappa = 10 cm2/g ; t_d = {T_D:.4e} s = {T_D / DIA:.2f} d")
    t_test = 3 * DIA
    i1, i2 = integral(t_test), integral_simpson(t_test)
    assert abs(i1 / i2 - 1) < 1e-6, "integral con sustitucion frente a Simpson fino"
    print(f"integral a 3 d: con sustitucion = {i1:.6e} ; Simpson fino = {i2:.6e} (cociente {i1 / i2:.8f})")
    g = (math.sqrt(5) - 1) / 2
    a, b = 0.2 * DIA, 20 * DIA
    c_, d_ = b - g * (b - a), a + g * (b - a)
    for _ in range(100):
        if lum(c_) > lum(d_):
            b = d_
        else:
            a = c_
        c_, d_ = b - g * (b - a), a + g * (b - a)
    tp = 0.5 * (a + b)
    lp, qp = lum(tp), q(tp)
    assert abs(lp / qp - 1) < 1e-4, "regla de Arnett"
    print(f"maximo: t_pico = {tp / DIA:.3f} d ; L_pico = {lp:.4e} W = {lp * 1e7:.3e} erg/s ; Q(t_pico) = {qp:.4e} W ; cociente = {lp / qp:.6f}")
    print(f"{'t [d]':>6} {'Q [W]':>12} {'L [W]':>12} {'L/Q':>7}")
    for td in (0.5, 1, 2, 5, 10, 20, 50):
        t = td * DIA
        print(f"{td:6.1f} {q(t):12.4e} {lum(t):12.4e} {lum(t) / q(t):7.3f}")
    # limite de tiempos largos: L -> Q
    t_l = 12 * T_D
    print(f"tiempos largos (t = 12 t_d): L/Q = {lum(t_l) / q(t_l):.4f}")
    assert abs(lum(t_l) / q(t_l) - 1) < 0.02
    # escalado del tiempo del pico con la masa (t_d ~ sqrt(M))
    print(f"t_d con 4x masa / t_d = {math.sqrt(4):.3f} (t_d es proporcional a la raiz de la masa)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
