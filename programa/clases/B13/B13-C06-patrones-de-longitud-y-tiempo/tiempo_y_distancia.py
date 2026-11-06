#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C06: de un error de frecuencia a un error de distancia.

Datos: constantes EXACTAS del SI (c = 299 792 458 m/s; Delta nu_Cs =
9 192 631 770 Hz; BIPM/NIST consultados 2026-11-05). Anio juliano =
365.25 d = 31 557 600 s (convencion). Las desviaciones relativas de
frecuencia (1e-13, 1e-15, 1e-16) son valores de ejemplo SINTETICOS.
Modelo: un reloj con desviacion relativa constante y respecto a un patron
acumula un error de tiempo dt = y * T tras un intervalo T; un telemetro por
tiempo de vuelo convierte tiempos en distancia: d = c * t / 2 (ida y vuelta).
Supuestos: y constante; vacio; sin efectos relativistas ni atmosfericos.
Validez: aritmetica racional exacta; las cifras en coma flotante se
muestran con 6 cifras. Tolerancia: identidades exactas.
"""
from __future__ import annotations
import platform
import sys
from fractions import Fraction

C = 299_792_458
DNU = 9_192_631_770
ANIO = Fraction(31_557_600)
DIA = Fraction(86_400)


def error_tiempo(y: Fraction, T: Fraction) -> Fraction:
    return y * T


def distancia_de_vuelo(t_ida_vuelta: Fraction) -> Fraction:
    return Fraction(C) * t_ida_vuelta / 2


def main() -> None:
    print(f"Python {platform.python_version()} (sin bibliotecas externas)")
    # 1) 1 ns de luz equivale a 0.299792458 m exactos
    assert Fraction(C, 10**9) == Fraction(299_792_458, 10**9)
    print(f"c * 1 ns = {float(Fraction(C, 10**9)):.9f} m")
    # 2) Resolucion de frecuencia necesaria para realizar el segundo a 1e-15
    res = DNU * Fraction(1, 10**15)
    print(f"1e-15 de la frecuencia del Cs = {float(res):.3e} Hz")
    # 3) Error de tiempo y de distancia tras 1 dia y 1 anio
    print("   y        T      dt (ns)        c*dt (m)")
    for y in (Fraction(1, 10**13), Fraction(1, 10**15), Fraction(1, 10**16)):
        for nombre, T in (("1 dia", DIA), ("1 anio", ANIO)):
            dt = error_tiempo(y, T)
            print(f"{float(y):8.0e} {nombre:>7s} {float(dt)*1e9:12.5f} {float(dt*C):12.5f}")
    dt_ref = error_tiempo(Fraction(1, 10**15), ANIO)
    assert dt_ref == Fraction(31_557_600, 10**15)          # 31.5576 ns exactos
    # 4) Ranging a la Luna: ida y vuelta de 2 * 384 400 km
    t_rt = Fraction(2 * 384_400_000, C)
    print(f"ida y vuelta Luna = {float(t_rt):.6f} s")
    assert distancia_de_vuelo(t_rt) == 384_400_000
    # 5) Precision temporal para 1 cm de distancia
    dt_1cm = Fraction(2, 100) / C
    print(f"1 cm de distancia = {float(dt_1cm)*1e12:.2f} ps de ida y vuelta")
    assert dt_1cm * C == Fraction(2, 100)
    # 6) Un reloj con y=1e-13 acumula en un dia un error mayor que el de 1 m de rango
    assert error_tiempo(Fraction(1, 10**13), DIA) * C > 2    # > 2 m de luz
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una identidad exacta no se cumple")
        sys.exit(1)
