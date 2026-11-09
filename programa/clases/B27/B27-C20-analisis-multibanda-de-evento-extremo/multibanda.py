#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C20: distribucion espectral de energia de dos jorobas y retardo entre bandas.

Datos: ninguna constante fisica. Contexto: GW170817 y GRB 170817A como ejemplo de observacion multimensajero
(arXiv:1710.05834, resumen, consultado 2026-11-09). Todos los espectros, curvas de luz, ruido y retardos son
SINTETICOS (generados aqui con semilla fija); no se cita ninguna medicion.
Modelo: (1) nu F_nu de cada joroba es una log-parabola log10(nuF) = a + b x + c x^2, x = log10(nu); el ajuste
por minimos cuadrados lineales da el pico x_p = -b/(2c). (2) Dos curvas de luz: la banda 1 es un paseo aleatorio
y la banda 2 es la 1 retrasada L muestras, escalada y con ruido; el retardo se recupera con la correlacion de Pearson
en funcion del desfase.
Supuestos: ruido gaussiano en log (SED) y blanco (curvas); sin huecos de muestreo. Validez: ilustrativa.
Tolerancia: 0.05 dex en la posicion del pico y 1 muestra en el retardo mediano.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys


def ajuste_parabola(xs, ys):
    """Minimos cuadrados de y = a + b x + c x^2 (ecuaciones normales 3x3 por eliminacion)."""
    s = [sum(x ** k for x in xs) for k in range(5)]
    t = [sum(y * x ** k for x, y in zip(xs, ys)) for k in range(3)]
    m = [[s[0], s[1], s[2], t[0]], [s[1], s[2], s[3], t[1]], [s[2], s[3], s[4], t[2]]]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(3):
            if r != i:
                f = m[r][i] / m[i][i]
                m[r] = [m[r][k] - f * m[i][k] for k in range(4)]
    return [m[i][3] / m[i][i] for i in range(3)]


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy)


def retardo(x, y, maxlag):
    mejor, lag_m = -2, 0
    for lag in range(-maxlag, maxlag + 1):
        if lag >= 0:
            r = pearson(x[:len(x) - lag], y[lag:])
        else:
            r = pearson(x[-lag:], y[:len(y) + lag])
        if r > mejor:
            mejor, lag_m = r, lag
    return lag_m, mejor


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    # 1) SED de dos jorobas (sinteticas): picos en log nu = 15 (sincrotron) y 22 (alta energia)
    def sed(x):
        h1 = -0.12 * (x - 15.0) ** 2 + (-10.0)
        h2 = -0.10 * (x - 22.0) ** 2 + (-10.8)
        return math.log10(10 ** h1 + 10 ** h2)
    xs = [10 + 0.25 * i for i in range(61)]
    dat = [(x, sed(x) + rng.gauss(0, 0.03)) for x in xs]
    for nombre, lo, hi, vp in (("joroba baja", 11.0, 18.0, 15.0), ("joroba alta", 19.5, 25.0, 22.0)):
        sub = [(x, y) for x, y in dat if lo <= x <= hi]
        a, b, c = ajuste_parabola([x for x, _ in sub], [y for _, y in sub])
        xp = -b / (2 * c)
        yp = a - b * b / (4 * c)
        print(f"{nombre}: pico en log nu = {xp:.3f} (verdadero {vp}) ; log10(nu F_nu) en el pico = {yp:.3f} ; curvatura = {c:.4f}")
        assert abs(xp - vp) < 0.05, f"pico de la {nombre}"
    # 2) retardo entre bandas
    L = 7
    lags = []
    for _ in range(100):
        n = 1000
        x = []
        v = 0.0
        for _ in range(n + L):
            v += rng.gauss(0, 1)
            x.append(v)
        b1 = x[L:]                    # banda 1: x(t)
        b2 = [0.8 * x[i] + rng.gauss(0, 0.5) for i in range(n)]   # banda 2: x(t - L)
        lag, _ = retardo(b1, b2, 30)
        lags.append(lag)
    med = statistics.median(lags)
    print(f"retardo verdadero = {L} muestras ; 100 realizaciones: mediana = {med} ; media = {statistics.mean(lags):.2f} ; desviacion = {statistics.pstdev(lags):.2f}")
    print(f"histograma de retardos (valor: veces): {dict(sorted((k, lags.count(k)) for k in set(lags)))}")
    assert abs(med - L) <= 1, "retardo mediano"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
