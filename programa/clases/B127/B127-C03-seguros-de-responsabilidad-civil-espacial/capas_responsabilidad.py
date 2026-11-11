#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B127-C03: perdida maxima probable (MPL) y capas de responsabilidad frente a terceros, SINTETICO.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de seguros ni describe un regimen aplicable a un caso real.
Consultado (2026-11-11), via resumen de WebFetch del eCFR: 14 CFR parte 440: MPL de terceros = perdida con probabilidad
de ocurrencia no menor que 1 en 10 millones (440.3); seguro exigido: monto fijado por la FAA, sin exceder el menor de
500 MUSD o el maximo disponible en el mercado a costo razonable (440.9(c)); el Gobierno de EE. UU. puede pagar reclamaciones
cubiertas que superen el seguro, hasta 1500 MUSD (ajustados por inflacion desde 1989), con condiciones (440.19).
Consultado (2026-11-11): Convenio de Responsabilidad 1972, Art. II (absoluta en la superficie y aeronaves en vuelo),
Art. III (por culpa en otros lugares), compilacion UNOOSA ST/SPACE/61/Rev.1.
ILUSTRATIVOS: la distribucion de la perdida de un evento de tercero (lognormal), la probabilidad de evento por lanzamiento.
Modelo: dado un evento con danos a terceros, L ~ Lognormal(mu, sigma). MPL = cuantil 1 - 1e-7 DEL EVENTO CONDICIONADO
(simplificacion didactica; el reglamento aplica la probabilidad a la perdida, no al evento condicionado).
Capas: seguro exigido = min(MPL, 500); excedente publico = min(max(L - seguro, 0), 1500); resto = no cubierto.
Unidades: MUSD ficticios. Tolerancias: cuantil de Monte Carlo al nivel 99.9 % frente al analitico: error relativo < 10 %.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

MU, SIGMA = 2.0, 1.6  # ln(MUSD)
TOPE_SEGURO, TOPE_PUBLICO = 500.0, 1500.0
N = NormalDist()


def cuantil(p):
    return math.exp(MU + SIGMA * N.inv_cdf(p))


def capas(L, seguro):
    s = min(L, seguro)
    pub = min(max(L - seguro, 0.0), TOPE_PUBLICO)
    resto = max(L - seguro - TOPE_PUBLICO, 0.0)
    return s, pub, resto


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Distribucion SINTETICA; consultados: 14 CFR 440 (via resumen) y Convenio de 1972 (Art. II-III).")
    print(f"L ~ Lognormal(mu={MU}, sigma={SIGMA}) MUSD ; mediana = {math.exp(MU):.2f} ; media = {math.exp(MU + SIGMA ** 2 / 2):.2f}")
    mpl = cuantil(1 - 1e-7)
    seguro = min(mpl, TOPE_SEGURO)
    print(f"MPL (cuantil 1-1e-7) = {mpl:.1f} MUSD ; seguro exigido = min(MPL, {TOPE_SEGURO:.0f}) = {seguro:.1f} MUSD")
    print("Cuantiles de L [MUSD]:")
    for p in (0.5, 0.9, 0.99, 0.999, 1 - 1e-4, 1 - 1e-6):
        print(f"  p = {p:.6f} -> {cuantil(p):10.2f}")
    # probabilidad de que L supere el seguro y el seguro + excedente
    ps = 1 - N.cdf((math.log(seguro) - MU) / SIGMA)
    pp = 1 - N.cdf((math.log(seguro + TOPE_PUBLICO) - MU) / SIGMA)
    print(f"P(L > seguro) = {ps:.3e} ; P(L > seguro + excedente publico) = {pp:.3e}")
    # Monte Carlo
    rng = random.Random(127)
    n = 400000
    xs = sorted(rng.lognormvariate(MU, SIGMA) for _ in range(n))
    q999_mc, q999 = xs[int(0.999 * n)], cuantil(0.999)
    err = abs(q999_mc - q999) / q999
    ms = mp = mr = 0.0
    for L in xs:
        a, b, c = capas(L, seguro)
        ms, mp, mr = ms + a, mp + b, mr + c
    print(f"Cuantil 99.9 %: analitico = {q999:.2f} ; Monte Carlo = {q999_mc:.2f} ; error relativo = {err:.2%}")
    print(f"Perdida media por evento: seguro = {ms / n:.3f} ; excedente publico = {mp / n:.3f} ; no cubierto = {mr / n:.5f} MUSD")
    print(f"Total = {(ms + mp + mr) / n:.3f} ; media analitica = {math.exp(MU + SIGMA ** 2 / 2):.3f}")
    print("Reparto de un evento de 800 MUSD: seguro %.1f ; publico %.1f ; no cubierto %.1f" % capas(800.0, seguro))
    assert err < 0.10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
