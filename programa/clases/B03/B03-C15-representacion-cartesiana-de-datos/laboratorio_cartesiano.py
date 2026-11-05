#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C15: representar pares (a, T) de los planetas en un plano cartesiano de texto.

Datos PUBLICADOS (NASA Planetary Fact Sheets: semieje mayor en 1e6 km y período sidéreo en días);
1 au = 149 597 870,7 km (SI); año terrestre 365,256 d. Modelo: transformar cada dato a la celda de
una rejilla de texto con escala lineal o logarítmica y comprobar que la transformación es
invertible. Supuestos: rejilla de 60 x 20 caracteres. Validez: ver la forma de los datos, no medirla.
Tolerancia: la inversa recupera el dato con error menor que media celda.
"""
from __future__ import annotations

import math
import platform

AU_KM = 149_597_870.7
ANIO_D = 365.256
DATOS = {"Mercurio": (57.909, 87.969), "Venus": (108.210, 224.701), "Tierra": (149.598, 365.256),
         "Marte": (227.956, 686.980), "Júpiter": (778.479, 4332.589), "Saturno": (1432.041, 10755.699),
         "Urano": (2867.043, 30685.400), "Neptuno": (4514.953, 60189.018)}
ANCHO, ALTO = 60, 20


def a_celda(v: float, vmin: float, vmax: float, n: int, log: bool) -> int:
    if log:
        v, vmin, vmax = math.log10(v), math.log10(vmin), math.log10(vmax)
    return round((v - vmin) / (vmax - vmin) * (n - 1))


def de_celda(i: int, vmin: float, vmax: float, n: int, log: bool) -> float:
    if log:
        lo, hi = math.log10(vmin), math.log10(vmax)
        return 10 ** (lo + i / (n - 1) * (hi - lo))
    return vmin + i / (n - 1) * (vmax - vmin)


def grafica(pares: dict[str, tuple[float, float]], log: bool) -> list[str]:
    xs = [p[0] for p in pares.values()]
    ys = [p[1] for p in pares.values()]
    xm, xM, ym, yM = min(xs) * (0.8 if log else 0), max(xs) * 1.1, min(ys) * (0.8 if log else 0), max(ys) * 1.1
    rej = [[" "] * ANCHO for _ in range(ALTO)]
    for i, (n, (x, y)) in enumerate(pares.items()):
        cx, cy = a_celda(x, xm, xM, ANCHO, log), a_celda(y, ym, yM, ALTO, log)
        rej[ALTO - 1 - cy][cx] = str(i + 1)     # 1 = Mercurio ... 8 = Neptuno
    return ["|" + "".join(f) for f in rej] + ["+" + "-" * ANCHO]


def pruebas() -> None:
    for log in (False, True):
        for v in (0.5, 3.0, 7.0, 29.0):
            i = a_celda(v, 0.1 if log else 0.0, 30.0, 61, log)
            w = de_celda(i, 0.1 if log else 0.0, 30.0, 61, log)
            media = (de_celda(min(i + 1, 60), 0.1 if log else 0.0, 30.0, 61, log) - de_celda(max(i - 1, 0), 0.1 if log else 0.0, 30.0, 61, log)) / 2
            assert abs(w - v) <= abs(media), (log, v, w)
    assert len(DATOS) == 8


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    pares = {n: (a * 1e6 / AU_KM, t / ANIO_D) for n, (a, t) in DATOS.items()}
    print("Leyenda: " + ", ".join(f"{i + 1} = {n}" for i, n in enumerate(pares)))
    for titulo, log in (("Escala lineal (a en au, T en años)", False), ("Escala logarítmica en ambos ejes", True)):
        print(f"\n{titulo}")
        print("\n".join(grafica(pares, log)))
    print("\nCSV (a_au,T_anios):")
    for n, (x, y) in pares.items():
        print(f"{n},{x:.4f},{y:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
