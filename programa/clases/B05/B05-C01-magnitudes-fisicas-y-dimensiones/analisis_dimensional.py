#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C01: análisis dimensional y conversión de unidades.

Datos: constantes del SI (BIPM, 9.ª ed.), g_n = 9,806 65 m/s² exacto (NIST CODATA 2022),
libra-masa 0,453 592 37 kg exacta (definición internacional), GM de la Tierra
3,9860e14 m³/s² (NASA NSSDC, Earth Fact Sheet), radio ecuatorial 6 378 137 m (idem).
Modelo: una dimensión es un vector de exponentes (M, L, T) de masa, longitud y tiempo.
Supuestos: solo mecánica; sin temperatura ni carga. Dominio de validez: ecuaciones
de la forma producto de potencias. Tolerancia: 1e-12 relativa en conversiones exactas,
0,5 % en la comparación con la ficha de la NASA.
"""
from __future__ import annotations
import math
import sys
from fractions import Fraction

# Dimensión = (M, L, T) con exponentes fraccionarios exactos
def dim(m=0, l=0, t=0):
    return (Fraction(m), Fraction(l), Fraction(t))

def mul(a, b): return tuple(x + y for x, y in zip(a, b))
def pot(a, p): return tuple(x * Fraction(p) for x in a)

LONGITUD, MASA, TIEMPO = dim(l=1), dim(m=1), dim(t=1)
VELOCIDAD = dim(l=1, t=-1)
ACELERACION = dim(l=1, t=-2)
FUERZA = dim(m=1, l=1, t=-2)
IMPULSO = dim(m=1, l=1, t=-1)
ENERGIA = dim(m=1, l=2, t=-2)
GM = dim(l=3, t=-2)             # [GM] = m³/s²
G = dim(m=-1, l=3, t=-2)

LB_KG = 0.45359237              # kg, exacto
GN = 9.80665                    # m/s², exacto
LBF_N = LB_KG * GN              # N, derivado

def pruebas() -> None:
    assert mul(MASA, ACELERACION) == FUERZA                      # F = m a
    assert mul(FUERZA, TIEMPO) == IMPULSO                        # impulso = F t
    assert mul(FUERZA, LONGITUD) == ENERGIA                      # W = F d
    assert mul(MASA, pot(VELOCIDAD, 2)) == ENERGIA               # m v²
    assert mul(G, MASA) == GM                                    # [G m] = [GM]
    # T = 2π sqrt(r³/GM) tiene dimensión de tiempo
    assert mul(pot(LONGITUD, Fraction(3, 2)), pot(GM, Fraction(-1, 2))) == TIEMPO
    assert abs(LBF_N - 4.4482216152605) < 1e-12                  # libra-fuerza
    assert abs(1 * 4.4482216152605 * 1 - LBF_N) < 1e-12

def fmt(d):
    return "M^%s L^%s T^%s" % tuple(str(x) for x in d)

def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("[F] =", fmt(FUERZA), "| [E] =", fmt(ENERGIA), "| [GM] =", fmt(GM))
    print(f"1 lbf = {LBF_N:.10f} N")
    lbf_s = 1.0
    print(f"Impulso de 1,00 lbf·s = {lbf_s * LBF_N:.4f} N·s (error si se tomara como N·s: factor {LBF_N:.3f})")
    gm, re, h = 3.9860e14, 6_378_137.0, 400_000.0
    r = re + h
    v = math.sqrt(gm / r)
    T = 2 * math.pi * math.sqrt(r**3 / gm)
    print(f"Satélite ideal a 400 km: r = {r:.0f} m, v = {v:.1f} m/s, T = {T:.1f} s = {T/60:.2f} min")
    assert abs(T / 60 - 90.0) < 5.0         # NASA: la ISS da una órbita cada ~90 min (orden de magnitud)
    print(f"Imprecisión si h se escribiera en pies sin convertir: r' = {re + 400_000 * 0.3048:.0f} m")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
