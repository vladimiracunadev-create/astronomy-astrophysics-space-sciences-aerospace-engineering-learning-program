#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C02: analisis dimensional y cadena de trazabilidad.

Datos: formulas estandar de mecanica orbital y de cohetes (sin cifras
medidas); valores de ejemplo SINTETICOS para la cadena de calibracion.
Modelo: cada magnitud lleva un vector de exponentes de las dimensiones base
(M masa, L longitud, T tiempo) con exponentes racionales; multiplicar suma
exponentes, elevar a una potencia los multiplica. Una ecuacion es
dimensionalmente consistente si ambos miembros tienen el mismo vector.
La cadena de trazabilidad se modela como incertidumbres tipicas que se
combinan en cuadratura (hipotesis de independencia; GUM 5.1.2 con c_i = 1).
Supuestos: solo dimensiones mecanicas; la consistencia dimensional es
necesaria, no suficiente (no detecta factores numericos como 2 o pi).
Tolerancia: igualdad exacta de exponentes; 1e-12 relativa en la cadena.
"""
from __future__ import annotations
import math
import platform
import sys
from fractions import Fraction


class Dim:
    def __init__(self, m=0, l=0, t=0):
        self.v = (Fraction(m), Fraction(l), Fraction(t))

    def __mul__(self, o):
        return Dim(*[a + b for a, b in zip(self.v, o.v)])

    def __truediv__(self, o):
        return Dim(*[a - b for a, b in zip(self.v, o.v)])

    def __pow__(self, p):
        p = Fraction(p)
        return Dim(*[a * p for a in self.v])

    def __eq__(self, o):
        return self.v == o.v

    def __repr__(self):
        nombres = ("M", "L", "T")
        partes = [f"{n}^{e}" for n, e in zip(nombres, self.v) if e != 0]
        return " ".join(partes) if partes else "1 (adimensional)"


M, L, T = Dim(1, 0, 0), Dim(0, 1, 0), Dim(0, 0, 1)
ADIM = Dim()
VEL = L / T
ACEL = L / (T ** 2)
FUERZA = M * ACEL
GM = (L ** 3) / (T ** 2)


def cadena_trazabilidad(u_pasos):
    """Incertidumbre tipica combinada de una cadena de calibraciones (cuadratura)."""
    return math.sqrt(sum(u * u for u in u_pasos))


def main() -> None:
    print(f"Python {platform.python_version()} (sin bibliotecas externas)")
    # Ecuaciones consistentes
    assert GM / (L ** 2) == ACEL                    # g = GM/r^2
    assert (GM / L) ** Fraction(1, 2) == VEL        # v = sqrt(GM/r)
    assert (L ** 3 / GM) ** Fraction(1, 2) == T     # P ~ sqrt(a^3/GM)
    assert VEL * (M / M) == VEL                     # Tsiolkovsky: v_e ln(m0/m)
    assert M * ACEL == FUERZA
    print("GM/r^2 ->", GM / (L ** 2), "| sqrt(GM/r) ->", (GM / L) ** Fraction(1, 2))
    # Ecuacion INCONSISTENTE a proposito (error tipico): v = GM/r
    malo = GM / L
    print("GM/r (mal) ->", malo, "| coincide con velocidad:", malo == VEL)
    assert malo != VEL
    # Cadena de trazabilidad SINTETICA (valores relativos en ppm)
    u = [0.10, 0.30, 0.50, 1.00]    # patron primario, patron nacional, laboratorio, instrumento
    uc = cadena_trazabilidad(u)
    print(f"cadena {u} ppm -> u_c = {uc:.4f} ppm")
    assert abs(uc - math.sqrt(0.01 + 0.09 + 0.25 + 1.0)) < 1e-12
    # Cada eslabon solo puede empeorar la incertidumbre
    acumulada = [cadena_trazabilidad(u[: i + 1]) for i in range(len(u))]
    assert all(b >= a for a, b in zip(acumulada, acumulada[1:]))
    print("acumulada por eslabon:", [round(x, 4) for x in acumulada])
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una prueba no se cumple")
        sys.exit(1)
