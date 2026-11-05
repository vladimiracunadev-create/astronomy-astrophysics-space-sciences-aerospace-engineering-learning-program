#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C07: listas, tuplas, diccionarios y conjuntos con datos planetarios.

Datos PUBLICADOS: NASA NSSDC, fichas individuales de planetas (act. 11-ene-2024 a
19-may-2025), consultadas el 2026-11-05: masa (1e24 kg) y radio ecuatorial (km).
Modelo: ninguno físico; se estudian estructuras de datos de Python.
Supuestos: los datos se transcriben tal como se publican (sin redondear más).
Dominio de validez: los ocho planetas. Tolerancia: conteos exactos; sumas con isclose.
"""

from __future__ import annotations

import math
import sys

PLANETAS = [  # lista de diccionarios: un registro por planeta
    {"nombre": "Mercurio", "masa_1e24kg": 0.33010, "radio_eq_km": 2440.5},
    {"nombre": "Venus", "masa_1e24kg": 4.8673, "radio_eq_km": 6051.8},
    {"nombre": "Tierra", "masa_1e24kg": 5.9722, "radio_eq_km": 6378.137},
    {"nombre": "Marte", "masa_1e24kg": 0.64169, "radio_eq_km": 3396.2},
    {"nombre": "Júpiter", "masa_1e24kg": 1898.13, "radio_eq_km": 71492.0},
    {"nombre": "Saturno", "masa_1e24kg": 568.32, "radio_eq_km": 60268.0},
    {"nombre": "Urano", "masa_1e24kg": 86.811, "radio_eq_km": 25559.0},
    {"nombre": "Neptuno", "masa_1e24kg": 102.409, "radio_eq_km": 24764.0},
]


def nombres_con_masa_mayor_que(planetas, umbral_1e24kg):
    """Devuelve la lista de nombres con masa estrictamente mayor que el umbral."""
    return [p["nombre"] for p in planetas if p["masa_1e24kg"] > umbral_1e24kg]


def ordenar_por(planetas, clave):
    """Devuelve una lista NUEVA ordenada de menor a mayor por la clave dada."""
    return sorted(planetas, key=lambda p: p[clave])


def pruebas() -> None:
    assert len(PLANETAS) == 8
    assert PLANETAS[0]["nombre"] == "Mercurio" and PLANETAS[-1]["nombre"] == "Neptuno"
    assert [p["nombre"] for p in PLANETAS[:3]] == ["Mercurio", "Venus", "Tierra"]
    assert nombres_con_masa_mayor_que(PLANETAS, 50.0) == ["Júpiter", "Saturno", "Urano", "Neptuno"]
    assert nombres_con_masa_mayor_que(PLANETAS, 1e9) == []                  # caso borde
    por_masa = ordenar_por(PLANETAS, "masa_1e24kg")
    assert [p["nombre"] for p in por_masa][:2] == ["Mercurio", "Marte"]
    assert PLANETAS[0]["nombre"] == "Mercurio"                              # el original no cambia
    indice = {p["nombre"]: p for p in PLANETAS}
    assert indice["Tierra"]["radio_eq_km"] == 6378.137
    copia = PLANETAS[:]                                                     # copia superficial
    copia.append({"nombre": "X"})
    assert len(PLANETAS) == 8 and len(copia) == 9
    alias = PLANETAS
    alias.append({"nombre": "Y"})
    assert len(PLANETAS) == 9                                               # alias: misma lista
    alias.pop()
    assert len(PLANETAS) == 8
    gigantes = {"Júpiter", "Saturno", "Urano", "Neptuno"}
    assert gigantes & {"Tierra", "Júpiter"} == {"Júpiter"}                  # intersección
    masa_total = sum(p["masa_1e24kg"] for p in PLANETAS)
    assert math.isclose(masa_total, 2667.48129, rel_tol=1e-9)               # cálculo propio


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Planetas por masa creciente (1e24 kg):")
    for p in ordenar_por(PLANETAS, "masa_1e24kg"):
        print(f"  {p['nombre']:<9}{p['masa_1e24kg']:>10.5f}")
    print("Masa mayor que 50e24 kg:", nombres_con_masa_mayor_que(PLANETAS, 50.0))
    masa_total = sum(p["masa_1e24kg"] for p in PLANETAS)
    masa_jupiter = {p["nombre"]: p for p in PLANETAS}["Júpiter"]["masa_1e24kg"]
    print(f"Masa total de los 8 planetas: {masa_total:.5f} e24 kg; Júpiter aporta {100 * masa_jupiter / masa_total:.1f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
