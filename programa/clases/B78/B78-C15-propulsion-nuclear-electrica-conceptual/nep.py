#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C15: carga util frente a velocidad de escape en un sistema electrico con planta de potencia (NEP) conceptual.

Datos CONSULTADOS (2026-11-10): g0 = 9.80665 m/s2 (NIST); la pagina de Dawn (NASA/JPL) indica que sus paneles podian generar mas de 10 kW en la Tierra (solo para dar orden de magnitud).
ILUSTRATIVOS (sinteticos, NO de un diseno ni de un reactor): masa especifica de la planta de potencia alpha = 20 kg/kW, eficiencia total del propulsor eta = 0.6,
tiempo de empuje 300 dias, Delta-v = 5000 m/s (y 15000 m/s en la comparacion). Se ignoran estructura, tanques y radiadores aparte de alpha.
Modelo: fraccion de propelente f_p = 1 - exp(-dv/Ve); potencia P = m_p Ve^2/(2 eta t); masa de la planta m_pow = alpha P;
fraccion util pi = 1 - f_p - m_pow/m0 = 1 - f_p (1 + alpha Ve^2/(2 eta t)).
Velocidad caracteristica v_c = sqrt(2 eta t/alpha) ; pi(Ve) tiene un maximo interior.
Segunda via: maximo por seccion aurea frente a una malla fina; verificacion de que el maximo es interior (pi baja a ambos lados).
Tolerancia: Ve optimo de ambas vias dentro de 0.05 %.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
ALPHA, ETA, T = 20.0 / 1000.0, 0.6, 300 * 86400.0  # kg/W, -, s


def pi_util(ve, dv):
    fp = 1 - math.exp(-dv / ve)
    return 1 - fp * (1 + ALPHA * ve ** 2 / (2 * ETA * T))


def optimo(dv):
    a, b = 1000.0, 60000.0
    fi = (math.sqrt(5) - 1) / 2
    for _ in range(100):
        c, d = b - fi * (b - a), a + fi * (b - a)
        if pi_util(c, dv) > pi_util(d, dv):
            b = d
        else:
            a = c
    v = 0.5 * (a + b)
    # malla fina
    vm = max(range(1000, 60001, 10), key=lambda x: pi_util(float(x), dv))
    assert abs(v - vm) / v < 5e-4
    assert pi_util(v * 0.8, dv) < pi_util(v, dv) > pi_util(v * 1.2, dv)
    return v, pi_util(v, dv)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    vc = math.sqrt(2 * ETA * T / ALPHA)
    print(f"NEP ILUSTRATIVO: alpha = {ALPHA*1e3:.0f} kg/kW, eta = {ETA}, t = {T/86400:.0f} dias -> v_c = sqrt(2 eta t/alpha) = {vc:.0f} m/s")
    for dv in (5000.0, 15000.0):
        print(f"Delta-v = {dv:.0f} m/s:")
        print("   Isp [s]   Ve [m/s]   f_prop    P/m0 [W/kg]  m_planta/m0   fraccion util")
        for isp in (500.0, 1000.0, 2000.0, 3000.0, 5000.0, 8000.0):
            ve = isp * G0
            fp = 1 - math.exp(-dv / ve)
            p_esp = fp * ve ** 2 / (2 * ETA * T)
            print(f"  {isp:>8.0f} {ve:>10.0f} {fp:>8.4f} {p_esp:>12.2f} {ALPHA*p_esp:>12.4f} {pi_util(ve, dv):>14.4f}")
        v, pi = optimo(dv)
        print(f"  Optimo: Ve = {v:.0f} m/s ; Isp = {v/G0:.0f} s ; fraccion util = {pi:.4f} ; Ve/v_c = {v/vc:.3f}")
    # masa de una planta de 10 kW (orden de magnitud de los paneles de Dawn, consultado)
    print(f"Planta de 10 kW con alpha = {ALPHA*1e3:.0f} kg/kW: {10*ALPHA*1e3:.0f} kg (ILUSTRATIVO; Dawn: paneles de mas de 10 kW, consultado)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
