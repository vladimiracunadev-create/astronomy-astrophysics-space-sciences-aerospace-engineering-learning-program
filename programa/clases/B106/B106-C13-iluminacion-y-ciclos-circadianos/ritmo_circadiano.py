#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C13: un oscilador de fase para ver cuando la luz arrastra el ritmo circadiano.

Consultado (Scheer et al. 2007, PLoS ONE 2(8): e721): luz moderadamente brillante (~450 lux) durante parte del episodio de vigilia arrastro a los participantes a un dia de 24.65 h
(sol marciano) y a uno de 23.5 h. Modelo PROPIO e ILUSTRATIVO (no es el modelo del articulo): dphi/dt = w0 - eps L(t) sin(phi - phi_ref), con periodo intrinseco de 24.2 h
(ILUSTRATIVO), L(t) = 1 durante las primeras 16 h de cada dia de duracion T y 0 el resto, eps ILUSTRATIVO. Arrastre si el periodo medio del oscilador iguala a T con tolerancia de 0.01 h.
Verificacion: sin luz (eps = 0) el periodo es 24.2 h; la teoria de Adler da el borde de arrastre |w0 - w_T| = eps d (d = fraccion de luz) y la simulacion lo reproduce.
"""
from __future__ import annotations
import math
import platform
import numpy as np

TAU0, EPS, DUTY = 24.2, 0.03, 16.0 / 24.0  # h; rad/h


def periodo(T, eps=EPS, dias=150, dt=0.01):
    """Integra dphi/dt (Euler) durante `dias` dias de calentamiento y mide el periodo medio en 100 dias mas."""
    w0 = 2 * math.pi / TAU0
    phi = 0.0

    def avance(i0, n, phi):
        for i in range(i0, i0 + n):
            tm = (i * dt) % T
            L = 1.0 if tm < DUTY * T else 0.0
            phi += dt * (w0 - eps * L * math.sin(phi - 2 * math.pi * tm / T))
        return phi

    n = int(dias * T / dt)
    phi = avance(0, n, phi)
    m = int(100 * T / dt)
    p1 = avance(n, m, phi)
    return 2 * math.pi / ((p1 - phi) / (m * dt))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: modelo propio ILUSTRATIVO (periodo 24.2 h, eps 0.03 rad/h); el arrastre a 24.65 h y 23.5 h es el resultado CONSULTADO de Scheer et al. (2007)")
    R = {}
    p0 = periodo(24.0, eps=0.0, dias=5)
    print(f"Sin luz (eps = 0): periodo {p0:.3f} h")
    assert abs(p0 - TAU0) < 0.01
    borde = EPS * DUTY
    w0 = 2 * math.pi / TAU0
    # Adler: |w0 - 2pi/T| <= eps*duty
    T_lo = 2 * math.pi / (w0 + borde)
    T_hi = 2 * math.pi / (w0 - borde)
    R["T_lo"], R["T_hi"] = T_lo, T_hi
    print(f"Adler: arrastre esperado para T entre {T_lo:.2f} h y {T_hi:.2f} h (ancho {T_hi-T_lo:.2f} h)")
    print("   T [h]   periodo simulado [h]   arrastrado   (Adler)")
    res = {}
    ok = 0
    for T in (22.0, 23.0, 23.5, 24.0, 24.2, 24.65, 25.5, 26.0, 27.0):
        p = periodo(T, dias=150)
        lock = abs(p - T) < 0.01
        res[T] = (p, lock)
        pred = T_lo <= T <= T_hi
        ok += (lock == pred)
        print(f"   {T:5.2f}   {p:18.3f}   {'si' if lock else 'no':>9}   {'si' if pred else 'no'}")
    R["ok"], R["n"] = ok, len(res)
    R["lock_2465"], R["lock_235"], R["lock_22"] = res[24.65][1], res[23.5][1], res[22.0][1]
    R["p_22"], R["p_27"] = res[22.0][0], res[27.0][0]
    print(f"Coincidencia simulacion-Adler en {ok} de {len(res)} casos")
    assert ok >= len(res) - 1
    assert res[24.65][1] and res[23.5][1] and not res[27.0][1]
    sol = 24 + 39 / 60 + 35 / 3600
    R["sol"] = sol
    print(f"Sol marciano: {sol:.4f} h ({(sol-24)*60:.1f} min mas que 24 h); retraso acumulado en 30 dias: {(sol-24)*30:.1f} h")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
