#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C04: potencias y raíces con la tercera ley de Kepler.

Datos PUBLICADOS (NASA NSSDC Planetary Fact Sheets: semieje mayor en 1e6 km y período
sidéreo en días; act. entre ene-2024 y may-2025). au = 149 597 870 700 m (SI, tabla 8).
Modelo: T^2 = a^3, con T en años (sidéreo terrestre: 365,256 d) y a en au. Supuestos:
órbitas keplerianas y masa planetaria despreciable frente a la solar. Validez: los ocho
planetas, no efemérides. Tolerancia: 1,5 % en T^2/a^3 (hay perturbaciones mutuas).
"""
from __future__ import annotations

import platform

AU_KM = 149_597_870.7
ANIO_D = 365.256
DATOS = {  # a [1e6 km], T [d]
    "Mercurio": (57.909, 87.969), "Venus": (108.210, 224.701), "Tierra": (149.598, 365.256),
    "Marte": (227.956, 686.980), "Júpiter": (778.479, 4332.589), "Saturno": (1432.041, 10755.699),
    "Urano": (2867.043, 30685.400), "Neptuno": (4514.953, 60189.018),
}


def raiz_n(x: float, n: int) -> float:
    return x ** (1 / n)


def pruebas() -> None:
    assert 2 ** 3 == 8 and 2 ** -2 == 0.25 and 5 ** 0 == 1
    assert abs(raiz_n(27, 3) - 3) < 1e-12 and abs(4 ** 1.5 - 8) < 1e-12
    for nombre, (a, t) in DATOS.items():
        au, anios = a * 1e6 / AU_KM, t / ANIO_D
        assert abs(anios ** 2 / au ** 3 - 1) < 0.015, nombre


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"{'Planeta':9s} {'a [au]':>8s} {'T [año]':>9s} {'a^1,5':>9s} {'T^2/a^3':>8s}")
    for n, (a, t) in DATOS.items():
        au, an = a * 1e6 / AU_KM, t / ANIO_D
        print(f"{n:9s} {au:8.4f} {an:9.3f} {au ** 1.5:9.3f} {an ** 2 / au ** 3:8.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
