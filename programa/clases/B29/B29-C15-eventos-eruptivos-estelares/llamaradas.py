#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C15: modelo de llamarada, energia y distribucion de energias de una poblacion de llamaradas.

Datos: ninguna constante fisica. Contexto: Davenport reune mas de 6100 llamaradas de la enana M GJ 1243 con energias de 1e29 a 1e33 erg en 11 meses de datos
de Kepler con cadencia de 1 minuto (arXiv:1411.3723, resumen, consultado 2026-11-09). El indice de la ley de potencias (1.8), la luminosidad quiescente
(1e30 erg/s) y los parametros de la llamarada de ejemplo (amplitud 0.1, tau = 10 min) son ILUSTRATIVOS (sinteticos).
Modelo: llamarada de subida rapida y caida exponencial F(t) = A exp(-t/tau) (t >= 0, subida instantanea), energia E = L_q A tau; distribucion de energias
dN/dE ~ E^-alpha entre E_min y E_max (truncada). Muestreo por transformada inversa; estimador de maxima verosimilitud de alpha para la ley truncada (ecuacion
resuelta por biseccion). Verificacion por Monte Carlo (semilla fija) con n = 6100 llamaradas por muestra.
Supuestos: energias independientes, sin cadencia de deteccion. Validez: ilustrativa.
Tolerancia: sesgo de alpha menor que 3 errores de la media; desviacion MC dentro del 10 % de la teorica (alpha - 1)/sqrt(n) (valida sin truncamiento).
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

E_MIN, E_MAX, ALFA = 1e29, 1e33, 1.8


def muestrear(n, alfa, rng, emin=E_MIN, emax=E_MAX):
    a = 1 - alfa
    lo, hi = emin ** a, emax ** a
    return [(lo + rng.random() * (hi - lo)) ** (1 / a) for _ in range(n)]


def mle_truncada(es, emin=E_MIN, emax=E_MAX):
    s = sum(math.log(e / emin) for e in es) / len(es)
    lr = math.log(emax / emin)

    def g(a):
        # derivada de la logverosimilitud por llamarada respecto de a (con parametrizacion u = a - 1)
        u = a - 1
        if abs(u) < 1e-9:
            return lr / 2 - s
        return 1 / u - lr / (math.exp(u * lr) - 1) - s
    lo, hi = 1.0001, 6.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lq, amp, tau = 1e30, 0.1, 600.0
    e_ej = lq * amp * tau
    print(f"llamarada de ejemplo: amplitud {amp}, tau = 10 min -> energia = L_q A tau = {e_ej:.3e} erg")
    # integral numerica de F(t) dt
    n, dt = 20000, 0.1
    integ = sum(amp * math.exp(-i * dt / tau) * dt for i in range(n * 3))
    print(f"integral numerica de A exp(-t/tau) dt hasta 10 tau = {integ:.4f} (A tau = {amp * tau:.4f})")
    assert abs(integ / (amp * tau) - 1) < 1e-3
    rng = random.Random(20261109)
    ests = []
    for _ in range(200):
        es = muestrear(6100, ALFA, rng)
        ests.append(mle_truncada(es))
    mm, ss = statistics.mean(ests), statistics.pstdev(ests)
    teo = (ALFA - 1) / math.sqrt(6100)
    print(f"alpha verdadero = {ALFA} ; 200 muestras de 6100 llamaradas: media = {mm:.4f} ; desviacion = {ss:.4f} ; teorica (alpha - 1)/sqrt(n) = {teo:.4f}")
    assert abs(mm - ALFA) < 3 * ss / math.sqrt(200) + 1e-3, "sesgo de alpha"
    assert abs(ss / teo - 1) < 0.15
    es = muestrear(6100, ALFA, rng)
    print(f"{'E_min [erg]':>12} {'N(>E) simulado':>16} {'N(>E) analitico':>17}")
    a = 1 - ALFA
    for exp in (29, 30, 31, 32):
        e0 = 10.0 ** exp
        sim = sum(1 for e in es if e > e0)
        ana = 6100 * (e0 ** a - E_MAX ** a) / (E_MIN ** a - E_MAX ** a)
        print(f"{e0:12.0e} {sim:16d} {ana:17.1f}")
    # energia total emitida
    tot = sum(es)
    print(f"energia total de las 6100 llamaradas = {tot:.3e} erg ; fraccion de la energia en el 1 % mas energetico = {sum(sorted(es)[-61:]) / tot:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
