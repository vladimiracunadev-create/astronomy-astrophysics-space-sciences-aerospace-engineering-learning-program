#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C21: dispersion Compton inversa, regimen de Klein-Nishina y razon sincrotron/Compton.

Datos: c, e, m_e, r_e, sigma_T, sigma_SB, k_B, mu_0 (NIST CODATA 2022), consultados 2026-11-09. El campo de fotones
(cuerpo negro de 2.7 K), los factores de Lorentz y el campo magnetico de 1e-9 T son ILUSTRATIVOS (sinteticos); no se
cita ninguna medicion.
Modelo: electron con factor de Lorentz gamma que choca de frente con un foton de energia eps. Energia maxima
dispersada exacta (transformando al sistema de reposo y de vuelta):
eps' = gamma (1+beta) eps; E1' = eps'/(1 + 2 eps'/(m c^2)); E1 = gamma (1+beta) E1'; aproximacion
E1 ~ 4 gamma^2 eps/(1 + 4 gamma eps/(m c^2)). Seccion eficaz de Klein-Nishina integrada numericamente sobre el angulo
y comparada con la forma cerrada. Cociente de potencias Compton/sincrotron = U_rad/U_B (regimen de Thomson).
Supuestos: foton monoenergetico, colision de frente, electron libre. Validez: gamma >> 1.
Tolerancia: 1e-3 entre energia exacta y aproximada para gamma >= 100; 1e-8 entre la integral de Klein-Nishina y la
forma cerrada; 1e-5 entre sigma_KN(x -> 0) y sigma_T.
"""
from __future__ import annotations
import math
import platform
import sys

C, E, ME = 299792458.0, 1.602176634e-19, 9.1093837139e-31
KB, SIG_SB, MU0 = 1.380649e-23, 5.670374419e-8, 1.25663706127e-6
RE, SIG_T = 2.8179403205e-15, 6.6524587051e-29
MC2 = ME * C ** 2


def e1_exacta(gamma, eps):
    beta = math.sqrt(1 - 1 / gamma ** 2)
    ep = gamma * (1 + beta) * eps
    e1p = ep / (1 + 2 * ep / MC2)
    return gamma * (1 + beta) * e1p


def e1_aprox(gamma, eps):
    return 4 * gamma ** 2 * eps / (1 + 4 * gamma * eps / MC2)


def sigma_kn_cerrada(x):
    if x < 1e-4:
        return 8 * math.pi / 3 * RE ** 2 * (1 - 2 * x)
    l = math.log(1 + 2 * x)
    return 2 * math.pi * RE ** 2 * ((1 + x) / x ** 3 * (2 * x * (1 + x) / (1 + 2 * x) - l) + l / (2 * x) - (1 + 3 * x) / (1 + 2 * x) ** 2)


def sigma_kn_numerica(x, n=40000):
    def f(mu):
        r = 1 / (1 + x * (1 - mu))
        return 0.5 * RE ** 2 * r ** 2 * (r + 1 / r - (1 - mu ** 2))
    h = 2.0 / n
    s = f(-1) + f(1)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(-1 + i * h)
    return 2 * math.pi * s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    t = 2.7
    eps = 2.7 * KB * t
    print(f"foton tipico (2.7 kT, T = {t} K): eps = {eps / E:.4e} eV")
    print(f"{'gamma':>8} {'E1 exacta [eV]':>16} {'E1 aprox [eV]':>15} {'4 gamma eps/mc2':>16} {'E1/(4 gamma^2 eps)':>19}")
    for g in (1e2, 1e3, 1e5, 1e7, 1e9):
        ex, ap = e1_exacta(g, eps), e1_aprox(g, eps)
        if g >= 100:
            assert abs(ex / ap - 1) < 1e-3, "energia exacta frente a aproximada"
        print(f"{g:8.0e} {ex / E:16.4e} {ap / E:15.4e} {4 * g * eps / MC2:16.4e} {ex / (4 * g ** 2 * eps):19.6f}")
    print(f"{'x = eps/mc2':>12} {'sigma_KN numerica [m2]':>24} {'cerrada [m2]':>14} {'sigma_KN/sigma_T':>17}")
    for x in (1e-6, 1e-2, 1.0, 10.0, 100.0):
        sn, sc = sigma_kn_numerica(x), sigma_kn_cerrada(x)
        assert abs(sn / sc - 1) < 1e-8, f"Klein-Nishina x={x}"
        print(f"{x:12.0e} {sn:24.6e} {sc:14.6e} {sc / SIG_T:17.6f}")
    assert abs(sigma_kn_cerrada(1e-6) / SIG_T - 1) < 1e-5, "limite de Thomson"
    assert abs(8 * math.pi / 3 * RE ** 2 / SIG_T - 1) < 1e-9, "sigma_T = 8 pi r_e^2/3"
    u_rad = 4 * SIG_SB / C * t ** 4
    b = 1e-9
    u_b = b ** 2 / (2 * MU0)
    print(f"U_rad(2.7 K) = {u_rad:.4e} J/m3 ; U_B(1e-9 T) = {u_b:.4e} J/m3 ; P_IC/P_sincrotron = U_rad/U_B = {u_rad / u_b:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
