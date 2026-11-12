#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Genera el programa académico unificado  a partir de la línea base y de la colocación de los módulos.

Entradas (solo lectura): catalogo/clases.jsonl y catalogo/estructura/colocacion/Rxx.json.
Salidas:
  PROGRAMA_ACADEMICO_COMPLETO.md         índice unificado por áreas y bloques
  catalogo/estructura/estructura.json        áreas y bloques con su tamaño
  catalogo/estructura/clases_programadas.jsonl  clases programadas (no redactadas) con su necesidad
  catalogo/estructura/equivalencias.json     dónde vive cada tema de cada módulo de ruta

Reglas: A01 (B01-B08) no cambia; los bloques se numeran de forma consecutiva en orden de área; las clases programadas se agregan al
final de un bloque existente (Bnn-C21, ...) o forman bloques nuevos (con numeración consecutiva). No se redacta ninguna clase.
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "catalogo" / "estructura"

AREAS = [
    ("A01", "Alfabetización científica, astronómica y tecnológica",
     "Punto de partida común: observar y medir el cielo, entender la ciencia como método y adquirir la matemática, la física, la química y la informática básicas. Nivel N0–N1. **Sin cambios respecto de la línea base.**"),
    ("A02", "Matemática, física computacional y métodos científicos",
     "Los lenguajes cuantitativos del programa: cálculo, álgebra lineal, simulación, estadística e incertidumbre, metrología, computación científica, señales y control; más aprendizaje automático, inferencia y verificación de software. Nivel N2–N3."),
    ("A03", "Astrofísica y ciencias fundamentales del universo",
     "La física del universo: estrellas, galaxias, cosmología, objetos compactos, mensajeros, exoplanetas, el Sol y su plasma, y física nuclear y de partículas, con profundización en interiores estelares, universo temprano y clima espacial. Nivel N2–N4."),
    ("A04", "Óptica, telescopios y observatorios científicos",
     "Cómo se observa: óptica, telescopios, detectores, espectroscopía, radioastronomía y observatorios terrestres y espaciales, con profundización en diseño óptico, antenas e interferometría. Nivel N3–N4."),
    ("A05", "Ciencias planetarias, astroquímica y habitabilidad",
     "Los mundos y la vida: formación planetaria, geología, atmósferas, química, astrobiología, observación terrestre, cuerpos menores y recursos, con bloques nuevos de vulcanismo, impactos, geofísica y astroquímica. Nivel N2–N4."),
    ("A06", "Mecánica orbital, navegación y vuelo espacial",
     "Órbitas, perturbaciones, navegación, trayectorias, dinámica cislunar, lanzamiento y propulsión, con optimización de trayectorias, transferencias de Lambert y fluidos de propulsión. Nivel N3–N4."),
    ("A07", "Ingeniería y construcción de sistemas espaciales",
     "La ingeniería del satélite y de la misión: sistemas, estructuras, térmica, potencia, actitud, aviónica, comunicaciones, integración y ensayos, con enlaces, antenas, comunicaciones ópticas y plataformas pequeñas. Nivel N3–N4."),
    ("A08", "Operaciones de misión y robótica espacial",
     "Operar la misión y construir fuera de la Tierra: control de misión, robótica, percepción, movilidad, manipulación, autonomía y logística extraterrestre. Nivel N3–N4."),
    ("A09", "Astronáutica humana, medicina y hábitats",
     "La persona en el espacio: preparación de astronautas, medicina y biología, hábitats y soporte vital, con bloques nuevos de salud, radiación, emergencias y bioregeneración. Nivel N3–N4."),
    ("A10", "Entorno orbital, derecho y seguridad espacial",
     "Un espacio compartido y seguro: tráfico y sostenibilidad orbital, derecho internacional y nacional, espectro y licencias, responsabilidad, seguridad y resiliencia. Tratamiento histórico, jurídico, defensivo y de resiliencia. Nivel N3–N4."),
    ("A11", "Economía, industria y gestión de proyectos espaciales",
     "Cadena de valor, costos, financiamiento, seguros, creación de empresas y gestión de proyectos espaciales. Nivel N3–N4."),
    ("A12", "Educación, historia aplicada y divulgación astronómica",
     "Enseñar, divulgar e investigar el cielo: historia y arqueoastronomía aplicadas, saberes y educación intercultural, didáctica, ciencia ciudadana, accesibilidad y comunicación. Nivel N3–N4."),
]
AREA_ORDEN = [a[0] for a in AREAS]

