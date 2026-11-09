#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C16: presupuesto de energia de supernovas y escala de una burbuja de Sedov.

Datos: G (NIST, CODATA 2022, 2026-11-09); GM_sol (IAU 2015 B3). Funcion de masa inicial por tramos de C07
(ruptura en 0,5 Msol, Kroupa 2001, arXiv:astro-ph/0009005, resumen consultado 2026-11-09; pendientes
1,3 y 2,3 y limites 0,08-100 Msol ILUSTRATIVOS). Energia por supernova 1e51 erg, umbral de 8 Msol,
eficiencia de acoplamiento 0,1 y velocidad de escape ~ 3 sigma: valores CONVENCIONALES/ILUSTRATIVOS,
no consultados. Galaxia enana SINTETICA (de C10): sigma = 7 km/s, M_gas = 1e7 Msol.
Modelo: (a) numero de SN por Msol formada = int_8^100 xi dm / int m xi dm; (b) energia de ligadura del gas
E_b = (1/2) M_gas (3 sigma)^2 y numero de SN = E_b / (eps E_SN); (c) analisis dimensional: el radio de una
explosion en un medio de densidad rho es R = xi (E t^2/rho)^(1/5), con xi ~ 1,15 (valor clasico de Sedov,
NO consultado: la combinacion de exponentes SI se verifica aqui).
Supuestos: explosiones independientes, medio uniforme, sin enfriamiento radiativo.
Validez: ordenes de magnitud; la burbuja radiativa real es mas pequena. Tolerancias: 1e-8 (IMF) y 1e-12 (algebra).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
PC = 3.0856776e16
MYR = 3.15576e13
E_SN = 1e51 * 1e-7  # J
MP = 1.67262192595e-27


def imf(m, a1=1.3, a2=2.3, mb=0.5):
    c1 = mb ** (a1 - a2)
    return c1 * m ** -a1 if m < mb else m ** -a2


def integra(f, lo, hi, n=20000):
    a, b = math.log(lo), math.log(hi)
    h = (b - a) / n
    g = lambda u: f(math.exp(u)) * imf(math.exp(u)) * math.exp(u)
    s = g(a) + g(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(a + i * h)
    return s * h / 3


def exponentes_dimensionales():
    """Resuelve [E]^a [rho]^b [t]^c = L con E: M L^2 T^-2, rho: M L^-3, t: T (eliminacion de Gauss 3x3)."""
    # incognitas a, b, c ; ecuaciones: M: a + b = 0 ; L: 2a - 3b = 1 ; T: -2a + c = 0
    A = [[1.0, 1.0, 0.0], [2.0, -3.0, 0.0], [-2.0, 0.0, 1.0]]
    y = [0.0, 1.0, 0.0]
    n = 3
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[piv] = A[piv], A[i]
        y[i], y[piv] = y[piv], y[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for k in range(i, n):
                A[r][k] -= f * A[i][k]
            y[r] -= f * y[i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(A[i][k] * x[k] for k in range(i + 1, n))) / A[i][i]
    return x


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: la IMF por cuadratura coincide con la forma cerrada (numero de estrellas >= 8 Msol)
    a1, a2 = 1.3, 2.3
    c1 = 0.5 ** (a1 - a2)
    n_tot = c1 * (0.08 ** (1 - a1) - 0.5 ** (1 - a1)) / (a1 - 1) + (0.5 ** (1 - a2) - 100 ** (1 - a2)) / (a2 - 1)
    n_8 = (8 ** (1 - a2) - 100 ** (1 - a2)) / (a2 - 1)
    assert abs(integra(lambda m: 1.0, 0.08, 100.0) / n_tot - 1) < 1e-8
    assert abs(integra(lambda m: 1.0, 8.0, 100.0) / n_8 - 1) < 1e-8
    m_tot = integra(lambda m: m, 0.08, 100.0)
    sn_por_msol = integra(lambda m: 1.0, 8.0, 100.0) / m_tot
    # Prueba 2: exponentes dimensionales (E t^2/rho)^(1/5)
    a, b, c = exponentes_dimensionales()
    assert abs(a - 0.2) < 1e-12 and abs(b + 0.2) < 1e-12 and abs(c - 0.4) < 1e-12
    # Prueba 3: escalado de R con E, rho y t
    R = lambda E, rho, t: 1.15 * (E * t ** 2 / rho) ** 0.2
    rho = 1.0 * MP * 1e6  # 1 cm^-3 de H
    t = 1.0 * MYR
    assert abs(R(32 * E_SN, rho, t) / R(E_SN, rho, t) - 2.0) < 1e-12
    assert abs(R(E_SN, rho, 32 * t) / R(E_SN, rho, t) - 4.0) < 1e-12
    e_sn_msol = sn_por_msol * E_SN
    sigma = 7e3
    m_gas = 1e7 * M_SOL
    e_lig = 0.5 * m_gas * (3 * sigma) ** 2
    n_sn = e_lig / (0.1 * E_SN)
    m_est = n_sn / sn_por_msol
    print(f"SN por Msol formada = {sn_por_msol:.4f} ; energia por Msol = {e_sn_msol:.3e} J/Msol")
    print(f"exponentes (E, rho, t) = ({a:.3f}, {b:.3f}, {c:.3f})")
    print(f"R_Sedov-Taylor (E = 1e51 erg, n = 1 cm^-3, t = 1 Myr) = {R(E_SN, rho, t) / PC:.0f} pc (sin enfriamiento)")
    print(f"enana sintetica: E_ligadura = {e_lig:.3e} J ; SN necesarias (eps = 0.1) = {n_sn:.0f} ; masa estelar = {m_est:.3e} Msol ({m_est / 1e7 * 100:.2f} % del gas)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
