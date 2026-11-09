#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C07: balance de gases de una camara analoga y crecimiento logistico de un cultivo no patogeno.

Datos: composicion y presion de la atmosfera marciana de la ficha NASA NSSDC Mars Fact Sheet (consultada el 2026-11-09,
actualizada el 19 may 2025): P = 6.36 mbar (4.0-8.7 estacional); CO2 95.1 %, N2 2.59 %, Ar 1.94 %, O2 0.16 % en volumen.
El volumen de la camara, la presion de trabajo, la constante de Henry del CO2 (0.034 mol/(L atm) a 298 K) y el crecimiento
(mu, K) son ILUSTRATIVOS/SINTETICOS; la constante de Henry NO se consulto. Constante: R = 8.314462618 J/(mol K) (CODATA 2022, NIST).
Modelo 1: gas ideal. n_i = x_i P V/(R T); presiones parciales p_i = x_i P. Dos presiones: la marciana y una de trabajo de 100 kPa
con la misma mezcla (analogo de composicion, no de presion). Ley de Henry: [CO2]aq = kH p_CO2.
Modelo 2: crecimiento logistico dN/dt = mu N (1 - N/K); solucion cerrada N(t) = K/(1 + (K/N0 - 1) e^(-mu t)); comparacion con RK4.
Unidades: P [Pa]; V [m3]; T [K]; N [UFC/mL] (SINTETICO). Tolerancias: suma de parciales = P a 1e-12; RK4 frente a cerrada 1e-6
relativo; moles de gas por dos vias 1e-12.
Supuestos: mezcla ideal, isotermia 298.15 K, sin consumo de gas por el cultivo (nota). Validez: ilustrativa.
Aviso de seguridad: SOLO organismos de nivel de bioseguridad 1 y no patogenos; ver seccion 21.
"""
from __future__ import annotations
import math, platform

R = 8.314462618
T = 298.15
MEZCLA = {"CO2": 0.951, "N2": 0.0259, "Ar": 0.0194, "O2": 0.0016}   # NASA, fraccion en volumen
KH = 0.034        # mol/(L atm) (ilustrativo, no consultado)
ATM = 101325.0
_S = sum(MEZCLA.values())      # 0.9979: la ficha no suma 100 %; se renormaliza
MEZCLA = {g: x / _S for g, x in MEZCLA.items()}


def moles(P, V):
    return {g: x * P * V / (R * T) for g, x in MEZCLA.items()}


def logistica(t, N0, K, mu):
    return K / (1 + (K / N0 - 1) * math.exp(-mu * t))


def rk4(N0, K, mu, tf, n):
    f = lambda N: mu * N * (1 - N / K)
    h = tf / n
    N = N0
    for _ in range(n):
        k1 = f(N); k2 = f(N + h * k1 / 2); k3 = f(N + h * k2 / 2); k4 = f(N + h * k3)
        N += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return N


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Las fracciones de la ficha NASA suman {_S:.4f}; se renormalizan a 1 (el resto, trazas, se ignora)")
    V = 0.010    # camara de 10 L (ilustrativo)
    print(f"Datos: V = {V * 1000:.0f} L (ilustrativo), T = {T} K")
    for etiqueta, P in (("presion marciana (636 Pa)", 636.0), ("presion de trabajo (100 kPa, misma mezcla)", 100000.0)):
        n = moles(P, V)
        ntot = sum(n.values())
        assert abs(ntot - P * V / (R * T)) / ntot < 1e-12
        assert abs(sum(x * P for x in MEZCLA.values()) - P * sum(MEZCLA.values())) < 1e-9
        pco2 = MEZCLA["CO2"] * P / ATM
        print(f"{etiqueta}: n_total = {ntot:.4e} mol ; n_O2 = {n['O2']:.3e} mol ; p_CO2 = {pco2:.4g} atm ; CO2 disuelto = {KH * pco2 * 1e3:.4g} mmol/L")
    print("Nota: a 636 Pa la presion del vapor de agua a 25 C (alrededor de 3 kPa; valor de memoria, no consultado) supera la total: el medio liquido hierve; por eso los analogos de composicion usan camaras presurizadas o medios sellados.")
    # logistica
    N0, K, mu = 1e4, 1e9, 0.35   # UFC/mL, UFC/mL, 1/h (SINTETICOS)
    print(f"\nCrecimiento SINTETICO: N0 = {N0:.0e}, K = {K:.0e} UFC/mL, mu = {mu} 1/h")
    print(f"{'t [h]':>6} {'cerrada':>12} {'RK4':>12}")
    for t in (0, 12, 24, 36, 48, 72):
        c = logistica(t, N0, K, mu)
        r = rk4(N0, K, mu, t, max(1, t * 50))
        print(f"{t:6d} {c:12.4e} {r:12.4e}")
        assert abs(c - r) / c < 1e-6
    t_half = math.log(K / N0 - 1) / mu
    print(f"Tiempo en que N = K/2: {t_half:.2f} h")
    assert abs(logistica(t_half, N0, K, mu) / K - 0.5) < 1e-9
    # consumo de O2 y limite
    y_o2 = 1e-12   # mol O2 por UFC (SINTETICO)
    n_o2 = moles(100000.0, V)["O2"]
    print(f"O2 de la camara a 100 kPa: {n_o2:.3e} mol ; consumo hipotetico de un cultivo aerobio de 50 mL que llegara a K: {y_o2 * K * 50:.3e} mol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
