#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C16: infraestructura espacial critica como grafo de dependencias y falla en cascada (red SINTETICA de 12 nodos).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): art. VI del tratado de 1967 (nota legal.un.org): responsabilidad del Estado por las actividades nacionales; art. VIII: jurisdiccion y control del Estado de registro
sobre el objeto. NO consultado: ninguna definicion legal de infraestructura critica ni inventario real.
Modelo: grafo dirigido "X depende de Y"; falla en cascada: un nodo falla si falla al menos la fraccion UMBRAL de sus dependencias (UMBRAL = 0.5; los nodos sin
dependencias solo fallan por ataque o averia inicial). Alcance transitivo calculado por busqueda en anchura y por Warshall; deben coincidir.
Todo SINTETICO: nombres genericos.
"""
import itertools, json, platform

DEP = {
    "energia": [],
    "fibra": ["energia"],
    "estacion1": ["energia", "fibra"],
    "estacion2": ["energia", "fibra"],
    "sat_A": ["estacion1"],
    "sat_B": ["estacion1", "estacion2"],
    "sat_C": ["estacion2"],
    "centro_control": ["energia", "fibra"],
    "servicio_nav": ["sat_A", "sat_B", "sat_C"],
    "servicio_com": ["sat_B", "sat_C", "centro_control"],
    "banco": ["servicio_nav", "servicio_com"],
    "hospital": ["servicio_com", "energia"],
}
NODOS = list(DEP)
UMBRAL = 0.5

def cascada(inicial):
    caidos = set(inicial)
    cambio = True
    while cambio:
        cambio = False
        for n in NODOS:
            if n in caidos or not DEP[n]:
                continue
            if sum(d in caidos for d in DEP[n]) / len(DEP[n]) >= UMBRAL:
                caidos.add(n); cambio = True
    return caidos

# alcance transitivo (quien depende, directa o indirectamente, de X)
def alcance_bfs(x):
    vistos, cola = set(), [x]
    while cola:
        y = cola.pop()
        for n in NODOS:
            if y in DEP[n] and n not in vistos:
                vistos.add(n); cola.append(n)
    return vistos
idx = {n: i for i, n in enumerate(NODOS)}
M = [[False] * len(NODOS) for _ in NODOS]
for n in NODOS:
    for d in DEP[n]:
        M[idx[d]][idx[n]] = True          # d -> n (n depende de d)
for k in range(len(NODOS)):
    for i in range(len(NODOS)):
        for j in range(len(NODOS)):
            if M[i][k] and M[k][j]:
                M[i][j] = True
for x in NODOS:
    assert alcance_bfs(x) == {NODOS[j] for j in range(len(NODOS)) if M[idx[x]][j]}, x

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Red SINTETICA de 12 nodos; art. VI y VIII consultados (2026-11-11); ninguna definicion legal de infraestructura critica consultada.")
print(" nodo inicial        alcance transitivo   caen en cascada (umbral 0.5)")
rank = []
for x in NODOS:
    a = len(alcance_bfs(x)); c = len(cascada({x})) - 1
    rank.append((c, a, x))
    print(f" {x:16s} {a:10d} {c:24d}")
rank.sort(reverse=True)
print("Mas critico por cascada:", rank[0][2], f"({rank[0][0]} nodos mas)")
# doble falla
cand = [n for n in NODOS if n not in ("energia", "fibra")]
pares = sorted(((-(len(cascada({a, b})) - 2), a, b) for a, b in itertools.combinations(cand, 2)))
mejor = (-pares[0][0], pares[0][1], pares[0][2])
print(f"Peor par de fallas iniciales (sin las raices energia y fibra): {mejor[1]} + {mejor[2]} -> {mejor[0]} nodos adicionales")
assert rank[0][2] == "energia" and rank[0][0] == 11
print("CLAVES " + json.dumps({"top": rank[0][2], "ntop": rank[0][0], "par": mejor[1] + "+" + mejor[2], "npar": mejor[0], "fibra": len(cascada({"fibra"})) - 1, "sat_A": len(cascada({"sat_A"})) - 1, "est1": len(cascada({"estacion1"})) - 1}))
print("Pruebas superadas.")
