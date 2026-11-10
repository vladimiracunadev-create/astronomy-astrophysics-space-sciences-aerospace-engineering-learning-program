#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C03: ecuacion de movimiento de dos cuerpos, baricentro y convergencia de RK4.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3); G = 6.67430e-11 (CODATA 2022);
fichas NASA/NSSDC: masa de la Tierra 5.9722e24 kg y de la Luna 0.07346e24 kg, a de la Luna 0.3844e6 km, radio medio de la Tierra 6371.000 km.
Orbita integrada SINTETICA: periapsis a 300 km de altitud, apoapsis a 10000 km de altitud, plano xy, marco inercial geocentrico (SI).
Modelo: r'' = -mu r/|r|^3 (movimiento relativo); RK4 con pasos T/N y N = 200, 400, 800, 1600.
Segunda via: tras exactamente un periodo T = 2 pi sqrt(a^3/mu) la solucion analitica es el estado inicial; el error de cierre debe caer
como dt^4 (cociente de errores ~16 al duplicar N; tolerancia 12 a 20 en los dos ultimos pasos).
Baricentro Tierra-Luna: d = a m_L/(m_T + m_L).
"""
from __future__ import annotations
import math, platform

MU = 3.986004e14
RE = 6.3781e6
G = 6.67430e-11
M_T, M_L = 5.9722e24, 0.07346e24
A_LUNA = 0.3844e9
RT_MEDIO = 6.371e6


def acc(x, y):
    d3 = (x * x + y * y) ** 1.5
    return -MU * x / d3, -MU * y / d3


def paso(s, dt):
    x, y, vx, vy = s
    def f(s):
        ax, ay = acc(s[0], s[1])
        return (s[2], s[3], ax, ay)
    k1 = f(s)
    k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
    k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
    k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
    return tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))


def una_vuelta(n):
    rp, ra = RE + 300e3, RE + 10000e3
    a = 0.5 * (rp + ra)
    vp = math.sqrt(MU * (2 / rp - 1 / a))
    t = 2 * math.pi * math.sqrt(a ** 3 / MU)
    s0 = (rp, 0.0, 0.0, vp)
    s = s0
    dt = t / n
    e0 = 0.5 * (s0[2] ** 2 + s0[3] ** 2) - MU / rp
    for _ in range(n):
        s = paso(s, dt)
    err_pos = math.hypot(s[0] - s0[0], s[1] - s0[1])
    e1 = 0.5 * (s[2] ** 2 + s[3] ** 2) - MU / math.hypot(s[0], s[1])
    return err_pos, abs(e1 - e0) / abs(e0), t, a, vp


def calcular():
    R = {}
    ns = [200, 400, 800, 1600]
    errs, derr = [], []
    for n in ns:
        e, de, t, a, vp = una_vuelta(n)
        errs.append(e); derr.append(de)
    R["ns"] = ns
    R["errs"] = errs
    R["derr"] = derr
    R["razones"] = [errs[i] / errs[i + 1] for i in range(3)]
    R["periodo_s"] = t
    R["a_m"] = a
    R["vp"] = vp
    R["d_bar"] = A_LUNA * M_L / (M_T + M_L)
    R["d_bar_rel"] = R["d_bar"] / RT_MEDIO
    R["razon_masas"] = M_T / M_L
    R["mu_rel_luna"] = G * (M_T + M_L)
    R["mu_t"] = MU
    R["efecto_mu"] = M_L / M_T
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("Orbita SINTETICA: periapsis 300 km, apoapsis 10000 km de altitud; a = %.3f km ; T = %.3f s ; v_p = %.3f m/s" % (R["a_m"] / 1e3, R["periodo_s"], R["vp"]))
    print("  N pasos/vuelta   error de cierre [m]   deriva relativa de la energia")
    for n, e, d in zip(R["ns"], R["errs"], R["derr"]):
        print(f"  {n:6d}           {e:12.4e}          {d:10.3e}")
    print("  cociente de errores al duplicar N: " + " ".join(f"{x:.2f}" for x in R["razones"]) + "  (orden 4 -> 16)")
    print(f"Baricentro Tierra-Luna: a m_L/(m_T+m_L) = {R['d_bar'] / 1e3:.1f} km del centro de la Tierra = {R['d_bar_rel']:.3f} radios terrestres (dentro de la Tierra)")
    print(f"  m_T/m_L = {R['razon_masas']:.2f} ; m_L/m_T = {R['efecto_mu']:.5f}")
    print(f"  G(m_T+m_L) = {R['mu_rel_luna']:.6e} m3/s2 frente a (GM)T = {R['mu_t']:.6e} m3/s2")
    assert R["errs"][-1] < R["errs"][0]
    assert all(10 < x < 22 for x in R["razones"][1:])
    assert R["d_bar"] < RT_MEDIO
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
