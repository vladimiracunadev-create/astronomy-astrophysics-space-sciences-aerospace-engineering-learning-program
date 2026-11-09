#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C21: deriva en frecuencia de un estallido de radio tipo III y recuperacion de la velocidad del haz.

Datos: e, m_e, epsilon_0, c (NIST CODATA 2022) y R_sol (IAU 2015 B3), consultados 2026-11-09. El modelo de densidad n(r) = 1e15 (R_sol/r)^2.5 m^-3, la velocidad del haz (0.2 c),
la altura inicial (1.2 R_sol), el ruido (sigma = 0.15) y la malla del espectro dinamico son ILUSTRATIVOS (sinteticos); ningun registro real se reproduce.
Modelo: el haz de electrones viaja a v constante, r(t) = r_0 + v t, y emite a la frecuencia de plasma local f(t) = f_p(n(r(t))) (con armonico 2 f_p opcional); deriva analitica
df/dt = -(beta/2) f v/r para n ~ r^-beta; espectro dinamico sintetico (cresta gaussiana en ln f mas ruido, semilla fija); recuperacion de la cresta por maximo en cada columna temporal y
ajuste de v por busqueda en rejilla refinada.
Supuestos: velocidad constante, emision en la frecuencia de plasma, medio con simetria esferica. Validez: ilustrativa.
Tolerancia: deriva numerica frente a analitica dentro del 0.5 % en f = 100 MHz; velocidad recuperada dentro del 2 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

E, ME, EPS0, C = 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12, 299792458.0
R_SOL = 6.957e8
N0, BETA = 1e15, 2.5
V = 0.2 * C
R0 = 1.2 * R_SOL


def fp(n):
    return math.sqrt(n * E ** 2 / (EPS0 * ME)) / (2 * math.pi)


def f_de_r(r, armonico=1):
    return armonico * fp(N0 * (R_SOL / r) ** BETA)


def f_de_t(t, v=V, armonico=1):
    return f_de_r(R0 + v * t, armonico)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"haz con v = {V / C:.2f} c = {V / 1e6:.2f} Mm/s desde r_0 = 1.2 R_sol ; n(r) = 1e15 (R_sol/r)^{BETA} m-3 (ilustrativo)")
    print(f"{'t [s]':>6} {'r [R_sol]':>10} {'f_p [MHz]':>10} {'2 f_p [MHz]':>12} {'df/dt numerica [MHz/s]':>23} {'analitica':>11}")
    for t in (0.0, 5.0, 10.0, 20.0, 40.0):
        r = R0 + V * t
        h = 0.01
        num = (f_de_t(t + h) - f_de_t(t - h if t > 0 else t)) / (2 * h if t > 0 else h)
        ana = -(BETA / 2) * f_de_t(t) * V / r
        print(f"{t:6.1f} {r / R_SOL:10.3f} {f_de_t(t) / 1e6:10.2f} {f_de_t(t, V, 2) / 1e6:12.2f} {num / 1e6:23.3f} {ana / 1e6:11.3f}")
        if t > 0:
            assert abs(num / ana - 1) < 5e-3, f"deriva t={t}"
    # tiempo en que cruza 100 MHz
    lo, hi = 0.0, 200.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if f_de_t(mid) > 1e8:
            lo = mid
        else:
            hi = mid
    t100 = 0.5 * (lo + hi)
    print(f"la frecuencia fundamental cruza 100 MHz en t = {t100:.3f} s, a r = {(R0 + V * t100) / R_SOL:.3f} R_sol")
    # espectro dinamico sintetico
    rng = random.Random(20261109)
    ts = [0.5 * i for i in range(121)]
    lf = [math.log(20e6) + i * math.log(300e6 / 20e6) / 199 for i in range(200)]
    pico = []
    for t in ts:
        mu = math.log(f_de_t(t))
        col = [math.exp(-0.5 * ((x - mu) / 0.05) ** 2) + rng.gauss(0, 0.15) for x in lf]
        pico.append(lf[max(range(200), key=lambda k: col[k])])
    validos = [(t, p) for t, p in zip(ts, pico) if 20e6 < math.exp(p) < 300e6]

    def sse(v):
        return sum((p - math.log(f_de_t(t, v))) ** 2 for t, p in validos)
    mejor = min((sse(0.05 * C + k * 0.0005 * C), 0.05 * C + k * 0.0005 * C) for k in range(0, 600))
    v_fino = mejor[1]
    for escala in (0.0005 * C, 0.00005 * C):
        mejor = min((sse(v_fino + k * escala / 10), v_fino + k * escala / 10) for k in range(-10, 11))
        v_fino = mejor[1]
    print(f"cresta recuperada en {len(validos)} columnas ; velocidad recuperada = {v_fino / C:.4f} c (verdadera {V / C:.4f} c) ; error relativo = {abs(v_fino / V - 1):.2%}")
    assert abs(v_fino / V - 1) < 0.02, "velocidad recuperada"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
