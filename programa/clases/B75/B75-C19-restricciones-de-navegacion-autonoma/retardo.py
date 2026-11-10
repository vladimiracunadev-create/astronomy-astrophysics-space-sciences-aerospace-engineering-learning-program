#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C19: retardo de luz Tierra-Marte en un periodo sinodico y necesidad de autonomia (modelo circular y coplanar).

Datos consultados (2026-11-10): semiejes y periodos siderales de las fichas NASA/NSSDC (Tierra 149.598e6 km y 365.256 d; Marte 227.956e6 km y 686.980 d). c = 299 792.458 km/s (valor exacto del SI, estandar, no consultado).
SINTETICOS / ILUSTRATIVOS: tiempo de proceso en tierra y de envio de comandos 1800 s; duraciones de eventos (captura 1800 s, pasada de aerofrenado 540 s, maniobra de correccion 120 s, aterrizaje con paracaidas 420 s).
Modelo: distancia por la ley de cosenos con ambos planetas en orbita circular; el Sol no bloquea la linea de vision salvo en conjuncion (no se modela la conjuncion solar).
Pruebas: (1) distancia por ley de cosenos igual a la norma de la diferencia de vectores (tol. 1e-6 km); (2) el maximo del muestreo diario difiere del analitico a_T + a_M en menos de 1 % y el minimo de a_M - a_T en menos de 1 %; (3) la fraccion del ciclo con RTLT > 30 min coincide con la analitica (tol. 0.5 puntos porcentuales).
"""
import math, platform
C = 299792.458
AE, AM = 149.598e6, 227.956e6
PE, PM = 365.256, 686.980
PROC = 1800.0
EVENTOS = [("Maniobra de correccion", 120.0), ("Pasada de aerofrenado", 540.0), ("Aterrizaje con paracaidas", 420.0), ("Captura en orbita", 1800.0)]


def dist(t):
    ang = 2 * math.pi * t * (1 / PE - 1 / PM)
    return math.sqrt(AE**2 + AM**2 - 2 * AE * AM * math.cos(ang)), ang


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    syn = 1 / (1 / PE - 1 / PM)
    n = int(syn) + 1
    ds = []; mal = 0
    for i in range(n):
        d, ang = dist(i)
        pe = [AE, 0.0]; pm = [AM * math.cos(ang), AM * math.sin(ang)]
        assert abs(d - math.dist(pe, pm)) < 1e-6
        ds.append(d)
        if 2 * d / C > 1800.0: mal += 1
    dmin, dmax = min(ds), max(ds)
    print(f"Periodo sinodico = {syn:.2f} d ; distancia minima (muestreo diario) = {dmin/1e6:.2f}e6 km ; maxima = {dmax/1e6:.2f}e6 km (analiticas: {(AM-AE)/1e6:.2f} y {(AM+AE)/1e6:.2f})")
    assert abs(dmax - (AE + AM)) / (AE + AM) < 0.01 and abs(dmin - (AM - AE)) / (AM - AE) < 0.01
    lts = [d / C for d in ds]
    print(f"Retardo unidireccional: minimo = {min(lts):.1f} s ({min(lts)/60:.2f} min) ; medio = {sum(lts)/n:.1f} s ({sum(lts)/n/60:.2f} min) ; maximo = {max(lts):.1f} s ({max(lts)/60:.2f} min)")
    print(f"Retardo de ida y vuelta: minimo = {2*min(lts)/60:.2f} min ; medio = {2*sum(lts)/n/60:.2f} min ; maximo = {2*max(lts)/60:.2f} min")
    frac = 100 * mal / n
    # fraccion analitica de RTLT > 30 min: d > 1800*c/2
    dl = 1800.0 * C / 2
    cosl = (AE**2 + AM**2 - dl**2) / (2 * AE * AM)
    fan = 100 * (1 - math.acos(cosl) / math.pi)
    print(f"Fraccion del ciclo con RTLT > 30 min: muestreo {frac:.1f} % ; analitica {fan:.1f} %")
    assert abs(frac - fan) < 0.5
    print(f"Tiempo de reaccion minimo desde tierra = RTLT + proceso ({PROC:.0f} s, SINTETICO):")
    print(" evento                     duracion [s]   reaccion en RTLT minimo [s]   en RTLT medio [s]   en RTLT maximo [s]   requiere autonomia")
    for nom, dur in EVENTOS:
        r0 = 2 * min(lts) + PROC; r1 = 2 * sum(lts) / n + PROC; r2 = 2 * max(lts) + PROC
        print(f"{nom:26s} {dur:10.0f} {r0:26.0f} {r1:19.0f} {r2:20.0f}   {'si' if dur < r0 else 'depende'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
