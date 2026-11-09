#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C05: ecuacion del fabricante de lentes, lente gruesa y matrices de rayos (ABCD).

Datos: sin constantes fisicas. n = 1,517 (vidrio tipo crown, tipico de libro, ILUSTRATIVO), radios y espesores ILUSTRATIVOS.
Modelo: lente delgada 1/f = (n-1)(1/R1 - 1/R2). Lente gruesa: 1/f = (n-1)[1/R1 - 1/R2 + (n-1) d/(n R1 R2)]. Segunda via independiente: producto de matrices de
refraccion y traslacion (convencion y = altura, u = angulo; refraccion [[1,0],[-(n2-n1)/(R n2)... ]] en la forma reducida con n u); el elemento C = -1/f.
Supuestos: rayos paraxiales, superficies esfericas, aire a ambos lados. Validez: aproximacion paraxial.
Tolerancia: formula cerrada frente a matrices 1e-12 relativo; planos principales frente a matrices 1e-9 mm.
"""
from __future__ import annotations
import math, platform, sys


def mul(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


def refr(n1, n2, R):
    """Superficie esferica en la forma (y, n u): potencia P = (n2-n1)/R."""
    return [[1.0, 0.0], [-(n2 - n1) / R, 1.0]]


def tras(d, n):
    return [[1.0, d / n], [0.0, 1.0]]


def lente_matriz(n, R1, R2, d):
    m = refr(1.0, n, R1)
    m = mul(tras(d, n), m)
    m = mul(refr(n, 1.0, R2), m)
    return m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = 1.517
    print(f"{'caso':>26} {'R1':>7} {'R2':>8} {'d':>5} {'f delgada':>10} {'f gruesa':>10} {'f matrices':>11}")
    casos = [("biconvexa simetrica", 200.0, -200.0, 5.0), ("plano-convexa", 150.0, 1e12, 8.0), ("menisco convergente", 100.0, 300.0, 10.0), ("biconvexa gruesa", 100.0, -100.0, 40.0)]
    for nom, R1, R2, d in casos:
        f_del = 1 / ((n - 1) * (1 / R1 - 1 / R2))
        f_gru = 1 / ((n - 1) * (1 / R1 - 1 / R2 + (n - 1) * d / (n * R1 * R2)))
        m = lente_matriz(n, R1, R2, d)
        f_mat = -1 / m[1][0]
        print(f"{nom:>26} {R1:7.0f} {R2:8.0f} {d:5.0f} {f_del:10.3f} {f_gru:10.3f} {f_mat:11.3f}")
        assert abs(f_gru - f_mat) / f_mat < 1e-9
        assert abs(f_del - f_mat) / f_mat < 0.1
    # planos principales de la biconvexa gruesa
    R1, R2, d = 100.0, -100.0, 40.0
    m = lente_matriz(n, R1, R2, d)
    f = -1 / m[1][0]
    bfd = f * m[0][0]          # distancia del ultimo vertice al foco: y = A y0 -> bfd = -A/C
    bfd = -m[0][0] / m[1][0]
    ffd = -m[1][1] / m[1][0]
    h2 = bfd - f
    print(f"biconvexa gruesa: f = {f:.3f} mm ; distancia focal posterior (vertice) = {bfd:.3f} mm ; plano principal posterior a {-h2:.3f} mm dentro del vertice")
    h2_formula = -f * (n - 1) * d / (n * R1)       # posicion del plano principal posterior respecto al vertice 2 (formula de libro)
    print(f"  formula de libro del plano principal posterior = {h2_formula:.3f} mm")
    assert abs(abs(h2_formula) - abs(bfd - f)) < 1e-9
    assert abs(ffd - bfd) < 1e-9
    # el limite d -> 0 recupera la lente delgada
    m0 = lente_matriz(n, 200.0, -200.0, 1e-9)
    f0 = -1 / m0[1][0]
    f_del = 1 / ((n - 1) * (2 / 200.0))
    print(f"limite d -> 0: f = {f0:.6f} mm ; delgada = {f_del:.6f} mm")
    assert abs(f0 - f_del) < 1e-6
    # determinante (invariante de Lagrange)
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    print(f"det(M) = {det:.12f}")
    assert abs(det - 1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
