#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B66-C04: red de drenaje D8 sobre un terreno SINTETICO y duracion minima del agua.

Datos: ninguno medido. El modelo de terreno es SINTETICO (plano inclinado + valle gaussiano + ruido de semilla fija 20261109), celdas de 100 m.
ILUSTRATIVOS (sinteticos, no consultados): produccion de escorrentia r = 5e-8 m/s, concentracion volumetrica de sedimento Cs = 1e-3,
volumen excavado V = 2e8 m3, umbral de canal de 30 celdas. Ninguna cifra describe una cuenca marciana real.
Modelo: llenado de depresiones por inundacion con prioridad (epsilon = 1e-4 m), direccion D8 (descenso mas pronunciado), acumulacion de area,
Q = r A, duracion minima T = V /(Cs Q). Segunda via: en un plano inclinado sin ruido la acumulacion exacta es j+1 columnas aguas arriba.
Supuestos: escorrentia uniforme y constante, sin infiltracion ni evaporacion, caudal de banca llena continuo. Tolerancia: conservacion del area exacta (entero).
"""
from __future__ import annotations
import heapq, math, platform, random

N, DX = 40, 100.0
R_ESC, CS, V_EXC, UMBRAL = 5e-8, 1e-3, 2e8, 30
VEC = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def terreno(ruido, semilla=20261109):
    rng = random.Random(semilla)
    z = []
    for i in range(N):
        fila = []
        for j in range(N):
            v = 50.0 * (1.0 - j / (N - 1)) - 6.0 * math.exp(-(((i - N / 2) / 5.0) ** 2)) * (j / (N - 1))
            if ruido:
                v += 0.6 * rng.random()
            fila.append(v)
        z.append(fila)
    return z


def rellenar(z, eps=1e-4):
    z = [f[:] for f in z]
    vis = [[False] * N for _ in range(N)]
    h = []
    for i in range(N):
        for j in range(N):
            if i in (0, N - 1) or j in (0, N - 1):
                vis[i][j] = True
                heapq.heappush(h, (z[i][j], i, j))
    while h:
        zc, i, j = heapq.heappop(h)
        for di, dj in VEC:
            a, b = i + di, j + dj
            if 0 <= a < N and 0 <= b < N and not vis[a][b]:
                vis[a][b] = True
                z[a][b] = max(z[a][b], zc + eps)
                heapq.heappush(h, (z[a][b], a, b))
    return z


def acumulacion(z):
    celdas = sorted(((z[i][j], i, j) for i in range(N) for j in range(N)), reverse=True)
    acc = [[1] * N for _ in range(N)]
    destino = {}
    for zc, i, j in celdas:
        mejor, dest = 0.0, None
        for di, dj in VEC:
            a, b = i + di, j + dj
            if 0 <= a < N and 0 <= b < N:
                pend = (zc - z[a][b]) / (math.hypot(di, dj) * DX)
                if pend > mejor:
                    mejor, dest = pend, (a, b)
        destino[(i, j)] = dest
        if dest is not None:
            acc[dest[0]][dest[1]] += acc[i][j]
    return acc, destino


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # prueba analitica: plano inclinado sin ruido
    zp = [[10.0 * (N - 1 - j) for j in range(N)] for i in range(N)]
    ap, _ = acumulacion(zp)
    print(f"Plano inclinado sin ruido: acumulacion en (20, 10) = {ap[20][10]} ; esperado j+1 = 11")
    assert all(ap[i][j] == j + 1 for i in range(N) for j in range(N))
    z = rellenar(terreno(True))
    acc, dest = acumulacion(z)
    salidas = sum(acc[i][j] for (i, j), d in dest.items() if d is None)
    print(f"Terreno SINTETICO {N}x{N}, celda {DX:.0f} m ({N * N} celdas); area total = {N * N * DX * DX / 1e6:.2f} km2")
    print(f"Celdas sin destino (salidas) acumulan {salidas} celdas de {N * N}")
    assert salidas == N * N
    canal = sum(1 for i in range(N) for j in range(N) if acc[i][j] >= UMBRAL)
    long_canal = 0.0
    for (i, j), d in dest.items():
        if d is not None and acc[i][j] >= UMBRAL:
            long_canal += math.hypot(i - d[0], j - d[1]) * DX
    area_km2 = N * N * DX * DX / 1e6
    print(f"Celdas de canal (umbral {UMBRAL}): {canal} ; longitud de canal = {long_canal / 1000:.2f} km ; densidad de drenaje = {long_canal / 1000 / area_km2:.3f} km/km2")
    amax = max(max(f) for f in acc)
    q = R_ESC * amax * DX * DX
    print(f"Mayor area drenada = {amax} celdas = {amax * DX * DX / 1e6:.2f} km2 ; Q = r A = {q:.2f} m3/s (ILUSTRATIVO)")
    for factor in (0.5, 1.0, 2.0):
        t = V_EXC / (CS * q * factor)
        print(f"  escorrentia x{factor}: T minimo = {t:.3e} s = {t / 3.15576e7:.1f} anos")
    assert canal > 0 and long_canal > 0
    assert abs(V_EXC / (CS * q * 0.5) - 2 * V_EXC / (CS * q)) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
