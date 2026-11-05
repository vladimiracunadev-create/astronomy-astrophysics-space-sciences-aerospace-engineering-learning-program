#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C15: rutas de archivos con pathlib, sin rutas absolutas fijas.

Datos: archivos reales de este repositorio (planetas_nssdc.csv de la clase B07-C08,
PUBLICADO por NASA NSSDC, consultado el 2026-11-05) y rutas de ejemplo inventadas para
comparar Windows y POSIX con las clases PurePath (no tocan el disco).
Modelo: una ruta es una secuencia de componentes; puede ser relativa (depende de dónde
se ejecuta) o absoluta (completa). Una ruta calculada desde __file__ no depende del
directorio de trabajo.
Supuestos: el script vive dentro del repositorio; AGENTS.md existe en su raíz.
Dominio de validez: Windows y POSIX. Tolerancia: coincidencia exacta de cadenas y conteos.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath

AQUI = Path(__file__).resolve().parent


def raiz_del_repositorio(desde: Path) -> Path:
    """Sube por los directorios padre hasta hallar AGENTS.md; lanza FileNotFoundError si no hay."""
    for carpeta in [desde, *desde.parents]:
        if (carpeta / "AGENTS.md").exists():
            return carpeta
    raise FileNotFoundError("no se encontró AGENTS.md hacia arriba desde " + str(desde))


def ruta_csv_planetas() -> Path:
    """Ruta al CSV de planetas de la clase C08, calculada desde este archivo."""
    return AQUI.parent / "B07-C08-lectura-de-archivos-csv" / "planetas_nssdc.csv"


def pruebas() -> None:
    assert AQUI.is_absolute() and not Path("datos/archivo.csv").is_absolute()
    csv = ruta_csv_planetas()
    assert csv.exists() and csv.suffix == ".csv" and csv.name == "planetas_nssdc.csv"
    primera = csv.read_text(encoding="utf-8").splitlines()[0]
    assert primera.startswith("nombre,semieje_1e6km")
    raiz = raiz_del_repositorio(AQUI)
    assert (raiz / "AGENTS.md").is_file() and csv.relative_to(raiz).parts[:2] == ("programa", "clases")
    assert PurePosixPath("/etc") / "init.d" / "reboot" == PurePosixPath("/etc/init.d/reboot")
    assert PurePosixPath("/etc") / "/ruta_absoluta" == PurePosixPath("/ruta_absoluta")   # lo absoluto reemplaza
    assert PureWindowsPath("c:/Datos/Kepler.CSV") == PureWindowsPath("C:/datos/kepler.csv")  # Windows ignora mayúsculas
    assert PurePosixPath("Datos/Kepler.CSV") != PurePosixPath("datos/kepler.csv")             # POSIX distingue
    assert PureWindowsPath("c:/datos/kepler.csv").as_posix() == "c:/datos/kepler.csv"
    assert Path("a/b/../c").resolve() == (Path.cwd() / "a" / "c").resolve()                   # resolve quita ..
    assert PurePosixPath("biblioteca.tar.gz").suffixes == [".tar", ".gz"]
    try:
        raiz_del_repositorio(Path(Path.home().anchor))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("debía fallar en la raíz del disco")


def main() -> int:
    pruebas()
    csv = ruta_csv_planetas()
    raiz = raiz_del_repositorio(AQUI)
    print(f"python {sys.version.split()[0]} | {sys.platform} | separador del sistema: {os.sep!r} | pruebas OK")
    print("Ruta relativa a la raíz del repositorio:", csv.relative_to(raiz).as_posix())
    print("Nombre:", csv.name, "| extensión:", csv.suffix, "| carpeta:", csv.parent.name)
    print("Líneas del CSV:", len(csv.read_text(encoding='utf-8').splitlines()))
    print("PurePosixPath('Datos/Kepler.CSV') == PurePosixPath('datos/kepler.csv'):",
          PurePosixPath("Datos/Kepler.CSV") == PurePosixPath("datos/kepler.csv"))
    print("PureWindowsPath('c:/Datos/Kepler.CSV') == PureWindowsPath('C:/datos/kepler.csv'):",
          PureWindowsPath("c:/Datos/Kepler.CSV") == PureWindowsPath("C:/datos/kepler.csv"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
