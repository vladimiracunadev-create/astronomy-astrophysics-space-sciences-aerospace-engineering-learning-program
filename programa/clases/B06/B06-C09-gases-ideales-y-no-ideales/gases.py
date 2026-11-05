#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C09: densidad y altura de escala de atmósferas con el gas ideal.

Datos PUBLICADOS (observados): NASA NSSDC Fact Sheets (Marte act. 19-may-2025,
Venus 11-ene-2024, Tierra 15-nov-2024): presión superficial, temperatura media,
gravedad media, peso molecular medio, densidad y altura de escala de referencia.
R = 8,314 462 618... J/(mol K) (CODATA 2022, de N_A y k exactas).
Parámetros de van der Waals del CO2 (a, b): SINTÉTICOS/ilustrativos, no consultados
en una fuente; sirven solo para mostrar la desviación del modelo ideal.
Modelo: PV = nRT => rho = P M/(R T) ; H = R T/(M g) (atmósfera isoterma).
Dominio de validez: gas lejos de la condensación; presión y temperatura medias.
Tolerancias: rho a 3 % (Venus, Tierra) o dentro de la incertidumbre NASA (Marte);
H a 2 %; Z de van der Waals a 1e-3 de 1 a presión baja.
"""

from __future__ import annotations

import sys

R = 8.314462618  # J/(mol K)
# nombre: (P [Pa], T [K], M [kg/mol], g [m/s2], rho_ref, H_ref [km])
PLANETAS = {
    "Marte": (636.0, 214.0, 0.04349, 3.73, 0.016, 11.0),
    "Venus": (9.2e6, 737.0, 0.04345, 8.87, 65.0, 15.9),
    "Tierra": (101_400.0, 288.0, 0.02897, 9.82, 1.217, 8.5),
}
A_VDW, B_VDW = 0.364, 4.27e-5   # Pa m6/mol2, m3/mol : ILUSTRATIVOS (sintéticos) para CO2


def densidad(P: float, T: float, M: float) -> float:
    return P * M / (R * T)


def altura_escala_km(T: float, M: float, g: float) -> float:
    return R * T / (M * g) / 1000.0


def volumen_molar_vdw(P: float, T: float, a: float = A_VDW, b: float = B_VDW) -> float:
    """Raíz gaseosa (la mayor) de la ecuación de van der Waals por bisección."""
    f = lambda v: R * T / (v - b) - a / v**2 - P
    lo, hi = b * 1.0001, 10 * R * T / P + 10 * b
    for _ in range(300):
        mid = (lo + hi) / 2
        # f es decreciente en la rama gaseosa: f(lo)>0 , f(hi)<0
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def z_vdw(P: float, T: float, a: float = A_VDW, b: float = B_VDW) -> float:
    return P * volumen_molar_vdw(P, T, a, b) / (R * T)


def pruebas() -> None:
    # límite ideal: a = b = 0 recupera PV = RT
    assert abs(z_vdw(9.2e6, 737.0, 0.0, 0.0) - 1.0) < 1e-9
    # a presión baja (Marte) Z de vdW es 1 dentro de 1e-3
    assert abs(z_vdw(636.0, 214.0) - 1.0) < 1e-3
    for n, (P, T, M, g, rho_ref, h_ref) in PLANETAS.items():
        rho, h = densidad(P, T, M), altura_escala_km(T, M, g)
        assert abs(h - h_ref) / h_ref < 0.02, (n, h)
        if n == "Marte":
            assert abs(rho - 0.016) <= 0.006, (n, rho)
        else:
            assert abs(rho - rho_ref) / rho_ref < 0.03, (n, rho)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Planeta | rho ideal [kg/m3] (NASA) | H [km] (NASA)")
    for n, (P, T, M, g, rho_ref, h_ref) in PLANETAS.items():
        print(f"  {n:6s} {densidad(P, T, M):8.4f} ({rho_ref})   {altura_escala_km(T, M, g):6.2f} ({h_ref})")
    print(f"Z de van der Waals (parámetros sintéticos): Marte {z_vdw(636.0, 214.0):.4f} ; "
          f"Tierra {z_vdw(101_400.0, 288.0):.4f} ; Venus {z_vdw(9.2e6, 737.0):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
