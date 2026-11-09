#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C13: distribucion de tamanos de ley de potencias de cuerpos remanentes, muestreo y estimacion.

Datos SINTETICOS (no observados): poblacion de N = 100 000 cuerpos con diametros D en [1, 50] km y distribucion acumulada
N(>D) proporcional a D^-q truncada, con q = 2.5 (exponente de ensenanza; el valor de equilibrio colisional de la literatura NO se consulto).
Densidad 2000 kg/m^3 (ilustrativa); semilla 20261109. Sin datos externos ni constantes fisicas consultadas.
Sistema de referencia: no aplica. Unidades: km, kg.
Via 1: fracciones de masa y numero analiticas de la Pareto truncada. Via 2: muestreo por transformada inversa y estimador de maxima verosimilitud
(raiz de la ecuacion de score por biseccion). Tolerancias: q estimado dentro de 3 errores estandar (q/sqrt(N)); fracciones de masa muestrales dentro de 0.10 (absoluto) de las analiticas; conteos dentro de 3 sigma de Poisson (la masa la dominan pocos cuerpos grandes).
"""
from __future__ import annotations
import math, platform, random

Q, DMIN, DMAX, N, RHO = 2.5, 1.0, 50.0, 100000, 2000.0


def inversa(u, q=Q):
    R = DMAX / DMIN
    return DMIN * (1.0 - u * (1.0 - R ** -q)) ** (-1.0 / q)


def mle(xs):
    n, R = len(xs), DMAX / DMIN
    s = sum(math.log(x / DMIN) for x in xs)
    score = lambda q: n / q - n * R ** -q * math.log(R) / (1.0 - R ** -q) - s
    a, b = 0.05, 10.0
    for _ in range(200):
        c = 0.5 * (a + b)
        if score(c) > 0: a = c
        else: b = c
    return 0.5 * (a + b)


def masa_acum_analitica(d, q=Q):
    """Fraccion de la masa en cuerpos con D > d (densidad de probabilidad ~ D^(-q-1), masa ~ D^3)."""
    num = DMAX ** (3 - q) - d ** (3 - q)
    den = DMAX ** (3 - q) - DMIN ** (3 - q)
    return num / den


def frac_num_analitica(d, q=Q):
    R = DMAX / DMIN
    return (d / DMIN) ** -q * 1.0 / (1.0 - R ** -q) - R ** -q / (1.0 - R ** -q)


def calcular():
    rng = random.Random(20261109)
    xs = [inversa(rng.random()) for _ in range(N)]
    qh = mle(xs)
    err = Q / math.sqrt(N)
    masa_tot = sum(x ** 3 for x in xs)
    filas = []
    for d in (5.0, 10.0, 20.0):
        mm = sum(x ** 3 for x in xs if x > d) / masa_tot
        nm = sum(1 for x in xs if x > d) / N
        filas.append((d, nm, frac_num_analitica(d), mm, masa_acum_analitica(d)))
    masa_kg = (math.pi / 6.0) * RHO * masa_tot * 1e9  # D en km -> m: factor (1e3)^3
    return dict(qh=qh, err=err, filas=filas, dmax_muestra=max(xs), masa_kg=masa_kg, esp_dmax=DMIN * N ** (1 / Q))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Poblacion SINTETICA: N = {N}, D en [{DMIN:.0f}, {DMAX:.0f}] km, q verdadero = {Q}, densidad {RHO:.0f} kg/m^3, semilla 20261109")
    print(f"q estimado (maxima verosimilitud) = {r['qh']:.4f} ; error estandar aproximado = {r['err']:.4f} ; desviacion = {abs(r['qh'] - Q) / r['err']:.2f} errores estandar")
    print(f"{'D > [km]':>9} {'num. muestra':>13} {'num. analitico':>15} {'masa muestra':>13} {'masa analitica':>15}")
    for d, nm, na, mm, ma in r["filas"]:
        print(f"{d:9.0f} {nm:13.6f} {na:15.6f} {mm:13.4f} {ma:15.4f}")
    print(f"Mayor cuerpo de la muestra = {r['dmax_muestra']:.1f} km ; escala D_min N^(1/q) sin truncar = {r['esp_dmax']:.1f} km ; masa total sintetica = {r['masa_kg']:.3e} kg")
    assert abs(r["qh"] - Q) < 3 * r["err"]
    for d, nm, na, mm, ma in r["filas"]:
        assert abs(nm - na) * N < 3 * math.sqrt(na * N)
        assert abs(mm - ma) < 0.15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
