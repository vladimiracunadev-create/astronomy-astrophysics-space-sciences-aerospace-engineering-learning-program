#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C21: erosion por pulverizacion y vida util de un propulsor electrico (modelo sintetico).

Datos CONSULTADOS (2026-11-10): e = 1.602176634e-19 C, u = 1.66053906892e-27 kg (NIST CODATA); Dawn (NASA/JPL): xenon 425 kg al lanzamiento, ~3.25 mg/s a empuje maximo, 91 mN por motor.
ILUSTRATIVOS (sinteticos, NO medidos ni de un material real): rendimiento de pulverizacion lineal Y(E) = a (E - E_th) con a = 0.002 atomos/(ion eV) y E_th = 30 eV;
energia de los iones que llegan a la pared E = 0.3 V_d ; densidad de corriente ionica a la pared j = 10 A/m2 ; densidad de la pared 2100 kg/m3 ;
masa atomica media 12.4 u ; espesor erosionable w = 2 mm ; la energia de impacto cae un 30 % al agotarse el espesor (pared que se retira).
Modelo: velocidad de recesion dz/dt = Y(E) (j/e) m_a/rho con E(z) = E0 (1 - 0.3 z/w) -> dz/dt = A - B z ; vida T = (1/B) ln(A/(A - B w)) si A > B w.
Segunda via: integracion numerica (Runge-Kutta de 4o orden) hasta z = w.
Tolerancia: la vida analitica y la numerica coinciden a 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

E_C, U = 1.602176634e-19, 1.66053906892e-27
A_Y, E_TH = 0.002, 30.0
J, RHO, MA, W = 10.0, 2100.0, 12.4 * U, 2e-3


def coef(vd):
    e0 = 0.3 * vd
    c = (J / E_C) * MA / RHO  # m/s por unidad de rendimiento
    a = c * A_Y * (e0 - E_TH)
    b = c * A_Y * e0 * 0.3 / W
    return a, b, e0


def vida_analitica(vd):
    a, b, e0 = coef(vd)
    if a <= 0:
        return math.inf
    if a - b * W <= 0:
        return math.inf
    return math.log(a / (a - b * W)) / b


def vida_rk4(vd, n=200000):
    a, b, _ = coef(vd)
    if a <= 0 or a - b * W <= 0:
        return math.inf
    t_est = vida_analitica(vd)
    h = t_est * 1.2 / n
    z, t = 0.0, 0.0
    f = lambda zz: a - b * zz
    while z < W:
        k1 = f(z); k2 = f(z + 0.5 * h * k1); k3 = f(z + 0.5 * h * k2); k4 = f(z + h * k3)
        znuevo = z + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        if znuevo >= W:
            return t + h * (W - z) / (znuevo - z)
        z, t = znuevo, t + h
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Modelo SINTETICO: Y(E) = 0.002 (E - 30 eV), E_impacto = 0.3 V_d, j = 10 A/m2, espesor 2 mm")
    print("  V_d [V]   E_impacto [eV]   Y [atomos/ion]   recesion inicial [nm/h]   vida [h]    vida [dias]")
    prev = math.inf
    for vd in (150.0, 200.0, 300.0, 450.0, 600.0):
        a, b, e0 = coef(vd)
        ta, tr = vida_analitica(vd), vida_rk4(vd)
        if math.isinf(ta):
            print(f" {vd:>8.0f} {e0:>15.1f}   por debajo del umbral (sin erosion en el modelo)")
            continue
        assert abs(ta - tr) / ta < 1e-6, (ta, tr)
        y = A_Y * (e0 - E_TH)
        print(f" {vd:>8.0f} {e0:>15.1f} {y:>16.4f} {a*3600*1e9:>25.2f} {ta/3600:>10.0f} {ta/86400:>11.1f}")
        assert ta < prev
        prev = ta
    # Dawn: cuanto dura el xenon si un solo motor lo consumiera a empuje maximo (calculo con datos consultados)
    md, f, xe = 3.25e-6, 0.091, 425.0
    t = xe / md
    print(f"Dawn (consultado): {xe:.0f} kg de xenon a {md*1e6:.2f} mg/s por un motor = {t/86400:.0f} dias ({t/86400/365.25:.1f} anos) de empuje maximo ; impulso = F t = {f*t:.3e} N s")
    print("Un requisito de vida impone un limite de proyecto: vida >= tiempo de empuje; aqui: vida del modelo a 300 V frente a ese tiempo:")
    ta = vida_analitica(300.0)
    print(f"  vida(300 V) = {ta/86400:.0f} dias ; cociente con el tiempo de consumo del xenon = {ta/t:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
