#!/usr/bin/env python3
"""Genera el glosario del programa a partir de las clases redactadas.

Fuentes (solo lo que ya dicen las clases, sin añadir hechos nuevos):
- sección 6 «Vocabulario» de cada CLASE.md: términos en **negrita**; la definición es la
  oración de la clase que contiene el término. Si la clase solo lista el término, se usa
  la primera oración de la propia clase (fuera del vocabulario) que lo menciona;
- sección 9 «Magnitudes, símbolos y unidades» de cada CLASE.md: tabla de símbolos.

Salida en `glosario/`, en orden alfabético:
- `README.md`: índice y cómo leerlo;
- `terminos-<letra>.md`: términos y definiciones (A–Z con Ñ tras N; `0-9` aparte);
- `siglas.md`: siglas y acrónimos;
- `simbolos-y-unidades.md`: símbolos, magnitudes y unidades.

Uso:  python herramientas/generar_glosario.py [--check]
"""
from __future__ import annotations

import collections
import glob
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SALIDA = ROOT / "glosario"
MAX_CLASES = 6
MAX_DEFS = 3
FRONTERA = re.compile(r"[.;!?]\s+(?=[A-ZÁÉÍÓÚÑ¿¡`*(])")


def clave(s: str) -> str:
    """Clave de orden alfabético español (ñ después de n)."""
    s = s.lower().strip().replace("ñ", "n￿")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^0-9a-z￿Ͱ-Ͽ ]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def letra(term: str) -> str:
    k = clave(term)
    if k and "a" <= k[0] <= "z":
        return k[0].upper()
    return "0-9"


def seccion(texto: str, n: int) -> str:
    m = re.search(rf"^## {n}\..*?\n(.*?)^## {n + 1}\.", texto, re.S | re.M)
    return m.group(1) if m else ""


def limpiar(s: str) -> str:
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    return re.sub(r"\s+", " ", s).strip()


def sin_negritas(s: str) -> str:
    return s.replace("**", "").strip()


def quitar_ticks(s: str) -> str:
    return s.replace("`", "").strip()


def palabras(s: str) -> int:
    return len(re.findall(r"\w+", s))


def oraciones(texto: str):
    out, ini = [], 0
    for m in FRONTERA.finditer(texto):
        out.append(texto[ini:m.end()].strip())
        ini = m.end()
    out.append(texto[ini:].strip())
    return [o for o in out if o]


def contexto_fuera(texto: str, term: str):
    """Primera oración útil de la clase (fuera del vocabulario y de las tablas) que menciona el término."""
    base = re.sub(r"\([^)]*\)", "", term.lower()).strip()
    if not base:
        return None
    for n in (7, 8, 5, 4, 3, 2, 10, 11, 12):
        for linea in seccion(texto, n).split("\n"):
            linea = linea.strip()
            if not linea or linea[0] in "|#`$-":
                continue
            for o in oraciones(limpiar(linea)):
                ol = sin_negritas(o)
                if base in ol.lower() and 40 <= len(ol) <= 320:
                    return ol
    return None


def extraer_terminos(texto: str):
    t = limpiar(seccion(texto, 6))
    res = []
    for m in re.finditer(r"\*\*([^*]+)\*\*", t):
        term = quitar_ticks(m.group(1)).strip(" .,:;")
        if term.endswith("\\"):  # «A\*» se escribió con el asterisco escapado
            term = term[:-1] + "*"
        if not term or not clave(term):
            continue
        ini = 0
        for b in FRONTERA.finditer(t[: m.start()]):
            ini = b.end()
        mf = FRONTERA.search(t[m.end():])
        fin = m.end() + mf.start() + 1 if mf else len(t)
        oracion = sin_negritas(t[ini:fin])
        defn = None if palabras(oracion) <= palabras(term) + 2 else oracion
        res.append((term, defn))
    return res


def dividir_fila(linea: str):
    linea = linea.strip()
    linea = linea[1:-1] if linea.endswith("|") else linea[1:]
    celdas, cur, dentro = [], "", False
    for ch in linea:
        if ch == "`":
            dentro = not dentro
            cur += ch
        elif ch == "|" and not dentro:
            celdas.append(cur.strip())
            cur = ""
        else:
            cur += ch
    celdas.append(cur.strip())
    return celdas


def extraer_simbolos(texto9: str):
    filas = []
    for l in texto9.split("\n"):
        l = l.strip()
        if not l.startswith("|"):
            continue
        celdas = dividir_fila(l)
        if len(celdas) < 3 or set("".join(celdas)) <= set("-: "):
            continue
        if celdas[0].lower().startswith(("símbolo", "simbolo")):
            continue
        celdas = (celdas + ["", "", ""])[:4]
        sim = quitar_ticks(celdas[0])
        if sim:
            filas.append([sim, quitar_ticks(celdas[1]), celdas[2].replace("`", "").strip(), celdas[3].replace("`", "").strip()])
    return filas


def titulo_clase(texto: str, cid: str) -> str:
    m = re.match(r"# \S+ — (.+)", texto)
    return m.group(1).strip() if m else cid


