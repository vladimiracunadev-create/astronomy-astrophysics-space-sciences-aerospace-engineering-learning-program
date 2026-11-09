#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C07: comparacion de un mapa modelado con uno observado (correlacion, razon y prueba de Kolmogorov-Smirnov calibrada por Monte Carlo).

Datos: ninguna constante fisica. Los mapas sinteticos de 24 x 24 pixeles (observado: bulto gaussiano mas ruido; modelo A: mismo bulto desplazado 1 pixel; modelo B: bulto mas ancho), el ruido (5 %) y la semilla fija
son ILUSTRATIVOS (sinteticos); no se compara ningun modelo coronal real con observaciones.
Modelo: correlacion de Pearson pixel a pixel, razon media modelo/observacion, desplazamiento optimo por correlacion cruzada y distancia D de Kolmogorov-Smirnov entre las distribuciones de intensidad;
el valor p se calibra con 500 permutaciones (reasignacion aleatoria de etiquetas) y se compara con la formula asintotica.
Supuestos: pixeles independientes (los mapas reales estan correlacionados espacialmente, lo que invalida el valor p ingenuo). Validez: ilustrativa.
Tolerancia: el desplazamiento recuperado es 1 pixel; el modelo A tiene mayor correlacion que el B.
"""
from __future__ import annotations
import math, platform, random, sys
N = 24

def mapa(cx, cy, s, rng=None, ruido=0.0):
    return [[math.exp(-((i - cx) ** 2 + (j - cy) ** 2) / (2 * s * s)) * (1 + (rng.gauss(0, ruido) if rng else 0)) for j in range(N)] for i in range(N)]

def plano(m):
    return [x for fila in m for x in fila]

def pearson(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))

def ks(a, b):
    sa, sb = sorted(a), sorted(b)
    i = j = 0
    d = 0.0
    while i < len(sa) and j < len(sb):
        if sa[i] <= sb[j]:
            i += 1
        else:
            j += 1
        d = max(d, abs(i / len(sa) - j / len(sb)))
    return d

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    obs = mapa(11.5, 11.5, 4.0, rng, 0.05)
    ma = mapa(12.5, 11.5, 4.0)
    mb = mapa(11.5, 11.5, 6.0)
    print(f"{'modelo':<28} {'correlacion':>12} {'razon media':>12} {'D (KS)':>8} {'p asintotico':>13} {'p por permutaciones':>20}")
    po = plano(obs)
    res = {}
    for nombre, m in (("A: desplazado 1 pixel", ma), ("B: bulto mas ancho", mb)):
        pm = plano(m)
        r = pearson(pm, po)
        razon = sum(pm) / sum(po)
        d = ks(pm, po)
        n = len(po)
        lam = (math.sqrt(n / 2) + 0.12 + 0.11 / math.sqrt(n / 2)) * d
        pa = 2 * sum((-1) ** (k - 1) * math.exp(-2 * k * k * lam * lam) for k in range(1, 100))
        pa = min(1.0, max(0.0, pa))
        mezcla = pm + po
        cuenta = 0
        for _ in range(500):
            rng.shuffle(mezcla)
            if ks(mezcla[:n], mezcla[n:]) >= d:
                cuenta += 1
        print(f"{nombre:<28} {r:12.4f} {razon:12.4f} {d:8.4f} {pa:13.4f} {cuenta / 500:20.4f}")
        res[nombre] = r
    # desplazamiento optimo por correlacion cruzada
    mejor = None
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            a = [ma[i][j] for i in range(3, N - 3) for j in range(3, N - 3)]
            b = [obs[i + dx][j + dy] for i in range(3, N - 3) for j in range(3, N - 3)]
            r = pearson(a, b)
            if mejor is None or r > mejor[0]:
                mejor = (r, dx, dy)
    print(f"desplazamiento optimo del modelo A respecto de lo observado: ({mejor[1]}, {mejor[2]}) pixeles con correlacion {mejor[0]:.4f}")
    assert (mejor[1], mejor[2]) == (1, 0) or (mejor[1], mejor[2]) == (-1, 0) or abs(mejor[1]) == 1
    assert res["A: desplazado 1 pixel"] > res["B: bulto mas ancho"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
