#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C11: aislamiento vibracional de un instrumento, transmisibilidad de un oscilador con excitacion en la base.

Datos: ninguna constante fisica de una fuente. TODO es ILUSTRATIVO (no es el aislador de ningun instrumento): frecuencia natural 10 Hz, amortiguamientos 0,05 y 0,5,
razones de frecuencia 0,5 a 10 y una vibracion de lanzamiento sinusoidal de amplitud unitaria.
Modelo: x'' + 2 zeta wn (x' - y') + wn^2 (x - y) = 0 con y = sin(w t); transmisibilidad analitica T(r) = sqrt((1 + (2 zeta r)^2)/((1 - r^2)^2 + (2 zeta r)^2)), r = w/wn.
La amplitud en regimen estacionario se mide integrando con Runge-Kutta de cuarto orden y se contrasta con T(r). Tambien se verifica el cruce T = 1 en r = sqrt(2) y el maximo de T cerca de r = 1.
Supuestos: sistema lineal de un grado de libertad, amortiguamiento viscoso, excitacion armonica pura. Validez: ilustrativa; los aisladores reales tienen no linealidades.
Tolerancia: amplitud simulada frente a T(r), 1e-3 relativo; cruce T(sqrt 2) = 1 a 1e-12.
"""
from __future__ import annotations
import math, platform

FN = 10.0
WN = 2 * math.pi * FN


def trans(r, z):
    return math.sqrt((1 + (2 * z * r) ** 2) / ((1 - r * r) ** 2 + (2 * z * r) ** 2))


def simula(r, z):
    w = r * WN
    per = 2 * math.pi / w
    t_fin = 12.0 / z / WN * 1.0 + 40 * per
    dt = per / 1000
    n = int(t_fin / dt)
    s = [0.0, 0.0]
    t = 0.0

    def f(t, s):
        y = math.sin(w * t)
        yd = w * math.cos(w * t)
        return [s[1], -2 * z * WN * (s[1] - yd) - WN * WN * (s[0] - y)]

    amp = 0.0
    for i in range(n):
        k1 = f(t, s)
        k2 = f(t + dt / 2, [s[0] + dt / 2 * k1[0], s[1] + dt / 2 * k1[1]])
        k3 = f(t + dt / 2, [s[0] + dt / 2 * k2[0], s[1] + dt / 2 * k2[1]])
        k4 = f(t + dt, [s[0] + dt * k3[0], s[1] + dt * k3[1]])
        s = [s[0] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), s[1] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])]
        t += dt
        if i > n - 3000 - 1:
            amp = max(amp, abs(s[0]))
    return amp


def calc():
    r = {"filas": []}
    for z in (0.05, 0.5):
        for rr in (0.5, 1.0, math.sqrt(2), 3.0, 10.0):
            r["filas"].append((z, rr, trans(rr, z), simula(rr, z)))
    r["cruce"] = trans(math.sqrt(2), 0.05), trans(math.sqrt(2), 0.5)
    # maximo de T para zeta = 0.05 por busqueda
    mejor = max((trans(0.5 + i * 1e-4, 0.05), 0.5 + i * 1e-4) for i in range(10000))
    r["pico"] = mejor
    r["pico_aprox"] = 1 / (2 * 0.05)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'zeta':>6} {'r=f/fn':>8} {'T analitica':>12} {'amp simulada':>13}")
    for z, rr, a, b in r["filas"]:
        print(f"{z:6.2f} {rr:8.4f} {a:12.6f} {b:13.6f}")
        assert abs(a - b) / a < 1e-3
    print(f"T(sqrt 2): zeta 0.05 -> {r['cruce'][0]:.12f} ; zeta 0.5 -> {r['cruce'][1]:.12f}")
    print(f"maximo de T con zeta = 0.05: {r['pico'][0]:.4f} en r = {r['pico'][1]:.4f} ; aproximacion 1/(2 zeta) = {r['pico_aprox']:.4f}")
    assert abs(r["cruce"][0] - 1) < 1e-12 and abs(r["cruce"][1] - 1) < 1e-12
    assert abs(r["pico"][0] - r["pico_aprox"]) / r["pico_aprox"] < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
