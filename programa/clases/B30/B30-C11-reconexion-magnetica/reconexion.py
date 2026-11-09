#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C11: difusion resistiva de una hoja de corriente y tasa de reconexion de Sweet-Parker.

Datos: mu_0 (NIST CODATA 2022), consultado 2026-11-09. El campo (0.01 T), la velocidad de Alfven (1e6 m/s), la longitud de la hoja (1e7 m) y los numeros de Lundquist
(1e4, 1e8, 1e12) son ILUSTRATIVOS (sinteticos).
Modelo: (1) difusion del campo dB/dt = eta d^2B/dx^2 desde un salto B(x, 0) = B0 sign(x); solucion analitica B(x, t) = B0 erf(x/sqrt(4 eta t)); esquema implicito de Crank-Nicolson
con algoritmo de Thomas. (2) Sweet-Parker: conservacion de la masa v_in L = v_out delta con v_out = v_A y delta/L = S^(-1/2), S = L v_A/eta; tasa de reconexion v_in/v_A = S^(-1/2);
tiempo de reconexion tau_A S^(1/2) con tau_A = L/v_A. (3) Energia magnetica liberada W = (B^2/(2 mu_0)) V.
Supuestos: resistividad uniforme, 1D, incompresible para Sweet-Parker. Validez: orientativa.
Tolerancia: perfil numerico frente a erf dentro de 2e-3 en valor absoluto (B/B0); conservacion de la masa v_in L = v_out delta a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

MU0 = 1.25663706127e-6


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


def difusion(eta, t_fin, nx=2001, xmax=10.0, pasos=2000):
    h = 2 * xmax / (nx - 1)
    xs = [-xmax + i * h for i in range(nx)]
    # suavizar el salto inicial con una escala de un paso (se compara con erf desde t > 0)
    b = [1.0 if x > 0 else (-1.0 if x < 0 else 0.0) for x in xs]
    dt = t_fin / pasos
    r = eta * dt / (2 * h * h)
    a = [0.0] + [-r] * (nx - 2) + [0.0]
    dia = [1.0] + [1 + 2 * r] * (nx - 2) + [1.0]
    c = [0.0] + [-r] * (nx - 2) + [0.0]
    for _ in range(pasos):
        d = [b[0]] + [b[i] + r * (b[i + 1] - 2 * b[i] + b[i - 1]) for i in range(1, nx - 1)] + [b[-1]]
        b = thomas(a, dia, c, d)
    return xs, b


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    eta, t = 1.0, 1.0
    xs, b = difusion(eta, t)
    print(f"{'x':>6} {'B/B0 numerico':>14} {'erf(x/sqrt(4 eta t))':>22} {'|dif|':>10}")
    peor = 0.0
    for x in (0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
        i = min(range(len(xs)), key=lambda k: abs(xs[k] - x))
        ana = math.erf(xs[i] / math.sqrt(4 * eta * t))
        d = abs(b[i] - ana)
        peor = max(peor, d)
        print(f"{xs[i]:6.2f} {b[i]:14.6f} {ana:22.6f} {d:10.2e}")
    assert peor < 2e-3, "difusion frente a erf"
    ancho = math.sqrt(4 * eta * t)
    print(f"escala de difusion sqrt(4 eta t) = {ancho:.3f} (en unidades de sqrt(eta t) = {ancho:.3f}); el campo en x = ancho vale erf(1) = {math.erf(1):.5f}")
    # Sweet-Parker
    L, va = 1e7, 1e6
    tau_a = L / va
    print(f"hoja de L = {L:.0e} m, v_A = {va:.0e} m/s: tau_A = L/v_A = {tau_a:.1f} s")
    print(f"{'S':>8} {'delta/L':>10} {'v_in/v_A':>10} {'v_in [m/s]':>11} {'tau_SP [s]':>12} {'tau_SP':>12}")
    for s in (1e2, 1e4, 1e8, 1e12):
        delta = L * s ** -0.5
        v_in = va * s ** -0.5
        assert abs(v_in * L - va * delta) < 1e-12 * va * delta, "conservacion de la masa"
        tsp = tau_a * s ** 0.5
        etiqueta = f"{tsp / 86400:.3g} d" if tsp > 86400 else f"{tsp / 60:.3g} min"
        print(f"{s:8.0e} {delta / L:10.2e} {v_in / va:10.2e} {v_in:11.3e} {tsp:12.3e} {etiqueta:>12}")
    # tasa necesaria para un evento de 100 s
    tasa = tau_a / 100
    print(f"tasa v_in/v_A para reconectar en 100 s: {tasa:.3f} -> S = {tasa ** -2:.0f} segun Sweet-Parker")
    # energia
    bm, vol = 0.01, 1e21
    w = bm ** 2 / (2 * MU0) * vol
    print(f"energia magnetica B^2/(2 mu_0) V con B = {bm} T y V = {vol:.0e} m3: {w:.3e} J = {w * 1e7:.3e} erg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
