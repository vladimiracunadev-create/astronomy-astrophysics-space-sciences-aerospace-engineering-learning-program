#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C04: revision automatica minima de un documento HTML SINTETICO para lectores de pantalla.

Criterios (inspirados en WCAG 2.2, consultada 2026-11-11: 1.1.1 contenido no textual; el resto de reglas son
del curso, NO una lista oficial): idioma declarado, titulo, un solo h1, sin saltos de nivel de encabezado, imagenes con alt
(decorativas con alt vacio), enlaces con texto distinguible, tablas con celdas de encabezado th.
Datos: un documento inventado sobre las lunas de Jupiter, una version "mala" y una "corregida". Sin datos reales.
Unidades: conteo de hallazgos. Segunda via: cada hallazgo se valida contra una lista esperada escrita a mano.
Tolerancia: igualdad exacta. Limite: una revision automatica NO sustituye la prueba con un lector de pantalla y con personas.
"""
from __future__ import annotations
import platform
from html.parser import HTMLParser

MALO = """<html><head></head><body>
<h2>Lunas galileanas</h2>
<img src="io.png">
<img src="fondo.png" alt="">
<img src="grafico.png" alt="grafico">
<h4>Datos</h4>
<p><a href="a.html">haz clic aqui</a> y <a href="b.html">mas informacion</a></p>
<table><tr><td>Luna</td><td>Periodo (d)</td></tr><tr><td>Io</td><td>1,77</td></tr></table>
<h1>Fin</h1>
</body></html>"""

BUENO = """<html lang="es"><head><title>Lunas galileanas</title></head><body>
<h1>Lunas galileanas</h1>
<img src="io.png" alt="Io, luna amarillenta con manchas oscuras de volcanes">
<img src="fondo.png" alt="">
<img src="grafico.png" alt="Grafico de periodos orbitales; datos en la tabla siguiente">
<h2>Datos</h2>
<p><a href="a.html">Guia de observacion de las lunas</a> y <a href="b.html">Tabla de efemerides</a></p>
<table><tr><th scope="col">Luna</th><th scope="col">Periodo (d)</th></tr><tr><td>Io</td><td>1,77</td></tr></table>
</body></html>"""

GENERICOS = {"haz clic aqui", "mas informacion", "aqui", "leer mas", "ver mas"}
ALT_POBRE = {"grafico", "imagen", "foto", "image"}


class Revisor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h = []; self.imgs = []; self.enlaces = []; self.th = 0; self.td = 0
        self.lang = None; self.titulo = False; self._a = None; self._t = ""; self._en_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._en_title = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.h.append(int(tag[1]))
        elif tag == "img":
            self.imgs.append(a.get("alt"))
        elif tag == "a":
            self._a = ""
        elif tag == "th":
            self.th += 1
        elif tag == "td":
            self.td += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._en_title = False
        if tag == "a" and self._a is not None:
            self.enlaces.append(self._a.strip().lower()); self._a = None

    def handle_data(self, data):
        if self._en_title and data.strip():
            self.titulo = True
        if self._a is not None:
            self._a += data


def revisar(html: str):
    r = Revisor(); r.feed(html)
    h = []
    if not r.lang: h.append("falta lang en <html>")
    if not r.titulo: h.append("falta <title>")
    if r.h.count(1) != 1: h.append(f"hay {r.h.count(1)} h1 (se espera 1)")
    for a, b in zip(r.h, r.h[1:]):
        if b > a + 1: h.append(f"salto de encabezado h{a} -> h{b}")
    for i, alt in enumerate(r.imgs, 1):
        if alt is None: h.append(f"imagen {i} sin atributo alt")
        elif alt.strip().lower() in ALT_POBRE: h.append(f"imagen {i} con alt poco informativo ({alt!r})")
    for e in r.enlaces:
        if e in GENERICOS: h.append(f"enlace con texto generico ({e!r})")
    if r.td and not r.th: h.append("tabla de datos sin celdas th")
    return h


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Documentos SINTETICOS; reglas del curso (no es lista oficial); no sustituye prueba con lector de pantalla.")
    hm = revisar(MALO)
    hb = revisar(BUENO)
    print(f"Documento MALO: {len(hm)} hallazgos")
    for x in hm: print("  -", x)
    print(f"Documento CORREGIDO: {len(hb)} hallazgos")
    for x in hb: print("  -", x)
    assert "falta lang en <html>" in hm and "falta <title>" in hm
    assert any("h2 -> h4" in x for x in hm) and any("sin atributo alt" in x for x in hm)
    assert any("generico" in x for x in hm) and "tabla de datos sin celdas th" in hm
    assert hb == [], hb
    # alt vacio en imagen decorativa NO es hallazgo (2.a imagen del malo)
    assert not any("imagen 2" in x for x in hm)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
