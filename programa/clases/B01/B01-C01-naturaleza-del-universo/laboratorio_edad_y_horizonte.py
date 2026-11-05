#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C01: edad y horizonte comóvil de un universo ΛCDM plano.

Datos de entrada SINTÉTICOS/ESTIMADOS (parámetros publicados, no observaciones
directas): H0 [km/s/Mpc], Ωm [adimensional]. Salidas SIMULADAS.

Modelo: universo plano, Ωm + Ωr + ΩΛ = 1, ΩΛ constante, sin curvatura.
    E(a) = sqrt(Ωm/a³ + Ωr/a⁴ + ΩΛ)          (adimensional)
    t0  = (1/H0) ∫₀¹ da / (a E(a))             [tiempo]
    D_c = (c/H0) ∫₀¹ da / (a² E(a))            [longitud comóvil hoy]
Dominio de validez: ΛCDM plano; no apto para decidir entre modelos
alternativos ni para certificar nada. Tolerancia de las pruebas: 1e-4 relativa.
"""

from __future__ import annotations

import sys

import numpy as np
from scipy.integrate import quad

C_KM_S = 299_792.458                 # velocidad de la luz [km/s], valor exacto SI
MPC_KM = 3.0856775814913673e19       # megaparsec [km] (IAU 2015 B2)
YEAR_S = 365.25 * 86_400.0           # año juliano [s]
LY_M = C_KM_S * 1e3 * YEAR_S         # año luz [m]
A_MIN = 1e-8                         # límite inferior numérico (a → 0)


def age_and_horizon(h0: float, om: float, orad: float = 0.0) -> tuple[float, float]:
    """Devuelve (edad [Gyr], horizonte comóvil [Gly]) para un ΛCDM plano."""
    ol = 1.0 - om - orad

    def e(a: float) -> float:
        return np.sqrt(om / a**3 + orad / a**4 + ol)

    t_int = quad(lambda a: 1.0 / (a * e(a)), A_MIN, 1.0, epsabs=0, epsrel=1e-10)[0]
    d_int = quad(lambda a: 1.0 / (a * a * e(a)), A_MIN, 1.0, epsabs=0, epsrel=1e-10)[0]
    age_gyr = t_int * (MPC_KM / h0) / YEAR_S / 1e9
    d_gly = d_int * (C_KM_S / h0) * MPC_KM * 1e3 / LY_M / 1e9
    return age_gyr, d_gly


def run_tests() -> None:
    # Caso analítico independiente: Einstein–de Sitter (Ωm = 1, Ωr = 0).
    # t0 = 2/(3 H0)  y  D_c = 2 c/H0.
    h0 = 70.0
    age, dgly = age_and_horizon(h0, 1.0)
    age_ref = (2.0 / 3.0) * (MPC_KM / h0) / YEAR_S / 1e9
    d_ref = 2.0 * (C_KM_S / h0) * MPC_KM * 1e3 / LY_M / 1e9
    assert abs(age - age_ref) / age_ref < 1e-4, (age, age_ref)
    assert abs(dgly - d_ref) / d_ref < 1e-4, (dgly, d_ref)
    # Coherencia: más H0 -> universo más joven.
    assert age_and_horizon(73.0, 0.315)[0] < age_and_horizon(67.4, 0.315)[0]


def main() -> int:
    run_tests()
    import scipy
    print(f"numpy {np.__version__} | scipy {scipy.__version__} | python {sys.version.split()[0]}")
    print("Pruebas analíticas EdS: OK (tolerancia 1e-4)")
    print(f"{'H0':>6} {'Om':>6} {'Or':>8} {'edad [Gyr]':>11} {'D_c [Gly]':>10}")
    for h0, om, orad in ((67.4, 0.315, 9.2e-5), (73.04, 0.315, 9.2e-5), (70.0, 0.3, 9.2e-5)):
        age, dgly = age_and_horizon(h0, om, orad)
        print(f"{h0:6.2f} {om:6.3f} {orad:8.1e} {age:11.3f} {dgly:10.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
