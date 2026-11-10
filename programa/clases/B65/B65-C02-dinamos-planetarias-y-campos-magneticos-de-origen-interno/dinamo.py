#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C02: escala de Elsasser, numero de Reynolds magnetico y decaimiento ohmico de un dipolo.

Datos consultados: mu0 = 1.25663706127e-6 N A^-2 (NIST, CODATA 2022, consulta 2026-11-09).
Datos ILUSTRATIVOS (sinteticos, de orden de magnitud terrestre; no son medidas): rho = 1.1e4 kg m^-3, sigma = 5e5 S m^-1, Omega = 7.292e-5 rad s^-1,
u = 5e-4 m s^-1, radio del nucleo 3.48e6 m, espesor del nucleo externo 2.26e6 m, radio superficial 6.371e6 m.
Modelo: (1) B = sqrt(Lambda rho Omega / sigma) con Lambda = 1 (Elsasser), Rm = mu0 sigma u L, dipolo en superficie por caida en r^-3.
(2) Decaimiento libre del modo dipolar poloidal de una esfera conductora en vacio: diferencias finitas implicitas, S_t = eta (S_xx - 2 S / x^2),
S(0) = 0, S'(1) + S(1) = 0 (campo exterior potencial), contra el decaimiento analitico tau = a^2 mu0 sigma / pi^2.
Supuestos: conductividad uniforme, sin flujo; (1) es una escala, no una prediccion. Validez: ilustrativa.
Tolerancia: tasa de decaimiento frente a pi^2 con error relativo < 2e-3.
"""
from __future__ import annotations
import math, platform

MU0 = 1.25663706127e-6            # N A^-2, NIST CODATA 2022
RHO, SIGMA, OMEGA = 1.1e4, 5.0e5, 7.292e-5
U, RC, DNUC, RSUP = 5.0e-4, 3.48e6, 2.26e6, 6.371e6

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

def tasa_decaimiento(N=400, dt=2.0e-4, t1=0.4, t2=0.5):
    """Devuelve la tasa lambda en unidades de eta/a^2 del modo mas lento (tiempo adimensional t eta/a^2)."""
    h = 1.0 / N
    x = [(i + 1) * h for i in range(N)]            # nodos 1..N (x = i*h)
    S = [xi**2 * (1.0 - 0.3 * xi) for xi in x]     # condicion inicial arbitraria
    a, b, c = [0.0] * N, [0.0] * N, [0.0] * N
    for i in range(N):
        xi = x[i]
        lo, hi = 1.0 / h**2, 1.0 / h**2
        diag = -2.0 / h**2 - 2.0 / xi**2
        a[i], b[i], c[i] = -dt * lo, 1.0 - dt * diag, -dt * hi
    # frontera en i = N-1 (x = 1): fantasma S_{N+1} = S_{N-1} - 2 h S_N
    a[N - 1] = -dt * (lo + hi)
    b[N - 1] = 1.0 - dt * (-2.0 / h**2 - 2.0 / x[N - 1]**2 - 2.0 * h / h**2)
    t, regs = 0.0, {}
    while t < t2 + 1e-12:
        S = thomas(a, b, c, S[:])
        t += dt
        if abs(t - t1) < dt / 2:
            regs["t1"] = S[N // 2]
        if abs(t - t2) < dt / 2:
            regs["t2"] = S[N // 2]
    return -math.log(regs["t2"] / regs["t1"]) / (t2 - t1)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # (1) Elsasser
    B = math.sqrt(1.0 * RHO * OMEGA / SIGMA)
    rm = MU0 * SIGMA * U * DNUC
    Bsup = B * (RC / RSUP) ** 3 / 2.0
    print(f"Elsasser (Lambda = 1): B_nucleo = {B*1e3:.3f} mT ; Rm = mu0 sigma u L = {rm:.1f} ; dipolo en superficie (B_nucleo (rc/R)^3 / 2) = {Bsup*1e6:.1f} uT")
    for lam in (0.1, 1.0, 10.0):
        print(f"  Lambda = {lam:5.1f} -> B_nucleo = {math.sqrt(lam*RHO*OMEGA/SIGMA)*1e3:.3f} mT")
    # (2) decaimiento
    lam_num = tasa_decaimiento()
    lam_ana = math.pi**2
    err = abs(lam_num - lam_ana) / lam_ana
    print(f"Tasa de decaimiento (unidades eta/a^2): diferencias finitas = {lam_num:.5f} ; analitica pi^2 = {lam_ana:.5f} ; error relativo = {err:.2e}")
    tau = RC**2 * MU0 * SIGMA / math.pi**2
    anio = 3.15576e7
    print(f"Tiempo de decaimiento tau = a^2 mu0 sigma / pi^2 con a = radio del nucleo (3.48e6 m): {tau/anio:.0f} anos")
    assert err < 2e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
