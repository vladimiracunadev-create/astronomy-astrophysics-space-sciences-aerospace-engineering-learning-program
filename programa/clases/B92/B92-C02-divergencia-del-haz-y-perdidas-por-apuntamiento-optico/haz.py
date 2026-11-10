#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C02: haz gaussiano, ganancia de transmision y perdida por apuntamiento.

Datos consultados (2026-11-10): c = 299792458 m/s (NIST, CODATA 2022); referencia de rejilla 1552.52 nm
(frecuencia 193.1 THz, CCSDS 141.0-B-1 sec. 3.2); divergencias de LCRD citadas solo como contexto: haz de
comunicaciones de unos 20 urad y balizas de mas de 200 urad (Israel et al., SPIE 2024, NTRS 20230018608).
ILUSTRATIVOS (sinteticos, no medidos): radio de cintura w0 = 4 cm, distancia 45 000 km, radio del receptor 0.1 m,
sigma de apuntamiento por eje 2 urad.
Modelo: semiangulo de divergencia 1/e^2 theta = lambda/(pi w0); radio del haz a distancia R: w = theta R;
ganancia en el eje G = 8/theta^2 (haz gaussiano, campo lejano); perdida por desapuntamiento delta:
L = exp(-2 delta^2/theta^2); error de apuntamiento 2D con sigma por eje (Rayleigh): <L> = 1/(1 + 4 sigma^2/theta^2).
Segunda via: Monte Carlo con semilla fija (random.Random(92), 200000 muestras) y fraccion exacta 1 - exp(-2 r^2/w^2).
Tolerancia: Monte Carlo frente a analitico 2e-3 absoluta.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
LAM = C / 193.1e12  # m, rejilla n = 0


def theta(lam, w0):
    return lam / (math.pi * w0)


def ganancia(th):
    return 8.0 / th ** 2


def perdida(delta, th):
    return math.exp(-2.0 * delta ** 2 / th ** 2)


def perdida_media(sigma, th):
    return 1.0 / (1.0 + 4.0 * sigma ** 2 / th ** 2)


def db(x):
    return 10.0 * math.log10(x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    w0 = 0.04
    th = theta(LAM, w0)
    print(f"lambda = {LAM * 1e9:.2f} nm ; w0 = {w0 * 100:.0f} cm (ILUSTRATIVO) ; theta = {th * 1e6:.3f} urad ; G = {db(ganancia(th)):.2f} dBi")
    r = 45000e3
    w = th * r
    print(f"A R = 45000 km (ILUSTRATIVO): radio del haz w = {w:.1f} m")
    rx = 0.1
    frac = 1.0 - math.exp(-2.0 * rx ** 2 / w ** 2)
    aprox = 2.0 * rx ** 2 / w ** 2
    print(f"Fraccion de potencia en un receptor de {rx} m de radio: exacta {frac:.4e} ; aproximada 2 r^2/w^2 {aprox:.4e}")
    print("Perdida por desapuntamiento fijo delta:")
    for d in (0.0, 2e-6, 4e-6, 6e-6, 8e-6):
        print(f"  delta = {d * 1e6:4.1f} urad  L = {perdida(d, th):.4f}  ({-db(perdida(d, th)):.2f} dB)")
    rng = random.Random(92)
    sigma = 2e-6
    n = 200000
    acc = 0.0
    for _ in range(n):
        dx, dy = rng.gauss(0.0, sigma), rng.gauss(0.0, sigma)
        acc += perdida(math.hypot(dx, dy), th)
    mc = acc / n
    an = perdida_media(sigma, th)
    print(f"Perdida media con sigma = {sigma * 1e6:.1f} urad por eje: analitica {an:.5f} ; Monte Carlo {mc:.5f} ; diferencia {abs(an - mc):.1e}")
    print(f"  -> {-db(an):.3f} dB de perdida media")
    sg = th * math.sqrt((10 ** 0.1 - 1.0) / 4.0)
    print(f"Sigma por eje que da 1 dB de perdida media: {sg * 1e6:.3f} urad = {sg / th:.4f} theta")
    print("Ganancia efectiva G <L> = 8/(theta^2 + 4 sigma^2) con sigma = 2 urad:")
    prev = 0.0
    for t in (5e-6, 10e-6, 20e-6, 40e-6):
        ge = ganancia(t) * perdida_media(sigma, t)
        print(f"  theta = {t * 1e6:5.1f} urad  G = {db(ganancia(t)):6.2f} dBi  G_efectiva = {db(ge):6.2f} dBi")
        assert abs(ge - 8.0 / (t ** 2 + 4.0 * sigma ** 2)) / ge < 1e-12
    print(f"Techo de la ganancia efectiva (theta -> 0): 2/sigma^2 = {db(2.0 / sigma ** 2):.2f} dBi")
    assert abs(an - mc) < 2e-3
    assert abs(frac - aprox) / frac < 1e-3
    assert abs(-db(perdida_media(sg, th)) - 1.0) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
