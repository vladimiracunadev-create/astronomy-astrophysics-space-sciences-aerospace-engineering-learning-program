#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C35: control estadistico de procesos: carta X-barra, EWMA, capacidad Cp/Cpk y longitud media de racha (ARL) por simulacion.

DATOS SINTETICOS (generados aqui, semilla 84035; NO medidos): una dimension de proceso con media 10,000 mm y sigma = 0,010 mm, especificacion 10,000 +/- 0,050 mm,
subgrupos de n = 5. Se simulan 40 subgrupos; desde el 21 la media se desplaza +1 sigma (0,010 mm).
Cartas con sigma conocida: Shewhart X-barra con limites mu +/- 3 sigma/sqrt(n); EWMA con lambda = 0,2 y L = 2,86 (L elegido para ARL0 cercano a 370; NO consultado en tablas:
se verifica aqui por simulacion), z_t = lambda xbar_t + (1 - lambda) z_(t-1), limites mu +/- L sigma sqrt(lambda/((2-lambda)n)(1-(1-lambda)^(2t))).
ARL por simulacion (3000 repeticiones para el proceso en control, 3000 para el desplazado). Segunda via: ARL teorica de Shewhart: 1/p con p = P(|Z| > 3 - delta sqrt(n)...) exacta con Phi.
Tolerancias: ARL0 de Shewhart dentro de 15 % de 370,4; ARL1 simulada dentro de 10 % de la teorica.
"""
from __future__ import annotations
import math, platform, random

MU, SG, N = 10.000, 0.010, 5
USL, LSL = 10.050, 9.950
LAM, LL = 0.2, 2.86


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def arl_teorica(delta_sigma):
    d = delta_sigma * math.sqrt(N)
    p = phi(-3 + d) + phi(-3 - d)
    return 1 / p


def corrida_shewhart(rng, delta, max_t=20000):
    lim = 3 * SG / math.sqrt(N)
    for t in range(1, max_t + 1):
        xb = MU + delta * SG + SG / math.sqrt(N) * rng.gauss(0, 1)
        if abs(xb - MU) > lim:
            return t
    return max_t


def corrida_ewma(rng, delta, max_t=20000):
    z = MU
    for t in range(1, max_t + 1):
        xb = MU + delta * SG + SG / math.sqrt(N) * rng.gauss(0, 1)
        z = LAM * xb + (1 - LAM) * z
        lim = LL * SG * math.sqrt(LAM / ((2 - LAM) * N) * (1 - (1 - LAM) ** (2 * t)))
        if abs(z - MU) > lim:
            return t
    return max_t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(84035)
    xb = []
    for g in range(40):
        desp = 1.0 if g >= 20 else 0.0
        xb.append(MU + desp * SG + SG / math.sqrt(N) * rng.gauss(0, 1))
    lim = 3 * SG / math.sqrt(N)
    print(f"Proceso SINTETICO: mu = {MU} mm, sigma = {SG} mm, n = {N}; limites de la carta X-barra: [{MU - lim:.5f}, {MU + lim:.5f}] mm")
    fuera = [g + 1 for g, v in enumerate(xb) if abs(v - MU) > lim]
    print(f"Desplazamiento de +1 sigma desde el subgrupo 21. Senales Shewhart (fuera de 3 sigma): subgrupos {fuera if fuera else 'ninguna'}")
    z = MU
    senales = []
    for t, v in enumerate(xb, 1):
        z = LAM * v + (1 - LAM) * z
        l_t = LL * SG * math.sqrt(LAM / ((2 - LAM) * N) * (1 - (1 - LAM) ** (2 * t)))
        if abs(z - MU) > l_t:
            senales.append(t)
    print(f"Senales EWMA (lambda = 0,2, L = 2,86): subgrupos {senales[:6] if senales else 'ninguna'}{' ...' if len(senales) > 6 else ''}")
    cp = (USL - LSL) / (6 * SG)
    cpk0 = min(USL - MU, MU - LSL) / (3 * SG)
    cpk1 = min(USL - (MU + SG), (MU + SG) - LSL) / (3 * SG)
    print(f"Capacidad: Cp = {cp:.3f}; Cpk centrado = {cpk0:.3f}; Cpk con desplazamiento de +1 sigma = {cpk1:.3f}")
    print("Longitudes medias de racha (ARL) por simulacion (3000 corridas), subgrupos hasta la senal:")
    r1 = random.Random(84036)
    print(f"{'desplazamiento':>15s} {'Shewhart sim':>13s} {'Shewhart teor.':>15s} {'EWMA sim':>10s}")
    for delta in (0.0, 0.5, 1.0, 2.0):
        s = sum(corrida_shewhart(r1, delta) for _ in range(3000)) / 3000
        e = sum(corrida_ewma(r1, delta) for _ in range(3000)) / 3000
        teo = arl_teorica(delta)
        print(f"{delta:12.1f} s {s:13.2f} {teo:15.2f} {e:10.2f}")
        if delta == 0.0:
            assert abs(s - teo) / teo < 0.15
        if delta == 1.0:
            assert abs(s - teo) / teo < 0.10
    print(f"ARL teorica de Shewhart con 3 sigma sin desplazamiento = {arl_teorica(0.0):.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
