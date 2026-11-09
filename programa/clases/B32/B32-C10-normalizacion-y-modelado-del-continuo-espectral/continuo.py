#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C10: normalizacion del continuo con ajuste polinomico iterativo y recorte sigma.

Datos: ninguna constante fisica. El continuo (polinomio cubico), las lineas (profundidades 0.1 a 0.6), el ruido (sigma = 0.005) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: espectro = continuo(x) x (1 - sum de lineas gaussianas) + ruido; ajuste por minimos cuadrados (ecuaciones normales resueltas con eliminacion gaussiana) de un polinomio de grado 3 con recortes
asimetricos (se descartan puntos mas de 1 sigma por debajo y 3 por encima) iterados; se compara con la mediana (normalizacion ingenua).
Supuestos: continuo suave y lineas de absorcion. Validez: ilustrativa.
Tolerancia: error maximo relativo del continuo recuperado menor del 1.5 % y al menos diez veces menor que el de la normalizacion ingenua.
"""
from __future__ import annotations
import math, platform, random, sys

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

def ajuste(xs, ys, g=3):
    a = [[sum(x ** (i + j) for x in xs) for j in range(g + 1)] for i in range(g + 1)]
    b = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(g + 1)]
    return resolver(a, b)

def ev(c, x):
    return sum(ci * x ** i for i, ci in enumerate(c))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    xs = [-1 + 2 * i / 599 for i in range(600)]
    cont = lambda x: 1.0 + 0.15 * x - 0.20 * x * x + 0.10 * x ** 3
    lineas = [(-0.7, 0.012, 0.4), (-0.3, 0.02, 0.6), (0.1, 0.015, 0.5), (0.45, 0.03, 0.3), (0.8, 0.012, 0.1)]
    ys = []
    for x in xs:
        d = sum(a * math.exp(-0.5 * ((x - c) / w) ** 2) for c, w, a in lineas)
        ys.append(cont(x) * (1 - d) + rng.gauss(0, 0.005))
    sel = list(range(len(xs)))
    for it in range(8):
        c = ajuste([xs[i] for i in sel], [ys[i] for i in sel])
        res = [ys[i] - ev(c, xs[i]) for i in range(len(xs))]
        sd = math.sqrt(sum(res[i] ** 2 for i in sel) / len(sel))
        nuevo = [i for i in range(len(xs)) if -1.0 * sd < res[i] < 3.0 * sd]
        if nuevo == sel:
            break
        sel = nuevo
    err = max(abs(ev(c, x) / cont(x) - 1) for x in xs)
    med = sorted(ys)[len(ys) // 2]
    err_med = max(abs(med / cont(x) - 1) for x in xs)
    print(f"iteraciones = {it + 1} ; puntos de continuo = {len(sel)} de {len(xs)} ; error maximo relativo del continuo recuperado = {err * 100:.3f} %")
    print(f"normalizacion ingenua con la mediana: error maximo = {err_med * 100:.2f} %")
    print(f"coeficientes recuperados: {[round(v, 4) for v in c]} ; verdaderos: [1.0, 0.15, -0.2, 0.1]")
    assert err < 0.015 and err < err_med / 10
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
