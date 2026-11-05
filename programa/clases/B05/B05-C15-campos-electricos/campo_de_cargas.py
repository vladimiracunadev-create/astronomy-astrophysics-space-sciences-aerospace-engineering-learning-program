#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C15: ley de Coulomb, campo eléctrico y partículas en un campo uniforme.

Datos PUBLICADOS (CODATA 2022 / SI 9.ª ed.): e = 1,602 176 634e-19 C (exacta); epsilon_0 =
8,854 187 8188e-12 F/m; m_p = 1,672 621 925 95e-27 kg; m_e = 9,109 383 7139e-31 kg;
G = 6,674 30e-11 m³ kg⁻¹ s⁻². Campo uniforme de 1,0e5 V/m y separaciones: SINTÉTICOS.
Modelo: cargas puntuales en el vacío, electrostática y mecánica no relativista.
Supuestos: sin radiación, sin campo magnético. Dominio de validez: velocidades << c.
Tolerancias: 1e-3 entre el campo dipolar aproximado y el exacto a 100 separaciones;
1e-12 en la conservación de energía en el campo uniforme.
"""
from __future__ import annotations
import math
import sys

E_CARGA = 1.602176634e-19
EPS0 = 8.8541878188e-12
M_P = 1.67262192595e-27
M_E = 9.1093837139e-31
G = 6.67430e-11
KE = 1.0 / (4 * math.pi * EPS0)

def campo_axial(q: float, x_q: float, x: float) -> float:
    """Campo en el eje x de una carga q en x_q (componente x)."""
    d = x - x_q
    return KE * q * math.copysign(1.0, d) / d**2

def main() -> int:
    # Prueba 1: dipolo; campo exacto vs aproximado a 100 separaciones
    d, r = 1.0e-9, 100e-9
    e_exacto = campo_axial(E_CARGA, d / 2, r) + campo_axial(-E_CARGA, -d / 2, r)
    p = E_CARGA * d
    e_aprox = 2 * KE * p / r**3
    assert abs(e_exacto - e_aprox) / e_aprox < 1e-3
    # Prueba 2: energía en un campo uniforme: qE d = 1/2 m v²
    E, dist = 1.0e5, 0.10
    a = E_CARGA * E / M_P
    v = math.sqrt(2 * a * dist)
    assert abs(0.5 * M_P * v * v - E_CARGA * E * dist) / (E_CARGA * E * dist) < 1e-12
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"k_e = 1/(4 pi eps0) = {KE:.6e} N m²/C²")
    f_ee = KE * E_CARGA**2 / 1.0**2
    print(f"Fuerza entre dos cargas elementales a 1 m: {f_ee:.4e} N")
    print(f"Cociente eléctrica/gravitatoria protón–protón: {KE*E_CARGA**2/(G*M_P**2):.4e}")
    print(f"Cociente eléctrica/gravitatoria protón–electrón: {KE*E_CARGA**2/(G*M_P*M_E):.4e}")
    print(f"Campo dipolar a 100 separaciones: exacto {e_exacto:.6e} V/m, aproximado {e_aprox:.6e} V/m")
    print(f"Protón en E = {E:.1e} V/m: a = {a:.4e} m/s²; tras {dist} m: v = {v:.4e} m/s ({v/299792458:.4f} c); energía = {E_CARGA*E*dist/E_CARGA:.1f} eV")
    print(f"Electrón en el mismo campo: a = {E_CARGA*E/M_E:.4e} m/s² (cociente con el protón {M_P/M_E:.1f})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
