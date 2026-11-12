# SPDX-License-Identifier: Apache-2.0
"""Mantiene en README.md la sección «Descargas y PDF» (entre marcas) y los accesos de la cabecera.

Los enlaces apuntan a `releases/latest`, así que no caducan al publicar una versión nueva.
Uso: python herramientas/publicacion/readme.py [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import *  # noqa: E402,F401,F403
import landing  # noqa: E402

INI, FIN = "<!-- descargas:inicio -->", "<!-- /descargas -->"


def paginas(nombre: str) -> str:
    """No se muestran las páginas: el PDF general incluye este README y quedaría desfasado."""
    return ""


def _paginas_reales(nombre: str) -> str:
    f = DIST / nombre
    if not f.exists():
        return ""
    try:
        import fitz
        with fitz.open(f) as d:
            return f" ({len(d):,} págs.)".replace(",", ".")
    except Exception:
        return ""


ARCHIVO_PDF = ROOT / "documentacion" / "DESCARGAS_Y_PDF.md"


def _apps() -> list[str]:
    rel = landing.URL_RELEASE
    return ["| Descarga | Archivo | Para qué |", "|---|---|---|",
            f"| [**Windows**]({rel}) | `Programa-Aeroespacial_v{VERSION}_Windows.zip` | Portable: extraer todo el ZIP y abrir `ProgramaAeroespacial.exe` (usa Edge o Chrome ya instalados) |",
            f"| [**Android**]({rel}) | `Programa-Aeroespacial_v{VERSION}_Android.apk` | Móvil y tableta (Android 7 o superior) |"]


def _avisos() -> list[str]:
    return ["> El APK está firmado con una clave de publicación propia del proyecto, **no** procede de Google Play: se instala "
            "permitiendo «orígenes desconocidos». Los ejecutables de Windows **no están firmados digitalmente**; SmartScreen puede avisar. "
            "Comprueba siempre el `SHA256SUMS.txt` de la versión antes de ejecutarlos."]


def bloque() -> str:
    L = landing.url_descarga
    out = [INI, "## 📦 Descargas y PDF", "",
           f"**Versión: {VERSION}** (primera publicación). Es la única versión del programa: está en el archivo [`VERSION`](VERSION) y los enlaces "
           "apuntan siempre a la última publicada, así que no caducan. Las estructuras y líneas base internas no llevan número de versión.", "",
           f"| PDF principal | Contenido |", "|---|---|",
           f"| [**📕 Programa general**]({L('Programa-General.pdf')}) | Portada, programa completo, guías de los 24 roles y de los 133 bloques, los 20 anexos, la documentación y los glosarios |", "",
           "📚 **Todos los demás PDF** (12 áreas y 24 roles, con todas sus clases) están listados en "
           "[**Descargas y PDF · lista completa**](documentacion/DESCARGAS_Y_PDF.md).", "",
           "### 🖥️ Aplicaciones sin conexión", ""] + _apps() + [""] + _avisos() + ["",
           "El contenido sigue en nivel E0 (redactado, pendiente de revisión disciplinar): ver [`STATUS.md`](STATUS.md). "
           "Cómo se generan estos archivos: [`herramientas/publicacion/`](herramientas/publicacion/README.md).", FIN]
    return chr(10).join(out)


def pagina_pdf() -> str:
    d = landing.datos_landing()
    L = landing.url_descarga
    o = ["# 📦 Descargas y PDF: lista completa", "",
         f"Versión **{VERSION}**. Todos los enlaces apuntan a la última versión publicada en "
         f"[Releases]({landing.URL_RELEASE}) y no caducan. Cada versión adjunta `SHA256SUMS.txt`:", "",
         "```bash", "sha256sum -c SHA256SUMS.txt", "```", "",
         "## 📕 PDF general", "",
         f"- [**Programa general**]({L('Programa-General.pdf')}): portada, programa completo, guías de los 24 roles y de los 133 bloques, los 20 anexos, la documentación y los glosarios.", "",
         "## 🗂️ PDF por área", "",
         "Guía de cada bloque del área y todas sus clases.", "", "| Área | PDF |", "|---|---|"]
    for a in d["areas"]:
        o.append(f"| {a['id']} · {a['titulo']} | [{a['pdf']}]({L(a['pdf'])}) |")
    o += ["", "## 🧭 PDF por rol", "", "Guía del rol y las clases que usa, en orden.", "", "| Rol | PDF |", "|---|---|"]
    for r in d["roles"]:
        o.append(f"| {r['id']} · {r['nombre']} | [{r['pdf']}]({L(r['pdf'])}) |")
    o += ["", "## 🖥️ Aplicaciones sin conexión", ""] + _apps() + [""] + _avisos() + ["",
          "Volver al [README](../README.md) · [Índice de la documentación](README.md)", ""]
    return chr(10).join(o)


def main() -> int:
    p = ROOT / "README.md"
    t = p.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in t else "\n"
    t = t.replace("\r\n", "\n")
    nuevo = bloque()
    pdf_md = pagina_pdf()
    if "--check" not in sys.argv:
        ARCHIVO_PDF.write_text(pdf_md, encoding="utf-8", newline="")
    elif not ARCHIVO_PDF.exists() or ARCHIVO_PDF.read_text(encoding="utf-8").replace(chr(13)+chr(10), chr(10)) != pdf_md:
        print("DESCARGAS_Y_PDF.md desactualizado")
        return 1
    if INI in t and FIN in t:
        t = re.sub(re.escape(INI) + r".*?" + re.escape(FIN), lambda m: nuevo, t, flags=re.S)
    else:
        ancla = "## 🎯 Qué es este programa"
        assert ancla in t
        t = t.replace(ancla, nuevo + "\n\n" + ancla, 1)
    # accesos de la cabecera
    pdf_general = landing.url_descarga("Programa-General.pdf")
    if "📕 PDF general" not in t:
        t = t.replace("[📚 Programa completo](PROGRAMA_ACADEMICO_COMPLETO.md) ·",
                      f"[📕 PDF general]({pdf_general}) · [📦 Descargas](#-descargas-y-pdf) · [📚 Programa completo](PROGRAMA_ACADEMICO_COMPLETO.md) ·", 1)
    else:
        t = re.sub(r"\[📕 PDF general\]\([^)]*\)", f"[📕 PDF general]({pdf_general})", t, count=1)
    if "img.shields.io/github/v/release" not in t:
        repo = landing.REPO
        t = t.replace("[![Versión documental]",
                      f"[![Release](https://img.shields.io/github/v/release/{repo}?style=for-the-badge&label=release)]({landing.URL_RELEASE})\n[![Versión documental]", 1)
    t = t.replace("\n", nl)
    if "--check" in sys.argv:
        if p.read_text(encoding="utf-8") != t:
            print("README desactualizado")
            return 1
        print("README al día")
        return 0
    p.write_text(t, encoding="utf-8", newline="")
    print("README actualizado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
