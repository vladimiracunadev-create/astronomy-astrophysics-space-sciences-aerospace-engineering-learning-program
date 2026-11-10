#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C06: simulacion Monte Carlo de una campana de ordenes con retardo y perdida de paquetes.

Datos CONSULTADOS (2026-11-10): distancias Tierra-Marte 54.6e6 km (minima) y 401.4e6 km (maxima) (ficha de Marte, NASA/NSSDC);
c = 299 792 458 m/s (CODATA 2022, NIST); t = d/c se CALCULA aqui.
SINTETICOS (no medidos, semilla 98006): 10 ordenes por campana; ejecucion a bordo 120 s por orden; decision del operador 60 s;
margen de temporizador 30 s sobre el viaje de ida y vuelta; probabilidad de perdida por trayecto p (subida y bajada
independientes) en {0, 0.05, 0.20}; 4000 campanas por caso. Sistema de referencia: tiempo de operaciones [s] desde la primera orden.
Modelo: una orden tiene exito con q = (1-p)^2; un intento fallido cuesta T_to = 2 t + margen (se espera y se reenvia);
uno con exito cuesta T_ok = 2 t + ejecucion + decision. Esperanza por orden E = T_ok + (1/q - 1) T_to.
Comprobacion: la media Monte Carlo debe coincidir con N E a menos de 1.5 % (error tipico ~ 0.2 %). Solo biblioteca estandar.
"""
from __future__ import annotations
import math, platform, random

C = 299_792_458.0
D_MIN, D_MAX = 54.6e9, 401.4e9
N_ORD, T_EJEC, T_DEC, MARGEN = 10, 120.0, 60.0, 30.0
CAMPANAS = 4000


def una_campana(t, p, rng):
    total = 0.0
    for _ in range(N_ORD):
        while True:
            sube, baja = rng.random() >= p, rng.random() >= p
            if sube and baja:
                total += 2 * t + T_EJEC + T_DEC
                break
            total += 2 * t + MARGEN
    return total


def esperanza(t, p):
    q = (1 - p) ** 2
    return N_ORD * ((2 * t + T_EJEC + T_DEC) + (1 / q - 1) * (2 * t + MARGEN))


def percentil(xs, f):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(f * len(xs)))]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Distancias: ficha de Marte (NASA/NSSDC, 2026-11-10); c: CODATA 2022 (NIST). Resto SINTETICO, semilla 98006")
    rng = random.Random(98006)
    print(f"{N_ORD} ordenes por campana, {CAMPANAS} campanas por caso")
    print(f"{'caso':24s} {'p':>5s} {'media [h]':>10s} {'p50 [h]':>8s} {'p95 [h]':>8s} {'formula [h]':>12s} {'dif.':>7s}")
    for nombre, d in (("Marte, dist. minima", D_MIN), ("Marte, dist. maxima", D_MAX)):
        t = d / C
        for p in (0.0, 0.05, 0.20):
            xs = [una_campana(t, p, rng) for _ in range(CAMPANAS)]
            media = sum(xs) / len(xs)
            f = esperanza(t, p)
            dif = abs(media - f) / f
            print(f"{nombre:24s} {p:5.2f} {media / 3600:10.2f} {percentil(xs, 0.5) / 3600:8.2f} {percentil(xs, 0.95) / 3600:8.2f} {f / 3600:12.2f} {dif:7.2%}")
            assert dif < 0.015
            if p == 0.0:
                assert abs(media - f) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
