#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B108-C05: evaluacion de una linea de tiempo de EVA SINTETICA con duraciones inciertas (Monte Carlo con semilla).

CONSULTADO (2026-11-10): Watts et al. (NTRS 20120007410): el banco PLSS 1.0 simulo EVAs nominales de 7 horas con cargas metabolicas de hasta 700 W
(se usa 7 h solo como referencia de duracion de consumibles). No se consultaron lineas de tiempo ni margenes de ninguna EVA real.
ILUSTRATIVOS (sinteticos, no medidos): tareas, duraciones triangulares (min, moda, max) en minutos, potencias metabolicas, dos tripulantes,
limite de planificacion T_lim = 360 min (7 h menos 1 h de reserva), presupuesto metabolico E_max = 2.6 kWh por tripulante.
Modelo: red de precedencias; duracion de cada tarea ~ Triangular(a, m, b) independiente; EVA = egreso + max(cadena A, cadena B) + tarea conjunta + retorno + ingreso.
Segunda via: media y varianza analiticas de la suma de triangulares (E = (a+m+b)/3; V = (a2+m2+b2-am-ab-mb)/18) frente a Monte Carlo de la cadena A;
convergencia de P(exceder) entre dos semillas dentro de 4 desviaciones binomiales. Tolerancias: media 0.5 min; P entre semillas 4 sigma.
Energia por tripulante = suma W_i * t_i. Unidades: min, W, kWh. Semillas 20261110 y 7.
"""
from __future__ import annotations
import math, platform, random

# (nombre, (a, m, b) min, W)
COMUN_ANTES = [("egreso", (25, 30, 40), 300.0)]
CADENA_A = [("traslado A", (30, 40, 60), 450.0), ("tarea A1", (60, 90, 150), 469.0), ("tarea A2", (30, 45, 90), 469.0)]
CADENA_B = [("traslado B", (30, 40, 60), 450.0), ("tarea B1", (45, 70, 120), 469.0)]
COMUN_DESPUES = [("tarea conjunta", (20, 30, 60), 469.0), ("retorno", (30, 40, 60), 450.0), ("ingreso", (25, 30, 45), 300.0)]
T_LIM, E_MAX = 360.0, 2.6


def tri(rng, a, m, b):
    return rng.triangular(a, b, m)


def media(t):
    return sum(t) / 3.0


def var(t):
    a, m, b = t
    return (a * a + m * m + b * b - a * m - a * b - m * b) / 18.0


def simula(n, semilla):
    rng = random.Random(semilla)
    mk, ea, eb = [], [], []
    for _ in range(n):
        d = {nm: tri(rng, *tt) for nm, tt, _ in COMUN_ANTES + CADENA_A + CADENA_B + COMUN_DESPUES}
        ca = sum(d[nm] for nm, _, _ in CADENA_A)
        cb = sum(d[nm] for nm, _, _ in CADENA_B)
        ant = sum(d[nm] for nm, _, _ in COMUN_ANTES)
        des = sum(d[nm] for nm, _, _ in COMUN_DESPUES)
        mk.append(ant + max(ca, cb) + des)
        w = {nm: p for nm, _, p in COMUN_ANTES + CADENA_A + CADENA_B + COMUN_DESPUES}
        e_a = sum(d[nm] * w[nm] for nm in d if nm not in {x[0] for x in CADENA_B}) * 60.0 / 3.6e6
        e_b = sum(d[nm] * w[nm] for nm in d if nm not in {x[0] for x in CADENA_A}) * 60.0 / 3.6e6
        ea.append(e_a); eb.append(e_b)
    return mk, ea, eb


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Linea de tiempo SINTETICA de EVA con dos tripulantes; duraciones triangulares (min, moda, max)")
    modo = lambda ch: sum(t[1] for _, t, _ in ch)
    ca, cb = modo(CADENA_A), modo(CADENA_B)
    det = modo(COMUN_ANTES) + max(ca, cb) + modo(COMUN_DESPUES)
    print(f"Ruta critica con duraciones modales: cadena A = {ca} min, cadena B = {cb} min -> critica = A; EVA = {det:.0f} min ({det/60:.2f} h); limite = {T_LIM:.0f} min")
    print(f"Holgura de la cadena B = {ca - cb} min")
    # segunda via analitica para la cadena A
    mA = sum(media(t) for _, t, _ in CADENA_A)
    vA = sum(var(t) for _, t, _ in CADENA_A)
    rng = random.Random(1)
    n = 200000
    s = [sum(tri(rng, *t) for _, t, _ in CADENA_A) for _ in range(n)]
    mm = sum(s) / n
    vv = sum((x - mm) ** 2 for x in s) / (n - 1)
    print(f"Cadena A: media analitica = {mA:.3f} min, Monte Carlo = {mm:.3f} min; desv. analitica = {math.sqrt(vA):.3f}, MC = {math.sqrt(vv):.3f}")
    N = 100000
    mk, ea, eb = simula(N, 20261110)
    mk2, _, _ = simula(N, 7)
    mean = sum(mk) / N
    srt = sorted(mk)
    p = sum(1 for x in mk if x > T_LIM) / N
    p2 = sum(1 for x in mk2 if x > T_LIM) / N
    print(f"Monte Carlo (N = {N}, semilla 20261110): EVA media = {mean:.1f} min; P50 = {srt[N//2]:.1f}; P90 = {srt[int(0.9*N)]:.1f}; P95 = {srt[int(0.95*N)]:.1f}")
    print(f"P(EVA > {T_LIM:.0f} min) = {p:.4f}; con semilla 7 = {p2:.4f}")
    pea = sum(1 for x in ea if x > E_MAX) / N
    peb = sum(1 for x in eb if x > E_MAX) / N
    print(f"Energia metabolica media: tripulante A = {sum(ea)/N:.3f} kWh, B = {sum(eb)/N:.3f} kWh; P(E > {E_MAX} kWh): A = {pea:.4f}, B = {peb:.4f}")
    margen = T_LIM - srt[int(0.9 * N)]
    print(f"Margen de tiempo frente al P90 = {margen:.1f} min")
    sig = 4 * math.sqrt(p * (1 - p) / N * 2) if 0 < p < 1 else 1e-3
    assert abs(mm - mA) < 0.5 and abs(math.sqrt(vv) - math.sqrt(vA)) < 0.5 and abs(p - p2) < sig + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
