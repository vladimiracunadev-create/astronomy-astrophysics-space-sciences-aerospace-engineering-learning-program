#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C03: factores de Franck-Condon entre dos osciladores armonicos desplazados (SINTETICO).

Datos: h, c y u de CODATA 2022 (NIST, consultados el 2026-11-09). S1.
Molecula: SINTETICA. Masa reducida 6.857 u (valor tipo CO con masas enteras, solo para dar una escala), frecuencias de oscilador
  inicial 2000 cm^-1 y final 1500 cm^-1 y desplazamiento de equilibrio 0.10 A son valores ILUSTRATIVOS; no describen ninguna transicion real.
Modelo: dos pozos armonicos 1D. FC(v'' , v') = |integral psi''_v''(x) psi'_v'(x - d) dx|^2 con funciones de Hermite.
  Caso A (misma frecuencia): FC(0,v') = exp(-S) S^v' / v'!, S = mu*omega*d^2/(2 hbar)  (solucion analitica).
  Caso B (frecuencias distintas): solo integral numerica; se comprueba la regla de suma sum_v' FC = 1.
Supuestos: aproximacion de Condon (momento de transicion electronico constante), sin rotacion, sin anarmonicidad.
Tolerancias: integral numerica vs formula analitica 1e-8 (trapecio con paso 1e-3 en unidades adimensionales); regla de suma 1e-6 (se trunca a v' <= 40).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

H = 6.62607015e-34
C = 299792458.0
U = 1.66053906892e-27
HBAR = H / (2 * math.pi)


def hermite_fn(n: int, x: np.ndarray) -> np.ndarray:
    """Funciones propias del oscilador armonico en unidades adimensionales (normalizadas), por recurrencia estable."""
    psi = np.zeros((n + 1, x.size))
    psi[0] = math.pi ** -0.25 * np.exp(-x * x / 2)
    if n >= 1:
        psi[1] = math.sqrt(2.0) * x * psi[0]
    for k in range(2, n + 1):
        psi[k] = math.sqrt(2.0 / k) * x * psi[k - 1] - math.sqrt((k - 1) / k) * psi[k - 2]
    return psi


def fc_matrix(mu_u: float, nu_i: float, nu_f: float, d_angstrom: float, nmax: int = 40) -> np.ndarray:
    """FC(v'', v') para v'' = 0..nmax y v' = 0..nmax. nu en cm^-1."""
    mu = mu_u * U
    wi, wf = 2 * math.pi * C * nu_i * 100.0, 2 * math.pi * C * nu_f * 100.0
    ai = math.sqrt(mu * wi / HBAR)   # 1/m
    af = math.sqrt(mu * wf / HBAR)
    # malla en metros
    L = 12.0 / min(ai, af)
    N = 20001
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]
    psi_i = hermite_fn(nmax, ai * x) * math.sqrt(ai)
    psi_f = hermite_fn(nmax, af * (x - d_angstrom * 1e-10)) * math.sqrt(af)
    ov = psi_i @ psi_f.T * dx
    return ov ** 2


def main() -> int:
    print(f"Python {platform.python_version()}, numpy {np.__version__}")
    print("Molecula SINTETICA (mu = 6.857 u, d = 0.10 A): ningun valor describe una transicion real; constantes h, c, u de CODATA 2022 (consultado 2026-11-09)")
    mu_u, nu, d = 6.857, 2000.0, 0.10
    S = mu_u * U * (2 * math.pi * C * nu * 100.0) * (d * 1e-10) ** 2 / (2 * HBAR)
    print(f"Caso A: misma frecuencia {nu:.0f} cm^-1, desplazamiento {d} A -> factor de Huang-Rhys S = {S:.5f}")
    M = fc_matrix(mu_u, nu, nu, d)
    print(" v'   FC numerico (0->v')   FC analitico   dif.")
    peor = 0.0
    for v in range(0, 7):
        an = math.exp(-S) * S ** v / math.factorial(v)
        peor = max(peor, abs(M[0, v] - an))
        print(f" {v}   {M[0, v]:.8f}        {an:.8f}   {abs(M[0, v]-an):.1e}")
    print(f"Diferencia maxima = {peor:.2e} ; suma FC(0,v') hasta 40 = {M[0].sum():.8f} ; v' mas intenso = {int(np.argmax(M[0]))}")
    assert peor < 1e-8 and abs(M[0].sum() - 1) < 1e-6, "Caso A fuera de tolerancia"
    # Caso B: frecuencias distintas
    MB = fc_matrix(mu_u, 2000.0, 1500.0, 0.10)
    print("Caso B: frecuencia inicial 2000 cm^-1, final 1500 cm^-1, d = 0.10 A (solo numerico)")
    print(" v'   FC(0,v')")
    for v in range(0, 6):
        print(f" {v}   {MB[0, v]:.6f}")
    print(f"Suma hasta v' = 40: {MB[0].sum():.8f} ; sin desplazamiento (d = 0) y misma frecuencia: FC(0,0) = {fc_matrix(mu_u,2000.0,2000.0,0.0)[0,0]:.8f}")
    assert abs(MB[0].sum() - 1) < 1e-6
    assert abs(fc_matrix(mu_u, 2000.0, 2000.0, 0.0)[0, 0] - 1) < 1e-8
    # intensidad relativa de una progresion (Condon): proporcional a FC
    rel = M[0, :6] / M[0, :6].max()
    print("Intensidades relativas de la progresion (caso A, v' = 0..5):", ", ".join(f"{r:.3f}" for r in rel))
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
