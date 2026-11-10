#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C08: mapa de traversabilidad y ruta de minimo riesgo sobre un terreno SINTETICO.

Datos consultados (2026-11-10): de la pagina «Rover Components» de Mars 2020 (NASA, science.nasa.gov): rueda de 52.5 cm de diametro,
capacidad de cruzar obstaculos del tamano de una rueda y evitacion operativa de inclinaciones superiores a 30 grados; se usan solo como
ESCALA de los umbrales. ILUSTRATIVOS (sinteticos, no un terreno real ni un procedimiento de mision): rejilla de 40 x 40 celdas de 2.0 m,
terreno = tres ondas senoidales (amplitudes 2.6, 1.6 y 0.9 m) + cuenca gaussiana de 7 m + rugosidad de 0.03 m + hasta 30 rocas (una se descarta por la regla siguiente) de 0.10 a 0.45 m (ninguna a 2 celdas o menos del inicio o la meta); umbrales: pendiente 30 deg,
altura de obstaculo 0.20 m, rugosidad 0.08 m; pesos de coste w_s = 4, w_r = 2; semilla 20261110.
Modelo: pendiente = atan(|grad z|) por diferencias centrales; plano local 3x3 por minimos cuadrados; altura de obstaculo = z central menos
el plano; rugosidad = desviacion tipica de los residuos 3x3; coste de celda = 1 + w_s (pendiente/limite)^2 + w_r (rugosidad/limite),
infinito si se supera algun umbral; ruta de Dijkstra con 8 vecinos, coste del paso = distancia x media de los costes de celda.
Sistema: coordenadas de rejilla (i hacia el norte, j hacia el este), alturas en m. Supuestos: terreno estatico, sin incertidumbre de la
elevacion, sin dinamica del vehiculo.
Tolerancias: pendiente de un plano de 20 deg = 20 deg con error < 1e-9; rugosidad de un plano < 1e-12; Dijkstra con coste uniforme
frente a la distancia octil analitica < 1e-9.
"""
from __future__ import annotations
import heapq, math, platform, random

N, DX = 40, 2.0
LIM_PEND, LIM_OBS, LIM_RUG = 30.0, 0.20, 0.08
WS, WR = 4.0, 2.0
INICIO, META = (2, 2), (37, 37)


def terreno(rng):
    ondas = [(2.6, 0.11, 0.07, 0.3), (1.6, 0.05, 0.19, 1.7), (0.9, 0.21, 0.13, 4.0)]
    z = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            v = sum(a * math.sin(ki * i + kj * j + ph) for a, ki, kj, ph in ondas)
            v -= 7.0 * math.exp(-(((i - 20) ** 2 + (j - 22) ** 2) / (2 * 6.0**2)))
            z[i][j] = v + rng.gauss(0.0, 0.03)
    rocas = []
    for _ in range(30):
        i, j = rng.randrange(1, N - 1), rng.randrange(1, N - 1)
        if max(abs(i - INICIO[0]), abs(j - INICIO[1])) <= 2 or max(abs(i - META[0]), abs(j - META[1])) <= 2:
            continue
        z[i][j] += rng.uniform(0.10, 0.45)
        rocas.append((i, j))
    return z, rocas


def pendiente(z):
    s = [[0.0] * N for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            gi = (z[i + 1][j] - z[i - 1][j]) / (2 * DX)
            gj = (z[i][j + 1] - z[i][j - 1]) / (2 * DX)
            s[i][j] = math.degrees(math.atan(math.hypot(gi, gj)))
    return s


def plano_local(z, i, j):
    """Plano z = c + a di + b dj ajustado a los 9 puntos; devuelve (c, residuo central, desviacion de residuos)."""
    pts = [(di, dj, z[i + di][j + dj]) for di in (-1, 0, 1) for dj in (-1, 0, 1)]
    c = sum(p[2] for p in pts) / 9.0
    a = sum(p[0] * p[2] for p in pts) / 6.0
    b = sum(p[1] * p[2] for p in pts) / 6.0
    res = [p[2] - (c + a * p[0] + b * p[1]) for p in pts]
    sd = math.sqrt(sum(r * r for r in res) / 9.0)
    return res[4], sd


def mapas(z, lim_pend=LIM_PEND):
    sl = pendiente(z)
    cost = [[math.inf] * N for _ in range(N)]
    obs = [[0.0] * N for _ in range(N)]
    rug = [[0.0] * N for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            o, sd = plano_local(z, i, j)
            obs[i][j], rug[i][j] = o, sd
            if sl[i][j] > lim_pend or o > LIM_OBS or sd > LIM_RUG:
                continue
            cost[i][j] = 1.0 + WS * (sl[i][j] / lim_pend) ** 2 + WR * (sd / LIM_RUG)
    return sl, obs, rug, cost


def dijkstra(cost, ini, fin):
    dist = {ini: 0.0}
    prev = {}
    cola = [(0.0, ini)]
    while cola:
        d, u = heapq.heappop(cola)
        if u == fin:
            break
        if d > dist.get(u, math.inf):
            continue
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                v = (u[0] + di, u[1] + dj)
                if not (0 <= v[0] < N and 0 <= v[1] < N) or math.isinf(cost[v[0]][v[1]]):
                    continue
                paso = DX * math.hypot(di, dj) * 0.5 * (cost[u[0]][u[1]] + cost[v[0]][v[1]])
                nd = d + paso
                if nd < dist.get(v, math.inf):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(cola, (nd, v))
    if fin not in dist:
        return None, math.inf
    ruta = [fin]
    while ruta[-1] != ini:
        ruta.append(prev[ruta[-1]])
    return ruta[::-1], dist[fin]


def longitud(ruta):
    return sum(DX * math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(ruta, ruta[1:]))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261110)
    z, rocas = terreno(rng)
    print(f"Terreno SINTETICO {N}x{N} celdas de {DX} m; {len(rocas)} rocas; z entre {min(min(f) for f in z):.2f} y {max(max(f) for f in z):.2f} m")
    sl, obs, rug, cost = mapas(z)
    celdas = (N - 2) ** 2
    letal = sum(1 for i in range(1, N - 1) for j in range(1, N - 1) if math.isinf(cost[i][j]))
    por_p = sum(1 for i in range(1, N - 1) for j in range(1, N - 1) if sl[i][j] > LIM_PEND)
    por_o = sum(1 for i in range(1, N - 1) for j in range(1, N - 1) if obs[i][j] > LIM_OBS)
    por_r = sum(1 for i in range(1, N - 1) for j in range(1, N - 1) if rug[i][j] > LIM_RUG)
    smax = max(max(f) for f in sl)
    print(f"Pendiente maxima = {smax:.2f} deg ; celdas interiores = {celdas}")
    print(f"Celdas intransitables = {letal} ({100 * letal / celdas:.1f} %): por pendiente {por_p}, por obstaculo {por_o}, por rugosidad {por_r} (se solapan)")
    finitos = [cost[i][j] for i in range(1, N - 1) for j in range(1, N - 1) if not math.isinf(cost[i][j])]
    print(f"Coste de celda transitable: minimo {min(finitos):.3f}, media {sum(finitos) / len(finitos):.3f}, maximo {max(finitos):.3f}")
    ruta, c = dijkstra(cost, INICIO, META)
    dir_ = DX * math.hypot(META[0] - INICIO[0], META[1] - INICIO[1])
    assert ruta is not None
    print(f"Ruta de minimo coste: {len(ruta)} celdas ; longitud = {longitud(ruta):.1f} m ; coste = {c:.1f} ; distancia en linea recta = {dir_:.1f} m")
    print(f"  pendiente maxima en la ruta = {max(sl[i][j] for i, j in ruta[1:-1]):.2f} deg ; rugosidad maxima = {max(rug[i][j] for i, j in ruta[1:-1]):.4f} m")
    print("Sensibilidad al umbral de pendiente:")
    for lim in (20.0, 25.0, 30.0, 35.0):
        _, _, _, cst = mapas(z, lim)
        r, cc = dijkstra(cst, INICIO, META)
        nl = sum(1 for i in range(1, N - 1) for j in range(1, N - 1) if math.isinf(cst[i][j]))
        txt = f"longitud {longitud(r):7.1f} m, coste {cc:8.1f}" if r else "sin ruta"
        print(f"  limite {lim:4.1f} deg: intransitables {nl:4d}; {txt}")
    # verificaciones
    t20 = math.tan(math.radians(20.0))
    zp = [[t20 * DX * i for j in range(N)] for i in range(N)]
    sp = pendiente(zp)
    e_s = max(abs(sp[i][j] - 20.0) for i in range(1, N - 1) for j in range(1, N - 1))
    e_r = max(plano_local(zp, i, j)[1] for i in range(1, N - 1) for j in range(1, N - 1))
    ruta_u, cu = dijkstra([[1.0] * N for _ in range(N)], (0, 0), (35, 35))
    octil = DX * 35 * math.sqrt(2.0)
    print(f"Plano de 20 deg: error de pendiente = {e_s:.2e} deg ; rugosidad = {e_r:.2e} m")
    print(f"Dijkstra con coste uniforme (diagonal de 35 celdas): {cu:.6f} frente a la distancia octil {octil:.6f}")
    assert e_s < 1e-9 and e_r < 1e-12 and abs(cu - octil) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
