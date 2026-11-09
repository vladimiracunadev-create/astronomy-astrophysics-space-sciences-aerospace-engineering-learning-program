#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C12: potencia, frecuencia critica y espectro de radiacion sincrotron.

Datos: c, e, m_e, mu_0, sigma_T (NIST CODATA 2022), consultados 2026-11-09. Campo magnetico 1e-9 T (10 microgauss) y
factores de Lorentz 1e3..1e7: valores ILUSTRATIVOS (sinteticos); no se cita ninguna medicion.
Modelo: un electron ultrarrelativista con angulo de paso 90 grados en un campo B irradia P = (4/3) sigma_T c gamma^2 beta^2 U_B,
U_B = B^2/(2 mu_0); frecuencia critica nu_c = 3 gamma^2 e B/(4 pi m_e). El espectro de un electron es
P(nu) proporcional a F(x) = x Int_x^inf K_{5/3}(y) dy, x = nu/nu_c, con Int_0^inf F dx = 8 pi/(9 sqrt 3). Una poblacion
N(gamma) ~ gamma^-p da una ley de potencias nu^-(p-1)/2.
Supuestos: campo uniforme, sin autoabsorcion, sin enfriamiento. Validez: gamma >> 1.
Tolerancia: 1e-4 relativa en Int F; 0.03 en la pendiente espectral.
"""
from __future__ import annotations
import math
import platform
import sys

C, E, ME = 299792458.0, 1.602176634e-19, 9.1093837139e-31
MU0, SIG_T = 1.25663706127e-6, 6.6524587051e-29


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def k53(x):
    """K_{5/3}(x) = Int_0^inf exp(-x cosh t) cosh(5t/3) dt."""
    tmax = math.acosh(1 + 700.0 / x)
    return simpson(lambda t: math.exp(-x * math.cosh(t)) * math.cosh(5 * t / 3), 0.0, tmax, 600)


def int_k53(x):
    """Int_x^inf K_{5/3}(y) dy = Int_0^inf exp(-x cosh t) cosh(5t/3)/cosh(t) dt."""
    tmax = math.acosh(1 + 700.0 / x)
    return simpson(lambda t: math.exp(-x * math.cosh(t)) * math.cosh(5 * t / 3) / math.cosh(t), 0.0, tmax, 600)


def F(x):
    return x * int_k53(x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) potencia y frecuencia critica
    B = 1e-9
    ub = B ** 2 / (2 * MU0)
    print(f"U_B(1e-9 T) = {ub:.4e} J/m3")
    print(f"{'gamma':>8} {'P [W]':>12} {'nu_c [Hz]':>12} {'t_enfr [anios]':>15}")
    for g in (1e3, 1e4, 1e5, 1e7):
        beta = math.sqrt(1 - 1 / g ** 2)
        p = 4 / 3 * SIG_T * C * g ** 2 * beta ** 2 * ub
        nu = 3 * g ** 2 * E * B / (4 * math.pi * ME)
        t = g * ME * C ** 2 / p / (365.25 * 86400)
        print(f"{g:8.0e} {p:12.4e} {nu:12.4e} {t:15.4e}")
    # 2) integral de F: 8 pi/(9 sqrt 3) = Int_0^inf K(y) y^2/2 dy
    ana = 8 * math.pi / (9 * math.sqrt(3))
    # Int F dx por Simpson en log x (x = e^s, dx = x ds) en [1e-6, 60]; la cola x<1e-6 aporta ~ x^{4/3}
    def fl(s):
        x = math.exp(s)
        return F(x) * x
    num = simpson(fl, math.log(1e-6), math.log(60.0), 600)
    num += 1.0 * 0   # cola inferior ~ 0.65 x^{4/3} * 3/4 en x<1e-6 (despreciable)
    print(f"Int_0^inf F(x) dx = {num:.6f} (analitico 8 pi/(9 sqrt 3) = {ana:.6f})")
    assert abs(num / ana - 1) < 1e-4, "integral del nucleo sincrotron"
    print(f"F(0.29) = {F(0.29):.4f} (maximo cercano a x = 0.29, F_max ~ 0.918)")
    # 3) poblacion de leyes de potencia: P(nu) ~ Int gamma^(1-p) F(nu/gamma^2) dln gamma
    tabla = [(math.log(10 ** (-8 + 0.05 * i)), F(10 ** (-8 + 0.05 * i))) for i in range(0, 201)]
    def Finterp(x):
        s = math.log(x)
        if s <= tabla[0][0]:
            return tabla[0][1] * (x / 10 ** -8) ** (1 / 3)
        if s >= tabla[-1][0]:
            return 0.0
        i = int((s - tabla[0][0]) / (0.05 * math.log(10)))
        i = min(i, len(tabla) - 2)
        s0, f0 = tabla[i]
        s1, f1 = tabla[i + 1]
        return math.exp(math.log(f0) + (s - s0) / (s1 - s0) * (math.log(f1) - math.log(f0)))
    for p in (2.0, 2.5, 3.0):
        def P(nu):
            f = lambda lg: math.exp((1 - p) * lg) * Finterp(nu / math.exp(2 * lg))
            return simpson(f, math.log(1e2), math.log(1e6), 800)
        n1, n2 = 1e6, 1e9
        pend = math.log(P(n2) / P(n1)) / math.log(n2 / n1)
        print(f"p = {p}: pendiente espectral = {pend:.4f} (esperada {-(p - 1) / 2:.4f})")
        assert abs(pend + (p - 1) / 2) < 0.03, "pendiente espectral"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
