#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B94-C05: repartir un enlace escaso entre tres clases de servicio (FIFO, prioridad estricta, reparto ponderado).

Consultado (2026-11-10, CCSDS 734.2-B-1, sept. 2015): el parametro de clase de servicio del protocolo de paquetes toma uno de tres valores:
'bulk', 'normal' o 'expedited'; la prioridad es un valor de 0 a 2 (0 = bulk, 1 = normal, 2 = expedited), con mayor valor = mayor urgencia;
dentro de 'expedited' puede haber un numero ordinal que refina la urgencia. NO consultado: como se planifica la cola en una implementacion
concreta (aqui hay tres disciplinas de cola propias y didacticas).
Datos SINTETICOS: contactos identicos de C = 30 MB; paquetes de 0.2 MB (expedited), 1 MB (normal) y 4 MB (bulk); llegadas de Poisson por
contacto (semilla 94007); reparto de la carga ofrecida 30 % / 50 % / 20 %; 2000 contactos; cargas ofrecidas de 0.8, 1.2 y 1.5 veces C.
Modelo fluido: un paquete puede servirse en varios contactos (se admite fragmentacion); las llegadas ocurren al inicio del contacto y pueden
servirse en el mismo. Retardo = contacto de finalizacion - contacto de llegada (en contactos). Pesos del reparto ponderado: 4 : 2 : 1.
Segunda via: conservacion (llegado = entregado + en cola) y propiedad de no ociosidad (el total entregado es igual en las tres disciplinas).
Tolerancias: 1e-6 MB.
"""
from __future__ import annotations
import math, platform, random
from collections import deque

C = 30.0
TAM = {"E": 0.2, "N": 1.0, "B": 4.0}
PARTE = {"E": 0.3, "N": 0.5, "B": 0.2}
PESO = {"E": 4.0, "N": 2.0, "B": 1.0}
NC = 2000


def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def llegadas(carga):
    rng = random.Random(94007)
    out = []
    for _ in range(NC):
        out.append({c: poisson(rng, carga * C * PARTE[c] / TAM[c]) for c in "ENB"})
    return out


def simula(politica, arr):
    colas = {c: deque() for c in "ENB"}  # [contacto_llegada, MB restantes]
    fifo = deque()
    retardos = {c: [] for c in "ENB"}
    entregado = {c: 0.0 for c in "ENB"}
    llegado = {c: 0.0 for c in "ENB"}

    def sirve(q, cap, clase, j):
        usado = 0.0
        while q and cap - usado > 1e-12:
            item = q[0]
            x = min(item[1], cap - usado)
            item[1] -= x
            usado += x
            entregado[clase if clase else item[2]] += x
            if item[1] <= 1e-12:
                q.popleft()
                retardos[clase if clase else item[2]].append(j - item[0])
        return usado

    for j in range(NC):
        for c in "ENB":
            for _ in range(arr[j][c]):
                llegado[c] += TAM[c]
                colas[c].append([j, TAM[c]])
                fifo.append([j, TAM[c], c])
        if politica == "FIFO":
            sirve(fifo, C, None, j)
        elif politica == "PRIO":
            cap = C
            for c in "ENB":
                cap -= sirve(colas[c], cap, c, j)
        else:  # reparto ponderado, sin ociosidad: llenado por pesos con redistribucion
            cap = C
            activos = [c for c in "ENB" if colas[c]]
            while activos and cap > 1e-12:
                tw = sum(PESO[c] for c in activos)
                gasto = 0.0
                for c in list(activos):
                    gasto += sirve(colas[c], cap * PESO[c] / tw, c, j)
                cap -= gasto
                activos = [c for c in activos if colas[c]]
                if gasto <= 1e-12:
                    break
    if politica == "FIFO":
        cola = {c: sum(x[1] for x in fifo if x[2] == c) for c in "ENB"}
    else:
        cola = {c: sum(x[1] for x in colas[c]) for c in "ENB"}
    return retardos, entregado, llegado, cola


def media(v):
    return sum(v) / len(v) if v else float("nan")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Capacidad por contacto C = {C} MB; reparto de carga E/N/B = {PARTE}; pesos = {PESO}; {NC} contactos (SINTETICO)")
    for carga in (0.8, 1.2, 1.5):
        arr = llegadas(carga)
        print(f"\nCarga ofrecida = {carga} C  ({carga * C:.1f} MB por contacto)")
        print(" disciplina   clase  retardo medio [contactos]  entregado [%]  en cola al final [MB]")
        totales = {}
        for pol in ("FIFO", "PRIO", "WFQ"):
            ret, ent, lle, cola = simula(pol, arr)
            for c in "ENB":
                print(f" {pol:10s}     {c}        {media(ret[c]):9.2f}              {100 * ent[c] / lle[c]:6.1f}        {cola[c]:9.1f}")
                assert abs(lle[c] - ent[c] - cola[c]) < 1e-6
            totales[pol] = sum(ent.values())
        assert abs(totales["FIFO"] - totales["PRIO"]) < 1e-6 and abs(totales["FIFO"] - totales["WFQ"]) < 1e-6
        print(f" total entregado (igual en las tres disciplinas) = {totales['FIFO']:.1f} MB; maximo posible {NC * C:.0f} MB")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
