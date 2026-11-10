#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C11: transmisibilidad de un sistema de un grado de libertad, factor Q y ecuacion de Miles.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B), Tabla 2.4-4 (minimo de mano de obra, 45,4 kg o menos): 20 Hz 0,01 g2/Hz; +3 dB/oct hasta 80 Hz;
0,04 g2/Hz hasta 500 Hz; -3 dB/oct hasta 2000 Hz con 0,01 g2/Hz; total publicado 6,8 g rms.
DATOS ILUSTRATIVOS: frecuencias propias 100 Hz y 300 Hz, factores Q = 10 y 25 (amortiguamiento zeta = 1/(2Q)), ASD plana de 0,04 g2/Hz.
Modelo: excitacion de base de un oscilador; transmisibilidad T(f) = sqrt((1 + (2 z r)^2)/((1 - r^2)^2 + (2 z r)^2)), r = f/fn.
Miles (ASD plana): g_rms = sqrt(pi/2 fn Q ASD(fn)). Segunda via: integral numerica de T^2 ASD(f) df (Simpson, 1 Hz a 5000 Hz, 1e6 pasos)
para ASD plana y para el perfil de la Tabla 2.4-4. Tolerancias: Miles frente a integral numerica < 1 % para ASD plana (Q >= 10).
"""
from __future__ import annotations
import math, platform


def T(f, fn, z):
    r = f / fn
    return math.sqrt((1 + (2 * z * r) ** 2) / ((1 - r * r) ** 2 + (2 * z * r) ** 2))


def asd_mano(f):
    if f < 20 or f > 2000:
        return 0.0
    if f <= 80:
        return 0.01 * (f / 20)
    if f <= 500:
        return 0.04
    return 0.04 * (500 / f)


def integra(fn, z, asd, f1=1.0, f2=5000.0, n=1_000_000):
    h = (f2 - f1) / n
    s = asd(f1) * T(f1, fn, z) ** 2 + asd(f2) * T(f2, fn, z) ** 2
    for i in range(1, n):
        f = f1 + i * h
        s += (4 if i % 2 else 2) * asd(f) * T(f, fn, z) ** 2
    return math.sqrt(s * h / 3)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Oscilador con excitacion de base (parametros ILUSTRATIVOS)")
    print(f"{'fn [Hz]':>8s} {'Q':>4s} {'zeta':>7s} {'Tmax exacta':>12s} {'f del pico/fn':>14s} {'T(fn)':>8s}")
    for fn, Q in ((100.0, 10.0), (100.0, 25.0), (300.0, 10.0)):
        z = 1 / (2 * Q)
        # pico exacto: r^2 = (sqrt(1+8z^2) - 1)/(4 z^2)... se obtiene por busqueda numerica
        best = max(((T(fn * (0.5 + i * 1e-5), fn, z), 0.5 + i * 1e-5) for i in range(100001)))
        print(f"{fn:8.0f} {Q:4.0f} {z:7.4f} {best[0]:12.4f} {best[1]:14.5f} {T(fn, fn, z):8.4f}")
    print("Respuesta rms a ASD plana de 0,04 g2/Hz: Miles frente a integral numerica")
    mx = 0.0
    for fn, Q in ((100.0, 10.0), (100.0, 25.0), (300.0, 10.0)):
        z = 1 / (2 * Q)
        miles = math.sqrt(math.pi / 2 * fn * Q * 0.04)
        num = integra(fn, z, lambda f: 0.04, n=200000)
        # La integral numerica llega hasta 5000 Hz y la ASD plana tambien; la diferencia es la cola
        d = abs(miles - num) / num
        mx = max(mx, d)
        print(f"  fn = {fn:5.0f} Hz, Q = {Q:3.0f}: Miles = {miles:7.3f} g rms ; numerica = {num:7.3f} g rms ; dif = {d * 100:.3f} %")
    print("Respuesta a la ASD de mano de obra minima del GEVS (Tabla 2.4-4):")
    for fn, Q in ((100.0, 10.0), (300.0, 10.0), (1000.0, 10.0)):
        z = 1 / (2 * Q)
        miles = math.sqrt(math.pi / 2 * fn * Q * asd_mano(fn))
        num = integra(fn, z, asd_mano, n=200000)
        print(f"  fn = {fn:6.0f} Hz, Q = {Q:3.0f}: Miles = {miles:7.3f} g rms ; numerica = {num:7.3f} g rms ; 3 sigma = {3 * num:7.2f} g")
    print("Entrada: 6,784 g rms (calculada en B84-C01); amplificacion rms a 300 Hz, Q = 10 = {:.2f}".format(
        integra(300.0, 0.05, asd_mano, n=200000) / 6.784))
    assert mx < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
