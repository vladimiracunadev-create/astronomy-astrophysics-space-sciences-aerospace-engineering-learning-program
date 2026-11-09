#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C09: redundancia y disponibilidad de un servicio durante un evento.

Datos: ninguna constante fisica. La probabilidad de falla de una unidad durante el evento (0.3), el numero de unidades (1 a 4), la tasa de fallas (1/2000 h), el tiempo de reparacion (24 h),
la duracion del evento (48 h) y la semilla fija son ILUSTRATIVOS (sinteticos); no representan ningun sistema real.
Modelo: (1) redundancia paralela con fallas independientes: P(servicio) = 1 - p^n, frente a Monte Carlo (200 000); (2) redundancia con un respaldo comun (factor beta de causa comun): P = 1 - [beta p + (1 - beta) p^n];
(3) disponibilidad estacionaria A = MTBF/(MTBF + MTTR) y numero de eventos de falla esperados en el periodo; (4) costo marginal de cada unidad adicional frente a la mejora de P.
Supuestos: independencia (salvo beta), tasas constantes. Validez: ilustrativa.
Tolerancia: Monte Carlo dentro de 4 errores estandar de la formula.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    p, rng = 0.3, random.Random(20261109)
    nrep = 200000
    print(f"{'n':>2} {'P = 1 - p^n':>12} {'Monte Carlo':>12} {'desviacion [errores]':>21} {'ganancia marginal':>18}")
    prev = 0.0
    for n in range(1, 5):
        pf = 1 - p ** n
        k = sum(1 for _ in range(nrep) if any(rng.random() > p for _ in range(n)))
        mc = k / nrep
        e = math.sqrt(pf * (1 - pf) / nrep)
        print(f"{n:2d} {pf:12.5f} {mc:12.5f} {abs(mc - pf) / e:21.2f} {pf - prev:18.5f}")
        assert abs(mc - pf) < 4 * e
        prev = pf
    print(f"{'beta':>5} " + "".join(f"{'n = ' + str(n):>10}" for n in range(1, 5)))
    for beta in (0.0, 0.1, 0.3):
        print(f"{beta:5.2f} " + "".join(f"{1 - (beta * p + (1 - beta) * p ** n):10.5f}" for n in range(1, 5)))
    mtbf, mttr, dur = 2000.0, 24.0, 48.0
    a = mtbf / (mtbf + mttr)
    print(f"disponibilidad A = MTBF/(MTBF + MTTR) = {a:.5f} ; fallas esperadas en {dur:.0f} h = {dur / mtbf:.3f} ; probabilidad de al menos una = {1 - math.exp(-dur / mtbf):.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