# Cinco bloques existentes (antes B57-B64 en la línea base 0.1.0) se reubican en áreas más claras.
AREA_BLOQUE_EXISTENTE = {"B96": "A08", "B97": "A08", "B104": "A09", "B105": "A09", "B106": "A09", "B118": "A10", "B119": "A10", "B124": "A11"}

# Bloques nuevos pequeños que se absorben en un bloque existente (como clases C21+).
FUSION = {
    "Criósferas y mundos helados": "B53",
    "Gobernanza, equidad y sostenibilidad espacial": "B119",
    "Marco jurídico internacional del espacio (profundización)": "B119",
    "Operaciones de cabina y vehículos tripulados": "B104",
    "Autonomía a bordo y planificación de decisiones": "nuevo: Autonomía y teleoperación espacial",
    "Teleoperación y autonomía supervisada": "nuevo: Autonomía y teleoperación espacial",
}

# Área final de los bloques nuevos cuya área propuesta no coincide con la estructura final.
AREA_NUEVO = {
    "Acondicionamiento físico y rehabilitación de astronautas": "A09", "Actividades extravehiculares y trajes espaciales": "A09",
    "Arquitectura y factores humanos de hábitats extraterrestres": "A09", "Emergencias y seguridad de tripulación": "A09",
    "Factores humanos y liderazgo de tripulación": "A09", "Radiobiología y protección radiológica espacial": "A09",
    "Salud conductual y bienestar en aislamiento": "A09", "Seguridad y respuesta a emergencias en hábitats": "A09",
    "Sistemas bioregenerativos y cultivo en hábitats": "A09", "Telemedicina y monitorización de salud en misión": "A09",
    "Urgencias médicas y atención clínica en misión": "A09",
    "Localización y mapeo robótico": "A08", "Logística y cadena de suministro extraterrestre": "A08", "Manipuladores robóticos espaciales": "A08",
    "Movilidad de robots planetarios": "A08", "Percepción visual robótica": "A08", "Autonomía y teleoperación espacial": "A08",
    "Resiliencia y continuidad de infraestructura espacial": "A10", "Espectro, licencias y regulación satelital": "A10",
    "Regulación nacional de actividades espaciales": "A10", "Responsabilidad, daños y controversias espaciales": "A10",
    "Historia y arqueoastronomía aplicadas": "A12", "Saberes astronómicos y educación intercultural": "A12",
    "Didáctica de la astronomía": "A12", "Ciencia ciudadana astronómica": "A12",
    "Accesibilidad e inclusión en la enseñanza de la astronomía": "A12", "Comunicación y divulgación científica": "A12",
    "Seguros espaciales": "A11", "Financiamiento de proyectos y negocios espaciales": "A11", "Creación y operación de empresas espaciales": "A11",
}


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def cargar_base():
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        filas = [json.loads(x) for x in f if x.strip()]
    tronco = [r for r in filas if r["tipo"] == "tronco_comun"]
    return tronco, {r["modulo_id"]: r["modulo_titulo"] for r in filas if r.get("modulo_id")}


