#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C13: modelo a escala del sistema solar y comprobación de la tercera ley de Kepler.

Datos PUBLICADOS (NASA NSSDC Planetary Fact Sheet, act. 18-mar-2025; Sun Fact Sheet,
act. 9-may-2024; Earth Fact Sheet): distancia al Sol [10^6 km], período orbital [d],
diámetro [km], masa [10^24 kg]. Constantes: 1 au = 149 597 870 700 m (exacta) y
GM_sol nominal = 1,3271244e20 m^3/s^2 (IAU 2015 B3, exacta por convención).
Modelo: (1) escala lineal 1 au = 1 m; (2) T²/a³ ≈ 1 (T en años, a en au) y, como referencia
independiente, T = 2π sqrt(a³/GM) para órbita circular alrededor del Sol.
Supuestos: órbitas casi circulares (excentricidades ≤ 0,21 para los 8 planetas) y masa
planetaria despreciable frente a la solar. Dominio de validez: planetas del sistema solar
con las cifras de la ficha (3–4 cifras). Tolerancias: razón T²/a³ dentro del 3 % de 1 (la fila de la ficha no se rotula como semieje mayor; Neptuno es el peor caso); período de
la Tierra por Kepler frente a la ficha, 0,1 %.
"""

from __future__ import annotations

import math
import platform
import sys

AU_M = 149_597_870_700
GM_SOL = 1.3271244e20          # m^3/s^2
ANIO_D = 365.25                # d (año juliano, convención)
# (nombre, distancia 1e6 km, período d, diámetro km, masa 1e24 kg)
PLANETAS = [
    ("Mercurio", 57.9, 88.0, 4879, 0.330),
    ("Venus", 108.2, 224.7, 12104, 4.87),
    ("Tierra", 149.6, 365.2, 12756, 5.97),
    ("Marte", 228.0, 687.0, 6792, 0.642),
    ("Júpiter", 778.5, 4331, 142984, 1898),
    ("Saturno", 1432.0, 10747, 120536, 568),
    ("Urano", 2867.0, 30589, 51118, 86.8),
    ("Neptuno", 4515.0, 59800, 49528, 102),
]
SOL_DIAM_KM = 2 * 695_700
SOL_MASA = 1_988_400.0         # 1e24 kg


def razon_kepler(a_millones_km: float, t_dias: float) -> float:
    a_au = a_millones_km * 1e6 / (AU_M / 1000)
    return (t_dias / ANIO_D) ** 2 / a_au**3


def pruebas() -> None:
    for nombre, a, t, _, _ in PLANETAS:
        r = razon_kepler(a, t)
        assert abs(r - 1) < 0.03, (nombre, r)                     # T²/a³ ≈ 1 en cada planeta
    t_teo = 2 * math.pi * math.sqrt(AU_M**3 / GM_SOL) / 86_400    # referencia independiente (IAU GM)
    assert abs(t_teo - 365.256) / 365.256 < 1e-3, t_teo           # Tierra: ficha 365,256 d
    assert abs(sum(m for *_, m in PLANETAS) / SOL_MASA - 0.00134) < 2e-5


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    t_teo = 2 * math.pi * math.sqrt(AU_M**3 / GM_SOL) / 86_400
    print(f"Período circular a 1 au con GM nominal: {t_teo:.2f} d (ficha: 365,256 d)")
    print("Escala 1 au = 1 m:")
    print(f"  Sol: diámetro {SOL_DIAM_KM * 1e3 / (AU_M / 1000) :.2f} mm")
    for nombre, a, t, d, m in PLANETAS:
        a_au = a * 1e6 / (AU_M / 1000)
        print(f"  {nombre:9s} a = {a_au:6.2f} au -> {a_au:6.2f} m | diám. {d * 1e3 / (AU_M / 1000):.3f} mm | T²/a³ = {razon_kepler(a, t):.4f}")
    masa = sum(m for *_, m in PLANETAS)
    print(f"Masa de los 8 planetas = {masa:.1f}e24 kg = {masa / SOL_MASA * 100:.3f} % de la solar; Júpiter = {1898 / masa * 100:.1f} % de los planetas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
