#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C05: energia de transporte de carga en la Luna y en Marte y ruta de minima energia.

CONSULTADO (2026-11-10, fichas NASA/NSSDC): gravedad media de la Luna 1.62 m/s2 y de Marte 3.73 m/s2; la gravedad terrestre 9.80665 m/s2 es un valor estandar no consultado en esta sesion.
ILUSTRATIVOS (no medidos): vehiculo de 800 kg con 400 kg de carga, coeficiente de rodadura sobre regolito 0.15, eficiencia 0.60,
bateria con energia especifica 150 Wh/kg y 200 kg de bateria. Sin regeneracion en bajada (la energia no puede ser negativa).
Modelo: fuerza de avance F = m g (Crr cos(theta) + sin(theta)); energia E = max(F,0) d / eta.
Terreno SINTETICO: rejilla 16 x 16 de celdas de 100 m, relieve suma de dos senos (amplitud 4 x 15-25 m y 4 x 8-14 m) con semilla fija; ruta de la esquina (0,0) a la (15,15) con 8 vecinos.
Segunda via: Dijkstra frente a Bellman-Ford sobre la misma rejilla. Tolerancia: costes iguales con 1e-9.
"""
from __future__ import annotations
import heapq
import math
import platform
import random

SEMILLA = 20261110
G = {"Tierra": 9.80665, "Luna": 1.62, "Marte": 3.73}
M_VEH, M_CARGA, CRR, ETA = 800.0, 400.0, 0.15, 0.60
E_ESP, M_BAT = 150.0 * 3600.0, 200.0  # J/kg, kg
N, CELDA = 16, 100.0


def energia_tramo(g, masa, dz, d):
    th = math.atan2(dz, d)
    f = masa * g * (CRR * math.cos(th) + math.sin(th))
    return max(f, 0.0) * math.hypot(d, dz) / ETA


def terreno():
    rng = random.Random(SEMILLA)
    a1, a2, p1, p2 = 4 * rng.uniform(15, 25), 4 * rng.uniform(8, 14), rng.uniform(0, 6), rng.uniform(0, 6)
    return [[a1 * math.sin(i / 3.0 + p1) + a2 * math.sin(j / 2.5 + p2) for j in range(N)] for i in range(N)]


def aristas(z, g, masa, modo):
    for i in range(N):
        for j in range(N):
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if (di or dj) and 0 <= i + di < N and 0 <= j + dj < N:
                        d = CELDA * math.hypot(di, dj)
                        dz = z[i + di][j + dj] - z[i][j]
                        c = energia_tramo(g, masa, dz, d) if modo == "energia" else math.hypot(d, dz)
                        yield (i, j), (i + di, j + dj), c


def dijkstra(z, g, masa, modo):
    """Devuelve (coste, camino) de (0,0) a (N-1,N-1)."""
    ady = {}
    for u, v, c in aristas(z, g, masa, modo):
        ady.setdefault(u, []).append((v, c))
    dist = {(0, 0): 0.0}
    padre = {}
    cola = [(0.0, (0, 0))]
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist.get(u, 1e300):
            continue
        for v, c in ady.get(u, []):
            if d + c < dist.get(v, 1e300):
                dist[v] = d + c
                padre[v] = u
                heapq.heappush(cola, (d + c, v))
    fin = (N - 1, N - 1)
    camino = [fin]
    while camino[-1] != (0, 0):
        camino.append(padre[camino[-1]])
    return dist[fin], camino[::-1]


def energia_camino(z, g, masa, camino):
    e = 0.0
    for (i, j), (k, l) in zip(camino, camino[1:]):
        e += energia_tramo(g, masa, z[k][l] - z[i][j], CELDA * math.hypot(k - i, l - j))
    return e


def bellman_ford(z, g, masa):
    e = list(aristas(z, g, masa, "energia"))
    dist = {(i, j): 1e300 for i in range(N) for j in range(N)}
    dist[(0, 0)] = 0.0
    for _ in range(N * N):
        cambio = False
        for u, v, c in e:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                cambio = True
        if not cambio:
            break
    return dist[(N - 1, N - 1)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla {SEMILLA}")
    print("Datos ILUSTRATIVOS: masas, Crr = 0.15, eta = 0.60, 150 Wh/kg, bateria 200 kg; terreno SINTETICO 16 x 16 de 100 m")
    masa = M_VEH + M_CARGA
    print(" cuerpo   g [m/s2]   E llano [Wh/km]   E llano [Wh/(t km)]   alcance llano [km]")
    for nom, g in G.items():
        e_km = energia_tramo(g, masa, 0.0, 1000.0)
        alc = M_BAT * E_ESP / e_km  # km
        print(f"{nom:7s} {g:9.5f} {e_km / 3600:15.1f} {e_km / 3600 / (M_CARGA / 1000):19.1f} {alc:18.1f}")
    z = terreno()
    print(f"Relieve sintetico: minimo {min(map(min, z)):.1f} m, maximo {max(map(max, z)):.1f} m")
    res = {}
    for nom in ("Luna", "Marte"):
        g = G[nom]
        e_min, cam_e = dijkstra(z, g, masa, "energia")
        d_min, cam_d = dijkstra(z, g, masa, "distancia")
        e_de_d = energia_camino(z, g, masa, cam_d)
        res[nom] = e_min
        assert e_min <= e_de_d + 1e-9
        print(f"{nom}: ruta de minima energia {e_min / 3.6e6:.4f} kWh ; ruta de minima distancia ({d_min:.1f} m) cuesta {e_de_d / 3.6e6:.4f} kWh "
              f"({(e_de_d / e_min - 1) * 100:.2f} % mas)")
    bf = bellman_ford(z, G["Luna"], masa)
    res["Luna"] = dijkstra(z, G["Luna"], masa, "energia")[0]
    print(f"Bellman-Ford (Luna): {bf / 3.6e6:.4f} kWh ; Dijkstra: {res['Luna'] / 3.6e6:.4f} kWh")
    print(f"Cociente de energia Marte/Luna en la ruta = {res['Marte'] / res['Luna']:.4f} ; g_M/g_L = {G['Marte'] / G['Luna']:.4f}")
    assert abs(bf - res["Luna"]) < 1e-9 * max(1.0, res["Luna"])
    assert res["Marte"] > res["Luna"] > 0
    assert abs(energia_tramo(G["Marte"], masa, 0.0, 1000.0) / energia_tramo(G["Luna"], masa, 0.0, 1000.0) - G["Marte"] / G["Luna"]) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
