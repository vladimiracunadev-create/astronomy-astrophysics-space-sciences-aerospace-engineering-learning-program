#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C09: cálculos con NumPy: densidad media de los planetas.

Datos PUBLICADOS: planetas_nssdc.csv (clase B07-C08): masa, radio medio volumétrico y
densidad publicada por el NASA NSSDC, consultados el 2026-11-05.
Modelo: planeta esférico homogéneo en volumen: densidad media = M / (4/3 π R³), con
R el radio medio volumétrico (la definición de ese radio hace que el volumen cuadre).
Supuestos: M y R exactos tal como se publican; esfera. Densidad calculada = DERIVADA.
Dominio de validez: cuerpos casi esféricos. Tolerancia: la densidad calculada debe
coincidir con la publicada (redondeada a entero) dentro de 0,2 %.
Requiere: numpy 2.4.4 (Python 3.12.9).
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
CSV = AQUI.parent / "B07-C08-lectura-de-archivos-csv" / "planetas_nssdc.csv"


def leer_columnas(ruta: Path):
    """Devuelve (nombres, dict columna -> arreglo float64) del CSV de planetas."""
    with ruta.open(encoding="utf-8", newline="") as f:
        filas = list(csv.DictReader(f))
    nombres = [fila["nombre"] for fila in filas]
    columnas = {c: np.array([float(fila[c]) for fila in filas]) for c in filas[0] if c != "nombre"}
    return nombres, columnas


def volumen_esfera(radio_m):
    """Volumen (m³) de una esfera de radio dado en metros (escalar o arreglo)."""
    return 4.0 / 3.0 * math.pi * np.asarray(radio_m, dtype=float) ** 3


def densidad_media(masa_kg, radio_m):
    """Densidad media (kg/m³) = masa / volumen de la esfera."""
    return np.asarray(masa_kg, dtype=float) / volumen_esfera(radio_m)


def pruebas() -> None:
    assert math.isclose(float(volumen_esfera(1.0)), 4.0 / 3.0 * math.pi)       # esfera unitaria
    assert math.isclose(float(densidad_media(8.0, 1.0)), 8.0 / (4.0 / 3.0 * math.pi))
    nombres, c = leer_columnas(CSV)
    assert len(nombres) == 8 and c["masa_1e24kg"].shape == (8,)
    rho = densidad_media(c["masa_1e24kg"] * 1e24, c["radio_medio_km"] * 1e3)
    desv = np.abs(rho / c["densidad_kg_m3"] - 1.0)
    assert desv.max() < 0.002, desv                                            # tolerancia declarada
    suma_np = float(c["masa_1e24kg"].sum())
    suma_py = sum(float(x) for x in c["masa_1e24kg"])
    assert math.isclose(suma_np, suma_py, rel_tol=1e-12)                        # NumPy = bucle


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | numpy {np.__version__} | pruebas OK")
    nombres, c = leer_columnas(CSV)
    rho = densidad_media(c["masa_1e24kg"] * 1e24, c["radio_medio_km"] * 1e3)
    print(f"{'planeta':<9}{'ρ calc (kg/m³)':>16}{'ρ publicada':>13}{'desv. %':>9}")
    for n, r, pub in zip(nombres, rho, c["densidad_kg_m3"]):
        print(f"{n:<9}{r:>16.1f}{pub:>13.0f}{100 * (r / pub - 1):>+9.3f}")
    print("Planeta más denso:", nombres[int(np.argmax(rho))], "| menos denso:", nombres[int(np.argmin(rho))])
    print(f"Densidad media de los 8 (sin ponderar): {rho.mean():.1f} kg/m³")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
