#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C01: propagacion de error de navegacion inercial a partir de sesgos de una IMU.

Datos consultados (2026-11-10): g media terrestre 9.820 m/s2 y radio ecuatorial 6378.137 km (ficha NASA/NSSDC);
g estandar 9.80665 m/s2 (NIST CODATA). Todo lo demas es SINTETICO e ILUSTRATIVO: sesgo de acelerometro b = 1.0e-3 m/s2 (aprox. 100 microg),
sesgo de giroscopio eps = 0.01 grados/h, tiempo de 600 s.
Modelo 1 (sin realimentacion de gravedad, plano local): x(t) = 0.5 b t^2 (error de posicion por sesgo de acelerometro).
Modelo 2: sesgo de giroscopio eps inclina la plataforma theta = eps t y la gravedad se proyecta como aceleracion falsa g theta:
  x(t) = g eps t^3 / 6 (aproximacion para t << periodo de Schuler).
Modelo 3: con la realimentacion de gravedad sobre una Tierra esferica, x(t) = eps R (t - sin(w_s t)/w_s), w_s = sqrt(g/R);
  el periodo de Schuler es 2 pi / w_s y el error crece linealmente con eps R, no cubicamente.
Segunda via: integracion numerica (Euler semi-implicito, dt = 0.01 s) de las ecuaciones diferenciales. Tolerancia: 0.5 % frente al analitico.
Sistema de referencia: navegacion local (ENU) fijo, sin rotacion terrestre; unidades SI, angulos en rad.
"""
from __future__ import annotations
import math, platform

G, R_T, G0 = 9.820, 6378.137e3, 9.80665
B_ACC = 1.0e-3
EPS = math.radians(0.01) / 3600.0
T = 600.0
DT = 0.01


def x_acc(t):
    return 0.5 * B_ACC * t * t


def x_gyro(t):
    return G * EPS * t ** 3 / 6.0


def numerico_acc(t_fin, dt=DT):
    v = x = 0.0
    n = int(round(t_fin / dt))
    for _ in range(n):
        v += B_ACC * dt
        x += v * dt
    return x


def numerico_gyro(t_fin, dt=DT):
    theta = v = x = 0.0
    n = int(round(t_fin / dt))
    for _ in range(n):
        theta += EPS * dt
        v += G * theta * dt
        x += v * dt
    return x


def schuler(t_fin, dt=0.05):
    """Error de inclinacion y de posicion con realimentacion de Schuler: x'' = g*theta_t ; theta' = eps - x'/R ; error de posicion x."""
    ws2 = G / R_T
    x = v = 0.0
    n = int(round(t_fin / dt))
    th = 0.0
    for _ in range(n):
        # theta' = eps - v/R ; v' = g*theta
        th += (EPS - v / R_T) * dt
        v += G * th * dt
        x += v * dt
    return x, th


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Sesgo acelerometro (SINTETICO) b = {B_ACC:.1e} m/s2 = {B_ACC / G0 * 1e6:.1f} micro-g ; sesgo giroscopio eps = {EPS:.4e} rad/s = 0.01 grados/h")
    print(" t [s]   x_acc analitico [m]  x_acc numerico [m]   x_gyro analitico [m]  x_gyro numerico [m]")
    dmax = 0.0
    for t in (60.0, 120.0, 300.0, 600.0):
        xa, xn = x_acc(t), numerico_acc(t)
        ga, gn = x_gyro(t), numerico_gyro(t)
        dmax = max(dmax, abs(xn - xa) / xa, abs(gn - ga) / ga)
        print(f"{t:6.0f} {xa:20.4f} {xn:20.4f} {ga:21.5f} {gn:19.5f}")
    print(f"Diferencia relativa maxima numerico frente a analitico = {dmax:.2e}")
    ws = math.sqrt(G / R_T)
    per = 2.0 * math.pi / ws
    print(f"Frecuencia de Schuler w_s = sqrt(g/R) = {ws:.6e} rad/s ; periodo = {per:.1f} s = {per / 60.0:.2f} min")
    # Con Schuler el error por sesgo de giroscopio crece de forma lineal (eps R t), no cubica
    xs_10, _ = schuler(600.0)
    xs_per, _ = schuler(per)
    cerrada = EPS * R_T * (600.0 - math.sin(ws * 600.0) / ws)
    print(f"Con realimentacion de Schuler: x(600 s) = {xs_10:.5f} m (sin ella {x_gyro(600.0):.5f} m) ; x(periodo) = {xs_per:.2f} m")
    print(f"Forma cerrada x(t) = eps R (t - sin(w_s t)/w_s): x(600 s) = {cerrada:.5f} m ; crecimiento lineal eps R = {EPS * R_T:.4f} m/s")
    # Hora de duplicar: tiempo para que el sesgo de acelerometro acumule 1 km
    t1km = math.sqrt(2.0 * 1000.0 / B_ACC)
    print(f"Tiempo para acumular 1 km de error con b = 1e-3 m/s2: {t1km:.0f} s = {t1km / 60.0:.1f} min")
    assert dmax < 5e-3
    assert abs(xs_10 - cerrada) / cerrada < 5e-3
    assert abs(xs_10 - x_gyro(600.0)) / x_gyro(600.0) < 0.05
    assert abs(xs_per - EPS * R_T * (per - math.sin(ws * per) / ws)) / xs_per < 5e-3
    assert abs(per / 60.0 - 84.4) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
