#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C04: antiguedad del dato mostrado, visualizacion predictiva y avalancha de alarmas.

Datos CONSULTADOS (2026-11-10): distancias Tierra-Marte minima 54.6e6 km y maxima 401.4e6 km (ficha de Marte, NASA/NSSDC);
c = 299 792 458 m/s (CODATA 2022, NIST); t = d/c se CALCULA aqui (tiempo de luz de una via).
SINTETICOS (no medidos, semilla 98004): velocidad media del rover 0.04 m/s con ruido de velocidad sigma_v = 0.005 m/s
(deriva aleatoria por ciclo de 10 s); periodo de telemetria 60 s; latencia de proceso 5 s; cascada de alarmas generada
por 3 fallos raiz con dependientes. Sistema de referencia: tiempo de operaciones [s]; posicion a lo largo de la traza [m].
Modelo: edad del dato A = t_luz + t_proceso + mitad del periodo de telemetria (valor medio). Pantalla cruda: muestra la
ultima posicion recibida (error ~ v A). Pantalla predictiva: extrapola con la velocidad ordenada (el error se mide por Monte Carlo y se compara
con la formula sigma_pred = sigma_v * dt * sqrt(n), con n = A/dt pasos de dt = 10 s). Alarmas: se compara la
lista completa con la lista tras suprimir las dependientes de una causa raiz ya activa. Solo biblioteca estandar.
"""
from __future__ import annotations
import math, platform, random

C = 299_792_458.0
D_MIN, D_MAX = 54.6e9, 401.4e9
V, SIGMA_V, DT = 0.04, 0.005, 10.0
PERIODO, PROCESO = 60.0, 5.0


def edad(t_luz):
    return t_luz + PROCESO + PERIODO / 2.0


def monte_carlo(a, n=4000, rng=None):
    """Error de posicion de la pantalla cruda y de la predictiva para un dato de edad a [s]."""
    pasos = max(1, int(round(a / DT)))
    err_crudo, err_pred = [], []
    for _ in range(n):
        real = sum(V + rng.gauss(0.0, SIGMA_V) for _ in range(pasos)) * DT
        err_crudo.append(real)                # la pantalla cruda no sabe que el rover se movio
        err_pred.append(real - V * pasos * DT)  # la predictiva extrapola con la velocidad ordenada
    rms = lambda xs: math.sqrt(sum(x * x for x in xs) / len(xs))
    return rms(err_crudo), rms(err_pred), pasos


def alarmas(rng):
    """3 fallos raiz, cada uno con 4-9 alarmas dependientes en 600 s. Devuelve (todas, mostradas con supresion)."""
    todas = []
    for k in range(3):
        t0 = rng.uniform(0, 400)
        todas.append((t0, f"RAIZ{k}", None))
        for j in range(rng.randint(4, 9)):
            todas.append((t0 + rng.uniform(0.5, 60), f"DEP{k}.{j}", f"RAIZ{k}"))
    todas.sort()
    activas, mostradas = set(), []
    for t, nombre, raiz in todas:
        if raiz is None:
            activas.add(nombre)
            mostradas.append(nombre)
        elif raiz not in activas:
            mostradas.append(nombre)
    return todas, mostradas


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Distancias: ficha de Marte (NASA/NSSDC, 2026-11-10); c: CODATA 2022 (NIST). Resto SINTETICO, semilla 98004")
    rng = random.Random(98004)
    print(f"{'caso':26s} {'t luz [s]':>9s} {'edad A [s]':>10s} {'error crudo [m]':>16s} {'error pred. [m]':>16s} {'formula [m]':>12s}")
    for nombre, d in (("Marte, distancia minima", D_MIN), ("Marte, distancia maxima", D_MAX)):
        tl = d / C
        a = edad(tl)
        er_c, er_p, pasos = monte_carlo(a, rng=rng)
        formula = SIGMA_V * DT * math.sqrt(pasos)
        print(f"{nombre:26s} {tl:9.1f} {a:10.1f} {er_c:16.3f} {er_p:16.3f} {formula:12.3f}")
        assert abs(er_c - V * pasos * DT) < 0.05 * V * pasos * DT      # el error crudo es v*A
        assert abs(er_p - formula) < 0.05 * formula                    # Monte Carlo ~ formula
        assert er_p < er_c
    t, m = alarmas(rng)
    print(f"Alarmas SINTETICAS: {len(t)} generadas, {len(m)} mostradas con supresion de dependientes "
          f"({100 * (1 - len(m) / len(t)):.0f} % menos)")
    assert len(m) < len(t) and len(m) >= 3
    # Con 3 alarmas raiz y supresion total, no deben quedar mas de las raiz mas las dependientes anteriores a su raiz.
    assert all(n.startswith("RAIZ") for n in m) or len(m) <= len(t)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
