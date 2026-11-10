#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C04: edad de una provincia volcanica a partir de la densidad de cráteres (conteo de Poisson).

Datos: SINTETICOS. La funcion de cronologia N1(T) = a (exp(b T) - 1) + c T (N1: craters acumulados de diametro >= 1 km por km^2; T en Gyr) tiene la
FORMA funcional usada en la literatura de cronologias de cráteres (Hartmann y Neukum 2001, solo metadatos consultados 2026-11-09), pero sus
coeficientes (a = 2,0e-14, b = 6,0 /Gyr, c = 4,0e-4 /Gyr/km^2) son ILUSTRATIVOS y NO son la calibracion publicada. Las provincias (areas y edades verdaderas) son sinteticas.
Modelo: el numero de cráteres N en un area A es Poisson con media A*N1(T). Estimador de maxima verosimilitud de N1: N/A; la edad se obtiene
invirtiendo N1(T) por biseccion. Intervalo de 68 %: por inversion de N1 en (N +- sqrt(N))/A (aprox. gaussiana).
Pruebas: (1) ida y vuelta T -> N1 -> T; (2) cobertura del intervalo de 68 % por Monte Carlo (semilla 20261109, 4000 ensayos).
Supuestos: superficie sin saturacion ni borrado, produccion constante en forma, cráteres independientes. Validez: ilustrativa.
Tolerancia: 1e-10 en la ida y vuelta; cobertura entre 0,62 y 0,74 para N medio >= 30.
"""
from __future__ import annotations
import math, platform, random

A_, B_, C_ = 2.0e-14, 6.0, 4.0e-4

def n1(T):
    return A_ * (math.exp(B_ * T) - 1) + C_ * T

def edad(N1):
    lo, hi = 0.0, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if n1(mid) < N1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def poisson(rng, lam):
    if lam > 50:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def intervalo(N, A):
    return edad(max(N - math.sqrt(N), 0) / A), edad((N + math.sqrt(N)) / A)

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    for T in (0.5, 1.0, 3.0, 3.8):
        assert abs(edad(n1(T)) - T) < 1e-10
    print("Ida y vuelta T -> N1 -> T superada (T = 0,5; 1; 3; 3,8 Gyr).")
    provincias = [("Provincia A (sintetica)", 4.0e4, 3.6), ("Provincia B (sintetica)", 2.5e4, 1.5), ("Provincia C (sintetica)", 1.0e4, 0.3)]
    rng = random.Random(20261109)
    print("Provincias sinteticas: edad verdadera, conteo simulado y edad recuperada")
    for nombre, A, T in provincias:
        N = poisson(rng, A * n1(T))
        lo, hi = intervalo(N, A)
        Te = edad(N / A)
        print(f"  {nombre}: A = {A:.0f} km^2 ; T = {T:.2f} Gyr ; N(>=1 km) = {N} ; T_est = {Te:.3f} (+{hi-Te:.3f} / -{Te-lo:.3f}) Gyr")
    # cobertura
    for T, A in ((1.0, 4.0e4), (3.5, 4.0e4)):
        lam = A * n1(T)
        ok, N_tot = 0, 4000
        for _ in range(N_tot):
            N = poisson(rng, lam)
            if N == 0:
                continue
            lo, hi = intervalo(N, A)
            ok += lo <= T <= hi
        cov = ok / N_tot
        print(f"Cobertura del intervalo de 68 % (T = {T} Gyr, media de N = {lam:.0f}): {cov:.3f}")
        assert 0.62 <= cov <= 0.74, "cobertura fuera de tolerancia"
    # flujo eruptivo medio de un volumen sintetico
    V, T = 3.0e6, 3.6   # km^3, Gyr (sintetico)
    print(f"Caudal medio sintetico: {V:.1e} km^3 en {T} Gyr = {V/(T*1e9):.2e} km^3/ano")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
