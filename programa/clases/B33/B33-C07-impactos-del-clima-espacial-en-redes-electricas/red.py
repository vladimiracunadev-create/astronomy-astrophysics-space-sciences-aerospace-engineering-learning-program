#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C07: corrientes de tierra en una red de corriente continua de tres subestaciones.

Datos: ninguna constante fisica. Las resistencias de tierra (0.5, 0.8, 0.4 ohm), las de las lineas (3, 4, 5 ohm) y los campos geoelectricos (1 V/km sobre lineas de 100, 150 y 80 km) son ILUSTRATIVOS (sinteticos).
Modelo: red de tres nodos conectados por tres lineas (triangulo); cada nodo tiene una resistencia a tierra; cada linea tiene una fuente V = E L en serie con su resistencia (campo uniforme); sistema
nodal G v = i (analisis nodal con eliminacion gaussiana); corrientes de tierra I_k = v_k/R_k; la suma de las corrientes de tierra es cero (conservacion de la corriente); comparacion con el caso analitico de
dos nodos I = V/(R_linea + R_1 + R_2).
Supuestos: red resistiva en corriente continua, sin transformadores no lineales. Validez: orientativa.
Tolerancia: suma de corrientes de tierra menor que 1e-12 A; caso de dos nodos frente al analitico a 1e-12.
"""
from __future__ import annotations
import platform, sys

def resolver(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x

def red(rt, lineas):
    """lineas: lista de (i, j, R, V) con la fuente V orientada de i a j. Devuelve corrientes de tierra."""
    n = len(rt)
    g = [[0.0] * n for _ in range(n)]
    iny = [0.0] * n
    for k in range(n):
        g[k][k] += 1 / rt[k]
    for i, j, r, v in lineas:
        g[i][i] += 1 / r; g[j][j] += 1 / r; g[i][j] -= 1 / r; g[j][i] -= 1 / r
        iny[j] += v / r        # la fuente en serie equivale a una inyeccion v/r en el nodo j y -v/r en i
        iny[i] -= v / r
    # referencia: se fija un nodo? no hace falta porque cada nodo tiene tierra
    volt = resolver(g, iny)
    return [volt[k] / rt[k] for k in range(n)], volt

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ia, _ = red([0.5, 0.8], [(0, 1, 3.0, 100.0)])
    ana = 100.0 / (3.0 + 0.5 + 0.8)
    print(f"dos nodos: corrientes de tierra = {ia[0]:.6f} A y {ia[1]:.6f} A ; analitico V/(R + R1 + R2) = {ana:.6f} A")
    assert abs(abs(ia[0]) - ana) < 1e-12 and abs(ia[0] + ia[1]) < 1e-12
    rt = [0.5, 0.8, 0.4]
    lin = [(0, 1, 3.0, 100.0), (1, 2, 4.0, 150.0), (0, 2, 5.0, 80.0)]
    i_t, v = red(rt, lin)
    print(f"{'nodo':>5} {'R tierra [ohm]':>15} {'V nodo [V]':>11} {'I tierra [A]':>13}")
    for k in range(3):
        print(f"{k:5d} {rt[k]:15.2f} {v[k]:11.4f} {i_t[k]:13.4f}")
    s = sum(i_t)
    print(f"suma de corrientes de tierra = {s:.2e} A (conservacion)")
    assert abs(s) < 1e-12
    i2, _ = red(rt, [(a, b, r, 2 * vv) for a, b, r, vv in lin])
    print(f"campo duplicado: corrientes = {[round(x, 4) for x in i2]} (el doble: {[round(2 * x, 4) for x in i_t]})")
    assert all(abs(x - 2 * y) < 1e-12 for x, y in zip(i2, i_t))
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
