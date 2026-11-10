#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C06: densidad de columna de un hielo a partir de una banda infrarroja de absorcion SINTETICA.

Datos: SINTETICOS. Banda gaussiana en profundidad optica tau(nu) con centro 3280 cm-1, FWHM 390 cm-1 y tau_pico 0.80 (ilustrativos; se evoca una banda de
estiramiento O-H, pero no se uso ningun espectro ni valor de fuerza de banda publicado); fuerza de banda A = 2.0e-16 cm por molecula (ILUSTRATIVA);
ruido gaussiano de sigma_tau = 0.01 con semilla fija. Boogert et al. (2015) se consulto solo por su resumen (observaciones infrarrojas de hielos); no se uso ninguna cifra suya.
Modelo: N = integral(tau d nu) / A. Integral por la regla del trapecio en una malla uniforme de 1 cm-1. Un monocapa se toma como 1e15 moleculas cm-2 (ILUSTRATIVO).
Supuestos: banda aislada, continuo ya restado, sin dispersion; ley de Beer lineal. Validez: ilustrativa.
Tolerancia: integral numerica sin ruido vs analitica tau_pico * FWHM * sqrt(pi / (4 ln 2)) a 1e-6 relativo; dispersion de N con ruido vs formula de propagacion a 5 %.
"""
from __future__ import annotations
import math, platform, random

NU0, FWHM, TAU0 = 3280.0, 390.0, 0.80
A_BAND = 2.0e-16          # cm por molecula (ILUSTRATIVA)
SIG = 0.01
MONOCAPA = 1.0e15         # moleculas cm-2 (ILUSTRATIVA)

def tau(nu):
    s = FWHM / (2.0 * math.sqrt(2.0 * math.log(2.0)))
    return TAU0 * math.exp(-0.5 * ((nu - NU0) / s) ** 2)

def integral(ruido, rng):
    lo, hi = NU0 - 6 * FWHM, NU0 + 6 * FWHM
    n = int(hi - lo)
    s = 0.0
    for i in range(n + 1):
        nu = lo + i
        t = tau(nu) + (rng.gauss(0.0, SIG) if ruido else 0.0)
        w = 0.5 if i in (0, n) else 1.0
        s += w * t
    return s, n + 1

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ana = TAU0 * FWHM * math.sqrt(math.pi / (4.0 * math.log(2.0)))
    num, npts = integral(False, None)
    err = abs(num - ana) / ana
    print("A. Banda SINTETICA: centro 3280 cm-1, FWHM 390 cm-1, tau_pico 0.80, A = 2.0e-16 cm/molecula (ILUSTRATIVA)")
    print(f"B. Integral de tau d nu: numerica = {num:.6f} cm-1 ; analitica = {ana:.6f} cm-1 ; error relativo = {err:.2e}")
    assert err < 1e-6
    N0 = ana / A_BAND
    print(f"C. Densidad de columna sin ruido N = {N0:.4e} moleculas cm-2 = {N0 / MONOCAPA:.1f} monocapas")
    # Monte Carlo con ruido
    rng = random.Random(12345)
    Ns = []
    for _ in range(400):
        s, _n = integral(True, rng)
        Ns.append(s / A_BAND)
    media = sum(Ns) / len(Ns)
    sd = math.sqrt(sum((x - media) ** 2 for x in Ns) / (len(Ns) - 1))
    sd_teo = SIG * math.sqrt(npts) / A_BAND      # trapecio con paso 1 cm-1 (extremos con peso 1/2: efecto despreciable)
    print(f"D. Monte Carlo (400 realizaciones con ruido 0.01, semilla 12345): N medio = {media:.4e} ; desviacion = {sd:.4e} ; formula sigma sqrt(Npts)/A = {sd_teo:.4e}")
    assert abs(sd - sd_teo) / sd_teo < 0.05, (sd, sd_teo)
    assert abs(media - N0) / N0 < 0.01
    print("E. Efecto de la fuerza de banda A (la incertidumbre de A se traslada a N)")
    print("A [cm/molec]   N [cm-2]")
    for f in (0.8, 1.0, 1.2):
        print(f"{A_BAND * f:.2e}    {ana / (A_BAND * f):.4e}")
    # monocapas por grano
    area_por_H = 4.7309e-21        # cm2 por H de la poblacion ilustrativa de B55-C05
    x_hielo = 1.0e-4               # moleculas de hielo por H (ILUSTRATIVO)
    ml = x_hielo / (area_por_H * MONOCAPA)
    print(f"F. Con x(hielo) = 1e-4 por H y area de grano 4.7309e-21 cm2/H (B55-C05, ilustrativa): {ml:.1f} monocapas")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