def cargar():
    terminos = collections.defaultdict(list)
    simbolos = collections.defaultdict(list)
    n_clases = 0
    for f in sorted(glob.glob(str(ROOT / "programa" / "clases" / "*" / "*" / "CLASE.md"))):
        p = Path(f)
        cid = "-".join(p.parent.name.split("-")[:2])
        texto = p.read_text(encoding="utf-8")
        n_clases += 1
        tit = titulo_clase(texto, cid)
        ruta = "../programa/clases/" + p.parent.parent.name + "/" + p.parent.name + "/CLASE.md"
        for term, defn in extraer_terminos(texto):
            ctx = None if defn else contexto_fuera(texto, term)
            terminos[clave(term)].append(dict(term=term, defn=defn, ctx=ctx, cid=cid, tit=tit, ruta=ruta))
        for fila in extraer_simbolos(seccion(texto, 9)):
            simbolos[fila[0]].append(dict(fila=fila, cid=cid, tit=tit, ruta=ruta))
    return terminos, simbolos, n_clases


def orden_cid(cid: str):
    m = re.match(r"B(\d+)-C(\d+)", cid)
    return (int(m[1]), int(m[2])) if m else (0, 0)


def enlaces(items, max_n=MAX_CLASES):
    vistos, out = set(), []
    for it in sorted(items, key=lambda x: orden_cid(x["cid"])):
        if it["cid"] in vistos:
            continue
        vistos.add(it["cid"])
        out.append(it)
    s = "; ".join(f"[{i['cid']} · {i['tit']}]({i['ruta']})" for i in out[:max_n])
    if len(out) > max_n:
        s += f" y {len(out) - max_n} más"
    return s


def es_sigla(term: str) -> bool:
    return bool(re.fullmatch(r"[A-Z][A-Z0-9\-/]{1,9}", term.strip()))


def sigla_en(term: str):
    m = re.search(r"\(([A-Z][A-Za-z0-9\-/]{1,9})\)", term)
    return m.group(1) if m else None


def nombre_visible(items):
    nombre = collections.Counter(i["term"] for i in items).most_common(1)[0][0]
    nombre = nombre[:1].upper() + nombre[1:] if nombre[:1].islower() else nombre
    return nombre.replace("*", "\\*")


def lineas_definicion(items):
    vistas, defs = set(), []
    for i in sorted(items, key=lambda x: orden_cid(x["cid"])):
        d = i["defn"]
        if d and clave(d) not in vistas:
            vistas.add(clave(d))
            defs.append(f"- {d}")
    out = defs[:MAX_DEFS]
    if len(defs) > MAX_DEFS:
        out.append(f"- *(y {len(defs) - MAX_DEFS} formulaciones más en otras clases; ábrelas desde los enlaces)*")
    if not defs:
        for i in sorted(items, key=lambda x: orden_cid(x["cid"])):
            if i["ctx"]:
                out.append(f"- {i['ctx']} *(tal como aparece en la clase)*")
                break
        if not out:
            out.append("- Término del vocabulario de la clase; su explicación completa está en la clase enlazada.")
    return out


def escribir_terminos(terminos):
    por_letra = collections.defaultdict(list)
    for k, items in terminos.items():
        por_letra[letra(items[0]["term"])].append(k)
    archivos, indice = {}, []
    for L in sorted(por_letra, key=lambda x: ("~" if x == "0-9" else x)):
        out = [f"# Términos · {L}", "", "[⬅️ Índice del glosario](README.md)", ""]
        for k in sorted(por_letra[L]):
            items = terminos[k]
            out += [f"### {nombre_visible(items)}", ""] + lineas_definicion(items)
            out += ["", f"📘 **Dónde se aprende:** {enlaces(items)}.", ""]
        nombre = f"terminos-{L.lower()}.md"
        archivos[nombre] = "\n".join(out).rstrip() + "\n"
        indice.append((L, nombre, len(por_letra[L])))
    return archivos, indice


def escribir_siglas(terminos):
    filas = {}
    for k, items in terminos.items():
        nom = items[0]["term"]
        if es_sigla(nom):
            filas.setdefault(nom, []).extend(items)
        else:
            for i in items:
                s = sigla_en(i["term"])
                if s and s.upper() == s:
                    filas.setdefault(s, []).append(i)
    out = ["# Siglas y acrónimos", "", "[⬅️ Índice del glosario](README.md)", "",
           "Siglas y acrónimos que las clases definen en su vocabulario, en orden alfabético. "
           "Si una sigla no aparece, ninguna clase la presentó en su vocabulario.", ""]
    for sig in sorted(filas, key=clave):
        items = filas[sig]
        nombres = sorted({i["term"] for i in items if not es_sigla(i["term"])})
        out += [f"### {sig}", ""]
        if nombres:
            out.append(f"- **Significa:** {'; '.join(nombres)}.")
        out += lineas_definicion(items)
        out += ["", f"📘 **Dónde se aprende:** {enlaces(items)}.", ""]
    return "\n".join(out).rstrip() + "\n", len(filas)


