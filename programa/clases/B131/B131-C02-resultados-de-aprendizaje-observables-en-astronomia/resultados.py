#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C02: revision de resultados de aprendizaje observables y de su alineacion con actividades y evaluacion.

CONTENIDO EDUCATIVO. Sin datos consultados: las listas de verbos y niveles son una convencion ILUSTRATIVA del curso (inspirada en las taxonomias
de objetivos, que NO se consultaron en una fuente concreta); los diez resultados, las actividades y los items son SINTETICOS.
Niveles (ilustrativos): 1 recordar, 2 comprender, 3 aplicar, 4 analizar, 5 evaluar, 6 crear. Verbos no observables: se rechazan.
Tolerancias: la cobertura se calcula por dos vias (matriz y conjuntos) y deben coincidir exactamente.
"""
from __future__ import annotations
import platform, re

VERBOS = {
    "enumerar": 1, "nombrar": 1, "identificar": 1, "describir": 2, "explicar": 2, "clasificar": 2, "calcular": 3, "medir": 3,
    "aplicar": 3, "comparar": 4, "analizar": 4, "estimar": 3, "justificar": 5, "criticar": 5, "evaluar": 5, "disenar": 6, "construir": 6,
}
NO_OBSERVABLES = {"comprender", "saber", "conocer", "apreciar", "entender", "interiorizar", "familiarizarse"}

# resultados sinteticos: id -> texto
RESULTADOS = {
    "R1": "Calcular la distancia a un asteroide a partir de su paralaje",
    "R2": "Comprender la gravitacion universal",
    "R3": "Explicar por que cambian las estaciones usando la inclinacion del eje",
    "R4": "Identificar las fases de la Luna en un diagrama",
    "R5": "Conocer la historia de la astronomia",
    "R6": "Disenar un experimento para medir el radio de la Tierra",
    "R7": "Comparar la luminosidad de dos estrellas con sus magnitudes",
    "R8": "Justificar la eleccion de una escala para un modelo del Sistema Solar",
    "R9": "Apreciar la belleza del cielo nocturno",
    "R10": "Estimar el periodo de un planeta con una curva de luz",
}
# actividades sinteticas -> resultados que trabajan
ACTIVIDADES = {"A1": ["R1", "R7"], "A2": ["R3", "R4"], "A3": ["R6"], "A4": ["R8"], "A5": ["R10", "R7"]}
# items de evaluacion sinteticos: (resultado, nivel del item)
ITEMS = {"I1": ("R1", 3), "I2": ("R3", 2), "I3": ("R4", 1), "I4": ("R6", 6), "I5": ("R7", 3), "I6": ("R8", 3), "I7": ("R10", 3)}


def verbo_de(texto):
    pal = re.findall(r"[a-z]+", texto.lower().replace("ñ", "n"))
    return pal[0]


def clasificar(texto):
    v = verbo_de(texto.replace("Diseñar", "Disenar").replace("diseñar", "disenar"))
    if v in NO_OBSERVABLES:
        return v, None, "no observable"
    if v in VERBOS:
        return v, VERBOS[v], "observable"
    return v, None, "desconocido"


def cobertura_matriz(ids):
    cols = {r: [0, 0] for r in ids}
    for a, rs in ACTIVIDADES.items():
        for r in rs:
            cols[r][0] += 1
    for _, (r, _) in ITEMS.items():
        cols[r][1] += 1
    return cols


def cobertura_conjuntos(ids):
    act = set(r for rs in ACTIVIDADES.values() for r in rs)
    ev = set(r for r, _ in ITEMS.values())
    return act, ev


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Resultados, actividades e items SINTETICOS; lista de verbos y niveles ILUSTRATIVA; ningun dato consultado.")
    print("id   verbo         nivel  estado           resultado")
    obs = []
    for rid, txt in RESULTADOS.items():
        v, n, est = clasificar(txt)
        if est == "observable":
            obs.append(rid)
        print(f"{rid:4s} {v:13s} {str(n or '-'):5s}  {est:15s}  {txt}")
    print(f"Observables: {len(obs)} de {len(RESULTADOS)} ; a reescribir: " + ", ".join(r for r in RESULTADOS if r not in obs))
    cols = cobertura_matriz(list(RESULTADOS))
    act, ev = cobertura_conjuntos(list(RESULTADOS))
    print("Cobertura (actividades, items) por resultado observable:")
    for r in obs:
        print(f"  {r}: actividades {cols[r][0]} ; items {cols[r][1]}")
    sin_act = [r for r in obs if r not in act]
    sin_ev = [r for r in obs if r not in ev]
    print(f"Observables sin actividad: {sin_act or 'ninguno'} ; sin item: {sin_ev or 'ninguno'}")
    # desajuste de nivel entre resultado e item
    print("Desajuste de nivel (item < resultado):")
    n_des = 0
    for iid, (r, nivel) in ITEMS.items():
        nr = clasificar(RESULTADOS[r])[1]
        if nr is not None and nivel < nr:
            n_des += 1
            print(f"  {iid} mide {r} en nivel {nivel} y el resultado pide {nr}")
    print(f"  total {n_des}")
    # verificacion: dos vias coinciden
    assert {r for r in obs if cols[r][0] > 0} == {r for r in obs if r in act}
    assert {r for r in obs if cols[r][1] > 0} == {r for r in obs if r in ev}
    assert clasificar("Calcular algo")[1] == 3 and clasificar("Saber algo")[2] == "no observable"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
