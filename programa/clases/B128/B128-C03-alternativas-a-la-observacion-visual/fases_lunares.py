#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C03: las fases de la Luna en texto, tabla y relieve (alternativas equivalentes).

Modelo (relacion geometrica estandar, verificada aqui por una segunda via): fraccion iluminada del disco
k = (1 - cos e) / 2, con e la elongacion Luna-Sol vista desde la Tierra (e = 0 luna nueva, e = 180 luna llena).
Unidades: grados y fraccion adimensional. Sistema: elongacion geocentrica, aproximacion de orbita circular.
Datos: las ocho elongaciones (0,45,...,315) son una DISCRETIZACION didactica; no son efemerides de fechas reales.
Segunda via: k por integracion numerica del ancho de la franja iluminada fila a fila (valida la integracion y el codigo; no es una prueba independiente de la geometria).
Tolerancia: 1e-4 entre las dos vias. Relieve: 5 niveles (0-4) por redondeo de k*4; la escala de relieve es ILUSTRATIVA.
"""
from __future__ import annotations
import math, platform

NOMBRES = {0: "nueva", 45: "creciente iluminada", 90: "cuarto creciente", 135: "gibosa creciente",
           180: "llena", 225: "gibosa menguante", 270: "cuarto menguante", 315: "menguante iluminada"}


def k_formula(e_deg: float) -> float:
    return (1.0 - math.cos(math.radians(e_deg))) / 2.0


def k_integral(e_deg: float, n: int = 20000) -> float:
    """Disco unitario: franja iluminada por filas. Terminador = elipse con semieje x = cos(e)*sqrt(1-y^2)."""
    e = math.radians(e_deg)
    area = 0.0
    dy = 2.0 / n
    for i in range(n):
        y = -1.0 + (i + 0.5) * dy
        w = math.sqrt(max(0.0, 1.0 - y * y))
        # el terminador es una elipse; nueva (e=0) => ancho 0; llena (e=180) => ancho 2w
        ancho = w * (1.0 - math.cos(e))
        area += ancho * dy
    return area / math.pi


def nivel_relieve(k: float, niveles: int = 4) -> int:
    return int(round(k * niveles))


def describir(e: int, k: float) -> str:
    lado = "derecha" if e < 180 else "izquierda"
    if e == 0:
        return "Disco oscuro, sin parte iluminada."
    if e == 180:
        return "Disco completo iluminado."
    return f"Parte iluminada de {k*100:.0f} % del disco, a la {lado} (hemisferio norte)."


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Discretizacion DIDACTICA de ocho elongaciones; no son efemerides de fechas reales.")
    print(" elong  fase                    k formula   k integral   nivel  relieve  descripcion")
    for e, nombre in NOMBRES.items():
        k, ki = k_formula(e), k_integral(e)
        assert abs(k - ki) < 1e-4, (e, k, ki)
        n = nivel_relieve(k)
        print(f"{e:5d}  {nombre:22s}  {k:9.4f}  {ki:11.4f}  {n:5d}  {'#'*n:7s}  {describir(e, k)}")
    # equivalencia: cada modalidad debe permitir ordenar las 8 fases de la menos a la mas iluminada
    ks = [k_formula(e) for e in NOMBRES]
    por_texto = sorted(NOMBRES, key=lambda e: round(k_formula(e) * 100))
    por_relieve = sorted(NOMBRES, key=lambda e: (nivel_relieve(k_formula(e)), e))
    print("Orden por texto (porcentaje):", por_texto)
    print("Orden por relieve (5 niveles):", por_relieve)
    distintos_relieve = len({nivel_relieve(k) for k in ks})
    print(f"Niveles de relieve distintos: {distintos_relieve} de 8 fases (el relieve pierde resolucion; se compensa con tabla y texto)")
    assert distintos_relieve == 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
