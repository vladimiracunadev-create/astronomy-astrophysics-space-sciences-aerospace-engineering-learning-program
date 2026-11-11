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
import json
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


SEC_EXPLICA = (8, 7, 13, 14, 5, 12, 3, 15, 16, 17)
LIMITE_ARCHIVO = 300_000


def frases_seccion(texto: str, n: int):
    out = []
    for linea in seccion(texto, n).split("\n"):
        l = linea.strip()
        if not l or l[0] in "|#`$>!" or l.startswith("```"):
            continue
        l = re.sub(r"^(?:[-*]\s+|\d+[.)]\s+)", "", l)
        out += oraciones(limpiar(l))
    out = [sin_negritas(o) for o in out]
    return [(o, raices(o)) for o in out]


def modelo_mental_clase(texto: str) -> str:
    s = sin_negritas(limpiar(seccion(texto, 7)))
    res = ""
    for x in oraciones(s)[:3]:
        if len(res) + len(x) > 360:
            break
        res += (" " if res else "") + x
    return res


def por_que_clase(texto: str) -> str:
    s = sin_negritas(limpiar(seccion(texto, 2)))
    o = oraciones(s)
    res = ""
    for x in o[:2]:
        if len(res) + len(x) > 330:
            break
        res += (" " if res else "") + x
    return res


