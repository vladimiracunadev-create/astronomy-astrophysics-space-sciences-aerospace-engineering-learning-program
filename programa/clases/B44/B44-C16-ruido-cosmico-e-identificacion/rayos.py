#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C16: rechazo de rayos cosmicos con una pila de cuadros y probabilidad de coincidencia.

Datos: ninguna constante fisica. Fondo de 100 e-, ruido de 5 e-, impactos de +500 e-, probabilidad de impacto por pixel y cuadro de 0,01 y cuadros de 100 x 100 pixeles
son ILUSTRATIVOS (sinteticos); no describen la tasa de rayos cosmicos de ningun sensor ni sitio.
Modelo: 5 cuadros con impactos independientes de un solo pixel. Se marca un pixel si x - mediana(pila) > 7 sigma_robusta (MAD de los residuos). Pixeles con 2 impactos o mas:
N [1 - (1-p)^5 - 5 p (1-p)^4]; con 3 o mas la mediana se contamina. Semilla 20261109.
Supuestos: impactos independientes, sin trazas extendidas ni apilamiento espacial. Validez: ilustrativa.
Tolerancia: todos los impactos con <= 2 por pixel se detectan; coincidencias observadas dentro de 4 sigma de Poisson de la esperada.
"""
from __future__ import annotations
import math, platform, random, sys

W = 100
N = W * W
K = 5
P = 0.01

def med(v):
    v = sorted(v); n = len(v)
    return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    frames, hits = [], []
    for _ in range(K):
        f, h = [], set()
        for i in range(N):
            x = rng.gauss(100, 5)
            if rng.random() < P:
                x += 500
                h.add(i)
            f.append(x)
        frames.append(f)
        hits.append(h)
    cuenta = [sum(1 for h in hits if i in h) for i in range(N)]
    n_imp = sum(cuenta)
    esp_imp = N * K * P
    print(f"impactos inyectados: {n_imp} (esperados {esp_imp:.0f})")
    mediana = [med([f[i] for f in frames]) for i in range(N)]
    res = [frames[k][i] - mediana[i] for k in range(K) for i in range(N)]
    sig = 1.4826 * med([abs(r) for r in res])
    print(f"sigma robusta de los residuos: {sig:.3f} e- (ruido del cuadro 5.000; los residuos respecto de la mediana son menores porque la mediana sigue al propio cuadro)")
    marc = {(k, i) for k in range(K) for i in range(N) if frames[k][i] - mediana[i] > 7 * sig}
    verd = {(k, i) for k in range(K) for i in hits[k]}
    # impactos en pixeles con <= 2 impactos
    ok = {(k, i) for (k, i) in verd if cuenta[i] <= 2}
    det = len(ok & marc)
    fp = len(marc - verd)
    print(f"impactos en pixeles con <= 2 impactos: {len(ok)} ; detectados {det} ; falsos positivos {fp}")
    assert det == len(ok) and fp <= 2
    c2 = sum(1 for c in cuenta if c >= 2)
    c3 = sum(1 for c in cuenta if c >= 3)
    p2 = N * (1 - (1 - P) ** K - K * P * (1 - P) ** (K - 1))
    print(f"pixeles con >= 2 impactos: observados {c2}, esperados {p2:.2f} ; con >= 3: observados {c3}")
    assert abs(c2 - p2) < 4 * math.sqrt(p2)
    # contaminacion de la media frente a la mediana en el apilado
    media_pila = sum(sum(f[i] for f in frames) / K for i in range(N)) / N
    med_pila = sum(mediana) / N
    print(f"nivel apilado: media {media_pila:.3f} e- (sesgo +{media_pila-100:.3f}; esperado +{500*P:.1f}) ; mediana {med_pila:.3f} e-")
    assert abs((media_pila - 100) - 500 * P) < 0.5 and abs(med_pila - 100) < 0.4
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
