#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C10: auditoria de comentarios de retroalimentacion segun cuatro niveles (tarea, proceso, autorregulacion, persona).

CONTENIDO EDUCATIVO. CONSULTADO (2026-11-11, solo resumenes): Hattie y Timperley (2007) y Wisniewski, Zierer y Hattie (2020): el efecto de la
retroalimentacion depende de su tipo y de como se da; el metaanalisis de 2020 (435 estudios, 994 tamanos de efecto, d = 0.48) informa heterogeneidad
significativa. Los NIVELES (tarea, proceso, autorregulacion, persona) son los de la referencia de 2007 y se citan de memoria: su texto NO se consulto.
SINTETICO: 24 comentarios inventados sobre un informe de medicion; la etiqueta 'manual' la asigna el autor del curso y es ILUSTRATIVA. El
clasificador por palabras clave es una heuristica del curso. 'Especifico' = el comentario cita un numero, una seccion o una magnitud.
Tolerancias: la exactitud se calcula por dos vias (matriz de confusion y conteo directo) y deben coincidir exactamente.
"""
from __future__ import annotations
import platform, re

NIVELES = ["tarea", "proceso", "autorregulacion", "persona"]
# (texto, etiqueta manual)
ANTES = [
    ("Muy bien, buen trabajo.", "persona"), ("Eres muy inteligente.", "persona"), ("Tu informe es un desastre.", "persona"),
    ("Falta la unidad en la tabla 2.", "tarea"), ("El resultado de R esta mal.", "tarea"), ("Incompleto.", "tarea"),
    ("Sigue asi, vas muy bien.", "persona"), ("No pusiste la incertidumbre.", "tarea"), ("Excelente, eres genial.", "persona"),
    ("Revisa los calculos.", "tarea"), ("Podrias esforzarte mas.", "persona"), ("Bien.", "persona"),
]
DESPUES = [
    ("La tabla 2 omite la unidad de la sombra (cm): anadela y recalcula Delta theta.", "tarea"),
    ("Para propagar la incertidumbre usa sigma_theta = sigma_S H/(H^2 + S^2) en cada sitio, y luego combinala.", "proceso"),
    ("Antes de entregar, comprueba tu radio con la segunda via (Monte Carlo) y compara las dos desviaciones.", "autorregulacion"),
    ("Tu resultado de 6525 km tiene +2.3 % respecto del nominal: explica si esa diferencia es mayor que tu sigma.", "tarea"),
    ("Tu estrategia de promediar las dos sombras de Caude es correcta; aplica el mismo criterio a Granada.", "proceso"),
    ("Como planificaste las lecturas, que paso te ayudaria a detectar tu error de unidades antes de calcular?", "autorregulacion"),
    ("Buen trabajo: la seccion 3 explica por que Delta theta es pequeno; falta citar la fuente de los datos.", "tarea"),
    ("Registra en tu lista de control los tres pasos que olvidaste y revisala en el proximo informe.", "autorregulacion"),
    ("Compara tu metodo con el de la seccion 8.3 y decide si usarias la mediana en lugar de la media.", "proceso"),
    ("Eres muy bueno en esto.", "persona"), ("La figura 1 no tiene ejes rotulados: anade magnitud y unidad.", "tarea"),
    ("Elige que criterio de la rubrica quieres mejorar primero y fijate una meta para la proxima version.", "autorregulacion"),
]
CLAVES = {
    "persona": ["eres", "genial", "inteligente", "bien.", "muy bien", "sigue asi", "desastre", "esfuerz", "muy bueno"],
    "autorregulacion": ["comprueba tu", "antes de entregar", "planific", "tu lista", "proximo informe", "meta", "elige", "fijate", "como planificaste", "registra"],
    "proceso": ["estrategia", "metodo", "usa ", "compara", "propagar", "aplica"],
}


def clasificar(txt):
    t = txt.lower()
    for nivel in ("autorregulacion", "persona", "proceso"):
        if any(k in t for k in CLAVES[nivel]):
            return nivel
    return "tarea"


def especifico(txt):
    return bool(re.search(r"\d|tabla|seccion|figura|sigma|incertidumbre|unidad", txt.lower()))


def evalua(nombre, lista):
    n = len(lista)
    pred = [clasificar(t) for t, _ in lista]
    gold = [g for _, g in lista]
    conf = {(g, p): 0 for g in NIVELES for p in NIVELES}
    for g, p in zip(gold, pred):
        conf[(g, p)] += 1
    acc_matriz = sum(conf[(x, x)] for x in NIVELES) / n
    acc_directa = sum(1 for g, p in zip(gold, pred) if g == p) / n
    assert acc_matriz == acc_directa and sum(conf.values()) == n
    print(f"{nombre} ({n} comentarios): exactitud del clasificador {acc_directa:.3f}")
    print("  nivel (etiqueta manual)   n    % ; especificos")
    for niv in NIVELES:
        cnt = [t for t, g in lista if g == niv]
        esp = sum(1 for t in cnt if especifico(t))
        print(f"  {niv:16s}        {len(cnt):3d}  {100 * len(cnt) / n:5.1f} % ; {esp}")
    esp_total = sum(1 for t, _ in lista if especifico(t))
    print(f"  comentarios especificos en total: {esp_total} de {n} ({100 * esp_total / n:.0f} %)")
    fallos = [(t, g, p) for (t, g), p in zip(lista, pred) if g != p]
    for t, g, p in fallos:
        print(f"    desacuerdo: '{t}' manual={g} clasificador={p}")
    return acc_directa


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Comentarios SINTETICOS; etiquetas manuales y clasificador ILUSTRATIVOS; niveles de Hattie y Timperley 2007 de memoria (texto NO consultado).")
    a1 = evalua("Antes", ANTES)
    a2 = evalua("Despues", DESPUES)
    p_antes = sum(1 for _, g in ANTES if g == "persona") / len(ANTES)
    p_des = sum(1 for _, g in DESPUES if g == "persona") / len(DESPUES)
    print(f"Proporcion de comentarios dirigidos a la persona: antes {100 * p_antes:.0f} % ; despues {100 * p_des:.0f} %")
    print("Referencia consultada (resumen, Wisniewski et al. 2020): d = 0.48 con heterogeneidad significativa; no se aplica a este conjunto sintetico.")
    assert p_des < p_antes
    assert a1 > 0.6 and a2 > 0.6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
