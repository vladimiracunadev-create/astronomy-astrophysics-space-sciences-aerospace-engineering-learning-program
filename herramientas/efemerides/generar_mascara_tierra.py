# SPDX-License-Identifier: Apache-2.0
"""Rasteriza la capa «land» de Natural Earth 1:110m (dominio público) en una máscara tierra/mar de 720x360 (0,5 grados).

Fuente: https://www.naturalearthdata.com/ (dominio público) vía el paquete npm world-atlas 2.0.2 (land-110m.json, TopoJSON).
Salida: simuladores/motor/mascara_tierra.js (1 bit por celda, base64, longitud -180..180 y latitud 90..-90).
Se usa sólo para dibujar la Tierra; no interviene en ningún cálculo de posición.
"""
import base64
import json
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw

RAIZ = Path(__file__).resolve().parents[2]
URL = "https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-110m.json"
W, H = 720, 360


def arcos(topo):
    sx, sy = topo["transform"]["scale"]; tx, ty = topo["transform"]["translate"]
    out = []
    for arc in topo["arcs"]:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sx + tx, y * sy + ty))
        out.append(pts)
    return out


def anillo(idxs, A):
    pts = []
    for i in idxs:
        seg = A[i] if i >= 0 else A[~i][::-1]
        pts += seg if not pts else seg[1:]
    return pts


def main():
    topo = json.load(urllib.request.urlopen(URL, timeout=60))
    A = arcos(topo)
    im = Image.new("1", (W, H), 0)
    d = ImageDraw.Draw(im)
    geoms = topo["objects"]["land"]["geometries"]
    polys = []
    for g in geoms:
        if g["type"] == "Polygon":
            polys.append(g["arcs"])
        elif g["type"] == "MultiPolygon":
            polys += g["arcs"]
    for poly in polys:
        for k, ring in enumerate(poly):
            pts = [((lon + 180) / 360 * W, (90 - lat) / 180 * H) for lon, lat in anillo(ring, A)]
            d.polygon(pts, fill=1 if k == 0 else 0)
    # Antártida: cerrar por el polo sur
    d.rectangle((0, H - 3, W, H), fill=1)
    raw = im.tobytes()
    b64 = base64.b64encode(raw).decode()
    (RAIZ / "simuladores" / "motor" / "mascara_tierra.js").write_text(
        "// SPDX-License-Identifier: Apache-2.0\n// Generado por herramientas/efemerides/generar_mascara_tierra.py (Natural Earth 1:110m, dominio público).\n"
        f"export const ANCHO = {W};\nexport const ALTO = {H};\nexport const BITS = \"{b64}\";\n", encoding="utf-8")
    land = sum(bin(b).count("1") for b in raw) / (W * H)
    print("fracción de tierra:", round(land, 3))


main()
