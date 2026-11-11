#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B110-C04: priorizacion de acciones cuando hay varias fallas simultaneas.

CONSULTADO (2026-11-10): orden de prioridad de decisiones (1) seguridad de la tripulacion, (2) seguridad del vehiculo, (3) exito de la mision;
las acciones de emergencia pueden sacrificar sistemas, funciones o incluso volumenes del modulo para mantener a salvo a la tripulacion; la secuencia
inicial Warn-Gather-Work; la tripulacion lidera la respuesta sin depender del control de mision (Tobias y McMillan, SpaceOps 2023, NASA JSC).
ILUSTRATIVOS (sinteticos, no son fallas ni tiempos reales): las fallas del caso, sus plazos (minutos hasta que la consecuencia ocurre si no se atiende)
y su esfuerzo (minutos de trabajo de UN equipo de respuesta que atiende de a una), y los escenarios aleatorios (semilla 110).
Modelo: una sola cola de trabajo; una falla atendida despues de su plazo «se consuma» (perdida). Perdida lexicografica (crew, vehiculo, mision):
primero se minimizan las perdidas de nivel tripulacion, luego las de vehiculo, luego las de mision. Optimo por fuerza bruta (n! ordenes).
Reglas comparadas: FIFO, severidad (nivel y despues orden de llegada), plazo mas cercano (EDF), nivel y despues EDF.
Tolerancia: el optimo se verifica contra un segundo algoritmo (programacion dinamica sobre subconjuntos) con igualdad exacta.
Contenido educativo: NO es un procedimiento ni una guia de decision real.
"""
from __future__ import annotations
import itertools, platform, random

NIVEL = {"T": 0, "V": 1, "M": 2}  # tripulacion, vehiculo, mision
# (nombre, nivel, plazo [min], esfuerzo [min]) en orden de llegada de la alarma
CASO = [
    ("F1 radiador (lazo termico)", "V", 90, 30),
    ("F2 humo en un rack", "T", 15, 10),
    ("F3 comunicaciones", "M", 240, 25),
    ("F4 fuga lenta de aire", "T", 55, 20),
    ("F5 filtro de CO2 fuera de servicio", "T", 120, 35),
    ("F6 experimento detenido", "M", 600, 15),
]


def perdidas(orden, fallas):
    """Tupla (perdidas T, perdidas V, perdidas M) para un orden de atencion."""
    t = 0.0
    out = [0, 0, 0]
    for i in orden:
        _, niv, plazo, esf = fallas[i]
        t += esf
        if t > plazo:
            out[NIVEL[niv]] += 1
    return tuple(out)


def optimo_fuerza_bruta(fallas):
    mejor, ordenes = None, []
    for p in itertools.permutations(range(len(fallas))):
        l = perdidas(p, fallas)
        if mejor is None or l < mejor:
            mejor, ordenes = l, [p]
        elif l == mejor:
            ordenes.append(p)
    return mejor, ordenes


def optimo_dp(fallas):
    """Segunda via: programacion dinamica sobre subconjuntos (tupla lexicografica minima)."""
    n = len(fallas)
    # f[mask] = (perdidas minimas, tiempo acumulado) atendiendo exactamente las fallas de mask en algun orden; el tiempo total solo depende de mask
    tiempo = [0.0] * (1 << n)
    for m in range(1, 1 << n):
        j = (m & -m).bit_length() - 1
        tiempo[m] = tiempo[m & (m - 1)] + fallas[j][3]
    f = {0: (0, 0, 0)}
    for m in range(1, 1 << n):
        mejor = None
        for j in range(n):
            if m >> j & 1:
                prev = f[m ^ (1 << j)]
                l = list(prev)
                if tiempo[m] > fallas[j][2]:
                    l[NIVEL[fallas[j][1]]] += 1
                l = tuple(l)
                if mejor is None or l < mejor:
                    mejor = l
        f[m] = mejor
    return f[(1 << n) - 1]


def regla(nombre, fallas):
    idx = list(range(len(fallas)))
    if nombre == "FIFO":
        return idx
    if nombre == "severidad":
        return sorted(idx, key=lambda i: (NIVEL[fallas[i][1]], i))
    if nombre == "EDF":
        return sorted(idx, key=lambda i: (fallas[i][2], i))
    if nombre == "nivel+EDF":
        return sorted(idx, key=lambda i: (NIVEL[fallas[i][1]], fallas[i][2], i))
    raise ValueError(nombre)


REGLAS = ["FIFO", "severidad", "EDF", "nivel+EDF"]


def escenario_aleatorio(rng, n):
    f = []
    for i in range(n):
        niv = rng.choices("TVM", weights=[0.4, 0.3, 0.3])[0]
        esf = rng.choice([5, 10, 15, 20, 30, 40])
        plazo = rng.choice([10, 20, 30, 45, 60, 90, 120, 240])
        f.append((f"F{i+1}", niv, plazo, esf))
    return f


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Caso ILUSTRATIVO de 6 fallas simultaneas (nivel T = tripulacion, V = vehiculo, M = mision; plazo y esfuerzo en min):")
    for i, (n, niv, pl, es) in enumerate(CASO):
        print(f"  {i}: {n:38s} nivel {niv}  plazo {pl:4d}  esfuerzo {es:3d}")
    mejor, ords = optimo_fuerza_bruta(CASO)
    print(f"Optimo por fuerza bruta (720 ordenes): perdidas (T, V, M) = {mejor}; {len(ords)} ordenes optimos; el primero: {ords[0]}")
    dp = optimo_dp(CASO)
    print(f"Optimo por programacion dinamica: {dp} (coincide: {dp == mejor})")
    assert dp == mejor
    print("Reglas simples sobre el caso:")
    for r in REGLAS:
        o = regla(r, CASO)
        print(f"  {r:10s} orden {o}  perdidas (T, V, M) = {perdidas(o, CASO)}")
    # sensibilidad a un error de estimacion de plazos: todos los plazos x 0,7, orden elegido con los plazos originales
    o = regla("nivel+EDF", CASO)
    c07 = [(n, v, p * 0.7, e) for n, v, p, e in CASO]
    print(f"Sensibilidad: orden nivel+EDF con plazos reales 30 % menores: perdidas {perdidas(o, c07)}; optimo con esos plazos {optimo_fuerza_bruta(c07)[0]}")
    # experimento aleatorio
    rng = random.Random(110)
    n_esc, n = 3000, 6
    estad = {r: [0, 0, 0] for r in REGLAS}  # [veces optima, perdidas T extra totales, veces con perdida T peor que el optimo]
    total_T_opt = 0
    for _ in range(n_esc):
        f = escenario_aleatorio(rng, n)
        opt, _ = optimo_fuerza_bruta(f)
        total_T_opt += opt[0]
        for r in REGLAS:
            l = perdidas(regla(r, f), f)
            if l == opt:
                estad[r][0] += 1
            estad[r][1] += l[0] - opt[0]
            if l[0] > opt[0]:
                estad[r][2] += 1
    print(f"Experimento: {n_esc} escenarios aleatorios de {n} fallas (semilla 110); perdidas T del optimo en total = {total_T_opt}")
    print("  regla       optima en   perdidas T extra (total)   escenarios con perdida T peor que el optimo")
    for r in REGLAS:
        print(f"  {r:10s} {100*estad[r][0]/n_esc:8.1f} %  {estad[r][1]:14d}  {estad[r][2]:26d}")
    assert perdidas(regla("nivel+EDF", CASO), CASO) >= mejor
    assert estad["EDF"][0] >= estad["FIFO"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
