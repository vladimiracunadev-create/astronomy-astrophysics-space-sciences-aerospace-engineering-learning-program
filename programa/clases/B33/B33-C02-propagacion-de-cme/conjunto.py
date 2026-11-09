#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C02: conjunto de propagacion de una CME con el modelo de arrastre y propagacion lineal de errores.

Datos: R_sol (UAI 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09. La velocidad inicial (1000 +/- 100 km/s), el viento (400 +/- 50 km/s), el arrastre (2e-8 +/- 1e-8 km^-1), la distancia inicial
(20 R_sol) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: tiempo de transito a 1 au del modelo de arrastre r(t) = r0 + w t + ln(1 + gamma (v0 - w) t)/gamma (biseccion); 20 000 miembros con parametros gaussianos; media, desviacion y percentiles;
propagacion lineal de errores con derivadas numericas centradas; fraccion de miembros que llegan antes de 48 h.
Supuestos: parametros independientes y gaussianos, arrastre cuadratico, viento uniforme. Validez: orientativa.
Tolerancia: desviacion del conjunto frente a la lineal dentro del 10 %.
"""
from __future__ import annotations
import math, platform, random, sys
R_SOL, AU = 6.957e5, 1.49597870700e8

def transito(v0, w, g, r0=20 * R_SOL):
    lo, hi = 0.0, 1e7
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        k = g * (v0 - w)
        r = r0 + w * mid + math.log(1 + k * mid) / g
        if r < AU:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) / 3600

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    p0 = (1000.0, 400.0, 2e-8)
    sg = (100.0, 50.0, 1e-8)
    t0 = transito(*p0)
    print(f"transito central = {t0:.2f} h")
    rng = random.Random(20261109)
    ts = []
    while len(ts) < 20000:
        v0 = rng.gauss(p0[0], sg[0]); w = rng.gauss(p0[1], sg[1]); g = rng.gauss(p0[2], sg[2])
        if g > 2e-9 and v0 > w + 50:
            ts.append(transito(v0, w, g))
    ts.sort()
    m = sum(ts) / len(ts)
    sd = math.sqrt(sum((t - m) ** 2 for t in ts) / (len(ts) - 1))
    print(f"conjunto: media = {m:.2f} h ; desviacion = {sd:.2f} h ; percentiles 5/50/95 = {ts[1000]:.1f}/{ts[10000]:.1f}/{ts[19000]:.1f} h")
    var = 0.0
    print(f"{'parametro':<10} {'dT/dp (h por unidad)':>22} {'contribucion a la varianza [h^2]':>34}")
    for j, nombre in enumerate(("v0", "w", "gamma")):
        h = sg[j] * 0.01
        a = list(p0); b = list(p0)
        a[j] += h; b[j] -= h
        d = (transito(*a) - transito(*b)) / (2 * h)
        c = (d * sg[j]) ** 2
        var += c
        print(f"{nombre:<10} {d:22.4e} {c:34.3f}")
    sl = math.sqrt(var)
    print(f"desviacion lineal = {sl:.2f} h ; conjunto = {sd:.2f} h ; cociente = {sd / sl:.3f}")
    assert abs(sd / sl - 1) < 0.10
    print(f"fraccion que llega en menos de 48 h: {sum(1 for t in ts if t < 48) / len(ts):.3f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
