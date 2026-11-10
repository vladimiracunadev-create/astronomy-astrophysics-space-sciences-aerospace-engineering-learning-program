#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C18: eclipse cilindrico, angulo beta y fase solar en una aproximacion V-bar.

Datos CONSULTADOS (2026-11-10): radio ecuatorial terrestre 6378.137 km (NASA/NSSDC) y radio medio lunar 1737.4 km (JPL, IAU 2015).
ILUSTRATIVOS (sinteticos): altitudes de 400 km (Tierra) y 100 km (Luna); angulos beta de 0, 30, 60 y 70 grados; umbral de fase "con contraluz" 120 grados
y "buena luz" 90 grados (hipotesis del autor, no un requisito de sensor consultado).
Modelo: sombra cilindrica (sin penumbra ni refraccion), Sol a distancia infinita con direccion s = (cos beta, 0, sin beta), orbita circular en el plano xy.
Eclipse: dentro si r.s < 0 y la distancia al eje < R. Formula: f = acos( sqrt(h^2 + 2 R h) / ((R+h) cos beta) ) / pi para |beta| < asin(R/(R+h)).
Aproximacion V-bar: perseguidor detras del objetivo (direccion objetivo->perseguidor = -y); cos(fase) = cos(beta) sin(n t).
Tolerancias: fraccion numerica (1e6 pasos) frente a formula < 1e-5.
"""
from __future__ import annotations
import math, os, platform, sys

R_T, R_L = 6378.137, 1737.4


def frac_formula(r, h, beta):
    b = math.radians(beta)
    if abs(math.sin(b)) >= r / (r + h):
        return 0.0
    return math.acos(math.sqrt(h * h + 2 * r * h) / ((r + h) * math.cos(b))) / math.pi


def frac_numerica(r, h, beta, n=1_000_000):
    b = math.radians(beta)
    s = (math.cos(b), 0.0, math.sin(b))
    a = r + h
    k = 0
    for i in range(n):
        th = 2 * math.pi * (i + 0.5) / n
        p = (a * math.cos(th), a * math.sin(th), 0.0)
        d = p[0] * s[0] + p[2] * s[2]
        if d < 0:
            perp2 = a * a - d * d
            if perp2 < r * r:
                k += 1
    return k / n


def ventanas(beta, h=400.0, r=R_T, n=3600):
    b = math.radians(beta)
    ok = sol = bien = 0
    for i in range(n):
        th = 2 * math.pi * (i + 0.5) / n
        a = r + h
        p = (a * math.cos(th), a * math.sin(th), 0.0)
        s = (math.cos(b), 0.0, math.sin(b))
        d = p[0] * s[0] + p[2] * s[2]
        sombra = d < 0 and (a * a - d * d) < r * r
        fase = math.degrees(math.acos(max(-1.0, min(1.0, math.cos(b) * math.sin(th)))))
        if not sombra:
            sol += 1
            if fase <= 90:
                bien += 1
            if fase <= 120:
                ok += 1
    return sol / n, ok / n, bien / n


def calcular():
    filas = []
    for beta in (0.0, 30.0, 60.0, 70.0):
        filas.append(dict(beta=beta, tierra=(frac_formula(R_T, 400.0, beta), frac_numerica(R_T, 400.0, beta, 200000)),
                          luna=(frac_formula(R_L, 100.0, beta), frac_numerica(R_L, 100.0, beta, 200000)),
                          vent=ventanas(beta)))
    p = 2 * math.pi * math.sqrt((R_T + 400.0) ** 3 / 398600.435507) / 60
    pl = 2 * math.pi * math.sqrt((R_L + 100.0) ** 3 / 4902.800118) / 60
    return dict(filas=filas, beta_crit_t=math.degrees(math.asin(R_T / (R_T + 400.0))),
                beta_crit_l=math.degrees(math.asin(R_L / (R_L + 100.0))), p=p, pl=pl)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Periodos circulares: Tierra 400 km = {r['p']:.2f} min ; Luna 100 km = {r['pl']:.2f} min")
    print(f"Beta critico (sin eclipse): Tierra 400 km = {r['beta_crit_t']:.2f} grados ; Luna 100 km = {r['beta_crit_l']:.2f} grados")
    print(" beta   eclipse Tierra (formula / numerico)   eclipse Luna (formula / numerico)   al sol   fase<=120   fase<=90")
    for q in r['filas']:
        print(f"{q['beta']:4.0f}   {q['tierra'][0]:8.5f} / {q['tierra'][1]:8.5f}              {q['luna'][0]:8.5f} / {q['luna'][1]:8.5f}              "
              f"{q['vent'][0]:6.3f}   {q['vent'][1]:8.3f}   {q['vent'][2]:8.3f}")
    for q in r['filas']:
        assert abs(q['tierra'][0] - q['tierra'][1]) < 1e-5 and abs(q['luna'][0] - q['luna'][1]) < 1e-5
    assert abs(r['filas'][0]['vent'][0] - (1 - r['filas'][0]['tierra'][0])) < 2e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
