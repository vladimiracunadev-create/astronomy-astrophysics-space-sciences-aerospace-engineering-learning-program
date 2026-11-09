#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C08: ajuste de la caida de una curva de luz y probabilidad de detectar un transitorio segun la cadencia.

Datos: ninguna constante fisica. Contexto: la contrapartida optica de GW170817 se identifico a ~10 arcsec de una galaxia
(arXiv:1710.05835, resumen). Todas las magnitudes, el indice de caida (1.3), el ruido (0.1 mag) y las cadencias son SINTETICOS
(generados aqui con semilla fija); no se cita ninguna medicion.
Modelo: tras el maximo, m(t) = m0 + 2.5 alpha log10(t/t0) (ley de potencias de indice alpha); ajuste lineal por minimos cuadrados
en log t con error estandar sigma_alpha = sigma/(2.5 sqrt(S_xx)); tiempo sobre un limite m_lim: t_lim = t0 10^(0.4 (m_lim - m0)/alpha);
probabilidad de que una cadencia D_cad detecte un evento visible durante T_vis: min(1, T_vis/D_cad).
Supuestos: ruido gaussiano independiente, sin extincion, un solo filtro. Validez: ilustrativa.
Tolerancia: la desviacion del indice recuperado debe coincidir con sigma_alpha dentro del 10 %; la probabilidad MC con min(1, T/D) dentro de 0.01.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys


def ajuste(ts, ms, t0):
    xs = [math.log10(t / t0) for t in ts]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ms) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ms))
    b = sxy / sxx
    return my - b * mx, b / 2.5, sxx


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    m0, t0, alpha, sig = 17.0, 1.0, 1.3, 0.1
    ts = [1.0 * 1.25 ** k for k in range(0, 14)]       # 1 .. ~18 d
    est = []
    for _ in range(500):
        ms = [m0 + 2.5 * alpha * math.log10(t / t0) + rng.gauss(0, sig) for t in ts]
        a0, a, sxx = ajuste(ts, ms, t0)
        est.append(a)
    sa = sig / (2.5 * math.sqrt(sxx))
    media, desv = statistics.mean(est), statistics.pstdev(est)
    print(f"{len(ts)} epocas entre {ts[0]:.1f} y {ts[-1]:.1f} d, ruido {sig} mag, alpha verdadero = {alpha}")
    print(f"500 realizaciones: alpha medio = {media:.4f} ; desviacion = {desv:.4f} ; error estandar analitico = {sa:.4f}")
    assert abs(desv / sa - 1) < 0.10 and abs(media - alpha) < 4 * sa / math.sqrt(500), "ajuste de alpha"
    # tiempo sobre un limite
    print(f"{'m_lim':>6} {'t_lim [d]':>10}")
    for ml in (19.0, 20.0, 21.0, 22.0):
        print(f"{ml:6.1f} {t0 * 10 ** (0.4 * (ml - m0) / alpha):10.2f}")
    # cadencia
    t_vis = 10 ** (0.4 * (21.0 - m0) / alpha) * t0
    print(f"visible por encima de m = 21 durante {t_vis:.2f} d")
    print(f"{'cadencia [d]':>13} {'P analitica':>12} {'P Monte Carlo':>14}")
    for cad in (2.0, 5.0, 10.0, 17.0, 30.0, 60.0):
        n = 40000
        hits = 0
        for _ in range(n):
            ini = rng.uniform(0, cad)        # fase de la cadencia respecto del inicio del evento
            # el evento es visible durante [0, t_vis]; se observa en ini + k cad
            if ini <= t_vis:
                hits += 1
        pa = min(1.0, t_vis / cad)
        pm = hits / n
        assert abs(pm - pa) < 0.01, f"cadencia {cad}"
        print(f"{cad:13.1f} {pa:12.4f} {pm:14.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
