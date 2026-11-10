#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C04: vida util de un deposito (Arrhenius) y evaporacion de un criogeno.

Constante R = 8.314462618 J/(mol K) (valor exacto del SI; no consultado en esta sesion).
ILUSTRATIVOS (no consultados, no medidos): suministro con constante de degradacion k_ref = 1.0e-3 1/d a T_ref = 293.15 K y Ea = 80 kJ/mol;
umbral de vida util: 90 % de la potencia inicial (t90 = ln(1/0.9)/k). Criogeno: 5000 kg de oxigeno liquido, calor de vaporizacion 213 kJ/kg,
fugas termicas de 5 W y 20 W (estimaciones ilustrativas), 180 d.
Segunda via: integracion numerica de dP/dt = -k P con paso de 0.01 d frente a la solucion exponencial. Tolerancia: 1e-4 relativa.
"""
from __future__ import annotations
import math
import platform

R = 8.314462618
K_REF, T_REF, EA = 1.0e-3, 293.15, 80e3


def k_T(temp):
    return K_REF * math.exp(-EA / R * (1.0 / temp - 1.0 / T_REF))


def t90(temp):
    return math.log(1 / 0.9) / k_T(temp)


def potencia_numerica(k, t_fin, h=0.01):
    p, t = 1.0, 0.0
    while t < t_fin - 1e-12:
        p -= k * p * h
        t += h
    return p


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos ILUSTRATIVOS: k_ref = 1.0e-3 1/d a 293.15 K, Ea = 80 kJ/mol, umbral 90 %")
    print(" T [K]    k [1/d]      t90 [d]   t90 [anios]")
    t_res = {}
    for t in (277.15, 293.15, 313.15):
        t_res[t] = t90(t)
        print(f"{t:7.2f}  {k_T(t):10.3e}  {t_res[t]:9.1f}  {t_res[t] / 365.25:10.2f}")
    q10 = k_T(303.15) / k_T(293.15)
    print(f"Factor por +10 K (293.15 -> 303.15): {q10:.3f}")
    k = k_T(293.15)
    p_ana = math.exp(-k * 180.0)
    p_num = potencia_numerica(k, 180.0)
    print(f"Potencia a 180 d a 293.15 K: analitica {p_ana:.6f} ; numerica {p_num:.6f} ; dif. relativa {abs(p_num - p_ana) / p_ana:.2e}")
    print("Evaporacion del criogeno (5000 kg, h_fg = 213 kJ/kg):")
    perdidas = {}
    for q in (5.0, 20.0):
        m_dot = q / 213e3 * 86400.0  # kg/dia
        perd = m_dot * 180.0
        perdidas[q] = perd
        print(f"  fuga {q:5.0f} W: {m_dot:6.3f} kg/d ; en 180 d {perd:7.1f} kg ({perd / 5000.0 * 100:.1f} % del total)")
    assert abs(p_num - p_ana) / p_ana < 1e-4
    assert t_res[277.15] > t_res[293.15] > t_res[313.15]
    assert abs(perdidas[20.0] / perdidas[5.0] - 4.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
