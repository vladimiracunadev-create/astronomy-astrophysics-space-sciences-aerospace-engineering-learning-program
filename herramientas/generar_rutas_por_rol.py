#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Genera las guías por rol (rutas/) con las áreas y bloques que cada rol necesita.

Entradas (solo lectura): catalogo/estructura/{colocacion,estructura.json,equivalencias.json},
catalogo/clases.jsonl, metadatos/rutas.json y la tabla de documentacion/MAPA_DE_RUTAS_PROFESIONALES.md.
Salidas:
  rutas/<slug>.md      guía del rol: la prosa la escribe una persona; el tramo entre
                       <!-- ruta:inicio --> y <!-- /ruta --> y el pie de navegación se generan aquí
  rutas/README.md      índice de roles con su ruta de áreas y bloques
  README.md            tabla «Rol → áreas y bloques» entre <!-- roles:inicio --> y <!-- /roles -->
Si la guía de un rol no existe, se crea un esqueleto con el estándar del programa de ciberseguridad.

Uso:
    python herramientas/generar_rutas_por_rol.py          # reescribe
    python herramientas/generar_rutas_por_rol.py --check  # falla si algo está desactualizado
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_programa as gp  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RUTAS = ROOT / "rutas"
NOMBRE_AREA = {a[0]: a[1] for a in gp.AREAS}
ORDEN_AREA = [a[0] for a in gp.AREAS]

EMOJI = {"R01": "⭐", "R02": "🌀", "R03": "🔭", "R04": "📡", "R05": "🪐", "R06": "🧪", "R07": "☀️", "R08": "🧮",
         "R09": "🛰️", "R10": "🧭", "R11": "🚀", "R12": "🛠️", "R13": "💾", "R14": "🧱", "R15": "📶", "R16": "🌍",
         "R17": "🤖", "R18": "👩‍🚀", "R19": "🩺", "R20": "🏗️", "R21": "⛏️", "R22": "🛡️", "R23": "⚖️", "R24": "🎓"}
VECINOS = {"R01": ["R02", "R07", "R08"], "R02": ["R01", "R08", "R07"], "R03": ["R04", "R12", "R16"], "R04": ["R03", "R15", "R01"],
           "R05": ["R06", "R16", "R21"], "R06": ["R05", "R19", "R20"], "R07": ["R01", "R22", "R16"], "R08": ["R01", "R02", "R13"],
           "R09": ["R10", "R11", "R12"], "R10": ["R09", "R17", "R13"], "R11": ["R09", "R14", "R12"], "R12": ["R13", "R14", "R15"],
           "R13": ["R12", "R17", "R22"], "R14": ["R12", "R11", "R20"], "R15": ["R12", "R04", "R22"], "R16": ["R05", "R08", "R22"],
           "R17": ["R10", "R13", "R20"], "R18": ["R19", "R20", "R17"], "R19": ["R18", "R06", "R20"], "R20": ["R18", "R19", "R14"],
           "R21": ["R05", "R23", "R20"], "R22": ["R15", "R13", "R23"], "R23": ["R22", "R21", "R24"], "R24": ["R23", "R01", "R18"]}


def slug_de(ruta_id: str) -> str:
    d = os.path.basename(glob.glob(str(ROOT / "programa" / "rutas-profesionales" / f"{ruta_id}-*"))[0])
    return d[len(ruta_id) + 1:]


def ancla(h: str) -> str:
    s = re.sub(r"[^\w\s-]", "", h.lower(), flags=re.UNICODE)
    return re.sub(r"\s", "-", s)


def comprimir(numeros: list[int]) -> str:
    numeros = sorted(set(numeros))
    partes, i = [], 0
    while i < len(numeros):
        j = i
        while j + 1 < len(numeros) and numeros[j + 1] == numeros[j] + 1:
            j += 1
        partes.append(f"C{numeros[i]:02d}" if i == j else f"C{numeros[i]:02d}–C{numeros[j]:02d}")
        i = j + 1
    return ", ".join(partes)


def mapa_fundamentos() -> dict[str, list[str]]:
    texto = (ROOT / "documentacion" / "MAPA_DE_RUTAS_PROFESIONALES.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^\| (R\d{2}) \|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|\s*$", texto, re.M):
        bloques = []
        for tok in re.split(r",\s*", m.group(2)):
            r = re.match(r"B(\d+)(?:–B(\d+))?$", tok.strip())
            if r:
                a, b = int(r.group(1)), int(r.group(2) or r.group(1))
                bloques += [f"B{n:02d}" for n in range(a, b + 1)]
        out[m.group(1)] = bloques
    return out


