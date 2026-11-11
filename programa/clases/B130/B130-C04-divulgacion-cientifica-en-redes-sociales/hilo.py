#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B130-C04: verificador de un hilo de divulgacion y cascada sintetica de compartidos.

CONSULTADO (2026-11-11, solo resumenes obtenidos por buscador; textos completos NO consultados):
  - Vosoughi, Roy y Aral (2018), Science: sobre ~126 000 historias verificadas en Twitter (2006-2017), las falsas llegaron mas lejos y
    mas rapido que las verdaderas; los bots las difundian al mismo ritmo que las verdaderas. NO se prueba ni se reproduce aqui.
  - Lewandowsky et al. (2012), Psychological Science in the Public Interest: las correcciones pueden fallar y hay recomendaciones para
    disenarlas. El orden "hecho antes que mito" que usa el verificador es un CRITERIO DE ESTA CLASE, no una cita de esa fuente.
SINTETICOS / ILUSTRATIVOS: el hilo de ejemplo, el limite de 280 caracteres (parametro, NO consultado como norma vigente de ninguna
plataforma) y la cascada: proceso de ramificacion de Galton-Watson con descendencia de Poisson(R), 10 generaciones, semilla 130.
Tolerancia: media simulada frente a la teorica (1 - R^11)/(1 - R) con error relativo < 5 % en 20 000 cascadas.
"""
from __future__ import annotations
import math
import platform
import random
import re

LIMITE = 280

HILO_TEXTO = ("Un mito comun: las estaciones se deben a que la Tierra esta mas cerca del Sol en verano. "
              "Hecho: las estaciones se deben a la inclinacion del eje de la Tierra, de 23,44 grados respecto de su orbita. "
              "La distancia al Sol solo varia entre 147,095 y 152,100 millones de km. "
              "Cuando un hemisferio se inclina hacia el Sol recibe la luz mas directa y los dias son mas largos. "
              "Esto ocurre en hemisferios opuestos en meses opuestos. "
              "Fuente: ficha de la Tierra de NASA/NSSDC, https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (consultada 2026-11-11).")


def dividir_hilo(texto, limite):
    frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+", texto) if f.strip()]
    posts, actual = [], ""
    reserva = 8  # espacio para " (k/n)"
    for f in frases:
        if len(f) > limite - reserva:
            raise ValueError("frase demasiado larga")
        if len(actual) + len(f) + 1 <= limite - reserva:
            actual = (actual + " " + f).strip()
        else:
            posts.append(actual)
            actual = f
    if actual:
        posts.append(actual)
    n = len(posts)
    return [f"{p} ({i}/{n})" for i, p in enumerate(posts, 1)]


def verificar(posts, limite, alt_text_imagenes):
    problemas = []
    if any(len(p) > limite for p in posts):
        problemas.append("publicacion sobre el limite")
    if not any(re.search(r"https?://", p) for p in posts):
        problemas.append("sin enlace a la fuente")
    if not any("consultada" in p.lower() for p in posts):
        problemas.append("sin fecha de consulta")
    for img, alt in alt_text_imagenes.items():
        if not alt.strip():
            problemas.append(f"imagen {img} sin texto alternativo")
    texto = " ".join(posts).lower()
    if "mito" in texto and "hecho" in texto and texto.index("hecho") > texto.index("mito") and texto.index("hecho") - texto.index("mito") > 200:
        problemas.append("el hecho llega muy tarde")
    return problemas


def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def cascada(rng, r, generaciones=10, tope=100000):
    total, actual = 1, 1
    for _ in range(generaciones):
        siguiente = sum(poisson(rng, r) for _ in range(actual))
        total += siguiente
        actual = siguiente
        if actual == 0 or total >= tope:
            break
    return total


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    posts = dividir_hilo(HILO_TEXTO, LIMITE)
    print(f"Hilo ILUSTRATIVO dividido en {len(posts)} publicaciones (limite parametrico {LIMITE} caracteres):")
    for p in posts:
        print(f"  [{len(p):3d}] {p[:60]}...")
    pr = verificar(posts, LIMITE, {"img1": "Esquema del eje inclinado de la Tierra con dos posiciones de la orbita"})
    print("Problemas del hilo completo:", pr or "ninguno")
    assert not pr
    malo = verificar(posts[:1], LIMITE, {"img1": ""})
    print("Problemas de un hilo cortado y una imagen sin texto alternativo:", malo)
    assert "sin enlace a la fuente" in malo and "imagen img1 sin texto alternativo" in malo

    print("Cascada SINTETICA (Galton-Watson, descendencia Poisson(R), 10 generaciones, 20000 cascadas, semilla 130):")
    rng = random.Random(130)
    for r in (0.8, 1.0, 1.2):
        t = sorted(cascada(rng, r) for _ in range(20000))
        media = sum(t) / len(t)
        teor = (1 - r ** 11) / (1 - r) if r != 1.0 else 11.0
        p50, p90 = t[len(t) // 2], t[int(0.9 * len(t))]
        g100 = sum(1 for x in t if x >= 100) / len(t)
        print(f"  R = {r:.1f}: media = {media:7.2f} (teorica {teor:6.2f}), mediana = {p50:3d}, p90 = {p90:4d}, P(alcance >= 100) = {g100:.4f}")
        assert abs(media - teor) / teor < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
