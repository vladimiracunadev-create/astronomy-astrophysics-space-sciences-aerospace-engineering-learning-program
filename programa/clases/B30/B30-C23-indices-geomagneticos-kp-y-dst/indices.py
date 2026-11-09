#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C23: construccion de un Kp sintetico de 28 valores y de un proxy de Dst con cuatro estaciones.

Datos: la escala de Kp de 28 valores (0 a 9, en tercios) y el promedio de trece estaciones de latitudes geomagneticas de 48 a 63 grados con muestreo trihorario (arXiv:1404.2836, solo
resumen) y la idea de un proxy de Dst obtenido de cuatro magnetometros terrestres (arXiv:2209.12571 y arXiv:2203.11001, solo resumen), consultados 2026-11-09. Los umbrales de rango
para K (5, 10, 20, 40, 70, 120, 200, 330, 500 nT), las latitudes de las cuatro estaciones (10, 20, 25, 30 grados), el ruido local (3 nT), los niveles de perturbacion y las lineas base
son ILUSTRATIVOS (sinteticos); no reproducen los algoritmos oficiales.
Modelo: (1) K de una estacion por tabla de umbrales de rango (0 a 9) y Kp = promedio de trece K redondeado al tercio mas cercano, con etiquetas 0o, 0+, 1-, 1o, ..., 9-, 9o;
(2) proxy de Dst: cada estacion i mide Delta H_i = Dst cos(lat_i) + ruido + linea base, y Dst_est = promedio de (Delta H_i - base_i)/cos(lat_i); Monte Carlo (10 000, semilla fija)
de la desviacion tipica frente a la teorica sigma sqrt(Sum 1/cos^2(lat_i))/4.
Supuestos: perturbacion simetrica, ruido gaussiano independiente. Validez: ilustrativa.
Tolerancia: 28 etiquetas distintas y ordenadas; ida y vuelta etiqueta -> tercios -> etiqueta; sesgo del proxy < 0.1 nT; desviacion Monte Carlo dentro del 3 % de la teorica.
"""
from __future__ import annotations
import math
import platform
import random
import sys

ETIQ = ["0o", "0+"]
for k in range(1, 9):
    ETIQ += [f"{k}-", f"{k}o", f"{k}+"]
ETIQ += ["9-", "9o"]
UMBRALES_K = (5, 10, 20, 40, 70, 120, 200, 330, 500)


def k_de_rango(rango):
    k = 0
    for i, u in enumerate(UMBRALES_K):
        if rango >= u:
            k = i + 1
    return k


def kp_etiqueta(ks):
    tercios = round(3 * sum(ks) / len(ks))
    return ETIQ[min(27, max(0, tercios))]


def tercios_de_etiqueta(e):
    return ETIQ.index(e)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert len(ETIQ) == 28 and len(set(ETIQ)) == 28
    print(f"escala de Kp: {len(ETIQ)} valores: " + " ".join(ETIQ))
    for e in ETIQ:
        assert ETIQ[tercios_de_etiqueta(e)] == e
    assert kp_etiqueta([5] * 13) == "5o" and kp_etiqueta([4] * 6 + [5] * 7) == "5-" and kp_etiqueta([9] * 13) == "9o"
    print(f"{'rango [nT]':>10} {'K':>3}")
    for r in (2, 5, 15, 45, 150, 250, 600):
        print(f"{r:10d} {k_de_rango(r):3d}")
    rng = random.Random(20261109)
    ks = [k_de_rango(abs(rng.gauss(0, 1)) * 60 + 5) for _ in range(13)]
    print(f"13 estaciones ilustrativas: K = {ks} ; promedio = {sum(ks) / 13:.3f} ; Kp = {kp_etiqueta(ks)}")
    # proxy de Dst
    lat = [math.radians(x) for x in (10, 20, 25, 30)]
    sigma = 3.0
    bases = [rng.uniform(-20, 20) for _ in lat]
    teor = sigma * math.sqrt(sum(1 / math.cos(l) ** 2 for l in lat)) / len(lat)
    print(f"latitudes (ilustrativas) {[round(math.degrees(l)) for l in lat]} grados ; ruido {sigma} nT ; desviacion teorica del proxy = {teor:.4f} nT")
    print(f"{'Dst verdadero [nT]':>19} {'media del proxy':>16} {'sesgo':>8} {'desviacion MC':>14} {'teorica':>9}")
    for dst in (-20.0, -100.0, -250.0):
        est = []
        for _ in range(10000):
            h = [dst * math.cos(l) + rng.gauss(0, sigma) + b for l, b in zip(lat, bases)]
            est.append(sum((hi - b) / math.cos(l) for hi, b, l in zip(h, bases, lat)) / len(lat))
        m = sum(est) / len(est)
        sd = math.sqrt(sum((x - m) ** 2 for x in est) / (len(est) - 1))
        print(f"{dst:19.1f} {m:16.3f} {m - dst:8.3f} {sd:14.4f} {teor:9.4f}")
        assert abs(m - dst) < 0.1 and abs(sd / teor - 1) < 0.03, f"proxy Dst={dst}"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
