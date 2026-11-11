#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C03: gas que consume una esclusa por ciclo, recuperacion de gas y tiempo de bombeo (gas ideal).

Datos consultados (2026-11-10): Stromgren et al. (2023, IEEE Aerospace): volumen de esclusa supuesto de 15 m3 (y ~13 m3 en el resumen del bombeo), cabina a 8.2 psi con 34 % de O2
(Burke et al. 2022), recuperacion del 90 % del gas con un tiempo de bombeo de 35 min para 13 m3, dos EVA de dos tripulantes por semana, masa anual de fluidos
(esclusa con recuperacion 510 kg; sin recuperacion 861 kg). R = 8.314462618 J/(mol K) (NIST CODATA 2022).
ILUSTRATIVOS / NO CONSULTADOS: T = 294.15 K; masas molares O2 31.998 y N2 28.014 g/mol (mezcla O2/N2 sin otros gases); 1 psi = 6894.757 Pa (conversion definida, no consultada);
diametro de escotilla 0.8 m. Modelo: m = P V M/(R T) por llenado; perdida neta por ciclo = m (1 - eta); bombeo exponencial P = P0 exp(-t/tau) con tau = t90/ln 10 y velocidad de bombeo S = V/tau.
Segunda via: integracion numerica de Euler del bombeo (paso 1 s) frente a la formula analitica (tolerancia 0.5 %); balance de masa recuperado + venteado = llenado (tolerancia 1e-9).
Unidades: presion [Pa], volumen [m3], masa [kg], tiempo [min], fuerza [kN].
"""
from __future__ import annotations
import math, platform

R = 8.314462618
PSI = 6894.757
P_CAB = 8.2 * PSI
T = 294.15
X_O2 = 0.34
M = X_O2 * 0.031998 + (1 - X_O2) * 0.028014
ETA = 0.90
CICLOS = 2 * 52  # dos EVA por semana durante un ano (Stromgren et al. 2023)
T90 = 35.0  # min para recuperar el 90 % con V = 13 m3
PUB_CON, PUB_SIN = 510.0, 861.0  # kg/ano (Tabla 2 de Stromgren et al. 2023, esclusa)


def masa_llenado(v):
    return P_CAB * v * M / (R * T)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Cabina 8.2 psi = {P_CAB:.0f} Pa ; 34 % O2 ; M = {M * 1000:.3f} g/mol ; T = {T} K (ILUSTRATIVO)")
    rho = P_CAB * M / (R * T)
    print(f"Densidad del gas de cabina = {rho:.4f} kg/m3")
    print(" V [m3]  masa por llenado [kg]  perdida neta/ciclo con 90 % recuperado [kg]  anual sin recuperar [kg]  anual con 90 % [kg]")
    for v in (13.0, 15.0):
        m = masa_llenado(v)
        print(f"{v:6.1f} {m:20.3f} {m * (1 - ETA):42.3f} {m * CICLOS:26.1f} {m * (1 - ETA) * CICLOS:18.1f}")
        assert abs(m * ETA + m * (1 - ETA) - m) < 1e-9
    ahorro_pub = PUB_SIN - PUB_CON
    m_impl = ahorro_pub / (ETA * CICLOS)
    print(f"Ahorro publicado con recuperacion = {ahorro_pub:.0f} kg/ano -> masa por ciclo implicita = {m_impl:.3f} kg -> volumen equivalente = {m_impl / rho:.2f} m3")
    tau = T90 / math.log(10)
    s = 13.0 / tau
    print(f"Bombeo: tau = {tau:.2f} min ; velocidad de bombeo = {s:.3f} m3/min (modelo exponencial, ILUSTRATIVO)")
    for frac in (0.90, 0.99):
        print(f"   tiempo para retirar el {frac * 100:.0f} % = {-tau * math.log(1 - frac):.1f} min")
    # segunda via: Euler
    p, t, dt = 1.0, 0.0, 1.0 / 60.0
    while p > 0.1:
        p -= p * dt / tau
        t += dt
    print(f"Euler (paso 1 s): 90 % retirado en {t:.2f} min frente a {T90:.2f} min analitico")
    assert abs(t - T90) / T90 < 0.005
    f = P_CAB * math.pi / 4 * 0.8 ** 2 / 1000
    print(f"Fuerza sobre una escotilla de 0.8 m con cabina a 8.2 psi y vacio fuera = {f:.1f} kN")
    assert m_impl / rho < 13.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
