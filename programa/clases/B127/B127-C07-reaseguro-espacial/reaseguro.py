#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C07: cuota parte frente a exceso de perdida sobre una cartera SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de seguros; no describe contratos de reaseguro reales.
Consultado (2026-11-11): Gallagher, Space insurance market update Q1 2026 (10-04-2026): el mercado espacial se describe por
capacidad (aportada por aseguradoras, Lloyd's y MGA) y su volatilidad; sirve de contexto. Las formas de reaseguro
(cuota parte, exceso de perdida) NO se consultaron en una fuente concreta: se verifican por simulacion.
ILUSTRATIVOS: frecuencia, severidad, cuota cedida, prioridad y limite del exceso de perdida, recargos.
Modelo: S = sum de X_i por anio (Poisson compuesto, X lognormal). Cuota parte: cede q de cada X.
Exceso de perdida por riesgo (per risk): paga min(max(X - P, 0), L) por siniestro. Neto de la cedente = bruto - recuperacion + prima de reaseguro.
Prima de reaseguro: cuota parte, q * prima_bruta * (1 - comision); XL, recuperacion esperada * (1 + recargo_re).
Unidades: MUSD ficticios. Tolerancias: Monte Carlo (20000 anios, semilla 127) frente a formulas de media: error relativo < 2.5 %.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

LAM, MU, S = 2.4, 2.5, 1.3  # siniestros/anio, severidad ln(MUSD)
N = NormalDist()
Q, COMISION = 0.30, 0.25
P, L = 40.0, 120.0  # exceso de perdida 120 xs 40
RECARGO_RE = 0.35
PRIMA_BRUTA = 80.0


def lev(u):
    if u <= 0:
        return 0.0
    z = (math.log(u) - MU) / S
    return math.exp(MU + S * S / 2) * N.cdf(z - S) + u * (1 - N.cdf(z))


def poisson(rng, lam):
    Lx, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= Lx:
            return k
        k += 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Cartera SINTETICA; el contexto de capacidad (Gallagher Q1 2026) es lo unico consultado.")
    ex = math.exp(MU + S * S / 2)
    bruto_medio = LAM * ex
    rec_xl_medio = LAM * (lev(P + L) - lev(P))
    rec_qs_medio = Q * bruto_medio
    prima_qs = Q * PRIMA_BRUTA * (1 - COMISION)
    prima_xl = rec_xl_medio * (1 + RECARGO_RE)
    print(f"Bruto medio anual = {bruto_medio:.3f} MUSD ; prima bruta = {PRIMA_BRUTA:.1f} ; loss ratio bruto medio = {bruto_medio / PRIMA_BRUTA:.0%}")
    print(f"Cuota parte {Q:.0%}: recuperacion media = {rec_qs_medio:.3f} ; prima cedida = {prima_qs:.3f}")
    print(f"XL {L:.0f} xs {P:.0f}: recuperacion media = {rec_xl_medio:.3f} ; prima = {prima_xl:.3f} ; tasa sobre limite por siniestro = {rec_xl_medio / LAM / L:.2%}")
    rng = random.Random(127)
    n = 20000
    brutos, netos_qs, netos_xl, recs = [], [], [], []
    for _ in range(n):
        k = poisson(rng, LAM)
        xs = [rng.lognormvariate(MU, S) for _ in range(k)]
        b = sum(xs)
        r_xl = sum(min(max(x - P, 0.0), L) for x in xs)
        brutos.append(b)
        recs.append(r_xl)
        netos_qs.append(b * (1 - Q) + prima_qs)
        netos_xl.append(b - r_xl + prima_xl)
    def stats(v):
        v2 = sorted(v)
        m = sum(v) / n
        sd = math.sqrt(sum((x - m) ** 2 for x in v) / (n - 1))
        return m, sd, v2[int(0.99 * n)]
    mb, sb, qb = stats(brutos)
    print(f"Monte Carlo: bruto medio = {mb:.3f} (error {abs(mb - bruto_medio) / bruto_medio:.2%}) ; recuperacion XL media = {sum(recs) / n:.3f} (error {abs(sum(recs) / n - rec_xl_medio) / rec_xl_medio:.2%})")
    print(" programa            costo neto medio  desv. est.  cuantil 99 %")
    for nom, v in (("sin reaseguro", [b + 0.0 for b in brutos]), ("cuota parte 30%", netos_qs), ("XL 120 xs 40", netos_xl)):
        m, sd, q99 = stats(v)
        print(f" {nom:18s} {m:15.3f} {sd:11.3f} {q99:12.3f}")
    assert abs(mb - bruto_medio) / bruto_medio < 0.025
    assert abs(sum(recs) / n - rec_xl_medio) / rec_xl_medio < 0.025
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
