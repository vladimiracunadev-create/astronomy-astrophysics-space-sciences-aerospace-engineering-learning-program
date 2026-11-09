#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C01: profundidad, duracion y curva de luz de un transito planetario.

Datos: G (NIST CODATA 2022), R_sol = 6.957e8 m, R_J(ecuatorial) = 7.1492e7 m, R_E(ecuatorial) = 6.3781e6 m y GM_sol (IAU 2015 B3), 1 au (IERS TN36),
consultados 2026-11-09. Contexto: TESS vigila al menos 200 000 enanas de la secuencia principal con I = 4-13 (arXiv:1406.0151, resumen).
Los coeficientes de oscurecimiento al limbo (u1 = 0.40, u2 = 0.26) y los parametros de impacto son ILUSTRATIVOS (sinteticos).
Modelo: profundidad (Rp/Rs)^2; duracion T14 = (P/pi) asin[(Rs/a) sqrt((1+k)^2 - b^2)/sen i]; orbita circular. Comprobacion independiente:
la duracion se obtiene tambien numericamente buscando por biseccion los contactos z(t) = 1 + k, con z = (a/Rs) sqrt(sen^2(phi) + cos^2 i cos^2(phi)).
Fraccion ocultada de un disco uniforme: area de interseccion de dos circulos (analitica) frente a integracion numerica sobre la rejilla;
con oscurecimiento al limbo cuadratico I(r) ~ 1 - u1(1 - mu) - u2(1 - mu)^2, mu = sqrt(1 - r^2): flujo por integracion en coronas.
Supuestos: orbita circular, estrella esferica, planeta opaco y oscuro. Validez: k pequeno.
Tolerancia: 1e-9 entre la duracion analitica y la numerica; 1e-4 entre el area de interseccion analitica y numerica; 2 % entre la profundidad numerica con
oscurecimiento y k^2 I(0)/<I>.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL, R_SOL, R_JUP, R_EAR = 1.3271244e20, 6.957e8, 7.1492e7, 6.3781e6
AU = 1.49597870700e11
DIA = 86400.0
U1, U2 = 0.40, 0.26


def semieje(p_s, gm):
    return (gm * (p_s / (2 * math.pi)) ** 2) ** (1 / 3)


def t14_formula(p, a, rs, k, b):
    inc = math.acos(b * rs / a)
    return p / math.pi * math.asin(rs / a * math.sqrt((1 + k) ** 2 - b * b) / math.sin(inc))


def t14_numerica(p, a, rs, k, b):
    inc = math.acos(b * rs / a)
    z = lambda t: a / rs * math.sqrt(math.sin(2 * math.pi * t / p) ** 2 + (math.cos(inc) * math.cos(2 * math.pi * t / p)) ** 2)
    lo, hi = 0.0, p / 4          # z(0) < 1+k (centro), z(p/4) = a/rs * 1 > 1+k
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if z(mid) < 1 + k:
            lo = mid
        else:
            hi = mid
    return 2 * 0.5 * (lo + hi)


def area_interseccion(d, r1, r2):
    """Area de interseccion de dos circulos de radios r1, r2 con centros a distancia d."""
    if d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a1 = r1 * r1 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    a2 = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    tri = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    return a1 + a2 - tri


def area_numerica(d, r1, r2, n=1500):
    h = 2 * r1 / n
    s = 0
    for i in range(n):
        x = -r1 + (i + 0.5) * h
        for j in range(n):
            y = -r1 + (j + 0.5) * h
            if x * x + y * y <= r1 * r1 and (x - d) ** 2 + y * y <= r2 * r2:
                s += 1
    return s * h * h


def intensidad(r):
    mu = math.sqrt(max(0.0, 1 - r * r))
    return 1 - U1 * (1 - mu) - U2 * (1 - mu) ** 2


def flujo_oscurecido(z, k, n=3000):
    """Flujo normalizado con oscurecimiento al limbo: 1 - (flujo ocultado)/(flujo total), por coronas de radio r.
    Fraccion de la corona cubierta por el disco planetario (radio k, a distancia z del centro): acos(c)/pi con c = (r^2 + z^2 - k^2)/(2 r z)."""
    h = 1.0 / n
    tot = ocu = 0.0
    for i in range(n):
        r = (i + 0.5) * h
        w = intensidad(r) * 2 * math.pi * r * h
        tot += w
        if z == 0.0:
            f = 1.0 if r < k else 0.0
        else:
            c = (r * r + z * z - k * k) / (2 * r * z)
            f = 0.0 if c >= 1.0 else (1.0 if c <= -1.0 else math.acos(c) / math.pi)
        ocu += w * f
    return 1 - ocu / tot


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'planeta':<10} {'k = Rp/Rs':>10} {'profundidad':>12} {'P [d]':>9} {'a [au]':>8} {'T14 [h]':>9} {'T14 numerica [h]':>17}")
    casos = (("Tierra", R_EAR, 365.25 * DIA), ("Jupiter", R_JUP, 4332.59 * DIA))
    for nombre, rp, p in casos:
        k = rp / R_SOL
        a = semieje(p, GM_SOL)
        tf, tn = t14_formula(p, a, R_SOL, k, 0.0), t14_numerica(p, a, R_SOL, k, 0.0)
        assert abs(tf / tn - 1) < 1e-9, "T14 analitico frente a numerico"
        print(f"{nombre:<10} {k:10.5f} {k * k:12.4e} {p / DIA:9.2f} {a / AU:8.4f} {tf / 3600:9.4f} {tn / 3600:17.4f}")
    # dependencia con el parametro de impacto (Jupiter)
    p = 4332.59 * DIA
    a = semieje(p, GM_SOL)
    k = R_JUP / R_SOL
    print(f"{'b':>5} {'T14 [h]':>9}")
    for b in (0.0, 0.3, 0.6, 0.9):
        tf = t14_formula(p, a, R_SOL, k, b)
        tn = t14_numerica(p, a, R_SOL, k, b)
        assert abs(tf / tn - 1) < 1e-9
        print(f"{b:5.1f} {tf / 3600:9.4f}")
    # area de interseccion analitica frente a numerica
    r1, r2 = 1.0, 0.3
    for d in (0.0, 0.5, 0.9, 1.1, 1.3):
        an, nu = area_interseccion(d, r1, r2), area_numerica(d, r1, r2)
        assert abs(an - nu) < 1e-4, f"interseccion d={d}"
        print(f"d = {d:3.1f}: area de interseccion analitica = {an:.6f} ; numerica = {nu:.6f}")
    # oscurecimiento al limbo: profundidad en el centro
    k = 0.1
    f0 = flujo_oscurecido(0.0, k)
    prom = 1 - U1 / 3 - U2 / 6
    esp = k * k * 1.0 / prom
    prof = 1 - f0
    print(f"k = {k}: profundidad con oscurecimiento al limbo = {prof:.6f} ; k^2 I(0)/<I> = {esp:.6f} ; sin oscurecimiento k^2 = {k * k:.6f}")
    assert abs(prof / esp - 1) < 0.02, "profundidad con oscurecimiento"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
