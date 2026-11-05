#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C19: refracción, lentes, límite de difracción y tiempos de luz.

Datos PUBLICADOS: c = 299 792 458 m/s (exacta, BIPM SI); distancia Tierra–Sol 149,598e6 km y radio
ecuatorial terrestre (NASA NSSDC, Earth Fact Sheet); semieje mayor lunar 384 400 km (NASA NSSDC,
Moon Fact Sheet). SINTÉTICOS: índices de refracción (1,00 y 1,50), distancias focales, longitud de onda
de 550 nm y diámetro de 0,10 m. Modelo: óptica geométrica (ley de Snell y lente delgada) y criterio de
Rayleigh del límite de difracción 1,22 lambda/D. Dominio de validez: ángulos pequeños en la lente
delgada; abertura circular ideal. Tolerancias: 1e-12 en reversibilidad y composición de lentes.
"""
from __future__ import annotations
import math
import sys

C = 299_792_458.0
AU = 149.598e9
A_LUNA = 3.844e8
ARCSEC_POR_RAD = 180.0 / math.pi * 3600.0

def snell(n1: float, n2: float, theta1_deg: float) -> float | None:
    s = n1 * math.sin(math.radians(theta1_deg)) / n2
    return None if abs(s) > 1.0 else math.degrees(math.asin(s))

def angulo_critico(n1: float, n2: float) -> float:
    return math.degrees(math.asin(n2 / n1))

def imagen_lente(f: float, d_obj: float) -> float:
    return 1.0 / (1.0 / f - 1.0 / d_obj)

def limite_difraccion_arcsec(lam: float, D: float) -> float:
    return 1.22 * lam / D * ARCSEC_POR_RAD

def main() -> int:
    # reversibilidad del rayo: ir y volver da el ángulo original
    t2 = snell(1.0, 1.5, 40.0)
    assert abs(snell(1.5, 1.0, t2) - 40.0) < 1e-12
    # incidencia normal: no se desvía
    assert snell(1.0, 1.5, 0.0) == 0.0
    # lente delgada: intercambio objeto-imagen (conjugados)
    f, d = 0.5, 2.0
    di = imagen_lente(f, d)
    assert abs(imagen_lente(f, di) - d) < 1e-12
    assert abs(1 / d + 1 / di - 1 / f) < 1e-12
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Refracción aire->vidrio (n=1,50) a 40°: {t2:.3f}°; ángulo crítico vidrio->aire = {angulo_critico(1.5, 1.0):.2f}°")
    print(f"Lente f = {f} m, objeto a {d} m: imagen a {di:.4f} m; aumento lateral = {-di/d:.4f}")
    for D in (0.10, 1.0, 8.0):
        print(f"  Límite de difracción (550 nm, D = {D:4.1f} m): {limite_difraccion_arcsec(550e-9, D):.4f} arcsec")
    print(f"1 rad = {ARCSEC_POR_RAD:.3f} arcsec")
    print(f"Luz Tierra–Luna: {A_LUNA/C:.4f} s; Sol–Tierra (1 au): {AU/C:.2f} s = {AU/C/60:.3f} min; satélite a 400 km: {400e3/C*1e3:.4f} ms")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
