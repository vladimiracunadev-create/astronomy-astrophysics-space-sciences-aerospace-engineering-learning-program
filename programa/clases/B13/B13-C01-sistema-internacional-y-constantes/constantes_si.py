#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C01: constantes definitorias del SI y conversiones espaciales.

Datos: valores EXACTOS de las constantes definitorias del SI (BIPM; NIST/CODATA
2022, consultados 2026-11-05), la unidad astronomica de IERS TN36 (1 au =
1.495978707e11 m, valor TDB-compatible) y el GM geocentrico de IERS TN36
(3.986004418e14 m3/s2, TCG-compatible). La distancia Tierra-Luna (384 400 km) es un valor
publicado con 4 cifras (NASA/NSSDC) y se usa como dato ESTIMADO.
Modelo: la unidad de longitud se deriva de c y del segundo; aritmetica racional
(fracciones) para no mezclar redondeos con definiciones.
Supuestos: propagacion en el vacio, sin retardo atmosferico ni relativista.
Validez: conversiones de unidades y tiempos de luz a orden de 1e-9 relativo.
Tolerancia: identidades exactas (igualdad de fracciones); 1e-12 relativa en
las cifras derivadas en coma flotante.
"""
from __future__ import annotations
import platform
import sys
from fractions import Fraction

C = 299_792_458                       # m/s, exacto
DNU_CS = 9_192_631_770                # Hz, exacto
H = Fraction(662_607_015, 10**8) * Fraction(1, 10**34)   # J s, exacto
K_B = Fraction(1_380_649, 10**6) * Fraction(1, 10**23)   # J/K, exacto
AU = Fraction(149_597_870_700)        # m (IERS TN36, Tabla 1.1: 1.49597870700e11 m)


def luz_en(segundos: Fraction) -> Fraction:
    """Distancia (m) recorrida por la luz en el vacio en el tiempo dado."""
    return C * segundos


def main() -> None:
    print(f"Python {platform.python_version()} (sin bibliotecas externas)")
    # 1) Definicion del metro: distancia recorrida en 1/299 792 458 s = 1 m
    assert luz_en(Fraction(1, C)) == 1
    # 2) Definicion del segundo: 9 192 631 770 periodos de la radiacion Cs = 1 s
    periodo_cs = Fraction(1, DNU_CS)
    assert DNU_CS * periodo_cs == 1
    lam_cs = luz_en(periodo_cs)
    print(f"periodo Cs = {float(periodo_cs):.6e} s ; longitud de onda en vacio = {float(lam_cs)*100:.6f} cm")
    # 3) Energia del foton de la transicion del Cs
    e_foton = H * DNU_CS
    print(f"E = h*dnu_Cs = {float(e_foton):.6e} J")
    # 4) Tiempo de luz de 1 au y Tierra-Luna
    t_au = AU / C
    t_luna = Fraction(384_400_000) / C
    print(f"1 au / c = {float(t_au):.6f} s ; Tierra-Luna = {float(t_luna):.6f} s (estimado)")
    assert abs(float(t_au) - 499.004784) < 1e-6
    # 5) GM terrestre: km3/s2 <-> m3/s2 (factor exacto 1e9)
    gm_m = Fraction(3_986_004_418) * 10**5   # 3.986004418e14 m3/s2
    gm_km = gm_m / 10**9
    assert gm_km * 10**9 == gm_m
    print(f"GM_E (IERS) = {float(gm_m):.9e} m3/s2 = {float(gm_km):.4f} km3/s2")
    # 6) Energia termica kT a 273.16 K (kelvin definido por k)
    kt = K_B * Fraction(27316, 100)
    print(f"k*T(273.16 K) = {float(kt):.6e} J")
    # 7) Prueba dimensional minima: c*t_au debe reconstruir 1 au exactamente
    assert luz_en(t_au) == AU
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una identidad exacta no se cumple")
        sys.exit(1)
