#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C08: gravedad, escape y temperatura de equilibrio de Marte.

Datos (NASA/NSSDC, hoja de datos de Marte, actualizada 2025-05-19, consultada el 2026-11-09):
masa 0,64169e24 kg; radio medio volumetrico 3389,5 km; gravedad media 3,73 m/s2; velocidad
de escape 5,03 km/s; presion media 636 Pa (6,36 mb); temperatura media 214 K; rango en el
sitio del Viking 1: 184 a 242 K; semieje mayor 227,956e6 km. G y sigma de NIST (CODATA 2022);
irradiancia solar 1361 W/m2 y luminosidad 3,828e26 W de la IAU 2015 B3 (texto del PDF
consultado el 2026-11-09). NO CONSULTADOS: la UA = 149 597 870 700 m (valor estandar) y el
albedo de Bond 0,25 (ILUSTRATIVO). Limite de replicacion: -28 C de COSPAR 2026.
Modelo: g = G M / R^2; v_esc = sqrt(2 G M / R); T_eq = [S (1-A) / (4 sigma)]^(1/4) con
S = 1361 W/m2 / (a/1 UA)^2.
Supuestos: esfera, sin efecto invernadero; albedo ilustrativo. Validez: orden de magnitud.
Tolerancia: g y v_esc coinciden con la hoja a < 1 %; el flujo por luminosidad y por
irradiancia coinciden a < 0,2 %.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
SIGMA = 5.670374419e-8
M, R = 0.64169e24, 3389.5e3
UA = 149597870700.0
A_MARTE = 227.956e9
S0, L0 = 1361.0, 3.828e26
LLT_K = 273.15 - 28.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    g = G * M / R ** 2
    v = math.sqrt(2 * G * M / R)
    print(f"g = {g:.3f} m/s2 (hoja: 3,73) ; v_esc = {v / 1000:.3f} km/s (hoja: 5,03)")
    assert abs(g / 3.73 - 1) < 0.01 and abs(v / 5030 - 1) < 0.01
    flujo_L = L0 / (4 * math.pi * A_MARTE ** 2)
    flujo_S = S0 * (UA / A_MARTE) ** 2
    print(f"Flujo solar en Marte: {flujo_L:.1f} W/m2 (por L) ; {flujo_S:.1f} W/m2 (por S)")
    assert abs(flujo_L / flujo_S - 1) < 0.002
    albedo = 0.25
    t_eq = (flujo_S * (1 - albedo) / (4 * SIGMA)) ** 0.25
    print(f"T_eq (albedo {albedo}, ilustrativo) = {t_eq:.1f} K ; hoja: media 214 K")
    t_max = 242.0
    print(f"Maximo en Viking 1: {t_max} K = {t_max - 273.15:.1f} C ; limite -28 C = {LLT_K:.2f} K ; "
          f"T_max - LLT = {t_max - LLT_K:.2f} K")
    assert t_max < LLT_K
    columna = 636.0 / g
    print(f"Masa de atmosfera por m2 = P/g = {columna:.0f} kg/m2 (Tierra ~ 1,03e4, ilustrativo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
