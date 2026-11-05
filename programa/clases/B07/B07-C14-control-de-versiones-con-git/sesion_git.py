#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C14: una sesión de Git completa en un repositorio temporal.

Datos: tres filas de períodos orbitales sidéreos (Mercurio 87.969 d, Venus 224.701 d,
Tierra 365.256 d), PUBLICADOS por el NASA NSSDC (fichas individuales, consultadas el
2026-11-05). La identidad Git usada es FICTICIA (Estudiante Ejemplo).
Modelo: el historial de un proyecto es una cadena de instantáneas (commits).
Supuestos: Git instalado y accesible como `git`; el repositorio se crea en una carpeta
temporal que se borra al terminar, sin tocar ningún repositorio real.
Dominio de validez: sesión local, sin servidor remoto. Tolerancia: coincidencia exacta de
las salidas de Git que se comprueban (estado corto, número de commits, texto del diff).
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ENTORNO = {**os.environ,
           "GIT_AUTHOR_NAME": "Estudiante Ejemplo", "GIT_AUTHOR_EMAIL": "estudiante@example.com",
           "GIT_COMMITTER_NAME": "Estudiante Ejemplo", "GIT_COMMITTER_EMAIL": "estudiante@example.com"}


def git(carpeta: Path, *args: str) -> str:
    """Ejecuta `git args` en `carpeta` y devuelve la salida estándar sin espacios finales."""
    resultado = subprocess.run(["git", *args], cwd=carpeta, env=ENTORNO, capture_output=True,
                               text=True, encoding="utf-8", check=True)
    return resultado.stdout.rstrip()


def sesion(carpeta: Path) -> dict:
    """Realiza la sesión y devuelve las salidas que se comprueban y se muestran."""
    out = {}
    git(carpeta, "init", "-b", "main")
    archivo = carpeta / "periodos.csv"
    archivo.write_text("nombre,periodo_d\nMercurio,87.969\nVenus,224.701\n", encoding="utf-8")
    out["estado_inicial"] = git(carpeta, "status", "--short")            # '?? periodos.csv'
    git(carpeta, "add", "periodos.csv")
    out["estado_staged"] = git(carpeta, "status", "--short")             # 'A  periodos.csv'
    git(carpeta, "commit", "-m", "Agrega períodos de Mercurio y Venus")
    archivo.write_text(archivo.read_text(encoding="utf-8") + "Tierra,365.256\n", encoding="utf-8")
    out["estado_modificado"] = git(carpeta, "status", "--short")         # ' M periodos.csv'
    out["diff"] = [l for l in git(carpeta, "diff").splitlines() if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    git(carpeta, "add", "periodos.csv")
    out["estado_staged2"] = git(carpeta, "status", "--short")            # 'M  periodos.csv'
    git(carpeta, "commit", "-m", "Agrega el período de la Tierra")
    out["log"] = git(carpeta, "log", "--oneline").splitlines()
    archivo.write_text("nombre,periodo_d\nMercurio,0\n", encoding="utf-8")   # un error a propósito
    out["estado_error"] = git(carpeta, "status", "--short")
    git(carpeta, "restore", "periodos.csv")                              # descarta la edición no confirmada
    out["estado_restaurado"] = git(carpeta, "status", "--short")
    out["contenido"] = archivo.read_text(encoding="utf-8")
    git(carpeta, "switch", "-c", "prueba-marte")
    out["rama"] = git(carpeta, "branch", "--show-current")
    git(carpeta, "switch", "main")
    out["ramas"] = sorted(l.strip("* ").strip() for l in git(carpeta, "branch").splitlines())
    out["version_git"] = git(carpeta, "--version")
    return out


def pruebas(o: dict) -> None:
    assert o["estado_inicial"] == "?? periodos.csv"
    assert o["estado_staged"] == "A  periodos.csv"
    assert o["estado_modificado"] == " M periodos.csv"
    assert o["diff"] == ["+Tierra,365.256"]
    assert o["estado_staged2"] == "M  periodos.csv"
    assert len(o["log"]) == 2 and o["log"][0].endswith("Agrega el período de la Tierra")
    assert o["estado_error"] == " M periodos.csv"
    assert o["estado_restaurado"] == ""                                  # árbol limpio
    assert o["contenido"].count("\n") == 4 and "Tierra,365.256" in o["contenido"]
    assert o["rama"] == "prueba-marte" and o["ramas"] == ["main", "prueba-marte"]


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        o = sesion(Path(tmp))
    pruebas(o)
    print(f"python {sys.version.split()[0]} | {o['version_git']} | pruebas OK")
    print("status inicial     :", o["estado_inicial"])
    print("status tras add    :", o["estado_staged"])
    print("status tras editar :", o["estado_modificado"])
    print("líneas del diff    :", o["diff"])
    print("log (--oneline), con el hash oculto:")
    for linea in o["log"]:
        print("  <hash>", linea.split(" ", 1)[1])
    print("status tras restore:", repr(o["estado_restaurado"]), "(vacío = árbol limpio)")
    print("ramas              :", o["ramas"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
