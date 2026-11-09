#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C14: centroide de una subapertura Shack-Hartmann, linealidad y ruido de fotones y de lectura.

Datos: mancha gaussiana de sigma = 0,85 pixeles (FWHM 2,0 px), ventana de 8 x 8 pixeles, ruido de lectura de 3 e- rms, escala de 0,5 arcsec/pixel y subapertura de 0,20 m son ILUSTRATIVOS.
Semilla 20261109. Ningun dato de un sensor real.
Modelo: los N fotones llegan en posiciones gaussianas alrededor de la posicion verdadera (desplazada por la inclinacion local del frente de onda), se asignan a pixeles de 1 px y se estima el
centroide c = sum(x I)/sum(I). Teoria de primer orden: var(c) = (sigma^2 + 1/12)/N (fotones, con el termino de cuantizacion de Sheppard) + sigma_r^2 sum (x - c)^2 / N^2 (lectura).
La pendiente local del frente de onda es alpha = c * escala (rad), y el desplazamiento de la fase a traves de la subapertura es alpha * d.
Supuestos: mancha gaussiana (no Airy), sin umbral ni ponderacion, sin fondo de cielo. Validez: conceptual; los sensores reales usan centroides ponderados, correlacion o pirámide.
Tolerancia: dispersion Monte Carlo frente a la teoria a 8 % ; ganancia lineal 1 hasta 1 px de desplazamiento a 2 %.
"""
from __future__ import annotations
import math, platform, random

SIG = 0.85
W = 8
ARCSEC = 206264.806247
ESC = 0.5          # arcsec por pixel
D_SUB = 0.20       # m

def centroide(rnd, mu_x, mu_y, n, lectura):
    img = [[0.0] * W for _ in range(W)]
    for _ in range(n):
        x = rnd.gauss(mu_x, SIG) + W / 2
        y = rnd.gauss(mu_y, SIG) + W / 2
        i, j = int(math.floor(y)), int(math.floor(x))
        if 0 <= i < W and 0 <= j < W:
            img[i][j] += 1
    if lectura:
        for i in range(W):
            for j in range(W):
                img[i][j] += rnd.gauss(0, lectura)
    s = sum(sum(r) for r in img)
    cx = sum((j + 0.5 - W / 2) * img[i][j] for i in range(W) for j in range(W)) / s
    cy = sum((i + 0.5 - W / 2) * img[i][j] for i in range(W) for j in range(W)) / s
    return cx, cy

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    # linealidad con muchos fotones (casi sin ruido)
    print(f"{'desplazamiento [px]':>20} {'centroide [px]':>15} {'ganancia':>9}")
    gan = {}
    for d in (0.1, 0.25, 0.5, 1.0, 2.0, 3.0):
        cs = [centroide(rnd, d, 0.0, 20000, 0.0)[0] for _ in range(5)]
        c = sum(cs) / len(cs)
        gan[d] = c / d
        print(f"{d:20.2f} {c:15.4f} {c / d:9.4f}")
    assert all(abs(gan[d] - 1) < 0.02 for d in (0.1, 0.25, 0.5, 1.0)), gan
    assert gan[3.0] < 0.99     # la ventana recorta y comprime la respuesta lejos del centro
    # ruido
    suma_cuad = sum((k + 0.5 - W / 2) ** 2 for k in range(W)) * W    # sum (x - c)^2 en la ventana con c = 0
    print(f"{'N fotones':>10} {'sigma lectura':>14} {'sigma MC [px]':>14} {'sigma teoria [px]':>18} {'cociente':>9}")
    nmc = 2500
    for n, sr in ((100, 0.0), (400, 0.0), (1600, 0.0), (400, 3.0), (1600, 3.0)):
        v = [centroide(rnd, 0.0, 0.0, n, sr)[0] for _ in range(nmc)]
        m = sum(v) / nmc
        sd = math.sqrt(sum((a - m) ** 2 for a in v) / (nmc - 1))
        teo = math.sqrt((SIG ** 2 + 1 / 12) / n + sr ** 2 * suma_cuad / n ** 2)
        print(f"{n:10d} {sr:14.1f} {sd:14.4f} {teo:18.4f} {sd / teo:9.3f}")
        assert abs(sd / teo - 1) < 0.08, (n, sr, sd, teo)
    # conversion a pendiente y a diferencia de camino
    c_px = 0.05
    alpha = c_px * ESC / ARCSEC
    print(f"un centroide de {c_px} px = {c_px * ESC:.3f} arcsec = {alpha:.3e} rad de pendiente ; sobre {D_SUB} m eso es {alpha * D_SUB * 1e9:.2f} nm de diferencia de camino entre bordes de la subapertura")
    assert abs(alpha * D_SUB * 1e9 - 24.2) < 0.2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
