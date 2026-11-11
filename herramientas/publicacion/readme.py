# SPDX-License-Identifier: Apache-2.0
"""Mantiene en README.md la sección «Descargas y PDF» (entre marcas).

Los enlaces apuntan a `releases/latest`, así que no caducan al publicar una versión nueva.
Uso: python herramientas/publicacion/readme.py [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: E402,F401,F403
import landing  # noqa: E402

INI, FIN = "<!-- descargas:inicio -->", "<!-- /descargas -->"


def paginas(nombre: str) -> str:
    """Las páginas no se muestran en el README para que el PDF general que lo incluye no quede desfasado."""
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


def bloque() -> str:
    d = landing.datos_landing()
    L = landing.url_descarga
    rel = landing.URL_RELEASE
    out = [INI, "## 📦 Descargas y PDF", "",
           "Los enlaces apuntan siempre a la **última versión** publicada y no caducan al publicar una nueva. "
           f"Cada versión adjunta `SHA256SUMS.txt` y sus notas. Versión actual: **{VERSION}**.", "",
           "| Descarga | Qué es |", "|---|---|",
           f"| [**📕 Programa general (PDF)**]({L('Programa-General.pdf')}){paginas('Programa-General.pdf')} | Programa completo, guías de los 24 roles y de los 133 bloques, los 20 anexos, la documentación y los glosarios |",
           f"| [**🖥️ Windows**]({rel}) · `Programa-Aeroespacial_v{VERSION}_Windows.zip` | Aplicación sin conexión, portable: extraer todo el ZIP y abrir `ProgramaAeroespacial.exe` (usa Edge o Chrome ya instalados) |",
           f"| [**📱 Android**]({rel}) · `Programa-Aeroespacial_v{VERSION}_Android.apk` | Aplicación sin conexión para móvil y tableta (Android 7 o superior) |",
           "", "<details><summary><b>📕 PDF por área</b> (guía de cada bloque y todas sus clases)</summary>", ""]
    for a in d["areas"]:
        out.append(f"- [{a['id']} · {a['titulo']}]({L(a['pdf'])}){paginas(a['pdf'])}")
    out += ["", "</details>", "",
            "<details><summary><b>📕 PDF por rol</b> (guía del rol y las clases que usa, en orden)</summary>", ""]
    for r in d["roles"]:
        out.append(f"- [{r['id']} · {r['nombre']}]({L(r['pdf'])}){paginas(r['pdf'])}")
    out += ["", "</details>", "",
            "Las aplicaciones muestran el mismo contenido que el [sitio web](" + landing.URL_PAGES + ") (Markdown convertido a HTML), con búsqueda y sin conexión. Para verificar lo que descargas:", "",
            "```bash", "sha256sum -c SHA256SUMS.txt", "```", "",
            "> El APK está firmado con una clave de publicación propia del proyecto y **no** procede de Google Play: se instala permitiendo «orígenes desconocidos». "
            "Los ejecutables de Windows **no están firmados digitalmente**; SmartScreen puede avisar. Comprueba siempre el `SHA256SUMS.txt` antes de ejecutarlos. "
            "Cómo se generan estos archivos: [`herramientas/publicacion/`](herramientas/publicacion/README.md).", FIN]
    return "\n".join(out)


def main() -> int:
    p = ROOT / "README.md"
    t = p.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in t else "\n"
    t = t.replace("\r\n", "\n")
    nuevo = bloque()
    if INI in t and FIN in t:
        t = re.sub(re.escape(INI) + r".*?" + re.escape(FIN), lambda m: nuevo, t, flags=re.S)
    else:
        ancla = "## 📎 Anexos y glosarios"
        assert ancla in t
        t = t.replace(ancla, nuevo + "\n\n" + ancla, 1)
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
