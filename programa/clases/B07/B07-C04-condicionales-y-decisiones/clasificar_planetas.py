#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C04: condicionales para clasificar planetas con reglas explícitas.

Datos PUBLICADOS: NASA NSSDC, fichas individuales de planetas (act. 11-ene-2024 a
19-may-2025), consultadas el 2026-11-05: radio ecuatorial (km) y período sidéreo (d).
Modelo: dos reglas DIDÁCTICAS propias (no son definiciones de la IAU ni de NASA):
  - tamaño: «grande» si el diámetro supera 20 000 km, si no «pequeño»;
  - posición: «interior» si el período es menor que el de la Tierra, «exterior» si es mayor.
Supuestos: umbrales elegidos para separar los ocho planetas; otro umbral daría otra clasificación.
Dominio de validez: solo estos ocho planetas. Tolerancia: la Tierra se reconoce con math.isclose.
"""

from __future__ import annotations

import math
import sys

UMBRAL_DIAMETRO_KM = 20_000.0
PERIODO_TIERRA_D = 365.256

PLANETAS = [  # (nombre, radio ecuatorial en km, período sidéreo en d)
    ("Mercurio", 2440.5, 87.969), ("Venus", 6051.8, 224.701), ("Tierra", 6378.137, 365.256),
    ("Marte", 3396.2, 686.980), ("Júpiter", 71492.0, 4332.589), ("Saturno", 60268.0, 10755.699),
    ("Urano", 25559.0, 30685.400), ("Neptuno", 24764.0, 60189.018),
]


def clasificar_tamano(diametro_km: float) -> str:
    """Devuelve 'grande' o 'pequeño' según el umbral didáctico."""
    if diametro_km > UMBRAL_DIAMETRO_KM:
        return "grande"
    return "pequeño"


def clasificar_posicion(periodo_d: float) -> str:
    """Devuelve 'interior', 'exterior' o 'igual a la Tierra'."""
    if math.isclose(periodo_d, PERIODO_TIERRA_D):
        return "igual a la Tierra"
    elif periodo_d < PERIODO_TIERRA_D:
        return "interior"
    else:
        return "exterior"


def pruebas() -> None:
    assert clasificar_tamano(20_000.0) == "pequeño"          # el umbral exacto no es «mayor que»
    assert clasificar_tamano(20_000.1) == "grande"
    assert clasificar_posicion(365.256) == "igual a la Tierra"
    assert clasificar_posicion(224.701) == "interior"
    assert clasificar_posicion(686.98) == "exterior"
    grandes = [n for n, r, _ in PLANETAS if clasificar_tamano(2 * r) == "grande"]
    assert grandes == ["Júpiter", "Saturno", "Urano", "Neptuno"]
    interiores = [n for n, _, t in PLANETAS if clasificar_posicion(t) == "interior"]
    assert interiores == ["Mercurio", "Venus"]


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    for nombre, radio, periodo in PLANETAS:
        diametro = 2 * radio
        print(f"{nombre:<9} {diametro:>9.1f} km  {clasificar_tamano(diametro):<8} {clasificar_posicion(periodo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
