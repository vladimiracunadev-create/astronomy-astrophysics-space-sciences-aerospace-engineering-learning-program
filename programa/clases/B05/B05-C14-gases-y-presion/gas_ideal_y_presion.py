#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C14: gas ideal, presión y atmósfera isoterma.

Datos PUBLICADOS: R = 8,314 462 618... J/(mol K) y k_B = 1,380 649e-23 J/K (CODATA 2022);
g_n = 9,806 65 m/s² (CODATA 2022); presión media en superficie 1014 mb y temperatura media
288 K (NASA NSSDC, Earth Fact Sheet, act. 15-nov-2024). SUPUESTO sin fuente consultada:
masa molar del aire 0,028 965 kg/mol. Modelo: gas ideal; atmósfera isoterma en equilibrio
hidrostático dp/dz = -rho g con g constante. Escotilla y volúmenes SINTÉTICOS. Dominio de
validez: unas decenas de km, T constante (la atmósfera real no lo es).
Tolerancias: 1e-4 relativa entre la integración numérica y p0 exp(-z/H).
"""
from __future__ import annotations
import math
import sys

R_GAS = 8.314462618
KB = 1.380649e-23
GN = 9.80665
P0 = 1014e2           # Pa (1014 mb)
T0 = 288.0            # K
M_AIRE = 0.028965     # kg/mol (supuesto)

def densidad(p: float, T: float, M: float = M_AIRE) -> float:
    return p * M / (R_GAS * T)

def presion_numerica(z_fin: float, n: int = 20_000) -> float:
    """Integra dp/dz = -(p M g)/(R T) con RK4."""
    h = z_fin / n
    k = M_AIRE * GN / (R_GAS * T0)
    p = P0
    for _ in range(n):
        k1 = -k * p
        k2 = -k * (p + 0.5 * h * k1)
        k3 = -k * (p + 0.5 * h * k2)
        k4 = -k * (p + h * k3)
        p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return p

def main() -> int:
    H = R_GAS * T0 / (M_AIRE * GN)
    for z in (1_000.0, 8_000.0, 20_000.0):
        pn, pa = presion_numerica(z), P0 * math.exp(-z / H)
        assert abs(pn - pa) / pa < 1e-4, (z, pn, pa)
    # ley de Boyle: p V constante a T constante
    p2 = P0 * 2.0 / 1.0
    assert abs(p2 * 1.0 - P0 * 2.0) < 1e-6
    rho = densidad(P0, T0)
    n_v = P0 / (KB * T0)
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Densidad del aire (supuesto M) a 1014 mb y 288 K: {rho:.4f} kg/m³")
    print(f"Moléculas por m³ = p/(k T) = {n_v:.4e}")
    print(f"Altura de escala isoterma H = R T/(M g) = {H:.0f} m")
    for z in (1_000.0, 8_000.0, 20_000.0, 100_000.0):
        print(f"  z = {z/1e3:6.1f} km: p = {P0*math.exp(-z/H):10.2f} Pa ({P0*math.exp(-z/H)/P0:.4f} de p0)")
    A = 0.50
    print(f"Fuerza sobre una escotilla sintética de {A} m² con 101,4 kPa de diferencia: {P0*A:.0f} N ({P0*A/GN:.0f} kgf)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
