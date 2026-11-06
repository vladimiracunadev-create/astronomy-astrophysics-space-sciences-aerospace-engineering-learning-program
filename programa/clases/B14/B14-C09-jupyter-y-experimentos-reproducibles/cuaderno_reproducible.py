#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C09: un cuaderno como registro reproducible y cómo se rompe.

Datos: SINTÉTICOS. El cuaderno de ejemplo estima la media de un flujo
relativo adimensional: 1000 muestras gaussianas de media 1.0 y desviación 0.01
generadas con una semilla fija (20261105). No es una observación real.
Modelo: un cuaderno .ipynb es un JSON (nbformat 4: claves nbformat,
nbformat_minor, metadata, cells; cada celda de código tiene source,
execution_count y outputs). "Reiniciar y ejecutar todo" se simula ejecutando
las celdas de código en orden, con exec, en un espacio de nombres nuevo.
Supuestos: sin kernel de Jupyter; solo se ejecuta código Python plano.
Validez: demostración de ideas (orden, estado oculto, semilla), no un
sustituto de ejecutar el cuaderno con un kernel real.
Tolerancia: la repetición con semilla debe dar resultados idénticos bit a
bit; el cuaderno debe validar contra el esquema nbformat.
"""
from __future__ import annotations
import contextlib, io, platform, sys
import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import numpy as np

CELDAS = [
    "import numpy as np\nrng = np.random.default_rng(20261105)",
    "x = rng.normal(1.0, 0.01, 1000)",
    "print(f'media = {x.mean():.6f}')",
]
CELDAS_SIN_SEMILLA = [
    "import numpy as np\nrng = np.random.default_rng()",
    CELDAS[1],
    CELDAS[2],
]


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def construir(celdas):
    nb = new_notebook(metadata={"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}})
    nb.cells.append(new_markdown_cell("# Media de un flujo sintético"))
    for c in celdas:
        nb.cells.append(new_code_cell(c))
    return nb


def ejecutar_en_orden(celdas, orden=None):
    """Reinicia el espacio de nombres y ejecuta las celdas (en el orden dado). Devuelve la salida."""
    ns: dict = {}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for i in (orden if orden is not None else range(len(celdas))):
            exec(celdas[i], ns)
    return buf.getvalue().strip()


def orden_lineal(nb):
    """True si los execution_count de las celdas con número son 1, 2, 3... sin saltos ni retrocesos."""
    cuentas = [c.execution_count for c in nb.cells if c.cell_type == "code" and c.execution_count is not None]
    return cuentas == list(range(1, len(cuentas) + 1))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  nbformat {nbformat.__version__}")
    nb = construir(CELDAS)
    nbformat.validate(nb)
    print(f"claves de nivel superior: {sorted(nb.keys())}; nbformat = {nb.nbformat}.{nb.nbformat_minor}; celdas = {len(nb.cells)}")
    prueba(nb.nbformat == 4, "nbformat 4")
    prueba({"cells", "metadata", "nbformat", "nbformat_minor"} <= set(nb.keys()), "claves obligatorias")
    prueba(all("outputs" in c and "execution_count" in c for c in nb.cells if c.cell_type == "code"), "campos de celda de código")

    # 1) reproducible con semilla: dos ejecuciones desde cero dan lo mismo
    a, b = ejecutar_en_orden(CELDAS), ejecutar_en_orden(CELDAS)
    print(f"ejecución 1: {a}\nejecución 2: {b}")
    prueba(a == b, "repetición con semilla idéntica")

    # 2) sin semilla: no reproducible
    c, d = ejecutar_en_orden(CELDAS_SIN_SEMILLA), ejecutar_en_orden(CELDAS_SIN_SEMILLA)
    print(f"sin semilla: {c} | {d}")
    prueba(c != d, "sin semilla debe diferir (probabilidad de coincidir ~ 0)")

    # 3) estado oculto: se ejecuta la celda 2 dos veces seguidas con la misma rng
    ns: dict = {}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(CELDAS[0], ns); exec(CELDAS[1], ns); exec(CELDAS[2], ns)   # 1ª vez
        exec(CELDAS[1], ns); exec(CELDAS[2], ns)                         # re-ejecutar celdas 2 y 3
    lineas = buf.getvalue().strip().splitlines()
    print(f"re-ejecutar la celda 2 sin reiniciar: {lineas[0]} -> {lineas[1]}")
    prueba(lineas[0] != lineas[1], "el generador conserva estado entre ejecuciones")
    prueba(lineas[0] == a, "la primera ejecución coincide con 'reiniciar y ejecutar todo'")

    # 4) detección de orden no lineal en el cuaderno guardado
    nb_ok = construir(CELDAS)
    for i, c in enumerate([c for c in nb_ok.cells if c.cell_type == "code"], start=1):
        c.execution_count = i
    nb_mal = construir(CELDAS)
    for c, n in zip([c for c in nb_mal.cells if c.cell_type == "code"], (1, 3, 2)):
        c.execution_count = n
    print(f"orden lineal (1,2,3): {orden_lineal(nb_ok)};  orden (1,3,2): {orden_lineal(nb_mal)}")
    prueba(orden_lineal(nb_ok) and not orden_lineal(nb_mal), "detección de orden")

    # 5) el cuaderno sobrevive a la ida y vuelta de serialización
    texto = nbformat.writes(nb)
    nb2 = nbformat.reads(texto, as_version=4)
    prueba([c.source for c in nb2.cells] == [c.source for c in nb.cells], "ida y vuelta JSON")
    print(f"serialización: {len(texto)} caracteres JSON; ida y vuelta igual")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