def grupo_simbolo(s: str):
    k = clave(s)
    if k and "a" <= k[0] <= "z":
        return 0
    if k and any("Ͱ" <= c <= "Ͽ" for c in k):
        return 1
    return 2


def escribir_simbolos(simbolos):
    out = ["# Símbolos, magnitudes y unidades", "", "[⬅️ Índice del glosario](README.md)", "",
           "Cada símbolo que las clases usan en su tabla de magnitudes, en orden alfabético: primero las letras latinas, "
           "después las griegas y al final los signos y operadores. Un mismo símbolo puede significar cosas distintas en "
           "clases distintas: se listan las variantes y cada una enlaza a la clase donde se usa. "
           "Los valores son los de cada clase.", ""]
    for s in sorted(simbolos, key=lambda x: (grupo_simbolo(x), clave(x), x)):
        items = simbolos[s]
        out += [f"### `{s}`", ""]
        variantes = {}
        for it in sorted(items, key=lambda x: orden_cid(x["cid"])):
            _, que, unidad, _ = it["fila"]
            variantes.setdefault((que, unidad), []).append(it)
        for n, ((que, unidad), its) in enumerate(variantes.items()):
            if n >= 6:
                out.append(f"- *(y {len(variantes) - 6} usos más en otras clases)*")
                break
            partes = [f"**{que}**" if que else "",
                      f"unidad: {unidad}" if unidad and unidad not in ("—", "-") else "sin unidad propia o adimensional"]
            nota = next((i["fila"][3] for i in its if i["fila"][3]), "")
            if nota:
                partes.append(f"valor o nota: {nota}")
            ids = ", ".join(sorted({i["cid"] for i in its}, key=orden_cid)[:3])
            out.append("- " + " · ".join(p for p in partes if p) + f" — *{ids}*")
        out += ["", f"📘 **Dónde se usa:** {enlaces(items)}.", ""]
    return "\n".join(out).rstrip() + "\n"


def main():
    terminos, simbolos, n_clases = cargar()
    archivos, indice = escribir_terminos(terminos)
    siglas, n_siglas = escribir_siglas(terminos)
    archivos["siglas.md"] = siglas
    archivos["simbolos-y-unidades.md"] = escribir_simbolos(simbolos)

    def fmt(n):
        return f"{n:,}".replace(",", ".")

    idx = ["# Glosario del programa", "",
           "Glosario en **orden alfabético** de los términos, siglas, magnitudes y símbolos que usan las clases del programa. "
           "Se construye con la sección «Vocabulario» y la tabla «Magnitudes, símbolos y unidades» de cada clase: "
           "no agrega hechos nuevos, y cada entrada enlaza a las clases donde se aprende, con su modelo mental, ejemplo y ejercicios. "
           "Las definiciones heredan el estado de las clases (todas en E0, pendientes de revisión disciplinar).", "",
           f"Contiene **{fmt(len(terminos))}** términos distintos, **{fmt(n_siglas)}** siglas y **{fmt(len(simbolos))}** símbolos, "
           f"tomados de {fmt(n_clases)} clases.", "",
           "## Cómo usarlo", "",
           "1. Busca el término por su letra inicial.",
           "2. Lee la oración de la clase que lo define (es la definición tal como se enseña) y abre la clase enlazada para ver el ejemplo y los ejercicios.",
           "3. Si ves un símbolo en una fórmula, búscalo en [símbolos y unidades](simbolos-y-unidades.md); si ves una sigla, en [siglas](siglas.md).",
           "4. Cuando una entrada muestra una frase «tal como aparece en la clase», la clase no define el término en su vocabulario: la explicación está en su modelo mental o su ejemplo trabajado.", "",
           "## Términos por letra", ""]
    for L, nombre, n in indice:
        idx.append(f"- [{L}]({nombre}) — {fmt(n)} términos")
    idx += ["", "## Otros listados", "",
            "- [Siglas y acrónimos](siglas.md)",
            "- [Símbolos, magnitudes y unidades](simbolos-y-unidades.md)", "",
            "Se regenera con `python herramientas/generar_glosario.py` y se comprueba con `--check`.", "",
            "[🏠 Volver al programa](../README.md)"]
    archivos["README.md"] = "\n".join(idx) + "\n"

    if "--check" in sys.argv:
        malos = [n for n, c in archivos.items()
                 if not (SALIDA / n).exists() or (SALIDA / n).read_text(encoding="utf-8").replace("\r\n", "\n") != c]
        if malos:
            print("Glosario desactualizado en:", ", ".join(malos))
            sys.exit(1)
        print("Glosario al día.")
        return
    SALIDA.mkdir(exist_ok=True)
    for sobra in {p.name for p in SALIDA.glob("*.md")} - set(archivos):
        (SALIDA / sobra).unlink()
    for nombre, cont in archivos.items():
        (SALIDA / nombre).write_text(cont, encoding="utf-8", newline="\n")
    print(f"Glosario generado: {len(terminos)} términos, {n_siglas} siglas, {len(simbolos)} símbolos, {len(archivos)} archivos.")


if __name__ == "__main__":
    main()
