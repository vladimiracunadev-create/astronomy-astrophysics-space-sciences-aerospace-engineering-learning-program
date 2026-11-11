#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C06: verificador de un paquete publicable de proyecto educativo (todo en memoria, SINTETICO).

CONSULTADO (2026-11-11):
  - DataCite Metadata Schema 4.5: propiedades obligatorias Identifier, Creator, Title, Publisher, PublicationYear, ResourceType.
  - Principios FAIR (GO FAIR; Wilkinson et al. 2016 es el articulo de origen, cuyo texto no se pudo abrir): F1-F4, A1-A2, I1-I3, R1.
  - Creative Commons CC BY 4.0 (resumen oficial): exige atribucion, enlace a la licencia e indicar cambios.
  - UNESCO, Recomendacion sobre Recursos Educativos Abiertos (25-11-2019): definicion de REA.
SINTETICOS / ILUSTRATIVOS: los archivos del paquete, el identificador "10.0000/ejemplo" (NO es un DOI registrado), los autores y las
reglas de formato abierto (lista de extensiones elegida por la clase). El vector de prueba SHA-256 de b"abc" es el publicado por NIST/FIPS 180;
aqui solo se usa para comprobar que hashlib funciona, NO se consulto el documento.
Tolerancias: huellas SHA-256 exactas; cualquier cambio de un byte debe cambiar la huella.
"""
from __future__ import annotations
import hashlib
import json
import platform
import re

OBLIGATORIOS = ["Identifier", "Creator", "Title", "Publisher", "PublicationYear", "ResourceType"]
FORMATOS_ABIERTOS = {".md", ".csv", ".json", ".txt", ".py", ".svg"}

ARCHIVOS = {
    "README.md": b"# Proyecto educativo ILUSTRATIVO\nDatos: [datos.csv](datos.csv). Figura: [fig.png](fig.png).\n",
    "datos.csv": b"id,valor\n1,0.5\n2,0.7\n",
    "LICENSE.txt": b"Contenido: CC BY 4.0. Codigo: Apache-2.0.\n",
}

METADATOS = {
    "Identifier": "10.0000/ejemplo",
    "Creator": "Autoria ficticia",
    "Title": "Proyecto educativo ilustrativo de divulgacion",
    "Publisher": "Repositorio de ejemplo",
    "PublicationYear": 2026,
    "ResourceType": "Dataset",
    "Description": "Paquete sintetico para practicar la publicacion verificable.",
    "Keywords": ["divulgacion", "astronomia", "educacion"],
    "License": "CC BY 4.0",
    "RelatedIdentifier": ["https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html"],
}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def manifiesto(archivos):
    return {n: sha256(b) for n, b in sorted(archivos.items())}


def huella_global(man):
    return sha256(json.dumps(man, sort_keys=True).encode("utf-8"))


def faltantes(meta):
    return [k for k in OBLIGATORIOS if meta.get(k) in (None, "", [])]


def enlaces_rotos(archivos):
    rotos = []
    for n, b in archivos.items():
        if n.endswith(".md"):
            for destino in re.findall(r"\]\(([^)#]+)\)", b.decode("utf-8")):
                if not destino.startswith("http") and destino not in archivos:
                    rotos.append((n, destino))
    return rotos


def formatos_no_abiertos(archivos):
    return [n for n in archivos if "." + n.rsplit(".", 1)[-1] not in FORMATOS_ABIERTOS]


def lista_fair(meta, archivos):
    r = {}
    r["F1 identificador"] = "cumple" if meta.get("Identifier") else "falla"
    r["F2 metadatos ricos"] = "cumple" if meta.get("Description") and len(meta.get("Keywords", [])) >= 3 else "falla"
    r["F3 metadatos con el identificador"] = "cumple" if "Identifier" in meta else "falla"
    r["F4 indexado en un buscador"] = "no verificable sin conexion"
    r["A1 recuperable por protocolo estandar"] = "no verificable sin conexion"
    r["A2 metadatos aun sin datos"] = "no verificable sin conexion"
    r["I1 formato abierto"] = "cumple" if not formatos_no_abiertos(archivos) else "falla"
    r["I2 vocabularios FAIR"] = "no verificable sin conexion"
    r["I3 referencias calificadas"] = "cumple" if meta.get("RelatedIdentifier") else "falla"
    r["R1 licencia y procedencia"] = "cumple" if meta.get("License") and "LICENSE.txt" in archivos else "falla"
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    assert sha256(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    print("Vector de prueba SHA-256 de b'abc': correcto.")
    print("Metadatos obligatorios (DataCite 4.5) que faltan:", faltantes(METADATOS) or "ninguno")
    assert faltantes(METADATOS) == []
    malo = dict(METADATOS)
    malo["Publisher"] = ""
    print("  con Publisher vacio faltan:", faltantes(malo))
    assert faltantes(malo) == ["Publisher"]

    man = manifiesto(ARCHIVOS)
    print("Manifiesto SHA-256 (archivos SINTETICOS):")
    for n, h in man.items():
        print(f"  {n:<12} {h[:16]}...")
    g = huella_global(man)
    print("Huella global:", g[:16] + "...")
    alterado = dict(ARCHIVOS)
    alterado["datos.csv"] = b"id,valor\n1,0.5\n2,0.8\n"
    g2 = huella_global(manifiesto(alterado))
    print("Huella global tras cambiar un caracter de datos.csv:", g2[:16] + "...", "->", "distinta" if g2 != g else "IGUAL")
    assert g2 != g

    print("Enlaces internos rotos:", enlaces_rotos(ARCHIVOS))
    assert enlaces_rotos(ARCHIVOS) == [("README.md", "fig.png")]
    ok = dict(ARCHIVOS)
    ok["fig.svg"] = b"<svg/>"
    ok["README.md"] = ARCHIVOS["README.md"].replace(b"fig.png", b"fig.svg")
    assert enlaces_rotos(ok) == []
    print("Formatos no abiertos en el paquete:", formatos_no_abiertos(ok) or "ninguno")

    print("Lista FAIR (sobre lo comprobable sin conexion):")
    f = lista_fair(METADATOS, ok)
    for k, v in f.items():
        print(f"  {k:<40} {v}")
    c = sum(1 for v in f.values() if v == "cumple")
    nv = sum(1 for v in f.values() if v.startswith("no verificable"))
    print(f"Resumen: {c} cumplen, {nv} no verificables sin conexion, {len(f) - c - nv} fallan de {len(f)}")
    assert c == 6 and nv == 4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
