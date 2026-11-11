#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C03: presupuesto de tiempo, legibilidad y jerga de un guion oral.

CONSULTADO (2026-11-11, resumen obtenido por buscador; texto completo NO consultado): Barrio-Cantalejo et al. (2008), Anales del
Sistema Sanitario de Navarra 31(2): escala INFLESZ con tramos <40 muy dificil, 40-55 algo dificil, 55-65 normal, 65-80 bastante facil,
>80 muy facil, y el umbral 55 para textos de salud. La FORMULA de Szigriszt-Pazos (IFSZ = 206.835 - 62.3 S/P - P/F) es la que
el autor de la clase conoce; NO se consulto en una fuente concreta. Verifiquela antes de usarla como estandar.
ILUSTRATIVOS / SINTETICOS: los dos guiones, el glosario de jerga, las velocidades de habla (120 y 150 palabras/minuto,
parametros de ejemplo, NO consultados como norma) y el reparto de tiempo.
Limites: el contador de silabas es una heuristica (diptongos e hiatos basicos) y se prueba con 10 palabras; el INFLESZ se calibro para
textos de salud, no para exposiciones orales.
"""
from __future__ import annotations
import platform
import re

FUERTES = set("aeoáéóíú")
DEBILES = set("iuü")
VOCALES = FUERTES | DEBILES


def silabas_palabra(p):
    p = p.lower()
    n, prev = 0, ""
    for ch in p:
        if ch in VOCALES:
            if not prev or prev not in VOCALES or (prev in FUERTES and ch in FUERTES):
                n += 1
        prev = ch
    return max(n, 1)


def palabras(texto):
    return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", texto)


def frases(texto):
    return max(1, len([f for f in re.split(r"[.!?]+", texto) if f.strip()]))


def ifsz(texto):
    pal = palabras(texto)
    s = sum(silabas_palabra(p) for p in pal)
    p, f = len(pal), frases(texto)
    return 206.835 - 62.3 * (s / p) - (p / f), p, f, s


def etiqueta(v):
    if v < 40:
        return "muy dificil"
    if v < 55:
        return "algo dificil"
    if v < 65:
        return "normal"
    if v < 80:
        return "bastante facil"
    return "muy facil"


JERGA = {"paralaje", "astrometria", "fotometrica", "heliocentrico", "espectroscopico", "calibracion", "magnitud", "baricentro"}


def sin_tildes(s):
    return s.lower().translate(str.maketrans("áéíóúü", "aeiouu"))


def densidad_jerga(texto):
    pal = [sin_tildes(p) for p in palabras(texto)]
    return sum(1 for p in pal if p in JERGA) / len(pal)


GUION_A = ("La paralaje astrometrica permite una calibracion heliocentrica de la magnitud fotometrica, "
           "y la medicion espectroscopica del baricentro condiciona la interpretacion de cada resultado.")
GUION_B = ("Si miras tu dedo con un ojo y luego con el otro, parece moverse. "
           "Los astronomos usan ese mismo efecto para medir la distancia a una estrella. "
           "Se llama paralaje. Cuanto mas cerca esta la estrella, mas se mueve.")


def presupuesto(minutos, diapositivas, reserva_preguntas, ppm, palabras_guion):
    habla = minutos * (1 - reserva_preguntas)
    return {"habla_min": habla, "seg_por_diapositiva": habla * 60 / diapositivas,
            "palabras_max": habla * ppm, "cabe": palabras_guion <= habla * ppm}


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    casos = {"casa": 2, "aire": 2, "tiene": 2, "país": 2, "ciencia": 2, "poeta": 3, "paralaje": 4, "estrella": 3, "cuidado": 3, "telescopio": 4}
    for w, esperado in casos.items():
        assert silabas_palabra(w) == esperado, (w, silabas_palabra(w))
    print("Silabas: 10 casos de prueba superados.")
    for nombre, g in (("A (jerga, ILUSTRATIVO)", GUION_A), ("B (llano, ILUSTRATIVO)", GUION_B)):
        v, p, f, s = ifsz(g)
        print(f"Guion {nombre}: palabras = {p}, frases = {f}, silabas = {s}, IFSZ = {v:.1f} ({etiqueta(v)}), jerga = {densidad_jerga(g)*100:.1f} %")
    va, vb = ifsz(GUION_A)[0], ifsz(GUION_B)[0]
    assert vb > va and etiqueta(va) in ("muy dificil", "algo dificil") and densidad_jerga(GUION_A) > densidad_jerga(GUION_B)
    print("Presupuesto de una charla ILUSTRATIVA (10 min, 8 diapositivas, 20 % para preguntas):")
    for ppm in (120, 150):
        r = presupuesto(10, 8, 0.2, ppm, 1000)
        print(f"  {ppm} palabras/min: habla {r['habla_min']:.1f} min, {r['seg_por_diapositiva']:.0f} s por diapositiva, "
              f"maximo {r['palabras_max']:.0f} palabras, guion de 1000 palabras: {'cabe' if r['cabe'] else 'NO cabe'}")
    assert not presupuesto(10, 8, 0.2, 120, 1000)["cabe"] and presupuesto(10, 8, 0.2, 150, 1000)["cabe"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
