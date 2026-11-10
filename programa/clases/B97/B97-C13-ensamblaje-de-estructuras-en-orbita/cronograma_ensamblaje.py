#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C13: cronograma de ensamblaje de una armadura con precedencias, ruta critica y k robots.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): 14 tareas con duraciones en minutos y precedencias; 1 a 4 robots identicos.
Modelo: planificacion por lista con prioridad al camino mas largo restante (HLF), sin tiempos de desplazamiento ni cambio de herramienta.
Cotas: makespan >= max(ruta critica, trabajo total/k) y makespan <= trabajo/k + (1 - 1/k) ruta critica (Graham, 1966; estas cotas son resultados estandar y no se consultaron aqui).
Segunda via: la ruta critica por programacion dinamica hacia adelante y por recursion hacia atras debe coincidir; las cotas deben cumplirse en cada k (tolerancia 1e-9).
Unidades: minutos. Sin fallas, sin reintentos y sin colisiones entre robots.
"""
from __future__ import annotations
import platform
from functools import lru_cache

TAREAS = {  # nombre: (duracion [min], predecesoras)  -- SINTETICAS
    "T01 posicionar base": (20, []),
    "T02 puntal A": (15, ["T01 posicionar base"]),
    "T03 puntal B": (15, ["T01 posicionar base"]),
    "T04 puntal C": (15, ["T01 posicionar base"]),
    "T05 nodo 1": (10, ["T02 puntal A", "T03 puntal B"]),
    "T06 nodo 2": (10, ["T03 puntal B", "T04 puntal C"]),
    "T07 diagonal 1": (18, ["T05 nodo 1"]),
    "T08 diagonal 2": (18, ["T06 nodo 2"]),
    "T09 puntal superior": (15, ["T07 diagonal 1", "T08 diagonal 2"]),
    "T10 soporte de panel": (25, ["T09 puntal superior"]),
    "T11 cableado": (12, ["T05 nodo 1", "T06 nodo 2"]),
    "T12 alineacion": (8, ["T09 puntal superior"]),
    "T13 inspeccion": (10, ["T10 soporte de panel", "T11 cableado", "T12 alineacion"]),
    "T14 cierre": (5, ["T13 inspeccion"]),
}
NOMBRES = list(TAREAS)


def ruta_adelante():
    fin = {}
    for n in NOMBRES:                       # el orden del diccionario ya es topologico
        d, pre = TAREAS[n]
        fin[n] = d + max((fin[p] for p in pre), default=0)
    return max(fin.values())


def ruta_atras():
    suc = {n: [m for m in NOMBRES if n in TAREAS[m][1]] for n in NOMBRES}

    @lru_cache(None)
    def largo(n):
        return TAREAS[n][0] + max((largo(m) for m in suc[n]), default=0)
    return max(largo(n) for n in NOMBRES), largo


def planificar(k):
    cp, largo = ruta_atras()
    libre = [0.0] * k
    fin, hecho = {}, set()
    pendientes = set(NOMBRES)
    while pendientes:
        listas = [n for n in pendientes if all(p in hecho for p in TAREAS[n][1])]
        # prioridad: camino mas largo restante; la tarea empieza cuando hay robot libre y estan terminadas sus predecesoras
        n = max(listas, key=lambda x: (largo(x), x))
        r = min(range(k), key=lambda i: libre[i])
        ini = max(libre[r], max((fin[p] for p in TAREAS[n][1]), default=0.0))
        fin[n] = ini + TAREAS[n][0]
        libre[r] = fin[n]
        hecho.add(n)
        pendientes.remove(n)
    return max(fin.values())


def calc():
    trabajo = sum(d for d, _ in TAREAS.values())
    cp_a, _ = ruta_adelante(), None
    cp_b, _l = ruta_atras()
    filas = []
    ok = True
    for k in (1, 2, 3, 4):
        ms = planificar(k)
        inf = max(cp_b, trabajo / k)
        sup = trabajo / k + (1 - 1 / k) * cp_b
        ok = ok and inf - 1e-9 <= ms <= sup + 1e-9
        filas.append((k, ms, inf, sup, trabajo / (k * ms)))
    return dict(trabajo=trabajo, cp=cp_b, dif_cp=abs(cp_a - cp_b), filas=filas, cotas_ok=ok, ms1=filas[0][1], ms2=filas[1][1], ms3=filas[2][1], ms4=filas[3][1],
                ef2=filas[1][4], ef4=filas[3][4], aceler2=filas[0][1] / filas[1][1], aceler4=filas[0][1] / filas[3][1], ntar=len(TAREAS))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Armadura SINTETICA: {r['ntar']} tareas; trabajo total = {r['trabajo']} min; ruta critica = {r['cp']} min (adelante y atras difieren en {r['dif_cp']:.1e})")
    print(" robots  makespan [min]  cota inferior  cota superior  eficiencia")
    for k, ms, inf, sup, ef in r["filas"]:
        print(f"{k:6d} {ms:15.1f} {inf:14.2f} {sup:14.2f} {ef:11.3f}")
    print(f"Aceleracion con 2 robots = {r['aceler2']:.3f}; con 4 robots = {r['aceler4']:.3f}")
    assert r["dif_cp"] < 1e-9 and r["cotas_ok"] and r["ms1"] == r["trabajo"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
