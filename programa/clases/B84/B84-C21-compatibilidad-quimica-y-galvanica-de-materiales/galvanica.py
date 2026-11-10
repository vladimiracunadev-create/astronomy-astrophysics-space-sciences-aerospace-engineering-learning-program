#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C21: corrosion galvanica de pares de metales: diferencia de potencial, corriente y velocidad de corrosion segun la relacion de areas.

Constante: F = 96485,33212 C/mol (e N_A del SI 2019; valor exacto, no consultado en esta sesion).
DATOS ILUSTRATIVOS (potenciales de corrosion tipicos en agua de mar frente a un electrodo de calomelanos, orden de magnitud, NO consultados):
  Mg AZ31 -1,60 V; Al 6061 -0,80 V; acero al carbono -0,65 V; Ti-6Al-4V -0,10 V; acero 304 pasivo -0,05 V; CFRP +0,20 V.
Resistencias de polarizacion lineal ILUSTRATIVAS: anodo Rp_a = 0,5 ohm m2; catodo Rp_c = 5 ohm m2 (superficie pasiva).
Modelo: corriente galvanica I = dV/(Rp_a/A_a + Rp_c/A_c) con areas en m2; densidad de corriente anodica i_a = I/A_a; velocidad de corrosion del anodo
v = i_a M/(n F rho) (m/s); se pasa a mm/ano. Aluminio: M = 26,98 g/mol, n = 3, rho = 2700 kg/m3.
Regla de contacto ILUSTRATIVA: dV <= 0,25 V para ambientes humedos; <= 0,50 V en interiores controlados (valores inventados para el ejercicio).
Segunda via: conservacion de carga (I anodica = I catodica) y perdida de masa por Faraday frente al espesor perdido.
Tolerancia: 1e-12 relativa.
"""
from __future__ import annotations
import math, platform

F = 96485.33212
POT = {"Mg AZ31": -1.60, "Al 6061": -0.80, "Acero C": -0.65, "Ti-6Al-4V": -0.10, "Acero 304": -0.05, "CFRP": 0.20}
RPA, RPC = 0.5, 5.0
AN = 365.25 * 86400.0


def velocidad_mm_ano(i, M, n, rho):
    return i * M / (n * F * rho) * AN * 1e3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Potenciales ILUSTRATIVOS (V vs calomelanos, agua de mar): " + "; ".join(f"{k} {v:+.2f}" for k, v in POT.items()))
    print("Diferencias de potencial y regla de contacto ilustrativa (<= 0,25 V humedo; <= 0,50 V interior):")
    pares = (("Al 6061", "Acero C"), ("Al 6061", "Acero 304"), ("Al 6061", "Ti-6Al-4V"), ("Al 6061", "CFRP"), ("Mg AZ31", "Al 6061"), ("Ti-6Al-4V", "Acero 304"))
    for a, c in pares:
        dv = abs(POT[c] - POT[a])
        print(f"  {a:10s} - {c:10s} dV = {dv:.2f} V  humedo: {'ok' if dv <= 0.25 else 'NO'}  interior: {'ok' if dv <= 0.50 else 'NO'}")
    print("Aluminio (anodo) acoplado a acero 304 (catodo): efecto de la relacion de areas A_c/A_a, con A_a = 1e-3 m2")
    dv = abs(POT["Acero 304"] - POT["Al 6061"])
    print(f"{'A_c/A_a':>8s} {'I [mA]':>9s} {'i_a [A/m2]':>11s} {'corrosion [mm/ano]':>19s} {'perdida de masa en 1 ano [g]':>30s}")
    prev = None
    for r in (0.1, 1.0, 10.0, 100.0):
        Aa, Ac = 1e-3, 1e-3 * r
        I = dv / (RPA / Aa + RPC / Ac)
        ia = I / Aa
        v = velocidad_mm_ano(ia, 26.98e-3, 3, 2700.0)
        masa = I * AN / (3 * F) * 26.98
        # segunda via: masa = rho * espesor * area
        esp = v * 1e-3 * Aa * 2700.0 * 1e3
        assert abs(masa - esp) / masa < 1e-12
        extra = "" if prev is None else f"  (x{v / prev:.2f})"
        print(f"{r:8.1f} {I * 1e3:9.3f} {ia:11.4f} {v:19.4f} {masa:30.3f}{extra}")
        prev = v
    print("Ventaja del area: anodo grande y catodo pequeno (A_c/A_a = 0,1) frente al caso desfavorable (100):")
    v1 = velocidad_mm_ano(dv / (RPA / 1e-3 + RPC / (1e-3 * 0.1)) / 1e-3, 26.98e-3, 3, 2700.0)
    v2 = velocidad_mm_ano(dv / (RPA / 1e-3 + RPC / (1e-3 * 100.0)) / 1e-3, 26.98e-3, 3, 2700.0)
    print(f"  {v1:.4f} mm/ano frente a {v2:.4f} mm/ano: factor {v2 / v1:.1f}")
    assert v2 > v1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
