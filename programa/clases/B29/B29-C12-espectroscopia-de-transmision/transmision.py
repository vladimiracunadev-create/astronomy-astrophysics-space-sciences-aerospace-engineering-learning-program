#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C12: profundidad optica a lo largo de una cuerda, radio efectivo y recuperacion de una abundancia por espectroscopia de transmision.

Datos: R_J(ecuatorial) y R_sol (IAU 2015 B3), consultados 2026-11-09. Contexto: Seager y Deming resumen la deteccion de caracteristicas moleculares en
atmosferas de exoplanetas (arXiv:1005.4037, resumen, consultado 2026-11-09). El radio (1.4 R_J), la altura de escala (430 km), la densidad en la base (1e25 m^-3),
las secciones eficaces (continuo 1e-28 m^2, linea 1e-26 m^2), el ancho de la linea, el ruido (20 ppm por canal) y la abundancia verdadera (0.01) son ILUSTRATIVOS.
Modelo: atmosfera exponencial n(z) = n0 exp(-z/H); profundidad optica a lo largo de una cuerda de parametro de impacto r = R0 + z:
tau(z) = 2 sigma Int_0^inf n(sqrt(r^2 + s^2) - R0) ds (cuadratura numerica) frente a la aproximacion sigma n(z) sqrt(2 pi r H);
radio efectivo: tau = 1; analitico R_eff = R0 + H ln(sigma n0 sqrt(2 pi R0 H)). Espectro: profundidad (R_eff(lambda)/R_s)^2 con sigma(lambda) = sigma_c + x sigma_L g(lambda)
(g gaussiana). Recuperacion de x por chi^2 en una rejilla logaritmica con Monte Carlo (semilla fija).
Supuestos: atmosfera isoterma, sin nubes, linea unica. Validez: H << R.
Tolerancia: tau por cuadratura frente a aproximacion dentro del 2 %; radio efectivo numerico frente a analitico dentro de 0.05 H; log10 x recuperado sin sesgo (3 errores de la media).
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

R_J, R_SOL = 7.1492e7, 6.957e8
R0, H, N0 = 1.4 * R_J, 430e3, 1e25
SIG_C, SIG_L = 1e-28, 1e-26
RS = R_SOL
NCAN, CENTRO, ANCHO = 40, 20.0, 3.0


def tau_numerica(z, sigma):
    r = R0 + z
    # integral sobre la cuerda: s de 0 a s_max (3 alturas mas alla)
    smax = math.sqrt((r + 12 * H) ** 2 - r ** 2)
    n = 4000
    h = smax / n
    f = lambda s: math.exp(-(math.sqrt(r * r + s * s) - R0) / H)
    tot = f(0) + f(smax)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(i * h)
    return 2 * sigma * N0 * tot * h / 3


def tau_aprox(z, sigma):
    return sigma * N0 * math.exp(-z / H) * math.sqrt(2 * math.pi * (R0 + z) * H)


def z_efectiva(sigma):
    lo, hi = -10 * H, 20 * H
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if tau_aprox(mid, sigma) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sigma_lambda(canal, x):
    g = math.exp(-0.5 * ((canal - CENTRO) / ANCHO) ** 2)
    return SIG_C + x * SIG_L * g


def espectro(x):
    return [((R0 + z_efectiva(sigma_lambda(c, x))) / RS) ** 2 for c in range(NCAN)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # tau numerica frente a aproximada
    print(f"{'z [H]':>6} {'tau numerica':>13} {'tau aprox':>11} {'cociente':>9}")
    for zh in (-2.0, 0.0, 2.0, 4.0):
        tn, ta = tau_numerica(zh * H, SIG_C), tau_aprox(zh * H, SIG_C)
        print(f"{zh:6.1f} {tn:13.5e} {ta:11.5e} {tn / ta:9.5f}")
        assert abs(tn / ta - 1) < 0.02, "tau numerica frente a aproximada"
    # radio efectivo
    zc = z_efectiva(SIG_C)
    za = H * math.log(SIG_C * N0 * math.sqrt(2 * math.pi * R0 * H))
    print(f"radio efectivo del continuo: z = {zc / 1e3:.2f} km ({zc / H:.3f} H) ; analitico = {za / 1e3:.2f} km ({za / H:.3f} H)")
    assert abs(zc - za) < 0.05 * H, "radio efectivo"
    # amplitud de la linea
    zl = z_efectiva(SIG_C + SIG_L)
    print(f"con x = 1 en el centro de la linea: z = {zl / 1e3:.2f} km ; aumento de {(zl - zc) / H:.3f} H = H ln[(sigma_c + sigma_L)/sigma_c] = {math.log((SIG_C + SIG_L) / SIG_C):.3f} H")
    assert abs((zl - zc) / H - math.log((SIG_C + SIG_L) / SIG_C)) < 0.02
    print(f"{'x':>7} {'profundidad en el centro [ppm]':>31} {'aumento sobre el continuo [ppm]':>33}")
    base = espectro(0.0)
    for x in (1e-4, 1e-3, 1e-2, 1e-1, 1.0):
        e = espectro(x)
        print(f"{x:7.0e} {e[int(CENTRO)] * 1e6:31.1f} {(e[int(CENTRO)] - base[int(CENTRO)]) * 1e6:33.1f}")
    # recuperacion por chi^2
    sig = 20e-6
    rejilla = [10 ** (-4 + 4 * i / 80) for i in range(81)]
    modelos = [espectro(x) for x in rejilla]
    rng = random.Random(20261109)
    x_v = 0.01
    verd = espectro(x_v)
    est = []
    for _ in range(300):
        d = [v + rng.gauss(0, sig) for v in verd]
        chi = [sum(((a - b) / sig) ** 2 for a, b in zip(d, m)) for m in modelos]
        est.append(math.log10(rejilla[min(range(len(chi)), key=lambda i: chi[i])]))
    mm, ss = statistics.mean(est), statistics.pstdev(est)
    print(f"recuperacion de log10 x (verdadero {math.log10(x_v):.3f}) en 300 realizaciones con {sig * 1e6:.0f} ppm por canal: media = {mm:.4f} ; desviacion = {ss:.4f}")
    assert abs(mm - math.log10(x_v)) < 3 * ss / math.sqrt(300) + 0.03, "sesgo de la abundancia"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
