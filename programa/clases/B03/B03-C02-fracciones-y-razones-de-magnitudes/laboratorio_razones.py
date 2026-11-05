#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C02: razones entre tamaños y masas.

Datos PUBLICADOS (NASA NSSDC Fact Sheets: radios medios volumétricos y masas;
Sun act. 9-may-2024, Earth 15-nov-2024, Moon 11-ene-2024, Jupiter 2-oct-2024).
Modelo: razón = cociente de dos magnitudes expresadas en la misma unidad.
Supuestos: los cuerpos se tratan como esferas. Validez: comparación de tamaños
medios. Tolerancia: 0,3 % frente a las razones de la tabla de razones de la NASA
(18-mar-2025): Luna/Tierra en diámetro 0,2724; Júpiter/Tierra en masa 317,8.
"""
from __future__ import annotations

import platform
from fractions import Fraction

R_KM = {"Sol": 695_700, "Tierra": 6_371.0, "Luna": 1_737.4, "Júpiter": 69_911}
M_E24 = {"Sol": 1_988_400, "Tierra": 5.9722, "Luna": 0.07346, "Júpiter": 1_898.13}


def razon(a: float, b: float) -> float:
    return a / b


def pruebas() -> None:
    assert Fraction(6, 8) == Fraction(3, 4) and Fraction(6, 8).denominator == 4
    assert razon(10, 4) == 2.5
    assert abs(razon(M_E24["Júpiter"], M_E24["Tierra"]) - 317.8) / 317.8 < 0.003
    assert abs(razon(R_KM["Luna"], R_KM["Tierra"]) - 0.2724) / 0.2724 < 0.003
    # la razón no depende de la unidad: m frente a km
    r_m = razon(R_KM["Sol"] * 1000, R_KM["Tierra"] * 1000)
    assert abs(r_m - razon(R_KM["Sol"], R_KM["Tierra"])) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"Radio Sol / Tierra    = {razon(R_KM['Sol'], R_KM['Tierra']):.2f}")
    r = razon(R_KM["Luna"], R_KM["Tierra"])
    print(f"Radio Luna / Tierra   = {r:.4f}  (aprox. fraccionaria: {Fraction(r).limit_denominator(20)})")
    print(f"Masa Júpiter / Tierra = {razon(M_E24['Júpiter'], M_E24['Tierra']):.1f}")
    print(f"Masa Sol / Tierra     = {razon(M_E24['Sol'], M_E24['Tierra']):.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
