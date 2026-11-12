# SPDX-License-Identifier: Apache-2.0
"""Utilidades comunes para construir la publicación (sitio HTML, PDF y aplicaciones).

Todo se genera en `build/` (ignorado por git) a partir del contenido Markdown del repositorio.
"""
from __future__ import annotations

import glob
import html
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "build"
WEB = BUILD / "web"
UNIDADES = BUILD / "pdf" / "unidades"
DIST = BUILD / "dist"

def _version() -> str:
    """Versión de publicación (release): archivo VERSION de la raíz del repositorio."""
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


VERSION = _version()
TITULO = "Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial"
AVISO = ("Texto de estudio en nivel E0: redactado y pendiente de revisión disciplinar. "
         "No otorga títulos ni habilita decisiones de vuelo, seguridad, médicas o jurídicas.")

# Carpetas y archivos que forman la publicación
RAICES_MD = ["programa", "rutas", "anexos", "talleres", "glosario", "documentacion", "fuentes", "instrucciones"]
ARCHIVOS_RAIZ = ["README.md", "PROGRAMA_ACADEMICO_COMPLETO.md", "STATUS.md", "ROADMAP.md", "SYLLABUS.md",
                 "CHANGELOG.md", "LICENSE-CONTENT.md", "CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md",
                 "THIRD_PARTY_NOTICES.md", "TRADEMARKS.md", "DATA_LICENSES.md", "ASSET_LICENSES.md",
                 "AGENTS.md", "FILE_INDEX.md", "LICENSING_AUDIT.md", "CODE_OF_CONDUCT.md"]
EXT_ACTIVOS = {".py", ".png", ".csv", ".jpg", ".jpeg", ".svg", ".txt", ".json", ".yaml", ".toml"}


def sin_acentos(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def slug_github(valor: str, separador: str = "-") -> str:
    """Ancla como la genera GitHub para los encabezados."""
    s = re.sub(r"[^\w\- ]", "", valor.lower()).replace(" ", "-")
    return s


def crear_md() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
        extension_configs={"toc": {"slugify": slug_github, "permalink": False}},
        output_format="html5",
    )


_MD = crear_md()


def titulo_de(texto: str, defecto: str) -> str:
    m = re.search(r"^#\s+(.+)$", texto, re.M)
    if not m:
        return defecto
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", m.group(1))
    return re.sub(r"[*`_]", "", t).strip()


def md_a_html(texto: str) -> str:
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    _MD.reset()
    return _diagramas(_MD.convert(texto))


def _diagramas(html_: str) -> str:
    """Sustituye los bloques Mermaid por su SVG (build/mermaid/cache); si falta, deja el texto."""
    import html as _h
    import mermaid_svg

    def sub(m):
        fuente = _h.unescape(m.group(1))
        svg = mermaid_svg.leer(fuente)
        if svg is None:
            return m.group(0)
        return f'<figure class="diagrama diagrama-svg">{svg}</figure>'

    return re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', sub, html_, flags=re.S)


def archivos_md() -> list[Path]:
    res = [ROOT / f for f in ARCHIVOS_RAIZ if (ROOT / f).exists()]
    for r in RAICES_MD:
        res += sorted((ROOT / r).rglob("*.md"))
    res += [p for p in sorted((ROOT / "catalogo").rglob("README.md"))]
    res += [ROOT / "herramientas" / "publicacion" / "README.md"]
    return res


def activos() -> list[Path]:
    res = []
    for r in ("programa", "talleres"):
        for p in (ROOT / r).rglob("*"):
            if p.is_file() and p.suffix.lower() in EXT_ACTIVOS and "__pycache__" not in p.parts:
                res.append(p)
    return res


def bloques_y_areas():
    est = json.loads((ROOT / "catalogo" / "estructura" / "estructura.json").read_text(encoding="utf-8"))
    areas, bloques = {}, {}
    for a in est:
        areas[a["area"]] = a["titulo"]
        for b in a["bloques"]:
            bloques[b["id"]] = {"titulo": b["titulo"], "area": a["area"]}
    return areas, bloques


def guia_bloque(bid: str) -> Path | None:
    g = sorted((ROOT / "programa" / "tronco-comun").glob(f"{bid}-*.md"))
    return g[0] if g else None


def clases_de_bloque(bid: str) -> list[Path]:
    return sorted((ROOT / "programa" / "clases" / bid).glob(f"{bid}-C*/CLASE.md"),
                  key=lambda p: int(re.search(r"-C(\d+)-", p.parent.name).group(1)))


def esc(s: str) -> str:
    return html.escape(s, quote=True)
