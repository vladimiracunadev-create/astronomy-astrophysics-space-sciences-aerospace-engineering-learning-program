#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Utilidades comunes de los laboratorios del bloque B90 (integracion, ensayos y calificacion espacial).

Convenciones del bloque: unidades SI salvo que el rotulo diga otra cosa (mm, dB, dias, etc.).
TODO dato de los laboratorios es SINTETICO (valores de ejemplo, no de un proyecto, norma o lanzador),
salvo las constantes con fuente rotulada en cada CLASE.md (por ejemplo k = 1.380649e-23 J/K, NIST, consultado 2026-11-10).
No hay aleatoriedad sin semilla fija. Salida solo ASCII para que sea identica en cualquier consola.
"""
from __future__ import annotations
import sys
import numpy as np


def cabecera(titulo: str) -> None:
    print(f"Python {sys.version.split()[0]} | numpy {np.__version__}")
    print(titulo)


def comprobar(condicion: bool, mensaje: str) -> None:
    """Falla con un mensaje claro si una comprobacion no se cumple."""
    if not condicion:
        raise AssertionError(mensaje)


def fin() -> None:
    print("Pruebas superadas.")
