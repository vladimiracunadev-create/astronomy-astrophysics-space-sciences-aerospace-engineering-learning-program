#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C17: escala de placa, disco de Airy y muestreo de Nyquist.

Datos: ninguna constante fisica medida; se usa la definicion de segundo de arco (648000/pi segundos de arco por radian, exacta). Apertura de 0,5 m, focal de 4000 mm, pixeles de 9 um,
longitud de onda de 550 nm y seeing de 1,5 segundos de arco son ILUSTRATIVOS (sinteticos); no describen un telescopio real.
Modelo: escala = 206264.806 * p / f [arcsec/pix]; FWHM del disco de Airy = 1,029 lambda/D (aproximacion estandar; aqui se comprueba numericamente con la funcion de Bessel J1 calculada por serie);
muestreo: FWHM/pixel; centroide de una gaussiana submuestreada frente a bien muestreada (simulacion con semilla 20261109) y ensanchamiento del segundo momento por el tamano del pixel, sigma_med^2 = sigma^2 + 1/12.
Supuestos: PSF gaussiana de FWHM dado; ruido de fotones gaussiano. Validez: ilustrativa.
Tolerancia: sigma medida por momentos frente a sqrt(sigma^2 + 1/12) dentro de 1 %; FWHM de Airy numerico frente a 1,029 lambda/D dentro de 0,5 %; escala por dos vias a 1e-9.
"""
from __future__ import annotations
import math, platform, random, sys

ARC = 648000.0 / math.pi

def j1(x):
    s, term, k = 0.0, x / 2, 0
    while abs(term) > 1e-17 or k < 5:
        s += term
        k += 1
        term *= -(x / 2) ** 2 / (k * (k + 1))
        if k > 200:
            break
    return s

def airy(x):
    return 1.0 if x == 0 else (2 * j1(x) / x) ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, F, p, lam, seeing = 0.5, 4.0, 9e-6, 550e-9, 1.5
    escala = ARC * p / F
    escala2 = math.degrees(math.atan(p / F)) * 3600
    print(f"escala de placa: {escala:.5f} arcsec/pix (definicion) ; {escala2:.5f} (atan) ")
    assert abs(escala - escala2) / escala < 1e-8
    # FWHM del disco de Airy: x = pi D theta / lambda ; I(x) = (2 J1/x)^2 = 0.5
    lo, hi = 0.5, 3.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if airy(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    fw_x = 2 * lo
    fw_rad = fw_x * lam / (math.pi * D)
    print(f"FWHM de Airy: numerico {fw_rad*ARC:.5f} arcsec ; 1.029 lambda/D = {1.029*lam/D*ARC:.5f} arcsec")
    assert abs(fw_rad / (1.029 * lam / D) - 1) < 0.005
    print(f"{'seeing [arcsec]':>16} {'FWHM [pix]':>11} {'muestreo':>10}")
    for s in (0.6, 1.5, 3.0, 6.0):
        r = s / escala
        print(f"{s:16.1f} {r:11.2f} {'sub-Nyquist' if r < 2 else 'adecuado':>10}")
    # centroide: perfil 1D de 15 pixeles de una PSF gaussiana de FWHM f (pix), 20000 fotones, centro verdadero 7,3 (fuera del centro del pixel)
    rng = random.Random(20261109)
    print(f"{'FWHM [pix]':>11} {'sesgo x [pix]':>14} {'error rms [pix]':>16} {'sigma med/ver':>14} {'analitico':>10}")
    res = {}
    for fw in (1.0, 2.0, 3.0):
        sg = fw / 2.3548200450309493
        cx = 7.3
        ests = []
        for _ in range(300):
            w = [math.erf((x + 0.5 - cx) / (sg * math.sqrt(2))) - math.erf((x - 0.5 - cx) / (sg * math.sqrt(2))) for x in range(15)]
            tot = sx = 0.0
            for x in range(15):
                v = 10000 * w[x]          # 20 000 fotones: la mitad del integral erf es 2
                v = max(0.0, v + rng.gauss(0, math.sqrt(max(v, 1.0) + 25)))
                tot += v
                sx += v * x
            ests.append(sx / tot)
        m = sum(ests) / len(ests)
        rms = math.sqrt(sum((e - cx) ** 2 for e in ests) / len(ests))
        # segundo momento del perfil integrado por pixel (sin ruido): sigma^2 + 1/12
        # promediado sobre 100 fases de subpixel (el efecto 1/12 es el promedio sobre la fase)
        m2 = 0.0
        for k in range(100):
            c = 7.0 + k / 100
            ww = [math.erf((x + 0.5 - c) / (sg * math.sqrt(2))) - math.erf((x - 0.5 - c) / (sg * math.sqrt(2))) for x in range(15)]
            m2 += sum(ww[x] * (x - c) ** 2 for x in range(15)) / sum(ww) / 100
        rel = math.sqrt(m2) / sg
        an = math.sqrt(1 + 1 / (12 * sg * sg))
        res[fw] = (m - cx, rms, rel, an)
        print(f"{fw:11.1f} {m-cx:14.4f} {rms:16.4f} {rel:14.4f} {an:10.4f}")
        assert abs(rel / an - 1) < 0.01
    assert res[3.0][1] < 0.05 and res[1.0][2] > 1.15 and res[3.0][2] < 1.03
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
