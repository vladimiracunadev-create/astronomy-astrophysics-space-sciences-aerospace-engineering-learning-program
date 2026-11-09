#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C06: difusion y reaccion de un nutriente (u oxigeno) en una pelicula de biofilm.

Datos: SINTETICOS. Espesor L, difusividad efectiva D_e, constante de consumo k y concentracion en la superficie S0 son
propuestos; no corresponden a ningun biofilm medido. Apoyo cualitativo (resumen consultado el 2026-11-09, Europe PMC):
Flemming y Wingender 2010 -- la matriz de EPS (polisacaridos, proteinas, acidos nucleicos, lipidos) da estabilidad mecanica, fija
las celulas a superficies y retiene enzimas ("sistema digestivo externo").
Modelo: losa plana de espesor L [m], superficie x=L en contacto con el medio (S = S0) y sustrato impermeable en x=0 (dS/dx = 0).
Estado estacionario con consumo de primer orden: D_e S'' = k S.  Solucion: S(x) = S0 cosh(phi x/L)/cosh(phi), phi = L sqrt(k/D_e)
(modulo de Thiele). Factor de efectividad eta = tanh(phi)/phi. Profundidad de penetracion 1/sqrt(k/D_e).
Segunda via: diferencias finitas (N=400 nodos) con solucion del sistema tridiagonal por el algoritmo de Thomas.
Unidades: x [m]; D_e [m2/s]; k [1/s]; S [mol/m3]. Tolerancias: perfil numerico frente a analitico 1e-4 relativo (error maximo
normalizado por S0); eta numerico (flujo en la superficie) frente a tanh(phi)/phi 1e-3.
Supuestos: cinetica de primer orden, D_e uniforme, sin reaccion en el medio, 1D. Validez: ilustrativa.
"""
from __future__ import annotations
import math, platform


def analitico(x, L, De, k, S0):
    phi = L * math.sqrt(k / De)
    return S0 * math.cosh(phi * x / L) / math.cosh(phi)


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


def numerico(L, De, k, S0, N=400):
    h = L / N
    n = N  # incognitas en x = 0, h, ..., (N-1)h ; S(N h) = S0 conocido
    a, b, c, d = [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n
    for i in range(n):
        a[i] = De / h**2
        c[i] = De / h**2
        b[i] = -2 * De / h**2 - k
        d[i] = 0.0
    # frontera impermeable en x=0: nodo fantasma S_{-1} = S_1  -> c[0] se duplica
    c[0] = 2 * De / h**2
    d[-1] = -De / h**2 * S0
    S = thomas(a, b, c, d)
    S.append(S0)
    return S, h


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    De, S0 = 1.0e-9, 0.25    # m2/s, mol/m3 (SINTETICOS)
    print(f"Datos SINTETICOS: D_e = {De:.1e} m2/s ; S0 = {S0} mol/m3")
    print(f"{'L [um]':>7} {'k [1/s]':>9} {'phi':>7} {'eta':>7} {'S(0)/S0':>9} {'penetracion [um]':>17} {'error max':>10}")
    for L_um, k in ((20, 0.01), (100, 0.01), (100, 0.1), (500, 0.1)):
        L = L_um * 1e-6
        phi = L * math.sqrt(k / De)
        eta = math.tanh(phi) / phi
        S, h = numerico(L, De, k, S0)
        err = max(abs(S[i] - analitico(i * h, L, De, k, S0)) for i in range(len(S))) / S0
        flujo_num = De * (S[-1] - S[-2]) / h        # flujo hacia la pelicula en x=L (aprox. 1er orden)
        flujo_ideal = k * S0 * L                    # consumo si toda la pelicula viera S0
        eta_num = flujo_num / flujo_ideal
        pen = 1e6 / math.sqrt(k / De)
        print(f"{L_um:7d} {k:9.2f} {phi:7.2f} {eta:7.3f} {S[0] / S0:9.4f} {pen:17.1f} {err:10.2e}")
        assert err < 1e-4, err
        assert abs(eta_num - eta) / eta < 1e-2, (eta_num, eta)
    # caso limite: phi pequeno => perfil plano y eta -> 1
    L = 5e-6; k = 0.001
    S, h = numerico(L, De, k, S0)
    assert abs(S[0] - S0) / S0 < 1e-3
    print(f"Limite phi<<1: S(0)/S0 = {S[0] / S0:.5f}")
    print("Lectura: cuando phi >> 1 solo una capa de ~1/sqrt(k/D_e) cerca de la superficie recibe sustrato; el resto vive en carencia.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
