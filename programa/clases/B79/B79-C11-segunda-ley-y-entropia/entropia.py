#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C11: segunda ley y entropia generada en componentes de un motor.

Consultado (2026-11-10): NASA Glenn, segunda ley: Delta S = Delta Q / T; S_f = S_i (reversible), S_f > S_i (irreversible);
ejemplo de transferencia de calor entre dos objetos con temperaturas medias T_h = (T1 + T_f)/2 y T_c = (T2 + T_f)/2.
ESTANDAR (no consultado): para gas ideal calorico ds = cp ln(T2/T1) - R ln(p2/p1); trabajo perdido (Gouy-Stodola) W_perdido = T0 s_gen.
ILUSTRATIVOS (sinteticos, no medidos): aire gamma = 1.4, R = 287.05 J/(kg K); compresor 300 K, relacion 8, eta 0.85;
turbina 1400 K, relacion 6, eta 0.88; valvula 8 -> 1 de presion; dos cuerpos con m c = 1000 J/K a 400 K y 300 K; T0 = 300 K.
Via 2: s por integral numerica de cp dT/T - R dp/p sobre un camino de dos tramos (isobaro + isotermo); balance de entropia del par de cuerpos con ln exacto.
Tolerancias: integral frente a cerrada < 1e-9 relativa.
"""
import math, platform

G, R = 1.4, 287.05
CP = G * R / (G - 1)
T0 = 300.0


def ds(t1, p1, t2, p2):
    return CP * math.log(t2 / t1) - R * math.log(p2 / p1)


def ds_integral(t1, p1, t2, p2, n=20000):
    """Camino: primero isobaro a p1 de t1 a t2, luego isotermo a t2 de p1 a p2."""
    s = 0.0
    h = (t2 - t1) / n
    for i in range(n):
        t = t1 + (i + 0.5) * h
        s += CP * h / t
    lp = math.log(p2 / p1) / n  # tramo isotermo: ds = -R dp/p = -R d(ln p)
    for _ in range(n):
        s += -R * lp
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Aire ILUSTRATIVO: cp = {CP:.3f} J/(kg K), R = {R} J/(kg K), T0 = {T0} K")
    peor = 0.0
    # compresor
    t1, p1, pr, eta = 300.0, 1.0, 8.0, 0.85
    t2s = t1 * pr ** ((G - 1) / G)
    t2 = t1 + (t2s - t1) / eta
    sg_c = ds(t1, p1, t2, pr * p1)
    peor = max(peor, abs(sg_c - ds_integral(t1, p1, t2, pr * p1)) / abs(sg_c))
    print(f"Compresor: s_gen = {sg_c:.3f} J/(kg K) ; trabajo perdido T0 s_gen = {T0 * sg_c / 1e3:.3f} kJ/kg ; isentropico s_gen = {ds(t1, p1, t2s, pr * p1):.2e}")
    # turbina
    t3, prt, et = 1400.0, 6.0, 0.88
    t4s = t3 * prt ** (-(G - 1) / G)
    t4 = t3 - et * (t3 - t4s)
    sg_t = ds(t3, prt, t4, 1.0)
    peor = max(peor, abs(sg_t - ds_integral(t3, prt, t4, 1.0)) / abs(sg_t))
    print(f"Turbina:   s_gen = {sg_t:.3f} J/(kg K) ; trabajo perdido T0 s_gen = {T0 * sg_t / 1e3:.3f} kJ/kg")
    # valvula
    sg_v = ds(300.0, 8.0, 300.0, 1.0)
    print(f"Valvula 8 -> 1: s_gen = {sg_v:.3f} J/(kg K) ; = -R ln(1/8) = {R * math.log(8.0):.3f}")
    # calor entre dos cuerpos
    c1, th, tc = 1000.0, 400.0, 300.0
    tf = 0.5 * (th + tc)
    q = c1 * (th - tf)
    s_exacta = c1 * math.log(tf / th) + c1 * math.log(tf / tc)
    s_nasa = -q / (0.5 * (th + tf)) + q / (0.5 * (tc + tf))
    print(f"Dos cuerpos (m c = {c1:.0f} J/K): Tf = {tf:.1f} K ; Q = {q / 1e3:.1f} kJ ; S_gen exacta = {s_exacta:.3f} J/K ; con temperaturas medias = {s_nasa:.3f} J/K")
    print(f" error del metodo de temperaturas medias = {100 * (s_nasa - s_exacta) / s_exacta:.2f} %")
    # calor de cuerpo caliente a frio con DeltaT pequeno: sg -> 0
    for dt_ in (100.0, 10.0, 1.0):
        thh, tcc = 300.0 + dt_, 300.0
        tff = 0.5 * (thh + tcc)
        s = c1 * math.log(tff / thh) + c1 * math.log(tff / tcc)
        print(f" salto inicial de {dt_:6.1f} K: S_gen = {s:.6f} J/K")
    assert peor < 1e-9
    assert sg_c > 0 and sg_t > 0 and sg_v > 0 and s_exacta > 0
    assert abs(ds(t1, p1, t2s, pr * p1)) < 1e-9
    print("Pruebas superadas.")


main()
