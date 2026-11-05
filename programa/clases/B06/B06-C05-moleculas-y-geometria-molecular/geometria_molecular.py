#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C05: ángulos de enlace desde coordenadas y suma de dipolos de enlace.

Datos PUBLICADOS: NIST CCCBDB (Release 22, mayo 2022), geometría experimental del
agua: r(O-H) = 0,958 A y ángulo H-O-H = 104,4776 +- 0,0019 grados (Hoy y Bunker,
J. Mol. Spectrosc. 74, 1, 1979). Las demás geometrías son IDEALES (sintéticas,
de modelo): lineal 180 grados y tetraedro regular arccos(-1/3).
Modelo: moléculas rígidas, átomos como puntos; dipolo de enlace = vector unitario
(todos los enlaces con la misma polaridad, solo para comparar geometrías).
Dominio de validez: comparación cualitativa de simetría, no momentos dipolares reales.
Tolerancia: 1e-9 grados en las pruebas geométricas.
"""

from __future__ import annotations

import math
import sys

R_OH_A = 0.958             # A, CCCBDB (agua)
ANG_HOH = 104.4776         # grados, CCCBDB (agua)


def angulo(a, centro, b) -> float:
    """Ángulo a-centro-b en grados a partir de coordenadas cartesianas."""
    u = [x - c for x, c in zip(a, centro)]
    v = [x - c for x, c in zip(b, centro)]
    cos = sum(p * q for p, q in zip(u, v)) / (math.hypot(*u) * math.hypot(*v))
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))


def agua(r: float = R_OH_A, theta: float = ANG_HOH):
    medio = math.radians(theta) / 2
    return (0, 0, 0), (r * math.sin(medio), r * math.cos(medio), 0), (-r * math.sin(medio), r * math.cos(medio), 0)


def dipolo_neto(vectores) -> float:
    """Módulo de la suma de vectores unitarios de enlace (centro en el origen)."""
    unit = []
    for v in vectores:
        n = math.hypot(*v)
        unit.append([x / n for x in v])
    return math.hypot(*[sum(c) for c in zip(*unit)])


def pruebas() -> None:
    o, h1, h2 = agua()
    assert abs(angulo(h1, o, h2) - ANG_HOH) < 1e-9                       # recupera el ángulo
    assert abs(math.dist(o, h1) - R_OH_A) < 1e-12                         # y la distancia
    tetra = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    ang_t = math.degrees(math.acos(-1 / 3))
    assert abs(angulo(tetra[0], (0, 0, 0), tetra[1]) - ang_t) < 1e-9      # tetraedro: 109,4712
    assert abs(angulo((1, 0, 0), (0, 0, 0), (-1, 0, 0)) - 180) < 1e-9     # lineal
    assert dipolo_neto(tetra) < 1e-12                                     # CH4 ideal: neto 0
    assert dipolo_neto([(1, 0, 0), (-1, 0, 0)]) < 1e-12                   # CO2 lineal: neto 0


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    o, h1, h2 = agua()
    print(f"Agua: H-H = {math.dist(h1, h2):.4f} A ; ángulo = {angulo(h1, o, h2):.4f} grados")
    ang_t = math.degrees(math.acos(-1 / 3))
    print(f"Tetraedro ideal: {ang_t:.4f} grados ; diferencia con el agua: {ang_t - ANG_HOH:.2f} grados")
    print(f"Dipolo neto relativo: H2O = {dipolo_neto([h1, h2]):.4f} ; CO2 (lineal) = 0 ; CH4 (tetraedro) = 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
