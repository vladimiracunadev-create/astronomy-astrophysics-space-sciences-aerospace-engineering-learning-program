#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C06: migracion de tipo I de un planeta en un disco sintetico de ley de potencias.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol y (GM)_Tierra nominales de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): disco de B52-C02 (Sigma = 1e4 kg/m^2 (r/ua)^-1.5, T = 280 K (r/ua)^-0.5, mu = 2.3);
coeficiente de par C = -2 (adimensional, sin fuente: los coeficientes publicados dependen de los gradientes del disco y NO se consultaron).
Sistema de referencia: orbita circular coplanar, estrella de (GM)_sol; SI.
Modelo: Gamma = C q^2 Sigma a^4 Omega^2 / h^2 (q = m/M*, h = H/a); L = m sqrt(GM a); dL/dt = Gamma.
Con las leyes de potencia del disco, da/dt = -K a_ua^(-1/2) y a^(3/2) = a0^(3/2) - (3/2) K t (solucion analitica).
Via 2: integracion RK4 de a(t) y, por separado, de L(t); ambas contra la analitica. Tolerancias: 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
GM_T = 3.986004e14
MSOL, MT = GM / G, GM_T / G
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
MU, S1, P, T1 = 2.3, 1.0e4, 1.5, 280.0
COEF = -2.0


def sigma(a): return S1 * a ** (-P)
def cs(a): return math.sqrt(K_B * T1 * a ** -0.5 / (MU * M_P))
def omega(a): return math.sqrt(GM / (a * UA) ** 3)
def h(a): return cs(a) / omega(a) / (a * UA)


def par(a, m):
    q = m / MSOL
    return COEF * q ** 2 * sigma(a) * (a * UA) ** 4 * omega(a) ** 2 / h(a) ** 2


def dadt(a, m):
    """da/dt en ua/s con a en ua."""
    ra = a * UA
    return 2.0 * par(a, m) * math.sqrt(ra) / (m * math.sqrt(GM)) / UA


def constante_K(m):
    return -dadt(1.0, m)


def a_analitica(a0, t, m):
    k = constante_K(m)
    v = a0 ** 1.5 - 1.5 * k * t
    return v ** (2.0 / 3.0) if v > 0 else 0.0


def rk4(f, y, hh):
    k1 = f(y); k2 = f(y + 0.5 * hh * k1); k3 = f(y + 0.5 * hh * k2); k4 = f(y + hh * k3)
    return y + hh / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def a_rk4(a0, t, m, n=2000):
    y, hh = a0, t / n
    for _ in range(n):
        y = rk4(lambda a: dadt(a, m), y, hh)
    return y


def a_rk4_L(a0, t, m, n=2000):
    """Integra L = m sqrt(GM a) con dL/dt = Gamma(a(L))."""
    L = m * math.sqrt(GM * a0 * UA)
    hh = t / n
    f = lambda L_: par((L_ / m) ** 2 / GM / UA, m)
    for _ in range(n):
        L = rk4(f, L, hh)
    return (L / m) ** 2 / GM / UA


def calcular():
    filas = []
    for m_t in (0.1, 1.0, 10.0):
        m = m_t * MT
        k = constante_K(m)
        tau5 = 5.0 / (-dadt(5.0, m)) / ANIO
        t_tot = (2.0 / (3.0 * k)) * (5.0 ** 1.5 - 0.1 ** 1.5)
        filas.append((m_t, k * ANIO, tau5, t_tot / ANIO))
    m = 1.0 * MT
    k = constante_K(m)
    t = 0.5 * (2.0 / (3.0 * k)) * (5.0 ** 1.5 - 0.1 ** 1.5)  # la mitad del tiempo hasta 0.1 ua
    an = a_analitica(5.0, t, m)
    n1 = a_rk4(5.0, t, m)
    n2 = a_rk4_L(5.0, t, m)
    return dict(filas=filas, t=t, an=an, rk_a=n1, rk_L=n2, h5=h(5.0), sig5=sigma(5.0))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Disco sintetico de B52-C02; coeficiente de par C = {COEF} (ilustrativo); h(5 ua) = {r['h5']:.4f}")
    print(f"{'m [M_T]':>8} {'K [ua^1.5/anio]':>16} {'tau(5 ua) [anios]':>18} {'5 -> 0.1 ua [anios]':>20}")
    for m_t, k, tau, tt in r["filas"]:
        print(f"{m_t:8.1f} {k:16.4e} {tau:18.4e} {tt:20.4e}")
    print(f"Planeta de 1 M_T: a(5 ua, t = {r['t'] / ANIO:.4e} anios): analitico = {r['an']:.8f} ua ; RK4 en a = {r['rk_a']:.8f} ua ; RK4 en L = {r['rk_L']:.8f} ua")
    assert abs(r["rk_a"] / r["an"] - 1) < 1e-6
    assert abs(r["rk_L"] / r["an"] - 1) < 1e-6
    assert r["filas"][2][2] < r["filas"][1][2] < r["filas"][0][2]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
