#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C01: velocidad de la luz en un medio, camino optico y principio de Fermat.

Datos: c = 299 792 458 m/s (exacta, NIST CODATA 2022, tabla allascii.txt, consultada el 2026-11-09). Los indices de refraccion (aire 1,0003,
agua 1,333, vidrio 1,517) y las distancias son ILUSTRATIVOS, tipicos de libro, no medidos ni consultados.
Modelo: v = c/n; camino optico = suma de n_i d_i; el tiempo de transito entre dos puntos a traves de una interfaz plana se minimiza numericamente
(busqueda ternaria, principio de Fermat) y el angulo obtenido se compara con la ley de Snell n1 sen t1 = n2 sen t2.
Supuestos: medios homogeneos e isotropos, interfaz plana, rayos (sin difraccion). Validez: optica geometrica, objetos mucho mayores que la longitud de onda.
Tolerancia: angulo de Fermat frente a Snell, 1e-6 rad; tiempos a 1e-12 relativo.
"""
from __future__ import annotations
import math, platform, sys

C = 299_792_458.0  # m/s, exacta


def tiempo(x, a, b, d, n1, n2):
    """Tiempo de transito: A=(0,a) sobre la interfaz y=0, B=(d,-b) debajo; el rayo cruza en (x,0)."""
    return (n1 * math.hypot(x, a) + n2 * math.hypot(d - x, b)) / C


def fermat(a, b, d, n1, n2):
    lo, hi = 0.0, d
    for _ in range(200):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if tiempo(m1, a, b, d, n1, n2) < tiempo(m2, a, b, d, n1, n2):
            hi = m2
        else:
            lo = m1
    x = 0.5 * (lo + hi)
    return x, math.atan2(x, a), math.atan2(d - x, b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"c = {C:.0f} m/s (exacta, NIST)")
    medios = [("vacio", 1.0), ("aire", 1.0003), ("agua", 1.333), ("vidrio", 1.517)]
    print(f"{'medio':>7} {'n':>7} {'v [km/s]':>12} {'t en 1 m [ns]':>14}")
    for nom, n in medios:
        v = C / n
        print(f"{nom:>7} {n:7.4f} {v/1e3:12.1f} {1/v*1e9:14.5f}")
        assert abs(v * n - C) < 1e-6
    # camino optico de una pila vidrio+agua+aire
    capas = [(1.517, 0.010), (1.333, 0.050), (1.0003, 0.200)]
    opl = sum(n * d for n, d in capas)
    t_pila = sum(n * d / C for n, d in capas)
    print(f"camino optico de la pila = {opl*1e3:.4f} mm ; tiempo = {t_pila*1e12:.4f} ps ; OPL/c = {opl/C*1e12:.4f} ps")
    assert abs(t_pila - opl / C) < 1e-24
    # Fermat frente a Snell
    n1, n2 = 1.0003, 1.517
    a, b, d = 0.30, 0.20, 0.40
    x, t1, t2 = fermat(a, b, d, n1, n2)
    snell = n1 * math.sin(t1) - n2 * math.sin(t2)
    print(f"Fermat: cruce x = {x*1e3:.4f} mm ; t1 = {math.degrees(t1):.4f} deg ; t2 = {math.degrees(t2):.4f} deg")
    t2_snell = math.asin(n1 * math.sin(t1) / n2)
    print(f"Snell : t2 = {math.degrees(t2_snell):.4f} deg ; diferencia = {abs(t2 - t2_snell):.2e} rad ; n1 sen t1 - n2 sen t2 = {snell:.2e}")
    assert abs(t2 - t2_snell) < 1e-6
    # el tiempo minimo es menor que el de la recta (no desviada)
    t_min = tiempo(x, a, b, d, n1, n2)
    x_rect = d * a / (a + b)
    t_rect = tiempo(x_rect, a, b, d, n1, n2)
    print(f"tiempo minimo = {t_min*1e12:.4f} ps ; trayecto recto = {t_rect*1e12:.4f} ps ; ahorro = {(t_rect-t_min)*1e15:.2f} fs")
    assert t_min < t_rect
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
