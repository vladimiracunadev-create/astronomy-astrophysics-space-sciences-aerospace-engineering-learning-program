#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C11: orbita relativa de inspeccion (Clohessy-Wiltshire) verificada por integracion numerica de dos cuerpos.

Datos consultados (2026-11-10): Tierra, g media 9.820 m/s2 y radio medio 6371.0 km (NASA/NSSDC); GM = g R^2 se CALCULA aqui (aproximacion).
ILUSTRATIVOS (sinteticos): orbita circular del objetivo a 400 km de altitud, elipse de inspeccion de 100 m en la direccion radial (200 m a lo largo de la traza), inicio en y0 = 0.
Modelo CW: sistema local (x radial hacia fuera, y a lo largo de la traza), orbita circular del objetivo, sin perturbaciones ni empuje. Sin deriva si vy0 = -2 n x0:
x = x0 cos(nt), y = y0 - 2 x0 sin(nt), elipse 1:2.
Segunda via: integracion RK4 (paso de 1 s) de las dos naves bajo gravedad puntual, con la posicion relativa expresada en el sistema local; tolerancia 0.5 m tras una orbita.
Unidades SI; sistema de referencia inercial centrado en la Tierra para la integracion y local (LVLH) para el resultado.
"""
from __future__ import annotations
import math, platform

G_T, R_T = 9.820, 6371.0e3             # NASA/NSSDC
GM = G_T * R_T ** 2                    # derivado, aproximado
A = R_T + 400e3                        # ILUSTRATIVO
N = math.sqrt(GM / A ** 3)
X0 = 100.0                             # m (ILUSTRATIVO)


def acel(x, y):
    r3 = math.hypot(x, y) ** 3
    return -GM * x / r3, -GM * y / r3


def rk4(est, dt):
    def f(s):
        ax, ay = acel(s[0], s[1])
        return [s[2], s[3], ax, ay]
    k1 = f(est)
    k2 = f([e + 0.5 * dt * k for e, k in zip(est, k1)])
    k3 = f([e + 0.5 * dt * k for e, k in zip(est, k2)])
    k4 = f([e + dt * k for e, k in zip(est, k3)])
    return [e + dt / 6.0 * (a + 2 * b + 2 * c + d) for e, a, b, c, d in zip(est, k1, k2, k3, k4)]


def cw(t, x0, y0, vx0, vy0):
    s, c = math.sin(N * t), math.cos(N * t)
    x = (4 - 3 * c) * x0 + s / N * vx0 + 2 / N * (1 - c) * vy0
    y = 6 * (s - N * t) * x0 + y0 - 2 / N * (1 - c) * vx0 + (4 * s - 3 * N * t) / N * vy0
    return x, y


def calc():
    vy0 = -2 * N * X0
    periodo = 2 * math.pi / N
    # integracion de dos cuerpos: objetivo en (A, 0) con velocidad circular; perseguidor desplazado
    objetivo = [A, 0.0, 0.0, N * A]
    pos_rel = (X0, 0.0)
    vel_rel = (0.0, vy0)
    persegu = [A + pos_rel[0], pos_rel[1], objetivo[2] + vel_rel[0] - N * pos_rel[1], objetivo[3] + vel_rel[1] + N * pos_rel[0]]
    dt, t, pasos = 1.0, 0.0, int(round(periodo))
    maxdif, mind, tray = 0.0, 1e9, []
    for k in range(pasos):
        objetivo, persegu = rk4(objetivo, dt), rk4(persegu, dt)
        t += dt
        r = math.hypot(objetivo[0], objetivo[1])
        rh = (objetivo[0] / r, objetivo[1] / r)
        th = (-rh[1], rh[0])
        dx, dy = persegu[0] - objetivo[0], persegu[1] - objetivo[1]
        xl, yl = dx * rh[0] + dy * rh[1], dx * th[0] + dy * th[1]
        xc, yc = cw(t, X0, 0.0, 0.0, vy0)
        maxdif = max(maxdif, math.hypot(xl - xc, yl - yc))
        mind = min(mind, math.hypot(xl, yl))
        tray.append((xl, yl))
    xf, yf = tray[-1]
    vmax = 2 * N * X0
    return dict(gm=GM, a_km=A / 1e3, n=N, T_min=periodo / 60.0, maxdif=maxdif, mind=mind, xf=xf, yf=yf, vmax=vmax, vy0=vy0,
                ymax=max(abs(p[1]) for p in tray), xmax=max(abs(p[0]) for p in tray), cierre=math.hypot(xf - X0, yf), pasos=pasos,
                deriva_sin=abs(6 * (-2 * math.pi) * X0) )


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"GM = g R^2 = {r['gm']:.4e} m3/s2 (derivado); objetivo ILUSTRATIVO a {r['a_km']-R_T/1e3:.0f} km: n = {r['n']:.6e} rad/s; periodo = {r['T_min']:.2f} min")
    print(f"Elipse de inspeccion: x0 = {X0} m, vy0 = {r['vy0']:.5f} m/s (condicion sin deriva); velocidad relativa maxima = {r['vmax']:.4f} m/s")
    print(f"Integracion RK4 ({r['pasos']} pasos de 1 s): amplitud radial = {r['xmax']:.2f} m; amplitud a lo largo de la traza = {r['ymax']:.2f} m; distancia minima al objetivo = {r['mind']:.2f} m")
    print(f"Cierre tras una orbita = {r['cierre']:.3f} m; diferencia maxima RK4 frente a CW = {r['maxdif']:.3f} m")
    print(f"Sin la condicion vy0 = -2 n x0, la deriva en una orbita seria {r['deriva_sin']:.0f} m a lo largo de la traza")
    assert r["maxdif"] < 0.5 and r["mind"] > 0.99 * X0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
