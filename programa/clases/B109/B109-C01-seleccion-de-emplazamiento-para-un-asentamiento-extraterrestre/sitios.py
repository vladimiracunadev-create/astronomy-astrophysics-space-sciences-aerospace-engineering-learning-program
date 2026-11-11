#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C01: matriz de decision ponderada para elegir un emplazamiento lunar (5 sitios SINTETICOS).

Datos consultados (2026-11-10; NASA/NSSDC Moon Fact Sheet): periodo sinodico 29.53 d; gravedad en superficie 1.62 m/s2.
SINTETICOS / ILUSTRATIVOS (no son mediciones de ningun lugar real): los cinco sitios y sus atributos, los umbrales de descarte
(pendiente <= 10 grados, iluminacion >= 50 %) y los pesos base. La nocturnidad se estima como (1 - f_iluminada) * 29.53 d (una sola noche por lunacion, ILUSTRATIVO).
Modelo: criterios beneficio (iluminacion, visibilidad de la Tierra) y coste (pendiente, distancia al recurso, peligro) normalizados min-max sobre los sitios
que pasan el descarte; puntuacion = suma ponderada. Incertidumbre: pesos ~ Dirichlet(20 w) con semilla 109001 y 20000 sorteos.
Segunda via: la puntuacion es lineal en los pesos; con todo el peso en un criterio gana el sitio que lidera ese criterio (comprobacion de esquinas).
Unidades: pendiente [grados], iluminacion [%], distancia [km], visibilidad de la Tierra [% del tiempo], peligro [indice 0-1]. Tolerancia: 1e-12.
"""
from __future__ import annotations
import platform
import random

SINODICO = 29.53  # d (NASA/NSSDC)
CRIT = ["pendiente", "iluminacion", "distancia", "tierra", "peligro"]
SENT = {"pendiente": -1, "iluminacion": +1, "distancia": -1, "tierra": +1, "peligro": -1}
W0 = {"pendiente": 0.25, "iluminacion": 0.25, "distancia": 0.20, "tierra": 0.15, "peligro": 0.15}
SITIOS = {  # SINTETICO: pendiente deg, iluminacion %, distancia km, tierra %, peligro
    "A": (4.0, 62.0, 12.0, 55.0, 0.30),
    "B": (8.0, 85.0, 25.0, 40.0, 0.45),
    "C": (6.0, 70.0, 6.0, 20.0, 0.25),
    "D": (12.0, 90.0, 3.0, 65.0, 0.20),   # descartado por pendiente
    "E": (3.0, 45.0, 2.0, 70.0, 0.10),    # descartado por iluminacion
}
PEND_MAX, ILUM_MIN = 10.0, 50.0


def descartar(sitios):
    ok = {k: v for k, v in sitios.items() if v[0] <= PEND_MAX and v[1] >= ILUM_MIN}
    return ok, [k for k in sitios if k not in ok]


def normalizar(sitios):
    n = {k: {} for k in sitios}
    for j, c in enumerate(CRIT):
        col = [v[j] for v in sitios.values()]
        lo, hi = min(col), max(col)
        for k, v in sitios.items():
            x = (v[j] - lo) / (hi - lo) if hi > lo else 1.0
            n[k][c] = x if SENT[c] > 0 else 1.0 - x
    return n


def puntuar(norm, w):
    return {k: sum(w[c] * norm[k][c] for c in CRIT) for k in norm}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS; umbrales y pesos ILUSTRATIVOS; periodo sinodico 29.53 d (NASA/NSSDC)")
    ok, fuera = descartar(SITIOS)
    print("Descartados:", ", ".join(f"{k}({'pendiente' if SITIOS[k][0] > PEND_MAX else 'iluminacion'})" for k in fuera))
    assert abs(sum(W0.values()) - 1) < 1e-12
    norm = normalizar(ok)
    pts = puntuar(norm, W0)
    print(" sitio  puntuacion  noche_max [d]")
    for k, s in sorted(pts.items(), key=lambda kv: -kv[1]):
        print(f"   {k}    {s:9.4f}   {(1 - SITIOS[k][1] / 100) * SINODICO:9.2f}")
        assert -1e-12 <= s <= 1 + 1e-12
    rng = random.Random(109001)
    n = 20000
    gana = {k: 0 for k in ok}
    for _ in range(n):
        g = [rng.gammavariate(20 * W0[c], 1.0) for c in CRIT]
        t = sum(g)
        w = {c: x / t for c, x in zip(CRIT, g)}
        p = puntuar(norm, w)
        gana[max(p, key=p.get)] += 1
    print("Probabilidad de ser primero con pesos inciertos (20000 sorteos, semilla 109001):")
    for k in sorted(gana, key=lambda k: -gana[k]):
        print(f"   {k}: {gana[k] / n:.4f}")
    assert sum(gana.values()) == n
    # segunda via: esquinas
    print("Comprobacion de esquinas (todo el peso en un criterio):")
    for c in CRIT:
        w = {x: (1.0 if x == c else 0.0) for x in CRIT}
        p = puntuar(norm, w)
        mejor = max(p, key=p.get)
        lider = max(norm, key=lambda k: norm[k][c])
        print(f"   {c:11s} gana {mejor}")
        assert p[mejor] == p[lider]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
