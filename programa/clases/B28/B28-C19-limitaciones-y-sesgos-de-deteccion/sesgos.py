#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C19: sesgo de seleccion de Malmquist en una muestra limitada por flujo.

Datos: ninguna constante fisica. Contexto: GWTC-1 reune las detecciones de las dos primeras campanas (arXiv:1811.12907, resumen,
consultado 2026-11-09). La poblacion (luminosidad gaussiana con M0 = -16 y sigma = 1 mag, uniforme en volumen hasta 1000 Mpc) y la
magnitud limite de 21 son ILUSTRATIVAS (sinteticas).
Modelo: m = M + 5 log10(d/Mpc) + 25; se detecta si m < m_lim. Probabilidad de deteccion a la distancia d: Phi(z), z = (m_lim - mu(d) - M0)/sigma,
mu(d) = 5 log10(d) + 25. Media de M entre los detectados (normal truncada): <M> = M0 - sigma phi(z)/Phi(z). Se promedia en cada capa de
distancia con peso d^2 (volumen). Monte Carlo con semilla fija.
Supuestos: sin extincion ni corte en masa. Validez: ilustrativa.
Tolerancia: la media de M de los detectados en cada capa dentro de 4 errores estadisticos del valor analitico.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys


def Phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))


def phi(z):
    return math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)


def analitico(d0, d1, m0, sig, mlim, n=4000):
    h = (d1 - d0) / n
    num = den = det = vol = 0.0
    for i in range(n):
        d = d0 + (i + 0.5) * h
        z = (mlim - (5 * math.log10(d) + 25) - m0) / sig
        p = Phi(z)
        w = d * d
        det += w * p
        vol += w
        if p > 1e-300:
            num += w * p * (m0 - sig * phi(z) / p)
            den += w * p
    return num / den, det / vol


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m0, sig, mlim, dmax = -16.0, 1.0, 21.0, 1000.0
    rng = random.Random(20261109)
    n = 600000
    capas = [(1.0, 30.0), (30.0, 100.0), (100.0, 300.0), (300.0, 1000.0)]
    datos = {c: [] for c in capas}
    tot = {c: 0 for c in capas}
    todos = []
    for _ in range(n):
        d = dmax * rng.random() ** (1 / 3)
        mm = rng.gauss(m0, sig)
        m = mm + 5 * math.log10(d) + 25
        det = m < mlim
        for c in capas:
            if c[0] <= d < c[1]:
                tot[c] += 1
                if det:
                    datos[c].append(mm)
        if det:
            todos.append(mm)
    print(f"{n} fuentes uniformes en volumen hasta {dmax:.0f} Mpc ; M0 = {m0}, sigma = {sig}, m_lim = {mlim}")
    print(f"{'capa [Mpc]':>12} {'n capa':>8} {'detectadas':>11} {'f_det MC':>9} {'f_det anal.':>12} {'<M> MC':>8} {'<M> anal.':>10} {'sesgo [mag]':>12}")
    for c in capas:
        mm = datos[c]
        am, fd = analitico(c[0], c[1], m0, sig, mlim)
        fmc = len(mm) / tot[c]
        media = statistics.mean(mm)
        err = statistics.pstdev(mm) / math.sqrt(len(mm))
        assert abs(media - am) < 4 * err + 1e-3, f"media en la capa {c}"
        assert abs(fmc - fd) < 4 * math.sqrt(fd * (1 - fd) / tot[c]) + 1e-3, f"fraccion detectada en la capa {c}"
        print(f"{c[0]:5.0f}-{c[1]:5.0f} {tot[c]:8d} {len(mm):11d} {fmc:9.4f} {fd:12.4f} {media:8.3f} {am:10.3f} {media - m0:12.3f}")
    print(f"muestra completa de detectados: {len(todos)} ; <M> = {statistics.mean(todos):.3f} (verdadero {m0}) ; sesgo = {statistics.mean(todos) - m0:+.3f} mag")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
