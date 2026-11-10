#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C01: directividad, ganancia, abertura efectiva y ancho de haz.

Datos consultados (2026-11-10): NASA/JPL DSN 810-005 modulo 101 rev. D (2011), Tabla 1 (transmision) y Tabla 2 (recepcion) de la antena de 70 m:
  X-band 7145 MHz, ganancia 73.23 dBi, HPBW 0.038 +- 0.004 deg; X-band 8420 MHz, ganancia 74.55 dBi (DSS-14), HPBW 0.032 +- 0.003 deg;
  S-band 2115 MHz, ganancia 62.95 dBi, HPBW 0.128 +- 0.013 deg. Diametro: 70 m (texto del modulo).
CALCULADO aqui: eficiencia de apertura implicita, HPBW teorico, directividad del dipolo de media onda.
Modelo: D = 4 pi U_max / integral(U dOmega) por integracion numerica (Simpson); apertura circular G = eta (pi D/lambda)^2; HPBW = k lambda/D.
Segunda via: forma cerrada D(dipolo) = 1.6409 (valor teorico estandar, no consultado en fuente concreta) y convergencia al duplicar N.
Supuestos: sin perdidas ohmicas; k = 1.02 (apertura uniforme) y 1.20 (apertura con apodizacion tipica), ambos ILUSTRATIVOS.
Tolerancias: Simpson N=2000 vs N=4000 < 1e-9; dipolo vs 1.6409 < 1e-4; HPBW teorico dentro del rango publicado +- 25 %.
"""
from __future__ import annotations
import math, platform

C = 299_792_458.0  # m/s, valor exacto SI


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def u_dipolo(th):
    s = math.sin(th)
    if abs(s) < 1e-12:
        return 0.0
    return (math.cos(0.5 * math.pi * math.cos(th)) / s) ** 2


def directividad_dipolo(n):
    # U(theta) simetrico en phi; integral = 2 pi * int U sin(theta) dtheta; U_max = 1 en theta = pi/2
    integral = 2.0 * math.pi * simpson(lambda t: u_dipolo(t) * math.sin(t), 0.0, math.pi, n)
    return 4.0 * math.pi * 1.0 / integral


def db(x):
    return 10.0 * math.log10(x)


def apertura(d, f_hz):
    lam = C / f_hz
    g_ideal = (math.pi * d / lam) ** 2
    return lam, g_ideal


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    d1, d2 = directividad_dipolo(2000), directividad_dipolo(4000)
    print(f"Dipolo lambda/2: D = {d1:.6f} ({db(d1):.3f} dBi); convergencia |N=2000 - N=4000| = {abs(d1 - d2):.2e}")
    assert abs(d1 - d2) < 1e-9 and abs(d1 - 1.6409) < 1e-4
    ae = lambda g, lam: g * lam * lam / (4 * math.pi)
    print("Abertura efectiva del dipolo (lambda = 1 m): Ae = %.4f m2 (= 0.1306 lambda^2)" % ae(d1, 1.0))
    print()
    print("Antena de 70 m (DSN, valores PUBLICADOS) frente a apertura ideal (CALCULADA), D = 70 m")
    print(" banda   f [MHz]  G_pub [dBi]  G_ideal [dBi]  eta_impl   HPBW_pub [deg]  HPBW k=1.02  k=1.20")
    filas = [("S tx", 2115.0, 62.95, 0.128, 0.013), ("X tx", 7145.0, 73.23, 0.038, 0.004), ("X rx", 8420.0, 74.55, 0.032, 0.003)]
    for nom, f, g_pub, h_pub, h_tol in filas:
        lam, g_id = apertura(70.0, f * 1e6)
        eta = 10 ** ((g_pub - db(g_id)) / 10)
        h1 = math.degrees(1.02 * lam / 70.0)
        h2 = math.degrees(1.20 * lam / 70.0)
        print(f" {nom:5s} {f:8.1f}   {g_pub:8.2f}    {db(g_id):9.2f}     {eta:6.3f}      {h_pub:6.3f}      {h1:8.4f} {h2:7.4f}")
        assert 0.5 < eta < 1.0
        assert abs(h1 - h_pub) / h_pub < 0.25
    # escalado con la frecuencia: +20 log(f/f0), como indica el modulo 101
    g_x7145 = 73.23
    g_x8420 = g_x7145 + 20 * math.log10(8420 / 7145)
    print(f"Escalado 20 log(f/f0) de 7145 a 8420 MHz: {g_x8420:.2f} dBi (publicado 74.55 en la antena DSS-14: diferencia {74.55 - g_x8420:+.2f} dB)")
    # Friis / abertura efectiva de la antena de 70 m en X rx
    lam = C / 8.42e9
    g = 10 ** (74.55 / 10)
    print(f"Abertura efectiva X rx: Ae = {ae(g, lam):.0f} m2; area geometrica = {math.pi * 35 ** 2:.0f} m2; ratio = {ae(g, lam) / (math.pi * 35 ** 2):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
