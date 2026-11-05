#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C17: ¿detectan las pruebas un error? Se introduce uno a propósito.

Datos: ninguno observado; usa el módulo y las pruebas de esta carpeta.
Modelo: una prueba vale si FALLA cuando el código está mal. Se copia el módulo a una
carpeta temporal, se le inyecta un error (el volumen con r² en vez de r³) y se ejecutan
las pruebas con pytest: la copia buena debe pasar y la mala debe fallar.
Supuestos: pytest 9.2.0 disponible para este mismo intérprete.
Dominio de validez: demostración local; no modifica los archivos originales.
Tolerancia: se comparan recuentos exactos de pruebas pasadas y falladas.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def ejecutar_pytest(carpeta: Path) -> tuple[int, int, int]:
    """Ejecuta pytest en `carpeta` y devuelve (pasadas, falladas, código de salida)."""
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                       cwd=carpeta, capture_output=True, text=True, encoding="utf-8")
    texto = r.stdout
    pasadas = int(m.group(1)) if (m := re.search(r"(\d+) passed", texto)) else 0
    falladas = int(m.group(1)) if (m := re.search(r"(\d+) failed", texto)) else 0
    return pasadas, falladas, r.returncode


def main() -> int:
    import pytest
    with tempfile.TemporaryDirectory() as tmp:
        buena = Path(tmp) / "buena"
        mala = Path(tmp) / "mala"
        for destino in (buena, mala):
            destino.mkdir()
            for nombre in ("funciones_matematicas.py", "test_funciones_matematicas.py"):
                shutil.copy(AQUI / nombre, destino / nombre)
        codigo = (mala / "funciones_matematicas.py").read_text(encoding="utf-8")
        assert "radio ** 3" in codigo
        (mala / "funciones_matematicas.py").write_text(codigo.replace("radio ** 3", "radio ** 2"), encoding="utf-8")
        p_buena = ejecutar_pytest(buena)
        p_mala = ejecutar_pytest(mala)
    assert p_buena[1] == 0 and p_buena[2] == 0 and p_buena[0] > 0   # la copia buena pasa todo
    assert p_mala[1] > 0 and p_mala[2] != 0                          # la copia mala es detectada
    print(f"python {sys.version.split()[0]} | pytest {pytest.__version__} | pruebas OK")
    print(f"Código correcto : {p_buena[0]} pasadas, {p_buena[1]} falladas (salida {p_buena[2]})")
    print(f"Con r² en vez de r³: {p_mala[0]} pasadas, {p_mala[1]} falladas (salida {p_mala[2]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
