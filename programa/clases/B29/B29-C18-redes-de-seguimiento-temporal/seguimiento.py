#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C18: planificacion voraz de observaciones de seguimiento y completitud de una red.

Datos: ninguna constante fisica. Contexto: la red de Las Cumbres Observatory proyecta incluir dos telescopios de 2 m, hasta 17 de 1 m y hasta 23 de 40 cm para
observaciones en el dominio del tiempo (arXiv:1305.2437, resumen, consultado 2026-11-09). Los blancos (8 por instancia), las ventanas de visibilidad, las duraciones,
las prioridades y el numero de telescopios son ILUSTRATIVOS (sinteticos).
Modelo: cada blanco i tiene ventana [s_i, e_i] (horas de la noche), duracion d_i y peso w_i; un telescopio observa un blanco a la vez; planificacion voraz por peso/duracion
con colocacion en el primer instante libre dentro de la ventana; el optimo para la politica de colocacion se obtiene por busqueda exhaustiva de los ordenes (8! = 40320).
Monte Carlo (semilla fija) sobre 150 instancias aleatorias: razon voraz/optimo y efecto de anadir telescopios.
Supuestos: sin tiempos de apuntado ni cambios de filtro, un solo lugar. Validez: ilustrativa.
Tolerancia: el valor voraz nunca supera al optimo (cuatro reglas); con 3 telescopios la completitud media no es menor que con 1.
"""
from __future__ import annotations
import itertools
import platform
import random
import statistics
import sys

NOCHE = 10.0


def colocar(orden, tareas, ntel):
    libres = [0.0] * ntel
    valor = 0.0
    hechas = []
    for i in orden:
        s, e, d, w = tareas[i]
        mejor = None
        for k in range(ntel):
            ini = max(libres[k], s)
            if ini + d <= e and ini + d <= NOCHE:
                if mejor is None or ini < mejor[0]:
                    mejor = (ini, k)
        if mejor is not None:
            ini, k = mejor
            libres[k] = ini + d
            valor += w
            hechas.append(i)
    return valor, hechas


REGLAS = {
    "peso/duracion": lambda t, i: -t[i][3] / t[i][2],
    "ventana mas estrecha": lambda t, i: t[i][1] - t[i][0] - t[i][2],
    "primer fin": lambda t, i: t[i][1],
    "peso": lambda t, i: -t[i][3],
}


def voraz(tareas, ntel, regla="peso/duracion"):
    f = REGLAS[regla]
    orden = sorted(range(len(tareas)), key=lambda i: f(tareas, i))
    return colocar(orden, tareas, ntel)


def optimo(tareas, ntel):
    mejor = (0.0, [])
    for orden in itertools.permutations(range(len(tareas))):
        v = colocar(orden, tareas, ntel)
        if v[0] > mejor[0]:
            mejor = v
    return mejor


def instancia(rng, n=8):
    t = []
    for _ in range(n):
        s = rng.uniform(0, 7)
        d = rng.uniform(0.5, 2.5)
        e = min(NOCHE, s + d + rng.uniform(0.5, 3.0))
        t.append((s, e, d, rng.uniform(1, 10)))
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ejemplo = instancia(rng)
    print(f"{'blanco':>6} {'inicio [h]':>11} {'fin [h]':>8} {'duracion [h]':>13} {'peso':>6}")
    for i, (s, e, d, w) in enumerate(ejemplo):
        print(f"{i:6d} {s:11.2f} {e:8.2f} {d:13.2f} {w:6.2f}")
    vg, hg = voraz(ejemplo, 1)
    vo, ho = optimo(ejemplo, 1)
    print(f"un telescopio: valor voraz = {vg:.2f} (blancos {hg}) ; optimo = {vo:.2f} (blancos {ho}) ; razon = {vg / vo:.3f}")
    razones = {r: [] for r in REGLAS}
    comp1, comp3 = [], []
    for _ in range(150):
        t = instancia(rng)
        vo1, _ = optimo(t, 1)
        wt = sum(x[3] for x in t)
        for r in REGLAS:
            vg1, _ = voraz(t, 1, r)
            assert vg1 <= vo1 + 1e-9, "el valor voraz no puede superar al optimo"
            if vo1 > 0:
                razones[r].append(vg1 / vo1)
        comp1.append(voraz(t, 1)[0] / wt)
        comp3.append(voraz(t, 3)[0] / wt)
    print(f"{'regla voraz':<22} {'razon media':>12} {'razon minima':>13} {'instancias optimas':>19}")
    for r in REGLAS:
        rr = razones[r]
        print(f"{r:<22} {statistics.mean(rr):12.3f} {min(rr):13.3f} {sum(1 for x in rr if x > 0.9999):19d}")
    print(f"completitud ponderada media con 1 telescopio = {statistics.mean(comp1):.3f} ; con 3 telescopios = {statistics.mean(comp3):.3f}")
    assert statistics.mean(comp3) >= statistics.mean(comp1)
    print(f"{'telescopios':>11} {'completitud media':>18}")
    for nt in (1, 2, 3, 5, 8):
        c = statistics.mean(voraz(instancia(random.Random(1000 + i)), nt)[0] / sum(x[3] for x in instancia(random.Random(1000 + i))) for i in range(150))
        print(f"{nt:11d} {c:18.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
