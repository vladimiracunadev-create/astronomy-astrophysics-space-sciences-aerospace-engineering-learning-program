#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C19: revisar un paquete publicable (código y datos).

Datos: SINTÉTICOS. Se crea en un directorio temporal un paquete ficticio con
README, LICENSE (identificador SPDX), CITATION.cff, un archivo de datos
sintético, un manifiesto con SHA-256 y una ficha de metadatos. NO se publica
nada y NO se acuña ningún DOI: el campo de identificador queda como
"pendiente".
Modelo: una lista de comprobación inspirada en los principios FAIR (F1-F4,
A1-A2, I1-I3, R1.1-R1.3, según go-fair) y en CITATION.cff. Las reglas son
convenciones de esta clase, no una certificación FAIR.
Supuestos: el revisor solo lee archivos locales.
Validez: demostración; "pasa la lista" no significa "es FAIR" ni "es correcto".
Tolerancia: el paquete completo pasa; cada paquete con un defecto sembrado
falla exactamente en la regla sembrada.
"""
from __future__ import annotations
import hashlib, json, os, platform, shutil, sys, tempfile

LICENCIAS_SPDX = {"Apache-2.0", "MIT", "CC-BY-4.0", "CC0-1.0", "BSD-3-Clause"}
CFF = """cff-version: 1.2.0
message: "Si usa estos datos, cítelos con esta información."
title: "Curva de luz sintética de demostración"
version: "0.1.0"
date-released: "2026-11-05"
authors:
  - family-names: "Autoría"
    given-names: "Ejemplo"
"""


def sha256(ruta):
    with open(ruta, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def crear_paquete(carpeta):
    os.makedirs(carpeta)
    datos = os.path.join(carpeta, "flujo.csv")
    with open(datos, "w", encoding="utf-8") as f:
        f.write("t_s,flujo\n0,1.0000\n2,0.9990\n4,1.0010\n")
    with open(os.path.join(carpeta, "README.md"), "w", encoding="utf-8") as f:
        f.write("# Demostración\nDatos sintéticos; ver CITATION.cff y metadatos.json.\n")
    with open(os.path.join(carpeta, "LICENSE"), "w", encoding="utf-8") as f:
        f.write("SPDX-License-Identifier: CC-BY-4.0\n")
    with open(os.path.join(carpeta, "CITATION.cff"), "w", encoding="utf-8") as f:
        f.write(CFF)
    meta = {
        "identificador": "pendiente (sin DOI acuñado)",
        "licencia_spdx": "CC-BY-4.0",
        "descripcion": "Tres muestras de flujo relativo adimensional, sintéticas.",
        "unidades": {"t_s": "s", "flujo": "relativo (adimensional)"},
        "procedencia": "sintético, escrito a mano en el script de la clase",
        "archivos": {"flujo.csv": sha256(datos)},
    }
    with open(os.path.join(carpeta, "metadatos.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)


def leer_cff(ruta):
    campos = {}
    for l in open(ruta, encoding="utf-8"):
        if ":" in l and not l.startswith(" ") and not l.startswith("-"):
            k, v = l.split(":", 1)
            campos[k.strip()] = v.strip().strip('"')
    return campos


def revisar(carpeta):
    fallos = []
    for nombre in ("README.md", "LICENSE", "CITATION.cff", "metadatos.json"):
        if not os.path.exists(os.path.join(carpeta, nombre)):
            fallos.append(f"falta {nombre}")
    if fallos:
        return fallos
    cff = leer_cff(os.path.join(carpeta, "CITATION.cff"))
    for k in ("cff-version", "message", "title"):
        if not cff.get(k):
            fallos.append(f"CITATION.cff sin {k}")
    if "authors:" not in open(os.path.join(carpeta, "CITATION.cff"), encoding="utf-8").read():
        fallos.append("CITATION.cff sin authors")
    meta = json.load(open(os.path.join(carpeta, "metadatos.json"), encoding="utf-8"))
    if meta.get("licencia_spdx") not in LICENCIAS_SPDX:
        fallos.append("licencia ausente o no es un identificador SPDX admitido (R1.1)")
    if not meta.get("procedencia"):
        fallos.append("sin procedencia (R1.2)")
    if not meta.get("descripcion") or not meta.get("unidades"):
        fallos.append("metadatos pobres: faltan descripción o unidades (F2, R1)")
    if "identificador" not in meta:
        fallos.append("sin campo de identificador persistente (F1)")
    for archivo, h in meta.get("archivos", {}).items():
        ruta = os.path.join(carpeta, archivo)
        if not os.path.exists(ruta):
            fallos.append(f"archivo declarado ausente: {archivo}")
        elif sha256(ruta) != h:
            fallos.append(f"huella no coincide: {archivo}")
    if not meta.get("archivos"):
        fallos.append("sin huellas de los archivos de datos")
    return fallos


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  (nada se publica; ningún DOI acuñado)")
    with tempfile.TemporaryDirectory() as td:
        ok = os.path.join(td, "ok")
        crear_paquete(ok)
        f0 = revisar(ok)
        print(f"paquete completo: {len(f0)} fallos {f0}")
        prueba(f0 == [], "el paquete completo debe pasar")
        siembras = {
            "sin licencia": lambda p: os.remove(os.path.join(p, "LICENSE")),
            "licencia no SPDX": lambda p: _cambiar(p, "licencia_spdx", "mi propia licencia"),
            "sin procedencia": lambda p: _cambiar(p, "procedencia", ""),
            "datos alterados": lambda p: open(os.path.join(p, "flujo.csv"), "a").write("6,1.0\n"),
            "sin unidades": lambda p: _cambiar(p, "unidades", {}),
            "sin CITATION": lambda p: os.remove(os.path.join(p, "CITATION.cff")),
        }
        esperado = {"sin licencia": "falta LICENSE", "licencia no SPDX": "SPDX", "sin procedencia": "procedencia",
                    "datos alterados": "huella no coincide", "sin unidades": "unidades", "sin CITATION": "falta CITATION.cff"}
        for nombre, siembra in siembras.items():
            p = os.path.join(td, nombre.replace(" ", "_"))
            shutil.copytree(ok, p)
            siembra(p)
            f = revisar(p)
            print(f"defecto sembrado «{nombre}»: {f}")
            prueba(any(esperado[nombre] in x for x in f), f"debe detectar «{nombre}»")
        meta = json.load(open(os.path.join(ok, "metadatos.json"), encoding="utf-8"))
        print(f"identificador persistente: {meta['identificador']}")
    print("Pruebas superadas.")


def _cambiar(p, clave, valor):
    ruta = os.path.join(p, "metadatos.json")
    meta = json.load(open(ruta, encoding="utf-8"))
    meta[clave] = valor
    json.dump(meta, open(ruta, "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
