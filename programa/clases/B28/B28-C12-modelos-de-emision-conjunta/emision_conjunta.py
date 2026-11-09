#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C12: chorro estructurado y brillo observado segun el angulo de vision.

Datos: ninguna constante fisica. Contexto: GRB 170817A fue un destello corto ordinario pero detectado 1.7 s despues de la fusion
(arXiv:1710.05446, resumen). El factor de Lorentz (100), el semiancho del nucleo (0.1 rad), el perfil gaussiano y el exponente
Doppler (3) son ILUSTRATIVOS (sinteticos); no se ajusta a ninguna observacion.
Modelo: cada elemento del chorro, a un angulo theta_e del eje y con energia E(theta_e) = E0 exp(-theta_e^2/(2 theta_c^2)), se mueve
con factor de Lorentz Gamma; el observador esta a theta_v del eje. El angulo entre la velocidad del elemento y la visual es
cos(alpha) = cos(theta_v) cos(theta_e) + sen(theta_v) sen(theta_e) cos(phi); el factor Doppler delta = 1/(Gamma (1 - beta cos alpha)).
Energia observada relativa (isotropa equivalente por unidad de angulo solido) proporcional a la media sobre el chorro de
E(theta_e) delta^3, normalizada a la visual sobre el eje.
Comprobacion independiente: para beta -> 0 (delta = 1) la integral doble sobre la esfera de E(theta_e) coincide con la integral
unidimensional (1/2) Int E(theta) sen(theta) dtheta.
Supuestos: elementos que emiten con la misma eficiencia, un solo factor de Lorentz. Validez: ilustrativa.
Tolerancia: 1e-5 entre integral doble e integral unidimensional (error de punto medio ~ h^2/24).
"""
from __future__ import annotations
import math
import platform
import sys


def delta(gamma, beta, cos_a):
    return 1.0 / (gamma * (1 - beta * cos_a))


def media_doppler(theta_v, gamma, theta_c, exp_d=3, n_t=3000, n_p=360, beta=None):
    """(1/4pi) Int E(theta_e) delta^exp_d dOmega_e, por punto medio en theta_e en [0, pi/2] y phi en [0, 2 pi]."""
    if beta is None:
        beta = math.sqrt(1 - 1 / gamma ** 2)
    ht, hp = (math.pi / 2) / n_t, 2 * math.pi / n_p
    s = 0.0
    cv, sv = math.cos(theta_v), math.sin(theta_v)
    for i in range(n_t):
        te = (i + 0.5) * ht
        e = math.exp(-te * te / (2 * theta_c ** 2))
        if e < 1e-300:
            continue
        ct, st = math.cos(te), math.sin(te)
        acum = 0.0
        for j in range(n_p):
            ph = (j + 0.5) * hp
            ca = cv * ct + sv * st * math.cos(ph)
            acum += delta(gamma, beta, ca) ** exp_d
        s += e * st * acum * hp * ht
    return s / (4 * math.pi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    theta_c = 0.1
    # comprobacion: delta = 1 (gamma casi 1)
    doble = media_doppler(0.3, 1.0, theta_c, exp_d=3, n_t=4000, n_p=4, beta=1e-9)
    n = 40000
    h = (math.pi / 2) / n
    uno = 0.0
    for i in range(n):
        t = (i + 0.5) * h
        uno += math.exp(-t * t / (2 * theta_c ** 2)) * math.sin(t) * h
    uno *= 2 * math.pi / (4 * math.pi)
    assert abs(doble / uno - 1) < 1e-5, "integral doble frente a unidimensional"
    print(f"beta -> 0: integral doble = {doble:.8f} ; integral unidimensional = {uno:.8f} (cociente {doble / uno:.8f})")
    gamma = 100.0
    ref = media_doppler(0.0, gamma, theta_c)
    print(f"Gamma = {gamma:.0f}, theta_c = {theta_c} rad, Doppler^3: referencia sobre el eje = {ref:.6e}")
    print(f"{'theta_v [rad]':>13} {'theta_v/theta_c':>16} {'brillo relativo':>16} {'-2.5 log10 [mag]':>17}")
    for tv in (0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8):
        r = media_doppler(tv, gamma, theta_c) / ref
        print(f"{tv:13.2f} {tv / theta_c:16.1f} {r:16.4e} {-2.5 * math.log10(r):17.2f}")
    # el brillo fuera del eje cae de forma monotona
    previo = 2.0
    for tv in (0.0, 0.1, 0.2, 0.4, 0.8):
        r = media_doppler(tv, gamma, theta_c) / ref
        assert r < previo, "monotonia"
        previo = r
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
