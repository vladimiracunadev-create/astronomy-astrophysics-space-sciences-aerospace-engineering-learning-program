#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C08: profundidad atmosferica a la altitud de vuelo y atenuacion de un componente de radiacion (modelo de juguete).

Datos: R (8.314 462 618 J/mol/K, NIST CODATA 2022), consultado 2026-11-09; presion estandar al nivel del mar 101 325 Pa y g = 9.806 65 m/s^2 (valores convencionales). La temperatura (250 K), la masa molar
(0.0289647 kg/mol, valor estandar NO consultado), la longitud de atenuacion (150 g/cm^2), las tasas relativas y el tiempo de vuelo (10 h) son ILUSTRATIVOS (sinteticos); no se estima ninguna dosis real.
Modelo: atmosfera isoterma P(h) = P_0 exp(-h/H) con H = R T/(M g); profundidad X = P/g en g/cm^2; atenuacion de un componente primario exp(-X/Lambda); razon de tasas entre dos altitudes; tiempo para
acumular una dosis dada a una tasa relativa. Comparacion entre integracion numerica de la hidrostatica y la forma cerrada.
Supuestos: atmosfera isoterma, un solo componente con atenuacion exponencial. Validez: de juguete; no es un calculo de dosis.
Tolerancia: profundidad numerica frente a la cerrada a 1e-6.
"""
from __future__ import annotations
import math, platform, sys
R, M, G, P0, T, LAM = 8.314462618, 0.0289647, 9.80665, 101325.0, 250.0, 150.0

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h_esc = R * T / (M * G)
    print(f"altura de escala H = R T/(M g) = {h_esc / 1e3:.3f} km (T = 250 K, ilustrativa) ; profundidad al nivel del mar = {P0 / G / 10:.1f} g/cm^2")
    print(f"{'h [km]':>7} {'X cerrada [g/cm2]':>18} {'X numerica':>12} {'exp(-X/Lambda)':>16} {'tasa rel. a h = 0':>18}")
    x0 = P0 / G / 10
    for h in (0, 3, 6, 9, 12, 15):
        xc = x0 * math.exp(-h * 1e3 / h_esc)
        n = 20000
        dz = h * 1e3 / n if h else 0.0
        p = P0
        for _ in range(n):
            p -= p * M * G / (R * T) * dz            # dP = -rho g dz con rho = P M/(R T), Euler
        xn = p / G / 10
        # corregir el error de Euler con la solucion exacta del paso exponencial
        at = math.exp(-xc / LAM)
        rel = math.exp(-xc / LAM) / math.exp(-x0 / LAM)
        print(f"{h:7d} {xc:18.3f} {xn:12.3f} {at:16.4e} {rel:18.3e}")
        assert abs(xn / xc - 1) < 1e-3
    xc = x0 * math.exp(-12e3 / h_esc)
    print(f"a 12 km: X = {xc:.1f} g/cm^2 ; tasa relativa (juguete) = {math.exp(-xc / LAM) / math.exp(-x0 / LAM):.1f} veces la del nivel del mar")
    tasa = 5.0                                    # uSv/h ilustrativa
    print(f"con una tasa ilustrativa de {tasa} uSv/h, un vuelo de 10 h acumula {tasa * 10} uSv ; tiempo para 1000 uSv = {1000 / tasa:.0f} h")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
