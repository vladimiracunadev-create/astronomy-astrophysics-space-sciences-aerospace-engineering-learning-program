#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C01: un algoritmo de búsqueda del máximo, con traza.

Datos PUBLICADOS (observados/estimados por NASA): períodos orbitales sidéreos en días,
NASA NSSDC, fichas individuales de planetas (Mercury…Neptune Fact Sheet; act. 11-ene-2024 a 19-may-2025), consultadas el 2026-11-05.
Modelo: ninguno físico; solo se estudia el procedimiento de búsqueda.
Supuestos: la lista no está vacía y los números son comparables.
Dominio de validez: cualquier lista no vacía de pares (nombre, número).
Tolerancia: exactitud entera en los conteos; los valores se comparan sin redondear.
"""

from __future__ import annotations

import sys

PERIODOS_DIAS = [
    ("Mercurio", 87.969),
    ("Venus", 224.701),
    ("Tierra", 365.256),
    ("Marte", 686.98),
    ("Júpiter", 4332.589),
    ("Saturno", 10755.699),
    ("Urano", 30685.4),
    ("Neptuno", 60189.018),
]


def buscar_maximo(pares):
    """Devuelve (nombre, valor, comparaciones) del par con el valor mayor."""
    mejor_nombre, mejor_valor = pares[0]
    comparaciones = 0
    for nombre, valor in pares[1:]:
        comparaciones += 1
        if valor > mejor_valor:
            mejor_nombre, mejor_valor = nombre, valor
    return mejor_nombre, mejor_valor, comparaciones


def contar_mayores(pares, umbral):
    """Cuenta cuántos valores superan estrictamente el umbral."""
    total = 0
    for _, valor in pares:
        if valor > umbral:
            total += 1
    return total


def pruebas() -> None:
    assert buscar_maximo([("a", 5.0)]) == ("a", 5.0, 0)            # un solo elemento
    assert buscar_maximo([("a", 1.0), ("b", 3.0), ("c", 2.0)])[:2] == ("b", 3.0)
    assert buscar_maximo(PERIODOS_DIAS) == ("Neptuno", 60189.018, 7)  # n-1 comparaciones
    assert contar_mayores(PERIODOS_DIAS, 365.256) == 5               # estrictamente mayores
    assert contar_mayores(PERIODOS_DIAS, 0.0) == 8
    assert contar_mayores([], 1.0) == 0                            # lista vacía


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    nombre, valor, comparaciones = buscar_maximo(PERIODOS_DIAS)
    print(f"Mayor período: {nombre} con {valor} d tras {comparaciones} comparaciones")
    print("Traza del algoritmo:")
    mejor = PERIODOS_DIAS[0][1]
    for nombre, valor in PERIODOS_DIAS[1:]:
        if valor > mejor:
            mejor = valor
            marca = "nuevo máximo"
        else:
            marca = "sin cambio"
        print(f"  {nombre:<8} {valor:>10.3f}  máximo actual {mejor:>10.3f}  {marca}")
    print("Planetas con período mayor que el de la Tierra:",
          contar_mayores(PERIODOS_DIAS, 365.256))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
