#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C14: despejar una fórmula y verificar por sustitución.

Datos: (GM) nominal de la Tierra 3,986004e14 m3 s-2 y (GM) nominal del Sol 1,3271244e20 m3 s-2
(IAU 2015 B3); velocidad de escape terrestre 11,186 km/s y radio medio 6371 km (NASA Earth Fact
Sheet); semieje terrestre 149,598e6 km y período sidéreo 365,256 d (NASA). Fórmulas DADAS (se
justifican en B05 y B71): v_esc = sqrt(2 GM / R) y T^2 = 4 pi^2 a^3 / GM. Modelo: dos cuerpos,
órbita circular o elíptica de semieje a. Validez: comprobación numérica de despejes. Tolerancia:
0,1 % frente a los datos de la NASA/IAU; 1e-9 en la verificación por sustitución.
"""
from __future__ import annotations

import math
import platform

GM_T = 3.986004e14
GM_S = 1.3271244e20
V_ESC = 11_186.0          # m/s (NASA)
R_T = 6.371e6             # m (NASA)
A_T = 149.598e9           # m
T_T = 365.256 * 86_400    # s


def v_escape(gm: float, r: float) -> float:
    return math.sqrt(2 * gm / r)


def r_desde_vesc(gm: float, v: float) -> float:
    return 2 * gm / v ** 2                       # despeje de R


def gm_desde_vesc(r: float, v: float) -> float:
    return v ** 2 * r / 2                        # despeje de GM


def gm_desde_kepler(a: float, t: float) -> float:
    return 4 * math.pi ** 2 * a ** 3 / t ** 2    # despeje de GM


def a_desde_kepler(gm: float, t: float) -> float:
    return (gm * t ** 2 / (4 * math.pi ** 2)) ** (1 / 3)   # despeje de a


def pruebas() -> None:
    # sustitución: lo despejado debe devolver el dato de partida
    r = r_desde_vesc(GM_T, V_ESC)
    assert abs(v_escape(GM_T, r) - V_ESC) / V_ESC < 1e-9
    gm = gm_desde_kepler(A_T, T_T)
    assert abs(a_desde_kepler(gm, T_T) - A_T) / A_T < 1e-9
    # contra los datos publicados
    assert abs(r - R_T) / R_T < 0.001, r
    assert abs(gm - GM_S) / GM_S < 0.001, gm
    assert 2 * 3 + 1 == 7 and (7 - 1) / 2 == 3        # operación inversa elemental


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    r = r_desde_vesc(GM_T, V_ESC)
    print(f"R desde v_esc y GM: {r / 1e3:.1f} km (NASA: 6371 km; dif. {abs(r - R_T) / R_T * 100:.3f} %)")
    print(f"GM_Tierra desde v_esc y R: {gm_desde_vesc(R_T, V_ESC):.5e} m3/s2 (IAU nominal {GM_T:.5e})")
    gm = gm_desde_kepler(A_T, T_T)
    print(f"GM_Sol desde la órbita terrestre: {gm:.5e} m3/s2 (IAU nominal {GM_S:.5e}; dif. {abs(gm - GM_S) / GM_S * 100:.3f} %)")
    print(f"a desde GM_Sol y T de la Tierra: {a_desde_kepler(GM_S, T_T) / 1e9:.3f} x 10^6 km (NASA: 149.598)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
