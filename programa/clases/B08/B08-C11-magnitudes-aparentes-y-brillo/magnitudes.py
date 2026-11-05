#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C11: la escala de magnitudes (Pogson) y la ganancia de un instrumento.

Datos PUBLICADOS: magnitud visual aparente del Sol -26,74 (NASA Sun Fact Sheet, act. 9-may-2024) y de la Luna llena
-12,74 (NASA Moon Fact Sheet, media en oposición, act. 11-ene-2024), consultadas 2026-11-05; límite de referencia 6,5
de la definición de ZHR de la IMO (glosario, consultado 2026-11-05). Definición: 5 magnitudes = factor 100 en flujo
(J. Battat, «Working with Magnitudes and Color Indices», 2005, PDF leído 2026-11-05). Salidas CALCULADAS.
Supuestos del cálculo de ganancia (SIMULADOS, declarados): pupila dilatada del ojo 7 mm, instrumento sin pérdidas,
fuente puntual, cielo oscuro e ideal. Dominio: fuentes puntuales; no vale para objetos extensos.
Prueba independiente: ejemplo trabajado de Battat (dos estrellas idénticas de magnitud 5 se ven de magnitud 4,25).
"""
from __future__ import annotations

import math
import sys

M_SOL, M_LUNA_LLENA = -26.74, -12.74
LM_REFERENCIA = 6.5
PUPILA_MM = 7.0                                    # supuesto declarado


def razon_flujo(delta_mag: float) -> float:
    """Cuántas veces más flujo tiene el objeto más brillante (delta_mag = m_débil - m_brillante)."""
    return 100.0 ** (delta_mag / 5.0)


def delta_mag(razon: float) -> float:
    return 2.5 * math.log10(razon)


def suma_magnitudes(*ms: float) -> float:
    return -2.5 * math.log10(sum(10.0 ** (-0.4 * m) for m in ms))


def ganancia_apertura_mag(d_mm: float, pupila_mm: float = PUPILA_MM) -> float:
    """Ganancia ideal en magnitud límite de una apertura de d_mm frente a la pupila (fuente puntual)."""
    return 5.0 * math.log10(d_mm / pupila_mm)


def pruebas() -> None:
    assert abs(razon_flujo(5.0) - 100.0) < 1e-9
    assert abs(razon_flujo(1.0) - 2.5119) < 1e-4
    assert abs(suma_magnitudes(5.0, 5.0) - 4.25) < 0.005, suma_magnitudes(5.0, 5.0)     # ejemplo de Battat
    assert abs(delta_mag(razon_flujo(3.3)) - 3.3) < 1e-12
    assert abs(ganancia_apertura_mag(PUPILA_MM)) < 1e-12
    assert abs(ganancia_apertura_mag(70.0) - 5.0) < 1e-9                               # 10 veces el diámetro = 5 mag


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Una magnitud = factor {razon_flujo(1):.4f}; 5 magnitudes = {razon_flujo(5):.1f}; 10 magnitudes = {razon_flujo(10):.0f}")
    print(f"Dos estrellas de magnitud 5 juntas: {suma_magnitudes(5.0, 5.0):.4f}")
    print(f"Estrellas de magnitud 3,0 y 4,0 juntas: {suma_magnitudes(3.0, 4.0):.3f}")
    print(f"Sol / Luna llena: {razon_flujo(M_LUNA_LLENA - M_SOL):,.0f} veces (magnitudes {M_SOL} y {M_LUNA_LLENA})")
    print(f"Ganancia ideal con pupila de {PUPILA_MM:.0f} mm (SIMULADO):")
    for d in (35, 50, 70, 100, 200):
        g = ganancia_apertura_mag(d)
        print(f"  D = {d:3d} mm: +{g:.2f} mag -> magnitud limite ideal {LM_REFERENCIA + g:.1f}; area x{(d / PUPILA_MM) ** 2:.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
