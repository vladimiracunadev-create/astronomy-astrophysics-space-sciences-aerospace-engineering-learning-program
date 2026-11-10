#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C01: red de tareas de ensamblaje, integracion y prueba (AIT) de un CubeSat 3U SINTETICO.

Calcula ruta critica y holguras (pasada hacia adelante y hacia atras), la verifica por enumeracion
de todos los caminos y mide el efecto de una falla en la prueba funcional (retrabajo + repeticion).
Unidades: dias de trabajo. Datos: duraciones SINTETICAS. Tolerancia: igualdad exacta (enteros).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

TAREAS = {  # id: (nombre, dias, predecesoras)
    "A": ("Recepcion e inspeccion de unidades", 2, []),
    "B": ("Preparacion de sala limpia", 1, []),
    "M": ("Fabricacion del arnes", 4, []),
    "C": ("Integracion de estructura y rieles", 2, ["A", "B"]),
    "D": ("Integracion de EPS y bateria", 3, ["C", "M"]),
    "E": ("Integracion de OBC y comunicaciones", 3, ["C"]),
    "F": ("Integracion de ADCS", 2, ["D"]),
    "G": ("Integracion de carga util", 4, ["E"]),
    "H": ("Prueba funcional integrada", 2, ["F", "G"]),
    "I": ("Ensayo de vibracion", 3, ["H"]),
    "J": ("Bakeout termico en vacio", 4, ["I"]),
    "K": ("Prueba funcional posensayo", 2, ["J"]),
    "L": ("Revision de datos y cierre", 2, ["K"]),
}


def cpm(tareas):
    orden, vistos = [], set()

    def visita(t):
        if t in vistos:
            return
        for p in tareas[t][2]:
            visita(p)
        vistos.add(t)
        orden.append(t)

    for t in tareas:
        visita(t)
    es, ef = {}, {}
    for t in orden:
        es[t] = max([ef[p] for p in tareas[t][2]], default=0)
        ef[t] = es[t] + tareas[t][1]
    fin_proy = max(ef.values())
    sucesoras = {t: [u for u in tareas if t in tareas[u][2]] for t in tareas}
    lf, ls = {}, {}
    for t in reversed(orden):
        lf[t] = min([ls[s] for s in sucesoras[t]], default=fin_proy)
        ls[t] = lf[t] - tareas[t][1]
    holgura = {t: ls[t] - es[t] for t in tareas}
    return orden, es, ef, ls, lf, holgura, fin_proy, sucesoras


def caminos(tareas, sucesoras):
    """Enumera todos los caminos inicio-fin con su duracion (verificacion independiente)."""
    inicios = [t for t in tareas if not tareas[t][2]]
    res = []

    def dfs(t, ruta, d):
        ruta, d = ruta + [t], d + tareas[t][1]
        if not sucesoras[t]:
            res.append((d, ruta))
        for s in sucesoras[t]:
            dfs(s, ruta, d)

    for t in inicios:
        dfs(t, [], 0)
    return sorted(res, reverse=True)


cabecera("Datos SINTETICOS: red AIT de un CubeSat 3U de ejemplo; duraciones en dias de trabajo")
orden, es, ef, ls, lf, holgura, T, suc = cpm(TAREAS)
print(f"Duracion del proyecto = {T} d ; tareas = {len(TAREAS)}")
print("id  inicio  fin  holgura  tarea")
for t in orden:
    print(f" {t}  {es[t]:5d} {ef[t]:5d} {holgura[t]:7d}  {TAREAS[t][0]}")
critica = [t for t in orden if holgura[t] == 0]
print("Ruta critica:", " -> ".join(critica))

todos = caminos(TAREAS, suc)
print(f"Caminos inicio-fin = {len(todos)} ; el mas largo = {todos[0][0]} d por {'-'.join(todos[0][1])}")
comprobar(todos[0][0] == T, "la ruta critica debe igualar el camino mas largo")
comprobar(all(h >= 0 for h in holgura.values()), "ninguna holgura puede ser negativa")
comprobar(sum(TAREAS[t][1] for t in critica) == T, "la suma de la ruta critica debe ser la duracion")

# Falla en la prueba funcional H: retrabajo R (3 d) y nueva prueba H2 (2 d)
T2 = dict(TAREAS)
T2["R"] = ("Retrabajo tras falla en H", 3, ["H"])
T2["H2"] = ("Repeticion de la prueba funcional", 2, ["R"])
T2["I"] = ("Ensayo de vibracion", 3, ["H2"])
_, _, _, _, _, h2, Tf, _ = cpm(T2)
print(f"Con una falla en H: duracion = {Tf} d (aumento = {Tf - T} d = 3 + 2)")
comprobar(Tf - T == 5, "el retraso debe ser retrabajo + repeticion")

# Falla en una tarea con holgura: el arnes M tiene holgura
print(f"Holgura de M (arnes) = {holgura['M']} d ; retraso de 2 d en M cambia la duracion en {max(0, 2 - holgura['M'])} d")
T3 = dict(TAREAS)
T3["M"] = ("Fabricacion del arnes", 4 + 2, [])
_, _, _, _, _, _, Tm, _ = cpm(T3)
comprobar(Tm - T == max(0, 2 - holgura["M"]), "el retraso en una tarea con holgura se absorbe hasta agotarla")
fin()
