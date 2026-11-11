#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C06: razon de contraste WCAG 2.2 y uso del color.

Consultado (2026-11-11): W3C, WCAG 2.2 «Understanding 1.4.3»: luminancia relativa L = 0.2126 R + 0.7152 G + 0.0722 B con canales
linealizados (c <= 0.04045 -> c/12.92; si no ((c+0.055)/1.055)^2.4); razon = (L1 + 0.05)/(L2 + 0.05), L1 la mas clara; sin redondear;
umbrales 4.5:1 (texto), 3:1 (texto grande: >= 18 pt o 14 pt negrita); 3:1 para componentes graficos (1.4.11); el color no puede ser el unico medio (1.4.1).
SINTETICO: las paletas de ejemplo (modo nocturno y leyenda de una imagen en falso color) son inventadas.
Unidades: razon adimensional (1 a 21). Sistema de color: sRGB, canales de 8 bits.
Verificacion: valores conocidos (negro/blanco = 21; igual/igual = 1; #767676 sobre blanco ~ 4.54; #777777 ~ 4.48) y simetria.
Tolerancia: 0.01 en la razon. Limite: la razon no mide tamano, trazo ni estado del usuario.
"""
from __future__ import annotations
import platform


def lin(c8: int) -> float:
    c = c8 / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexa: str) -> float:
    r, g, b = (int(hexa[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def razon(a: str, b: str) -> float:
    la, lb = lum(a), lum(b)
    l1, l2 = max(la, lb), min(la, lb)
    return (l1 + 0.05) / (l2 + 0.05)


def veredicto_texto(r: float, grande: bool = False) -> str:
    return "pasa" if r >= (3.0 if grande else 4.5) else "NO pasa"


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Formula y umbrales: WCAG 2.2 Understanding 1.4.3 (consultado 2026-11-11). Paletas SINTETICAS.")
    # pruebas de la implementacion
    assert abs(razon("#000000", "#FFFFFF") - 21.0) < 0.01
    assert abs(razon("#336699", "#336699") - 1.0) < 1e-12
    assert abs(razon("#767676", "#FFFFFF") - 4.54) < 0.01 and abs(razon("#777777", "#FFFFFF") - 4.48) < 0.01
    assert razon("#112233", "#EEDDCC") == razon("#EEDDCC", "#112233")
    print("Pruebas de la implementacion superadas (21:1, 1:1, 4.54, 4.48, simetria).")
    pares = [("texto negro sobre blanco", "#000000", "#FFFFFF"), ("gris #767676 sobre blanco", "#767676", "#FFFFFF"),
             ("gris #777777 sobre blanco", "#777777", "#FFFFFF"), ("rojo #FF0000 sobre negro (modo nocturno)", "#FF0000", "#000000"),
             ("rojo oscuro #800000 sobre negro", "#800000", "#000000"), ("azul #0000FF sobre negro", "#0000FF", "#000000"),
             ("amarillo #FFD400 sobre blanco", "#FFD400", "#FFFFFF")]
    print(f"{'par':44s} {'razon':>7s}  texto 4.5  grande 3.0")
    for n, f, g in pares:
        r = razon(f, g)
        print(f"{n:44s} {r:7.2f}  {veredicto_texto(r):8s}  {veredicto_texto(r, True)}")
    # leyenda de imagen en falso color (SINTETICA): series adyacentes y contra el fondo
    leyenda = {"frio": "#1B3A6B", "templado": "#2E8B57", "caliente": "#D95F02"}
    fondo = "#FFFFFF"
    print("Leyenda SINTETICA contra fondo blanco (1.4.11 pide >= 3):")
    for n, c in leyenda.items():
        r = razon(c, fondo)
        print(f"  {n:9s} {c}  razon {r:5.2f}  {'pasa' if r >= 3 else 'NO pasa'}")
    nombres = list(leyenda)
    print("Distincion por luminancia entre series (si es < 1.2 hace falta etiqueta o patron, 1.4.1; umbral del curso):")
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            r = razon(leyenda[nombres[i]], leyenda[nombres[j]])
            print(f"  {nombres[i]:9s} vs {nombres[j]:9s}: {r:5.2f}  {'solo color insuficiente' if r < 1.2 else 'distinguible por luminancia'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
