#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C09: presupuesto de delta-v de una mision Tierra-Marte (modelo circular y coplanar) y masa de propulsante.

Datos consultados (2026-11-10): masas Tierra 5.9722e24 kg y Marte 0.64169e24 kg, radios (Tierra 6371.0 km, Marte 3396.2 km), semiejes 149.598e6 y 227.956e6 km (fichas NASA/NSSDC);
G = 6.67430e-11 (registro del JPL); GM de cada planeta = G M. GM_sol = 1.32712440e11 km3/s2 y g0 = 9.80665 m/s2 (estandar, no consultados).
SINTETICOS / ILUSTRATIVOS (decisiones del ejercicio, no de una mision): orbita de salida circular a 300 km, orbita final de Marte 300 x 20 000 km de altitud,
correcciones de trayectoria 0.10 km/s, ajuste de orbita 0.05 km/s, margen del 10 % sobre lo determinista, Isp = 320 s, masa seca final 1000 kg.
Modelo: conicas empalmadas, impulsos instantaneos.
Pruebas: (1) masa inicial por producto de razones de masa por fase = masa inicial por la suma de delta-v (tol. 1e-12 relativa); (2) integracion numerica de la ecuacion del cohete (paso de masa) iguala la forma cerrada (tol. 1e-5 relativa).
"""
import math, platform
G = 6.67430e-20
MU = 1.32712440e11
G0 = 9.80665e-3  # km/s2
GME, GMM = G * 5.9722e24, G * 0.64169e24
RE_, RM_ = 6371.0, 3396.2
AE, AM = 149.598e6, 227.956e6


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    at = 0.5 * (AE + AM)
    vinf_d = math.sqrt(MU * (2 / AE - 1 / at)) - math.sqrt(MU / AE)
    vinf_a = math.sqrt(MU / AM) - math.sqrt(MU * (2 / AM - 1 / at))
    r0 = RE_ + 300.0
    dv_dep = math.sqrt(vinf_d**2 + 2 * GME / r0) - math.sqrt(GME / r0)
    rp = RM_ + 300.0; ra = RM_ + 20000.0; ael = 0.5 * (rp + ra)
    dv_cap = math.sqrt(vinf_a**2 + 2 * GMM / rp) - math.sqrt(2 * GMM / rp - GMM / ael)
    fases = [("Salida desde orbita baja terrestre (300 km)", dv_dep),
             ("Correcciones de trayectoria (sintetico)", 0.10),
             ("Captura en orbita 300 x 20000 km (Marte)", dv_cap),
             ("Ajuste de orbita (sintetico)", 0.05)]
    print(f"v_inf salida = {vinf_d:.4f} km/s ; v_inf llegada = {vinf_a:.4f} km/s ; heliocentrico Hohmann suma = {vinf_d+vinf_a:.4f} km/s")
    print("Fase                                          dv [km/s]")
    for n, d in fases: print(f"{n:45s} {d:8.4f}")
    det = sum(d for _, d in fases)
    marg = 0.10 * det
    tot = det + marg
    print(f"Determinista = {det:.4f} km/s ; margen 10 % = {marg:.4f} km/s ; TOTAL = {tot:.4f} km/s")
    isp = 320.0; mf = 1000.0
    # razon de masa por fase (en orden inverso: la ultima fase se calcula primero), con el margen repartido proporcionalmente
    m = mf; prod = 1.0
    for n, d in reversed(fases):
        dd = d * 1.10
        rm = math.exp(dd / (isp * G0)); m *= rm; prod *= rm
    m_total_suma = mf * math.exp(tot / (isp * G0))
    print(f"Isp = {isp:.0f} s (sintetico) ; masa inicial por fases = {m:.3f} kg ; por suma de delta-v = {m_total_suma:.3f} kg ; propulsante = {m-mf:.3f} kg ({(m-mf)/m*100:.1f} % de la masa inicial)")
    assert abs(m - m_total_suma) / m < 1e-12
    # Prueba 2: integracion de la ecuacion del cohete con pasos de masa
    n = 200000; v = 0.0; mm = m
    dm = (m - mf) / n
    for _ in range(n):
        mid = mm - 0.5 * dm
        v += isp * G0 * dm / mid
        mm -= dm
    print(f"Prueba 2: dv por integracion numerica = {v:.6f} km/s ; dv total = {tot:.6f} km/s")
    assert abs(v - tot) / tot < 1e-5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
