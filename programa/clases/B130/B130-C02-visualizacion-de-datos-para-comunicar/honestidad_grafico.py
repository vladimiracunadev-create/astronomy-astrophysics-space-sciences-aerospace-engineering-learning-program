#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C02: honestidad de un grafico (eje truncado, escala de color, contraste, clases de histograma).

CONSULTADO (2026-11-11): formulas de luminancia relativa y razon de contraste, y umbrales 4.5:1 (texto normal) y 3:1 (texto grande),
de la pagina de comprension del criterio de contraste minimo de WCAG 2.2 (W3C).
SINTETICOS / ILUSTRATIVOS (no medidos, no consultados): los valores 52 y 56 de las barras; la muestra bimodal (semilla 130);
los colores ancla de las dos escalas (una escala 'arcoiris' y una escala 'tipo viridis' aproximada), que son aproximaciones del autor.
Definicion adoptada (LF, no consultada en Tufte): LF = efecto_en_grafico / efecto_en_datos, con efecto = (B - A)/A.
Tolerancias: luminancia y contraste exactos a 1e-12 en los casos blanco/negro (L=1, L=0, razon 21).
"""
from __future__ import annotations
import platform
import random


def lin(c8):
    c = c8 / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminancia(rgb):
    r, g, b = (lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(c1, c2):
    l1, l2 = sorted((luminancia(c1), luminancia(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


ARCOIRIS = ["#0000FF", "#00FFFF", "#00FF00", "#FFFF00", "#FF0000"]  # ILUSTRATIVA
TIPO_VIRIDIS = ["#440154", "#3B528B", "#21908C", "#5DC863", "#FDE725"]  # ILUSTRATIVA, aproximada


def violaciones_monotonia(colores):
    lum = [luminancia(hexrgb(c)) for c in colores]
    return sum(1 for a, b in zip(lum, lum[1:]) if b < a), lum


def lf_eje_truncado(a, b, base):
    """LF de dos barras (A, B) dibujadas con el eje empezando en 'base'."""
    efecto_datos = (b - a) / a
    efecto_grafico = ((b - base) - (a - base)) / (a - base)
    return efecto_grafico / efecto_datos


def maximos_locales(datos, k, lo, hi):
    ancho = (hi - lo) / k
    cuentas = [0] * k
    for x in datos:
        cuentas[min(k - 1, int((x - lo) / ancho))] += 1
    return sum(1 for i in range(1, k - 1) if cuentas[i] > cuentas[i - 1] and cuentas[i] >= cuentas[i + 1] and cuentas[i] > 2), cuentas


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    # 1. Eje truncado (barras ILUSTRATIVAS 52 y 56)
    print("Eje truncado, barras ILUSTRATIVAS 52 y 56:")
    for base in (0, 40, 50):
        lf = lf_eje_truncado(52, 56, base)
        print(f"  eje desde {base:>2}: LF = {lf:6.2f}")
    assert abs(lf_eje_truncado(52, 56, 0) - 1.0) < 1e-12
    assert lf_eje_truncado(52, 56, 50) > 25

    # 2. Luminancia y contraste (WCAG, consultado)
    assert abs(luminancia((255, 255, 255)) - 1.0) < 1e-12 and luminancia((0, 0, 0)) == 0.0
    assert abs(contraste((255, 255, 255), (0, 0, 0)) - 21.0) < 1e-12
    print("Contraste (WCAG 2.2): blanco/negro =", round(contraste((255, 255, 255), (0, 0, 0)), 3))
    pares = {"gris #767676 sobre blanco": ((0x76, 0x76, 0x76), (255, 255, 255)),
             "gris #999999 sobre blanco": ((0x99, 0x99, 0x99), (255, 255, 255)),
             "amarillo #FFFF00 sobre blanco": ((255, 255, 0), (255, 255, 255))}
    for n, (a, b) in pares.items():
        r = contraste(a, b)
        print(f"  {n:<32} {r:6.3f}:1  texto normal (4.5): {'cumple' if r >= 4.5 else 'NO cumple'}  grande (3): {'cumple' if r >= 3 else 'NO cumple'}")

    # 3. Escalas de color
    print("Luminancia relativa a lo largo de cada escala (ancla a ancla):")
    for nombre, esc in (("arcoiris (ILUSTRATIVA)", ARCOIRIS), ("tipo viridis (ILUSTRATIVA)", TIPO_VIRIDIS)):
        v, lum = violaciones_monotonia(esc)
        print(f"  {nombre:<28} " + " ".join(f"{x:.3f}" for x in lum) + f"  -> descensos: {v}")
    assert violaciones_monotonia(TIPO_VIRIDIS)[0] == 0 and violaciones_monotonia(ARCOIRIS)[0] >= 1

    # 4. Clases de un histograma (muestra SINTETICA bimodal, semilla 130)
    rng = random.Random(130)
    datos = [rng.gauss(30, 6) for _ in range(150)] + [rng.gauss(60, 6) for _ in range(150)]
    print("Maximos locales segun el numero de clases (muestra SINTETICA bimodal, n = 300, semilla 130):")
    res = {}
    for k in (2, 12, 60):
        m, _ = maximos_locales(datos, k, 0, 90)
        res[k] = m
        print(f"  {k:>2} clases -> {m} maximos")
    assert res[2] == 0 and res[12] == 2 and res[60] > 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
