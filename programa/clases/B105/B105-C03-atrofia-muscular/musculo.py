#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C03: atrofia muscular como balance de proteina (modelo DIDACTICO, datos SINTETICOS).

Modelo: reserva de proteina muscular P(t) con dP/dt = -delta P (balance neto negativo proporcional a la reserva). Solucion P = P0 exp(-delta t),
t en dias. delta ~ N(0.0030, 0.0010) por dia (ILUSTRATIVO) sin contramedida y delta/2 con contramedida (ILUSTRATIVO). La fuerza maxima es
F = sigma * A con sigma = 25 N/cm2 (tension especifica de ensenanza) y A proporcional a P; A0 = 70 cm2 (seccion de un musculo grande, ilustrativa).
Fuente consultada (NASA, 'Human body in space', 2026-11-10): sin dieta ni ejercicio adecuados el musculo se pierde mas rapido en microgravedad
que en la Tierra (cualitativo). Poblacion SINTETICA de 5000, semilla 105. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

SIGMA, A0 = 25.0, 70.0


def area(delta, t):
    return A0 * np.exp(-delta * t)


def fuerza(delta, t):
    return SIGMA * area(delta, t)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): delta, A0 y sigma ilustrativos; la unica cifra consultada es cualitativa (NASA, 2026-11-10)")
    for d in (0.0030, 0.0015):
        print(f"delta = {d:.4f}/dia: area a 30/90/180 dias = " + ", ".join(f"{area(d, t):5.1f}" for t in (30, 90, 180)) + " cm2; fuerza a 180 d = " + f"{fuerza(d, 180):6.1f} N (inicial {fuerza(d, 0):.1f} N)")
    rng = np.random.default_rng(105)
    d = rng.normal(0.0030, 0.0010, 5000).clip(0.0, None)
    res = {}
    for nombre, f in (("sin contramedida", 1.0), ("con contramedida (delta/2)", 0.5)):
        perd = 100 * (1 - np.exp(-f * d * 90))
        res[nombre] = perd
        print(f"{nombre:28s} perdida a 90 dias: media {perd.mean():5.2f} %, DE {perd.std():5.2f}, p5-p95 = {np.percentile(perd, 5):5.2f}-{np.percentile(perd, 95):5.2f} %")
    dif = res["sin contramedida"] - res["con contramedida (delta/2)"]
    print(f"Reduccion media de la perdida por la contramedida simulada = {dif.mean():.2f} puntos porcentuales (n = 5000)")
    # estimacion de delta a partir de mediciones ruidosas de area
    t = np.array([0, 15, 30, 45, 60, 90.0])
    a_obs = area(0.0030, t) * (1 + rng.normal(0, 0.01, t.size))
    pend = np.polyfit(t, np.log(a_obs), 1)[0]
    print(f"Ajuste log-lineal de 6 mediciones sinteticas con 1 % de ruido: delta = {-pend:.5f}/dia (verdad 0.00300)")
    assert abs(area(0.003, 30) - 63.96) < 0.05
    assert res["con contramedida (delta/2)"].mean() < res["sin contramedida"].mean()
    assert abs(-pend - 0.003) < 0.0005
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
