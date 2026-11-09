#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C07: longitud de Debye, parametro de plasma y apantallamiento de una carga de prueba.

Datos: epsilon_0, k_B y e (NIST CODATA 2022), consultados 2026-11-09. Las densidades y temperaturas de los cuatro entornos (viento solar a 1 au: 5e6 m^-3 y 1e5 K;
corona: 1e15 m^-3 y 1.5e6 K; ionosfera F: 1e12 m^-3 y 1500 K; plasma de laboratorio: 1e18 m^-3 y 1e5 K) son ILUSTRATIVAS.
Modelo: lambda_D = sqrt(epsilon_0 k_B T/(n e^2)); numero de particulas en la esfera de Debye N_D = (4 pi/3) n lambda_D^3; potencial apantallado de una carga q
phi(r) = q exp(-r/lambda_D)/(4 pi epsilon_0 r), resuelto numericamente con u = r phi: u'' = u/lambda_D^2 (diferencias finitas, algoritmo de Thomas) y comparado con la forma cerrada;
carga de apantallamiento total -q (integral de la densidad inducida -epsilon_0 phi/lambda_D^2).
Supuestos: plasma de electrones con iones de fondo, aproximacion lineal (e phi << k_B T), un solo tipo de carga movil. Validez: respuesta estatica.
Tolerancia: potencial numerico frente al analitico a 1e-3 relativo en r = 0.5, 1, 2, 4 lambda_D; carga inducida total entre -0.99 q y -1.01 q.
"""
from __future__ import annotations
import math
import platform
import sys

EPS0, KB, E = 8.8541878188e-12, 1.380649e-23, 1.602176634e-19


def debye(n, t):
    return math.sqrt(EPS0 * KB * t / (n * E ** 2))


def thomas(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m if i < n - 1 else 0.0
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'entorno (ilustrativo)':<24} {'n [m-3]':>9} {'T [K]':>9} {'lambda_D [m]':>13} {'N_D':>12}")
    for nombre, n, t in (("viento solar (1 au)", 5e6, 1e5), ("corona", 1e15, 1.5e6), ("ionosfera F", 1e12, 1500.0), ("plasma de laboratorio", 1e18, 1e5)):
        ld = debye(n, t)
        nd = 4 * math.pi / 3 * n * ld ** 3
        print(f"{nombre:<24} {n:9.1e} {t:9.3g} {ld:13.4e} {nd:12.4e}")
    # escalas: lambda_D proporcional a sqrt(T/n)
    assert abs(debye(1e12, 4e4) / debye(1e12, 1e4) - 2) < 1e-12 and abs(debye(4e12, 1e4) / debye(1e12, 1e4) - 0.5) < 1e-12
    # apantallamiento numerico: u'' = u/lambda^2, u(0) = 1 (unidades de q/(4 pi eps0)), u(R) = 0
    ld = 1.0
    rmax, n = 40.0, 8000
    h = rmax / n
    a = [0.0] + [1.0 / h ** 2] * (n - 1)
    b = [1.0] + [-(2.0 / h ** 2 + 1.0 / ld ** 2)] * (n - 1)
    c = [0.0] + [1.0 / h ** 2] * (n - 1)
    d = [1.0] + [0.0] * (n - 1)
    b[-1] = 1.0
    a[-1] = 0.0
    d[-1] = 0.0
    u = thomas(a, b, c, d)
    print(f"{'r/lambda_D':>10} {'u numerico':>12} {'u analitico = exp(-r/lambda)':>29} {'dif. relativa':>14}")
    for r in (0.5, 1.0, 2.0, 4.0):
        i = int(round(r / h))
        ana = math.exp(-r / ld)
        print(f"{r:10.1f} {u[i]:12.6f} {ana:29.6f} {abs(u[i] / ana - 1):14.2e}")
        assert abs(u[i] / ana - 1) < 1e-3, f"apantallamiento en r={r}"
    # carga inducida total: Int -eps0 phi/lambda^2 4 pi r^2 dr, en unidades de q: phi = u/r -> -Int u r dr/lambda^2
    s = 0.0
    for i in range(1, n):
        r = i * h
        s += (4 if i % 2 else 2) * u[i] * r
    s = s * h / 3
    q_ind = -s / ld ** 2
    print(f"carga inducida total = {q_ind:.5f} q (esperada -1)")
    assert -1.01 < q_ind < -0.99, "carga de apantallamiento"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
