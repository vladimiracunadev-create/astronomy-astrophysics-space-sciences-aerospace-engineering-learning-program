#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C22: la lógica de una búsqueda por tiempo, instrumento y cadencia, sin red.

AVISO: este laboratorio NO usa SunPy ni accede a VSO, JSOC ni CDAWeb. Implementa
en miniatura la idea de «buscar primero, descargar después» sobre un ÍNDICE
SINTÉTICO de registros de imágenes solares ficticias, para comprobar la lógica
(rangos de tiempo, filtros, submuestreo y manejo de errores de un proveedor).
Datos: SINTÉTICOS. 24 horas de registros del 2026-01-01 con cadencia de 12 s
para el instrumento «AIA-ficticio» en dos longitudes de onda (171 y 193 angstrom)
y un segundo instrumento «EUV-ficticio» con cadencia de 60 s. Nombres ficticios;
ninguna fila corresponde a una observación real.
Modelo: un registro = (instrumento, t, longitud de onda). Búsqueda = filtro por
intervalo cerrado-abierto [t0, t1), instrumento y longitud de onda; el
submuestreo toma el primer registro de cada ventana de `muestra` segundos.
Supuestos: los tiempos son UTC en segundos desde el inicio del día (sin saltos de
segundo); un proveedor puede fallar y el resultado debe conservar el error.
Validez: demostración; los servicios reales tienen más atributos y particularidades.
Tolerancia: conteos exactos calculados analíticamente.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import pandas as pd


def construir_indice():
    filas = []
    t = np.arange(0, 86_400, 12)
    for w in (171, 193):
        filas.append(pd.DataFrame({"instrumento": "AIA-ficticio", "t_s": t, "onda_A": w, "proveedor": "A"}))
    t2 = np.arange(0, 86_400, 60)
    filas.append(pd.DataFrame({"instrumento": "EUV-ficticio", "t_s": t2, "onda_A": 304, "proveedor": "B"}))
    return pd.concat(filas, ignore_index=True)


def buscar(indice, t0, t1, instrumento=None, onda=None, muestra=None, proveedores_caidos=()):
    """Devuelve (tabla, errores). El intervalo es [t0, t1). `muestra` en segundos."""
    errores = []
    disponibles = indice[~indice["proveedor"].isin(proveedores_caidos)]
    for p in proveedores_caidos:
        errores.append(f"proveedor {p} no respondió")
    m = (disponibles["t_s"] >= t0) & (disponibles["t_s"] < t1)
    if instrumento is not None:
        m &= disponibles["instrumento"] == instrumento
    if onda is not None:
        m &= disponibles["onda_A"] == onda
    sel = disponibles[m]
    if muestra is not None and len(sel):
        grupos = []
        for _, g in sel.groupby(["instrumento", "onda_A"]):
            g = g.sort_values("t_s")
            ventana = (g["t_s"] - t0) // muestra
            grupos.append(g.groupby(ventana).head(1))
        sel = pd.concat(grupos)
    return sel.sort_values(["instrumento", "onda_A", "t_s"]).reset_index(drop=True), errores


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  pandas {pd.__version__}  (sin red, sin SunPy)")
    idx = construir_indice()
    print(f"índice sintético: {len(idx)} registros")
    prueba(len(idx) == 7200 * 2 + 1440, "tamaño del índice")

    r, e = buscar(idx, 0, 86_400, instrumento="AIA-ficticio", onda=171)
    print(f"AIA-ficticio 171 A, 24 h: {len(r)} registros (esperado 86400/12 = 7200)")
    prueba(len(r) == 7200 and e == [], "7200 registros")

    r, _ = buscar(idx, 3_600, 7_200, instrumento="AIA-ficticio", onda=171)
    print(f"AIA-ficticio 171 A, [3600, 7200): {len(r)} registros (esperado 3600/12 = 300; el extremo 7200 no cuenta)")
    prueba(len(r) == 300 and r["t_s"].max() == 7_188, "intervalo cerrado-abierto")

    r, _ = buscar(idx, 0, 86_400, instrumento="AIA-ficticio", onda=171, muestra=7_200)
    print(f"submuestreo cada 120 min: {len(r)} registros (esperado 12)")
    prueba(len(r) == 12 and list(r["t_s"]) == [7_200 * k for k in range(12)], "submuestreo")

    r, _ = buscar(idx, 0, 86_400, instrumento="AIA-ficticio", muestra=7_200)
    print(f"AIA-ficticio, ambas longitudes de onda, cada 120 min: {len(r)} registros (esperado 24)")
    prueba(len(r) == 24, "dos longitudes de onda")

    r, e = buscar(idx, 0, 3_600, proveedores_caidos=("B",))
    print(f"proveedor B caído, 1 h: {len(r)} registros de {sorted(r['instrumento'].unique())}; errores = {e}")
    prueba(len(r) == 2 * 300 and e == ["proveedor B no respondió"], "un proveedor caído se informa, no se silencia")

    r, _ = buscar(idx, 0, 3_600)
    prueba(len(r) == 2 * 300 + 60, "sin filtros: 600 + 60 registros en una hora")
    print(f"sin filtros, 1 h: {len(r)} registros (esperado 300 + 300 + 60 = 660)")
    prueba(len(r) == 660, "660")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
