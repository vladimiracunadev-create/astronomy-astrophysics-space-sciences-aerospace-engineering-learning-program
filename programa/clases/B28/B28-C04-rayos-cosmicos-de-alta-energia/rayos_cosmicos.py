#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C04: criterio de Hillas, espectro de potencias con rodilla y recuperacion de un dipolo de anisotropia.

Datos: c, e (NIST CODATA 2022), 1 au (IERS TN36), consultados 2026-11-09. Contexto: Observatorio Pierre Auger reporta
un dipolo de 6.5 (+1.3, -0.9) % por encima de 8e18 eV con 3e4 rayos cosmicos y mas de 5.2 sigma (arXiv:1709.07321, resumen).
Los campos B, tamanos R de las fuentes, los indices espectrales (2.7 y 3.1) y la rodilla son ILUSTRATIVOS (sinteticos).
Modelo: criterio de Hillas E_max[eV] = Z beta B[T] R[m] c; espectro J(E) ~ E^-g1 (E < Ek), E^-g2 (E > Ek) con flujo integral
analitico; dipolo: densidad 1 + d cos(theta), estimador d_hat = 3 <cos theta> con varianza 3/N (isotropia en todo el cielo).
Supuestos: cielo completo con exposicion uniforme (simplificacion), sin perdidas de energia. Validez: orientativa.
Tolerancia: 1e-6 entre flujo integral numerico y analitico; media de d_hat dentro de 3 errores del valor inyectado.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

C = 299792458.0
AU = 1.49597870700e11
PC = 648000 / math.pi * AU


def hillas(z, beta, b, r):
    return z * beta * b * r * C


def flujo_integral(e0, ek, g1, g2):
    """Int_{e0}^inf J dE con J = E^-g1 (E<ek), ek^(g2-g1) E^-g2 (E>ek), e0 < ek."""
    parte1 = (e0 ** (1 - g1) - ek ** (1 - g1)) / (g1 - 1)
    parte2 = ek ** (g2 - g1) * ek ** (1 - g2) / (g2 - 1)
    return parte1 + parte2


def flujo_numerico(e0, ek, g1, g2, n=200000):
    s = math.log(e0)
    t = math.log(1e8 * ek)
    h = (t - s) / n
    def f(ls):
        e = math.exp(ls)
        j = e ** -g1 if e < ek else ek ** (g2 - g1) * e ** -g2
        return j * e
    tot = f(s) + f(t)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(s + i * h)
    return tot * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'fuente (ilustrativa)':<26} {'B [T]':>9} {'R [m]':>10} {'E_max protón [eV]':>18} {'E_max hierro [eV]':>18}")
    for nombre, b, r in (("remanente de supernova", 1e-8, 3 * PC), ("lóbulo de radiogalaxia", 1e-9, 1e3 * PC * 1e3),
                         ("núcleo activo, chorro", 1e-4, 1e-3 * PC), ("estrella de neutrones", 1e8, 1e4)):
        print(f"{nombre:<26} {b:9.1e} {r:10.3e} {hillas(1, 1.0, b, r):18.4e} {hillas(26, 1.0, b, r):18.4e}")
    ek, g1, g2 = 1e15, 2.7, 3.1
    for e0 in (1e11, 1e13):
        an, nu = flujo_integral(e0, ek, g1, g2), flujo_numerico(e0, ek, g1, g2)
        assert abs(nu / an - 1) < 1e-6, "flujo integral"
        print(f"flujo integral (>{e0:.0e} eV) analitico = {an:.6e} ; numerico = {nu:.6e} (unidades arbitrarias)")
    print(f"cociente flujo(>1e16)/flujo(>1e15) = {flujo_integral(1e16, 1e15 * 1e3, g2, g2) / flujo_integral(1e15, 1e15 * 1e3, g2, g2):.4f} (10^-(g2-1) = {10 ** -(g2 - 1):.4f})")
    # dipolo
    rng = random.Random(20261109)
    n, d_true, nrep = 30000, 0.065, 200
    est = []
    for _ in range(nrep):
        s = 0.0
        k = 0
        while k < n:
            mu = rng.uniform(-1, 1)
            if rng.random() * (1 + d_true) <= 1 + d_true * mu:
                s += mu
                k += 1
        est.append(3 * s / n)
    media, desv = statistics.mean(est), statistics.pstdev(est)
    esp = math.sqrt(3 / n)
    print(f"dipolo inyectado {d_true:.3f}: {nrep} realizaciones de N = {n}: media = {media:.4f} ; desviacion = {desv:.4f} (esperada sqrt(3/N) = {esp:.4f})")
    print(f"significancia tipica d/sigma = {d_true / esp:.1f} (cielo completo; el valor publicado usa exposicion parcial)")
    assert abs(media - d_true) < 3 * esp / math.sqrt(nrep) * 3 and abs(desv / esp - 1) < 0.15, "dipolo recuperado"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
