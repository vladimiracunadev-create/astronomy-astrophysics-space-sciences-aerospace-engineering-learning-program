#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C19: registrar una ejecución para poder reproducirla.

Datos: planetas_nssdc.csv (PUBLICADO, NASA NSSDC, clase B07-C08, consultado el 2026-11-05),
del que se registra su huella SHA-256. El experimento es SINTÉTICO: estimar π por Monte
Carlo (puntos aleatorios en el cuadrado unidad; fracción dentro del cuarto de círculo × 4).
Modelo: π ≈ 4 × (puntos con x²+y² ≤ 1) / N. Error típico (desviación estándar de la estimación) ≈ 4·sqrt(p(1−p)/N) con p = π/4.
Supuestos: generador numpy.random.default_rng(semilla); N fijo; mismo NumPy.
Dominio de validez: la reproducibilidad exacta se espera con la misma versión de NumPy y
la misma semilla (la documentación de NumPy no garantiza compatibilidad entre versiones).
Tolerancia: dos ejecuciones con la misma semilla deben coincidir exactamente; la
estimación con semilla 2026 debe estar a menos de 4 desviaciones típicas de math.pi.
Requiere: numpy 2.4.4 (Python 3.12.9).
"""

from __future__ import annotations

import hashlib
import importlib.util
import inspect
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
CSV = AQUI.parent / "B07-C08-lectura-de-archivos-csv" / "planetas_nssdc.csv"
KEPLER = AQUI.parent / "B07-C06-funciones-y-modularidad" / "kepler.py"


def sha256_de(ruta: Path) -> str:
    """Devuelve la huella SHA-256 (hexadecimal) del contenido de un archivo."""
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def estimar_pi(n: int, semilla: int) -> float:
    """Estima π con n puntos aleatorios (Monte Carlo) usando una semilla explícita."""
    rng = np.random.default_rng(semilla)
    x = rng.random(n)
    y = rng.random(n)
    return 4.0 * float(np.count_nonzero(x * x + y * y <= 1.0)) / n


def sigma_pi(n: int) -> float:
    """Desviación típica teórica de la estimación de π con n puntos: 4·sqrt(p(1−p)/n), p = π/4."""
    p = math.pi / 4.0
    return 4.0 * math.sqrt(p * (1.0 - p) / n)


def registrar(n: int, semilla: int) -> dict:
    """Ejecuta el experimento y devuelve un registro con entradas, entorno y resultado."""
    return {
        "entradas": {"n": n, "semilla": semilla, "csv_sha256": sha256_de(CSV)},
        "entorno": {"python": platform.python_version(), "numpy": np.__version__,
                    "sistema": platform.system()},
        "resultado": {"pi_estimado": estimar_pi(n, semilla)},
    }


def funciones_sin_docstring(ruta: Path) -> list[str]:
    """Devuelve los nombres de las funciones públicas de un módulo (cargado desde su ruta) sin docstring."""
    especificacion = importlib.util.spec_from_file_location(ruta.stem, ruta)
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return [nombre for nombre, f in inspect.getmembers(modulo, inspect.isfunction)
            if f.__module__ == modulo.__name__ and not nombre.startswith("_") and not inspect.getdoc(f)]


def pruebas() -> None:
    """Detiene el programa si falla la reproducibilidad, la huella, el registro o la documentación."""
    a, b = registrar(10_000, 42), registrar(10_000, 42)
    assert a == b                                                         # misma semilla: idéntico
    assert registrar(10_000, 43)["resultado"] != a["resultado"]           # otra semilla: cambia
    n = 100_000
    estimacion = estimar_pi(n, 2026)
    assert abs(estimacion - math.pi) < 4 * sigma_pi(n)                     # cota estadística amplia
    assert len(sha256_de(CSV)) == 64 and sha256_de(CSV) == sha256_de(CSV)  # huella estable
    assert json.loads(json.dumps(a)) == a                                 # el registro cabe en JSON
    assert funciones_sin_docstring(KEPLER) == []                           # el módulo de C06 está documentado
    assert funciones_sin_docstring(Path(__file__)) == []                   # y este script también


def main() -> int:
    """Ejecuta las pruebas e imprime el registro de una ejecución con semilla 2026."""
    pruebas()
    r = registrar(100_000, 2026)
    print(f"python {sys.version.split()[0]} | numpy {np.__version__} | pruebas OK")
    print(json.dumps(r, indent=2, ensure_ascii=False))
    print("Misma semilla 2026, segunda ejecución idéntica:", registrar(100_000, 2026) == r)
    print("Semilla 2027 (sintético) π ≈", estimar_pi(100_000, 2027))
    print(f"Desviación típica teórica = {sigma_pi(100_000):.5f} | error observado con 2026: "
          f"{abs(r['resultado']['pi_estimado'] - math.pi):.5f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
