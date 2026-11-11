#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C10: dotacion minima para sostener funciones esenciales de una institucion SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni de gestion. Datos SINTETICOS (inventados). Marco conceptual (solo ficha y resumen consultados
el 2026-11-11): NIST SP 800-34 Rev. 1 (2010), planificacion de contingencias; la norma ISO 22301 NO se consulto.
Modelo: una funcion esencial requiere al menos k personas disponibles de un equipo de n; cada persona esta disponible con probabilidad p
independiente (supuesto); P(cumplir) = sum_{j>=k} C(n,j) p^j (1-p)^(n-j). Unidades: personas, probabilidades. Sistema de referencia: un turno.
Tolerancias: Monte Carlo (200000, semilla 122) vs binomial exacta < 0.003; la plantilla minima se busca con P >= objetivo.
"""
from __future__ import annotations
import math, platform, random

P_DISP = 0.85         # prob. de que una persona este disponible en una emergencia (ilustrativa)
OBJETIVO = 0.99
FUNCIONES = {"Control de la mision": 3, "Seguridad de las comunicaciones": 2, "Comunicacion de crisis": 1, "Soporte de TI": 2}  # k minimo


def p_cumple(n, k, p=P_DISP):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def plantilla_minima(k, objetivo=OBJETIVO, p=P_DISP):
    n = k
    while p_cumple(n, k, p) < objetivo:
        n += 1
    return n


def mc(n, k, trials, seed, p=P_DISP):
    rng = random.Random(seed)
    ok = 0
    for _ in range(trials):
        if sum(rng.random() < p for _ in range(n)) >= k:
            ok += 1
    return ok / trials


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"DATOS SINTETICOS: p de disponibilidad = {P_DISP} (ilustrativa); objetivo = {OBJETIVO}.")
    assert abs(sum(math.comb(5, j) * 0.3 ** j * 0.7 ** (5 - j) for j in range(6)) - 1) < 1e-12
    total = 0
    print(" funcion                          k  n_min  P(n_min)  P(k personas exactas)  MC(n_min)")
    for f, k in FUNCIONES.items():
        n = plantilla_minima(k)
        pe, pm = p_cumple(n, k), p_cumple(k, k)
        m = mc(n, k, 200000, 122)
        assert abs(pe - m) < 0.003
        total += n
        print(f" {f:32s} {k}  {n:4d}   {pe:.5f}   {pm:.5f}              {m:.5f}")
    print(f"Plantilla total (equipos disjuntos) = {total} personas para {sum(FUNCIONES.values())} puestos minimos")
    print("Efecto de la disponibilidad p en la plantilla de 'Control de la mision' (k=3):")
    for p in (0.95, 0.85, 0.70):
        print(f"  p = {p:.2f} : n_min = {plantilla_minima(3, p=p)}")
    # probabilidad conjunta de cumplir todas con los equipos minimos (independientes)
    conj = 1.0
    for f, k in FUNCIONES.items():
        conj *= p_cumple(plantilla_minima(k), k)
    print(f"Probabilidad de cubrir TODAS las funciones a la vez = {conj:.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
