# SPDX-License-Identifier: Apache-2.0
"""Verifica que los SVG de los talleres sean legibles: sin textos solapados y sin textos fuera del lienzo.

Estimación geométrica (ancho de carácter ≈ 0,55 × tamaño de fuente), suficiente para detectar los defectos habituales.
Uso: python talleres/_comun/verificar_figuras.py   (sale con código 1 si hay problemas)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
TEXTO = re.compile(r'<text x="([\d.\-]+)" y="([\d.\-]+)" font-size="(\d+)" fill="[^"]+" text-anchor="(\w+)"[^>]*>([^<]*)</text>')
ANCHO = re.compile(r'viewBox="0 0 (\d+) (\d+)"')


def revisar(f: Path) -> list[str]:
    s = f.read_text(encoding="utf-8")
    ancho, alto = (int(v) for v in ANCHO.search(s).groups())
    cajas = []
    for m in TEXTO.finditer(s):
        x, y, tam, anc, txt = float(m.group(1)), float(m.group(2)), int(m.group(3)), m.group(4), m.group(5)
        w = len(txt) * tam * 0.55
        x0 = x if anc == "start" else (x - w / 2 if anc == "middle" else x - w)
        cajas.append((x0, x0 + w, y - tam, y, txt))
    prob = []
    for x0, x1, y0, y1, txt in cajas:
        if x0 < 0 or x1 > ancho or y0 < 0 or y1 > alto:
            prob.append(f"fuera del lienzo: «{txt[:40]}»")
    for i, a in enumerate(cajas):
        for b in cajas[i + 1:]:
            if a[0] < b[1] and b[0] < a[1] and a[2] < b[3] and b[2] < a[3]:
                prob.append(f"solape: «{a[4][:30]}» con «{b[4][:30]}»")
    return prob


def main() -> int:
    total = 0
    n = 0
    for f in sorted(RAIZ.glob("T*/figuras/*.svg")):
        n += 1
        for p in revisar(f):
            total += 1
            print(f"{f.relative_to(RAIZ)}: {p}")
    print(f"{n} figuras revisadas, {total} problemas")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
