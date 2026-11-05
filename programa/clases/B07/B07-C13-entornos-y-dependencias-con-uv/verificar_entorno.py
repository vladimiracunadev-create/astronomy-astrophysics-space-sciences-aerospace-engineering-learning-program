#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C13: comprueba que el entorno instalado coincide con lo declarado.

Datos: proyecto_laboratorios/pyproject.toml (declaración de dependencias con versión
exacta, escrita para esta clase). No hay datos astronómicos.
Modelo: un entorno es reproducible si cada paquete instalado tiene exactamente la versión
que el proyecto declara con «==».
Supuestos: las dependencias se declaran como «nombre==versión»; Python 3.12.
Dominio de validez: entornos pequeños con versiones fijadas. Tolerancia: igualdad exacta
de cadenas de versión (sin tolerancia).
Uso recomendado: uv run --project proyecto_laboratorios python verificar_entorno.py
"""

from __future__ import annotations

import sys
import tomllib
from importlib import metadata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PYPROJECT = AQUI / "proyecto_laboratorios" / "pyproject.toml"


def separar_requisito(requisito: str) -> tuple[str, str]:
    """Separa 'nombre==versión' en (nombre, versión); lanza ValueError si no tiene '=='."""
    if "==" not in requisito:
        raise ValueError(f"requisito sin versión exacta: {requisito!r}")
    nombre, version = requisito.split("==", 1)
    return nombre.strip(), version.strip()


def declaradas(ruta: Path) -> list[tuple[str, str]]:
    """Devuelve (nombre, versión) de las dependencias y del grupo dev declaradas en pyproject."""
    datos = tomllib.loads(ruta.read_text(encoding="utf-8"))
    requisitos = list(datos["project"]["dependencies"]) + list(datos["dependency-groups"]["dev"])
    return [separar_requisito(r) for r in requisitos]


def comparar(declaradas_: list[tuple[str, str]], instaladas: dict[str, str]) -> list[str]:
    """Devuelve la lista de discrepancias (vacía si todo coincide)."""
    problemas = []
    for nombre, version in declaradas_:
        actual = instaladas.get(nombre)
        if actual is None:
            problemas.append(f"{nombre}: no instalado (declarado {version})")
        elif actual != version:
            problemas.append(f"{nombre}: instalado {actual}, declarado {version}")
    return problemas


def pruebas() -> None:
    assert separar_requisito("numpy==2.4.4") == ("numpy", "2.4.4")
    try:
        separar_requisito("numpy>=2")
    except ValueError:
        pass
    else:
        raise AssertionError("debía rechazar una versión no exacta")
    decl = [("a", "1.0"), ("b", "2.0"), ("c", "3.0")]
    assert comparar(decl, {"a": "1.0", "b": "2.0", "c": "3.0"}) == []                 # todo coincide
    assert comparar(decl, {"a": "1.0", "b": "2.1"}) == [
        "b: instalado 2.1, declarado 2.0", "c: no instalado (declarado 3.0)"]       # dos discrepancias
    assert len(declaradas(PYPROJECT)) == 5                                           # 4 + 1 de dev


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas internas OK")
    decl = declaradas(PYPROJECT)
    instaladas = {}
    for nombre, _ in decl:
        try:
            instaladas[nombre] = metadata.version(nombre)
        except metadata.PackageNotFoundError:
            pass
    for nombre, version in decl:
        print(f"  {nombre:<11} declarado {version:<7} instalado {instaladas.get(nombre, '—')}")
    problemas = comparar(decl, instaladas)
    if problemas:
        print("DISCREPANCIAS:")
        for p in problemas:
            print("  -", p)
        return 1
    print("Entorno reproducible: todo coincide con pyproject.toml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
