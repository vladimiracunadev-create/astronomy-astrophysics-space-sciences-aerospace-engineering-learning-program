#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C05: ruta de exportacion ESQUEMATICA y costo esperado del retraso de una licencia (modelo SINTETICO).

CONTENIDO EDUCATIVO: NO es asesoria legal ni de cumplimiento. La clasificacion real de un articulo la hace un especialista con el texto vigente.
Datos consultados (2026-11-11): 22 CFR 120.1 (Cornell LII; sin fecha de version en la pagina): la Ley de Control de Exportaciones de Armas faculta
al Presidente, delegado en el Departamento de Estado, y la Direccion de Controles del Comercio de Defensa (DDTC) tiene oficinas de licencias,
cumplimiento y politica. 22 CFR 121.1, Categoria XV (extracto leido): cubre componentes y naves «calificados para el espacio» (diseñados,
fabricados o probados para operar sobre 100 km) y los articulos disenados especificamente para una nave no listados en el parrafo (e) quedan
bajo las EAR. Reglamento (UE) 2021/821: regimen unico de control de exportacion, intermediacion, asistencia tecnica, transito y transferencia de
articulos de doble uso; la transferencia electronica de software o tecnologia fuera de la UE cuenta como exportacion; hay autorizaciones
individual, global, general nacional y general de la Union. NINGUNA lista, umbral ni plazo real se uso en el calculo (no consultados).
ILUSTRATIVOS (sinteticos): atributos de 6 articulos y 3 destinos con grupos A/B/C inventados; retraso de licencia ~ exponencial con media 45 dias;
plazo de entrega comprometido T0 = 60 dias; penalizacion por demora 2 000 u.m. por dia; probabilidad de denegacion 8 %.
Unidades: dias, u.m. Tolerancias: costo esperado analitico frente a Monte Carlo (200 000 casos, semilla 125) dentro de 1 %.
"""
from __future__ import annotations
import math, platform, random

ARTICULOS = [
    # nombre, en_lista_control(sintetica), tecnologia_intangible, uso_final_sensible
    ("estrella-sintetica 1", True, False, False),
    ("panel solar generico", False, False, False),
    ("software de actitud", True, True, False),
    ("planos de carga util", True, True, False),
    ("tornillo estandar", False, False, False),
    ("modulo de propulsion", True, False, True),
]
DESTINOS = {"pais-A (socio estrecho)": "A", "pais-B (intermedio)": "B", "pais-C (restringido)": "C"}


def ruta(en_lista, intangible, uso_sensible, grupo):
    """Clasificador ESQUEMATICO: devuelve una etiqueta de ruta; NO es una decision legal."""
    if grupo == "C" and (en_lista or uso_sensible):
        return "consulta especializada: probable denegacion"
    if en_lista or uso_sensible:
        return "licencia probable" + (" (incluye transferencia intangible)" if intangible else "")
    return "sin control aparente (verificar)"


def costo_esperado(media, t0, penal, p_deneg):
    """Retraso T ~ Exp(media): E[max(0, T - T0)] = media * exp(-T0/media). Si hay denegacion no hay entrega (se excluye)."""
    demora_esperada = media * math.exp(-t0 / media)
    return (1.0 - p_deneg) * penal * demora_esperada, demora_esperada


def monte_carlo(media, t0, penal, p_deneg, n, semilla):
    rng = random.Random(semilla)
    tot = 0.0
    for _ in range(n):
        if rng.random() < p_deneg:
            continue
        t = rng.expovariate(1.0 / media)
        tot += penal * max(0.0, t - t0)
    return tot / n


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Articulos, listas y destinos SINTETICOS; NO es una clasificacion real ni asesoria legal.")
    print("articulo               pais-A                                   pais-C")
    for nombre, lista, intang, sens in ARTICULOS:
        ra = ruta(lista, intang, sens, "A")
        rc = ruta(lista, intang, sens, "C")
        print(f"{nombre:22s} {ra:40s} {rc}")
    ce, de = costo_esperado(45.0, 60.0, 2000.0, 0.08)
    mc = monte_carlo(45.0, 60.0, 2000.0, 0.08, 200000, 125)
    assert abs(ce - mc) / ce < 0.01
    print(f"Demora esperada sobre el plazo = {de:.2f} dias ; costo esperado analitico = {ce:.0f} u.m. ; Monte Carlo = {mc:.0f} u.m.")
    print("media del tramite [dias]  plazo T0 [dias]  costo esperado [u.m.]")
    for media in (30.0, 45.0, 90.0):
        for t0 in (60.0, 120.0):
            print(f"{media:23.0f}  {t0:15.0f}  {costo_esperado(media, t0, 2000.0, 0.08)[0]:20.0f}")
    # Probabilidad de incumplir el plazo
    p_inc = (1 - 0.08) * math.exp(-60.0 / 45.0)
    print(f"Probabilidad de entregar fuera de plazo (analitica, sin denegacion) = {math.exp(-60.0/45.0):.3f} ; con denegacion no entrega: {0.08:.2f}")
    assert 0 < p_inc < 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
