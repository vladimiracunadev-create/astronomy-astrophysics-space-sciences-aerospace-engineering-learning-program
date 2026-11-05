#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C09: números negativos en cuenta regresiva, tiempo de luz y energía ligada.

Datos: GM nominal de la Tierra 3,986004e14 m3 s-2 (IAU 2015 B3); semieje lunar 384 400 km y
velocidad orbital media 1,022 km/s (NASA Moon Fact Sheet); 1 au = 149 597 870 700 m y c = 299 792 458
m/s (SI). La cuenta regresiva es SINTÉTICA (ejemplo didáctico). Modelo: energía específica de una
órbita ligada e = v^2/2 - GM/r = -GM/(2a). Supuestos: dos cuerpos, órbita circular o casi. Validez:
estimación del signo y del orden de magnitud. Tolerancia: 1 % entre las dos formas de e.
"""
from __future__ import annotations

import platform

GM_T = 3.986004e14
A_LUNA = 3.844e8
V_LUNA = 1.022e3
AU = 149_597_870_700
C = 299_792_458


def energia_especifica_vis_viva(v: float, r: float) -> float:
    return 0.5 * v * v - GM_T / r


def energia_especifica_semieje(a: float) -> float:
    return -GM_T / (2 * a)


def t_evento(t_obs: float, distancia_m: float) -> float:
    """Tiempo del evento = tiempo observado - tiempo de luz (resta; resultado anterior al observado)."""
    return t_obs - distancia_m / C


def formato_t(segundos: int) -> str:
    signo = "T-" if segundos < 0 else "T+"
    s = abs(segundos)
    return f"{signo}{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def pruebas() -> None:
    assert (-3) + 5 == 2 and (-3) - 5 == -8 and (-3) * (-5) == 15 and (-12) / 4 == -3
    assert 5 - (-3) == 8 and abs(-7.5) == 7.5
    e1, e2 = energia_especifica_vis_viva(V_LUNA, A_LUNA), energia_especifica_semieje(A_LUNA)
    assert e1 < 0 and e2 < 0                                   # órbita ligada
    assert abs(e1 - e2) / abs(e2) < 0.01, (e1, e2)
    assert formato_t(-600) == "T-00:10:00" and formato_t(75) == "T+00:01:15"
    assert abs(t_evento(0.0, AU) + 499.0047838) < 1e-6          # el evento fue 499 s antes


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    e1 = energia_especifica_vis_viva(V_LUNA, A_LUNA)
    e2 = energia_especifica_semieje(A_LUNA)
    print(f"e (v^2/2 - GM/r) = {e1:.4e} J/kg; e (-GM/2a) = {e2:.4e} J/kg; dif. rel. = {abs(e1 - e2) / abs(e2) * 100:.2f} %")
    print(f"Energía cinética específica: {0.5 * V_LUNA ** 2:.4e} J/kg; potencial: {-GM_T / A_LUNA:.4e} J/kg")
    print(f"Tiempo del evento si t_obs = 0 s y d = 1 au: {t_evento(0.0, AU):.3f} s")
    print(f"Cuenta regresiva (sintética): {formato_t(-600)} ... {formato_t(0)} ... {formato_t(75)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
