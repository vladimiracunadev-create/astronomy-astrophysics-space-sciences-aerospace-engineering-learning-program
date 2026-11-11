#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B108-C02: ruta de traslacion de una EVA sobre una estructura SINTETICA de asideros.

CONSULTADO (2026-11-10): Hagale y Price (NTRS 20000067662, resumen): el analisis de puestos de trabajo EVA modela con CAD el acceso
y la manipulacion de la tripulacion en la estructura. No se consultaron requisitos de diseno EVA ni la ubicacion de asideros de ninguna estacion.
ILUSTRATIVOS (sinteticos, no medidos): coordenadas de 9 nodos (asideros), alcance maximo entre asideros consecutivos 2.0 m,
velocidad de traslacion mano a mano 0.25 m/s, penalizacion de 20 s por cambio de asidero, longitud de cordon de seguridad 15 m.
Modelo: grafo no dirigido; arista valida si distancia <= alcance; coste = distancia/velocidad + penalizacion.
Algoritmo: Dijkstra con cola de prioridad. Segunda via: enumeracion exhaustiva de caminos simples (DFS) con el mismo coste.
Restriccion de cordon: todo nodo de la ruta debe estar a distancia euclidea <= 15 m del punto de anclaje (nodo A).
Sistema de referencia: ejes cartesianos de la estructura sintetica, origen en el nodo A, metros. Tolerancia: costes iguales con 1e-9 s.
"""
from __future__ import annotations
import heapq, math, platform

NODOS = {"A": (0, 0, 0), "B": (1.8, 0, 0), "C": (3.6, 0, 0), "D": (3.6, 1.8, 0), "E": (5.4, 1.8, 0),
         "F": (5.4, 3.6, 0), "G": (7.2, 3.6, 0), "H": (3.8, 3.4, 0.6), "I": (9.0, 3.6, 0)}
ALCANCE, VEL, PEN, CORDON, ANCLAJE = 2.0, 0.25, 20.0, 15.0, "A"


def dist(a, b):
    return math.dist(NODOS[a], NODOS[b])


def aristas(alcance=ALCANCE):
    g = {n: [] for n in NODOS}
    for a in NODOS:
        for b in NODOS:
            if a < b and dist(a, b) <= alcance:
                c = dist(a, b) / VEL + PEN
                g[a].append((b, c)); g[b].append((a, c))
    return g


def dijkstra(g, s, t, permitido):
    pq, mejor, previo = [(0.0, s)], {s: 0.0}, {}
    while pq:
        c, u = heapq.heappop(pq)
        if u == t:
            break
        if c > mejor[u]:
            continue
        for v, w in g[u]:
            if v in permitido and c + w < mejor.get(v, 1e18):
                mejor[v], previo[v] = c + w, u
                heapq.heappush(pq, (c + w, v))
    if t not in mejor:
        return None, None
    ruta, n = [t], t
    while n != s:
        n = previo[n]; ruta.append(n)
    return mejor[t], ruta[::-1]


def enumerar(g, s, t, permitido):
    mejor = [1e18, None]
    def dfs(u, vis, c):
        if u == t:
            if c < mejor[0]:
                mejor[0], mejor[1] = c, list(vis)
            return
        for v, w in g[u]:
            if v in permitido and v not in vis:
                vis.append(v); dfs(v, vis, c + w); vis.pop()
    dfs(s, [s], 0.0)
    return (mejor[0], mejor[1]) if mejor[1] else (None, None)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Estructura SINTETICA: {len(NODOS)} nodos; alcance {ALCANCE} m; velocidad {VEL} m/s; penalizacion {PEN} s por asidero")
    g = aristas()
    print(f"Aristas validas: {sum(len(v) for v in g.values()) // 2}")
    todos = set(NODOS)
    permitido = {n for n in NODOS if dist(ANCLAJE, n) <= CORDON}
    print(f"Nodos dentro del cordon de {CORDON} m desde {ANCLAJE}: {len(permitido)} de {len(NODOS)}")
    c1, r1 = dijkstra(g, "A", "I", permitido)
    c2, r2 = enumerar(g, "A", "I", permitido)
    print(f"Ruta A->I (Dijkstra): {'-'.join(r1)}; coste = {c1:.2f} s ({c1/60:.2f} min)")
    print(f"Ruta A->I (enumeracion): {'-'.join(r2)}; coste = {c2:.2f} s; diferencia = {abs(c1 - c2):.1e} s")
    long_ = sum(dist(a, b) for a, b in zip(r1, r1[1:]))
    print(f"Longitud recorrida = {long_:.2f} m en {len(r1) - 1} traslados; distancia directa = {dist('A', 'I'):.2f} m")
    c3, r3 = dijkstra(g, "A", "I", todos)
    print(f"Sin cordon: ruta {'-'.join(r3)} coste {c3:.2f} s")
    corto = {n for n in NODOS if dist(ANCLAJE, n) <= 8.0}
    c4, r4 = dijkstra(g, "A", "I", corto)
    print(f"Con cordon de 8.0 m: {'sin ruta (I queda fuera)' if r4 is None else '-'.join(r4)}")
    c5, r5 = dijkstra(aristas(1.5), "A", "I", todos)
    print(f"Con alcance de 1.5 m: {'sin ruta (grafo desconectado)' if r5 is None else '-'.join(r5)}")
    assert abs(c1 - c2) < 1e-9 and r1 is not None and r4 is None and r5 is None
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
