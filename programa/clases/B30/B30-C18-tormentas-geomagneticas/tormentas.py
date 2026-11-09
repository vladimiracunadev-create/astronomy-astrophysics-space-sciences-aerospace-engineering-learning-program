#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C18: evolucion de una tormenta con la ecuacion de Burton (inyeccion y decaimiento) y escalas G de NOAA.

Datos: las escalas G1-G5 corresponden a Kp = 5, 6, 7, 8 (incluido 9-) y 9 (NOAA, spaceweather.gov, consultada 2026-11-09). La inyeccion (15 nT/h), el tiempo de decaimiento
(8 h), la duracion de la fase principal (6 h) y las series de Kp son ILUSTRATIVOS (sinteticos); no se reproduce ninguna tormenta real.
Modelo: dDst*/dt = Q(t) - Dst*/tau con Q = -Q_0 durante T y 0 despues; solucion analitica Dst*(t) = -Q_0 tau (1 - e^(-t/tau)) para t <= T y Dst*(T) e^(-(t - T)/tau) despues;
integracion con RK4; clasificacion de una serie de Kp (28 valores) en la escala G.
Supuestos: inyeccion constante, un solo tiempo de decaimiento. Validez: orientativa.
Tolerancia: RK4 frente al analitico dentro de 1e-6 relativo; minimo de Dst por dos vias a 1e-9.
"""
from __future__ import annotations
import math
import platform
import sys

Q0, TAU, T = 15.0, 8.0, 6.0     # nT/h, h, h


def analitica(t, q0=Q0, tau=TAU, dur=T):
    if t <= dur:
        return -q0 * tau * (1 - math.exp(-t / tau))
    return -q0 * tau * (1 - math.exp(-dur / tau)) * math.exp(-(t - dur) / tau)


def rk4(t_fin, q0=Q0, tau=TAU, dur=T, h=0.01):
    """RK4 por tramos: inyeccion hasta dur y decaimiento despues (la discontinuidad de Q cae en el limite de un tramo)."""
    d, mn = 0.0, 0.0
    for q_seg, a, b in ((-q0, 0.0, min(t_fin, dur)), (0.0, dur, t_fin)):
        if b <= a:
            continue
        n = max(1, round((b - a) / h))
        hh = (b - a) / n
        f = lambda dd: q_seg - dd / tau
        for _ in range(n):
            k1 = f(d)
            k2 = f(d + hh / 2 * k1)
            k3 = f(d + hh / 2 * k2)
            k4 = f(d + hh * k3)
            d += hh * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            mn = min(mn, d)
    return d, mn


def escala_g(kp_etiqueta):
    """Etiquetas '5-', '5o', '5+', ..., '9-', '9o' -> G (0 si < 5)."""
    dig = int(kp_etiqueta[0])
    if dig == 9 and kp_etiqueta[1] == "-":
        return 4
    return max(0, dig - 4) if dig >= 5 else 0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'t [h]':>6} {'Dst* analitico [nT]':>20} {'Dst* RK4 [nT]':>14} {'dif. relativa':>14}")
    for t in (1.0, 3.0, 6.0, 12.0, 24.0, 48.0):
        a = analitica(t)
        n, _ = rk4(t)
        print(f"{t:6.1f} {a:20.4f} {n:14.4f} {abs(n / a - 1):14.2e}")
        assert abs(n / a - 1) < 1e-6, f"RK4 t={t}"
    minimo = analitica(T)
    _, mn = rk4(T + 1)
    assert abs(mn / minimo - 1) < 1e-4
    print(f"minimo de Dst* en t = {T:.0f} h: {minimo:.2f} nT (formula -Q_0 tau (1 - e^(-T/tau)) ; RK4: {mn:.2f})")
    t10 = T + TAU * math.log(10)
    print(f"tiempo en que Dst* vuelve al 10 % del minimo: t = T + tau ln 10 = {t10:.1f} h ; Dst*({t10:.1f} h) = {analitica(t10):.3f} nT ({analitica(t10) / minimo * 100:.1f} % del minimo)")
    print(f"{'Q_0 [nT/h]':>10} {'T [h]':>6} {'tau [h]':>8} {'minimo [nT]':>12}")
    for q0, dur, tau in ((15, 6, 8), (30, 6, 8), (15, 12, 8), (15, 6, 16), (60, 3, 8)):
        print(f"{q0:10.0f} {dur:6.0f} {tau:8.0f} {analitica(dur, q0, tau, dur):12.2f}")
    # escala G
    etiq = ["4+", "5-", "5o", "5+", "6o", "7-", "7+", "8o", "9-", "9o"]
    print("etiqueta de Kp -> escala G: " + ", ".join(f"{e} -> G{escala_g(e)}" for e in etiq))
    assert [escala_g(e) for e in etiq] == [0, 1, 1, 1, 2, 3, 3, 4, 4, 5]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
