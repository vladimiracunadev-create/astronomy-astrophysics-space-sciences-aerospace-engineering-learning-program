#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B20-C01: registro reproducible de una búsqueda bibliográfica.

Datos: SINTÉTICOS (20 registros inventados que imitan metadatos bibliográficos;
no son artículos reales). Modelo: normalización de títulos y DOI, eliminación
de duplicados, criterios de inclusión/exclusión explícitos y conteo de flujo.
Además construye (sin conectarse) la URL de consulta de la API de arXiv según
su manual (S2 de la clase). Supuestos: los metadatos están completos salvo lo
indicado. Dominio de validez: demostración didáctica; no sustituye una búsqueda
real. Tolerancia: los conteos son enteros y deben conservarse exactamente.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from urllib.parse import quote

# (clave, título, año, DOI, revisado_por_pares, tema)
REGISTROS = [
    ("a1", "Pulsating variable stars: a photometric survey", 2019, "10.0000/x.001", True, "variables"),
    ("a2", "Pulsating Variable Stars - A Photometric Survey", 2019, "10.0000/x.001", True, "variables"),
    ("a3", "Period analysis of variable stars with sparse data", 2021, "10.0000/x.002", True, "variables"),
    ("a4", "Period analysis of variable stars with sparse data", 2021, "", False, "variables"),
    ("a5", "A catalogue of eclipsing binaries", 2016, "10.0000/x.003", True, "binarias"),
    ("a6", "Pulsation models for evolved stars", 2012, "10.0000/x.004", True, "variables"),
    ("a7", "Machine learning for light-curve classification", 2022, "10.0000/x.005", False, "variables"),
    ("a8", "Instrumental drift in survey photometry", 2020, "10.0000/x.006", True, "variables"),
    ("a9", "Dust extinction maps toward the Galactic plane", 2018, "10.0000/x.007", True, "polvo"),
    ("a10", "Calibration of photometric zero points", 2023, "10.0000/x.008", True, "variables"),
    ("a11", "Variable star periods from a ground-based network", 2017, "10.0000/x.009", True, "variables"),
    ("a12", "Variable star periods from a ground-based network", 2017, "10.0000/x.009", True, "variables"),
    ("a13", "Stellar rotation in young clusters", 2015, "10.0000/x.010", True, "rotacion"),
    ("a14", "Detection limits for periodic signals", 2024, "10.0000/x.011", True, "variables"),
    ("a15", "Photometric noise models for small telescopes", 2014, "10.0000/x.012", True, "variables"),
    ("a16", "Classification of variable stars: a review", 2013, "10.0000/x.013", True, "variables"),
    ("a17", "Exoplanet transit timing", 2022, "10.0000/x.014", True, "exoplanetas"),
    ("a18", "Sparse sampling and aliasing in period searches", 2021, "10.0000/x.015", True, "variables"),
    ("a19", "Opinion: the future of variable-star astronomy", 2020, "", False, "variables"),
    ("a20", "Period searches in unevenly sampled series", 2019, "10.0000/x.016", True, "variables"),
]

# Criterios (fijados ANTES de mirar los registros)
ANIO_MIN, ANIO_MAX = 2015, 2024
TEMA = "variables"


def normaliza(titulo: str) -> str:
    """Minúsculas, sin tildes ni puntuación, espacios simples."""
    base = unicodedata.normalize("NFD", titulo.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", base).strip()


def desduplica(registros):
    """Conserva el primero de cada DOI o, sin DOI, de cada título normalizado."""
    vistos, unicos = set(), []
    for r in registros:
        clave = r[3] if r[3] else "t:" + normaliza(r[1])
        clave_titulo = "t:" + normaliza(r[1])
        if clave in vistos or clave_titulo in vistos:
            continue
        vistos.add(clave)
        vistos.add(clave_titulo)
        unicos.append(r)
    return unicos


def cribado(registros):
    """Devuelve (incluidos, excluidos con motivo)."""
    incluidos, excluidos = [], []
    for r in registros:
        if not (ANIO_MIN <= r[2] <= ANIO_MAX):
            excluidos.append((r[0], "fuera de periodo"))
        elif r[5] != TEMA:
            excluidos.append((r[0], "fuera de tema"))
        elif not r[4]:
            excluidos.append((r[0], "sin arbitraje"))
        else:
            incluidos.append(r)
    return incluidos, excluidos


def url_arxiv(campo_palabras, max_results=20, start=0):
    """URL de consulta a la API de arXiv (manual del usuario, S2); no se envía."""
    q = quote(campo_palabras, safe="")
    return f"http://export.arxiv.org/api/query?search_query={q}&start={start}&max_results={max_results}"


def pruebas() -> None:
    assert normaliza("Pulsating Variable Stars - A Photometric Survey") == "pulsating variable stars a photometric survey"
    assert normaliza("Pulsating variable stars: a photometric survey") == normaliza("Pulsating Variable Stars - A Photometric Survey")
    unicos = desduplica(REGISTROS)
    inc, exc = cribado(unicos)
    # conservación del flujo: identificados − duplicados = cribados = incluidos + excluidos
    assert len(REGISTROS) - len(unicos) + len(unicos) == len(REGISTROS)
    assert len(inc) + len(exc) == len(unicos)
    # caso de referencia contado a mano en la clase (sección 13): 3 duplicados, 9 excluidos (3+4+2), 8 incluidos
    assert len(REGISTROS) - len(unicos) == 3, len(REGISTROS) - len(unicos)
    assert len(exc) == 9, len(exc)
    assert len(inc) == 8, len(inc)
    # codificación de URL según el manual: comillas %22, espacio %20
    esperado = "http://export.arxiv.org/api/query?search_query=ti%3A%22variable%20stars%22&start=0&max_results=20"
    assert url_arxiv('ti:"variable stars"') == esperado, url_arxiv('ti:"variable stars"')


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK | datos SINTÉTICOS")
    unicos = desduplica(REGISTROS)
    inc, exc = cribado(unicos)
    print(f"Identificados: {len(REGISTROS)}")
    print(f"Duplicados eliminados: {len(REGISTROS) - len(unicos)}")
    print(f"Cribados: {len(unicos)}")
    motivos = {}
    for _, m in exc:
        motivos[m] = motivos.get(m, 0) + 1
    for m, n in sorted(motivos.items()):
        print(f"  excluidos por {m}: {n}")
    print(f"Incluidos: {len(inc)}  ({', '.join(r[0] for r in inc)})")
    print("URL de consulta (no enviada):", url_arxiv('ti:"variable stars" AND abs:period'))
    print("Pausa mínima entre consultas repetidas a la API: 3 s (manual de arXiv)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
