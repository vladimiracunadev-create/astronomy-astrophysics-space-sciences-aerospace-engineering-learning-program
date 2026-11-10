#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C10: perdida de un impulso finito frente al impulsivo en la salida desde una orbita baja terrestre.

Datos consultados (2026-11-10): masa de la Tierra 5.9722e24 kg y radio medio 6371.0 km (ficha NASA/NSSDC); G = 6.67430e-11 (registro JPL); GM_tierra = G M.
v_inf de salida = 2.9452 km/s: resultado del modelo de C01 (Hohmann Tierra-Marte, circular y coplanar). g0 = 9.80665 m/s2 y GM_sol = 1.32712440e11 km3/s2 (estandar, no consultados).
SINTETICOS / ILUSTRATIVOS: orbita inicial circular a 300 km, Isp = 320 s, razones empuje/peso inicial de 0.02 a 500; empuje constante y direccion = velocidad (prograda).
Modelo: dos cuerpos con empuje finito integrado con RK4; el motor se apaga cuando la energia especifica alcanza v_inf^2/2.
Pruebas: (1) con empuje/peso 500 la perdida relativa es menor que 1e-3; (2) la perdida crece al bajar el empuje/peso; (3) al apagar, la energia es la objetivo (tol. 1e-3 km2/s2).
"""
import math, platform
G = 6.67430e-20
GME = G * 5.9722e24
R0 = 6371.0 + 300.0
G0 = 9.80665e-3  # km/s2
ISP = 320.0
VINF = 2.9452
EPS_T = 0.5 * VINF**2


def acc(x, y, vx, vy, m, emp):
    r = math.hypot(x, y); v = math.hypot(vx, vy)
    ax = -GME * x / r**3 + emp / m * vx / v
    ay = -GME * y / r**3 + emp / m * vy / v
    return ax, ay


def quema(tw, dt):
    m0 = 1000.0
    emp = tw * m0 * G0          # km*kg/s2 (kN equivalente en estas unidades)
    mdot = emp / (ISP * G0)
    x, y, vx, vy, m = R0, 0.0, 0.0, math.sqrt(GME / R0), m0
    eps_prev = 0.5 * (vx * vx + vy * vy) - GME / R0
    t = 0.0
    while True:
        def f(s):
            x, y, vx, vy, m = s
            ax, ay = acc(x, y, vx, vy, m, emp)
            return [vx, vy, ax, ay, -mdot]
        s = [x, y, vx, vy, m]
        k1 = f(s); k2 = f([a + 0.5 * dt * b for a, b in zip(s, k1)])
        k3 = f([a + 0.5 * dt * b for a, b in zip(s, k2)]); k4 = f([a + dt * b for a, b in zip(s, k3)])
        s2 = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]
        eps = 0.5 * (s2[2] ** 2 + s2[3] ** 2) - GME / math.hypot(s2[0], s2[1])
        t += dt
        if eps >= EPS_T:
            fr = (EPS_T - eps_prev) / (eps - eps_prev)
            m_end = s[4] + fr * (s2[4] - s[4])
            return ISP * G0 * math.log(m0 / m_end), t - dt + fr * dt, EPS_T
        x, y, vx, vy, m = s2; eps_prev = eps


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    vc = math.sqrt(GME / R0)
    dv_imp = math.sqrt(VINF**2 + 2 * GME / R0) - vc
    print(f"Orbita inicial: r = {R0:.0f} km ; v_circ = {vc:.4f} km/s ; periodo = {2*math.pi*math.sqrt(R0**3/GME)/60:.2f} min")
    print(f"Impulsivo: dv = {dv_imp:.4f} km/s")
    print(" empuje/peso inicial   duracion [min]   dv finito [km/s]   perdida [km/s]   perdida relativa [%]")
    perdidas = []
    for tw in (0.02, 0.05, 0.1, 0.5, 5.0, 500.0):
        est = dv_imp / (tw * G0) * 1.0
        dt = max(est / 20000.0, 1e-4)
        dvf, tq, eps = quema(tw, dt)
        perdidas.append(dvf - dv_imp)
        print(f"{tw:15.3f} {tq/60:15.2f} {dvf:18.4f} {dvf-dv_imp:15.3g} {100*(dvf-dv_imp)/dv_imp:18.3g}")
    assert perdidas[-1] / dv_imp < 1e-3
    assert all(a > b for a, b in zip(perdidas, perdidas[1:]))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
