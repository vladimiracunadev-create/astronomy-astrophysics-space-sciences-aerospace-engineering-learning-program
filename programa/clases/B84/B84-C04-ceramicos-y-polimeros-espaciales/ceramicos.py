#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C04: estadistica de Weibull de una ceramica, efecto de tamano y parametro de choque termico.

DATOS SINTETICOS (generados aqui con semilla fija, NO medidos): 30 resistencias de probetas de una ceramica ilustrativa
con modulo de Weibull verdadero m = 10 y resistencia caracteristica sigma0 = 400 MPa (volumen de referencia V0 = 1 cm3).
Ceramica ILUSTRATIVA (alumina tipica, no consultada): E = 370 GPa, nu = 0,22, alpha = 8e-6 1/K, k = 30 W/(m K), sigma_f = 400 MPa.
Modelo: P_f = 1 - exp(-(V/V0) (sigma/sigma0)^m). Ajuste por rangos medianos (Bernard: P = (i-0,3)/(n+0,4)) y regresion de
ln(-ln(1-P)) frente a ln(sigma). Segunda via: maxima verosimilitud (Newton sobre m). Choque termico: Delta T critico = sigma_f (1-nu)/(E alpha).
Unidades SI. Tolerancia: mismo valor de P_f en dos volumenes por la ley de escala exacta < 1e-12; ajuste de m dentro del 50 % del valor verdadero (n = 30 da una incertidumbre de m del orden del 15-20 %).
"""
from __future__ import annotations
import math, platform, random

M_V, S0_V = 10.0, 400.0  # verdaderos (sinteticos)


def muestra(n, seed=84004):
    rng = random.Random(seed)
    xs = []
    for _ in range(n):
        u = rng.random()
        xs.append(S0_V * (-math.log(1 - u)) ** (1 / M_V))
    return sorted(xs)


def ajuste_rangos(xs):
    n = len(xs)
    X = [math.log(x) for x in xs]
    Y = [math.log(-math.log(1 - (i + 1 - 0.3) / (n + 0.4))) for i in range(n)]
    mx, my = sum(X) / n, sum(Y) / n
    m = sum((a - mx) * (b - my) for a, b in zip(X, Y)) / sum((a - mx) ** 2 for a in X)
    s0 = math.exp(mx - my / m)
    return m, s0


def ajuste_mv(xs):
    n = len(xs)
    L = [math.log(x) for x in xs]
    m = 5.0
    for _ in range(100):
        xm = [x ** m for x in xs]
        s1 = sum(xm)
        s2 = sum(a * l for a, l in zip(xm, L))
        s3 = sum(a * l * l for a, l in zip(xm, L))
        f = s2 / s1 - 1 / m - sum(L) / n
        df = (s3 * s1 - s2 * s2) / s1 ** 2 + 1 / m ** 2
        paso = f / df
        m -= paso
        if abs(paso) < 1e-12:
            break
    s0 = (sum(x ** m for x in xs) / n) ** (1 / m)
    return m, s0


def pf(sigma, v_rel, m, s0):
    return 1 - math.exp(-v_rel * (sigma / s0) ** m)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xs = muestra(30)
    print(f"30 resistencias SINTETICAS (semilla 84004): min = {xs[0]:.1f} MPa, mediana = {(xs[14] + xs[15]) / 2:.1f} MPa, max = {xs[-1]:.1f} MPa")
    m1, s1 = ajuste_rangos(xs)
    m2, s2 = ajuste_mv(xs)
    print(f"Verdadero (sintetico):        m = {M_V:.2f}   sigma0 = {S0_V:.1f} MPa")
    print(f"Rangos medianos + regresion:  m = {m1:.2f}   sigma0 = {s1:.1f} MPa")
    print(f"Maxima verosimilitud:         m = {m2:.2f}   sigma0 = {s2:.1f} MPa")
    print("Efecto de tamano con el ajuste de maxima verosimilitud (V0 = 1 cm3):")
    sig_ref = s2 * (math.log(2)) ** (1 / m2)
    print(f"  Resistencia mediana de la probeta de referencia = {sig_ref:.1f} MPa")
    for v in (1.0, 10.0, 100.0, 1000.0):
        # esfuerzo con P_f = 0,5 en volumen V: (V/V0)(s/s0)^m = ln 2
        s = s2 * (math.log(2) / v) ** (1 / m2)
        print(f"  V = {v:7.1f} cm3: resistencia mediana = {s:7.1f} MPa ({s / sig_ref:.3f} de la de referencia)")
    # ley de escala exacta: misma P_f con V1 sigma1^m = V2 sigma2^m
    v1, v2 = 1.0, 100.0
    sg1 = 300.0
    sg2 = sg1 * (v1 / v2) ** (1 / m2)
    dif = abs(pf(sg1, v1, m2, s2) - pf(sg2, v2, m2, s2))
    print(f"Misma P_f a 300 MPa en 1 cm3 y a {sg2:.1f} MPa en 100 cm3: diferencia = {dif:.1e}")
    # Resistencia de diseno con P_f = 1e-3 (ilustrativa)
    sd = s2 * (-math.log(1 - 1e-3) / 1.0) ** (1 / m2)
    print(f"Resistencia con P_f = 1e-3 en 1 cm3: {sd:.1f} MPa")
    E, nu, al, kc, sf = 370e9, 0.22, 8e-6, 30.0, 400e6
    dT = sf * (1 - nu) / (E * al)
    R2 = kc * dT
    print(f"Choque termico ILUSTRATIVO (alumina tipica): Delta T critico = {dT:.1f} K ; R' = k dT = {R2:.0f} W/m")
    assert dif < 1e-12
    assert abs(m2 - M_V) / M_V < 0.5 and abs(m1 - M_V) / M_V < 0.5
    assert abs(s2 - S0_V) / S0_V < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
