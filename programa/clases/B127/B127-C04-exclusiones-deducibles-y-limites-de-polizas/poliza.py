#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C04: pago esperado de cuatro polizas SINTETICAS con deducible, limite, exclusion y coaseguro.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de seguros; no interpreta ninguna poliza real.
Consultado (2026-11-11), via resumen de WebFetch del eCFR: 14 CFR 440.13: la poliza paga desde el primer dolar salvo que el
deducible este respaldado en garantia (escrow) o en fondos libres; las exclusiones deben especificarse; 440.19(c): exclusiones
usuales no disponibles comercialmente a tarifas razonables. Solo se usan como concepto.
ILUSTRATIVOS: severidad lognormal, deducible, limite, probabilidad de exclusion, coaseguro.
Modelo: pago(L) = c * min(max(L - D, 0), Lim) con probabilidad 1 - pexc; 0 si el evento es excluido.
Formula cerrada: E[min(L, u)] = exp(mu+s^2/2) Phi((ln u - mu - s^2)/s) + u (1 - Phi((ln u - mu)/s)); pago medio = c (1-pexc) (LEV(D+Lim) - LEV(D)).
Unidades: MUSD ficticios. Tolerancias: Monte Carlo (400000 eventos, semilla 127) frente a la formula: error relativo < 1.5 %.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

MU, S = 1.5, 1.2
N = NormalDist()
POLIZAS = [  # nombre, deducible, limite, prob. exclusion, coaseguro
    ("A sin deducible", 0.0, 200.0, 0.00, 1.0),
    ("B deducible 5", 5.0, 200.0, 0.00, 1.0),
    ("C deducible 5 y limite 50", 5.0, 50.0, 0.00, 1.0),
    ("D como C, 10% excluido, 80% coas.", 5.0, 50.0, 0.10, 0.80),
]


def lev(u):
    """E[min(L, u)] para L lognormal."""
    if u <= 0:
        return 0.0
    z = (math.log(u) - MU) / S
    return math.exp(MU + S * S / 2) * N.cdf(z - S) + u * (1 - N.cdf(z))


def pago_medio(D, lim, pexc, c):
    return c * (1 - pexc) * (lev(D + lim) - lev(D))


def pago(L, D, lim, c):
    return c * min(max(L - D, 0.0), lim)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Severidad SINTETICA; 14 CFR 440.13 (via resumen) se usa solo como concepto.")
    media = math.exp(MU + S * S / 2)
    print(f"L ~ Lognormal(mu={MU}, s={S}) MUSD ; media = {media:.3f}")
    rng = random.Random(127)
    n = 400000
    Ls = [rng.lognormvariate(MU, S) for _ in range(n)]
    excl = [rng.random() for _ in range(n)]
    print(" poliza                              pago cerrado  pago MC   err rel   %perdida pagada")
    peor = 0.0
    for nom, D, lim, pe, c in POLIZAS:
        cer = pago_medio(D, lim, pe, c)
        mc = sum(pago(L, D, lim, c) for L, e in zip(Ls, excl) if e >= pe) / n
        err = abs(mc - cer) / cer if cer else 0.0
        peor = max(peor, err)
        print(f" {nom:34s} {cer:11.4f} {mc:9.4f} {err:8.2%} {cer / media:12.1%}")
    # efecto del deducible sobre la frecuencia de reclamo
    for D in (0.0, 5.0, 20.0):
        p_rec = 1 - N.cdf((math.log(D) - MU) / S) if D > 0 else 1.0
        print(f"P(L > D={D:4.1f}) = {p_rec:.4f}")
    print(f"Perdida retenida por el asegurado en B = {media - pago_medio(5.0, 200.0, 0.0, 1.0):.4f} MUSD por evento")
    assert peor < 0.015
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
