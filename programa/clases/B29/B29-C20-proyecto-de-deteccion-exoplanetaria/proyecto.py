#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C20: busqueda de transitos con ajuste de cajas e inyeccion-recuperacion para medir la completitud.

Datos: ninguna constante fisica. Contexto: Kovacs, Zucker y Mazeh estudian las caracteristicas estadisticas de un algoritmo de ajuste de cajas para buscar transitos periodicos
y muestran que el parametro crucial es la relacion senal-ruido efectiva (arXiv:astro-ph/0206099, resumen, consultado 2026-11-09). La cadencia de 2 h, la duracion de 60 d,
el ruido de 400 ppm por muestra, la duracion del transito (3 h) y las profundidades inyectadas son ILUSTRATIVOS (sinteticos).
Modelo: serie f_i = 1 + ruido (sigma = 400 ppm) con un tren de transitos en caja (profundidad d, periodo P, duracion D, epoca T0); busqueda de cajas: para cada periodo de
una rejilla logaritmica se pliegan las muestras en bins de ancho D y se busca la caja de un bin con maxima relacion senal-ruido SNR = (media_fuera - media_dentro)/(sigma sqrt(1/n_dentro + 1/n_fuera));
se recupera si el periodo hallado difiere menos de 1 % del verdadero y SNR > 7. Completitud = fraccion recuperada en inyecciones aleatorias (semilla fija).
Supuestos: ruido blanco gaussiano, transito en caja, un solo planeta. Validez: ilustrativa.
Tolerancia: caso ilustrativo recuperado con error de periodo < 1 %; completitud no decreciente con la profundidad (permitiendo 0.15 de fluctuacion estadistica).
"""
from __future__ import annotations
import math
import platform
import random
import sys

CAD, DUR, SIG, DUR_T = 2.0 / 24, 60.0, 400e-6, 3.0 / 24
TS = [i * CAD for i in range(int(DUR / CAD))]


def serie(depth, p, t0, rng):
    return [1 + rng.gauss(0, SIG) - (depth if ((t - t0) % p) < DUR_T else 0.0) for t in TS]


def bls(ys, periodos):
    n = len(ys)
    tot = sum(ys)
    mejor = (0.0, 0.0, 0.0)
    for p in periodos:
        nb = max(4, int(round(p / DUR_T)))
        sumas = [0.0] * nb
        cuentas = [0] * nb
        for t, y in zip(TS, ys):
            k = int(((t % p) / p) * nb)
            sumas[k] += y
            cuentas[k] += 1
        for k in range(nb):
            nd = cuentas[k]
            if nd < 2 or n - nd < 2:
                continue
            md = sumas[k] / nd
            mf = (tot - sumas[k]) / (n - nd)
            snr = (mf - md) / (SIG * math.sqrt(1 / nd + 1 / (n - nd)))
            if snr > mejor[0]:
                mejor = (snr, p, mf - md)
    return mejor


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ratio = 1.002
    periodos = []
    p = 2.0
    while p < 20.0:
        periodos.append(p)
        p *= ratio
    print(f"{len(TS)} muestras (cadencia {CAD * 24:.0f} h, {DUR:.0f} d), {len(periodos)} periodos de prueba entre 2 y 20 d, ruido {SIG * 1e6:.0f} ppm")
    p_v, d_v = 7.3, 1500e-6
    ys = serie(d_v, p_v, 2.1, rng)
    snr, pf, dep = bls(ys, periodos)
    print(f"caso ilustrativo: P = {p_v} d, profundidad {d_v * 1e6:.0f} ppm -> periodo hallado = {pf:.4f} d ; profundidad = {dep * 1e6:.0f} ppm ; SNR = {snr:.1f}")
    assert abs(pf / p_v - 1) < 0.01
    # ruido puro: distribucion del maximo de SNR
    maxs = []
    for _ in range(12):
        sn, _, _ = bls([1 + rng.gauss(0, SIG) for _ in TS], periodos)
        maxs.append(sn)
    print(f"ruido puro: SNR maximo sobre la rejilla (12 series) = {min(maxs):.2f} - {max(maxs):.2f} (media {sum(maxs) / len(maxs):.2f}); umbral de recuperacion = 7")
    # inyeccion-recuperacion
    niveles = (500e-6, 1000e-6, 1500e-6, 3000e-6)
    print(f"{'profundidad [ppm]':>18} {'inyecciones':>12} {'recuperadas':>12} {'completitud':>12}")
    comp = []
    for d in niveles:
        rec = 0
        n_iny = 10
        for _ in range(n_iny):
            pv = math.exp(rng.uniform(math.log(2.5), math.log(15.0)))
            ys = serie(d, pv, rng.uniform(0, pv), rng)
            sn, pf, _ = bls(ys, periodos)
            if sn > 7 and abs(pf / pv - 1) < 0.01:
                rec += 1
        comp.append(rec / n_iny)
        print(f"{d * 1e6:18.0f} {n_iny:12d} {rec:12d} {rec / n_iny:12.2f}")
    for a, b in zip(comp[:-1], comp[1:]):
        assert b >= a - 0.15, "completitud no decreciente"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
