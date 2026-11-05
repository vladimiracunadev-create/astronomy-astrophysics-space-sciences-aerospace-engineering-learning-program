#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C17: identificar líneas de Balmer en un espectro SINTÉTICO y medir z.

Datos PUBLICADOS: NIST Atomic Spectra Database v5.12, longitudes de onda en aire de H I
(punto medio del rango de componentes: Halfa 656,2810; Hbeta 486,1327; Hgamma 434,0463;
Hdelta 410,1734 nm); CODATA 2022: R_inf, m_p/m_e, c.
El ESPECTRO OBSERVADO es SINTÉTICO: z_verdadero = 0,0101 (el de B01-C01) con
desplazamientos fijos de -0,04 a +0,03 nm que simulan el error de medida. El
espectro molecular (rotor rígido, B = 2,0 cm^-1) es también sintético.
Modelo: lambda_obs = lambda_reposo (1 + z) ; v = c z (no relativista, z << 1);
identificación por búsqueda en rejilla de z que minimiza las discrepancias.
Supuestos: líneas en aire, sin ensanchamiento. Dominio de validez: z < 0,1.
Tolerancias: |z recuperado - z verdadero| < 2e-4 ; B recuperado a 1e-9.
"""

from __future__ import annotations

import sys

C_KMS = 299_792.458
REPOSO = {"Hα": 656.2810, "Hβ": 486.1327, "Hγ": 434.0463, "Hδ": 410.1734}   # nm, aire (NIST ASD)
Z_VERDADERO = 0.0101
RUIDO = {"Hα": +0.030, "Hβ": -0.040, "Hγ": +0.020, "Hδ": -0.010}            # nm (sintético)
R_INF, MP_ME = 10_973_731.568157, 1836.152673426
R_H = R_INF / (1 + 1 / MP_ME)


def espectro_sintetico() -> list[float]:
    return sorted(REPOSO[k] * (1 + Z_VERDADERO) + RUIDO[k] for k in REPOSO)


def error_total(z: float, observadas: list[float]) -> float:
    pred = [r * (1 + z) for r in REPOSO.values()]
    return sum(min(abs(o - p) for p in pred) for o in observadas)


def ajustar_z(observadas: list[float], z_max: float = 0.1, paso: float = 1e-5) -> float:
    n = int(z_max / paso)
    mejor = min(range(n + 1), key=lambda i: error_total(i * paso, observadas))
    return mejor * paso


def lambda_vacio_nm(n_alto: int, n_bajo: int) -> float:
    return 1e9 / (R_H * (1 / n_bajo**2 - 1 / n_alto**2))


def rotor_rigido(b_cm1: float, j_max: int) -> list[float]:
    """Números de onda (cm^-1) de las transiciones J -> J+1: 2 B (J+1)."""
    return [2 * b_cm1 * (j + 1) for j in range(j_max)]


def pruebas() -> None:
    obs = espectro_sintetico()
    z = ajustar_z(obs)
    assert abs(z - Z_VERDADERO) < 2e-4, z
    # sin corrimiento (z = 0) el error es mucho mayor que con el z ajustado
    assert error_total(0.0, obs) > 10 * error_total(z, obs)
    # el rotor rígido: el espaciado entre líneas consecutivas es 2B
    lineas = rotor_rigido(2.0, 6)
    b = (lineas[1] - lineas[0]) / 2
    assert abs(b - 2.0) < 1e-9 and all(abs((lineas[i + 1] - lineas[i]) - 4.0) < 1e-9 for i in range(5))
    # Lyman-alfa en el vacío (con masa reducida) ~121,567 nm
    assert abs(lambda_vacio_nm(2, 1) - 121.567) < 0.01


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    obs = espectro_sintetico()
    print("Líneas observadas (sintético) [nm]:", ", ".join(f"{o:.3f}" for o in obs))
    z = ajustar_z(obs)
    print(f"z ajustado = {z:.5f} (verdadero {Z_VERDADERO}) ; v = c z = {C_KMS * z:.0f} km/s ; "
          f"error total residual = {error_total(z, obs):.3f} nm")
    print(f"Halfa observada esperada = {REPOSO['Hα'] * (1 + z):.3f} nm")
    print("Series en el vacío (masa reducida) [nm]:")
    print(f"  Lyman-alfa  (2->1): {lambda_vacio_nm(2, 1):.3f}")
    print(f"  Balmer-alfa (3->2): {lambda_vacio_nm(3, 2):.3f}")
    print(f"  Paschen-alfa (4->3): {lambda_vacio_nm(4, 3):.1f}")
    print(f"  Brackett-alfa (5->4): {lambda_vacio_nm(5, 4):.1f}")
    print("Rotor rígido sintético (B = 2.0 cm^-1):", rotor_rigido(2.0, 5), "cm^-1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
