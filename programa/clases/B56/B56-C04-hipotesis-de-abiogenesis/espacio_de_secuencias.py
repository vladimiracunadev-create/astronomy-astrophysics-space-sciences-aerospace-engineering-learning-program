#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C04: espacio de secuencias y fraccion explorada por un ambiente.

Datos: N_A de NIST (CODATA 2022, consultado 2026-11-09). Volumen del ambiente, concentracion,
tiempo y numero de ciclos son SINTETICOS e ILUSTRATIVOS (una charca hipotetica); no describen
ninguna Tierra primitiva real.
Modelo: el numero de secuencias de longitud L con alfabeto de 4 letras es M = 4^L. Si se
producen N secuencias al azar, uniformes e independientes, la fraccion esperada del espacio
explorado es 1 - (1 - 1/M)^N ~ 1 - exp(-N/M).
Supuestos: muestreo uniforme (en la realidad hay sesgos quimicos); sin seleccion.
Validez: ordenes de magnitud. Tolerancia: la simulacion con semilla 12345 coincide con la
forma cerrada con error relativo < 0,02.
"""
from __future__ import annotations
import math
import platform
import random
import sys

NA = 6.02214076e23


def fraccion_esperada(M, N):
    return -math.expm1(N * math.log1p(-1.0 / M)) if M > 1 else 1.0


def simulacion(M, N, semilla=12345):
    rng = random.Random(semilla)
    vistos = set()
    for _ in range(N):
        vistos.add(rng.randrange(M))
    return len(vistos) / M


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: Monte Carlo frente a forma cerrada (espacio pequeno)
    M, N = 20000, 30000
    f_c, f_s = fraccion_esperada(M, N), simulacion(M, N)
    print(f"M={M}, N={N}: cerrada={f_c:.4f} ; simulada={f_s:.4f}")
    assert abs(f_s - f_c) / f_c < 0.02
    # Prueba 2: aproximacion exponencial
    assert abs(fraccion_esperada(M, N) - (1 - math.exp(-N / M))) < 1e-4
    # Caso ilustrativo: charca de 1e3 m^3 con 1e-6 mol/L de oligomeros, 1e4 ciclos de renovacion
    vol_l = 1e3 * 1e3
    n_por_ciclo = 1e-6 * vol_l * NA
    N_total = n_por_ciclo * 1e4
    print(f"Moleculas por ciclo = {n_por_ciclo:.2e} ; totales = {N_total:.2e}")
    for L in (20, 30, 40, 60, 100):
        log10_M = L * math.log10(4)
        log10_frac = math.log10(N_total) - log10_M
        frac = 1.0 if log10_frac > 0 else 10 ** log10_frac
        print(f"L={L:3d}: log10(M)={log10_M:6.1f} ; fraccion explorada ~ {frac:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
