#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C08: metricas simples de claridad antes y despues de reescribir un texto SINTETICO.

Consultado (2026-11-11): digital.gov, «Writing for understanding» (guia de lenguaje claro de EE. UU.): voz activa, tiempo presente,
verbos en vez de sustantivos escondidos, secciones cortas con titulos, listas para elementos paralelos, hablar al lector. La pagina NO fija
limites numericos de frase o parrafo.
ILUSTRATIVOS (del curso, NO consultados): umbral de 25 palabras por frase, lista de jerga, heuristica de voz pasiva en espanol.
SINTETICO: los dos textos (original y reescrito) son inventados y tratan sobre un eclipse; los numeros del texto son inventados.
Unidades: palabras, frases, conteos. Verificacion: el texto reescrito conserva el mismo conjunto de cifras que el original (segunda via: comparacion de conjuntos).
Tolerancia: igualdad exacta. Limite: las metricas no miden comprension; eso exige probar el texto con lectores reales.
"""
from __future__ import annotations
import platform, re

ORIGINAL = ("La realizacion de la observacion del eclipse fue efectuada por los estudiantes durante 3 horas, y los datos fueron "
            "registrados en una planilla en la cual se consignaron la magnitud del oscurecimiento y la elongacion angular, "
            "siendo necesaria la utilizacion de filtros solares certificados para evitar la ocurrencia de danos oculares. "
            "La parallax del Sol es considerada despreciable. Las cifras de 12 % de oscurecimiento fueron obtenidas.")
REESCRITO = ("Los estudiantes observaron el eclipse durante 3 horas. Anotaron en una planilla cuanto se oscurecio el Sol "
             "y la elongacion angular. Usen siempre filtros solares certificados: protegen los ojos. "
             "Puedes ignorar la paralaje del Sol: es muy pequena. El oscurecimiento llego a 12 %.")
JERGA = {"elongacion angular", "parallax", "paralaje", "magnitud del oscurecimiento"}
UMBRAL = 25
PASIVA = re.compile(r"\b(fue|fueron|es|son|siendo)\s+(\w+(ado|ido|ados|idos|ada|adas|ida|idas|ecta|echa))\b", re.I)
NOMINALES = re.compile(r"\b(realizacion|utilizacion|ocurrencia|observacion)\s+de\b", re.I)


def frases(t: str):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()]


def palabras(t: str):
    return re.findall(r"[\wáéíóúñ]+", t.lower())


def cifras(t: str):
    return set(re.findall(r"\d+", t))


def metricas(t: str):
    fs = frases(t)
    lens = [len(palabras(f)) for f in fs]
    return {"frases": len(fs), "palabras": sum(lens), "media": sum(lens) / len(lens), "max": max(lens),
            "largas": sum(1 for x in lens if x > UMBRAL), "pasivas": len(PASIVA.findall(t)),
            "nominalizaciones": len(NOMINALES.findall(t)), "jerga": sum(1 for j in JERGA if j in t.lower())}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Textos SINTETICOS; umbral de 25 palabras y heuristicas ILUSTRATIVOS (la guia consultada no fija numeros).")
    a, b = metricas(ORIGINAL), metricas(REESCRITO)
    print(f"{'metrica':18s} {'original':>9s} {'reescrito':>10s}")
    for k in a:
        va, vb = a[k], b[k]
        fa = f"{va:9.1f}" if isinstance(va, float) else f"{va:9d}"
        fb = f"{vb:10.1f}" if isinstance(vb, float) else f"{vb:10d}"
        print(f"{k:18s} {fa} {fb}")
    ca, cb = cifras(ORIGINAL), cifras(REESCRITO)
    print(f"Cifras conservadas: original {sorted(ca)} | reescrito {sorted(cb)}")
    assert ca == cb, (ca, cb)
    assert b["media"] < a["media"] and b["max"] <= UMBRAL and b["pasivas"] < a["pasivas"] and b["nominalizaciones"] < a["nominalizaciones"]
    assert a["largas"] >= 1 and b["largas"] == 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
