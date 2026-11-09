#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C14: periodo, curva de fase y ajuste de armonicos de una estrella variable periodica.

Datos: ninguna constante fisica. Contexto: el periodograma de Lomb-Scargle es el algoritmo habitual para detectar senales periodicas en series con muestreo desigual
(VanderPlas, arXiv:1703.09824, resumen, consultado 2026-11-09). El periodo (5.3 d), la amplitud (0.30 mag), los armonicos, el ruido (0.03 mag), el numero de
medidas (120) y la duracion (100 d) son ILUSTRATIVOS (sinteticos); no se simula ninguna estrella real.
Modelo: m(t) = m0 + Sum_k a_k cos(2 pi k t/P) + b_k sen(2 pi k t/P) (k = 1..3); busqueda del periodo por chi^2 de un ajuste lineal de K armonicos en una rejilla de
frecuencias, afinada por parabola; dispersion de fase (PDM) como metodo independiente; incertidumbre teorica del periodo para una sinusoide
sigma_f = sqrt(6) sigma/(pi T A sqrt(N)) (formula estandar, no consultada), contrastada con Monte Carlo (semilla fija).
Supuestos: ruido blanco, periodo constante. Validez: ilustrativa.
Tolerancia: periodo recuperado con error < 3 sigma_P; PDM y ajuste de armonicos coinciden en el periodo dentro de 1e-3 relativo; sigma_P MC dentro del 30 % de la teorica.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

P0, AMP, SIG, N, T = 5.3, 0.30, 0.03, 120, 100.0
ARMS = ((0.30, 0.10), (0.08, -0.05), (0.02, 0.03))


def curva(t, p=P0):
    return sum(a * math.cos(2 * math.pi * (k + 1) * t / p) + b * math.sin(2 * math.pi * (k + 1) * t / p) for k, (a, b) in enumerate(ARMS))


def resolver(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(n):
            if r != i:
                f = m[r][i] / m[i][i]
                m[r] = [m[r][c] - f * m[i][c] for c in range(n + 1)]
    return [m[i][n] / m[i][i] for i in range(n)]


def chi2_armonicos(ts, ms, p, nh):
    X = []
    for t in ts:
        fila = [1.0]
        for k in range(1, nh + 1):
            fila += [math.cos(2 * math.pi * k * t / p), math.sin(2 * math.pi * k * t / p)]
        X.append(fila)
    n = len(X[0])
    A = [[sum(x[i] * x[j] for x in X) for j in range(n)] for i in range(n)]
    B = [sum(x[i] * m for x, m in zip(X, ms)) for i in range(n)]
    c = resolver(A, B)
    return sum((m - sum(ci * xi for ci, xi in zip(c, x))) ** 2 for x, m in zip(X, ms))


def pdm(ts, ms, p, nb=10):
    bins = [[] for _ in range(nb)]
    for t, m in zip(ts, ms):
        bins[int(((t / p) % 1.0) * nb)].append(m)
    var = statistics.pvariance(ms)
    s = sum(statistics.pvariance(b) * len(b) for b in bins if len(b) > 1)
    n = sum(len(b) for b in bins if len(b) > 1)
    return (s / n) / var


def buscar(ts, ms, nh, f0=0.05, f1=1.0, nf=1800):
    mejor = (1e30, 0.0)
    fs = [f0 + (f1 - f0) * i / nf for i in range(nf + 1)]
    cs = [chi2_armonicos(ts, ms, 1 / f, nh) for f in fs]
    i = min(range(len(cs)), key=lambda j: cs[j])
    if 0 < i < len(cs) - 1:
        y0, y1, y2 = cs[i - 1], cs[i], cs[i + 1]
        d = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
        return 1 / (fs[i] + d * (fs[1] - fs[0]))
    return 1 / fs[i]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ts = sorted(rng.uniform(0, T) for _ in range(N))
    ms = [curva(t) + rng.gauss(0, SIG) for t in ts]
    p1 = buscar(ts, ms, 1)
    p3 = buscar(ts, ms, 3)
    # PDM en torno
    cand = [p3 * (1 + d) for d in [i * 1e-4 for i in range(-200, 201)]]
    ppdm = min(cand, key=lambda p: pdm(ts, ms, p))
    print(f"periodo verdadero = {P0} d ; ajuste de 1 armonico: {p1:.5f} d ; de 3 armonicos: {p3:.5f} d ; PDM: {ppdm:.5f} d")
    assert abs(p3 / P0 - 1) < 1e-3 and abs(ppdm / p3 - 1) < 1e-3
    # amplitud pico a pico a partir del ajuste de 3 armonicos y de la curva verdadera
    fase = [(t / p3) % 1.0 for t in ts]
    print(f"theta PDM en el periodo verdadero = {pdm(ts, ms, P0):.4f} ; en un periodo erroneo (1.37 x) = {pdm(ts, ms, 1.37 * P0):.4f}")
    # Monte Carlo del periodo con 1 armonico (sinusoide pura)
    amp1 = math.hypot(*ARMS[0])
    ps = []
    for _ in range(60):
        ts2 = sorted(rng.uniform(0, T) for _ in range(N))
        ms2 = [amp1 * math.cos(2 * math.pi * t / P0 + 0.5) + rng.gauss(0, SIG) for t in ts2]
        ps.append(buscar(ts2, ms2, 1, 0.15, 0.23, 120))
    mm, ss = statistics.mean(ps), statistics.pstdev(ps)
    sf = math.sqrt(6) * SIG / (math.pi * T * amp1 * math.sqrt(N))
    sp = sf * P0 ** 2
    print(f"sinusoide pura (amplitud {amp1:.3f} mag): periodo MC = {mm:.5f} +/- {ss:.5f} d ; teorico sigma_P = {sp:.5f} d")
    assert abs(mm - P0) < 3 * ss / math.sqrt(60) + 1e-4, "sesgo del periodo"
    assert abs(ss / sp - 1) < 0.30, "sigma_P frente a la teorica"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
