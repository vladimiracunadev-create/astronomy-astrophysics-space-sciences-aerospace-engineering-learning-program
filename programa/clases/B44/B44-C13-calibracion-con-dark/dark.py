#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C13: cuadro maestro de dark y reescalado por tiempo de exposicion.

Datos: ninguna constante fisica. Tasa oscura media (0,05 e-/s/pix con dispersion log-normal y 3 pixeles calientes), bias (500 e-), ruido de lectura (5 e-), exposiciones de 60 s y 300 s
y cuadros de 32 x 32 pixeles son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: dark = bias + tasa t + ruido (Poisson aproximado por gaussiano + lectura). Maestro de dark = media de 9 cuadros menos el bias maestro; reescalado: D(300) = D(60) 300/60.
Se compara con un maestro medido directamente a 300 s. Semilla 20261109.
Supuestos: corriente oscura lineal con t; bias estable. Validez: ilustrativa.
Tolerancia: tasa escalada frente a la medida a 300 s dentro de 3 sigma en cada pixel normal; diferencia media dentro de 4 errores estandar.
"""
from __future__ import annotations
import math, platform, random, sys

W = 32
N = W * W

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    rn, b0 = 5.0, 500.0
    tasa = [0.05 * math.exp(rng.gauss(0, 0.3)) for _ in range(N)]
    calientes = (100, 400, 777)
    for i in calientes:
        tasa[i] = 2.0
    def cuadro(t):
        return [b0 + rng.gauss(tasa[i] * t, math.sqrt(tasa[i] * t)) + rng.gauss(0, rn) for i in range(N)]
    nf = 9
    bf = [cuadro(0.0) for _ in range(25)]
    bias = [sum(c[i] for c in bf) / 25 for i in range(N)]
    def maestro(t, k=nf):
        cs = [cuadro(t) for _ in range(k)]
        return [sum(c[i] for c in cs) / k - bias[i] for i in range(N)]
    d60 = maestro(60.0)
    d300 = maestro(300.0)
    esc = [d * 5.0 for d in d60]
    normales = [i for i in range(N) if i not in calientes]
    dif = [esc[i] - d300[i] for i in normales]
    md = sum(dif) / len(dif)
    print(f"tasa media verdadera (pixeles normales) {sum(tasa[i] for i in normales)/len(normales):.4f} e-/s ; a 60 s: {sum(d60[i] for i in normales)/len(normales)/60:.4f} ; a 300 s: {sum(d300[i] for i in normales)/len(normales)/300:.4f}")
    print(f"diferencia media (escalado - directo a 300 s): {md:+.3f} e- por pixel")
    a_ = lambda i, t: (tasa[i] * t + rn ** 2) / nf
    sd = [math.sqrt(25 * a_(i, 60) + a_(i, 300) + 16 * rn ** 2 / 25) for i in normales]
    err_med = math.sqrt(sum(x * x for x in sd) / len(sd) / len(sd))
    print(f"error estandar esperado de la diferencia media: {err_med:.3f} e- ; ruido por pixel de la diferencia: {sum(sd)/len(sd):.2f} e-")
    assert abs(md) < 4 * err_med
    dentro = sum(1 for d, s in zip(dif, sd) if abs(d) < 3 * s)
    print(f"pixeles normales dentro de 3 sigma: {dentro}/{len(normales)}")
    assert dentro / len(normales) > 0.99
    for i in calientes:
        print(f"pixel caliente {i}: tasa verdadera 2.000 ; medida a 300 s {d300[i]/300:.3f} e-/s")
        assert abs(d300[i] / 300 / 2.0 - 1) < 0.05
    # ruido del dark maestro de 9 cuadros a 300 s en un pixel normal tipico
    i0 = normales[0]
    print(f"pixel tipico: tasa {tasa[i0]:.4f} e-/s -> dark(300 s) {d300[i0]:.2f} e-")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
