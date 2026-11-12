# SPDX-License-Identifier: Apache-2.0
"""Valida los talleres integradores de misión (`talleres/Txx-*/`).

Comprueba por cada taller:
  - README.md y diez capítulos numerados 01..10, el último con rúbrica y el resto con ejercicio;
  - enlaces relativos de todos los .md y referencias a figuras existentes;
  - que `laboratorio_Txx.py` se ejecuta sin error y declara unidades, sistema de referencia, modelo y tolerancia;
  - que `figuras_Txx.py` regenera exactamente los SVG versionados (para que no queden figuras desfasadas);
  - que ningún texto de las figuras se sale del lienzo ni se solapa (talleres/_comun/verificar_figuras.py).
No comprueba la exactitud de los datos históricos: esos llevan ⚠ y exigen contraste con la fuente primaria.
Uso: python herramientas/validar_talleres.py
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
TALLERES = RAIZ / "talleres"
ENLACE = re.compile(r"\]\(([^)#\s][^)\s]*)\)")
errores: list[str] = []


def err(msg: str) -> None:
    errores.append(msg)
    print("ERROR", msg)


def validar(d: Path) -> None:
    tid = d.name.split("-")[0]
    if not (d / "README.md").exists():
        err(f"{d.name}: falta README.md")
    caps = sorted(p for p in d.glob("[0-9][0-9]-*.md"))
    nums = [p.name[:2] for p in caps]
    if nums != [f"{i:02d}" for i in range(1, 11)]:
        err(f"{d.name}: los capítulos deben ser 01..10 y hay {nums}")
    for p in caps:
        t = p.read_text(encoding="utf-8")
        if not t.startswith("# Capítulo"):
            err(f"{p.relative_to(RAIZ)}: debe empezar con «# Capítulo»")
        if p.name.startswith("10-"):
            if "Rúbrica" not in t and "rúbrica" not in t:
                err(f"{p.relative_to(RAIZ)}: falta la rúbrica")
        elif "Ejercicio del capítulo" not in t:
            err(f"{p.relative_to(RAIZ)}: falta «Ejercicio del capítulo»")
    for p in [d / "README.md"] + caps:
        if not p.exists():
            continue
        for l in ENLACE.findall(p.read_text(encoding="utf-8")):
            if l.startswith(("http", "mailto")):
                continue
            if not (p.parent / l.split("#")[0]).resolve().exists():
                err(f"{p.relative_to(RAIZ)}: enlace roto {l}")
    lab = d / f"laboratorio_{tid}.py"
    if not lab.exists():
        err(f"{d.name}: falta {lab.name}")
    else:
        texto = lab.read_text(encoding="utf-8")
        for palabra in ("UNIDADES", "SISTEMA DE REFERENCIA", "MODELO", "TOLERANCIA"):
            if palabra not in texto:
                err(f"{lab.relative_to(RAIZ)}: el encabezado debe declarar {palabra}")
        r = subprocess.run([sys.executable, str(lab)], capture_output=True, text=True, encoding="utf-8",
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        if r.returncode:
            err(f"{lab.relative_to(RAIZ)}: falla al ejecutarse: {r.stderr[-200:]}")
    fig = d / f"figuras_{tid}.py"
    if not fig.exists():
        err(f"{d.name}: falta {fig.name}")
        return
    antes = {p.name: p.read_bytes() for p in (d / "figuras").glob("*.svg")}
    r = subprocess.run([sys.executable, str(fig)], capture_output=True, text=True, encoding="utf-8", cwd=str(d),
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    if r.returncode:
        err(f"{fig.relative_to(RAIZ)}: falla al ejecutarse: {r.stderr[-200:]}")
    despues = {p.name: p.read_bytes() for p in (d / "figuras").glob("*.svg")}
    for n in set(antes) | set(despues):
        if antes.get(n) != despues.get(n):
            err(f"{d.name}/figuras/{n}: no coincide con lo que genera {fig.name} (regenera y sube las figuras)")


def main() -> int:
    carpetas = sorted(p for p in TALLERES.glob("T[0-9][0-9]-*") if p.is_dir())
    if not carpetas:
        err("no hay talleres")
    for d in carpetas:
        validar(d)
    r = subprocess.run([sys.executable, str(TALLERES / "_comun" / "verificar_figuras.py")], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip())
    if r.returncode:
        err("figuras con textos fuera del lienzo o solapados")
    idx = (TALLERES / "README.md").read_text(encoding="utf-8")
    for d in carpetas:
        if d.name not in idx:
            err(f"talleres/README.md no enlaza a {d.name}")
    print(f"{len(carpetas)} talleres revisados, {len(errores)} errores")
    if not errores:
        print("TALLERES VÁLIDOS (estructura y consistencia; la exactitud de los datos requiere contraste con fuentes)")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
