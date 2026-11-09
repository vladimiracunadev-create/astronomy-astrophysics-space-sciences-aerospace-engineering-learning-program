#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C12: limite de Roche de un modelo de dos esferas en contacto alrededor de Saturno.

Datos consultados el 2026-11-09 (NASA/NSSDC, ficha de planetas, tabla metrica): Saturno, diametro 120 536 km, densidad 687 kg/m^3,
masa 568e24 kg. G de NIST (CODATA 2022). La ficha no da incertidumbres.
Datos ILUSTRATIVOS: densidad del hielo de las particulas 920 kg/m^3 y 1000 kg/m^3 (sinteticos); radio de las particulas irrelevante (el limite escala con R).
Los coeficientes clasicos del limite de Roche (rigido ~1.26, fluido ~2.44) NO se consultaron; este modelo es de ensenanza.
Sistema de referencia: rotante sincrono con la orbita circular del centro de masa del par; SI.
Modelo: dos esferas identicas de radio r y masa m en contacto, con el eje que las une radial. Se separan cuando la aceleracion relativa de marea
(diferencia de gravedad entre sus centros mas la diferencia centrifuga, Omega^2 = G M / d^3, rotacion sincrona) iguala a la autogravedad G m/(2r)^2.
Via 1: biseccion de la ecuacion exacta de las dos esferas. Via 2: aproximacion de primer orden en r/d: d^3 = 24 M r^3/m, es decir d = R (24 rhoM/rhom)^(1/3).
Tolerancias: exacto frente a primer orden 5e-3 relativo; escala d ~ rho^(-1/3) a 1e-12.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
M_SAT = 568e24
R_SAT = 120536e3 / 2.0
RHO_SAT = 687.0


def d_exacto(rho_p, R=R_SAT, rho_M=RHO_SAT):
    M = 4.0 / 3.0 * math.pi * R ** 3 * rho_M
    r = 1.0 * (R / 1000.0)  # el limite no depende de r; se usa r = R/1000
    m = 4.0 / 3.0 * math.pi * r ** 3 * rho_p
    f = lambda d: G * M / (d - r) ** 2 - G * M / (d + r) ** 2 + (G * M / d ** 3) * 2 * r - G * m / (2 * r) ** 2
    a, b = 1.05 * R, 50.0 * R
    for _ in range(300):
        c = 0.5 * (a + b)
        if f(c) > 0: a = c
        else: b = c
    return 0.5 * (a + b), M


def d_primer_orden(rho_p, R=R_SAT, rho_M=RHO_SAT):
    return R * (24.0 * rho_M / rho_p) ** (1.0 / 3.0)


def calcular():
    filas = []
    for rho in (920.0, 1000.0, 2000.0, 7360.0):
        d, M = d_exacto(rho)
        d1 = d_primer_orden(rho)
        filas.append((rho, d / R_SAT, d1 / R_SAT, d / d1 - 1.0))
    d1, M = d_exacto(920.0)
    d8, _ = d_exacto(920.0 * 8)
    return dict(filas=filas, m_calc=M, m_ficha=M_SAT, escala=d8 / d1, dens_ok=M / (4.0 / 3.0 * math.pi * R_SAT ** 3))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Saturno (ficha NASA/NSSDC, 2026-11-09): R = {R_SAT / 1e3:.0f} km ; densidad = {RHO_SAT:.0f} kg/m^3 ; masa de la ficha = {r['m_ficha']:.3e} kg ; masa de la esfera = {r['m_calc']:.3e} kg ({r['m_calc'] / r['m_ficha'] - 1:+.2%})")
    print(f"{'rho particula':>14} {'d exacto / R':>13} {'d 1er orden / R':>16} {'dif. rel.':>10}")
    for rho, de, d1, dd in r["filas"]:
        print(f"{rho:14.0f} {de:13.4f} {d1:16.4f} {dd:10.2e}")
    print(f"Cociente d(8 rho)/d(rho) = {r['escala']:.9f} (esperado 0.5 por d ~ rho^(-1/3))")
    assert all(abs(f[3]) < 5e-3 for f in r["filas"])
    assert abs(d_primer_orden(920.0 * 8) / d_primer_orden(920.0) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
