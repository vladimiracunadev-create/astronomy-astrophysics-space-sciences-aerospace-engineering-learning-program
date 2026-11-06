#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C02: continuidad, saltos y teorema del valor intermedio.

Datos: cohete de dos etapas SINTÉTICO (no corresponde a ningún vehículo real).
g_n = 9.80665 m/s2 (exacta; CODATA 2022 en NIST).
Modelo: masa m(t) por tramos, empuje T(t) por tramos, aceleración propia
a(t) = T/m (sin gravedad ni arrastre). Clasificación de discontinuidades con
límites laterales (DLMF 1.4(ii)); teorema del valor intermedio por bisección.
Supuestos: separación instantánea; caudal de masa constante en cada etapa.
Validez: solo ilustración matemática. Tolerancia: 1e-9 s en la raíz.
"""
from __future__ import annotations
import math, platform, sys

G_N = 9.80665
# etapa 1: 0 <= t < 100 s ; etapa 2: 100 <= t <= 250 s
M0, MDOT1, T1, TS = 100_000.0, 500.0, 1.5e6, 100.0
M_DRY1 = 8_000.0
MDOT2, T2, TF = 120.0, 4.0e5, 250.0


def masa(t):
    if t < TS:
        return M0 - MDOT1 * t
    return (M0 - MDOT1 * TS - M_DRY1) - MDOT2 * (t - TS)


def empuje(t):
    return T1 if t < TS else T2


def acel(t):
    return empuje(t) / masa(t)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def lim_lateral(f, a, lado, h=1e-9):
    return f(a + lado * h)


def biseccion(f, a, b, tol=1e-12):
    fa = f(a)
    prueba(fa * f(b) < 0, "el intervalo no cambia de signo")
    while b - a > tol:
        c = 0.5 * (a + b)
        if fa * f(c) <= 0:
            b = c
        else:
            a, fa = c, f(c)
    return 0.5 * (a + b)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # 1) límites laterales en la separación
    for nombre, f in (("masa [kg]", masa), ("empuje [N]", empuje), ("aceleración [m/s2]", acel)):
        izq, der = lim_lateral(f, TS, -1), lim_lateral(f, TS, +1)
        print(f"{nombre:20s} izq={izq:14.4f}  der={der:14.4f}  salto={der-izq:14.4f}")
    salto_m = lim_lateral(masa, TS, +1) - lim_lateral(masa, TS, -1)
    prueba(abs(salto_m + M_DRY1) < 1e-3, "salto de masa = -masa seca de la etapa 1")
    # 2) continuidad de la masa DENTRO de cada etapa
    prueba(abs(masa(50 + 1e-9) - masa(50)) < 1e-5, "masa continua en t = 50 s")
    # 3) valor intermedio: ¿cuándo a = 2,5 g_n en la etapa 1?
    objetivo = 2.5 * G_N
    t_num = biseccion(lambda t: acel(t) - objetivo, 0.0, TS - 1e-6)
    t_exacto = (M0 - T1 / objetivo) / MDOT1
    print(f"a = 2.5 g_n = {objetivo:.5f} m/s2 en t = {t_num:.9f} s (exacto {t_exacto:.9f} s)")
    prueba(abs(t_num - t_exacto) < 1e-9, "bisección = solución analítica")
    # 4) discontinuidad removible: sin x / x
    f = lambda x: math.sin(x) / x if x != 0 else 1.0
    print(f"sin x/x: f(1e-6)={f(1e-6):.12f}; f(0) redefinida={f(0.0)}")
    prueba(abs(f(1e-6) - f(0.0)) < 1e-12, "extensión continua de sin x/x")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
