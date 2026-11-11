#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C11: auditoria de un recurso educativo SINTETICO con criterios criticos y priorizacion.

Criterios: los de las clases C01-C10 de este bloque; los umbrales numericos citados provienen de WCAG 2.2 (consultada 2026-11-11: 1.1.1, 1.2.2, 1.4.1,
1.4.3 con 4.5:1) o son del curso (ILUSTRATIVOS, no consultados). Esta auditoria NO es una evaluacion de conformidad WCAG.
SINTETICO: el recurso («Guia de observacion de las lunas de Jupiter»), los resultados por criterio, el alcance y el esfuerzo son inventados.
Estados: cumple (1.0), parcial (0.5), no cumple (0.0), no evaluado (se EXCLUYE del puntaje y se lista aparte: nunca cuenta como cumplido).
Reglas: puntaje = suma(peso*valor)/suma(peso) sobre lo evaluado; si un criterio CRITICO no cumple, el veredicto es NO CONFORME aunque el puntaje sea alto.
Prioridad = peso * (1 - valor) * personas_afectadas / esfuerzo (todos sinteticos). Segunda via: puntaje recalculado con fracciones exactas.
Tolerancia: 1e-12.
"""
from __future__ import annotations
import platform
from fractions import Fraction

# id, criterio, peso, critico, estado, personas afectadas (SINTETICO, de 100), esfuerzo (horas, SINTETICO)
CRITERIOS = [
    ("C1", "Alternativa no visual de la observacion (C01,C03)", 3, True, "parcial", 12, 6),
    ("C2", "Plan con varias vias de acceso (DUA) (C02)", 2, False, "cumple", 0, 0),
    ("C3", "Documento legible por lector de pantalla (C04)", 3, True, "no cumple", 10, 4),
    ("C4", "Subtitulos y transcripcion del video (C05)", 3, True, "cumple", 0, 0),
    ("C5", "Contraste de texto >= 4.5:1 y color no unico (C06)", 2, True, "parcial", 8, 3),
    ("C6", "Modelo tactil o sonificacion con tabla de datos (C07)", 2, False, "no cumple", 6, 10),
    ("C7", "Lenguaje claro (C08)", 1, False, "parcial", 25, 5),
    ("C8", "Glosario y apoyo en otro idioma (C09)", 1, False, "no evaluado", 0, 0),
    ("C9", "Funciona con baja conectividad (C10)", 2, False, "parcial", 20, 8),
]
VALOR = {"cumple": 1.0, "parcial": 0.5, "no cumple": 0.0}


def puntaje(cs):
    ev = [c for c in cs if c[4] in VALOR]
    return sum(c[2] * VALOR[c[4]] for c in ev) / sum(c[2] for c in ev)


def puntaje_exacto(cs):
    ev = [c for c in cs if c[4] in VALOR]
    return sum(Fraction(c[2]) * Fraction(VALOR[c[4]]).limit_denominator(2) for c in ev) / sum(Fraction(c[2]) for c in ev)


def prioridad(c):
    return c[2] * (1 - VALOR[c[4]]) * c[5] / c[6] if c[4] in VALOR and c[6] else 0.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Recurso y resultados SINTETICOS; criterios del bloque; NO es una evaluacion de conformidad WCAG.")
    p, pe = puntaje(CRITERIOS), puntaje_exacto(CRITERIOS)
    assert abs(p - float(pe)) < 1e-12
    ne = [c[0] for c in CRITERIOS if c[4] == "no evaluado"]
    print(f"Criterios: {len(CRITERIOS)}; evaluados: {len(CRITERIOS) - len(ne)}; no evaluados: {ne} (no cuentan como cumplidos)")
    print(f"Puntaje ponderado sobre lo evaluado: {p*100:.1f} % (exacto {pe})")
    fallan = [c[0] for c in CRITERIOS if c[3] and c[4] != "cumple"]
    veredicto = "NO CONFORME" if fallan else "SIN BLOQUEOS CRITICOS"
    print(f"Criterios criticos que no cumplen del todo: {fallan} -> {veredicto}")
    print("Prioridad de correccion (peso*(1-valor)*afectadas/esfuerzo):")
    orden = sorted((c for c in CRITERIOS if prioridad(c) > 0), key=lambda c: (-prioridad(c), c[0]))
    for c in orden:
        print(f"  {c[0]}  {prioridad(c):6.2f}  {c[4]:9s}  {c[1]}")
    assert veredicto == "NO CONFORME" and orden[0][0] == "C3" and ne == ["C8"]
    # un puntaje alto no compensa un critico: quitar el fallo de C3 y C1 y C5 cambia el veredicto
    mejorado = [(c[0], c[1], c[2], c[3], "cumple" if c[0] in ("C1", "C3", "C5") else c[4], c[5], c[6]) for c in CRITERIOS]
    f2 = [c[0] for c in mejorado if c[3] and c[4] != "cumple"]
    print(f"Tras corregir C1, C3 y C5: puntaje {puntaje(mejorado)*100:.1f} %, criticos pendientes {f2}")
    assert f2 == []
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
