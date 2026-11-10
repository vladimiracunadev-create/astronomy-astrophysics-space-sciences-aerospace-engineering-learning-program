#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C05: distancia de frenado de un reflejo a bordo frente a la intervencion desde Tierra, e histeresis.

Datos CONSULTADOS (2026-11-10): distancias Tierra-Marte 54.6e6 km (minima) y 401.4e6 km (maxima) (ficha de Marte, NASA/NSSDC);
c = 299 792 458 m/s (CODATA 2022, NIST); t = d/c se CALCULA aqui.
SINTETICOS (no medidos): velocidad 0.04 m/s; desaceleracion 0.10 m/s2; ciclo del reflejo 0.1 s (10 Hz) mas latencia de
sensor 0.2 s; alcance de deteccion de peligros 3.0 m; tiempo de decision en tierra 600 s; sensor de distancia con ruido
gaussiano sigma = 0.05 m (semilla 98005). Sistema de referencia: distancia recorrida por el rover [m] desde el instante en que
aparece el peligro; tiempo de reloj de operaciones [s].
Modelo: d_frenado = v (t_sensor + t_ciclo) + v^2 / (2 a). Sin reflejo: d = v (2 t_luz + t_decision) + v^2/(2a).
Velocidad maxima admisible v_max: raiz positiva de v tau + v^2/(2a) = R_deteccion (solucion cerrada, contrastada por biseccion con
tolerancia 1e-9). Histeresis: umbral de parada 1.0 m con banda de 0.2 m frente a umbral unico. Solo biblioteca estandar.
"""
from __future__ import annotations
import math, platform, random

C = 299_792_458.0
D_MIN, D_MAX = 54.6e9, 401.4e9
V, A = 0.04, 0.10
T_SENSOR, T_CICLO, R_DET, T_DEC = 0.2, 0.1, 3.0, 600.0
TAU = round(T_SENSOR + T_CICLO, 6)


def d_frenado(v, tau=TAU, a=A):
    return v * tau + v * v / (2.0 * a)


def v_max(r, tau=TAU, a=A):
    # a-resolver: v^2/(2a) + tau v - r = 0
    return -a * tau + math.sqrt((a * tau) ** 2 + 2.0 * a * r)


def v_max_biseccion(r, tau=TAU, a=A):
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if d_frenado(mid, tau, a) < r:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def conmutaciones(rng, histeresis):
    """Cuenta cambios de estado PARAR/MARCHAR con un obstaculo estacionario a 1.0 m medido con ruido."""
    estado, cambios = "MARCHAR", 0
    for _ in range(2000):
        z = 1.0 + rng.gauss(0.0, 0.05)
        if histeresis:
            nuevo = "PARAR" if z < 0.9 else ("MARCHAR" if z > 1.1 else estado)
        else:
            nuevo = "PARAR" if z < 1.0 else "MARCHAR"
        if nuevo != estado:
            cambios += 1
            estado = nuevo
    return cambios


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Distancias: ficha de Marte (NASA/NSSDC, 2026-11-10); c: CODATA 2022 (NIST). Resto SINTETICO, semilla 98005")
    print(f"Reflejo a bordo (v = {V} m/s, tau = {TAU} s, a = {A} m/s2): distancia de frenado = {d_frenado(V):.4f} m (alcance {R_DET} m)")
    for nombre, d in (("Marte, distancia minima", D_MIN), ("Marte, distancia maxima", D_MAX)):
        tl = d / C
        sin = V * (2 * tl + T_DEC) + V * V / (2 * A)
        print(f"{nombre}: t luz {tl:.1f} s; sin reflejo recorre {sin:.1f} m antes de parar ({sin / R_DET:.1f} veces el alcance)")
        assert sin > R_DET > d_frenado(V)
    vm, vb = v_max(R_DET), v_max_biseccion(R_DET)
    print(f"Velocidad maxima admisible con reflejo para alcance {R_DET} m: {vm:.4f} m/s (biseccion {vb:.4f} m/s)")
    assert abs(vm - vb) < 1e-9 and d_frenado(vm) <= R_DET + 1e-9
    for tau in (0.3, 1.0, 5.0):
        print(f"  tau = {tau:4.1f} s -> v_max = {v_max(R_DET, tau):.4f} m/s")
    rng = random.Random(98005)
    sin_h, con_h = conmutaciones(rng, False), conmutaciones(rng, True)
    print(f"Conmutaciones PARAR/MARCHAR en 2000 ciclos con sensor ruidoso: umbral unico {sin_h}, con histeresis {con_h}")
    assert con_h * 10 < sin_h
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
