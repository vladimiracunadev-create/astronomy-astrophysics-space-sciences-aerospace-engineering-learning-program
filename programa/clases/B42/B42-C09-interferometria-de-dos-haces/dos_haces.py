#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C09: interferometro de Michelson, visibilidad y recuperacion de fase por cuatro pasos.

Datos: ninguna constante fisica. lambda = 632,8 nm, razon de intensidades de los brazos 0,5 y el ruido gaussiano de sigma = 0,01 (en unidades de I0 = 1) son ILUSTRATIVOS; semilla 20261109.
Modelo: I(d) = I1 + I2 + 2 sqrt(I1 I2) cos(2 pi * 2 d / lambda + phi) para un desplazamiento d del espejo (la diferencia de camino es 2 d). La visibilidad es
V = 2 sqrt(I1 I2)/(I1+I2). Fase por cuatro pasos de pi/2: phi = atan2(I4 - I2, I1 - I3). Se contrasta (a) la visibilidad con el contraste medido, (b) el barrido de d con el
periodo lambda/2 de las franjas, (c) la dispersion de phi con la prediccion sigma/(sqrt(2) A) con A = 2 sqrt(I1 I2) la amplitud de modulacion.
Supuestos: fuente monocromatica, sin inclinacion de espejos, ruido aditivo independiente. Validez: ilustrativa de la metrologia de superficies.
Tolerancia: fase sin ruido a 1e-12 ; dispersion de la fase estimada con 20000 repeticiones a 3 % de la prediccion ; periodo de franjas a 1e-9.
"""
from __future__ import annotations
import math, platform, random

LAM = 632.8e-9
I1, I2 = 1.0, 0.5

def inten(d, phi=0.0):
    return I1 + I2 + 2 * math.sqrt(I1 * I2) * math.cos(2 * math.pi * 2 * d / LAM + phi)

def fase4(phi, ruido=0.0, rnd=None):
    # pasos de pi/2: desplazamientos de espejo d = k lambda/8
    s = []
    for k in range(4):
        v = I1 + I2 + 2 * math.sqrt(I1 * I2) * math.cos(phi + k * math.pi / 2)
        if ruido:
            v += rnd.gauss(0, ruido)
        s.append(v)
    return math.atan2(s[3] - s[1], s[0] - s[2])

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    v_teo = 2 * math.sqrt(I1 * I2) / (I1 + I2)
    muestras = [inten(i * LAM / 400.0) for i in range(2000)]
    mx, mn = max(muestras), min(muestras)
    v_med = (mx - mn) / (mx + mn)
    print(f"visibilidad teorica = {v_teo:.6f} ; medida en el barrido = {v_med:.6f} ; Imax = {mx:.4f} ; Imin = {mn:.4f}")
    assert abs(v_med - v_teo) < 1e-4
    # periodo de franjas: dos maximos consecutivos separados lambda/2
    maximos = [i for i in range(1, 1999) if muestras[i] > muestras[i - 1] and muestras[i] >= muestras[i + 1]]
    per = (maximos[1] - maximos[0]) * LAM / 400.0
    print(f"periodo de franjas = {per * 1e9:.2f} nm (lambda/2 = {LAM / 2 * 1e9:.2f} nm)")
    assert abs(per - LAM / 2) / (LAM / 2) < 1e-9 + 1e-12 or abs(per - LAM / 2) < LAM / 400
    # fase sin ruido
    peor = 0.0
    for deg in (-150, -90, -30, 0, 45, 120, 170):
        ph = math.radians(deg)
        peor = max(peor, abs(math.atan2(math.sin(fase4(ph) - ph), math.cos(fase4(ph) - ph))))
    print(f"fase sin ruido: error maximo = {peor:.2e} rad")
    assert peor < 1e-12
    # ruido
    sigma = 0.01
    a_mod = 2 * math.sqrt(I1 * I2)
    teo = sigma / (math.sqrt(2) * a_mod)
    n = 20000
    ph0 = 0.7
    errs = []
    for _ in range(n):
        e = fase4(ph0, sigma, rnd) - ph0
        errs.append(math.atan2(math.sin(e), math.cos(e)))
    m = sum(errs) / n
    sd = math.sqrt(sum((e - m) ** 2 for e in errs) / (n - 1))
    h = 0.5 * LAM / (2 * math.pi) * 1.0
    print(f"ruido sigma = {sigma} : desviacion de la fase = {sd * 1e3:.4f} mrad ; prediccion sigma/(sqrt(2) A) = {teo * 1e3:.4f} mrad ; sesgo = {m * 1e3:+.4f} mrad")
    print(f"en altura de superficie (camino doble): sigma_h = lambda/(4 pi) * sigma_phi = {LAM / (4 * math.pi) * sd * 1e12:.2f} pm")
    assert abs(sd - teo) / teo < 0.03
    # correspondencia fase - desplazamiento
    d = 80e-9
    ph = 2 * math.pi * 2 * d / LAM
    print(f"desplazamiento de {d * 1e9:.0f} nm -> fase {ph:.4f} rad = {ph / (2 * math.pi):.4f} franjas ; lambda/2 = 1 franja")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
