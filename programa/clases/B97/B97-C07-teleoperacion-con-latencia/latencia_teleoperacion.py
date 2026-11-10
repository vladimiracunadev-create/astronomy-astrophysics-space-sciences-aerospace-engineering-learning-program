#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C07: retardo de luz y duracion de una tarea teleoperada con el ciclo "mover y esperar".

Datos consultados (2026-11-10): distancia media Tierra-Luna 384.4e3 km (NASA/NSSDC); distancia Tierra-Marte minima 54.6e6 km y maxima 401.4e6 km (NASA/NSSDC);
velocidad de la luz c = 299 792 458 m/s (NIST, exacta); velocidad maxima de Perseverance ~152 m/h (NASA).
ILUSTRATIVOS (sinteticos): tarea de 40 pasos de 0.5 m, 6 s de movimiento por paso, 20 s de decision del operador por ciclo, bloques de k pasos con autonomia supervisada.
Modelo: retardo de ida t = d / c (propagacion en el vacio, sin retardos de procesamiento ni de red); ciclo = t_mov*k + 2 t + t_op; tiempo = (N/k) ciclo.
Segunda via: simulacion de la linea de tiempo de eventos frente a la forma cerrada (tolerancia 1e-9 s).
Unidades SI; las distancias son las de las fichas (rango de la distancia Tierra-Marte), no una geometria de mision concreta.
"""
from __future__ import annotations
import platform

C = 299792458.0                        # m/s (NIST)
DIST_KM = {"Luna (media)": 384.4e3, "Marte (minima)": 54.6e6, "Marte (maxima)": 401.4e6}   # NASA/NSSDC
N, PASO, T_MOV, T_OP = 40, 0.5, 6.0, 20.0                                                 # ILUSTRATIVOS
V_ROVER = 152.0 / 3600.0               # m/s (NASA)


def retardo(d_km):
    return d_km * 1e3 / C


def forma_cerrada(t, k):
    return (N / k) * (T_MOV * k + 2 * t + T_OP)


def simulada(t, k):
    reloj = 0.0
    for _ in range(N // k):
        reloj += T_MOV * k          # el robot ejecuta el bloque
        reloj += t                  # la telemetria viaja a la Tierra
        reloj += T_OP               # el operador decide
        reloj += t                  # la orden viaja al robot
    return reloj


def calc():
    r = {}
    for nombre, d in DIST_KM.items():
        t = retardo(d)
        r[nombre] = dict(t=t, rtt=2 * t, k1=forma_cerrada(t, 1), k10=forma_cerrada(t, 10), k40=forma_cerrada(t, 40), ciega=V_ROVER * 2 * t)
    dif = max(abs(forma_cerrada(v["t"], k) - simulada(v["t"], k)) for v in r.values() for k in (1, 2, 4, 5, 8, 10, 20, 40))
    ideal = N * T_MOV
    return dict(r=r, dif=dif, ideal=ideal, t_luna=r["Luna (media)"]["t"], t_min=r["Marte (minima)"]["t"], t_max=r["Marte (maxima)"]["t"],
                k1_luna=r["Luna (media)"]["k1"], k1_marte_max=r["Marte (maxima)"]["k1"], k10_marte_max=r["Marte (maxima)"]["k10"],
                k40_marte_max=r["Marte (maxima)"]["k40"], ciega_max=r["Marte (maxima)"]["ciega"], rtt_max_min=r["Marte (maxima)"]["rtt"] / 60.0,
                rtt_luna=r["Luna (media)"]["rtt"], rtt_min_min=r["Marte (minima)"]["rtt"] / 60.0, rel1=r["Marte (maxima)"]["k1"] / ideal)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"c = {C:.0f} m/s; tarea ILUSTRATIVA: {N} pasos de {PASO} m, {T_MOV} s de movimiento por paso, {T_OP} s de decision por ciclo; tiempo sin latencia = {r['ideal']:.0f} s")
    print(" enlace              ida [s]   ida y vuelta [s]  k=1 [min]  k=10 [min]  k=40 [min]  avance ciego a 152 m/h [m]")
    for n, v in r["r"].items():
        print(f"{n:17s} {v['t']:9.3f} {v['rtt']:17.3f} {v['k1']/60:10.2f} {v['k10']/60:11.2f} {v['k40']/60:11.2f} {v['ciega']:16.2f}")
    print(f"Diferencia maxima entre forma cerrada y linea de tiempo simulada = {r['dif']:.2e} s")
    assert r["dif"] < 1e-9 and r["t_min"] < r["t_max"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
