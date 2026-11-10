#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C12: procesos adiabaticos, isentropicos y politropicos de un gas ideal en un cilindro.

Consultado (2026-11-10): NASA Glenn, relaciones isentropicas y primera ley (E2 - E1 = Q - W); segunda ley (S_f = S_i si es reversible).
ESTANDAR (no consultado): p v^g = cte, T v^(g-1) = cte, T p^((1-g)/g) = cte; trabajo w = (p1 v1 - p2 v2)/(g - 1) por kg;
proceso politropico p v^n = cte con n = ln(p2/p1)/ln(v1/v2).
ILUSTRATIVOS (sinteticos, no medidos): aire gamma = 1.4, R = 287.05 J/(kg K); estado inicial 300 K y 100000 Pa; relacion de volumenes 10;
politropico con n = 1.25; isotermo n = 1.
Via 2: integracion numerica (RK4) de dT/dv = -(p/cv) = -(R T/(cv v)) para el proceso adiabatico reversible, frente a la forma cerrada.
Via 3: trabajo recibido por integral numerica de p dv (punto medio, 200000 pasos).
Tolerancias: T final por RK4 frente a cerrada < 1e-9 relativa; trabajo por integral < 1e-8 relativa.
"""
import math, platform

G, R = 1.4, 287.05
CV = R / (G - 1)
T1, P1, RV = 300.0, 100000.0, 10.0


def rk4_adiabatico(t0, v0, v1, n=2000):
    h = (v1 - v0) / n
    f = lambda v, t: -(R * t) / (CV * v)
    t, v = t0, v0
    for _ in range(n):
        k1 = f(v, t)
        k2 = f(v + h / 2, t + h * k1 / 2)
        k3 = f(v + h / 2, t + h * k2 / 2)
        k4 = f(v + h, t + h * k3)
        t += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        v += h
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    v1 = R * T1 / P1
    v2 = v1 / RV
    print(f"Aire ILUSTRATIVO: gamma = {G}, estado 1: T = {T1} K, p = {P1:.0f} Pa, v = {v1:.4f} m3/kg ; compresion a v2 = v1/{RV:.0f}")
    print(" proceso        n      T2 [K]     p2 [kPa]    w [kJ/kg]   w (integral p dv) [kJ/kg]   Delta s [J/(kg K)]")
    peor_w = 0.0
    filas = {}
    for nombre, n in (("isotermo", 1.0), ("politropico", 1.25), ("isentropico", G)):
        p2 = P1 * RV ** n
        t2 = p2 * v2 / R
        if abs(n - 1.0) < 1e-12:
            w = P1 * v1 * math.log(RV)
        else:
            w = (p2 * v2 - P1 * v1) / (n - 1.0)  # trabajo recibido por el gas, positivo en compresion
        # trabajo recibido = integral de p dv entre v2 y v1 con p = P1 (v1/v)^n
        s = 0.0
        m_ = 200000
        h = (v1 - v2) / m_
        for i in range(m_):
            v = v2 + (i + 0.5) * h
            s += P1 * (v1 / v) ** n * h
        peor_w = max(peor_w, abs(s - w) / abs(w))
        ds = (G * R / (G - 1)) * math.log(t2 / T1) - R * math.log(p2 / P1)
        filas[nombre] = (t2, p2, w)
        print(f" {nombre:12s} {n:5.2f}  {t2:8.2f}   {p2 / 1e3:9.1f}    {w / 1e3:8.3f}        {s / 1e3:8.3f}                   {ds:9.3f}")
    t_rk = rk4_adiabatico(T1, v1, v2)
    t_cer = T1 * RV ** (G - 1)
    err = abs(t_rk - t_cer) / t_cer
    print(f"Isentropico: T2 cerrada = {t_cer:.4f} K ; T2 por RK4 (primera ley, dT = -p dv / cv) = {t_rk:.4f} K ; diferencia = {err:.2e}")
    w_cv = CV * (filas['isentropico'][0] - T1)
    print(f"Trabajo isentropico por cv (T2 - T1) = {w_cv / 1e3:.3f} kJ/kg")
    # el isotermo exige extraer calor
    q_iso = -filas["isotermo"][2]
    print(f"Isotermo: calor cedido = {-q_iso / 1e3:.3f} kJ/kg ; ahorro de trabajo frente al isentropico = {(filas['isentropico'][2] - filas['isotermo'][2]) / 1e3:.3f} kJ/kg")
    assert err < 1e-9 and peor_w < 1e-8
    assert abs(w_cv - filas["isentropico"][2]) / w_cv < 1e-12
    print("Pruebas superadas.")


main()
