#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C04: secuenciacion conceptual de una unidad como grafo de prerrequisitos.

CONTENIDO EDUCATIVO. Sin datos consultados: el grafo de 12 conceptos de la unidad 'Dia, estaciones y fases lunares' y sus
prerrequisitos son una propuesta ILUSTRATIVA del curso (no validada con estudiantes ni tomada de una progresion de aprendizaje publicada).
Tolerancias: el orden topologico se verifica arista por arista; el numero de ordenes validos se calcula por programacion dinamica sobre
subconjuntos y se compara con un muestreo aleatorio (semilla 131), solo como orden de magnitud.
"""
from __future__ import annotations
import platform, random
from functools import lru_cache

CONCEPTOS = {
    "luz": "La luz viaja en linea recta",
    "esfera": "La Tierra es una esfera",
    "rotacion": "Rotacion de la Tierra (dia y noche)",
    "orbita": "Traslacion de la Tierra alrededor del Sol",
    "inclinacion": "Inclinacion del eje terrestre",
    "angulo": "Angulo de incidencia y flujo por area",
    "estaciones": "Causa de las estaciones",
    "luna_orbita": "La Luna orbita la Tierra",
    "mitad": "La Luna siempre tiene una mitad iluminada",
    "fases": "Fases lunares como vista de la parte iluminada",
    "eclipses": "Eclipses (por que no ocurren cada mes)",
    "modelo": "Escala del sistema Tierra-Luna-Sol",
}
PRE = {
    "luz": [], "esfera": [], "modelo": [], "luna_orbita": ["modelo"],
    "rotacion": ["esfera", "luz"], "orbita": ["modelo"], "inclinacion": ["esfera"],
    "angulo": ["luz"], "estaciones": ["orbita", "inclinacion", "angulo"],
    "mitad": ["luz", "luna_orbita"], "fases": ["mitad", "luna_orbita", "rotacion"],
    "eclipses": ["fases", "inclinacion"],
}


def orden_topologico(pre):
    grado = {n: len(p) for n, p in pre.items()}
    sig = {n: [] for n in pre}
    for n, ps in pre.items():
        for p in ps:
            sig[p].append(n)
    listos = sorted(n for n, g in grado.items() if g == 0)
    sal = []
    while listos:
        n = listos.pop(0)
        sal.append(n)
        for m in sorted(sig[n]):
            grado[m] -= 1
            if grado[m] == 0:
                listos.append(m)
        listos.sort()
    return sal if len(sal) == len(pre) else None  # None: hay ciclo


def violaciones(orden, pre):
    pos = {n: i for i, n in enumerate(orden)}
    return [(p, n) for n, ps in pre.items() for p in ps if pos[p] > pos[n]]


def camino_critico(pre, orden):
    prof = {}
    for n in orden:
        prof[n] = 1 + max((prof[p] for p in pre[n]), default=0)
    return prof


def contar_ordenes(pre):
    nombres = sorted(pre)
    idx = {n: i for i, n in enumerate(nombres)}
    mask_pre = [sum(1 << idx[p] for p in pre[n]) for n in nombres]
    N = len(nombres)

    @lru_cache(None)
    def f(mask):
        if mask == (1 << N) - 1:
            return 1
        return sum(f(mask | (1 << i)) for i in range(N) if not mask >> i & 1 and mask_pre[i] & mask == mask_pre[i])

    return f(0)


def muestreo(pre, n=200000, seed=131):
    rng = random.Random(seed)
    nombres = list(pre)
    buenos = 0
    for _ in range(n):
        rng.shuffle(nombres)
        if not violaciones(nombres, pre):
            buenos += 1
    return buenos / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Grafo de 12 conceptos ILUSTRATIVO (propuesta del curso); sin progresion de aprendizaje publicada consultada.")
    orden = orden_topologico(PRE)
    print("Orden topologico (empates por nombre):")
    for i, n in enumerate(orden, 1):
        print(f"  {i:2d}. {n:12s} <- {', '.join(PRE[n]) or '(sin prerrequisito)'}")
    print(f"Violaciones del orden propuesto: {len(violaciones(orden, PRE))}")
    prof = camino_critico(PRE, orden)
    mx = max(prof.values())
    final = [n for n, d in prof.items() if d == mx]
    print(f"Camino critico: {mx} conceptos (acaba en {', '.join(final)}) ; si se ensenan de a uno por sesion hacen falta al menos {mx} sesiones encadenadas")
    # un orden de un docente que salta prerrequisitos
    docente = ["estaciones", "luz", "esfera", "modelo", "orbita", "inclinacion", "angulo", "rotacion", "luna_orbita", "mitad", "fases", "eclipses"]
    v = violaciones(docente, PRE)
    print(f"Orden del docente (estaciones primero): {len(v)} violaciones ; p. ej. {v[0][0]} debe ir antes que {v[0][1]}")
    # ciclo
    ciclico = {k: list(vv) for k, vv in PRE.items()}
    ciclico["luz"] = ["estaciones"]
    print(f"Con 'luz' dependiendo de 'estaciones': orden = {orden_topologico(ciclico)} (None indica ciclo)")
    # numero de ordenes validos
    total = contar_ordenes(PRE)
    import math
    p_exacta = total / math.factorial(len(PRE))
    p_mc = muestreo(PRE)
    print(f"Ordenes validos exactos (programacion dinamica): {total} de {math.factorial(len(PRE))} permutaciones ; fraccion {p_exacta:.3e}")
    print(f"Muestreo de 200000 permutaciones al azar: {p_mc:.1e} cumplen el orden (un orden al azar casi nunca es valido)")
    assert not violaciones(orden, PRE) and orden_topologico(ciclico) is None
    assert total >= 1 and p_exacta < 1e-3
    assert contar_ordenes({"a": [], "b": ["a"], "c": ["a"]}) == 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
