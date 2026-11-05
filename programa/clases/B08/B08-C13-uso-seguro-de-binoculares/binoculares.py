#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C13: qué números de unos binoculares importan.

Datos: especificaciones tipo «MxD» (aumento M, objetivo D mm), entre 7x35 y 10x50 recomendadas por NASA Night Sky
Network (consultada 2026-11-05) más 15x70 como caso grande. Modelo (SIMULADO): pupila de salida = D/M; apertura efectiva =
min(D, M*pupila_ojo); campo real = campo aparente / M (campo aparente SUPUESTO de 60 grados, valor de ejemplo, no de fuente);
ganancia ideal 5 log10(D_efectiva / pupila_ojo) en magnitud límite de fuente puntual (C11). Pupila del ojo SUPUESTA de 7 mm (joven,
dilatada) o 5 mm (ejemplo). Dominio: binoculares sin pérdidas, fuentes puntuales. Tolerancias: exactitud analítica 1e-9.
Prueba independiente: casos analíticos (7x50 -> pupila 7,142857 mm; 10x50 -> 5 mm) y la regla de que
una apertura 10 veces mayor que la pupila gana exactamente 5 magnitudes.
"""
from __future__ import annotations

import math
import sys

CAMPO_APARENTE_DEG = 60.0     # supuesto de ejemplo


def pupila_salida_mm(m: float, d_mm: float) -> float:
    return d_mm / m


def apertura_efectiva_mm(m: float, d_mm: float, pupila_ojo_mm: float) -> float:
    return min(d_mm, m * pupila_ojo_mm)


def ganancia_mag(m: float, d_mm: float, pupila_ojo_mm: float) -> float:
    return 5.0 * math.log10(apertura_efectiva_mm(m, d_mm, pupila_ojo_mm) / pupila_ojo_mm)


def campo_real_deg(m: float, campo_aparente: float = CAMPO_APARENTE_DEG) -> float:
    return campo_aparente / m


def pruebas() -> None:
    assert abs(pupila_salida_mm(7, 50) - 50 / 7) < 1e-12
    assert abs(pupila_salida_mm(10, 50) - 5.0) < 1e-12
    assert abs(5.0 * math.log10(70.0 / 7.0) - 5.0) < 1e-9                 # 10x la pupila = 5 magnitudes
    assert abs(apertura_efectiva_mm(7, 50, 5.0) - 35.0) < 1e-12           # ojo de 5 mm con 7x50: se aprovechan solo 35 mm
    assert abs(campo_real_deg(10) - 6.0) < 1e-12


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Modelo SIMULADO. campo aparente supuesto 60 grados; pupila del ojo 7 mm / 5 mm")
    print("MxD    | pupila salida | campo real | D efectiva (7|5 mm) | ganancia ideal respecto del ojo con esa pupila (7|5 mm)")
    for m, d in [(7, 35), (7, 50), (8, 42), (10, 50), (15, 70)]:
        print(f"{m:2d}x{d:<3d} | {pupila_salida_mm(m, d):6.2f} mm | {campo_real_deg(m):5.1f} gr | "
              f"{apertura_efectiva_mm(m, d, 7.0):4.0f} | {apertura_efectiva_mm(m, d, 5.0):4.0f} mm | "
              f"+{ganancia_mag(m, d, 7.0):.2f} | +{ganancia_mag(m, d, 5.0):.2f} mag")
    luna = 0.5 * 10
    print(f"La Luna (0,5 grados) vista con aumento 10 ocupa {luna:.1f} grados de campo aparente: {luna / CAMPO_APARENTE_DEG * 100:.0f} % de un campo de {CAMPO_APARENTE_DEG:.0f} grados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
