#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B64-C04: actividad del agua de una salmuera y balance osmotico de una celula.

Datos: SINTETICOS e ILUSTRATIVOS. Coeficiente osmotico phi (constante por tramo), molalidades y fraccion de volumen
no osmotico (b = 0.25) son propuestos. Cualitativamente se apoya en Oren 2008 (resumen consultado el 2026-11-09,
Europe PMC): dos estrategias osmoticas, acumular KCl ("salt-in") o excluir sal y acumular solutos compatibles.
Modelo: a_w = exp(-nu m phi M_w), con nu = 2 (NaCl), m [mol/kg], M_w = 0.018015 kg/mol y phi el coeficiente osmotico.
Comparacion con la solucion ideal de Raoult por fraccion molar: a_w = n_w/(n_w + nu m n_w M_w) = 1/(1 + nu m M_w).
Presion osmotica: Pi = -(R T / V_w) ln a_w, con V_w = 1.8e-5 m3/mol (agua, aprox.) y R = 8.314462618 J/(mol K) (CODATA 2022,
NIST, consultado 2026-11-09). Cambio de volumen celular por choque hipoosmotico (Boyle-van't Hoff): V/V0 = b + (1-b) Pi0/Pi1.
Pruebas: (1) para m -> 0 ambas formas coinciden con a_w ~ 1 - nu m M_w phi (error relativo < 1e-3 en m = 0.01);
(2) integracion numerica (regla del trapecio, 2000 pasos) de ln a_w = -nu M_w int phi dm con phi constante frente a la forma cerrada;
(3) K+ interno de equilibrio: m_in tal que a_w(in) = a_w(out) coincide con la inversion analitica m = -ln a_w/(nu M_w phi).
Supuestos: soluciones diluidas a 298.15 K, ideal-no ideal solo via phi. Validez: ilustrativa; NO sustituye a modelos de Pitzer.
"""
from __future__ import annotations
import math, platform

R = 8.314462618
MW = 0.018015      # kg/mol
VW = 1.8e-5        # m3/mol
T = 298.15
NU = 2
B = 0.25           # fraccion de volumen no osmotico (sintetico)


def aw_phi(m, phi):
    return math.exp(-NU * m * phi * MW)


def aw_raoult(m):
    return 1.0 / (1.0 + NU * m * MW)


def pi_pa(aw):
    return -(R * T / VW) * math.log(aw)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS: phi constante por fila; NaCl (nu=2); T = 298.15 K")
    print(f"{'m [mol/kg]':>11} {'phi':>5} {'a_w (phi)':>10} {'a_w (Raoult)':>13} {'Pi [MPa]':>9}")
    for m, phi in ((0.01, 0.93), (0.5, 0.92), (2.0, 1.0), (4.0, 1.1), (6.0, 1.25)):
        print(f"{m:11.2f} {phi:5.2f} {aw_phi(m, phi):10.4f} {aw_raoult(m):13.4f} {pi_pa(aw_phi(m, phi)) / 1e6:9.2f}")
    # prueba 1: limite diluido
    m = 0.01
    lin = 1 - NU * m * MW * 1.0
    assert abs(aw_phi(m, 1.0) - lin) / lin < 1e-3 and abs(aw_raoult(m) - lin) / lin < 1e-3
    print(f"Prueba limite diluido (m=0.01): exp {aw_phi(m, 1.0):.6f} ; Raoult {aw_raoult(m):.6f} ; lineal {lin:.6f}")
    # prueba 2: integracion numerica
    phi, m = 1.1, 4.0
    n = 2000
    h = m / n
    integral = sum(0.5 * h * (phi + phi) for _ in range(n))
    aw_num = math.exp(-NU * MW * integral)
    assert abs(aw_num - aw_phi(m, phi)) < 1e-12
    print(f"Prueba integral: a_w numerica {aw_num:.8f} ; cerrada {aw_phi(m, phi):.8f}")
    # prueba 3: equilibrio de a_w
    aw_out = aw_phi(4.0, 1.1)
    m_in = -math.log(aw_out) / (NU * MW * 1.1)
    assert abs(aw_phi(m_in, 1.1) - aw_out) < 1e-12 and abs(m_in - 4.0) < 1e-9
    print(f"KCl interno de equilibrio con phi=1.1: {m_in:.3f} mol/kg (igual a la sal externa, estrategia 'salt-in')")
    # choque hipoosmotico
    pi0 = pi_pa(aw_out)
    print(f"Choque: celula equilibrada a Pi0 = {pi0 / 1e6:.2f} MPa que pasa a agua dulce (a_w=0.9999):")
    for aw1 in (0.95, 0.99, 0.9999):
        pi1 = pi_pa(aw1)
        print(f"  a_w externa {aw1}: Pi1 = {pi1 / 1e6:.3f} MPa ; V/V0 = {B + (1 - B) * pi0 / pi1:.2f} (celula sin pared: cota teorica)")
    print("Nota: V/V0 > 1 indica que una celula sin pared ni valvulas de salida estallaria; es la razon de las valvulas mecanosensibles.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
