#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B128-C05: calidad de subtitulos WebVTT y tasa de error de palabras (WER).

Consultado (2026-11-11): W3C WAI, "Captions/Subtitles": los subtitulos deben sincronizarse; la transcripcion automatica
sin revisar puede cambiar el sentido (ejemplo de un "no" omitido); WebVTT es el formato web mas comun.
Umbrales de LECTURA (<= 17 caracteres/s, <= 2 lineas, <= 37 caracteres por linea, duracion 1-7 s): del CURSO, ILUSTRATIVOS, NO consultados.
Datos SINTETICOS: un guion inventado de 5 subtitulos y una "transcripcion automatica" inventada con errores.
Unidades: segundos, caracteres, palabras. WER = (S + D + I) / N con distancia de Levenshtein por palabras.
Segunda via: WER por programacion dinamica frente a una busqueda recursiva con memoria. Tolerancia: igualdad exacta.
"""
from __future__ import annotations
import platform, re
from functools import lru_cache

VTT = """WEBVTT

1
00:00:01.000 --> 00:00:04.000
Hoy medimos el brillo de una estrella variable.

2
00:00:04.000 --> 00:00:05.200
Observen la curva de luz que aparece ahora en pantalla con todos sus detalles.

3
00:00:05.500 --> 00:00:08.500
[sonido de aplausos]

4
00:00:08.000 --> 00:00:12.000
El brillo no cambia durante el transito,
salvo por una caida pequena.

5
00:00:12.000 --> 00:00:20.500
Esto es todo.
"""
UMB = dict(cps=17.0, lineas=2, ancho=37, dmin=1.0, dmax=7.0)


def t(s: str) -> float:
    h, m, r = s.split(":"); return int(h) * 3600 + int(m) * 60 + float(r)


def parsear(vtt: str):
    out = []
    for bloque in vtt.strip().split("\n\n")[1:]:
        ls = bloque.split("\n")
        a, b = [t(x.strip()) for x in ls[1].split("-->")]
        out.append((a, b, ls[2:]))
    return out


def revisar(cues):
    hall = []
    prev_fin = 0.0
    for i, (a, b, lineas) in enumerate(cues, 1):
        txt = " ".join(lineas)
        dur = b - a
        cps = len(txt) / dur
        if cps > UMB["cps"]: hall.append(f"cue {i}: {cps:.1f} car/s > {UMB['cps']}")
        if len(lineas) > UMB["lineas"]: hall.append(f"cue {i}: {len(lineas)} lineas")
        if any(len(l) > UMB["ancho"] for l in lineas): hall.append(f"cue {i}: linea > {UMB['ancho']} car")
        if dur < UMB["dmin"] or dur > UMB["dmax"]: hall.append(f"cue {i}: duracion {dur:.1f} s fuera de [{UMB['dmin']},{UMB['dmax']}]")
        if a < prev_fin: hall.append(f"cue {i}: se solapa con el anterior ({prev_fin - a:.1f} s)")
        prev_fin = b
    return hall


def pal(s): return re.findall(r"\w+", s.lower())


def wer_dp(ref, hip):
    d = list(range(len(hip) + 1))
    for i in range(1, len(ref) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(hip) + 1):
            cur = min(d[j] + 1, d[j - 1] + 1, prev + (ref[i - 1] != hip[j - 1]))
            prev, d[j] = d[j], cur
    return d[len(hip)]


def wer_rec(ref, hip):
    @lru_cache(None)
    def f(i, j):
        if i == 0: return j
        if j == 0: return i
        return min(f(i - 1, j) + 1, f(i, j - 1) + 1, f(i - 1, j - 1) + (ref[i - 1] != hip[j - 1]))
    return f(len(ref), len(hip))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Guion y 'transcripcion automatica' SINTETICOS; umbrales de lectura ILUSTRATIVOS (no consultados).")
    cues = parsear(VTT)
    print(f"Cues: {len(cues)}")
    for i, (a, b, l) in enumerate(cues, 1):
        print(f"  {i}: {a:5.1f}-{b:5.1f} s  {len(' '.join(l))/(b-a):5.1f} car/s")
    hall = revisar(cues)
    print(f"Hallazgos de formato: {len(hall)}")
    for h in hall: print("  -", h)
    ref = pal("el brillo no cambia durante el transito salvo por una caida pequena")
    hip = pal("el brillo cambia durante el transito salvo por una caida pequena")  # omite "no"
    w1, w2 = wer_dp(ref, hip), wer_rec(tuple(ref), tuple(hip))
    assert w1 == w2 == 1
    print(f"Referencia: {len(ref)} palabras; hipotesis: {len(hip)}; errores = {w1}; WER = {w1/len(ref)*100:.1f} %")
    print("Un WER bajo no garantiza el sentido: la hipotesis OMITE 'no' y afirma lo contrario con un solo error.")
    hip2 = pal("el brillo no cambia durante el transito salvo por una caida pequena")
    assert wer_dp(ref, hip2) == 0
    assert len(hall) == 7, hall
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
