#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C10: primera ley para volumenes de control - flujo estacionario y llenado de un deposito.

Consultado (2026-11-10): NASA Glenn, primera ley E2 - E1 = Q - W (cambio de energia = calor - trabajo realizado).
ESTANDAR (no consultado): balance de volumen de control en flujo estacionario Q - W = m [(h2 - h1) + (V2^2 - V1^2)/2];
para un gas ideal calorico h = cp T; llenado de un deposito inicialmente vacio con T_final = gamma T_linea.
ILUSTRATIVOS (sinteticos, no medidos): aire con gamma = 1.4, R = 287.05 J/(kg K), cp = 1004.675 J/(kg K);
compresor: m = 2 kg/s, T1 = 300 K, relacion de presiones 8, rendimiento isentropico 0.85;
turbina: m = 2 kg/s, T3 = 1400 K, relacion de presiones 6, rendimiento isentropico 0.88; tobera: T1 = 900 K, caida isentropica a 600 K.
Via 2 (compresor/turbina isentropicos): trabajo como integral de v dp calculada numericamente.
Via 2 (deposito): integracion numerica de dm/dt = m_in y d(m u)/dt = m_in h_linea.
Tolerancias: trabajo por integral frente a entalpia < 1e-6 relativa; T final del deposito frente a gamma T_linea < 1e-9.
"""
import math, platform

G, R = 1.4, 287.05
CP = G * R / (G - 1)
CV = CP - R


def comp_ideal(t1, pr):
    return t1 * pr ** ((G - 1) / G)


def trabajo_vdp(t1, p1, pr, n=20000):
    """w_ideal = integral v dp con p v^g = cte, entre p1 y pr p1 (punto medio en ln p)."""
    v1 = R * t1 / p1
    s = 0.0
    lp0, lp1 = math.log(p1), math.log(pr * p1)
    h = (lp1 - lp0) / n
    for i in range(n):
        p = math.exp(lp0 + (i + 0.5) * h)
        v = v1 * (p1 / p) ** (1 / G)
        s += v * p * h
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Aire ILUSTRATIVO: gamma = {G}, R = {R} J/(kg K), cp = {CP:.3f} J/(kg K)")
    m = 2.0
    # compresor
    t1, pr, eta = 300.0, 8.0, 0.85
    t2s = comp_ideal(t1, pr)
    w_s = CP * (t2s - t1)
    w_vdp = trabajo_vdp(t1, 101325.0, pr)
    t2 = t1 + (t2s - t1) / eta
    w_real = CP * (t2 - t1)
    print(f"Compresor: T2s = {t2s:.2f} K ; w_ideal (entalpia) = {w_s / 1e3:.3f} kJ/kg ; w_ideal (integral v dp) = {w_vdp / 1e3:.3f} kJ/kg")
    print(f"           T2 real = {t2:.2f} K ; w_real = {w_real / 1e3:.3f} kJ/kg ; potencia = {m * w_real / 1e3:.2f} kW")
    d1 = abs(w_vdp - w_s) / w_s
    # turbina
    t3, prt, etat = 1400.0, 6.0, 0.88
    t4s = t3 * prt ** (-(G - 1) / G)
    t4 = t3 - etat * (t3 - t4s)
    w_t = CP * (t3 - t4)
    print(f"Turbina:   T4s = {t4s:.2f} K ; T4 real = {t4:.2f} K ; w = {w_t / 1e3:.3f} kJ/kg ; potencia = {m * w_t / 1e3:.2f} kW")
    # balance del volumen de control (adiabatico): Q = 0 y verificacion
    q_ctrl = m * (CP * t4 - CP * t3) + m * w_t
    print(f"           balance adiabatico: m(h4 - h3) + W = {q_ctrl:.3e} W")
    # tobera
    t1n, t2n = 900.0, 600.0
    v2 = math.sqrt(2 * CP * (t1n - t2n))
    print(f"Tobera:    V2 = {v2:.2f} m/s (h1 = h2 + V2^2/2, V1 = 0)")
    # estrangulamiento
    print("Valvula (estrangulamiento adiabatico, gas ideal): h2 = h1, por tanto T2 = T1")
    # deposito
    t_line = 300.0
    m_t, u_t = 0.0, 0.0  # energia interna total
    dt, mdot = 1e-3, 0.1
    for _ in range(int(2.0 / dt)):
        m_t += mdot * dt
        u_t += mdot * CP * t_line * dt
    t_fin = u_t / (m_t * CV)
    print(f"Deposito (inicialmente vacio) llenado desde la linea a {t_line} K: T_final = {t_fin:.4f} K ; gamma T_linea = {G * t_line:.4f} K")
    assert d1 < 1e-6
    assert abs(q_ctrl) < 1e-6
    assert abs(t_fin - G * t_line) < 1e-9
    print("Pruebas superadas.")


main()