def construir():
    tronco, mod_nombre = cargar_base()
    bloques_base = collections.OrderedDict()
    for r in tronco:
        bloques_base.setdefault(r["bloque_id"], {"id": r["bloque_id"], "titulo": r["bloque_titulo"], "area_base": r["area"], "clases": []})["clases"].append(r)

    def area_de_existente(bid: str) -> str:
        return AREA_BLOQUE_EXISTENTE.get(bid, bloques_base[bid]["area_base"])

    # --- recoger propuestas en orden determinista (ruta, módulo, tema) ---
    propuestas = collections.OrderedDict()   # (destino, titulo_norm) -> dict
    for f in sorted(glob.glob(str(SALIDA / "colocacion" / "R*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for m in d["modulos"]:
            for t in m["temas"]:
                if t["destino"] != "nueva":
                    continue
                p = t["propuesta"]
                destino = p["bloque"]
                nombre_nuevo = destino[len("nuevo: "):] if destino.startswith("nuevo: ") else None
                if nombre_nuevo and nombre_nuevo in FUSION:
                    destino = FUSION[nombre_nuevo]
                if destino.startswith("nuevo: "):
                    nombre_nuevo = destino[len("nuevo: "):]
                else:
                    nombre_nuevo = None
                k = (destino, norm(p["titulo"]))
                e = propuestas.setdefault(k, {"destino": destino, "titulo": p["titulo"], "necesidad": p["necesidad"],
                                              "area_propuesta": p["area"], "roles": [], "origen": []})
                if d["ruta_id"] not in e["roles"]:
                    e["roles"].append(d["ruta_id"])
                e["origen"].append(t["clases_ruta"])
                t["_k"] = k

    # --- bloques nuevos: área final y numeración consecutiva ---
    nuevos = {}
    for (destino, _), e in propuestas.items():
        if destino.startswith("nuevo: "):
            nombre = destino[len("nuevo: "):]
            if nombre not in AREA_NUEVO:
                m = re.match(r"^A0[2-7]$", e["area_propuesta"])
                if not m:
                    raise SystemExit(f"falta el área final del bloque nuevo: {nombre!r} (área propuesta {e['area_propuesta']!r})")
                AREA_NUEVO[nombre] = e["area_propuesta"]
            nuevos.setdefault(nombre, {"nombre": nombre, "area": AREA_NUEVO[nombre], "clases": []})
    orden = sorted(nuevos.values(), key=lambda b: (AREA_ORDEN.index(b["area"]), norm(b["nombre"])))
    # numeración consecutiva por área: los bloques existentes ya la traen y los nuevos continúan
    n = 0
    for aid in AREA_ORDEN:
        for bid in [x for x in bloques_base if area_de_existente(x) == aid]:
            n += 1
            assert bid == f"B{n:02d}", f"el bloque {bid} debería ser B{n:02d} para que la numeración sea consecutiva"
        for b in orden:
            if b["area"] == aid:
                n += 1
                b["id"] = f"B{n:02d}"
    por_nombre = {b["nombre"]: b for b in orden}

    # --- numerar clases programadas ---
    extension = collections.defaultdict(list)    # bloque existente -> clases
    for (destino, _), e in propuestas.items():
        if destino.startswith("nuevo: "):
            b = por_nombre[destino[len("nuevo: "):]]
            e["bloque_id"] = b["id"]
            b["clases"].append(e)
            e["id"] = f"{b['id']}-C{len(b['clases']):02d}"
            e["area"] = b["area"]
        else:
            extension[destino].append(e)
            e["bloque_id"] = destino
            e["id"] = f"{destino}-C{20 + len(extension[destino]):02d}"
            e["area"] = area_de_existente(destino)
    return tronco, mod_nombre, bloques_base, extension, orden, propuestas, area_de_existente


def areas_redactadas(estructura: list) -> str:
    """Describe qué áreas tienen todas sus clases redactadas (se calcula con las carpetas de programa/clases)."""
    completas, parciales = [], []
    for a in estructura:
        ids = {b["id"] for b in a["bloques"]}
        n = sum(1 for f in glob.glob(str(ROOT / "programa" / "clases" / "*" / "*" / "CLASE.md"))
                if Path(f).parent.parent.name in ids)
        tot = a["existentes"] + a["programadas"]
        if n == tot:
            completas.append(a["area"])
        elif n:
            parciales.append(f"{a['area']} parcial ({n} de {tot})")
    if not completas and not parciales:
        return "ninguna área completa"
    txt = "áreas completas: " + (f"{completas[0]} a {completas[-1]}" if len(completas) > 1 else (completas[0] if completas else "ninguna"))
    return txt + ("; " + "; ".join(parciales) if parciales else "")


def escribir_todo() -> dict:
    tronco, mod_nombre, bloques_base, extension, nuevos, propuestas, area_de = construir()
    for e in propuestas.values():
        assert not e["area"] == "A01", e
    # --- estructura por área ---
    estructura = []
    total_exist = total_prog = 0
    for aid, titulo, intro in AREAS:
        bl = []
        for bid, b in bloques_base.items():
            if area_de(bid) == aid:
                ext = extension.get(bid, [])
                bl.append({"id": bid, "titulo": b["titulo"], "existentes": 20, "programadas": len(ext), "nuevo": False})
        for b in nuevos:
            if b["area"] == aid:
                bl.append({"id": b["id"], "titulo": b["nombre"], "existentes": 0, "programadas": len(b["clases"]), "nuevo": True})
        estructura.append({"area": aid, "titulo": titulo, "bloques": bl,
                           "existentes": sum(x["existentes"] for x in bl), "programadas": sum(x["programadas"] for x in bl)})
        total_exist += estructura[-1]["existentes"]
        total_prog += estructura[-1]["programadas"]
    # --- documento ---
    L = []
    L += ["# Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial", "",
          "**Estructura vigente** (aprobada por el autor, 2026-11-05)  |  **Base:** línea base inicial (2026-10-31)", "",
          "**Alcance:** índice unificado de clases: todo el contenido del programa vive dentro de áreas (A) y bloques (B). "
          "Los contenidos que antes formaban los módulos de las rutas profesionales se ubicaron en el bloque que les corresponde; "
          "lo que ningún bloque cubría aparece como **clase programada**: citada, ubicada y justificada, **no redactada**. "
          "El área A01 no cambia. Los bloques están numerados de forma consecutiva (B01–B133).", "",
          "## Resumen", "",
          "| Área | Bloques | Clases de la línea base | Clases programadas | Total |", "|---|---:|---:|---:|---:|"]
    for a in estructura:
        L.append(f"| **{a['area']}** · {a['titulo']} | {len(a['bloques'])} | {a['existentes']} | {a['programadas']} | {a['existentes'] + a['programadas']} |")
    nb = sum(len(a["bloques"]) for a in estructura)
    L += [f"| **Total** | **{nb}** | **{miles(total_exist)}** | **{total_prog}** | **{miles(total_exist + total_prog)}** |", "",
          "Las áreas **no** tienen el mismo tamaño: crecen según el contenido que necesitan. "
          f"La línea base tenía 8 áreas, 64 bloques y 1.280 clases de tronco; esta propuesta tiene {len(estructura)} áreas, {nb} bloques y {miles(total_exist + total_prog)} clases. "
          "Las 3.840 clases de las rutas se integraron aquí: 1.101 de sus 1.920 temas ya estaban cubiertos por clases existentes y 819 dieron lugar a "
          f"{total_prog} clases programadas distintas (varios temas coinciden en una misma clase). Hoy hay {miles(len(glob.glob(str(ROOT / 'programa' / 'clases' / '*' / '*' / 'CLASE.md'))))} clases con texto redactado ({areas_redactadas(estructura)}), todas pendientes de revisión disciplinar; el resto no está redactado.", "",
          "**Cómo leer una línea:** `- **ID — título.** descripción`. Las clases programadas llevan la marca *Programada* y la necesidad que resuelven.", ""]
    for a, (aid, titulo, intro) in zip(estructura, AREAS):
        L += [f"## {aid} — {titulo}", "", intro, ""]
        for b in a["bloques"]:
            if not b["nuevo"]:
                base = bloques_base[b["id"]]
                ext = extension.get(b["id"], [])
                L += [f"### {b['id']} — {b['titulo']}", ""]
                if ext:
                    L += [f"*Bloque ampliado: {len(base['clases'])} clases de la línea base y {len(ext)} más.*", ""]
                for r in base["clases"]:
                    L.append(f"- **{r['id']} — {r['titulo']}.** {r['descripcion_preliminar']}")
                for e in ext:
                    L.append(f"- **{e['id']} — {e['titulo']}.** {marca(e)}")
                L.append("")
            else:
                nuevo = next(x for x in nuevos if x["id"] == b["id"])
                muestra = "; ".join(c["titulo"] for c in nuevo["clases"][:3])
                L += [f"### {b['id']} — {b['titulo']}", "",
                      f"*Bloque nuevo ({len(nuevo['clases'])} clases): {muestra}"
                      + ("…" if len(nuevo["clases"]) > 3 else ".") + "*", ""]
                for e in nuevo["clases"]:
                    L.append(f"- **{e['id']} — {e['titulo']}.** {marca(e)}")
                L.append("")
    # --- equivalencias ---
    equiv = {}
    L += ["## Equivalencias con los módulos de las rutas de la línea base", "",
          "Los módulos `Rxx-Mxx` de la línea base ya no son una capa de contenido; sus IDs se conservan como referencia. "
          "Para cada módulo: los bloques donde vive su contenido y cuántos de sus 10 temas estaban cubiertos o se programaron.", ""]
    por_k = {k: e for k, e in propuestas.items()}
    for f in sorted(glob.glob(str(SALIDA / "colocacion" / "R*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        rid = d["ruta_id"]
        L += [f"### {rid}", ""]
        for m in d["modulos"]:
            bl = collections.Counter()
            ex = pr = 0
            for t in m["temas"]:
                if t["destino"] == "existente":
                    ex += 1
                    for c in t["tronco"]:
                        bl[c.split("-")[0]] += 1
                    equiv[t["clases_ruta"]] = {"tema": t["tema"], "destino": "existente", "clases": t["tronco"]}
                else:
                    pr += 1
                    p = t["propuesta"]
                    destino = p["bloque"]
                    nom = destino[len("nuevo: "):] if destino.startswith("nuevo: ") else None
                    if nom and nom in FUSION:
                        destino = FUSION[nom]
                    e = propuestas[(destino, norm(p["titulo"]))]
                    bl[e["bloque_id"]] += 1
                    equiv[t["clases_ruta"]] = {"tema": t["tema"], "destino": "programada", "clases": [e["id"]]}
            bloques = ", ".join(sorted(bl))
            L.append(f"- **{m['modulo']} — {m['nombre']}:** {bloques} · {ex} temas en clases de la línea base, {pr} en clases programadas")
        L.append("")
    texto = "\n".join(L).rstrip() + "\n"
    (ROOT / "PROGRAMA_ACADEMICO_COMPLETO.md").write_text(texto, encoding="utf-8", newline="\n")
    (SALIDA / "estructura.json").write_text(json.dumps(estructura, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (SALIDA / "equivalencias.json").write_text(json.dumps(equiv, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    with (SALIDA / "clases_programadas.jsonl").open("w", encoding="utf-8", newline="\n") as fh:
        for e in propuestas.values():
            fh.write(json.dumps({"id": e["id"], "area": e["area"], "bloque_id": e["bloque_id"], "titulo": e["titulo"],
                                 "estado": "programada_sin_redactar", "necesidad": e["necesidad"], "roles": e["roles"],
                                 "origen": e["origen"]}, ensure_ascii=False) + "\n")
    escribir_guias_y_metadatos(estructura, nuevos, bloques_base)
    return {"areas": len(estructura), "bloques": nb, "existentes": total_exist, "programadas": total_prog}


def redactada(cid: str) -> bool:
    return bool(glob.glob(str(ROOT / "programa" / "clases" / cid.split("-")[0] / f"{cid}-*" / "CLASE.md")))


def marca(e: dict) -> str:
    if redactada(e["id"]):
        return f"*Texto redactado, pendiente de revisión.* {e['necesidad']}"
    return f"*Programada.* {e['necesidad']}"


def slug(titulo: str) -> str:
    base = unicodedata.normalize("NFD", titulo.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def escribir_guias_y_metadatos(estructura, nuevos, bloques_base) -> None:
    """Guía de cada bloque nuevo en programa/tronco-comun/ y metadatos de los 133 bloques, en orden consecutivo."""
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    nombre_ruta = {r["id"]: r["nombre"] for r in rutas}
    dir_ruta = {r["id"]: Path(glob.glob(str(ROOT / "programa" / "rutas-profesionales" / f"{r['id']}-*"))[0]).name[len(r["id"]) + 1:] for r in rutas}
    areas = {aid: titulo for aid, titulo, _ in AREAS}
    for b in nuevos:
        L = [f"# {b['id']} — {b['nombre']}", "",
             f"> **Bloque nuevo de la estructura vigente.** Sus {len(b['clases'])} clases están programadas y ninguna está redactada: "
             "se citan aquí con la necesidad que resuelven. El [programa completo](../../PROGRAMA_ACADEMICO_COMPLETO.md) las lista junto con el resto del área.", "",
             "**Programa:** Programa Integral de Astronomía, Astrofísica, Ciencias Espaciales e Ingeniería Aeroespacial  ",
             f"**Área:** {b['area']} — {areas[b['area']]}  ",
             "**Estado:** programado; no contiene clases desarrolladas.  ",
             f"**Total:** {len(b['clases'])} clases programadas.", "",
             "## Alcance", "",
             f"Este bloque existe porque los contenidos de los roles que lo necesitan no estaban cubiertos por ninguna clase de la línea base. "
             f"Cubre desde «{b['clases'][0]['titulo']}» hasta «{b['clases'][-1]['titulo']}». "
             "El orden de las clases es el de su programación y no es todavía una secuencia pedagógica revisada.", ""]
        roles = sorted({r for c in b["clases"] for r in c["roles"]})
        L += ["## Clases programadas", ""]
        for c in b["clases"]:
            L += [f"### {c['id']} — {c['titulo']}", "", marca(c), ""]
        L += ["## Roles que lo usan", ""]
        L += [f"- [{nombre_ruta[r]}](../../rutas/{dir_ruta[r]}.md)" for r in roles]
        L.append("")
        destino = ROOT / "programa" / "tronco-comun" / f"{b['id']}-{slug(b['nombre'])}.md"
        # No pisar una guía ya reescrita como guía pedagógica (la plantilla de bloque programado dice «ninguna está redactada»).
        if destino.exists() and "y ninguna está redactada: " not in destino.read_text(encoding="utf-8"):
            continue
        destino.write_text(chr(10).join(L), encoding="utf-8", newline=chr(10))
    # metadatos: todos los bloques y áreas en orden consecutivo
    previos = {x["id"]: x for x in json.loads((ROOT / "metadatos" / "bloques.json").read_text(encoding="utf-8"))}
    out = []
    for a in estructura:
        for b in a["bloques"]:
            x = dict(previos.get(b["id"], {}))
            x.update({"id": b["id"], "nombre": b["titulo"], "area": a["area"],
                      "total_clases": b["existentes"] + b["programadas"],
                      "estado_programa": "nuevo_programado" if b["nuevo"] else "linea_base"})
            x.setdefault("fuentes_preliminares", [])
            out.append(x)
    (ROOT / "metadatos" / "bloques.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8", newline=chr(10))
    ar = [{"id": a["area"], "nombre": a["titulo"], "bloques": [b["id"] for b in a["bloques"]]} for a in estructura]
    (ROOT / "metadatos" / "areas.json").write_text(json.dumps(ar, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8", newline=chr(10))


if __name__ == "__main__":
    r = escribir_todo()
    print(f"Programa: {r['areas']} áreas, {r['bloques']} bloques, {r['existentes']} clases de la línea base y {r['programadas']} programadas "
          f"(total {miles(r['existentes'] + r['programadas'])}).")
