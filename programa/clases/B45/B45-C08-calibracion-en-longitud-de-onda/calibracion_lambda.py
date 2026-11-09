#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C08: calibracion en longitud de onda con lineas de lampara sinteticas.

Datos: lineas de lampara SINTETICAS: 14 posiciones aleatorias (semilla 20261109) en un detector de 2048 pixeles, con longitudes de onda exactas generadas con la dispersion verdadera
lambda(u) = 600 + 50 u + 2 u^2 - 1 u^3 nm, u = (x - 1023,5)/1023,5, y centroides con ruido gaussiano de 0,05 pixel. No son lineas de ninguna lampara real. La formula de Edlen/Birch-Downs
para el indice del aire (n - 1 = 1e-8 [8342,13 + 2406030/(130 - s^2) + 15997/(38,9 - s^2)], s = 1/lambda en 1/micra) es conocimiento de libro NO consultado aqui y se usa solo de orden de magnitud.
Modelo: ajuste polinomico de minimos cuadrados (ecuaciones normales con eliminacion gaussiana) de grado 1 a 5; validacion cruzada dejando una linea fuera.
Supuestos: ruido blanco en los centroides, catalogo exacto, dispersion suave. Validez: la extrapolacion fuera del rango de lineas no esta respaldada por el ajuste.
Tolerancia: el grado 3 reproduce la dispersion verdadera con RMS menor que 0,003 nm dentro del rango; el grado 1 deja un RMS de mas de 0,3 nm.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
NPIX = 2048


def lam_true(x):
    u = (x - 1023.5) / 1023.5
    return 600 + 50 * u + 2 * u ** 2 - 1 * u ** 3


def resolver(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def ajustar(xs, ys, grado):
    us = [(x - 1023.5) / 1023.5 for x in xs]
    k = grado + 1
    A = [[sum(u ** (i + j) for u in us) for j in range(k)] for i in range(k)]
    b = [sum(y * u ** i for u, y in zip(us, ys)) for i in range(k)]
    return resolver(A, b)


def evaluar(c, x):
    u = (x - 1023.5) / 1023.5
    return sum(ci * u ** i for i, ci in enumerate(c))


def rms(v):
    return math.sqrt(sum(a * a for a in v) / len(v))


def calcular():
    rnd = random.Random(SEMILLA)
    xs_true = sorted(rnd.uniform(60, 1990) for _ in range(14))
    lam = [lam_true(x) for x in xs_true]
    xs = [x + rnd.gauss(0, 0.05) for x in xs_true]
    r = {"n": len(xs), "filas": []}
    rejilla = [i * 8 for i in range(256)]
    for g in range(1, 6):
        c = ajustar(xs, lam, g)
        res = [evaluar(c, x) - l for x, l in zip(xs, lam)]
        # validacion cruzada
        cv = []
        for i in range(len(xs)):
            xi = xs[:i] + xs[i + 1:]
            li = lam[:i] + lam[i + 1:]
            ci = ajustar(xi, li, g)
            cv.append(evaluar(ci, xs[i]) - lam[i])
        dentro = [x for x in rejilla if xs[0] <= x <= xs[-1]]
        err_dentro = rms([evaluar(c, x) - lam_true(x) for x in dentro])
        err_ext = abs(evaluar(c, -150) - lam_true(-150))
        r["filas"].append((g, rms(res), rms(cv), err_dentro, err_ext))
    r["disp"] = (lam_true(2047) - lam_true(0)) / 2047
    r["xmin"], r["xmax"] = xs[0], xs[-1]
    # aire frente a vacio en 589,3 nm
    s2 = (1 / 0.5893) ** 2
    r["n_aire"] = 1e-8 * (8342.13 + 2406030 / (130 - s2) + 15997 / (38.9 - s2))
    r["dlam_aire"] = 589.3 * r["n_aire"]
    r["dv_aire"] = r["n_aire"] * 299792.458
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{r['n']} lineas entre x = {r['xmin']:.1f} y {r['xmax']:.1f} ; dispersion media = {r['disp']*1000:.2f} pm/pixel")
    print(f"{'grado':>5} {'RMS ajuste (nm)':>16} {'RMS CV (nm)':>12} {'error dentro (nm)':>18} {'error en x=-150 (nm)':>21}")
    for g, a, b, c, d in r["filas"]:
        print(f"{g:5d} {a:16.5f} {b:12.5f} {c:18.5f} {d:21.4f}")
    print(f"indice del aire en 589,3 nm: n - 1 = {r['n_aire']:.4e} ; delta lambda = {r['dlam_aire']:.4f} nm ; equivale a {r['dv_aire']:.1f} km/s")
    f = {g: (a, b, c, d) for g, a, b, c, d in r["filas"]}
    assert f[1][0] > 0.3
    assert f[3][2] < 0.003
    assert f[3][1] < 0.01
    assert f[5][3] > f[3][3]
    assert 0.15 < r["dlam_aire"] < 0.18
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
