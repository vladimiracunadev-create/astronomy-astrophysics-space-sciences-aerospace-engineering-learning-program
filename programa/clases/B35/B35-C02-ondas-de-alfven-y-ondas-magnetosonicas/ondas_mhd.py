#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C02: velocidades de fase de las ondas MHD y simulacion de una onda de Alfven.

Datos: mu_0, m_p y k_B (NIST CODATA 2022, tabla allascii.txt, consultados 2026-11-09). La densidad (5 cm^-3), el campo (5 nT), la temperatura (1e5 K) y gamma = 5/3 son ILUSTRATIVOS (sinteticos);
no son una medicion del viento solar.
Modelo: v_A = B/sqrt(mu0 rho); c_s = sqrt(gamma p/rho); velocidades de fase rapida y lenta v^2 = 1/2[(cs^2+vA^2) +- sqrt((cs^2+vA^2)^2 - 4 cs^2 vA^2 cos^2 th)].
Segunda via independiente: ecuacion de onda transversal d2b/dt2 = vA^2 d2b/dx2 integrada con diferencias finitas centradas y salto de rana (CFL = 0.5) sobre un pulso gaussiano; se mide el
desplazamiento del maximo y se compara con vA t.
Supuestos: plasma uniforme, MHD ideal, amplitud pequena. Validez: ilustrativa.
Tolerancia: velocidad medida frente a vA con error relativo < 1 %; limites th = 0 y th = 90 grados exactos a 1e-6 m/s.
"""
from __future__ import annotations
import math, platform, sys

MU0 = 1.25663706127e-6
M_P = 1.67262192595e-27
K_B = 1.380649e-23

def fase(cs, va, th):
    s = cs * cs + va * va
    d = math.sqrt(max(s * s - 4 * cs * cs * va * va * math.cos(th) ** 2, 0.0))
    return math.sqrt(0.5 * (s + d)), math.sqrt(0.5 * (s - d))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, B, T, gam = 5e6, 5e-9, 1e5, 5.0 / 3.0
    rho = n * M_P
    va = B / math.sqrt(MU0 * rho)
    p = 2 * n * K_B * T  # protones y electrones a la misma T
    cs = math.sqrt(gam * p / rho)
    beta = p / (B * B / (2 * MU0))
    print(f"vA = {va/1e3:.2f} km/s ; cs = {cs/1e3:.2f} km/s ; beta = {beta:.3f}")
    print(f"{'th [grados]':>11} {'rapida [km/s]':>14} {'Alfven [km/s]':>14} {'lenta [km/s]':>13}")
    for deg in (0, 30, 60, 90):
        th = math.radians(deg)
        f, s = fase(cs, va, th)
        print(f"{deg:11d} {f/1e3:14.2f} {va*abs(math.cos(th))/1e3:14.2f} {s/1e3:13.2f}")
    f0, s0 = fase(cs, va, 0.0)
    assert abs(f0 - max(cs, va)) < 1e-6 and abs(s0 - min(cs, va)) < 1e-6
    f9, s9 = fase(cs, va, math.pi / 2)
    assert abs(f9 - math.sqrt(cs * cs + va * va)) < 1e-6 and s9 < 1e-3
    # simulacion de la onda de Alfven transversal (unidades normalizadas: vA = 1, L = 1)
    N = 800; L = 1.0; dx = L / N; dt = 0.5 * dx
    x = [i * dx for i in range(N)]
    x0, w = 0.3, 0.03
    bn = [math.exp(-0.5 * ((xi - x0) / w) ** 2) for xi in x]
    bp = [math.exp(-0.5 * ((xi + dt - x0) / w) ** 2) for xi in x]  # paso previo de un pulso que viaja a +x
    c2 = (dt / dx) ** 2
    t = 0.0
    pasos = int(round(0.4 / dt))
    for _ in range(pasos):
        bnext = [2 * bn[i] - bp[i] + c2 * (bn[(i + 1) % N] - 2 * bn[i] + bn[i - 1]) for i in range(N)]
        bp, bn = bn, bnext
        t += dt
    imax = max(range(N), key=lambda i: bn[i])
    ym, y0, yp = bn[imax - 1], bn[imax], bn[(imax + 1) % N]
    off = 0.5 * (ym - yp) / (ym - 2 * y0 + yp)
    xmax = (imax + off) * dx
    v_medida = (xmax - x0) / t
    print(f"Simulacion: t = {t:.4f} ; desplazamiento = {xmax - x0:.5f} ; v_medida/vA = {v_medida:.5f} ; amplitud = {bn[imax]:.4f}")
    assert abs(v_medida - 1) < 0.01
    assert abs(bn[imax] - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
