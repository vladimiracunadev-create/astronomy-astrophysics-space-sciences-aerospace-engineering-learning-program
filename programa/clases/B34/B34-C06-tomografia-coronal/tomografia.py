#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C06: reconstruccion tomografica de una emisividad 2D con el metodo de Kaczmarz (ART).

Datos: ninguna constante fisica. La rejilla (16 x 16), el fantasma (un bulto gaussiano y un anillo), las direcciones de vista (0, 90, 45 y 135 grados), el ruido (1 %) y la semilla fija son ILUSTRATIVOS
(sinteticos); no se reconstruye ninguna corona real.
Modelo: integrales de linea por suma de pixeles a lo largo de filas, columnas y dos familias de diagonales; resolucion de A x = b con iteraciones de Kaczmarz (proyecciones sucesivas sobre cada ecuacion)
con positividad; error cuadratico medio relativo frente al fantasma con 2 direcciones (0 y 90) y con 4 direcciones; efecto del ruido.
Supuestos: geometria de pixeles discretos, vistas en direcciones ortogonales y diagonales. Validez: ilustrativa.
Tolerancia: el residuo disminuye con las iteraciones; el error con 4 direcciones es menor que con 2.
"""
from __future__ import annotations
import math, platform, random, sys
N = 16

def fantasma():
    f = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            r1 = math.hypot(i - 5.5, j - 5.5)
            r2 = math.hypot(i - 10.5, j - 9.5)
            f[i][j] = math.exp(-r1 ** 2 / 4.0) + (1.0 if 2.5 < r2 < 4.0 else 0.0)
    return f

def ecuaciones(dirs):
    eq = []
    if 0 in dirs:
        eq += [[(i, j) for j in range(N)] for i in range(N)]
    if 90 in dirs:
        eq += [[(i, j) for i in range(N)] for j in range(N)]
    if 45 in dirs:
        eq += [[(i, i + k) for i in range(N) if 0 <= i + k < N] for k in range(-N + 1, N)]
    if 135 in dirs:
        eq += [[(i, s - i) for i in range(N) if 0 <= s - i < N] for s in range(2 * N - 1)]
    return [e for e in eq if e]

def reconstruir(eqs, b, it=200):
    x = [[0.0] * N for _ in range(N)]
    for _ in range(it):
        for e, bi in zip(eqs, b):
            s = sum(x[i][j] for i, j in e)
            d = (bi - s) / len(e)
            for i, j in e:
                x[i][j] = max(0.0, x[i][j] + d)
    return x

def ecm(a, b):
    num = sum((a[i][j] - b[i][j]) ** 2 for i in range(N) for j in range(N))
    den = sum(b[i][j] ** 2 for i in range(N) for j in range(N))
    return math.sqrt(num / den)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f = fantasma()
    rng = random.Random(20261109)
    print(f"{'direcciones':<24} {'ecuaciones':>10} {'iteraciones':>12} {'error relativo (sin ruido)':>28} {'error con ruido 1 %':>21}")
    res = {}
    for dirs in ((0, 90), (0, 90, 45, 135)):
        eqs = ecuaciones(dirs)
        b = [sum(f[i][j] for i, j in e) for e in eqs]
        bn = [x * (1 + rng.gauss(0, 0.01)) for x in b]
        for it in (10, 200):
            r0 = ecm(reconstruir(eqs, b, it), f)
            r1 = ecm(reconstruir(eqs, bn, it), f)
            print(f"{str(dirs):<24} {len(eqs):10d} {it:12d} {r0:28.4f} {r1:21.4f}")
            res[(dirs, it)] = (r0, r1)
    assert res[((0, 90), 200)][0] < res[((0, 90), 10)][0] + 1e-9
    assert res[((0, 90, 45, 135), 200)][0] < res[((0, 90), 200)][0]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
