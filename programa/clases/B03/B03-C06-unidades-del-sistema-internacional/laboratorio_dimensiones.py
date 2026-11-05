#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C06: análisis dimensional con exponentes de m, kg y s.

Datos PUBLICADOS: GM nominal de la Tierra 3,986004e14 m3 s-2 y radios nominales (IAU 2015 B3);
radio medio volumétrico 6371 km, g medio 9,820 m/s2 y v de escape 11,186 km/s (NASA Earth Fact
Sheet, 15-nov-2024); masa del Sol 1,9884e30 kg y volumen 1,412e18 km3 (NASA Sun Fact Sheet,
9-may-2024). Modelo: cada unidad coherente del SI es un producto m^a kg^b s^c; multiplicar suma
exponentes y dividir los resta. Supuestos: magnitudes sin ángulos ni temperatura. Validez:
comprobación de coherencia, no sustituye el cálculo. Tolerancia: 0,1 % en g; 0,05 % en v de escape.
"""
from __future__ import annotations

import math
import platform

Dim = tuple[int, int, int]    # exponentes de (m, kg, s)
M, KG, S = (1, 0, 0), (0, 1, 0), (0, 0, 1)


def mul(a: Dim, b: Dim) -> Dim:
    return tuple(x + y for x, y in zip(a, b))        # type: ignore[return-value]


def div(a: Dim, b: Dim) -> Dim:
    return tuple(x - y for x, y in zip(a, b))        # type: ignore[return-value]


def pot(a: Dim, n: int) -> Dim:
    return tuple(n * x for x in a)                   # type: ignore[return-value]


VEL = div(M, S)
ACEL = div(VEL, S)
FUERZA = mul(KG, ACEL)                               # newton
ENERGIA = mul(FUERZA, M)                             # julio
POTENCIA = div(ENERGIA, S)                           # vatio
G_DIM = div(mul(pot(M, 3), pot(KG, -1)), pot(S, 2))  # m3 kg-1 s-2
GM_DIM = mul(G_DIM, KG)                              # m3 s-2

GM_TIERRA = 3.986004e14          # m3 s-2 (IAU 2015 B3, nominal)
R_MEDIO = 6.371e6                # m (NASA)


def pruebas() -> None:
    assert FUERZA == (1, 1, -2) and ENERGIA == (2, 1, -2) and POTENCIA == (2, 1, -3)
    assert GM_DIM == (3, 0, -2)
    assert div(GM_DIM, pot(M, 2)) == ACEL                    # GM / R^2 es una aceleración
    assert div(GM_DIM, M) == (2, 0, -2) == pot(VEL, 2)        # GM/R tiene dimensión de v^2
    g = GM_TIERRA / R_MEDIO ** 2
    assert abs(g - 9.820) / 9.820 < 0.001, g                 # NASA: 9,820 m/s2
    v = math.sqrt(2 * GM_TIERRA / R_MEDIO)
    assert abs(v - 11186.0) / 11186.0 < 0.0005, v            # NASA: 11,186 km/s
    rho = 1.9884e30 / (1.412e18 * 1e9)                       # km3 -> m3
    assert abs(rho - 1408) / 1408 < 0.002, rho               # NASA: 1408 kg/m3


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"Dimensión de G: m^{G_DIM[0]} kg^{G_DIM[1]} s^{G_DIM[2]}")
    print(f"Dimensión de GM: m^{GM_DIM[0]} kg^{GM_DIM[1]} s^{GM_DIM[2]}")
    print(f"g = GM/R^2 = {GM_TIERRA / R_MEDIO ** 2:.3f} m/s^2 (NASA: 9,820)")
    print(f"v_escape = sqrt(2GM/R) = {math.sqrt(2 * GM_TIERRA / R_MEDIO) / 1000:.3f} km/s (NASA: 11,186)")
    print(f"Densidad media del Sol = {1.9884e30 / (1.412e18 * 1e9):.0f} kg/m^3 (NASA: 1408)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
