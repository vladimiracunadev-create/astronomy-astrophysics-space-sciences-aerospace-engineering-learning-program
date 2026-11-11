#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C05: calendarizacion de siembras escalonadas para cubrir una demanda diaria de hortalizas frescas.

DATO CONSULTADO: 78 g de masa fresca por planta de lechuga en un sistema NFT en el experimento de Monje et al. (2019,
NASA/KSC, 300 umol m-2 s-1, 3000 umol/mol de CO2, 40 % de humedad, 23 C; promedio de n = 3) y 100 g en condiciones de menos CO2 y
mas humedad (sensibilidad). TODO LO DEMAS ES SINTETICO O DE DISENO ILUSTRATIVO (no es una recomendacion nutricional): tripulacion de
4 personas, 100 g de hortaliza fresca por persona y dia, ciclo de 35 dias de siembra a cosecha, vida util de 5 dias tras la
cosecha, 0.04 m2 por planta, y fallos aleatorios (probabilidad 10 % por lote de perder el 50 %; semilla 115).
Unidades: g, dia, m2. Metodo: cada Delta dias se siembra un lote de n plantas y se cosecha un lote igual; el inventario se
consume por antiguedad (FIFO) y lo que supera la vida util se descarta. Verificacion: sin fallos, la cobertura simulada debe
coincidir con la analitica min(1, vida util / Delta); el area se calcula de forma cerrada. Solo numpy y la biblioteca estandar.
"""
from __future__ import annotations
import math
import platform
import numpy as np

TRIP, G_PERSONA, CICLO, VIDA, A_PLANTA = 4, 100.0, 35, 5, 0.04
DEMANDA = TRIP * G_PERSONA           # g/dia
P_FALLO, PERDIDA = 0.10, 0.50
DIAS = 400


def plan(delta, rend, margen=1.0):
    n = math.ceil(margen * DEMANDA * delta / rend)
    lotes = math.ceil(CICLO / delta)
    return n, lotes, n * lotes, n * lotes * A_PLANTA


def simular(delta, rend, margen, p_fallo, rng):
    n, _, _, _ = plan(delta, rend, margen)
    inventario = []                   # [masa, edad]
    cubiertos, total, descartado, cosechado = 0, 0, 0.0, 0.0
    for dia in range(DIAS):
        if dia >= CICLO and (dia - CICLO) % delta == 0:
            perdida = PERDIDA if rng.random() < p_fallo else 0.0
            masa = n * rend * (1 - perdida)
            inventario.append([masa, 0])
            cosechado += masa
        necesidad = DEMANDA
        for lote in inventario:
            tomar = min(lote[0], necesidad)
            lote[0] -= tomar
            necesidad -= tomar
        if dia >= CICLO + delta:      # se evalua despues del arranque
            total += 1
            cubiertos += necesidad < 1e-9
        nuevo = []
        for lote in inventario:
            lote[1] += 1
            if lote[1] >= VIDA:
                descartado += lote[0]
            elif lote[0] > 1e-9:
                nuevo.append(lote)
        inventario = nuevo
    return cubiertos / total, descartado / max(cosechado, 1e-9)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATO CONSULTADO: 78 g/planta (Monje et al., 2019); RESTO SINTETICO/DE DISENO: 4 personas, 100 g/persona/dia, ciclo 35 d, vida util 5 d")
    print(f"Demanda = {DEMANDA:.0f} g/dia; rendimiento nominal = 78 g/planta -> {DEMANDA/78:.2f} plantas/dia")
    print("Plan de siembra escalonada (margen 1.0, 78 g/planta)")
    print("   Delta[d]  plantas/lote  lotes en cultivo  plantas totales  area[m2]  cobertura sim sin fallos[%]  analitica[%]")
    for delta in (1, 3, 7, 14):
        n, lotes, pl, area = plan(delta, 78.0)
        sim, _ = simular(delta, 78.0, 1.0, 0.0, np.random.default_rng(115))
        ana = min(1.0, VIDA / delta)
        print(f"   {delta:8d}  {n:12d}  {lotes:16d}  {pl:15d}  {area:8.2f}  {sim*100:27.1f}  {ana*100:11.1f}")
        assert abs(sim - ana) < 0.02, "cobertura sin fallos fuera de tolerancia"
    print("Monte Carlo con fallos (300 repeticiones de 400 dias, semilla 115): cobertura y descarte segun el margen de plantas")
    print("   Delta[d]  margen  cobertura media[%]  descarte[%]  area[m2]")
    elegido = {}
    for delta in (1, 3, 7):
        for margen in (1.0, 1.1, 1.2, 1.3, 1.5):
            cob, desc = [], []
            for k in range(300):
                c, d = simular(delta, 78.0, margen, P_FALLO, np.random.default_rng(115 + k))
                cob.append(c)
                desc.append(d)
            area = plan(delta, 78.0, margen)[3]
            print(f"   {delta:8d}  {margen:6.1f}  {np.mean(cob)*100:18.1f}  {np.mean(desc)*100:11.1f}  {area:8.2f}")
            if np.mean(cob) >= 0.95 and delta not in elegido:
                elegido[delta] = (margen, area)
    print("Margen minimo ensayado con cobertura media >= 95 %: " +
          ", ".join(f"Delta {d} d -> x{m:.1f} ({a:.1f} m2)" for d, (m, a) in elegido.items()))
    print("Sensibilidad al rendimiento por planta (Delta = 1 d, margen 1.0)")
    for rend in (50.0, 78.0, 100.0):
        n, lotes, pl, area = plan(1, rend)
        print(f"   {rend:5.0f} g/planta -> {n:2d} plantas/lote, {pl:3d} plantas, {area:5.2f} m2")
    n1 = plan(1, 78.0)[3]
    assert abs(n1 - 8.4) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
