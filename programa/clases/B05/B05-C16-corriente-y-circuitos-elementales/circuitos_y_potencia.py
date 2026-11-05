#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C16: circuitos resistivos, balance de potencia y presupuesto de energía.

Datos: SINTÉTICOS (resistencias, fuente, paneles, cargas); flujo solar calculado desde datos
publicados de la NASA (Sun Fact Sheet: luminosidad 382,8e24 W; Earth Fact Sheet: semieje mayor
149,598e6 km, radio ecuatorial 6378,137 km). Modelo: circuito lineal resistivo en régimen
estacionario resuelto por análisis nodal (eliminación gaussiana); eclipse con sombra cilíndrica,
Sol en el infinito, órbita circular de ángulo beta = 0. Supuestos: fuentes ideales, sin
dependencia de temperatura, eficiencia constante. Dominio de validez: corriente continua.
Tolerancias: 1e-9 de residuo en las leyes de Kirchhoff; 1e-12 en el balance de potencia.
"""
from __future__ import annotations
import math
import sys

L_SOL = 382.8e24
A_TIERRA = 149.598e9
R_T = 6_378_137.0

def resolver(A: list[list[float]], b: list[float]) -> list[float]:
    n = len(b)
    M = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][c] * x[c] for c in range(i + 1, n))) / M[i][i]
    return x

def fraccion_eclipse(r: float) -> float:
    return math.asin(R_T / r) / math.pi

def main() -> int:
    # Fuente 12 V -> R1 (4 ohm) -> nodo A; A a tierra por R2 (6 ohm); A -> B por R3 (6 ohm); B a tierra por R4 (12 ohm).
    V, R1, R2, R3, R4 = 12.0, 4.0, 6.0, 6.0, 12.0
    g1, g2, g3, g4 = 1 / R1, 1 / R2, 1 / R3, 1 / R4
    # Análisis nodal: A: (g1+g2+g3) vA - g3 vB = g1 V ; B: -g3 vA + (g3+g4) vB = 0
    vA, vB = resolver([[g1 + g2 + g3, -g3], [-g3, g3 + g4]], [g1 * V, 0.0])
    i1, i2, i3, i4 = (V - vA) * g1, vA * g2, (vA - vB) * g3, vB * g4
    rpar = 1 / (g2 + 1 / (R3 + R4))
    vA_ana = V * rpar / (R1 + rpar)
    assert abs(vA - vA_ana) < 1e-12 and abs(vB - vA_ana * R4 / (R3 + R4)) < 1e-12
    assert abs(i1 - (i2 + i3)) < 1e-12 and abs(i3 - i4) < 1e-12   # Kirchhoff de corriente en A y en B
    p_fuente = V * i1
    p_res = i1**2 * R1 + i2**2 * R2 + i3**2 * R3 + i4**2 * R4
    assert abs(p_fuente - p_res) < 1e-12                        # balance de potencia
    assert abs(fraccion_eclipse(R_T) - 0.5) < 1e-12 and fraccion_eclipse(1e12) < 1e-5
    s = L_SOL / (4 * math.pi * A_TIERRA**2)
    r = R_T + 400_000.0
    T = 2 * math.pi * math.sqrt(r**3 / 3.9860e14)
    fe = fraccion_eclipse(r)
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Circuito: vA = {vA:.4f} V, vB = {vB:.4f} V; I1 = {i1:.4f} A, I2 = {i2:.4f} A, I3 = I4 = {i3:.4f} A; R_eq = {R1 + rpar:.3f} ohm; P_fuente = {p_fuente:.3f} W")
    print(f"Flujo solar a 1 au (de L y distancia) = {s:.1f} W/m²")
    area, eta, carga = 10.0, 0.28, 2000.0
    p_panel = s * area * eta
    print(f"Panel sintético: {area} m², eficiencia {eta} -> {p_panel:.0f} W; carga {carga:.0f} W")
    print(f"Órbita a 400 km: T = {T:.1f} s; fracción en eclipse = {fe:.4f} ({fe*T/60:.1f} min)")
    e_bat = carga * fe * T
    print(f"Energía de batería para el eclipse: {e_bat:.3e} J = {e_bat/3.6e6:.3f} kWh")
    e_gen = (p_panel - carga) * (1 - fe) * T
    print(f"Excedente disponible al sol para recargar: {e_gen:.3e} J (ratio con batería: {e_gen/e_bat:.2f})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
