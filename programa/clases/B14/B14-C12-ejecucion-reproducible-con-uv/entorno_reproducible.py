#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C12: huella de entorno y archivo de bloqueo con uv.

Datos: ninguno científico. Se usa un proyecto mínimo y SINTÉTICO creado en un
directorio temporal con una dependencia fijada (numpy==2.5.4).
Modelo: (a) huella del entorno actual con importlib.metadata (versión de
Python, de numpy y de scipy si existe); (b) un proyecto uv con pyproject.toml;
`uv lock` produce uv.lock; `uv lock --check` verifica que el bloqueo coincide
con el proyecto; al cambiar la dependencia, la verificación debe FALLAR.
Supuestos: uv instalado (python -m uv) y acceso al índice de paquetes; si no,
la parte (b) se reporta como OMITIDA y el script termina con código 2 (no se
da por aprobada).
Validez: demostración del flujo de bloqueo; no instala ni ejecuta el proyecto.
Tolerancia: coincidencia exacta de cadenas de versión; el bloqueo debe
contener versión y sumas SHA-256 de la dependencia fijada.
"""
from __future__ import annotations
import importlib.metadata as md, os, platform, re, subprocess, sys, tempfile, tomllib

PYPROJECT = """[project]
name = "demo-repro"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["numpy==2.5.4"]
"""


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def huella():
    out = {"python": platform.python_version(), "plataforma": platform.system()}
    for p in ("numpy", "scipy", "astropy"):
        try:
            out[p] = md.version(p)
        except md.PackageNotFoundError:
            out[p] = None
    return out


def uv(*args, cwd):
    return subprocess.run([sys.executable, "-m", "uv", *args], cwd=cwd, capture_output=True, text=True)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    h = huella()
    print("huella del entorno actual:", h)
    prueba(h["python"].count(".") == 2, "versión de Python con tres componentes")

    with tempfile.TemporaryDirectory() as td:
        v = uv("--version", cwd=td)
        if v.returncode != 0:
            print("OMITIDA la parte uv: uv no está disponible"); raise SystemExit(2)
        print("uv:", v.stdout.strip())
        with open(os.path.join(td, "pyproject.toml"), "w", encoding="utf-8") as f:
            f.write(PYPROJECT)
        r = uv("lock", cwd=td)
        if r.returncode != 0:
            print("OMITIDA la parte uv: no se pudo resolver (¿sin red?):", r.stderr.strip()[-200:]); raise SystemExit(2)
        print("uv lock ->", (r.stderr.strip().splitlines() or [""])[-1])
        with open(os.path.join(td, "uv.lock"), "rb") as f:
            contenido = f.read()
        lock = tomllib.loads(contenido.decode("utf-8"))
        paquetes = {p["name"]: p for p in lock["package"]}
        print(f"uv.lock: version={lock['version']} revision={lock.get('revision')} requires-python={lock['requires-python']}; paquetes: {sorted(paquetes)}")
        prueba(paquetes["numpy"]["version"] == "2.5.4", "numpy fijado a 2.5.4")
        hashes = re.findall(r'hash = "sha256:([0-9a-f]{64})"', contenido.decode("utf-8"))
        print(f"sumas SHA-256 en el bloqueo: {len(hashes)} (sdist + ruedas de cada plataforma)")
        prueba(len(hashes) >= 2, "el bloqueo contiene sumas de verificación")

        c1 = uv("lock", "--check", cwd=td)
        print(f"uv lock --check con el proyecto sin cambios: código {c1.returncode}")
        prueba(c1.returncode == 0, "el bloqueo coincide con el proyecto")

        with open(os.path.join(td, "pyproject.toml"), "w", encoding="utf-8") as f:
            f.write(PYPROJECT.replace("numpy==2.5.4", "numpy==2.4.4"))
        c2 = uv("lock", "--check", cwd=td)
        msg = next((l for l in c2.stderr.splitlines() if "needs to be updated" in l), c2.stderr.strip())
        print(f"uv lock --check tras cambiar la dependencia a numpy==2.4.4: código {c2.returncode}; mensaje: {msg}")
        prueba(c2.returncode != 0, "el cambio de dependencia debe invalidar el bloqueo")
        with open(os.path.join(td, "uv.lock"), "rb") as f:
            prueba(f.read() == contenido, "--check no modifica uv.lock")
        print("--check no modificó uv.lock")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
