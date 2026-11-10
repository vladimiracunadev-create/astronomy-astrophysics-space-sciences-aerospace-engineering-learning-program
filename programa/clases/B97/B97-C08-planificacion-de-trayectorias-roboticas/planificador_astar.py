#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C08: planificacion de rutas en una rejilla con A* y comprobacion contra Dijkstra.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): mapa de 40 x 40 celdas de 1 m, 22 % de obstaculos, 15 % de celdas rugosas con costo 3 (resto 1),
inicio (0, 0), meta (39, 39), semilla fija (se prueban semillas consecutivas hasta que exista ruta). Ningun mapa corresponde a un terreno real.
Modelo: 8 conectividad; costo de un movimiento = longitud (1 o raiz de 2) por el costo medio de las dos celdas; sin cortar esquinas.
A* con heuristica octil (admisible porque el costo minimo por celda es 1). Segunda via: Dijkstra (heuristica cero) debe dar el MISMO costo (tolerancia 1e-9).
Unidades: metros y costo adimensional. Sin dinamica del vehiculo ni incertidumbre de localizacion.
"""
from __future__ import annotations
import heapq, math, platform, random

N, P_OBS, P_RUG, SEMILLA0 = 40, 0.22, 0.15, 20261110      # SINTETICOS
INI, META = (0, 0), (N - 1, N - 1)
R2 = math.sqrt(2.0)


def mapa(semilla):
    rng = random.Random(semilla)
    obs = [[False] * N for _ in range(N)]
    cst = [[1.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            u = rng.random()
            if u < P_OBS:
                obs[i][j] = True
            elif u < P_OBS + P_RUG:
                cst[i][j] = 3.0
    obs[INI[0]][INI[1]] = obs[META[0]][META[1]] = False
    return obs, cst


def heur(a, b):
    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
    return (dx + dy) + (R2 - 2.0) * min(dx, dy)           # octil con costo minimo 1


def vecinos(obs, cst, p):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            q = (p[0] + dx, p[1] + dy)
            if not (0 <= q[0] < N and 0 <= q[1] < N) or obs[q[0]][q[1]]:
                continue
            if dx and dy and (obs[p[0] + dx][p[1]] or obs[p[0]][p[1] + dy]):
                continue
            yield q, (R2 if dx and dy else 1.0) * 0.5 * (cst[p[0]][p[1]] + cst[q[0]][q[1]])


def buscar(obs, cst, usar_h):
    g = {INI: 0.0}
    padre = {}
    abierta = [(heur(INI, META) if usar_h else 0.0, INI)]
    cerrado = set()
    while abierta:
        _, p = heapq.heappop(abierta)
        if p in cerrado:
            continue
        cerrado.add(p)
        if p == META:
            ruta = [p]
            while ruta[-1] in padre:
                ruta.append(padre[ruta[-1]])
            return g[p], ruta[::-1], len(cerrado)
        for q, c in vecinos(obs, cst, p):
            ng = g[p] + c
            if ng < g.get(q, math.inf):
                g[q] = ng
                padre[q] = p
                heapq.heappush(abierta, (ng + (heur(q, META) if usar_h else 0.0), q))
    return None


def calc():
    for s in range(SEMILLA0, SEMILLA0 + 50):
        obs, cst = mapa(s)
        a = buscar(obs, cst, True)
        if a:
            break
    d = buscar(obs, cst, False)
    costo, ruta, exp_a = a
    longitud = sum(math.hypot(ruta[i + 1][0] - ruta[i][0], ruta[i + 1][1] - ruta[i][1]) for i in range(len(ruta) - 1))
    rugosas = sum(1 for p in ruta if cst[p[0]][p[1]] > 1.0)
    return dict(semilla=s, costo=costo, costo_d=d[0], dif=abs(costo - d[0]), long=longitud, celdas=len(ruta), exp_a=exp_a, exp_d=d[2],
                ahorro=1 - exp_a / d[2], recta=math.hypot(N - 1, N - 1), rugosas=rugosas, h0=heur(INI, META), sobre=longitud / math.hypot(N - 1, N - 1),
                obstaculos=sum(sum(1 for v in f if v) for f in obs), total=N * N)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Mapa SINTETICO {N} x {N} (semilla {r['semilla']}): {r['obstaculos']} obstaculos de {r['total']} celdas; inicio {INI}, meta {META}")
    print(f"A*      : costo = {r['costo']:.4f}; longitud = {r['long']:.2f} m en {r['celdas']} celdas ({r['rugosas']} rugosas); nodos expandidos = {r['exp_a']}")
    print(f"Dijkstra: costo = {r['costo_d']:.4f}; nodos expandidos = {r['exp_d']}; ahorro de A* = {100*r['ahorro']:.1f} %")
    print(f"Diferencia de costo A* frente a Dijkstra = {r['dif']:.2e}; heuristica en el inicio = {r['h0']:.3f} <= costo")
    print(f"Distancia en linea recta = {r['recta']:.2f} m; la ruta es {r['sobre']:.3f} veces mas larga")
    assert r["dif"] < 1e-9 and r["h0"] <= r["costo"] + 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
