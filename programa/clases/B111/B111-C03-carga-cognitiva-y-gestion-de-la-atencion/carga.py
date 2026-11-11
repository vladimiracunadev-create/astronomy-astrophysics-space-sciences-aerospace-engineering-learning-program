#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C03: carga de trabajo ponderada (estilo NASA-TLX) y utilizacion de una linea de tiempo.

Datos SINTETICOS (ilustrativos, no de personas reales). Esquema NASA-TLX (Hart y Staveland 1988; solo metadatos consultados):
seis subescalas con valoracion 0-100 y 15 comparaciones por pares que dan un peso 0..5 a cada una (suma 15);
carga ponderada = sum(valoracion * peso) / 15; carga cruda = media simple de las seis valoraciones.
Subescalas: exigencia mental, fisica, temporal, rendimiento, esfuerzo, frustracion.
Valoraciones sinteticas: (70, 20, 80, 35, 65, 40). Preferencia sintetica en cada par: gana la subescala con mayor
'importancia' ficticia (importancia = 6, 1, 5, 2, 4, 3 para las seis, en orden).
Segunda via: los pesos se obtienen por enumeracion explicita de los 15 pares y, por separado, con la formula cerrada
(peso de la subescala con rango k de importancia, k = 0 la menor, es k).
Linea de tiempo SINTETICA: 4 tareas con demanda 0-1 por ventana de 10 s (12 ventanas = 120 s); sobrecarga si la demanda
total supera 1.0. Se reprograma la tarea D desplazandola y se compara el pico.
Supuestos: demandas aditivas (sin recursos multiples), sin aprendizaje ni fatiga.
"""
from __future__ import annotations
import itertools, platform

ESCALAS = ["Mental", "Fisica", "Temporal", "Rendimiento", "Esfuerzo", "Frustracion"]
VAL = [70, 20, 80, 35, 65, 40]
IMP = [6, 1, 5, 2, 4, 3]

TAREAS = {
    "A": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    "B": [0.0, 0.0, 0.4, 0.4, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "C": [0.0, 0.0, 0.0, 0.3, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "D": [0.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}


def pesos_enumeracion():
    w = [0] * 6
    for i, j in itertools.combinations(range(6), 2):
        w[i if IMP[i] > IMP[j] else j] += 1
    return w


def pesos_formula():
    orden = sorted(range(6), key=lambda i: IMP[i])
    w = [0] * 6
    for k, i in enumerate(orden):
        w[i] = k
    return w


def total(tareas):
    n = len(next(iter(tareas.values())))
    return [round(sum(t[k] for t in tareas.values()), 6) for k in range(n)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    w1, w2 = pesos_enumeracion(), pesos_formula()
    assert w1 == w2 and sum(w1) == 15
    print("Subescala     valoracion  peso  aporte (val*peso/15)")
    for e, v, w in zip(ESCALAS, VAL, w1):
        print(f"{e:12s} {v:10d} {w:5d} {v * w / 15:12.3f}")
    pond = sum(v * w for v, w in zip(VAL, w1)) / 15
    cruda = sum(VAL) / 6
    print(f"Pesos por enumeracion = {w1} ; por formula = {w2} ; suma = {sum(w1)}")
    print(f"Carga ponderada = {pond:.3f} ; carga cruda = {cruda:.3f} (escala 0-100)")
    tot = total(TAREAS)
    print("Linea de tiempo SINTETICA (ventanas de 10 s): demanda total por ventana")
    print("  " + " ".join(f"{x:4.1f}" for x in tot))
    sobre = [k for k, x in enumerate(tot) if x > 1.0 + 1e-9]
    print(f"Pico = {max(tot):.2f} ; ventanas en sobrecarga = {len(sobre)} ({10 * len(sobre)} s de 120 s)")
    t2 = dict(TAREAS)
    t2["D"] = [0.0] * 8 + [0.3, 0.3, 0.0, 0.0]
    tot2 = total(t2)
    print("Tras desplazar la tarea D a las ventanas 9-10:")
    print("  " + " ".join(f"{x:4.1f}" for x in tot2))
    sobre2 = [k for k, x in enumerate(tot2) if x > 1.0 + 1e-9]
    print(f"Pico = {max(tot2):.2f} ; ventanas en sobrecarga = {len(sobre2)} ; utilizacion media = {sum(tot2) / len(tot2):.3f}")
    assert abs(sum(TAREAS["D"]) - sum(t2["D"])) < 1e-9
    assert max(tot2) <= 1.0 + 1e-9 < max(tot)
    assert abs(sum(total(TAREAS)) - sum(tot2)) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
