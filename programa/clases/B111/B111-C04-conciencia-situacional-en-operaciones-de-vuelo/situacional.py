#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C04: conciencia situacional (tres niveles) de una tripulacion SINTETICA.

Marco (Endsley 1995; solo metadatos y resumen consultados): nivel 1 percepcion de elementos, nivel 2 comprension de su
significado, nivel 3 proyeccion de su estado futuro. Una puntuacion tipo SAGAT congela la simulacion y pregunta por
cada nivel; aqui se SIMULA, no se mide.
Parametros SINTETICOS: cuatro tripulantes con (p1, p2|1, p3|2): probabilidades de acertar el nivel 1, el nivel 2
dado el 1 y el nivel 3 dado el 2. Probabilidad acumulada de acertar los tres niveles = p1 * p2|1 * p3|2.
Segunda via: Monte Carlo con semilla 114 y 100000 sondeos por tripulante; tolerancia 0.006.
Equipo: cobertura compartida = probabilidad de que al menos un tripulante tenga correcto el nivel 1 de un elemento
(independencia), y acuerdo = probabilidad de que dos tripulantes dados acierten ambos.
Degradacion: la probabilidad de que el dato siga vigente tras t segundos sin verificar es exp(-t/tau), con tau
SINTETICO = 600 s; el intervalo maximo para mantener >= 0.90 es t = -tau ln(0.90).
Supuestos: sondeos independientes, sin sesgo de respuesta, sin automatizacion que cambie la tasa de error.
"""
from __future__ import annotations
import math, platform, random

TRIP = {"T1": (0.97, 0.92, 0.85), "T2": (0.95, 0.88, 0.78), "T3": (0.90, 0.85, 0.70), "T4": (0.93, 0.80, 0.65)}
TAU = 600.0


def acumulada(p):
    return p[0] * p[1] * p[2]


def montecarlo(p, rng, m=100000):
    n1 = n2 = n3 = 0
    for _ in range(m):
        if rng.random() < p[0]:
            n1 += 1
            if rng.random() < p[1]:
                n2 += 1
                if rng.random() < p[2]:
                    n3 += 1
    return n1 / m, n2 / m, n3 / m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(114)
    print("Tripulacion SINTETICA; puntuacion simulada por nivel (acumulada: acierta todos los niveles previos)")
    print("  trip   L1 an.   L2 an.   L3 an.   L1 MC    L2 MC    L3 MC   dif. max")
    dmax = 0.0
    for nom, p in TRIP.items():
        a = (p[0], p[0] * p[1], acumulada(p))
        mc = montecarlo(p, rng)
        d = max(abs(x - y) for x, y in zip(a, mc))
        dmax = max(dmax, d)
        print(f"  {nom:4s} {a[0]:8.4f} {a[1]:8.4f} {a[2]:8.4f} {mc[0]:8.4f} {mc[1]:8.4f} {mc[2]:8.4f} {d:9.5f}")
    print(f"Diferencia maxima analitica/Monte Carlo = {dmax:.5f}")
    cob = 1.0
    for p in TRIP.values():
        cob *= 1.0 - p[0]
    cob = 1.0 - cob
    print(f"Cobertura del equipo en nivel 1 (al menos uno percibe el elemento) = {cob:.6f}")
    print(f"Acuerdo T1-T2 en nivel 1 = {TRIP['T1'][0] * TRIP['T2'][0]:.4f} ; T3-T4 = {TRIP['T3'][0] * TRIP['T4'][0]:.4f}")
    print(f"Degradacion SINTETICA con tau = {TAU:.0f} s:")
    print("  t sin verificar [s]  P(dato vigente)")
    for t in (0, 60, 120, 300, 600, 1200):
        print(f"  {t:19d}  {math.exp(-t / TAU):14.4f}")
    tmax = -TAU * math.log(0.90)
    print(f"Intervalo maximo de verificacion para >= 0.90: {tmax:.2f} s ; comprobacion exp(-t/tau) = {math.exp(-tmax / TAU):.4f}")
    assert dmax < 0.006
    assert abs(math.exp(-tmax / TAU) - 0.90) < 1e-12
    assert all(acumulada(p) < p[0] for p in TRIP.values())
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
