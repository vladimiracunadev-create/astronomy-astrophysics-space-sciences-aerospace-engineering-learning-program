#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C22: ciclo de trabajo de un propulsor electrico en orbita baja (eclipse, potencia disponible y Delta-v por dia).

Datos CONSULTADOS (2026-11-10): G = 6.67430e-11 m3 kg-1 s-2 y g0 = 9.80665 m/s2 (NIST CODATA); masa de la Tierra 5.9722e24 kg y radio ecuatorial 6378.137 km (NASA/NSSDC, Earth Fact Sheet);
rango de Hall de naves pequenas 0.25-55 mN y 200-1920 s y tope de ~75 mN/kW (NASA SSVI, Tabla 4-1).
ILUSTRATIVOS (sinteticos, no de una mision): orbita circular a 500 km de altitud (se eleva a 1000 km), nave de 300 kg, propulsor de 40 mN e Isp 1500 s que consume 700 W (57 mN/kW, bajo el tope consultado),
sin baterias para empujar (solo empuja a la luz del Sol), fraccion de la orbita disponible para empuje tangencial util 0.70 (por restricciones de actitud), disponibilidad termica 1.0, plano orbital con beta = 0 (eclipse maximo).
Modelo: orbita circular; sombra cilindrica: fraccion de eclipse = asin(R/a)/pi ; ciclo de trabajo = (1 - eclipse) x fraccion util x disponibilidad ;
elevacion de orbita circular coplanar con empuje tangencial: Delta-v = v1 - v2 ; masa constante (aproximacion).
Segunda via: integracion numerica de da/dt = 2 a_t sqrt(a^3/GM) con el ciclo de trabajo como aceleracion media, frente a t = Delta-v/(a_t x ciclo).
Tolerancia: tiempos de elevacion por las dos vias coinciden a 1e-4 relativa.
"""
from __future__ import annotations
import math, platform

G, G0 = 6.67430e-11, 9.80665
MT, RT = 5.9722e24, 6378.137e3
GM = G * MT
M, F, ISP, P_PROP = 300.0, 40e-3, 1500.0, 700.0
FRAC_UTIL, DISP, ETA_ARR = 0.70, 1.0, 1.0


def periodo(a):
    return 2 * math.pi * math.sqrt(a ** 3 / GM)


def eclipse(a):
    return math.asin(RT / a) / math.pi


def vc(a):
    return math.sqrt(GM / a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"GM = G M_Tierra = {GM:.6e} m3/s2 (G de NIST, M y R de la ficha de la Tierra de la NASA)")
    a1, a2 = RT + 500e3, RT + 1000e3
    for n, a in (("500 km", a1), ("1000 km", a2)):
        print(f"  orbita a {n}: periodo = {periodo(a)/60:.2f} min ; v circular = {vc(a):.1f} m/s ; eclipse (beta = 0) = {eclipse(a)*100:.2f} % ({eclipse(a)*periodo(a)/60:.2f} min)")
    ciclo = (1 - eclipse(a1)) * FRAC_UTIL * DISP
    print(f"Ciclo de trabajo a 500 km = (1 - eclipse) x fraccion util x disponibilidad = {(1-eclipse(a1)):.4f} x {FRAC_UTIL} x {DISP} = {ciclo:.4f}")
    print(f"Propulsor ILUSTRATIVO: F = {F*1e3:.0f} mN ; Isp = {ISP:.0f} s ; P = {P_PROP:.0f} W -> F/P = {F/P_PROP*1e6:.1f} mN/kW (tope consultado 75)")
    assert F / P_PROP * 1e6 < 75
    a_t = F / M
    dv_dia = a_t * 86400 * ciclo
    print(f"Aceleracion = {a_t*1e3:.4f} mm/s2 ; dv por dia con ese ciclo = {dv_dia:.3f} m/s (sin eclipse ni restricciones seria {a_t*86400:.3f} m/s)")
    dv_req = vc(a1) - vc(a2)
    dv_req = abs(dv_req)
    t_an = dv_req / (a_t * ciclo)
    print(f"Elevacion 500 -> 1000 km: dv = v1 - v2 = {dv_req:.2f} m/s ; tiempo analitico = {t_an/86400:.1f} dias")
    # integracion numerica de a(t) con aceleracion media
    a, t, dt = a1, 0.0, 600.0
    while a < a2:
        a += 2 * (a_t * ciclo) * math.sqrt(a ** 3 / GM) * dt
        t += dt
    print(f"  integracion numerica de da/dt = 2 a_t sqrt(a^3/GM): {t/86400:.1f} dias")
    assert abs(t - t_an) / t_an < 1e-2, (t, t_an)
    ve = ISP * G0
    mp = M * (1 - math.exp(-dv_req / ve))
    print(f"  propelente = M (1 - exp(-dv/Ve)) = {mp:.3f} kg ; tiempo de encendido = {t_an*ciclo/86400:.1f} dias ; energia electrica = {P_PROP*t_an*ciclo/3.6e6:.1f} kWh")
    # sin restricciones de actitud y sin eclipse vs con
    for nombre, c in (("ideal (sin eclipse ni restriccion)", 1.0), ("solo eclipse", 1 - eclipse(a1)), ("eclipse + restriccion util", ciclo)):
        print(f"  {nombre:<36} ciclo = {c:.3f} -> {dv_req/(a_t*c)/86400:>7.1f} dias")
    # potencia: energia de bateria si se quisiera empujar en el eclipse
    e_ecl = P_PROP * eclipse(a1) * periodo(a1) / 3600.0
    print(f"Energia de bateria por orbita para empujar tambien en eclipse: {e_ecl:.1f} Wh (descarga profunda y masa de bateria; no se incluyen)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