PALABRAS_VACIAS = {"de", "del", "la", "el", "los", "las", "en", "con", "por", "para", "una", "uno", "que", "al", "sus", "sin", "como"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def raiz(w: str) -> str:
    w = norm(w)
    for suf in ("ciones", "cion", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def raices(s: str):
    return {raiz(w) for w in re.findall(r"\w+", s) if len(w) >= 3}


def palabras_clave(term: str):
    base = re.sub(r"\([^)]*\)", "", term)
    return [raiz(w) for w in re.findall(r"\w+", base) if len(w) >= 4 and w.lower() not in PALABRAS_VACIAS]


def coincide(term: str, oracion: str, raices_oracion) -> bool:
    ks = palabras_clave(term)
    if not ks:
        base = re.sub(r"\([^)]*\)", "", term.lower()).strip()
        return len(base) >= 2 and re.search(r"(?<!\w)" + re.escape(base) + r"(?!\w)", oracion.lower()) is not None
    return all(k in raices_oracion for k in ks)


def contexto_clase(cache, term: str, defn):
    """Oraciones de la propia clase que explican el término (pasos, modelo mental, ejemplo) y su error frecuente."""
    if len(re.sub(r"\W", "", term)) < 2:
        return [], None
    vistos = {clave(defn)} if defn else set()
    ex = []
    for n in SEC_EXPLICA:
        for ol, rs in cache[n]:
            if 40 <= len(ol) <= 340 and clave(ol) not in vistos and coincide(term, ol, rs):
                ex.append(ol)
                vistos.add(clave(ol))
                if len(ex) == 2:
                    break
        if len(ex) == 2:
            break
    er = None
    for ol, rs in cache[18]:
        if 30 <= len(ol) <= 300 and coincide(term, ol, rs):
            er = ol
            break
    return ex, er


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
        cache = {n: frases_seccion(texto, n) for n in SEC_EXPLICA + (18,)}
        pq = por_que_clase(texto)
        mm = modelo_mental_clase(texto)
        lista = extraer_terminos(texto)
        nombres = [x for x, _ in lista]
        for term, defn in lista:
            ex, er = contexto_clase(cache, term, defn)
            vec = [n for n in nombres if clave(n) != clave(term)][:4]
            terminos[clave(term)].append(dict(term=term, defn=defn, ex=ex, er=er, pq=pq, mm=mm, vec=vec, cid=cid, tit=tit, ruta=ruta))
        for fila in extraer_simbolos(seccion(texto, 9)):
            simbolos[fila[0]].append(dict(fila=fila, cid=cid, tit=tit, ruta=ruta))
    return terminos, simbolos, n_clases


def slug_github(h: str) -> str:
    return re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")


def cargar_esencial():
    """Mapa clave de término -> (archivo, encabezado, ancla) del glosario esencial escrito a mano."""
    mapa = {}
    carpeta = SALIDA / "esencial"
    if not carpeta.exists():
        return mapa
    for f in sorted(carpeta.glob("*.md")):
        if f.name == "README.md":
            continue
        lineas = f.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
        for i, l in enumerate(lineas):
            if not l.startswith("### "):
                continue
            h = l[4:].strip()
            siguiente = next((x for x in lineas[i + 1:] if x.strip()), "")
            if siguiente.startswith("Ver "):
                continue  # entrada de remisión
            partes = {h} | {x.strip() for x in re.split(r" y | e |/|\(|\)|,| — ", h) if x.strip()}
            for parte in partes:
                k = clave(parte)
                if len(k) >= 4:
                    mapa.setdefault(k, (f.name, h, slug_github(h)))
    return mapa


def cargar_areas():
    """Devuelve {bloque: (área, título del bloque)} y {área: título}."""
    est = json.loads((ROOT / "catalogo" / "v0.2.0" / "estructura.json").read_text(encoding="utf-8"))
    bloques, areas = {}, {}
    for a in est:
        areas[a["area"]] = a["titulo"]
        for b in a["bloques"]:
            bloques[b["id"]] = (a["area"], b["titulo"])
    return bloques, areas


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
    def calidad(x):
        d = x["defn"] or ""
        return (not re.search(r"\b(es|son|se llama|se define|mide|indica|describe|significa)\b", d), orden_cid(x["cid"]))

    for i in sorted(items, key=calidad):
        d = i["defn"]
        if d and clave(d) not in vistas:
            vistas.add(clave(d))
            defs.append(f"- {d}")
    out = defs[:MAX_DEFS]
    if len(defs) > MAX_DEFS:
        out.append(f"- *(y {len(defs) - MAX_DEFS} formulaciones más en otras clases; ábrelas desde los enlaces)*")
    if not defs:
        out.append("- La clase presenta este término en su vocabulario sin una definición aparte; su explicación está en lo que sigue y en la clase enlazada.")
    return out


def bloque_contexto(items):
    ordenados = sorted(items, key=lambda x: orden_cid(x["cid"]))
    for i in ordenados:
        if i["ex"] or i["er"]:
            out = ["", f"💡 **Cómo se explica en la clase [{i['cid']}]({i['ruta']}):**"]
            out += [f"- {s}" for s in i["ex"]]
            if i["er"]:
                out.append(f"- ⚠️ **Error frecuente:** {i['er']}")
            if i["pq"]:
                out.append(f"- 🎯 **Por qué importa:** {i['pq']}")
            if i["vec"]:
                out.append("- 🔗 **Se estudia junto con:** " + ", ".join(i["vec"]) + ".")
            return out
    i = ordenados[0]
    out = ["", f"💡 **Contexto en la clase [{i['cid']}]({i['ruta']}):**"]
    if i["mm"]:
        out.append(f"- **Idea central (modelo mental):** {i['mm']}")
    if i["pq"]:
        out.append(f"- 🎯 **Por qué importa:** {i['pq']}")
    if i["vec"]:
        out.append("- 🔗 **Se estudia junto con:** " + ", ".join(i["vec"]) + ".")
    return out if len(out) > 1 else []


def paginar(base, titulo, intro, entradas):
    """Reparte las entradas en archivos de tamaño razonable para que GitHub los muestre."""
    partes, actual, tam = [], [], 0
    for e in entradas:
        s = "\n".join(e)
        if actual and tam + len(s) > LIMITE_ARCHIVO:
            partes.append(actual)
            actual, tam = [], 0
        actual.append(s)
        tam += len(s) + 1
    if actual:
        partes.append(actual)
    nombres = [f"{base}.md" if i == 0 else f"{base}-{i + 1}.md" for i in range(len(partes))]
    archivos = {}
    for i, ps in enumerate(partes):
        cab = [f"# {titulo}" + (f" (parte {i + 1} de {len(partes)})" if len(partes) > 1 else ""), ""] + intro
        if len(partes) > 1:
            cab += ["Partes: " + " · ".join(f"**{j + 1}**" if j == i else f"[{j + 1}]({nombres[j]})" for j in range(len(nombres))), ""]
        archivos[nombres[i]] = "\n".join(cab + ps).rstrip() + "\n"
    return archivos, nombres


def n_clases(items):
    return len({i["cid"] for i in items})


def escribir_terminos(terminos, esencial):
    por_letra = collections.defaultdict(list)
    for k, items in terminos.items():
        por_letra[letra(items[0]["term"])].append(k)
    letras = sorted(por_letra, key=lambda x: ("~" if x == "0-9" else x))
    archivos, indice = {}, []
    for L in letras:
        nav = " · ".join(f"**{x}**" if x == L else f"[{x}](terminos-{x.lower()}.md)" for x in letras)
        intro = ["[⬅️ Índice del glosario](README.md) · [siglas](siglas.md) · [símbolos](simbolos-y-unidades.md)", "", nav, ""]
        entradas = []
        for k in sorted(por_letra[L]):
            items = terminos[k]
            e = [f"### {nombre_visible(items)}", ""] + lineas_definicion(items) + bloque_contexto(items)
            if k in esencial:
                f, h, a = esencial[k]
                e += ["", f"📖 **Explicado a fondo:** [{h}](esencial/{f}#{a}) (intuición, fórmula, ejemplo numérico y errores frecuentes)."]
            n = n_clases(items)
            e += ["", f"📘 **Dónde se aprende** ({n} {'clase' if n == 1 else 'clases'}): {enlaces(items)}.", ""]
            entradas.append(e)
        arch, nombres = paginar(f"terminos-{L.lower()}", f"Términos · {L}", intro, entradas)
        archivos.update(arch)
        indice.append((L, nombres[0], len(por_letra[L])))
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
    intro = ["[⬅️ Índice del glosario](README.md)", "",
             "Siglas y acrónimos que las clases definen en su vocabulario, en orden alfabético. "
             "Si una sigla no aparece, ninguna clase la presentó en su vocabulario.", ""]
    entradas = []
    for sig in sorted(filas, key=clave):
        items = filas[sig]
        nombres = sorted({i["term"] for i in items if not es_sigla(i["term"])})
        out = [f"### {sig}", ""]
        if nombres:
            out.append(f"- **Significa:** {'; '.join(nombres)}.")
        out += lineas_definicion(items) + bloque_contexto(items)
        out += ["", f"📘 **Dónde se aprende:** {enlaces(items)}.", ""]
        entradas.append(out)
    return paginar("siglas", "Siglas y acrónimos", intro, entradas)[0], len(filas)


def escribir_mas_usados(terminos, esencial, minimo=6):
    candidatos = sorted(((n_clases(items), k) for k, items in terminos.items()), key=lambda x: (-x[0], x[1]))
    candidatos = [(n, k) for n, k in candidatos if n >= minimo][:300]
    entradas = []
    for n, k in sorted(candidatos, key=lambda x: clave(terminos[x[1]][0]["term"])):
        items = terminos[k]
        e = [f"### {nombre_visible(items)}", "", f"*Aparece en {n} clases.*", ""] + lineas_definicion(items) + bloque_contexto(items)
        if k in esencial:
            f, h, a = esencial[k]
            e += ["", f"📖 **Explicado a fondo:** [{h}](esencial/{f}#{a})."]
        e += ["", f"📘 **Dónde se aprende:** {enlaces(items)}.", ""]
        entradas.append(e)
    intro = ["[⬅️ Índice del glosario](README.md)", "",
             f"Los {len(entradas)} términos que más clases comparten (desde {minimo} clases), en orden alfabético. "
             "Son el vocabulario transversal del programa: conviene dominarlos primero.", ""]
    return paginar("mas-usados", "Los términos más usados del programa", intro, entradas)[0], len(entradas)


def escribir_por_area(terminos):
    bloques, areas = cargar_areas()
    por_bloque = collections.defaultdict(dict)
    for k, items in terminos.items():
        for i in sorted(items, key=lambda x: orden_cid(x["cid"])):
            b = i["cid"].split("-")[0]
            por_bloque[b].setdefault(k, (nombre_visible(items), i))
    archivos = {}
    resumen = []
    for area in sorted(areas):
        out = [f"# Términos del área {area} · {areas[area]}", "", "[⬅️ Índice del glosario](README.md)", "",
               "Los términos que presentan las clases de cada bloque del área, en orden alfabético. "
               "Cada término enlaza a la clase donde aparece en el vocabulario.", ""]
        total = 0
        for b in sorted((x for x, v in bloques.items() if v[0] == area), key=lambda x: int(x[1:])):
            datos = por_bloque.get(b, {})
            if not datos:
                continue
            total += len(datos)
            out += [f"## {b} · {bloques[b][1]}", "", f"{len(datos)} términos.", ""]
            fila = []
            for k in sorted(datos):
                nombre, it = datos[k]
                fila.append(f"[{nombre}]({it['ruta']})")
            out += [" · ".join(fila), ""]
        archivos[f"por-area-{area}.md"] = "\n".join(out).rstrip() + "\n"
        resumen.append((area, areas[area], total))
    return archivos, resumen


def grupo_simbolo(s: str):
    k = clave(s)
    if k and "a" <= k[0] <= "z":
        return 0
    if k and any("Ͱ" <= c <= "Ͽ" for c in k):
        return 1
    return 2


def escribir_simbolos(simbolos):
    intro = ["[⬅️ Índice del glosario](README.md)", "",
           "Cada símbolo que las clases usan en su tabla de magnitudes, en orden alfabético: primero las letras latinas, "
           "después las griegas y al final los signos y operadores. Un mismo símbolo puede significar cosas distintas en "
           "clases distintas: se listan las variantes y cada una enlaza a la clase donde se usa. "
           "Los valores son los de cada clase.", ""]
    entradas = []
    for s in sorted(simbolos, key=lambda x: (grupo_simbolo(x), clave(x), x)):
        items = simbolos[s]
        out = [f"### `{s}`", ""]
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
        entradas.append(out)
    return paginar("simbolos-y-unidades", "Símbolos, magnitudes y unidades", intro, entradas)[0]


def main():
    terminos, simbolos, n_clases = cargar()
    esencial = cargar_esencial()
    archivos, indice = escribir_terminos(terminos, esencial)
    por_area, resumen_areas = escribir_por_area(terminos)
    archivos.update(por_area)
    mas_usados, n_mas = escribir_mas_usados(terminos, esencial)
    archivos.update(mas_usados)
    siglas, n_siglas = escribir_siglas(terminos)
    archivos.update(siglas)
    archivos.update(escribir_simbolos(simbolos))

    def fmt(n):
        return f"{n:,}".replace(",", ".")

    idx = ["# Glosario del programa", "",
           "> 📖 **¿Quieres entender, no solo reconocer?** Empieza por el [**glosario esencial**](esencial/README.md): "
           "conceptos clave explicados a fondo, con intuición, fórmula con unidades, ejemplo numérico y errores frecuentes. "
           "Este glosario completo es el índice extendido: cada término trae la oración de la clase que lo define, cómo lo explica la clase, su error frecuente y por qué importa.", "",
           "Glosario en **orden alfabético** de los términos, siglas, magnitudes y símbolos que usan las clases del programa. "
           "Se construye con la sección «Vocabulario» y la tabla «Magnitudes, símbolos y unidades» de cada clase: "
           "no agrega hechos nuevos, y cada entrada enlaza a las clases donde se aprende, con su modelo mental, ejemplo y ejercicios. "
           "Las definiciones heredan el estado de las clases (todas en E0, pendientes de revisión disciplinar).", "",
           f"Contiene **{fmt(len(terminos))}** términos distintos, **{fmt(n_siglas)}** siglas y **{fmt(len(simbolos))}** símbolos, "
           f"tomados de {fmt(n_clases)} clases.", "",
           "## Cómo usarlo", "",
           "1. Busca el término por su letra inicial.",
           "2. Lee la definición, la explicación (💡), el error frecuente (⚠️) y por qué importa (🎯); abre la clase enlazada para ver el ejemplo y los ejercicios.",
           "3. Si ves un símbolo en una fórmula, búscalo en [símbolos y unidades](simbolos-y-unidades.md); si ves una sigla, en [siglas](siglas.md).",
           "4. Si una entrada dice que la clase no define el término aparte, la explicación (💡) sale de su modelo mental, su explicación paso a paso o su ejemplo trabajado.",
           "5. Las listas largas están repartidas en partes para que se vean completas en GitHub.", "",
           "## Términos por letra", ""]
    for L, nombre, n in indice:
        idx.append(f"- [{L}]({nombre}) — {fmt(n)} términos")
    idx += ["", "## Vocabulario transversal", "",
            f"- [Los {n_mas} términos más usados](mas-usados.md): los que comparten más clases; conviene dominarlos primero.", "",
            "## Términos por área del programa", "",
            "Útil para estudiar un tema: cada área reúne el vocabulario de sus bloques.", ""]
    for area, titulo, n in resumen_areas:
        idx.append(f"- [{area} · {titulo}](por-area-{area}.md) — {fmt(n)} términos")
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
