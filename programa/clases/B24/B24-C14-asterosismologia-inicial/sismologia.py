#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C14: separacion grande Delta nu de un politropo n = 3 y su escala con la densidad media.

Datos: GM_sol, R_sol nominales (IAU 2015 B3, arXiv:1510.07674); G (NIST CODATA 2022).
Modelo: modelo politropo n = 3 (Lane-Emden) de una estrella de masa M y radio R; velocidad
del sonido c^2 = gamma P / rho = gamma (Pc/rho_c) theta con gamma = 5/3, a^2 = (n+1) Pc /
(4 pi G rho_c^2), r = a xi. Separacion grande (aproximacion de rayos): Delta nu = 1/(2 int_0^R dr/c).
Supuestos: gas adiabatico ideal en toda la estrella, sin atmosfera ni convection distinta;
el politropo NO reproduce la estructura solar real. Validez: escalas y orden de magnitud.
Tolerancia: 1e-6 del solver frente a la solucion analitica n = 1; 1e-9 en la escala homologa.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
M_SOL = GM_SOL / G


def lane_emden(n, h=1e-4, xi_max=50.0):
    """RK4 de theta'' + 2 theta'/xi + theta^n = 0; devuelve xi1, theta(xi), derivadas."""
    xi = h
    th = 1 - xi * xi / 6 + n * xi ** 4 / 120
    dth = -xi / 3 + n * xi ** 3 / 30
    xs, ths = [0.0, xi], [1.0, th]

    def f(x, y, z):
        return z, -2 * z / x - (max(y, 0.0) ** n)

    while th > 0 and xi < xi_max:
        k1 = f(xi, th, dth)
        k2 = f(xi + h / 2, th + h / 2 * k1[0], dth + h / 2 * k1[1])
        k3 = f(xi + h / 2, th + h / 2 * k2[0], dth + h / 2 * k2[1])
        k4 = f(xi + h, th + h * k3[0], dth + h * k3[1])
        th_n = th + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        dth_n = dth + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        if th_n <= 0:
            # interpolacion lineal de la raiz
            xi1 = xi + h * th / (th - th_n)
            return xi1, dth, xs, ths
        xi += h
        th, dth = th_n, dth_n
        xs.append(xi)
        ths.append(th)
    raise RuntimeError("no hay superficie")


def delta_nu_uHz(M, R, n=3, gamma=5 / 3):
    xi1, dth1, xs, ths = lane_emden(n)
    rho_m = M / (4 / 3 * math.pi * R ** 3)
    rho_c = rho_m * xi1 ** 3 / (3 * abs(dth1) * xi1 ** 2)
    a = R / xi1
    pc_rhoc = 4 * math.pi * G * rho_c * a * a / (n + 1)   # Pc / rho_c
    # integral de dxi / c, c = sqrt(gamma Pc/rho_c * theta); regla trapezoidal en xi con theta>0
    integ = 0.0
    for i in range(1, len(xs)):
        x0, x1 = xs[i - 1], xs[i]
        c0 = math.sqrt(gamma * pc_rhoc * max(ths[i - 1], 1e-30))
        c1 = math.sqrt(gamma * pc_rhoc * max(ths[i], 1e-30))
        integ += 0.5 * (1 / c0 + 1 / c1) * (x1 - x0)
    # ultimo tramo hasta xi1 (la integral de 1/sqrt(theta) converge: theta ~ (xi1 - xi))
    x_last, th_last = xs[-1], ths[-1]
    c_last = math.sqrt(gamma * pc_rhoc * th_last)
    integ += 2 * (xi1 - x_last) / c_last      # int dx/sqrt(k (xi1-x)) = 2 sqrt(dx)/sqrt(k) ~ 2 dx / c_last
    return 1e6 / (2 * a * integ)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # prueba del solver: n = 1 -> theta = sin(xi)/xi, xi1 = pi
    xi1, _, xs, ths = lane_emden(1)
    assert abs(xi1 - math.pi) < 1e-6, "Lane-Emden n=1: xi1 != pi"
    k = len(xs) // 3
    assert abs(ths[k] - math.sin(xs[k]) / xs[k]) < 1e-9
    # n = 0 -> xi1 = sqrt(6)
    xi0, _, _, _ = lane_emden(0)
    assert abs(xi0 - math.sqrt(6)) < 1e-6
    xi3, dth3, _, _ = lane_emden(3)
    print(f"solver: n=1 xi1 = {xi1:.6f} (pi = {math.pi:.6f}) ; n=0 xi1 = {xi0:.6f} ; n=3 xi1 = {xi3:.5f}")
    d_sol = delta_nu_uHz(M_SOL, R_SOL)
    # escala homologa: Delta nu ~ sqrt(M / R^3)
    d2 = delta_nu_uHz(2 * M_SOL, 1.5 * R_SOL)
    esperado = d_sol * math.sqrt(2 / 1.5 ** 3)
    assert abs(d2 / esperado - 1) < 1e-9, "escala homologa"
    print(f"politropo n=3 'solar': Delta nu = {d_sol:.1f} uHz")
    print(f"M=2, R=1.5: Delta nu = {d2:.1f} uHz ; esperado por escala = {esperado:.1f} uHz")
    rho_rel = lambda M, R: (M / M_SOL) / (R / R_SOL) ** 3
    gig = delta_nu_uHz(1.3 * M_SOL, 11 * R_SOL)
    print(f"gigante roja (M=1.3, R=11, ilustrativa): Delta nu = {gig:.2f} uHz ; densidad media relativa = {rho_rel(1.3 * M_SOL, 11 * R_SOL):.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
