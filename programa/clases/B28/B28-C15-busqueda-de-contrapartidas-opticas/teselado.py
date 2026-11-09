#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C15: teselado voraz de una region de localizacion y compromiso entre cobertura y profundidad.

Datos: ninguna constante fisica. Contexto: GW170817 se localizo en 31 grados cuadrados y su contrapartida optica se identifico a
~10 arcsec de una galaxia (arXiv:1710.05833 y arXiv:1710.05835, resumenes, consultados 2026-11-09). El mapa de probabilidad
(dos manchas gaussianas de 6 grados), el campo de vision de 4 grados de radio, la magnitud limite de 1 s (16.5 mag), el tiempo total
(3600 s) y el brillo de la fuente (19.5 mag) son ILUSTRATIVOS (sinteticos).
Modelo: rejilla de Fibonacci de N celdas; cada celda tiene una probabilidad; un apuntado cubre las celdas a menos de r_fov de su centro;
algoritmo voraz: en cada paso se elige el centro que suma mas probabilidad aun no cubierta. Garantia teorica del algoritmo voraz para
cobertura: al menos (1 - 1/e) del optimo; se comprueba contra la cota aproximada 'suma de las k m celdas mas probables' (m = numero medio de celdas por apuntado; no es una cota rigurosa). Profundidad
limitada por el fondo: m_lim = m_1s + 1.25 log10(t) (la senal-ruido crece como sqrt(t) y 2.5 log10(sqrt t) = 1.25 log10 t).
Supuestos: mapa conocido, campo circular, un solo filtro. Validez: ilustrativa.
Tolerancia: cobertura voraz >= (1 - 1/e) de la cota superior en cada paso.
"""
from __future__ import annotations
import math
import platform
import sys


def rejilla(n):
    ga = math.pi * (3 - math.sqrt(5))
    pts = []
    for i in range(n):
        z = 1 - (2 * i + 1) / n
        r = math.sqrt(1 - z * z)
        pts.append((r * math.cos(ga * i), r * math.sin(ga * i), z))
    return pts


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vec(ra_deg, dec_deg):
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = 4000
    rej = rejilla(n)
    cel = 4 * math.pi / n * (180 / math.pi) ** 2
    s = math.radians(6.0)
    centros = [(vec(40, 20), 0.7), (vec(220, -35), 0.3)]
    w = []
    for p in rej:
        v = 0.0
        for c, peso in centros:
            ang = math.acos(max(-1.0, min(1.0, dot(p, c))))
            v += peso * math.exp(-0.5 * (ang / s) ** 2)
        w.append(v)
    tot = sum(w)
    w = [x / tot for x in w]
    print(f"rejilla: {n} celdas de {cel:.2f} deg2 ; mapa: dos manchas gaussianas de 6 grados (70 % y 30 %)")
    r_fov = math.radians(4.0)
    cosr = math.cos(r_fov)
    vec_n = []
    for i in range(n):
        vec_n.append([j for j in range(n) if dot(rej[i], rej[j]) >= cosr])
    medio = sum(len(v) for v in vec_n) / n
    print(f"campo de vision de 4 grados de radio: {math.pi * (4.0) ** 2:.1f} deg2 ~ {medio:.1f} celdas por apuntado")
    cubierto = [False] * n
    acum = 0.0
    orden_prob = sorted(w, reverse=True)
    print(f"{'apuntados k':>11} {'prob. acumulada':>16} {'cota aprox.':>14} {'cociente':>9}")
    res = {}
    for k in range(1, 31):
        mejor, mi = -1.0, -1
        for i in range(n):
            g = sum(w[j] for j in vec_n[i] if not cubierto[j])
            if g > mejor:
                mejor, mi = g, i
        for j in vec_n[mi]:
            cubierto[j] = True
        acum += mejor
        ub = sum(orden_prob[:min(n, int(round(k * medio * 1.0)))])
        res[k] = acum
        assert acum >= (1 - 1 / math.e) * min(ub, 1.0) - 1e-12, f"garantia voraz k={k}"
        if k in (1, 2, 3, 5, 10, 20, 30):
            print(f"{k:11d} {acum:16.4f} {min(ub, 1.0):14.4f} {acum / min(ub, 1.0):9.3f}")
    # compromiso cobertura / profundidad
    m1s, t_total, m_fuente = 16.5, 3600.0, 19.5
    print(f"{'k':>4} {'t por campo [s]':>16} {'m_lim [mag]':>12} {'detectable':>11} {'P cob x det':>12}")
    mejor_k, mejor_p = 0, -1.0
    for k in (1, 2, 3, 5, 10, 20, 30):
        t = t_total / k
        ml = m1s + 1.25 * math.log10(t)
        det = ml >= m_fuente
        p = res[k] * (1.0 if det else 0.0)
        if p > mejor_p:
            mejor_p, mejor_k = p, k
        print(f"{k:4d} {t:16.1f} {ml:12.2f} {str(det):>11} {p:12.4f}")
    print(f"mejor plan (fuente de {m_fuente} mag): k = {mejor_k} campos con probabilidad total {mejor_p:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
