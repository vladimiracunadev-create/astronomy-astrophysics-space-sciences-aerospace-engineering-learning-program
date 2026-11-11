#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B108-C03: par de apriete, reaccion y deriva de una herramienta en EVA (cuerpo rigido, SINTETICO).

CONSULTADOS (2026-11-10, solo resumen del registro): Poliner, Wilmington y Klute, NASA TP-3433 (NTRS 19940017154, 1993): fuerzas maximas de
aprox. 400 a 750 N segun orientacion y direccion del esfuerzo; razon de efectividad de la fuerza (FER) de 0.55 a 0.90.
Rajulu, Poliner y Klute, NASA TP-3424 (NTRS 19940016133, 1993): sin restriccion de pies, trabajar hacia el cuerpo es mas efectivo que alejarse.
ILUSTRATIVOS (sinteticos, no medidos): brazo de palanca L = 0.30 m, par de una herramienta electrica 20 N m durante 2 s,
momento de inercia del conjunto persona+traje respecto al eje de la herramienta I = 30 kg m2, masa total 150 kg,
empuje de 100 N durante 0.5 s, herramienta suelta de 1.5 kg con velocidad 0.05 m/s.
Modelo: cuerpo rigido libre (sin restriccion ni amortiguacion); tau = F L FER; alpha = tau/I; theta = alpha t^2/2.
Segunda via: integracion numerica semiimplicita (Euler simplectico) con dt = 1e-4 s. Tolerancia: angulo 1e-3 rad relativa 1e-3.
Unidades SI. Sistema de referencia: ejes del cuerpo, origen en el centro de masa; el par reactivo es opuesto al aplicado.
"""
from __future__ import annotations
import math, platform

L = 0.30
I = 30.0
M = 150.0


def par(f, fer, brazo=L):
    return f * brazo * fer


def rotacion_analitica(tau, inercia, t):
    a = tau / inercia
    return a, a * t, 0.5 * a * t * t


def rotacion_numerica(tau, inercia, t, dt=1e-4):
    w = th = 0.0
    for _ in range(int(round(t / dt))):
        w += tau / inercia * dt
        th += w * dt
    return w, th


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Par de apriete tau = F L FER, con L = 0.30 m (ILUSTRATIVO) y F, FER de TP-3433 (consultados)")
    print("  F [N]   FER    tau [N m]")
    for f, fer in ((400, 0.55), (400, 0.90), (750, 0.55), (750, 0.90)):
        print(f"  {f:5d}  {fer:4.2f}  {par(f, fer):8.1f}")
    tau, t = 20.0, 2.0
    a, w, th = rotacion_analitica(tau, I, t)
    wn, thn = rotacion_numerica(tau, I, t)
    print(f"Reaccion: herramienta de {tau:.0f} N m durante {t:.0f} s sobre I = {I:.0f} kg m2 (cuerpo libre, ILUSTRATIVO)")
    print(f"  analitica: alpha = {a:.4f} rad/s2, omega = {w:.4f} rad/s, theta = {th:.4f} rad = {math.degrees(th):.2f} grados")
    print(f"  numerica:  omega = {wn:.4f} rad/s, theta = {thn:.4f} rad; diferencia relativa en theta = {abs(thn - th)/th:.2e}")
    # empuje lineal
    f, ts = 100.0, 0.5
    dv = f * ts / M
    print(f"Empuje de {f:.0f} N durante {ts} s sobre {M:.0f} kg: dv = {dv:.4f} m/s; desplazamiento en 10 s = {dv*10:.2f} m")
    # conservacion de momento con una herramienta suelta
    m_t, v_t = 1.5, 0.05
    deriva10, deriva60 = v_t * 600.0, v_t * 3600.0
    print(f"Herramienta suelta de {m_t} kg a {v_t} m/s: deriva {deriva10:.0f} m en 10 min y {deriva60:.0f} m en 1 h")
    p_total = m_t * v_t + M * (-m_t * v_t / M)
    print(f"Momento lineal total tras lanzar la herramienta y retroceder el cuerpo = {p_total:.1e} kg m/s (se conserva)")
    # sensibilidad: inercia
    print("Rotacion tras 2 s segun la inercia (tau = 20 N m):")
    for ii in (15.0, 30.0, 60.0):
        print(f"  I = {ii:4.0f} kg m2 -> theta = {math.degrees(rotacion_analitica(tau, ii, t)[2]):6.2f} grados")
    assert abs(thn - th) / th < 1e-3 and abs(wn - w) / w < 1e-3 and abs(p_total) < 1e-12
    assert abs(par(750, 0.9) - 202.5) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
