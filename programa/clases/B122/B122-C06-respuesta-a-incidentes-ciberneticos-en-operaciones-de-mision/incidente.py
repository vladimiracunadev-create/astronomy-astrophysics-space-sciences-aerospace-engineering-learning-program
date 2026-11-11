#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C06: cronologia de un incidente cibernetico SIMULADO y costo de la demora de deteccion y contencion.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria ni de seguridad; no describe tecnicas de intrusion.
Datos SINTETICOS (inventados). Marco conceptual (solo ficha y resumen consultados el 2026-11-11): NIST SP 800-61 Rev. 3 (2025, respuesta a
incidentes alineada con CSF 2.0). El ciclo usado (preparar, detectar, contener, erradicar, recuperar, aprender) es ilustrativo.
Modelo: el numero de cuentas/sistemas afectados crece como N(t) = N0 exp(r t) desde el inicio hasta la contencion; tiempo de deteccion D ~ Exp(media m),
tiempo de contencion tras la deteccion C fijo. Analitico: E[N] = N0 exp(r C) / (1 - r m) si r m < 1.
Unidades: horas, conteos de sistemas. Sistema de referencia: t = 0 es el inicio del incidente (desconocido para el equipo hasta la deteccion).
Tolerancias: Monte Carlo (400000, semilla 122) vs analitico < 1 % (solo si 2 r m < 1: varianza finita; por eso m <= 8 h).
"""
from __future__ import annotations
import math, platform, random

N0, R = 1.0, 0.05      # sistemas iniciales; tasa de propagacion 1/h (ilustrativa)
M_DET = 6.0            # h, media de detectar (ilustrativa)
C_CONT = 2.0           # h, de la deteccion a la contencion
FASES = [("Detectar y analizar", 6.0), ("Contener", 2.0), ("Erradicar", 10.0), ("Recuperar", 14.0)]  # h, un caso sintetico


def esperado_analitico(m, c):
    assert R * m < 1
    return N0 * math.exp(R * c) / (1 - R * m)


def esperado_mc(m, c, n, seed):
    rng = random.Random(seed)
    s = 0.0
    for _ in range(n):
        d = rng.expovariate(1 / m)
        s += N0 * math.exp(R * (d + c))
    return s / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: tasas, tiempos y fases son inventados; no hay ningun incidente real.")
    t = 0.0
    print("Cronologia de un caso sintetico (horas desde el inicio del incidente):")
    for nom, d in FASES:
        print(f"  {t:5.1f} h -> {t + d:5.1f} h : {nom}")
        t += d
    print(f"Duracion total = {t} h ; tiempo hasta la contencion = {FASES[0][1] + FASES[1][1]} h")
    print("Sistemas afectados esperados al contener, segun la media de deteccion m:")
    for m in (1.0, 3.0, 6.0, 8.0):
        a = esperado_analitico(m, C_CONT)
        b = esperado_mc(m, C_CONT, 400000, 122)
        assert abs(a - b) / a < 0.01, (m, a, b)
        print(f"  m = {m:4.1f} h : analitico = {a:6.3f} ; Monte Carlo = {b:6.3f} ; dif = {abs(a - b) / a * 100:.2f} %")
    print("Efecto de acortar la contencion C con m = 6 h:")
    for c in (0.5, 2.0, 6.0):
        print(f"  C = {c:3.1f} h : E[N] = {esperado_analitico(6.0, c):.3f}")
    print(f"Umbral de inestabilidad: m = 1/r = {1 / R:.1f} h (con m >= 1/r el valor esperado diverge en el modelo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
