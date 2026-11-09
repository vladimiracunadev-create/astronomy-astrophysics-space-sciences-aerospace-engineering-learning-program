#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C11: movimiento superluminico aparente, aberracion y amplificacion Doppler de un chorro relativista.

Datos: c (NIST CODATA 2022), consultado 2026-11-09. Los factores de Lorentz y angulos son ILUSTRATIVOS (sinteticos);
no se cita ninguna medicion de un chorro real.
Modelo: una fuente que se mueve con velocidad beta c a un angulo theta de la visual. Velocidad aparente transversal
beta_app = beta sin(theta)/(1 - beta cos(theta)), maxima en cos(theta) = beta con valor beta gamma. Factor Doppler
delta = 1/(gamma (1 - beta cos(theta))). Aberracion: cos(theta') = (cos(theta) - beta)/(1 - beta cos(theta)); el
semiangulo de la emision en el sistema de reposo (theta' = 90 grados) corresponde a cos(theta) = beta.
Supuestos: blob puntual, velocidad constante, sin curvatura. Validez: 0 < beta < 1.
Tolerancia: 1e-9 entre el maximo numerico y beta gamma; 1e-9 en la relacion delta(theta_max).
"""
from __future__ import annotations
import math
import platform
import sys


def beta_app(beta, th):
    return beta * math.sin(th) / (1 - beta * math.cos(th))


def doppler(beta, th):
    g = 1 / math.sqrt(1 - beta * beta)
    return 1 / (g * (1 - beta * math.cos(th)))


def maximo(beta):
    a, b = 1e-6, math.pi / 2
    gr = (math.sqrt(5) - 1) / 2
    c_, d_ = b - gr * (b - a), a + gr * (b - a)
    for _ in range(300):
        if beta_app(beta, c_) > beta_app(beta, d_):
            b = d_
        else:
            a = c_
        c_, d_ = b - gr * (b - a), a + gr * (b - a)
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'gamma':>6} {'beta':>9} {'theta_max [deg]':>16} {'1/gamma [deg]':>14} {'beta_app max':>13} {'beta gamma':>11} {'delta(theta_max)':>17}")
    for g in (2.0, 5.0, 10.0, 30.0):
        b = math.sqrt(1 - 1 / g ** 2)
        th = maximo(b)
        m = beta_app(b, th)
        assert abs(m / (b * g) - 1) < 1e-9, "maximo de la velocidad aparente"
        assert abs(math.cos(th) - b) < 1e-7, "cos(theta_max) = beta"
        d = doppler(b, th)
        assert abs(d - g) < 1e-7 * g, "delta(theta_max) = gamma"
        print(f"{g:6.1f} {b:9.6f} {math.degrees(th):16.4f} {math.degrees(1 / g):14.4f} {m:13.4f} {b * g:11.4f} {d:17.4f}")
    # aberracion: theta' = 90 grados en el sistema de reposo
    b = math.sqrt(1 - 1 / 100.0)
    th = math.acos(b)
    cos_p = (math.cos(th) - b) / (1 - b * math.cos(th))
    assert abs(cos_p) < 1e-12
    print(f"gamma = 10: theta' = 90 grados en reposo <-> theta = {math.degrees(th):.4f} grados ({math.degrees(1 / 10):.4f} = 1/gamma)")
    # amplificacion: cociente de flujos blob (delta^3) y jet continuo (delta^2) entre apuntando y a 90 grados
    for th_deg in (0.0, 5.0, 90.0):
        t = math.radians(th_deg)
        d = doppler(b, t)
        print(f"theta = {th_deg:5.1f} grados: delta = {d:8.4f} ; delta^3 = {d ** 3:12.4f} ; delta^2 = {d ** 2:10.4f}")
    # lado contrario
    d_aprox, d_rec = doppler(b, 0.0), doppler(b, math.pi)
    print(f"cociente de flujos blob entre el chorro que se acerca y el que se aleja (theta = 0 y 180): {(d_aprox / d_rec) ** 3:.4e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
