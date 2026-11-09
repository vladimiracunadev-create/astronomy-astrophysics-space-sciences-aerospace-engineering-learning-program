#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C20: modelo politropo n = 3 del Sol contrastado con valores de referencia.

Datos: G, k_B, m_u (NIST CODATA 2022, consultados 2026-11-09); GM_sol y R_sol nominales
(IAU 2015 B3). Valores de referencia (modelo solar de la NASA Sun Fact Sheet, actualizada
2024-05-09; son valores de MODELO, no medidos): densidad central 1.622e5 kg/m3, presion central
2.477e11 bar, temperatura central 1.571e7 K. mu = 0.6 (gas ionizado, composicion solar):
valor ESTIMADO.
Modelo: politropo n = 3 (modelo estandar de Eddington) con M y R fijos: rho = rho_c theta^3,
P = P_c theta^4, a = R / xi_1, rho_c = rho_medio xi_1^3 / (3 omega_3), P_c = 4 pi G a^2 rho_c^2 / 4,
T_c = P_c mu m_u /(rho_c k_B).
Supuestos: gas ideal, sin presion de radiacion explicita, sin convección distinta, estructura
unica. Validez: orden de magnitud (factor ~2) para el Sol; no es un modelo solar.
Tolerancias: 1e-6 del solver frente a n = 1 y n = 5; 1e-3 en la masa por integral; 5e-3 en el
equilibrio hidrostatico por diferencias finitas.
"""
from __future__ import annotations
import math
import platform
import sys

G, KB, M_U = 6.67430e-11, 1.380649e-23, 1.66053906892e-27
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
M_SOL = GM_SOL / G
REF = {"rho_c": 1.622e5, "P_c": 2.477e11 * 1e5, "T_c": 1.571e7}


def lane_emden(n, h=2e-4, xi_max=60.0, parcial=False):
    """Devuelve xi1, omega = -xi1^2 theta'(xi1) y perfil (xi, theta)."""
    xi = h
    th = 1 - xi * xi / 6 + n * xi ** 4 / 120
    dth = -xi / 3 + n * xi ** 3 / 30
    xs, ts = [0.0, xi], [1.0, th]

    def f(x, y, z):
        return z, -2 * z / x - (max(y, 0.0) ** n)

    while xi < xi_max:
        k1 = f(xi, th, dth)
        k2 = f(xi + h / 2, th + h / 2 * k1[0], dth + h / 2 * k1[1])
        k3 = f(xi + h / 2, th + h / 2 * k2[0], dth + h / 2 * k2[1])
        k4 = f(xi + h, th + h * k3[0], dth + h * k3[1])
        th_n = th + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        dth_n = dth + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if th_n <= 0:
            xi1 = xi + h * th / (th - th_n)
            d1 = dth + (dth_n - dth) * (xi1 - xi) / h
            xs.append(xi1)
            ts.append(0.0)
            return xi1, -xi1 ** 2 * d1, xs, ts
        xi, th, dth = xi + h, th_n, dth_n
        xs.append(xi)
        ts.append(th)
    if parcial:
        return None, None, xs, ts
    raise RuntimeError("sin superficie")


def modelo(M, R, mu=0.6, n=3):
    xi1, omega, xs, ts = lane_emden(n)
    rho_m = M / (4 / 3 * math.pi * R ** 3)
    rho_c = rho_m * xi1 ** 3 / (3 * omega)
    a = R / xi1
    p_c = 4 * math.pi * G * a * a * rho_c ** 2 / (n + 1)
    t_c = p_c * mu * M_U / (rho_c * KB)
    return xi1, omega, rho_c, p_c, t_c, a, xs, ts


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    x1 = lane_emden(1)[0]
    assert abs(x1 - math.pi) < 1e-6, "n=1: xi1 != pi"
    xi5 = 5.0
    # n = 5 analitico: theta = (1 + xi^2/3)^(-1/2)
    _, _, xs5, ts5 = lane_emden(5, xi_max=6.0, parcial=True)
    j = min(range(len(xs5)), key=lambda i: abs(xs5[i] - xi5))
    assert abs(ts5[j] - (1 + xs5[j] ** 2 / 3) ** -0.5) < 1e-7, "n=5 analitico"
    xi1, omega, rho_c, p_c, t_c, a, xs, ts = modelo(M_SOL, R_SOL)
    # masa por integracion: M = Int 4 pi r^2 rho dr
    m_int = 0.0
    for i in range(1, len(xs)):
        r0, r1 = a * xs[i - 1], a * xs[i]
        d0, d1 = rho_c * ts[i - 1] ** 3, rho_c * ts[i] ** 3
        m_int += 0.5 * (4 * math.pi * r0 * r0 * d0 + 4 * math.pi * r1 * r1 * d1) * (r1 - r0)
    assert abs(m_int / M_SOL - 1) < 1e-3, "masa por integral != M"
    # equilibrio hidrostatico: dP/dr = -G m rho / r^2 en un punto interior (diferencias finitas)
    k = len(xs) // 2
    r_k = a * xs[k]
    dp = (p_c * ts[k + 1] ** 4 - p_c * ts[k - 1] ** 4) / (a * (xs[k + 1] - xs[k - 1]))
    m_k = 0.0
    for i in range(1, k + 1):
        r0, r1 = a * xs[i - 1], a * xs[i]
        m_k += 0.5 * (4 * math.pi * r0 ** 2 * rho_c * ts[i - 1] ** 3 + 4 * math.pi * r1 ** 2 * rho_c * ts[i] ** 3) * (r1 - r0)
    rhs = -G * m_k * rho_c * ts[k] ** 3 / r_k ** 2
    assert abs(dp / rhs - 1) < 5e-3, "equilibrio hidrostatico"
    print(f"solver validado: n=1 xi1 = {x1:.6f} ; n=5 verificado en xi = {xs5[j]:.3f}")
    print(f"n=3: xi1 = {xi1:.5f} ; omega_3 = {omega:.5f} ; rho_c/rho_medio = {rho_c / (M_SOL / (4 / 3 * math.pi * R_SOL ** 3)):.2f}")
    print(f"masa por integral / M = {m_int / M_SOL:.5f} ; dP/dr / (-G m rho/r^2) a r = {r_k / R_SOL:.2f} R = {dp / rhs:.5f}")
    print(f"{'':16s}{'politropo':>12s}{'referencia':>12s}{'cociente':>10s}")
    for nom, v, ref in (("rho_c [kg/m3]", rho_c, REF["rho_c"]), ("P_c [Pa]", p_c, REF["P_c"]), ("T_c [K]", t_c, REF["T_c"])):
        print(f"{nom:16s}{v:12.4e}{ref:12.4e}{v / ref:10.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
