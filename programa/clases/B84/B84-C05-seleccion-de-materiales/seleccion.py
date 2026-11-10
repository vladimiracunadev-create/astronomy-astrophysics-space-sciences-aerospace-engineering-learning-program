#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C05: seleccion de materiales con indices de merito y matriz de decision ponderada, con sensibilidad a los pesos.

DATOS ILUSTRATIVOS (valores tipicos, NO consultados, no de diseno):
  material        E [GPa]  rho [kg/m3]  sigma_y [MPa]  coste relativo (Al = 1)  disponibilidad de proceso (0-10)
  Al 6061-T6        69      2700          275              1                      9
  Ti-6Al-4V        114      4430          880             12                      6
  Mg AZ31           45      1780          200              2                      6
  CFRP cuasi-iso    54      1550          500 (traccion)  30                      5
Indices de Ashby: panel rigido a flexion M1 = E^(1/3)/rho; tirante de resistencia M2 = sigma_y/rho; columna M3 = E^(1/2)/rho.
Matriz ponderada: puntuacion = suma w_i x_i/max(x_i) con criterios M1, M2, 1/coste y disponibilidad. Sensibilidad: 2000 conjuntos de
pesos Dirichlet(1,1,1,1) con semilla fija; se cuenta cuantas veces gana cada material.
Unidades: GPa, MPa, kg/m3. Tolerancia: pesos suman 1 a 1e-12; la suma de victorias = 2000.
"""
from __future__ import annotations
import math, platform, random

MAT = {  # E GPa, rho, sigma_y MPa, coste, disponibilidad
    "Al 6061-T6": (69.0, 2700.0, 275.0, 1.0, 9.0),
    "Ti-6Al-4V": (114.0, 4430.0, 880.0, 12.0, 6.0),
    "Mg AZ31": (45.0, 1780.0, 200.0, 2.0, 6.0),
    "CFRP cuasi-iso": (54.0, 1550.0, 500.0, 30.0, 5.0),
}


def indices():
    out = {}
    for n, (E, rho, sy, c, d) in MAT.items():
        out[n] = (E ** (1 / 3) / (rho / 1e3), sy / (rho / 1e3), E ** 0.5 / (rho / 1e3), 1.0 / c, d)
    return out


def puntuar(w, ind, cols):
    mx = [max(v[k] for v in ind.values()) for k in cols]
    return {n: sum(wi * v[k] / m for wi, k, m in zip(w, cols, mx)) for n, v in ind.items()}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ind = indices()
    print("Indices con datos ILUSTRATIVOS (no consultados):")
    print(f"{'material':16s} {'M1 E^1/3/rho':>13s} {'M2 sy/rho':>10s} {'M3 E^1/2/rho':>13s} {'1/coste':>8s} {'disp.':>6s}")
    for n, v in ind.items():
        print(f"{n:16s} {v[0]:13.3f} {v[1]:10.1f} {v[2]:13.3f} {v[3]:8.3f} {v[4]:6.1f}")
    for k, nom in ((0, "panel rigido M1"), (1, "tirante M2"), (2, "columna M3")):
        mejor = max(ind, key=lambda x: ind[x][k])
        print(f"Mejor por {nom}: {mejor}")
    cols = (0, 1, 3, 4)
    w0 = [0.35, 0.35, 0.15, 0.15]
    assert abs(sum(w0) - 1) < 1e-12
    pun = puntuar(w0, ind, cols)
    print("Puntuacion con pesos [rigidez 0,35; resistencia 0,35; coste 0,15; disponibilidad 0,15]:")
    for n in sorted(pun, key=pun.get, reverse=True):
        print(f"  {n:16s} {pun[n]:.4f}")
    rng = random.Random(84005)
    gana = {n: 0 for n in MAT}
    for _ in range(2000):
        g = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        w = [x / sum(g) for x in g]
        p = puntuar(w, ind, cols)
        gana[max(p, key=p.get)] += 1
    print("Sensibilidad: victorias en 2000 pesos aleatorios (Dirichlet, semilla 84005):")
    for n, c in sorted(gana.items(), key=lambda x: -x[1]):
        print(f"  {n:16s} {c:5d} ({c / 20:.1f} %)")
    ganador0 = max(pun, key=pun.get)
    print(f"Ganador con los pesos base: {ganador0}; gana en {gana[ganador0] / 20:.1f} % de los pesos aleatorios")
    assert sum(gana.values()) == 2000
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
