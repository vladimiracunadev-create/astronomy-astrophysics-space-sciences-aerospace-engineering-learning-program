#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C05: difusion de fotones y criterio de Schwarzschild.

Datos: c, G, sigma (NIST CODATA 2022, consultados 2026-11-09); GM_sol, R_sol, L_sol nominales
(IAU 2015 B3). Recorrido libre medio del fotón y las capas de la estrella son valores
SINTETICOS / ILUSTRATIVOS (no medidos): la opacidad real varía en varios órdenes de magnitud.
Modelo: (1) marcha aleatoria isótropa con paso fijo l: <r^2> = N l^2; tiempo de difusión
t = R^2/(l c). (2) Criterio de Schwarzschild: hay convección si grad_rad > grad_ad, con
grad_rad = 3 kappa L P /(16 pi a c G m T^4), a = 4 sigma/c, y grad_ad = (gamma-1)/gamma.
Supuestos: gas ideal monoatómico (gamma = 5/3); sin rotación ni campo; l y kappa uniformes en cada capa.
Validez: orden de magnitud. Tolerancia: 3 % en <r^2> de 20000 caminantes (semilla fija) y 1e-6 en grad_ad.
"""
from __future__ import annotations
import math
import platform
import random
import sys

C, G = 299792458.0, 6.67430e-11
SIGMA = 5.670374419e-8
A_RAD = 4 * SIGMA / C
GM_SOL, R_SOL, L_SOL = 1.3271244e20, 6.957e8, 3.828e26
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0


def t_difusion(R, l):
    return R * R / (l * C)


def caminata_r2(n_pasos, n_cam, semilla=24):
    rng = random.Random(semilla)
    s = 0.0
    for _ in range(n_cam):
        x = y = z = 0.0
        for _ in range(n_pasos):
            cz = 2 * rng.random() - 1
            ph = 2 * math.pi * rng.random()
            sn = math.sqrt(1 - cz * cz)
            x += sn * math.cos(ph)
            y += sn * math.sin(ph)
            z += cz
        s += x * x + y * y + z * z
    return s / n_cam


def grad_ad_numerico(gamma=5 / 3):
    """grad_ad = dlnT/dlnP a entropía constante, evaluado con diferencias finitas.
    Gas ideal: P = rho T, s = ln(T^(1/(gamma-1)) / rho) constante."""
    k = 1 / (gamma - 1)

    def p_de_t(T):
        rho = T ** k  # entropía constante
        return rho * T

    t0, h = 1.0, 1e-5
    return (math.log(t0 * (1 + h)) - math.log(t0 * (1 - h))) / (
        math.log(p_de_t(t0 * (1 + h))) - math.log(p_de_t(t0 * (1 - h))))


def grad_rad(kappa, L, P, m, T):
    return 3 * kappa * L * P / (16 * math.pi * A_RAD * C * G * m * T ** 4)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, ncam = 400, 20000
    r2 = caminata_r2(n, ncam)
    assert abs(r2 / n - 1) < 0.03, "marcha aleatoria: <r^2> != N l^2"
    gad = grad_ad_numerico()
    assert abs(gad - 0.4) < 1e-6, "grad_ad != 0.4"
    print(f"marcha aleatoria: <r^2>/(N l^2) = {r2 / n:.4f} (esperado 1)")
    print(f"grad_ad numerico = {gad:.6f} (gamma=5/3 -> 0.4)")
    for l in (0.1e-2, 1e-2):
        print(f"t_dif (Sol, l = {l * 100:.1f} cm) = {t_difusion(R_SOL, l) / YR:,.0f} anios")
    capas = [("capa interna (sintetica)", 0.1, 1.0e16, 0.3 * M_SOL, 1.0e7),
             ("capa externa (sintetica)", 20.0, 1.0e11, M_SOL, 1.0e6)]
    for nom, kap, P, m, T in capas:
        gr = grad_rad(kap, L_SOL, P, m, T)
        modo = "convectiva" if gr > gad else "radiativa"
        print(f"{nom}: grad_rad = {gr:.3f} -> {modo}")
    assert grad_rad(0.1, L_SOL, 1.0e16, 0.3 * M_SOL, 1.0e7) < 0.4
    assert grad_rad(20.0, L_SOL, 1.0e11, M_SOL, 1.0e6) > 0.4
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
