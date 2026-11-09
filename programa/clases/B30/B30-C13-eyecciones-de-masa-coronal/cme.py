#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C13: modelo de arrastre de una eyeccion de masa coronal y tiempo de transito a 1 au.

Datos: R_sol (IAU 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09. El viento ambiente (400 km/s), el parametro de arrastre (2e-8 km^-1), la distancia inicial (20 R_sol) y las
velocidades iniciales (500, 1000, 2000 km/s) son ILUSTRATIVOS (sinteticos); no se simula ningun evento concreto.
Modelo: dv/dt = -gamma (v - w)|v - w|; para v0 > w la solucion cerrada es v(t) = w + (v0 - w)/(1 + gamma (v0 - w) t) y r(t) = r0 + w t + ln(1 + gamma (v0 - w) t)/gamma;
integracion numerica con RK4; tiempo de transito a 1 au por biseccion sobre la forma cerrada; comparacion con el transito a velocidad constante.
Supuestos: arrastre cuadratico, viento ambiente uniforme y constante, 1D radial. Validez: orientativa.
Tolerancia: RK4 frente a la forma cerrada dentro de 1e-6 relativo en r y v; transito por biseccion y por RK4 dentro de 0.1 %.
"""
from __future__ import annotations
import math
import platform
import sys

R_SOL, AU = 6.957e5, 1.49597870700e8     # km
GAMMA, W = 2e-8, 400.0                    # km^-1 ; km/s


def cerrada(t, v0, r0):
    k = GAMMA * (v0 - W)
    return r0 + W * t + math.log(1 + k * t) / GAMMA, W + (v0 - W) / (1 + k * t)


def rk4(v0, r0, t_fin, h=60.0):
    r, v, t = r0, v0, 0.0
    f = lambda vv: -GAMMA * (vv - W) * abs(vv - W)
    while t < t_fin - 1e-9:
        d = min(h, t_fin - t)
        k1v = f(v); k1r = v
        k2v = f(v + 0.5 * d * k1v); k2r = v + 0.5 * d * k1v
        k3v = f(v + 0.5 * d * k2v); k3r = v + 0.5 * d * k2v
        k4v = f(v + d * k3v); k4r = v + d * k3v
        v += d * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        r += d * (k1r + 2 * k2r + 2 * k3r + k4r) / 6
        t += d
    return r, v


def transito(v0, r0, objetivo=AU):
    lo, hi = 0.0, 1e7
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if cerrada(mid, v0, r0)[0] < objetivo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    global GAMMA
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r0 = 20 * R_SOL
    print(f"r0 = 20 R_sol = {r0:.4e} km ; 1 au = {AU:.4e} km ; viento ambiente = {W:.0f} km/s ; gamma = {GAMMA:.1e} km^-1")
    print(f"{'v0 [km/s]':>10} {'t cerrada [h]':>14} {'r RK4 / 1 au':>14} {'v(1 au) [km/s]':>15} {'t const [h]':>12}")
    for v0 in (500.0, 1000.0, 2000.0):
        t = transito(v0, r0)
        r_c, v_c = cerrada(t, v0, r0)
        assert abs(r_c / AU - 1) < 1e-9
        r_n, v_n = rk4(v0, r0, t)
        assert abs(r_n / r_c - 1) < 1e-6 and abs(v_n / v_c - 1) < 1e-6, f"RK4 frente a la cerrada v0={v0}"
        tc = (AU - r0) / v0
        print(f"{v0:10.0f} {t / 3600:14.2f} {r_n / AU:14.6f} {v_c:15.1f} {tc / 3600:12.2f}")
    # el viento ambiente es una cota para v0 > w y v0 < w no se trata
    # sensibilidad al parametro de arrastre
    print(f"{'gamma [km^-1]':>14} {'t(1000 km/s) [h]':>17}")
    g0 = GAMMA
    for g in (0.5e-8, 1e-8, 2e-8, 4e-8):
        GAMMA = g
        print(f"{g:14.1e} {transito(1000.0, r0) / 3600:17.2f}")
    GAMMA = g0
    # distancia a la que la velocidad cae a w + 10 % del exceso
    v0 = 2000.0
    k = GAMMA * (v0 - W)
    t10 = (10 - 1) / k
    print(f"para v0 = 2000 km/s la velocidad cae al 10 % del exceso sobre el viento en t = {t10 / 3600:.1f} h, r = {cerrada(t10, v0, r0)[0] / AU:.2f} au")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
