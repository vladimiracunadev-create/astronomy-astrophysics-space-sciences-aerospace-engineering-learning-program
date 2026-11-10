#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C16: exploracion autonoma por fronteras frente a un paseo aleatorio en una rejilla.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): 15 mapas de 30 x 30 celdas con 20 % de obstaculos, alcance del sensor de 3 celdas (cuadrado, sin linea de vision),
inicio en (0, 0), semilla fija, tope de 20000 pasos para el paseo aleatorio. Ningun mapa es un terreno real.
Modelo: el robot conoce solo lo que ha visto; una frontera es una celda libre conocida con una vecina desconocida; la estrategia va a la frontera mas cercana por BFS
sobre celdas libres conocidas. El paseo aleatorio elige una vecina libre al azar. Ambos terminan al conocer todas las celdas libres alcanzables (la estrategia por fronteras
termina cuando no quedan fronteras).
Segunda via: la cobertura se mide contra la alcanzabilidad real (BFS sobre el mapa verdadero) y se comprueba que ninguna celda 'libre' conocida sea un obstaculo.
Unidades: celdas y pasos. Sin ruido de sensor, sin incertidumbre de localizacion ni coste energetico.
"""
from __future__ import annotations
import collections, platform, random, statistics

N, P_OBS, R, NMAPAS, TOPE, SEMILLA = 30, 0.20, 3, 15, 20000, 20261110                # SINTETICOS
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def mapa(rng):
    m = [[rng.random() < P_OBS for _ in range(N)] for _ in range(N)]
    m[0][0] = False
    return m


def alcanzables(m):
    vis = {(0, 0)}
    q = collections.deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if 0 <= a < N and 0 <= b < N and not m[a][b] and (a, b) not in vis:
                vis.add((a, b)); q.append((a, b))
    return vis


def ver(m, conocido, p, alc=None):
    nuevas = 0
    for a in range(max(0, p[0] - R), min(N, p[0] + R + 1)):
        for b in range(max(0, p[1] - R), min(N, p[1] + R + 1)):
            if conocido[a][b] == 0:
                conocido[a][b] = 2 if m[a][b] else 1          # 1 libre, 2 obstaculo, 0 desconocido
                if alc is not None and (a, b) in alc:
                    nuevas += 1
    return nuevas


def es_frontera(conocido, c):
    if conocido[c[0]][c[1]] != 1:
        return False
    for dx, dy in DIRS:
        a, b = c[0] + dx, c[1] + dy
        if 0 <= a < N and 0 <= b < N and conocido[a][b] == 0:
            return True
    return False


def siguiente_paso(conocido, p):
    """BFS sobre celdas libres conocidas hasta la frontera mas cercana; devuelve la primera celda del camino."""
    padre = {p: None}
    q = collections.deque([p])
    while q:
        c = q.popleft()
        if c != p and es_frontera(conocido, c):
            while padre[c] != p:
                c = padre[c]
            return c
        for dx, dy in DIRS:
            a, b = c[0] + dx, c[1] + dy
            if 0 <= a < N and 0 <= b < N and conocido[a][b] == 1 and (a, b) not in padre:
                padre[(a, b)] = c; q.append((a, b))
    return None


def explorar_fronteras(m, alc):
    conocido = [[0] * N for _ in range(N)]
    p, pasos = (0, 0), 0
    ver(m, conocido, p)
    while True:
        s = siguiente_paso(conocido, p)
        if s is None:
            break
        p = s; pasos += 1
        ver(m, conocido, p)
    libres = sum(1 for c in alc if conocido[c[0]][c[1]] == 1)
    falsos = sum(1 for a in range(N) for b in range(N) if conocido[a][b] == 1 and m[a][b])
    return pasos, libres / len(alc), falsos


def paseo(m, alc, objetivo_libres, rng):
    conocido = [[0] * N for _ in range(N)]
    p, pasos = (0, 0), 0
    n_conocidas = ver(m, conocido, p, alc)
    while pasos < TOPE:
        if n_conocidas >= objetivo_libres:
            return pasos, True
        opciones = [(p[0] + dx, p[1] + dy) for dx, dy in DIRS if 0 <= p[0] + dx < N and 0 <= p[1] + dy < N and not m[p[0] + dx][p[1] + dy]]
        if not opciones:
            return pasos, False
        p = rng.choice(opciones); pasos += 1
        n_conocidas += ver(m, conocido, p, alc)
    return pasos, False


def calc():
    rng = random.Random(SEMILLA)
    pf, pr, cob, falsos, alcs, logrados = [], [], [], 0, [], 0
    for _ in range(NMAPAS):
        m = mapa(rng)
        alc = alcanzables(m)
        pasos, cobertura, f = explorar_fronteras(m, alc)
        n_obj = int(round(cobertura * len(alc)))
        pasos_r, ok = paseo(m, alc, n_obj, rng)
        pf.append(pasos); pr.append(pasos_r); cob.append(cobertura); falsos += f; alcs.append(len(alc)); logrados += ok
    return dict(pasos_f=statistics.mean(pf), pasos_r=statistics.mean(pr), razon=statistics.mean(pr) / statistics.mean(pf), cob_min=min(cob), cob_media=statistics.mean(cob),
                falsos=falsos, alc=statistics.mean(alcs), logrados=logrados, nmapas=NMAPAS, p_obs=P_OBS, max_f=max(pf), min_f=min(pf), mejor=sum(1 for a, b in zip(pf, pr) if a < b))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: {NMAPAS} mapas de {N} x {N}; {int(P_OBS*100)} % de obstaculos; sensor de {R} celdas; semilla {SEMILLA}")
    print(f"Celdas libres alcanzables (media) = {r['alc']:.1f}; cobertura de la estrategia por fronteras: media {100*r['cob_media']:.2f} %, minima {100*r['cob_min']:.2f} %")
    print(f"Pasos por fronteras: media {r['pasos_f']:.1f} (min {r['min_f']}, max {r['max_f']}); paseo aleatorio hasta la misma cobertura: media {r['pasos_r']:.1f} ({r['logrados']} de {r['nmapas']} dentro del tope)")
    print(f"El paseo necesita {r['razon']:.1f} veces mas pasos; fronteras gana en {r['mejor']} de {r['nmapas']} mapas")
    print(f"Celdas conocidas como libres que eran obstaculos = {r['falsos']}")
    assert r["falsos"] == 0 and r["cob_media"] > 0.9 and r["razon"] > 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
