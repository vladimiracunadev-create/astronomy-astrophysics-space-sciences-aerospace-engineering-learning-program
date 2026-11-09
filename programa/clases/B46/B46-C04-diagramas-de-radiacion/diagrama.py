#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C04: diagrama de radiacion de una apertura lineal con distintas iluminaciones.

Datos: ninguno externo. La apertura (D = 20 lambda, 4000 muestras) y las leyes de iluminacion (uniforme, coseno, coseno al cuadrado) son ILUSTRATIVAS.
Modelo: patron de potencia |F(u)|^2 con F(u) = suma de a(x) exp(i 2 pi u x) y u = sin(theta)/(lambda) normalizado a D (u en unidades de lambda/D).
Se mide el ancho a media potencia, el primer lobulo lateral y la eficiencia de apertura (suma a)^2 / (N suma a^2), frente a los valores
analiticos conocidos: sinc -13,26 dB y 0,886 lambda/D para la iluminacion uniforme.
Supuestos: apertura 1D continua discretizada, campo lejano, sin acoplamiento. Validez: orientativa.
Tolerancia: iluminacion uniforme dentro de 0,005 lambda/D en el ancho y 0,05 dB en el lobulo lateral.
"""
from __future__ import annotations
import math, platform

N = 400

def apertura(ley):
    xs = [(i + 0.5) / N - 0.5 for i in range(N)]
    if ley == "uniforme":
        return [1.0] * N
    if ley == "coseno":
        return [math.cos(math.pi * x) for x in xs]
    return [math.cos(math.pi * x) ** 2 for x in xs]

def patron(a, u):
    re = im = 0.0
    for i, ai in enumerate(a):
        x = (i + 0.5) / N - 0.5
        ph = 2 * math.pi * u * x
        re += ai * math.cos(ph)
        im += ai * math.sin(ph)
    return (re * re + im * im)

def analiza(ley):
    a = apertura(ley)
    p0 = patron(a, 0.0)
    pasos = 0.01
    us = [k * pasos for k in range(0, 600)]
    p = [patron(a, u) / p0 for u in us]
    # ancho a media potencia
    for k in range(1, len(us)):
        if p[k] < 0.5:
            u1 = us[k - 1] + (p[k - 1] - 0.5) / (p[k - 1] - p[k]) * pasos
            break
    # primer minimo y maximo posterior
    k = 1
    while not (p[k] < p[k - 1] and p[k] <= p[k + 1]):
        k += 1
    while p[k + 1] >= p[k] or True:
        k += 1
        if p[k] > p[k + 1] and p[k] >= p[k - 1]:
            break
    sll = 10 * math.log10(p[k])
    ef = sum(a) ** 2 / (len(a) * sum(x * x for x in a))
    return dict(hpbw=2 * u1, sll=sll, ef=ef)

def calc():
    return {ley: analiza(ley) for ley in ("uniforme", "coseno", "coseno2")}

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'iluminacion':<11} {'HPBW [lambda/D]':>16} {'1er lobulo [dB]':>16} {'eficiencia':>11}")
    for k, v in r.items():
        print(f"{k:<11} {v['hpbw']:16.3f} {v['sll']:16.2f} {v['ef']:11.3f}")
    u = r["uniforme"]
    assert abs(u["hpbw"] - 0.886) < 0.005
    assert abs(u["sll"] + 13.26) < 0.05
    assert r["coseno"]["sll"] < u["sll"] - 8 and r["coseno2"]["sll"] < r["coseno"]["sll"] - 5
    assert u["hpbw"] < r["coseno"]["hpbw"] < r["coseno2"]["hpbw"]
    assert abs(u["ef"] - 1) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
