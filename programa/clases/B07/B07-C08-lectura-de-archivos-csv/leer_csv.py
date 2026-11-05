#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C08: lectura de archivos CSV con el módulo estándar csv.

Datos PUBLICADOS: planetas_nssdc.csv transcribe, de las fichas individuales del NASA
NSSDC (act. 11-ene-2024 a 19-may-2025) y de su tabla comparativa (densidad y gravedad
redondeadas), consultadas el 2026-11-05: semieje mayor, período sidéreo, masa, radios,
densidad y gravedad de los ocho planetas.
datos_sinteticos_sucios.csv es SINTÉTICO (inventado para esta clase) y contiene errores
a propósito.
Modelo: ninguno físico; se estudia la lectura y validación de una tabla.
Supuestos: separador coma, codificación UTF-8, punto decimal, primera fila = encabezados.
Dominio de validez: archivos pequeños que caben en memoria. Tolerancia: conteos exactos.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
COLUMNAS_NUMERICAS = ["semieje_1e6km", "periodo_sidereo_d", "masa_1e24kg", "radio_medio_km",
                      "radio_ecuatorial_km", "densidad_kg_m3", "gravedad_m_s2"]


def leer_planetas(ruta: Path) -> list[dict]:
    """Lee el CSV de planetas y convierte las columnas numéricas a float."""
    filas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            registro = {"nombre": fila["nombre"]}
            for col in COLUMNAS_NUMERICAS:
                registro[col] = float(fila[col])
            filas.append(registro)
    return filas


def leer_tolerante(ruta: Path, columnas: list[str]):
    """Lee un CSV sin detenerse: devuelve (filas_validas, problemas) con número de línea."""
    validas, problemas = [], []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            n = lector.line_num
            if None in fila:
                problemas.append((n, "campos de más"))
                continue
            try:
                registro = {"nombre": fila["nombre"]}
                for col in columnas:
                    texto = fila[col]
                    if texto == "":
                        raise ValueError("valor vacío en " + col)
                    registro[col] = float(texto)
            except ValueError as error:
                problemas.append((n, str(error)))
                continue
            validas.append(registro)
    return validas, problemas


def pruebas() -> None:
    planetas = leer_planetas(AQUI / "planetas_nssdc.csv")
    assert len(planetas) == 8                                          # 8 planetas
    assert planetas[2]["nombre"] == "Tierra" and planetas[4]["nombre"] == "Júpiter"   # UTF-8
    assert planetas[2]["periodo_sidereo_d"] == 365.256 and isinstance(planetas[2]["masa_1e24kg"], float)
    assert all(p[c] > 0 for p in planetas for c in COLUMNAS_NUMERICAS)  # todo positivo
    with (AQUI / "planetas_nssdc.csv").open(encoding="utf-8", newline="") as f:
        assert next(csv.reader(f)) == ["nombre"] + COLUMNAS_NUMERICAS    # encabezado esperado
    validas, problemas = leer_tolerante(AQUI / "datos_sinteticos_sucios.csv",
                                        ["semieje_1e6km", "masa_1e24kg"])
    assert [v["nombre"] for v in validas] == ["Alfa"]
    assert [n for n, _ in problemas] == [3, 4, 5, 6]                    # líneas con problemas


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    planetas = leer_planetas(AQUI / "planetas_nssdc.csv")
    print(f"Filas leídas: {len(planetas)} | columnas: {len(planetas[0])}")
    for p in planetas[:3]:
        print(f"  {p['nombre']:<9} a = {p['semieje_1e6km']:>8.3f} e6 km   T = {p['periodo_sidereo_d']:>9.3f} d")
    validas, problemas = leer_tolerante(AQUI / "datos_sinteticos_sucios.csv",
                                        ["semieje_1e6km", "masa_1e24kg"])
    print(f"Archivo sintético sucio: {len(validas)} fila válida, {len(problemas)} con problemas")
    for n, motivo in problemas:
        print(f"  línea {n}: {motivo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
