#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C16: curva de luz de una supernova con plantilla, estiramiento y tiempo del maximo; incertidumbre frente a Cramer-Rao.

Datos: ninguna constante fisica. Contexto: Maoz y colaboradores revisan las supernovas de tipo Ia y sus progenitores (arXiv:1312.0628, resumen, consultado 2026-11-09).
La plantilla (subida con constante 8 d y caida con constante 25 d), el estiramiento verdadero (1.10), el ruido (3 % del maximo), el calendario de 30 epocas y el
maximo (t0 = 20 d) son ILUSTRATIVOS (sinteticos); no representan ninguna supernova real.
Modelo: flujo f(t) = A g((t - t0)/s) con plantilla g(x) = exp(x/8) para x < 0 y exp(-x/25) para x >= 0 (cociente de subida y caida asimetrico, maximo en x = 0)
y parametros (A, t0, s). Ajuste por Nelder-Mead; incertidumbre teorica de Cramer-Rao sigma^2 (J^T J)^-1 con jacobiano numerico, frente a la desviacion de
Monte Carlo (semilla fija).
Supuestos: ruido gaussiano de desviacion constante, plantilla conocida. Validez: ilustrativa.
Tolerancia: desviacion Monte Carlo de (A, t0, s) dentro del 15 % de la de Cramer-Rao; sesgo menor que 3 errores de la media.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys


def g(x):
    return math.exp(x / 8.0) if x < 0 else math.exp(-x / 25.0)


def modelo(t, a, t0, s):
    return a * g((t - t0) / s)


def nelder_mead(f, x0, paso, iters=500):
    n = len(x0)
    pts = [list(x0)] + [[x0[j] + (paso[j] if j == i else 0) for j in range(n)] for i in range(n)]
    vals = [f(p) for p in pts]
    for _ in range(iters):
        orden = sorted(range(n + 1), key=lambda i: vals[i])
        pts, vals = [pts[i] for i in orden], [vals[i] for i in orden]
        c = [sum(pts[i][j] for i in range(n)) / n for j in range(n)]
        xr = [c[j] + (c[j] - pts[-1][j]) for j in range(n)]
        fr = f(xr)
        if fr < vals[0]:
            xe = [c[j] + 2 * (c[j] - pts[-1][j]) for j in range(n)]
            fe = f(xe)
            pts[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = [c[j] + 0.5 * (pts[-1][j] - c[j]) for j in range(n)]
            fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n + 1):
                    pts[i] = [pts[0][j] + 0.5 * (pts[i][j] - pts[0][j]) for j in range(n)]
                    vals[i] = f(pts[i])
    i = min(range(n + 1), key=lambda i: vals[i])
    return pts[i], vals[i]


def inversa3(m):
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(3)] for i, row in enumerate(m)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        pv = a[i][i]
        a[i] = [x / pv for x in a[i]]
        for r in range(3):
            if r != i:
                f = a[r][i]
                a[r] = [a[r][c] - f * a[i][c] for c in range(6)]
    return [row[3:] for row in a]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ts = [-5 + 3.0 * i for i in range(30)]
    verd = (1.0, 20.0, 1.10)
    sig = 0.03
    # Cramer-Rao
    J = []
    for t in ts:
        fila = []
        for k in range(3):
            d = 1e-6
            p1, p2 = list(verd), list(verd)
            p1[k] += d
            p2[k] -= d
            fila.append((modelo(t, *p1) - modelo(t, *p2)) / (2 * d))
        J.append(fila)
    M = [[sum(r[i] * r[j] for r in J) for j in range(3)] for i in range(3)]
    inv = inversa3(M)
    cr = [sig * math.sqrt(inv[i][i]) for i in range(3)]
    rng = random.Random(20261109)
    est = []
    for _ in range(300):
        ds = [modelo(t, *verd) + rng.gauss(0, sig) for t in ts]
        chi2 = lambda p: sum((d - modelo(t, *p)) ** 2 for t, d in zip(ts, ds)) if p[2] > 0.3 else 1e30
        mejor, _ = nelder_mead(chi2, [0.9, 18.0, 1.0], [0.1, 2.0, 0.1])
        est.append(mejor)
    nombres = ["A", "t0 [d]", "s"]
    print(f"{'parametro':<8} {'verdadero':>10} {'media':>9} {'sigma MC':>9} {'Cramer-Rao':>11} {'cociente':>9}")
    for i in range(3):
        col = [e[i] for e in est]
        mm, ss = statistics.mean(col), statistics.pstdev(col)
        print(f"{nombres[i]:<8} {verd[i]:10.4f} {mm:9.4f} {ss:9.4f} {cr[i]:11.4f} {ss / cr[i]:9.3f}")
        assert abs(mm - verd[i]) < 3 * ss / math.sqrt(300) + 1e-3, nombres[i]
        assert abs(ss / cr[i] - 1) < 0.15, f"Cramer-Rao {nombres[i]}"
    # relacion del estiramiento con el ancho: tiempo para caer a la mitad del maximo
    for s in (0.8, 1.0, 1.1, 1.3):
        t_half = s * 25.0 * math.log(2)
        print(f"estiramiento s = {s:.2f}: tiempo para caer a la mitad tras el maximo = {t_half:.2f} d")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
