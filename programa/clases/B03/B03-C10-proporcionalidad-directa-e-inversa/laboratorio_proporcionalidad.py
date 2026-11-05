#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C10: proporcionalidad directa e inversa con datos del Sistema Solar.

Datos PUBLICADOS: irradiancia solar nominal a 1 au S = 1361 W/m2 (IAU 2015 B3); semiejes mayores
de la NASA (Planetary Fact Sheets) y radios medios volumétricos de Tierra y Luna. Modelo: fuente
puntual, S(d) = k / d^2 con k = S(1 au) x (1 au)^2; circunferencia = 2*pi*R (directa).
Resultados de irradiancia: CALCULADOS (simulados con el modelo), no medidos. Supuestos: sin
atmósfera ni órbitas excéntricas. Validez: orden de magnitud. Tolerancia: 1e-9 en las pruebas.
"""
from __future__ import annotations

import math
import platform

S_1AU = 1361.0
AU_KM = 149_597_870.7
A_1E6KM = {"Mercurio": 57.909, "Venus": 108.210, "Tierra": 149.598, "Marte": 227.956,
           "Júpiter": 778.479, "Saturno": 1432.041, "Urano": 2867.043, "Neptuno": 4514.953}
R_KM = {"Tierra": 6371.0, "Luna": 1737.4}


def irradiancia(d_au: float) -> float:
    return S_1AU / d_au ** 2


def constante_directa(xs, ys):
    razones = [y / x for x, y in zip(xs, ys)]
    return razones


def pruebas() -> None:
    assert abs(irradiancia(2.0) - S_1AU / 4) < 1e-9 and abs(irradiancia(0.5) - 4 * S_1AU) < 1e-9
    ds = [a * 1e6 / AU_KM for a in A_1E6KM.values()]
    productos = [irradiancia(d) * d * d for d in ds]
    assert max(productos) - min(productos) < 1e-6          # S x d^2 es constante (inversa al cuadrado)
    c = constante_directa([R_KM["Tierra"], R_KM["Luna"]], [2 * math.pi * R_KM["Tierra"], 2 * math.pi * R_KM["Luna"]])
    assert abs(c[0] - c[1]) < 1e-9 and abs(c[0] - 2 * math.pi) < 1e-9     # circunferencia/radio = 2 pi


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"{'Planeta':9s} {'d [au]':>8s} {'S [W/m2]':>10s} {'S/S_Tierra':>10s}")
    for n, a in A_1E6KM.items():
        d = a * 1e6 / AU_KM
        print(f"{n:9s} {d:8.4f} {irradiancia(d):10.1f} {irradiancia(d) / S_1AU:10.4f}")
    print(f"Circunferencia/radio (Tierra y Luna): {2 * math.pi:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
