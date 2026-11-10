#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C04: espiral tangencial de bajo empuje entre orbitas circulares (Edelbaum) y comparacion con la integracion directa.

Datos: GM de la Tierra = 398600.435507 km^3/s^2 (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Radios (ILUSTRATIVOS, sinteticos): orbita inicial 7000 km, final 42164 km (radios del orden de una orbita baja y una geoestacionaria); aceleracion
de empuje constante e igual a 1e-3 m/s^2 = 1e-6 km/s^2 (ILUSTRATIVA); inclinacion a cambiar: 28,5 grados (ILUSTRATIVA).
Sistema de referencia: inercial geocentrico; km, km/s, s.
Modelo: dos cuerpos con empuje tangencial a la velocidad (coplanar). Promediado: da/dt = 2 a_t sqrt(a^3/mu), de donde dv = |v0 - v1| y t = dv/a_t.
Edelbaum con cambio de plano (aceleracion constante, guiado optimo): dv = sqrt(v0^2 - 2 v0 v1 cos(pi/2 di) + v1^2).
Integrador de la prueba directa: DOP853, rtol = 1e-10, atol = 1e-12 (dos cuerpos con empuje tangencial) hasta alcanzar el semieje deseado.
Tolerancias: tiempo promediado frente a dv/a_t < 1e-6 relativo; directo frente a promediado < 1e-2 relativo; excentricidad final < 1e-2.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp

MU = 398600.435507
R0, R1 = 7000.0, 42164.0
AT = 1.0e-6  # km/s^2


def rhs(t, y):
    r = y[:2]
    v = y[2:]
    rn = np.linalg.norm(r)
    return np.concatenate([v, -MU * r / rn**3 + AT * v / np.linalg.norm(v)])


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    v0, v1 = math.sqrt(MU / R0), math.sqrt(MU / R1)
    dv_coplanar = v0 - v1
    print(f"Orbitas ILUSTRATIVAS: r0 = {R0:.0f} km (v = {v0:.4f} km/s), r1 = {R1:.0f} km (v = {v1:.4f} km/s) ; a_t = {AT*1e3:.1e} m/s^2")
    print(f"dv coplanar (|v0 - v1|) = {dv_coplanar*1e3:.2f} m/s ; tiempo = dv/a_t = {dv_coplanar/AT/86400:.3f} d")
    di = math.radians(28.5)
    dv_e = math.sqrt(v0**2 - 2 * v0 * v1 * math.cos(math.pi / 2 * di) + v1**2)
    print(f"dv de Edelbaum con cambio de plano de 28,5 grados = {dv_e*1e3:.2f} m/s (+{(dv_e/dv_coplanar-1)*100:.1f} % ) ; tiempo = {dv_e/AT/86400:.3f} d")
    # promediado: integrar a(t)
    s = solve_ivp(lambda t, a: [2 * AT * math.sqrt(a[0]**3 / MU)], (0, 1e8), [R0], rtol=1e-12, atol=1e-9,
                  events=lambda t, a: a[0] - R1)
    t_av = s.t_events[0][0]
    rel = abs(t_av - dv_coplanar / AT) / (dv_coplanar / AT)
    print(f"Promediado: tiempo para a = r1 = {t_av/86400:.4f} d ; diferencia relativa con dv/a_t = {rel:.2e}")
    # directo: integrar dos cuerpos con empuje tangencial
    y0 = np.array([R0, 0.0, 0.0, v0])
    ev = lambda t, y: (-MU / (2 * (0.5 * (y[2]**2 + y[3]**2) - MU / math.hypot(y[0], y[1])))) - R1
    ev.terminal = True
    sd = solve_ivp(rhs, (0, 1e8), y0, method="DOP853", rtol=1e-10, atol=1e-12, events=ev)
    td = sd.t_events[0][0]
    yf = sd.y_events[0][0]
    r = np.linalg.norm(yf[:2]); v = np.linalg.norm(yf[2:])
    h = yf[0] * yf[3] - yf[1] * yf[2]
    ecc = math.sqrt(max(0.0, 1 + 2 * (0.5 * v**2 - MU / r) * h**2 / MU**2))
    dvd = AT * td
    print(f"Directo: tiempo = {td/86400:.4f} d ; dv = a_t t = {dvd*1e3:.2f} m/s ; excentricidad final = {ecc:.4f}")
    print(f"Diferencia directo frente a promediado = {abs(td - t_av)/t_av:.2e} ; revoluciones aprox. = {np.sum(np.abs(np.diff(np.unwrap(np.arctan2(sd.y[1], sd.y[0]))))) / (2*math.pi):.0f}")
    assert rel < 1e-6
    assert abs(td - t_av) / t_av < 1e-2 and ecc < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
