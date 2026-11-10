#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C17: reduccion logaritmica de esporas y presupuesto de carga biologica.

Datos: limites de la categoria IVa para Marte de la politica COSPAR 2026 (Space Research
Today n. 224, texto completo consultado el 2026-11-09, seccion 6.1.2.2.2): carga total
<= 5e5 esporas, carga superficial <= 3e5 esporas y densidad media <= 300 esporas/m2. La
definicion de "espora" (microorganismos mesofilos, heterotrofos y aerobios que sobreviven a
80 C durante 15 minutos) es de la seccion 4.3. TODO LO DEMAS es SINTETICO e ILUSTRATIVO: la
nave de 40 m2, la densidad inicial de 2000 esporas/m2, el valor D de 2 h (tiempo para
reducir 10 veces la poblacion) y el tiempo de proceso. No es un proceso de esterilizacion real.
Modelo: N(t) = N0 10^(-t/D); reduccion logaritmica = log10(N0/N). Probabilidad de que una
muestra de area a no contenga ninguna espora: exp(-rho a) (Poisson).
Supuestos: cinetica de primer orden sin "cola"; esporas distribuidas al azar.
Validez: ilustra el calculo; no sustituye el protocolo del ensayo ni la verificacion
microbiologica. Tolerancia: integracion de Euler con paso 1e-4 h frente a la forma cerrada
con error relativo < 1e-3.
"""
from __future__ import annotations
import math
import platform
import sys

LIM_TOTAL, LIM_SUPERFICIE, LIM_DENSIDAD = 5e5, 3e5, 300.0


def n_final(n0, t, d):
    return n0 * 10 ** (-t / d)


def n_euler(n0, t, d, dt=1e-4):
    k = math.log(10) / d
    n = n0
    for _ in range(int(round(t / dt))):
        n -= k * n * dt
    return n


def tiempo_necesario(n0, n_objetivo, d):
    return d * math.log10(n0 / n_objetivo)


def cumple(area, rho):
    total = area * rho
    return (total <= LIM_TOTAL, total <= LIM_SUPERFICIE, rho <= LIM_DENSIDAD)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    area, rho0, D = 40.0, 2000.0, 2.0
    n0 = area * rho0
    print(f"Inicial: {n0:.0f} esporas en {area:.0f} m2 ({rho0:.0f}/m2) ; cumple (total, superficie, densidad): {cumple(area, rho0)}")
    t = tiempo_necesario(rho0, LIM_DENSIDAD, D)
    print(f"Reduccion necesaria para {LIM_DENSIDAD:.0f}/m2: {math.log10(rho0 / LIM_DENSIDAD):.3f} log ; tiempo = {t:.2f} h con D = {D} h")
    n_c, n_e = n_final(n0, t, D), n_euler(n0, t, D)
    print(f"Tras ese tiempo: cerrada = {n_c:.2f} ; Euler = {n_e:.2f} esporas ; densidad = {n_c / area:.1f}/m2")
    assert abs(n_e / n_c - 1) < 1e-3
    assert abs(n_c / area - LIM_DENSIDAD) < 1e-6
    assert all(cumple(area, n_c / area))
    p0 = math.exp(-(n_c / area) * 0.01)
    print(f"P(0 esporas en una muestra de 0,01 m2 a {n_c / area:.0f}/m2) = {p0:.3f}")
    # Que area haria activo el limite de 3e5 esporas a 300/m2:
    print(f"Area a la que 300/m2 alcanza 3e5 esporas = {LIM_SUPERFICIE / LIM_DENSIDAD:.0f} m2")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
