#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C02: ecuacion del CCD, apertura optima y error de una curva de luz fotometrica.

Datos: ninguna constante fisica. Contexto: TESS usa cuatro camaras CCD de campo amplio para vigilar estrellas brillantes
(arXiv:1406.0151, resumen, consultado 2026-11-09). El flujo de la estrella (50 000 e-), el cielo (20 e-/pixel), el ruido de lectura
(10 e-/pixel), la corriente de oscuridad (despreciable) y la anchura de la PSF (sigma = 1.5 pixeles) son ILUSTRATIVOS (sinteticos).
Modelo: PSF gaussiana circular; fraccion de la estrella dentro de una apertura de radio r: 1 - exp(-r^2/(2 sigma^2)); n_pix = pi r^2;
SNR = N*/sqrt(N* + n_pix (N_cielo + N_lect^2)) con N* = F f(r); error en magnitud sigma_m = 1.0857/SNR. Se busca la apertura optima
(razon aurea) y se verifica por Monte Carlo (semilla fija) que la desviacion de la fotometria simulada coincide con N*/SNR.
Supuestos: ruido de Poisson + lectura, cielo uniforme y conocido, sin ruido de centrado. Validez: ilustrativa.
Tolerancia: 3 % entre la desviacion Monte Carlo y la prediccion; 1e-6 en la posicion del maximo.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

F_STAR, SKY, READ, SIGMA = 50000.0, 20.0, 10.0, 1.5


def fraccion(r):
    return 1 - math.exp(-r * r / (2 * SIGMA ** 2))


def snr(r, f=F_STAR):
    n_star = f * fraccion(r)
    npix = math.pi * r * r
    return n_star / math.sqrt(n_star + npix * (SKY + READ ** 2))


def maximo(f, a, b):
    g = (math.sqrt(5) - 1) / 2
    c_, d_ = b - g * (b - a), a + g * (b - a)
    for _ in range(300):
        if f(c_) > f(d_):
            b = d_
        else:
            a = c_
        c_, d_ = b - g * (b - a), a + g * (b - a)
    return 0.5 * (a + b)


def gauss_pois(lam, rng):
    return max(0.0, rng.gauss(lam, math.sqrt(lam)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'r [pix]':>8} {'fraccion':>9} {'n_pix':>8} {'SNR':>8} {'sigma_m [mmag]':>15}")
    for r in (1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 10.0):
        s = snr(r)
        print(f"{r:8.1f} {fraccion(r):9.4f} {math.pi * r * r:8.1f} {s:8.2f} {1085.7 / s:15.3f}")
    r_opt = maximo(snr, 0.5, 15.0)
    print(f"apertura optima = {r_opt:.4f} pix = {r_opt / SIGMA:.3f} sigma ; SNR maximo = {snr(r_opt):.3f} ; sigma_m = {1085.7 / snr(r_opt):.3f} mmag")
    # escalas: fuente brillante (dominada por ruido de Poisson) y debil (dominada por cielo y lectura)
    for f in (5e6, 5e4, 500.0):
        ro = maximo(lambda r: snr(r, f), 0.5, 15.0)
        print(f"flujo {f:9.0f} e-: apertura optima = {ro:5.2f} pix ; SNR = {snr(ro, f):9.2f}")
    # Monte Carlo en la apertura optima
    rng = random.Random(20261109)
    r = r_opt
    n_star = F_STAR * fraccion(r)
    npix = math.pi * r * r
    medidas = []
    for _ in range(20000):
        s = gauss_pois(n_star, rng)
        fondo = gauss_pois(npix * SKY, rng) + rng.gauss(0, READ * math.sqrt(npix))
        medidas.append(s + fondo - npix * SKY)          # se resta el cielo conocido
    esp_media, esp_desv = n_star, n_star / snr(r)
    media, desv = statistics.mean(medidas), statistics.pstdev(medidas)
    print(f"Monte Carlo (20000): flujo medio = {media:.1f} (esperado {esp_media:.1f}) ; desviacion = {desv:.2f} (esperada {esp_desv:.2f})")
    assert abs(desv / esp_desv - 1) < 0.03, "desviacion de la fotometria"
    assert abs(media / esp_media - 1) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
