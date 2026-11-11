#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C02: zonificacion de un habitat por flujos (busqueda exhaustiva sobre una cuadricula 2 x 4).

Datos consultados (2026-11-10; Burke, Howard y Kessler 2022, AIAA ASCEND, Tabla 4 «Recommended vs. Final Areas in SH Internal Layout»):
areas recomendadas y areas del trazado de referencia de un Surface Habitat lunar de 2 tripulantes (no es un diseno de vuelo).
SINTETICOS / ILUSTRATIVOS: los flujos entre zonas (viajes/dia), las penalizaciones de separacion, la cuadricula 2 x 4 y el paso de celda (2.6 m).
Las areas de zona del laboratorio agrupan filas de la Tabla 4 (ver ZONAS). Modelo: coste = sum_{i<j} f_ij * d_ij con d = distancia Manhattan entre celdas [m];
f > 0 atrae (flujo), f < 0 separa (incompatibilidad, p. ej. polvo de la esclusa frente a dormitorios). Se evalua cada una de las 8! = 40320 permutaciones.
Segunda via: el grupo de simetrias de la cuadricula 2 x 4 tiene 4 elementos, asi que el numero de trazados optimos es multiplo de 4; ademas el optimo no supera a ninguno de 2000 trazados al azar (semilla 109002).
Unidades: area [m2], flujo [viajes/dia], distancia [m], coste [viaje*m/dia]. Tolerancia de igualdad de costes: 1e-9.
"""
from __future__ import annotations
import itertools, platform, random

PASO = 2.6  # m, ILUSTRATIVO (celda 6.76 m2 >= mayor area de zona)
ZONAS = ["Dormitorios", "Higiene", "Cocina-mesa", "Medico", "Ejercicio", "Trabajo", "Control", "Esclusa"]
AREA_ZONA = {"Dormitorios": 2.68 + 3.70, "Higiene": 1.04 + 1.04, "Cocina-mesa": 0.95 + 1.17 + 2.23, "Medico": 3.43,
             "Ejercicio": 2.09, "Trabajo": 1.30, "Control": 2.10 + 0.97, "Esclusa": 5.18}
# flujos SINTETICOS (viajes/dia); negativos = separacion deseada
F = {("Dormitorios", "Higiene"): 20, ("Dormitorios", "Cocina-mesa"): 12, ("Cocina-mesa", "Higiene"): 6,
     ("Trabajo", "Control"): 14, ("Trabajo", "Esclusa"): 10, ("Esclusa", "Control"): 8, ("Medico", "Higiene"): 3,
     ("Medico", "Control"): 4, ("Ejercicio", "Higiene"): 5, ("Cocina-mesa", "Trabajo"): 6, ("Esclusa", "Higiene"): 2,
     ("Esclusa", "Dormitorios"): -5, ("Esclusa", "Cocina-mesa"): -5, ("Ejercicio", "Dormitorios"): -3}
# Tabla 4 (Burke et al. 2022): filas recomendadas y de trazado, y totales publicados
REC = [1.40, 1.82, 1.87, 1.5, 0.91, 1.06, 1.62, 1.37, 1.82, 0.56, 0.56]
LAY = [2.68, 3.70, 3.43, 2.09, 1.04, 1.04, 2.23, 1.30, 0.97, 2.10, 0.95, 1.17, 5.07, 8.65, 5.79]
TOT_REC, TOT_LAY = 14.6, 42.63
CELDAS = [(r, c) for r in range(2) for c in range(4)]


def dist(a, b):
    return PASO * (abs(a[0] - b[0]) + abs(a[1] - b[1]))


def coste(perm):  # perm[i] = indice de celda de la zona i
    pos = {z: CELDAS[perm[i]] for i, z in enumerate(ZONAS)}
    return sum(f * dist(pos[a], pos[b]) for (a, b), f in F.items())


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Flujos SINTETICOS; areas de la Tabla 4 de Burke et al. (2022); paso de celda 2.6 m ILUSTRATIVO")
    print(f"Suma de filas recomendadas = {sum(REC):.2f} m2 (total publicado {TOT_REC}; diferencia {TOT_REC - sum(REC):.2f})")
    print(f"Suma de filas del trazado  = {sum(LAY):.2f} m2 (total publicado {TOT_LAY}; diferencia {TOT_LAY - sum(LAY):.2f})")
    assert max(AREA_ZONA.values()) <= PASO ** 2
    costes = [coste(p) for p in itertools.permutations(range(8))]
    mejor, peor = min(costes), max(costes)
    n_opt = sum(1 for c in costes if abs(c - mejor) < 1e-9)
    rng = random.Random(109002)
    azar = [coste(rng.sample(range(8), 8)) for _ in range(2000)]
    media_azar = sum(azar) / len(azar)
    print(f"Trazados evaluados: {len(costes)}")
    print(f"Coste minimo = {mejor:.1f} ; maximo = {peor:.1f} ; media al azar = {media_azar:.1f}")
    print(f"Trazados optimos = {n_opt} (multiplo de 4: {n_opt % 4 == 0})")
    print(f"Ahorro del optimo frente a la media al azar = {100 * (media_azar - mejor) / abs(media_azar):.1f} %")
    mejor_perm = next(p for p in itertools.permutations(range(8)) if abs(coste(p) - mejor) < 1e-9)
    rejilla = [["" for _ in range(4)] for _ in range(2)]
    for i, z in enumerate(ZONAS):
        r, c = CELDAS[mejor_perm[i]]
        rejilla[r][c] = z
    print("Un trazado optimo (filas de la cuadricula):")
    for fila in rejilla:
        print("  " + " | ".join(f"{z:11s}" for z in fila))
    assert n_opt % 4 == 0
    assert all(mejor <= a + 1e-9 for a in azar)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
