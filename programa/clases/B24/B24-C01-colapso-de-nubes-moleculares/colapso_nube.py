#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C01: masa de Jeans y tiempo de caida libre de un nucleo molecular.

Datos: G = 6.67430e-11 m3 kg-1 s-2, k_B = 1.380649e-23 J/K, m_p = 1.67262192595e-27 kg
(NIST, CODATA 2022, consultados 2026-11-09); GM_sol = 1.3271244e20 m3/s2 (IAU 2015 B3).
Nube: T, n(H2) y masas por particula son valores TIPICOS ILUSTRATIVOS (estimados, sin
fuente consultada); no son una observacion de una nube concreta.
Modelo: gas isotermo e ideal, sin rotacion, campo magnetico ni turbulencia. Velocidad del
sonido c_s = sqrt(k T / (mu m_H)); longitud de Jeans lambda_J = sqrt(pi c_s^2 / (G rho));
masa de Jeans M_J = (4 pi/3) rho (lambda_J/2)^3; tiempo de caida libre t_ff = sqrt(3 pi/(32 G rho)).
Supuestos: esfera uniforme que cae desde el reposo, sin presion durante la caida; m_H ~ m_p.
Validez: orden de magnitud para nucleos fríos (T ~ 10 K). Tolerancia de las pruebas: 1e-9
(relativa) en la identidad algebraica y 1e-6 en la cuadratura.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
KB = 1.380649e-23
MH = 1.67262192595e-27
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
YR = 365.25 * 86400.0


def c_sonido(T, mu=2.33):
    return math.sqrt(KB * T / (mu * MH))


def rho_de_n(n_h2_cm3, mu_h2=2.8):
    return n_h2_cm3 * 1e6 * mu_h2 * MH


def lambda_jeans(T, rho, mu=2.33):
    return math.sqrt(math.pi * c_sonido(T, mu) ** 2 / (G * rho))


def masa_jeans(T, rho, mu=2.33):
    lam = lambda_jeans(T, rho, mu)
    return 4 * math.pi / 3 * rho * (lam / 2) ** 3


def masa_jeans_cerrada(T, rho, mu=2.33):
    return math.pi ** 2.5 * c_sonido(T, mu) ** 3 / (6 * G ** 1.5 * rho ** 0.5)


def t_caida(rho):
    return math.sqrt(3 * math.pi / (32 * G * rho))


def t_caida_cuadratura(r0, M, n=2000):
    """t = int_0^r0 dr / sqrt(2GM(1/r-1/r0)); con r = r0 sin^2(phi) el integrando es suave."""
    h = (math.pi / 2) / n
    f = lambda p: 2 * r0 ** 1.5 * math.sin(p) ** 2 / math.sqrt(2 * G * M)
    s = f(0) + f(math.pi / 2)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    T, n = 10.0, 1e4
    rho = rho_de_n(n)
    cs, lam = c_sonido(T), lambda_jeans(T, rho)
    mj = masa_jeans(T, rho)
    # Prueba 1: identidad algebraica independiente
    assert abs(mj / masa_jeans_cerrada(T, rho) - 1) < 1e-9, "M_J no coincide con la forma cerrada"
    # Prueba 2: cuadratura frente al tiempo de caida libre cerrado
    r0 = 0.1 * 3.0857e16  # 0.1 pc (valor ilustrativo)
    M = 4 * math.pi / 3 * rho * r0 ** 3
    t_num = t_caida_cuadratura(r0, M)
    rho_chk = M / (4 * math.pi / 3 * r0 ** 3)
    assert abs(t_num / t_caida(rho_chk) - 1) < 1e-6, "t_ff por cuadratura no coincide"
    # Prueba 3: escalas M_J ~ T^(3/2) n^(-1/2)
    m2 = masa_jeans(2 * T, rho)
    m3 = masa_jeans(T, 4 * rho)
    assert abs(m2 / mj - 2 ** 1.5) < 1e-9 and abs(m3 / mj - 0.5) < 1e-9
    print(f"T = {T:.0f} K, n(H2) = {n:.0e} cm^-3 -> rho = {rho:.3e} kg/m^3")
    print(f"c_s = {cs:.1f} m/s ; lambda_J = {lam / 3.0857e16:.3f} pc ; M_J = {mj / M_SOL:.2f} Msol")
    print(f"t_ff = {t_caida(rho) / YR / 1e6:.3f} Myr ; por cuadratura = {t_num / YR / 1e6:.3f} Myr")
    print(f"M_J(2T)/M_J(T) = {m2 / mj:.4f} (2^1.5 = {2 ** 1.5:.4f}) ; M_J(4 rho)/M_J = {m3 / mj:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
