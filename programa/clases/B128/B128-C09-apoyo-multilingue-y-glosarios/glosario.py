#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C09: coherencia y cobertura de un glosario trilingue (es-en-pt) SINTETICO.

Consultado (2026-11-11): UNESCO, «Inclusion in education»: la lengua figura entre las barreras que dejan a personas fuera del aprendizaje y hay que
identificarlas y quitarlas. NO se consultaron los glosarios multilingues de la IAU: las traducciones de abajo las PROPONE el curso como ejemplo,
no son terminologia normativa y deben validarse con una fuente y con hablantes antes de usarse.
SINTETICO: el glosario de 6 terminos y el texto de ejemplo (en espanol) son inventados.
Unidades: conteos. Comprobaciones: (1) identificadores unicos; (2) ningun termino repetido dentro de un idioma (biyeccion);
(3) cobertura: terminos del texto con entrada; (4) coherencia: variantes no autorizadas del mismo concepto en el texto.
Segunda via: la cobertura se calcula por busqueda de subcadena y por recuento de tokens; deben coincidir. Tolerancia: igualdad exacta.
"""
from __future__ import annotations
import platform, re

GLOSARIO = {  # id: (es, en, pt, definicion breve en espanol)
    "agujero-negro": ("agujero negro", "black hole", "buraco negro", "Region de la que ni la luz puede escapar."),
    "curva-de-luz": ("curva de luz", "light curve", "curva de luz", "Grafico del brillo de un astro en el tiempo."),
    "paralaje": ("paralaje", "parallax", "paralaxe", "Desplazamiento aparente de un astro al cambiar el punto de vista."),
    "transito": ("transito", "transit", "transito", "Paso de un cuerpo por delante de una estrella."),
    "magnitud": ("magnitud", "magnitude", "magnitude", "Escala logaritmica del brillo aparente."),
    "ocular": ("ocular", "eyepiece", "ocular", "Lente por la que mira el observador."),
}
VARIANTES_NO_AUTORIZADAS = {"agujero-negro": ["hoyo negro"], "curva-de-luz": ["grafica de brillo"], "ocular": ["lente de ojo"]}
TEXTO = ("Un agujero negro no emite luz. Para estudiar un transito se mide la curva de luz con un telescopio. "
         "El hoyo negro de la figura es solo un dibujo. La paralaje permite medir distancias; la magnitud mide el brillo. "
         "La tabla muestra la curva de luz y la grafica de brillo. Cada estudiante usa un ocular distinto y la nebulosa del pie.")


def revisar(g):
    hall = []
    for i, idx in enumerate((0, 1, 2)):
        vals = [v[idx] for v in g.values()]
        dup = {x for x in vals if vals.count(x) > 1}
        if dup: hall.append(f"terminos repetidos en idioma {('es','en','pt')[i]}: {sorted(dup)}")
    return hall


def cobertura_subcadena(texto, g):
    t = texto.lower()
    return {k for k, v in g.items() if v[0] in t}


def cobertura_tokens(texto, g):
    toks = re.findall(r"[\wáéíóúñ]+", texto.lower())
    s = " ".join(toks)
    out = set()
    for k, v in g.items():
        n = len(v[0].split())
        if any(" ".join(toks[i:i + n]) == v[0] for i in range(len(toks) - n + 1)): out.add(k)
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Glosario y texto SINTETICOS; traducciones PROPUESTAS por el curso (no normativas, no consultadas en la IAU).")
    assert len(GLOSARIO) == len(set(GLOSARIO))
    print(f"Terminos: {len(GLOSARIO)}; idiomas: es, en, pt")
    h = revisar(GLOSARIO)
    print("Hallazgos de biyeccion:", h if h else "ninguno")
    c1, c2 = cobertura_subcadena(TEXTO, GLOSARIO), cobertura_tokens(TEXTO, GLOSARIO)
    assert c1 == c2, (c1, c2)
    print(f"Terminos del glosario que aparecen en el texto: {len(c1)} de {len(GLOSARIO)} -> {sorted(c1)}")
    print("Variantes NO autorizadas detectadas en el texto:")
    n = 0
    for k, vs in VARIANTES_NO_AUTORIZADAS.items():
        for v in vs:
            if v in TEXTO.lower():
                n += 1
                print(f"  '{v}' -> usar '{GLOSARIO[k][0]}' (en: {GLOSARIO[k][1]}, pt: {GLOSARIO[k][2]})")
    assert n == 2  # "lente de ojo" no aparece en el texto
    # terminos candidatos que el texto usa y el glosario no tiene (SINTETICO)
    candidatos = ["nebulosa"]
    falta = [c for c in candidatos if c in TEXTO.lower() and not any(v[0] == c for v in GLOSARIO.values())]
    print("Terminos usados sin entrada en el glosario:", falta)
    assert falta == ["nebulosa"]
    sin_dif = [k for k, v in GLOSARIO.items() if v[0] == v[1]]
    print("Terminos identicos en es y en (cognados; no hace falta traducir):", sin_dif)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
