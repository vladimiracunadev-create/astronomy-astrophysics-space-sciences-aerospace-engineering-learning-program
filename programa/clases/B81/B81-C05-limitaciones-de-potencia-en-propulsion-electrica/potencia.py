#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C05: potencia solar disponible, empuje de un propulsor electrico y saturacion con la distancia al Sol.

Datos consultados (2026-11-10): luminosidad del Sol L = 382.8e24 W (NASA/NSSDC, ficha del Sol) y UA = 149597870.7 km (JPL SSD, astro_par);
de ellas se CALCULA la irradiancia a 1 UA (no se consulto un valor publicado de la constante solar). NASA SST SOA (propulsion): iones con rejilla
500-3000 s, Hall 200-1920 s, empuje/potencia generalmente inferior a 75 mN/kW (dispositivos de naves pequenas; no son limites fisicos).
g0 = 9,80665 m/s^2 (valor convencional; no consultado en esta sesion).
Todo lo demas es ILUSTRATIVO (sintetico): potencia de paneles a 1 UA 10 kW, eficiencia de conversion 0,60, Isp 2500 s, potencia maxima del propulsor 4,5 kW,
minima 0,5 kW, masa 1000 kg, degradacion de paneles 0 (sin degradacion).
Modelo: P(r) = P1 (1 UA/r)^2 (paneles perpendiculares al Sol); T = 2 eta P_u/(g0 Isp) con P_u = min(P, Pmax); apagado si P < Pmin.
Tolerancias: irradiancia calculada entre 1300 y 1450 W/m^2; empuje por kW inferior a 75 mN/kW; escala 1/r^2 exacta antes de saturar (1e-12).
"""
from __future__ import annotations
import math, platform

L_SUN = 382.8e24   # W (NSSDC)
AU_KM = 149597870.7
G0 = 9.80665
P1, ETA, ISP, PMAX, PMIN, MASA = 10_000.0, 0.60, 2500.0, 4_500.0, 500.0, 1000.0


def empuje(r_ua):
    P = P1 / r_ua**2
    if P < PMIN:
        return P, 0.0, 0.0
    Pu = min(P, PMAX)
    return P, Pu, 2 * ETA * Pu / (G0 * ISP)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    S = L_SUN / (4 * math.pi * (AU_KM * 1e3) ** 2)
    print(f"Irradiancia calculada a 1 UA = L/(4 pi UA^2) = {S:.1f} W/m^2")
    print(f"Empuje por kW = 2 eta/(g0 Isp) = {2*ETA/(G0*ISP)*1e6:.2f} mN/kW (NASA SST SOA: generalmente < 75 mN/kW)")
    r_sat = math.sqrt(P1 / PMAX)
    r_off = math.sqrt(P1 / PMIN)
    print(f"Datos ILUSTRATIVOS: P1 = {P1:.0f} W, eta = {ETA}, Isp = {ISP:.0f} s, Pmax = {PMAX:.0f} W, Pmin = {PMIN:.0f} W, masa = {MASA:.0f} kg")
    print(f"Radio de saturacion = {r_sat:.4f} UA ; radio de apagado = {r_off:.4f} UA")
    print(" r [UA]   P [W]   P_util [W]   T [mN]   a [um/s^2]   dv en 30 d [m/s]")
    filas = {}
    for r in (0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0):
        P, Pu, T = empuje(r)
        a = T / MASA
        filas[r] = (P, Pu, T)
        print(f"{r:6.2f} {P:8.1f} {Pu:10.1f} {T*1e3:9.2f} {a*1e6:11.2f} {a*30*86400:12.3f}")
    # escala 1/r^2 antes de saturar
    e2 = max(abs(filas[r][2] * r**2 - filas[2.0][2] * 4.0) / (filas[2.0][2] * 4.0) for r in (1.5, 2.0, 3.0, 4.0))
    print(f"Escala T r^2 constante entre 1,5 y 4 UA (zona sin saturar): desviacion relativa maxima = {e2:.1e}")
    # dv acumulado de una arco radial lento de 1 UA a 3 UA con velocidad radial 5 km/s (tiempo proporcional)
    n = 20000
    dv_tot = 0.0
    r = 1.0
    vr_ua_d = 5.0 * 86400 / AU_KM
    dt = (3.0 - 1.0) / vr_ua_d / n
    for i in range(n):
        rm = 1.0 + (i + 0.5) * (3.0 - 1.0) / n
        dv_tot += empuje(rm)[2] / MASA * dt * 86400
    print(f"Dv acumulado (ILUSTRATIVO) al alejarse de 1 a 3 UA con velocidad radial 5 km/s, empuje siempre disponible: {dv_tot:.1f} m/s")
    assert 1300 < S < 1450
    assert 2 * ETA / (G0 * ISP) * 1e6 < 75
    assert e2 < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
