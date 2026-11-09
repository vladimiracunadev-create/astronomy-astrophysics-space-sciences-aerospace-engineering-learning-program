#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C07: telescopio afocal de Kepler y de Galileo, aumento angular y pupila de salida.

Datos: sin constantes fisicas. Objetivo f = 1000 mm con D = 100 mm y oculares de 25, 10 y 5 mm son ILUSTRATIVOS.
Modelo: dos lentes delgadas separadas d = f_o + f_e; aumento angular M = -f_o/f_e (Kepler) o +f_o/|f_e| (Galileo, ocular negativo). Segunda via: producto
de matrices ABCD: el elemento C se anula (sistema afocal) y el elemento D es el aumento angular. Pupila de salida D/|M| por trazado de dos rayos marginales.
Supuestos: lentes delgadas, rayos paraxiales. Validez: paraxial.
Tolerancia: C = 0 a 1e-15; M de las matrices frente a la formula 1e-12.
"""
from __future__ import annotations
import math, platform, sys


def mul(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


def lente(f):
    return [[1.0, 0.0], [-1.0 / f, 1.0]]


def tras(d):
    return [[1.0, d], [0.0, 1.0]]


def sistema(fo, fe):
    return mul(lente(fe), mul(tras(fo + fe), lente(fo)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    fo, D = 1000.0, 100.0
    print(f"objetivo f = {fo:.0f} mm, D = {D:.0f} mm (ilustrativo)")
    print(f"{'ocular':>8} {'tipo':>8} {'M formula':>10} {'M matriz':>10} {'C':>10} {'pupila salida [mm]':>19} {'longitud [mm]':>14}")
    for fe in (25.0, 10.0, 5.0, -50.0):
        s = sistema(fo, fe)
        m_f = -fo / fe
        tipo = "Kepler" if fe > 0 else "Galileo"
        m_m = s[1][1]
        # pupila de salida por rayo marginal: y = D/2, u = 0 entra; sale con y' = A y
        y_sal = s[0][0] * (D / 2)
        pupila = 2 * abs(y_sal)
        print(f"{fe:8.0f} {tipo:>8} {m_f:10.2f} {m_m:10.2f} {s[1][0]:10.1e} {pupila:19.3f} {fo + fe:14.0f}")
        assert abs(s[1][0]) < 1e-15
        assert abs(m_f - m_m) < 1e-12
        assert abs(pupila - D / abs(m_f)) < 1e-9
        assert abs(s[0][0] - 1 / m_m) < 1e-12 if abs(m_m) > 0 else True
    # un rayo de entrada con angulo u sale con angulo M u
    s = sistema(fo, 25.0)
    u = math.radians(0.5)
    y1 = s[0][1] * u
    u1 = s[1][1] * u
    print(f"rayo a 0,5 deg con ocular de 25 mm: sale a {math.degrees(u1):.3f} deg (M = {s[1][1]:.1f}), altura {y1:.3f} mm")
    assert abs(u1 + 40 * u) < 1e-12
    # aumento util: la pupila de salida no debe superar la del ojo (7 mm ilustrativo)
    print("aumento minimo para que la pupila de salida no pase de 7 mm (ilustrativo):", round(D / 7.0, 2))
    # aumento maximo practico orientativo 2 por mm de apertura
    print("aumento maximo orientativo (regla 2 D[mm]):", 2 * D)
    # ojo humano 'apertura' 0.5 mm -> pupila de salida de 0,5 mm a:
    print("aumento con pupila de salida de 0,5 mm:", D / 0.5)
    assert abs(D / 7.0 - 14.2857142857) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
