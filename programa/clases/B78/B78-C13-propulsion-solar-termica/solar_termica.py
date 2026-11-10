#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C13: propulsion solar termica (hidrogeno calentado con luz solar concentrada), balance de energia.

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K), g0 = 9.80665 m/s2 (NIST CODATA); luminosidad solar 382.8e24 W y distancia 149.6e6 km (NASA/NSSDC, Sun Fact Sheet).
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): masa molar del H2 = 2.016 g/mol, gamma = 1.40, temperatura de entrada 300 K.
ILUSTRATIVOS (sinteticos, no de un diseno): area del colector 100 m2, eficiencia optica 0.70, eficiencia de absorcion termica 0.80,
temperatura del gas 2500 K (limite de materiales supuesto), razon de presiones pc/pe = 100, masa de nave 500 kg, Delta-v 1000 m/s.
Modelo: P_th = I A eta_o eta_t ; ṁ = P_th/(cp (T - T0)) ; Ve isentropico (como en C03) ; F = ṁ Ve ; gas ideal de cp constante.
Segunda via: balance de energia, P_jet = (1/2) ṁ Ve^2 no puede superar la entalpia aportada ṁ cp (T - T0).
Tolerancia: P_jet <= P_th (eficiencia de tobera < 1) y F = 2 P_jet/Ve con 1e-12.
"""
from __future__ import annotations
import math, platform

R, G0 = 8.314462618, 9.80665
L_SUN, AU = 382.8e24, 149.6e9
M_H2, GAMMA, T0 = 2.016e-3, 1.40, 300.0
A, ETA_O, ETA_T, T, RZ = 100.0, 0.70, 0.80, 2500.0, 100.0


def ve(t, m=M_H2, g=GAMMA, rz=RZ):
    return math.sqrt(2 * g / (g - 1) * R * t / m * (1 - rz ** (-(g - 1) / g)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    i = L_SUN / (4 * math.pi * AU ** 2)
    p_th = i * A * ETA_O * ETA_T
    cp = GAMMA * R / ((GAMMA - 1) * M_H2)
    md = p_th / (cp * (T - T0))
    v = ve(T)
    f = md * v
    pj = 0.5 * md * v ** 2
    assert pj <= p_th and abs(f - 2 * pj / v) / f < 1e-12
    print(f"I a 1 UA = {i:.1f} W/m2 ; P_th = {p_th/1e3:.2f} kW (A = {A:.0f} m2, eta_o = {ETA_O}, eta_t = {ETA_T}; ILUSTRATIVOS)")
    print(f"cp(H2) = {cp:.0f} J/(kg K) ; mdot = {md*1e3:.3f} g/s ; Ve = {v:.0f} m/s ; Isp = {v/G0:.1f} s ; F = {f:.2f} N")
    print(f"Potencia del chorro = {pj/1e3:.2f} kW ; eficiencia de tobera P_jet/P_th = {pj/p_th:.3f}")
    print("Efecto de la temperatura del gas (misma P_th):")
    print("  T [K]   Ve [m/s]  Isp [s]   mdot [g/s]   F [N]")
    prev = None
    for t in (1500.0, 2000.0, 2500.0, 3000.0):
        vv = ve(t)
        mm = p_th / (cp * (t - T0))
        ff = mm * vv
        assert prev is None or vv > prev
        prev = vv
        print(f" {t:>6.0f} {vv:>10.0f} {vv/G0:>8.1f} {mm*1e3:>11.3f} {ff:>8.2f}")
    # tiempo de empuje y propelente para dv = 1000 m/s con 500 kg
    m0, dv = 500.0, 1000.0
    mp = m0 * (1 - math.exp(-dv / v))
    t_emp = mp / md
    print(f"Delta-v 1000 m/s con 500 kg: propelente = {mp:.2f} kg ; tiempo de empuje = {t_emp/3600:.2f} h ; aceleracion inicial = {f/m0*1e3:.1f} mm/s2")
    # comparacion con un electrico de Isp 3000 s y eta 0.6 alimentado por la misma P_th (ILUSTRATIVO)
    ve_e = 3000.0 * G0
    f_e = 2 * 0.6 * p_th / ve_e
    mp_e = m0 * (1 - math.exp(-dv / ve_e))
    print(f"Electrico ILUSTRATIVO (Isp 3000 s, eta 0.6) con la misma potencia: F = {f_e:.2f} N ; propelente = {mp_e:.2f} kg ; tiempo = {mp_e/(f_e/ve_e)/3600:.2f} h")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
