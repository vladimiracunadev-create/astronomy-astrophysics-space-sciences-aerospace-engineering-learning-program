#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C10: localizacion de una fuente por tiempos de llegada y region creible sobre la esfera.

Datos: c (NIST CODATA 2022) y radio ecuatorial terrestre nominal 6.3781e6 m (IAU 2015 B3), consultados 2026-11-09.
Contexto: BAYESTAR produce mapas de localizacion en segundos (arXiv:1508.03634, resumen); GW170817 se localizo inicialmente en
31 grados cuadrados (arXiv:1710.05833, resumen). Las posiciones de los tres detectores (latitud, longitud) y el error temporal de
0.5 ms por detector son ILUSTRATIVOS (sinteticos); no se pretende reproducir ningun detector real.
Modelo: llegada a cada detector t_i = t0 - r_i . n / c (n apunta a la fuente); se observan las dos diferencias de tiempo respecto
del detector 0 con errores gaussianos independientes de desviacion sigma por detector (covarianza sigma^2 [[2,1],[1,2]]).
Posterior sobre una rejilla de Fibonacci de N puntos en la esfera (area de celda 4 pi/N): p(n) ~ exp(-chi2/2), chi2 con esa covarianza.
Region creible 90 %: celdas ordenadas por probabilidad hasta acumular 0.9 (region de maxima densidad a posteriori).
Cobertura: fraccion de ensayos (fuente verdadera aleatoria) cuya fuente cae dentro de la region 90 %.
Supuestos: ruido gaussiano, tiempos de llegada independientes de la forma de onda. Validez: ilustrativa.
Tolerancia: cobertura entre 0.84 y 0.96 en 400 ensayos con semilla fija.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

C = 299792458.0
R_T = 6.3781e6
LUG = {"A": (46.5, -119.4), "B": (30.6, -90.8), "C": (43.6, 10.5)}      # ilustrativos
SIGMA_T = 0.5e-3


def pos(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return (R_T * math.cos(la) * math.cos(lo), R_T * math.cos(la) * math.sin(lo), R_T * math.sin(la))


def rejilla(n):
    ga = math.pi * (3 - math.sqrt(5))
    pts = []
    for i in range(n):
        z = 1 - (2 * i + 1) / n
        r = math.sqrt(1 - z * z)
        pts.append((r * math.cos(ga * i), r * math.sin(ga * i), z))
    return pts


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def dt_modelo(base, n):
    return -dot(base, n) / C


def posterior_3(rej, b1, b2, d1, d2):
    inv = (2 / (3 * SIGMA_T ** 2), -1 / (3 * SIGMA_T ** 2), 2 / (3 * SIGMA_T ** 2))
    pr = []
    for n in rej:
        e1, e2 = dt_modelo(b1, n) - d1, dt_modelo(b2, n) - d2
        chi2 = inv[0] * e1 * e1 + 2 * inv[1] * e1 * e2 + inv[2] * e2 * e2
        pr.append(math.exp(-0.5 * chi2))
    s = sum(pr)
    return [p / s for p in pr]


def posterior_2(rej, b1, d1):
    pr = [math.exp(-0.5 * (dt_modelo(b1, n) - d1) ** 2 / (2 * SIGMA_T ** 2)) for n in rej]
    s = sum(pr)
    return [p / s for p in pr]


def region90(pr):
    orden = sorted(pr, reverse=True)
    acum, k = 0.0, 0
    for p in orden:
        acum += p
        k += 1
        if acum >= 0.9:
            return k, p
    return k, orden[-1]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rA, rB, rC = (pos(*LUG[k]) for k in "ABC")
    b1 = tuple(rB[i] - rA[i] for i in range(3))
    b2 = tuple(rC[i] - rA[i] for i in range(3))
    print(f"lineas de base: A-B = {math.sqrt(dot(b1, b1)) / 1e3:.0f} km (tiempo maximo {math.sqrt(dot(b1, b1)) / C * 1e3:.2f} ms) ; A-C = {math.sqrt(dot(b2, b2)) / 1e3:.0f} km ({math.sqrt(dot(b2, b2)) / C * 1e3:.2f} ms)")
    n_rej = 12000
    rej = rejilla(n_rej)
    cel = 4 * math.pi / n_rej * (180 / math.pi) ** 2
    print(f"rejilla de Fibonacci: {n_rej} puntos ; area de celda = {cel:.2f} grados cuadrados ; cielo = {4 * math.pi * (180 / math.pi) ** 2:.0f} grados cuadrados")
    rng = random.Random(20261109)
    cob3 = cob2 = 0
    areas3, areas2 = [], []
    nens = 400
    for _ in range(nens):
        z = rng.uniform(-1, 1)
        ph = rng.uniform(0, 2 * math.pi)
        r = math.sqrt(1 - z * z)
        n0 = (r * math.cos(ph), r * math.sin(ph), z)
        t1, t2 = dt_modelo(b1, n0), dt_modelo(b2, n0)
        e = [rng.gauss(0, SIGMA_T) for _ in range(3)]
        d1, d2 = t1 + e[1] - e[0], t2 + e[2] - e[0]
        pr3 = posterior_3(rej, b1, b2, d1, d2)
        k3, umbral3 = region90(pr3)
        areas3.append(k3 * cel)
        # densidad del posterior en n0 (misma normalizacion) frente al umbral de la region
        inv = (2 / (3 * SIGMA_T ** 2), -1 / (3 * SIGMA_T ** 2), 2 / (3 * SIGMA_T ** 2))
        e1, e2 = dt_modelo(b1, n0) - d1, dt_modelo(b2, n0) - d2
        chi2 = inv[0] * e1 * e1 + 2 * inv[1] * e1 * e2 + inv[2] * e2 * e2
        s = sum(math.exp(-0.5 * (inv[0] * (dt_modelo(b1, n) - d1) ** 2 + 2 * inv[1] * (dt_modelo(b1, n) - d1) * (dt_modelo(b2, n) - d2) + inv[2] * (dt_modelo(b2, n) - d2) ** 2)) for n in rej)
        if math.exp(-0.5 * chi2) / s >= umbral3:
            cob3 += 1
        pr2 = posterior_2(rej, b1, d1)
        k2, umbral2 = region90(pr2)
        areas2.append(k2 * cel)
        s2 = sum(math.exp(-0.5 * (dt_modelo(b1, n) - d1) ** 2 / (2 * SIGMA_T ** 2)) for n in rej)
        if math.exp(-0.5 * (dt_modelo(b1, n0) - d1) ** 2 / (2 * SIGMA_T ** 2)) / s2 >= umbral2:
            cob2 += 1
    c3, c2 = cob3 / nens, cob2 / nens
    print(f"3 detectores: area 90 %: mediana = {statistics.median(areas3):.0f} grados cuadrados ; cobertura = {c3:.3f} (esperada 0.90)")
    print(f"2 detectores: area 90 %: mediana = {statistics.median(areas2):.0f} grados cuadrados ; cobertura = {c2:.3f} (esperada 0.90)")
    assert 0.84 <= c3 <= 0.96 and 0.84 <= c2 <= 0.96, "cobertura"
    print(f"cociente de areas 2 detectores / 3 detectores = {statistics.median(areas2) / statistics.median(areas3):.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
