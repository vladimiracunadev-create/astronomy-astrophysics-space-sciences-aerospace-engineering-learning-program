#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C07: banco de variantes de transferencia cercana, media y lejana de un problema de la tercera ley de Kepler.

CONTENIDO EDUCATIVO. CONSULTADOS (2026-11-11): IAU 2015 B3 (PDF leido): (GM) solar nominal 1.3271244e20 m3 s-2 y (GM) de Jupiter nominal 1.2668653e17 m3 s-2.
ESTANDAR NO CONSULTADO: 1 UA = 1.495978707e11 m; ano juliano 365.25 d = 3.15576e7 s; semiejes y masas de los cuerpos de los enunciados son
ILUSTRATIVOS (sistemas SINTETICOS; no son datos de ninguna medicion).
Relaciones: P^2 = a^3 / M (P en anos, a en UA, M en masas solares nominales) y, como segunda via, P = 2 pi sqrt(a^3 / GM) en SI.
Tolerancias: ambas vias coinciden dentro de 1e-3 relativo en todas las variantes (la primera ignora la masa del cuerpo menor).
Clasificacion de la transferencia (convencion ILUSTRATIVA del curso, no la taxonomia de la bibliografia): numero de rasgos que cambian
respecto del problema original (cuerpo central, magnitud pedida, contexto y unidades).
"""
from __future__ import annotations
import math, platform, random

GM_SOL, GM_JUP = 1.3271244e20, 1.2668653e17
UA, ANIO = 1.495978707e11, 3.15576e7


def periodo_ua(a_ua, m_sol):
    return math.sqrt(a_ua ** 3 / m_sol)  # anos


def periodo_si(a_m, gm):
    return 2 * math.pi * math.sqrt(a_m ** 3 / gm)  # s


def semieje_ua(p_anos, m_sol):
    return (p_anos ** 2 * m_sol) ** (1 / 3)


def banco(seed=131):
    rng = random.Random(seed)
    items = []
    # original: planeta alrededor del Sol, pedir P
    a = round(rng.uniform(1.5, 6.0), 2)
    items.append(("original", 0, f"Un planeta SINTETICO orbita al Sol con a = {a} UA. Halla P.", ("P", a, 1.0, "sol")))
    # cercana: otro semieje y se pide a partir de P
    p = round(rng.uniform(2.0, 20.0), 1)
    items.append(("cercana", 1, f"Un cuerpo SINTETICO orbita al Sol con P = {p} anos. Halla a.", ("a", p, 1.0, "sol")))
    # media: otra estrella
    m = round(rng.uniform(0.3, 2.0), 2)
    a2 = round(rng.uniform(0.05, 1.0), 2)
    items.append(("media", 2, f"Un planeta SINTETICO orbita una estrella de {m} masas solares con a = {a2} UA. Halla P.", ("P", a2, m, "sol")))
    # lejana: satelite de Jupiter con a en radios jovianos, se pide P en dias
    a3_rj = round(rng.uniform(5.0, 30.0), 1)
    items.append(("lejana", 3, f"Un satelite SINTETICO orbita a Jupiter con a = {a3_rj} radios jovianos nominales. Halla P en dias.", ("Psat", a3_rj, None, "jup")))
    return items


def resolver(clave):
    tipo, x, m, cuerpo = clave
    if tipo == "P":
        return periodo_ua(x, m), "anos", periodo_si(x * UA, GM_SOL * m) / ANIO
    if tipo == "a":
        return semieje_ua(x, m), "UA", ((GM_SOL * (x * ANIO) ** 2 / (4 * math.pi ** 2)) ** (1 / 3)) / UA
    # satelite de Jupiter: solo via SI (la forma en UA y masas solares exige convertir (GM) a masa solar)
    a_m = x * 7.1492e7
    p_dias = periodo_si(a_m, GM_JUP) / 86400
    m_jup_sol = GM_JUP / GM_SOL
    p_ua = periodo_ua(a_m / UA, m_jup_sol) * 365.25
    return p_dias, "dias", p_ua


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("(GM) nominales IAU 2015 B3 CONSULTADOS; UA, ano y valores de los enunciados ESTANDAR/ILUSTRATIVOS; sistemas SINTETICOS.")
    items = banco()
    print("variante   rasgos  enunciado -> respuesta (via 1) ; respuesta (via 2) ; diferencia relativa")
    peor = 0.0
    for nom, rasgos, texto, clave in items:
        v1, u, v2 = resolver(clave)
        dif = abs(v1 - v2) / v1
        peor = max(peor, dif)
        print(f"{nom:9s} {rasgos}  {texto}")
        print(f"          -> {v1:.4g} {u} ; {v2:.4g} {u} ; {dif:.1e}")
    print(f"Mayor diferencia entre vias: {peor:.1e} (tolerancia 1e-3)")
    # prueba: la Tierra con a = 1 UA
    print(f"Comprobacion: a = 1 UA, M = 1 -> P = {periodo_ua(1.0, 1.0):.4f} anos ; por SI = {periodo_si(UA, GM_SOL) / ANIO:.5f} anos")
    # sensibilidad: el exponente 3/2
    print("Si a se duplica, P se multiplica por " + f"{periodo_ua(2.0, 1.0) / periodo_ua(1.0, 1.0):.4f} (2^1.5 = {2 ** 1.5:.4f})")
    assert peor < 1e-3
    assert abs(periodo_ua(1.0, 1.0) - 1.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
