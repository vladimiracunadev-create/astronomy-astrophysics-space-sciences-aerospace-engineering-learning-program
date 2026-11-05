#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C13: constante de equilibrio, cociente de reacción y tabla ICE.

Datos PUBLICADOS: NIST WebBook (CO2): punto triple 216,58 K y 5,185 bar,
Delta_sub H = 26,1 kJ/mol (25,2-27,2); NASA NSSDC Marte: 636 Pa y 95,1 % CO2 en
volumen; CODATA 2022: R. Modelo del CO2(s) <-> CO2(g): K(T) = P_sat(T)/p0 con
Clausius-Clapeyron (Delta H constante) y p0 = 1 bar; Q = p_CO2/p0.
La reacción A <-> 2B con K = 0,10 y c0 = 0,50 mol/L es SINTÉTICA (ilustrativa).
Supuestos: gas ideal, actividad del sólido = 1, concentraciones en mol/L.
Dominio de validez: equilibrio ideal a T constante; no trata velocidad.
Tolerancias: 1e-9 en Q = K tras resolver; 1e-6 entre dos métodos de resolución.
"""

from __future__ import annotations

import math
import sys

R = 8.314462618
P0 = 1e5                         # Pa, presión estándar (1 bar)
TTP, PTP, DH = 216.58, 5.185e5, 26_100.0   # CO2, NIST WebBook
P_MARTE, Y_CO2 = 636.0, 0.951                # NASA: Pa, fracción molar


def k_sub(T: float, dh: float = DH) -> float:
    """K de CO2(s) <-> CO2(g): presión de saturación (Pa) / p0."""
    return PTP * math.exp(-dh / R * (1 / T - 1 / TTP)) / P0


def temperatura_equilibrio(p_pa: float, dh: float = DH) -> float:
    return 1 / (1 / TTP - R * math.log(p_pa / PTP) / dh)


def direccion(q: float, k: float) -> str:
    return "hacia productos" if q < k * (1 - 1e-9) else ("hacia reactivos" if q > k * (1 + 1e-9) else "en equilibrio")


def ice_a_2b(k: float, a0: float, b0: float = 0.0) -> tuple[float, float]:
    """Equilibrio A <-> 2B por bisección en el avance x (A = a0 - x, B = b0 + 2x)."""
    lo, hi = -b0 / 2 + 1e-15, a0 - 1e-15
    f = lambda x: (b0 + 2 * x) ** 2 / (a0 - x) - k
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    x = (lo + hi) / 2
    return a0 - x, b0 + 2 * x


def ice_cuadratica(k: float, a0: float) -> tuple[float, float]:
    x = (-k + math.sqrt(k * k + 16 * k * a0)) / 8
    return a0 - x, 2 * x


def pruebas() -> None:
    k, c0 = 0.10, 0.50
    a, b = ice_a_2b(k, c0)
    assert abs(b * b / a - k) < 1e-9                                   # Q = K en el equilibrio
    a2, b2 = ice_cuadratica(k, c0)
    assert abs(a - a2) < 1e-6 and abs(b - b2) < 1e-6                   # dos métodos coinciden
    assert abs(a - 0.4) < 1e-6 and abs(b - 0.2) < 1e-6                 # solución exacta: x = 0,1
    # Le Chatelier: añadir B desplaza hacia reactivos y se recupera Q = K
    q_nuevo = (b + 0.3) ** 2 / a
    assert direccion(q_nuevo, k) == "hacia reactivos"
    a3, b3 = ice_a_2b(k, a, b + 0.3)
    assert abs(b3 * b3 / a3 - k) < 1e-9 and a3 > a
    # la presión de saturación en el punto triple da K = P_tp/p0
    assert abs(k_sub(TTP) - PTP / P0) < 1e-12
    t_eq = temperatura_equilibrio(Y_CO2 * P_MARTE)
    assert abs(k_sub(t_eq) - Y_CO2 * P_MARTE / P0) < 1e-12            # Q = K en el punto de escarcha


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    p_co2 = Y_CO2 * P_MARTE
    q = p_co2 / P0
    t_eq = temperatura_equilibrio(p_co2)
    print(f"CO2 en Marte: p = {p_co2:.1f} Pa ; Q = {q:.3e} ; temperatura de equilibrio (escarcha) = {t_eq:.2f} K "
          f"(con la presión total: {temperatura_equilibrio(P_MARTE):.2f} K)")
    for T in (140.0, 148.0, 160.0, 214.0):
        print(f"  T = {T:5.0f} K : K = {k_sub(T):.3e} ; Q = {q:.3e} -> {direccion(q, k_sub(T))}")
    print(f"K(160 K)/K(140 K) = {k_sub(160.0) / k_sub(140.0):.1f}")
    a, b = ice_a_2b(0.10, 0.50)
    print(f"ICE A <-> 2B (K=0.10, c0=0.50): [A] = {a:.4f} ; [B] = {b:.4f} ; conversión = {100 * (0.5 - a) / 0.5:.1f} %")
    a3, b3 = ice_a_2b(0.10, a, b + 0.30)
    print(f"Tras añadir 0.30 mol/L de B: Q = {(b + 0.3) ** 2 / a:.3f} -> {direccion((b + 0.3) ** 2 / a, 0.10)} ; "
          f"nuevo equilibrio [A] = {a3:.4f} ; [B] = {b3:.4f}")
    print(f"van 't Hoff, DH = -165 kJ/mol, 300 K -> 600 K: K2/K1 = {math.exp(165000 / R * (1 / 600 - 1 / 300)):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
