#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C04: intervalos, conos de luz y tiempo propio de los gemelos por integracion numerica.

Datos: ninguno observado. Viaje de los gemelos (velocidad, duracion): SINTETICO (ilustrativo).
Modelo: intervalo s^2 = (c dt)^2 - dx^2 (genero tiempo si > 0, espacio si < 0, luz si = 0).
Tiempo propio a lo largo de una linea de universo: tau = Int sqrt(1 - v(t)^2/c^2) dt. Viaje de ida y
vuelta con velocidad constante v y tiempo coordenado total T: tau = T sqrt(1 - beta^2).
Supuestos: aceleraciones instantaneas en el giro (se desprecia su duracion). Validez: ilustrativa.
Tolerancia: 1e-9 (relativa a T) entre la integracion numerica y la solucion analitica.
"""
from __future__ import annotations
import math
import platform
import sys


def clasifica(ct, x):
    s2 = ct * ct - x * x
    if abs(s2) < 1e-12:
        return "luz"
    return "tiempo" if s2 > 0 else "espacio"


def tau_numerico(beta_de_t, T, n=200000):
    h = T / n
    s = 0.0
    for i in range(n):
        t = (i + 0.5) * h
        s += math.sqrt(1 - beta_de_t(t, T) ** 2) * h
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for ct, x in ((5, 3), (3, 5), (4, 4), (-2, 1)):
        print(f"evento (ct, x) = ({ct}, {x}): s^2 = {ct * ct - x * x:+d} -> intervalo de genero {clasifica(ct, x)}")
    T = 20.0
    for beta in (0.6, 0.8, 0.99):
        f = lambda t, TT, b=beta: b if t < TT / 2 else -b
        num = tau_numerico(f, T)
        ana = T * math.sqrt(1 - beta ** 2)
        assert abs(num - ana) < 1e-9 * T, "tau numerico != analitico"
        print(f"beta = {beta}: tau (viajero) = {num:.6f} anios ; analitico = {ana:.6f} ; el gemelo en la Tierra envejece {T:.1f}")
    g = lambda t, TT: 0.9 * math.sin(math.pi * t / TT)
    tau_v = tau_numerico(g, T, 100000)
    assert tau_v < T
    print(f"velocidad sinusoidal (max 0.9 c): tau = {tau_v:.4f} anios < {T}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