def datos():
    est = json.loads((ROOT / "catalogo" / "estructura" / "estructura.json").read_text(encoding="utf-8"))
    equiv = json.loads((ROOT / "catalogo" / "estructura" / "equivalencias.json").read_text(encoding="utf-8"))
    bloque = {}
    for a in est:
        for b in a["bloques"]:
            bloque[b["id"]] = {**b, "area": a["area"], "total": b["existentes"] + b["programadas"]}
    uso = {}
    for f in sorted(glob.glob(str(ROOT / "catalogo" / "estructura" / "colocacion" / "R*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        ids = set()
        for m in d["modulos"]:
            for t in m["temas"]:
                if t["destino"] == "existente":
                    ids.update(t["tronco"])
                else:
                    ids.update(equiv[t["clases_ruta"]]["clases"])
        uso[d["ruta_id"]] = ids
    return bloque, uso, mapa_fundamentos()


_CLASES: dict[str, str] = {}


def ruta_clase(cid: str) -> str:
    """Enlace relativo (desde rutas/) a la CLASE.md de una clase del programa."""
    if not _CLASES:
        for d in glob.glob(str(ROOT / "programa" / "clases" / "B*" / "B*-C*-*")):
            n = os.path.basename(d)
            _CLASES["-".join(n.split("-")[:2])] = os.path.relpath(os.path.join(d, "CLASE.md"), RUTAS).replace(os.sep, "/")
    return _CLASES[cid]


def evaluacion() -> dict:
    ev = json.loads((ROOT / "metadatos" / "rutas_evaluacion.json").read_text(encoding="utf-8"))
    for n in range(1, 25):
        rid = f"R{n:02d}"
        e = ev.get(rid)
        if not e:
            raise SystemExit(f"metadatos/rutas_evaluacion.json: falta {rid}")
        p = e.get("proyecto", {})
        if len(e.get("diagnostico", [])) < 4 or len(e.get("salida", [])) < 3 or not (p.get("titulo") and p.get("descripcion"))                 or len(p.get("entregables", [])) < 4 or len(p.get("criterios", [])) < 4:
            raise SystemExit(f"metadatos/rutas_evaluacion.json: {rid} está incompleto (4 preguntas, proyecto con 4 entregables y 4 criterios, 3 criterios de salida)")
    return ev


def recorrido_de(rid: str, equiv: dict) -> str:
    """Tramo generado: diagnóstico, módulos con sus clases y checkpoint, proyecto final y criterio de salida."""
    ev = evaluacion()[rid]
    col = json.loads((ROOT / "catalogo" / "estructura" / "colocacion" / f"{rid}.json").read_text(encoding="utf-8"))
    L = ["<!-- recorrido:inicio -->", "### 🗺️ Recorrido módulo por módulo", "",
         "El rol se estudia en **8 módulos** de 10 temas cada uno (cada tema es un par «concepto + aplicación»). "
         "Haz el diagnóstico, avanza por los módulos **en orden** y cierra cada uno con su checkpoint; al final, el proyecto y el criterio de salida.", "",
         "**🩺 Diagnóstico de entrada.** Si respondes «no sé» a dos o más, empieza por los fundamentos de arriba:", ""]
    L += [f"- {q}" for q in ev["diagnostico"]]
    L.append("")
    for m in col["modulos"]:
        temas = m["temas"]
        L += [f"#### {m['modulo']} · {m['nombre']}", ""]
        for i, tm in enumerate(temas, 1):
            clases = tm["tronco"] if tm["destino"] == "existente" else equiv[tm["clases_ruta"]]["clases"]
            enl = ", ".join(f"[`{c}`]({ruta_clase(c)})" for c in clases)
            L.append(f"{i}. **{tm['tema']}** — {enl}")
        sel = [temas[0]["tema"], temas[len(temas) // 2]["tema"], temas[-1]["tema"]]
        L += ["", f"✅ **Checkpoint {m['modulo']}.** Sin mirar el material, explica cómo se relacionan «{sel[0]}», «{sel[1]}» y «{sel[2]}», y resuelve un ejercicio de dos de esos temas. "
              "Guarda el resultado como evidencia de este módulo.", ""]
    p = ev["proyecto"]
    L += [f"**🎯 Proyecto final · {p['titulo']}.** {p['descripcion']}", "", "Entregables:", ""]
    L += [f"- {x}" for x in p["entregables"]]
    L += ["", "Criterios de evaluación:", ""]
    L += [f"- {x}" for x in p["criterios"]]
    L += ["", "**🏁 Criterio de salida.** Has terminado la ruta cuando:", ""]
    L += [f"- {x}" for x in ev["salida"]]
    L += ["", "<!-- /recorrido -->"]
    return chr(10).join(L)


def enlace_bloque(bid: str, b: dict) -> str:
    return "../programa/tronco-comun/" + os.path.basename(glob.glob(str(ROOT / "programa" / "tronco-comun" / f"{bid}-*.md"))[0])


def ruta_de(rid: str, bloque, uso, fund) -> tuple[str, list[str]]:
    """Devuelve el tramo generado de la guía y la lista breve (áreas y bloques) para los índices."""
    por_bloque: dict[str, list[int]] = {}
    for cid in uso[rid]:
        por_bloque.setdefault(cid.split("-")[0], []).append(int(cid.split("-C")[1]))
    nucleo = sorted(por_bloque, key=lambda b: (ORDEN_AREA.index(bloque[b]["area"]), int(b[1:])))
    fundamentos = [b for b in fund.get(rid, []) if b in bloque and b not in por_bloque]
    L = ["<!-- ruta:inicio -->", "## 📚 Tu ruta en el programa", "",
         "Orden recomendado. El programa es un solo conjunto de áreas y bloques; este rol no tiene clases propias: usa las que se indican. "
         "Las clases exactas de cada bloque están en el [programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md).", ""]
    resumen = []
    if fundamentos:
        L += ["### 🧱 Fundamentos (según tu diagnóstico)", ""]
        for i, bid in enumerate(fundamentos, 1):
            b = bloque[bid]
            L.append(f"{i}. 📚 [**{bid}** · {b['titulo']}]({enlace_bloque(bid, b)}) — {b['area']} · {b['total']} clases")
        L.append("")
    L += ["### 🎯 El núcleo del rol", ""]
    areas = []
    for bid in nucleo:
        if bloque[bid]["area"] not in areas:
            areas.append(bloque[bid]["area"])
    n = 0
    for a in areas:
        L.append(f"**{a} · {NOMBRE_AREA[a]}**")
        L.append("")
        for bid in nucleo:
            b = bloque[bid]
            if b["area"] != a:
                continue
            n += 1
            nums = por_bloque[bid]
            L.append(f"{n}. 📚 [**{bid}** · {b['titulo']}]({enlace_bloque(bid, b)}) — usa {len(nums)} de {b['total']} clases: `{bid}-` {comprimir(nums)}")
            resumen.append(f"{bid} · {b['titulo']}")
        L.append("")
    L += ["<!-- /ruta -->"]
    breve = [f"{a} · {NOMBRE_AREA[a]}: " + ", ".join(x for x in nucleo if bloque[x]["area"] == a) for a in areas]
    return chr(10).join(L), breve


ESQUELETO = """# {emoji} {nombre}

> <!-- pendiente: resumen del rol en dos líneas -->
>
> **Nivel de entrada:** <!-- pendiente --> · **Foco:** <!-- pendiente --> · **Entrega:** <!-- pendiente -->

## 🧭 Qué es y por qué importa

<!-- pendiente -->

### 🚫 Qué NO es este rol (y con quién se confunde)

<!-- pendiente -->

## 🗓️ Un día en el puesto

<!-- pendiente -->

## 🧠 Qué necesitas saber

### Conocimiento técnico

<!-- pendiente -->

### Herramientas del oficio

<!-- pendiente -->

### Habilidades no técnicas

<!-- pendiente -->

<!-- ruta:inicio -->
<!-- /ruta -->

### 🧪 Práctica y evidencias

<!-- pendiente -->

## 🎓 Reconocimientos y referencias profesionales

<!-- pendiente -->

## 📈 Progresión del rol

<!-- pendiente -->

## ⚠️ Mitos y errores comunes

<!-- pendiente -->

## 🚀 Siguientes pasos

<!-- pendiente -->

<!-- pie:inicio -->
<!-- /pie -->
"""


def pie(rid: str, nombres: dict, slugs: dict) -> str:
    vec = " · ".join(f"[{nombres[v]}]({slugs[v]}.md)" for v in VECINOS[rid])
    return ("<!-- pie:inicio -->\n---\n\n- ⬅️ [Volver al índice de rutas](./README.md)\n"
            f"- 🔀 Rutas vecinas: {vec}\n"
            "- 🧭 [Recorrido detallado y equivalencias de los módulos]"
            f"(../programa/rutas-profesionales/{os.path.basename(glob.glob(str(ROOT / 'programa' / 'rutas-profesionales' / (rid + '-*')))[0])}/RECORRIDO.md)\n"
            "- 🏠 [Inicio del programa](../README.md)\n<!-- /pie -->")


def sustituir(texto: str, marca: str, bloque: str) -> str:
    ini, fin = f"<!-- {marca}:inicio -->", f"<!-- /{marca} -->"
    if ini not in texto:
        raise SystemExit(f"falta el marcador {ini}")
    a = texto.index(ini)
    b = texto.index(fin) + len(fin)
    return texto[:a] + bloque + texto[b:]


def main() -> int:
    check = "--check" in sys.argv
    bloque, uso, fund = datos()
    equiv = json.loads((ROOT / "catalogo" / "estructura" / "equivalencias.json").read_text(encoding="utf-8"))
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    nombres = {r["id"]: r["nombre"] for r in rutas}
    slugs = {r["id"]: slug_de(r["id"]) for r in rutas}
    RUTAS.mkdir(exist_ok=True)
    cambios = []
    breves = {}
    for r in rutas:
        rid = r["id"]
        tramo, breve = ruta_de(rid, bloque, uso, fund)
        breves[rid] = breve
        destino = RUTAS / f"{slugs[rid]}.md"
        actual = destino.read_text(encoding="utf-8").replace("\r\n", "\n") if destino.exists() else ESQUELETO.format(emoji=EMOJI[rid], nombre=nombres[rid])
        nuevo = sustituir(actual, "ruta", tramo)
        rec = recorrido_de(rid, equiv)
        if "<!-- recorrido:inicio -->" in nuevo:
            nuevo = sustituir(nuevo, "recorrido", rec)
        else:
            nuevo = nuevo.replace("<!-- /ruta -->", "<!-- /ruta -->" + chr(10) + chr(10) + rec, 1)
        nuevo = sustituir(nuevo, "pie", pie(rid, nombres, slugs))
        if not destino.exists() or nuevo != actual:
            cambios.append(destino.name)
            if not check:
                destino.write_text(nuevo, encoding="utf-8", newline="\n")
    # rutas/README.md
    L = ["# 🧭 Rutas guiadas por rol", "",
         "El programa tiene un solo conjunto de áreas y bloques; **no todo es para todos a la vez**. Estas rutas ordenan el recorrido según el rol al que apuntas: qué áreas y bloques usar, en qué orden, y qué evidencia construir. "
         "Un rol no tiene clases propias: reutiliza las del programa. Todas asumen que empiezas por el **área A01** (fundamentos) o lo acreditas con un diagnóstico.", "",
         "> Leyenda: 📚 áreas y bloques · 🧪 práctica y evidencias · 📖 guía completa del rol.", ""]
    for r in rutas:
        rid = r["id"]
        destino = RUTAS / f"{slugs[rid]}.md"
        txt = destino.read_text(encoding="utf-8") if destino.exists() else ESQUELETO
        m = re.search(r"^> (?!<!--)(.+?)(?:\n>\n|\n\n)", txt, re.S | re.M)
        resumen = re.sub(r"\n> ?", " ", m.group(1)).strip() if m else "Guía en elaboración."
        L += [f"## {EMOJI[rid]} {nombres[rid]}", "", resumen, ""]
        for i, linea in enumerate(breves[rid], 1):
            L.append(f"{i}. 📚 {linea}")
        L.append(f"- 🎯 Proyecto final: {evaluacion()[rid]['proyecto']['titulo']}")
        L += ["", f"- 📖 **[Guía completa del rol →]({slugs[rid]}.md)**", ""]
    L += ["---", "", "- 🏠 [Inicio del programa](../README.md)", "- 📚 [Programa completo](../PROGRAMA_ACADEMICO_COMPLETO.md)", ""]
    nuevo_idx = "\n".join(L)
    idx = RUTAS / "README.md"
    if not idx.exists() or idx.read_text(encoding="utf-8").replace("\r\n", "\n") != nuevo_idx:
        cambios.append("README.md")
        if not check:
            idx.write_text(nuevo_idx, encoding="utf-8", newline="\n")
    # tabla en el README principal
    T = ["<!-- roles:inicio -->", "| Rol | Áreas y bloques que usa | Guía |", "|---|---|---|"]
    for r in rutas:
        rid = r["id"]
        compacto = "; ".join(re.sub(r" · [^:]+:", ":", x) for x in breves[rid])
        T.append(f"| {EMOJI[rid]} **{nombres[rid]}** | {compacto} | [📖 abrir](rutas/{slugs[rid]}.md) |")
    T.append("<!-- /roles -->")
    rp = ROOT / "README.md"
    crlf = "\r\n" in rp.read_text(encoding="utf-8", errors="ignore")
    t = rp.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "<!-- roles:inicio -->" in t:
        t2 = sustituir(t, "roles", "\n".join(T))
        if t2 != t:
            cambios.append("README.md (principal)")
            if not check:
                rp.write_text(t2, encoding="utf-8", newline="\r\n" if crlf else "\n")
    pendientes = [f.name for f in sorted(RUTAS.glob("*.md")) if f.name != "README.md" and "<!-- pendiente" in f.read_text(encoding="utf-8")]
    if pendientes:
        print(f"Guías con secciones pendientes: {len(pendientes)} de {len(rutas)}")
        if "--completo" in sys.argv:
            return 1
    if check and cambios:
        print("Guías por rol desactualizadas:", ", ".join(cambios))
        return 1
    print("Guías por rol al día." if check else f"Guías por rol actualizadas ({len(cambios)} archivos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
