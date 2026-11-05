#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C15: la «prueba de la Luna» con datos actuales.

Datos PUBLICADOS (NASA NSSDC, consultadas el 2026-11-05): radio medio de la Tierra 6 371,0 km y
gravedad media en superficie 9,820 m/s² (Earth Fact Sheet, act. 15-nov-2024); semieje mayor de la
Luna 384,4x10^3 km y período sidéreo 27,3217 d (Moon Fact Sheet, act. 11-ene-2024); semiejes y
períodos de los satélites galileanos (Jovian Satellite Fact Sheet, act. 6-dic-2023).
Modelo: órbita circular y atracción proporcional a 1/r^2. Supuestos: la Tierra y Júpiter como
masas puntuales; la masa de la Luna y de los satélites es despreciable. Validez: ~1 %.
Tolerancias: 2 % en la prueba de la Luna; 0,5 % en la constancia de a^3/T^2 (Júpiter).
"""

from __future__ import annotations

import math
import sys

R_TIERRA = 6371.0e3        # m
G_SUP = 9.820              # m/s²
A_LUNA = 384.4e6           # m
T_LUNA = 27.3217 * 86400   # s
JOVIANOS = {
    "Ío": (421.8e6, 1.769138 * 86400),
    "Europa": (671.1e6, 3.551181 * 86400),
    "Ganimedes": (1070.4e6, 7.154553 * 86400),
    "Calisto": (1882.7e6, 16.689017 * 86400),
}


def aceleracion_centripeta(a: float, t: float) -> float:
    return 4.0 * math.pi**2 * a / t**2


def pruebas() -> None:
    assert abs(aceleracion_centripeta(1.0, 2 * math.pi) - 1.0) < 1e-12          # caso analítico: omega = 1
    pred = G_SUP * (R_TIERRA / A_LUNA) ** 2
    real = aceleracion_centripeta(A_LUNA, T_LUNA)
    assert abs(pred / real - 1.0) < 0.02, (pred, real)                           # prueba de la Luna
    gm = [4 * math.pi**2 * a**3 / t**2 for a, t in JOVIANOS.values()]
    assert max(gm) / min(gm) - 1.0 < 0.005                                       # GM constante


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    pred = G_SUP * (R_TIERRA / A_LUNA) ** 2
    real = aceleracion_centripeta(A_LUNA, T_LUNA)
    print(f"Distancia Luna/radio Tierra: {A_LUNA / R_TIERRA:.2f}  (cuadrado: {(A_LUNA / R_TIERRA) ** 2:.0f})")
    print(f"Aceleración predicha por 1/r²: {pred:.4e} m/s²")
    print(f"Aceleración centrípeta de la Luna: {real:.4e} m/s²")
    print(f"Razón predicha/medida: {pred / real:.4f}")
    print("GM de Júpiter implícito (4π²a³/T²) por satélite:")
    for n, (a, t) in JOVIANOS.items():
        print(f"  {n:9s} {4 * math.pi**2 * a**3 / t**2:.5e} m³/s²")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
