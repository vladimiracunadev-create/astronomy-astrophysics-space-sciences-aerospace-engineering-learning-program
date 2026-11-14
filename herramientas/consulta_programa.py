#!/usr/bin/env python3
"""Consulta rápida del programa (solo biblioteca estándar): encuentra bloques y clases por tema, muestra un bloque y busca en el texto de las clases.

Pensado para que una persona o un agente localice en segundos QUÉ parte del programa responde una pregunta (p. ej. «delta-v», «escudo térmico»,
«ventana de lanzamiento») y la cite con su ruta. Las clases están redactadas pero **pendientes de revisión**: ninguna está impartida, revisada ni
verificada; cítelas como material de estudio, no como fuente normativa.

Uso:
  consulta_programa.py tema "ventana de lanzamiento" [-n 15] [--texto]    clases cuyo título/bloque (o, con --texto, cuyo contenido) coinciden
  consulta_programa.py bloque B96                                          guía del bloque y lista de sus clases
  consulta_programa.py area A06                                            bloques del área
  consulta_programa.py areas                                               las 12 áreas
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def norm(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def cargar_json(ruta: str):
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def clases():
    """[(id, titulo, ruta_relativa)] de las clases redactadas en programa/clases."""
    out = []
    for f in sorted((RAIZ / "programa" / "clases").glob("B*/*/CLASE.md")):
        cid = re.match(r"(B\d+-C\d+)", f.parent.name)
        with f.open(encoding="utf-8") as fh:
            t = next((l.lstrip("# ").strip() for l in fh if l.startswith("#")), f.parent.name)
        out.append((cid.group(1) if cid else f.parent.name, t, f.relative_to(RAIZ).as_posix()))
    return out


def bloques():
    return {b["id"]: b for b in cargar_json("metadatos/bloques.json")}


def guia_bloque(bid: str):
    g = sorted((RAIZ / "programa" / "tronco-comun").glob(f"{bid}-*.md"))
    return g[0].relative_to(RAIZ).as_posix() if g else None


def cmd_tema(q: str, n: int, texto: bool) -> int:
    palabras = [norm(p) for p in re.findall(r"\w+", q) if len(p) > 2]
    if not palabras:
        print("Indique al menos una palabra de 3 letras o más."); return 2
    B = bloques(); res = []
    for cid, titulo, ruta in clases():
        bid = cid.split("-")[0]; cab = norm(f"{titulo} {B.get(bid, {}).get('nombre', '')}")
        puntos = sum(3 if p in norm(titulo) else 1 for p in palabras if p in cab)
        if texto:
            cuerpo = norm((RAIZ / ruta).read_text(encoding="utf-8"))
            puntos += sum(min(cuerpo.count(p), 5) for p in palabras) * 0.3 + min(cuerpo.count(norm(q.strip())), 10) * 2   # la frase exacta pesa más
        if puntos > 0 and (all(p in cab or (texto and p in cuerpo) for p in palabras) or puntos >= 3 * len(palabras)):
            res.append((puntos, cid, titulo, ruta, bid))
    res.sort(key=lambda r: (-r[0], r[1]))
    if not res:
        print("Sin coincidencias. Pruebe con --texto o con sinónimos."); return 1
    for _, cid, titulo, ruta, bid in res[:n]:
        print(f"{cid}  {titulo}  [{bid} · {B.get(bid, {}).get('nombre', '')}]\n    {ruta}")
    print(f"\n{min(n, len(res))} de {len(res)} coincidencias. Clases pendientes de revisión: cítelas como material de estudio.")
    return 0


def cmd_bloque(bid: str) -> int:
    B = bloques()
    if bid not in B:
        print(f"Bloque desconocido: {bid} (use B01…B133)"); return 2
    b = B[bid]; print(f"{bid} · {b['nombre']} · área {b['area']} · {b.get('total_clases', '?')} clases · guía: {guia_bloque(bid)}")
    for cid, titulo, ruta in clases():
        if cid.startswith(bid + "-"):
            print(f"  {cid}  {titulo}\n      {ruta}")
    return 0


def cmd_area(aid: str) -> int:
    A = {a["id"]: a for a in cargar_json("metadatos/areas.json")}
    if aid not in A:
        print(f"Área desconocida: {aid} (A01…A12)"); return 2
    print(f"{aid} · {A[aid]['nombre']}")
    for bid, b in bloques().items():
        if b["area"] == aid:
            print(f"  {bid}  {b['nombre']}  ({b.get('total_clases', '?')} clases)")
    return 0


def autotest() -> int:
    """El índice de clases debe reflejar el catálogo y las consultas conocidas deben dar las clases esperadas."""
    mal = []
    n = len(clases())
    if n < 2000:
        mal.append(f"se esperaban ≥ 2 000 clases redactadas y hay {n}")
    ids = {c[0] for c in clases()}
    for esperado in ("B75-C03", "B75-C09"):
        if esperado not in ids:
            mal.append(f"falta la clase {esperado}")
    if "A06" not in {a["id"] for a in cargar_json("metadatos/areas.json")} or "B75" not in bloques():
        mal.append("faltan el área A06 o el bloque B75")
    if guia_bloque("B75") is None:
        mal.append("falta la guía del bloque B75")
    for x in mal:
        print("ERROR", x)
    print("consulta_programa: autotest", "FALLÓ" if mal else f"correcto ({n} clases)")
    return 1 if mal else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tema"); t.add_argument("consulta"); t.add_argument("-n", type=int, default=15); t.add_argument("--texto", action="store_true")
    sub.add_parser("bloque").add_argument("id"); sub.add_parser("area").add_argument("id"); sub.add_parser("areas"); sub.add_parser("autotest")
    a = ap.parse_args()
    if a.cmd == "autotest":
        return autotest()
    if a.cmd == "tema":
        return cmd_tema(a.consulta, a.n, a.texto)
    if a.cmd == "bloque":
        return cmd_bloque(a.id.upper())
    if a.cmd == "area":
        return cmd_area(a.id.upper())
    for x in cargar_json("metadatos/areas.json"):
        print(f"{x['id']}  {x['nombre']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
