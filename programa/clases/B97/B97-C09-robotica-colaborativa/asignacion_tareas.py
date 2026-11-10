#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C09: asignacion de tareas entre robots, heuristica voraz frente al optimo exacto.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): 8 robots y 8 tareas en un area de 100 x 100 m, velocidades de 0.05 a 0.15 m/s,
tiempos de trabajo de 300 a 900 s por tarea, semilla fija, 300 instancias.
Modelo: costo(i, j) = distancia(robot i, tarea j)/velocidad_i + trabajo_j [s]; asignacion uno a uno que minimiza el tiempo total.
Metodos: voraz (cada tarea, en orden, toma el robot libre mas barato) y optimo exacto por permutaciones (8! = 40320).
Segunda via: programacion dinamica sobre subconjuntos de robots; debe dar el mismo optimo en cada instancia (tolerancia 1e-9).
Unidades: metros, m/s y segundos. Sin colisiones, sin comunicacion y sin precedencias entre tareas.
"""
from __future__ import annotations
import itertools, math, platform, random

N, NINST, SEMILLA = 8, 300, 20261110                       # SINTETICOS


def instancia(rng):
    rob = [(rng.uniform(0, 100), rng.uniform(0, 100), rng.uniform(0.05, 0.15)) for _ in range(N)]
    tar = [(rng.uniform(0, 100), rng.uniform(0, 100), rng.uniform(300, 900)) for _ in range(N)]
    return [[math.hypot(r[0] - t[0], r[1] - t[1]) / r[2] + t[2] for t in tar] for r in rob]


def voraz(c):
    libres, tot = set(range(N)), 0.0
    for j in range(N):
        i = min(libres, key=lambda r: c[r][j])
        libres.remove(i)
        tot += c[i][j]
    return tot


def exacto_perm(c):
    return min(sum(c[p[j]][j] for j in range(N)) for p in itertools.permutations(range(N)))


def exacto_dp(c):
    inf = math.inf
    f = [inf] * (1 << N)
    f[0] = 0.0
    for m in range(1 << N):
        if f[m] == inf:
            continue
        j = bin(m).count("1")              # siguiente tarea a asignar
        if j == N:
            continue
        for i in range(N):
            if not m >> i & 1:
                v = f[m] + c[i][j]
                if v < f[m | 1 << i]:
                    f[m | 1 << i] = v
    return f[(1 << N) - 1]


def calc():
    rng = random.Random(SEMILLA)
    brecha, peor, dmax, n_opt = [], 0.0, 0.0, 0
    primero = None
    for k in range(NINST):
        c = instancia(rng)
        v = voraz(c)
        e = exacto_dp(c)
        if k < 20:                          # la permutacion completa solo en 20 instancias (costo de calculo)
            dmax = max(dmax, abs(exacto_perm(c) - e))
        g = v / e - 1
        brecha.append(g)
        peor = max(peor, g)
        n_opt += g < 1e-12
        if primero is None:
            primero = (v, e)
    media = sum(brecha) / NINST
    return dict(media=media, peor=peor, dif=dmax, n_opt=n_opt, v0=primero[0], e0=primero[1], g0=primero[0] / primero[1] - 1,
                v0_h=primero[0] / 3600, e0_h=primero[1] / 3600, frac=n_opt / NINST)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: {N} robots y {N} tareas; {NINST} instancias; semilla {SEMILLA}")
    print(f"Instancia 1: voraz = {r['v0']:.1f} s ({r['v0_h']:.3f} h); optimo = {r['e0']:.1f} s ({r['e0_h']:.3f} h); brecha = {100*r['g0']:.2f} %")
    print(f"Brecha media del voraz = {100*r['media']:.2f} %; peor caso = {100*r['peor']:.2f} %; instancias en que el voraz es optimo = {r['n_opt']} de {NINST} ({100*r['frac']:.1f} %)")
    print(f"Diferencia maxima entre permutaciones y programacion dinamica (20 instancias) = {r['dif']:.2e} s")
    assert r["dif"] < 1e-9 and r["media"] >= 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
