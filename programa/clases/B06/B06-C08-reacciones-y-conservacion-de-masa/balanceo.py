#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C08: balanceo de ecuaciones y defecto de masa nuclear.

Datos PUBLICADOS: CODATA 2022 (NIST): u = 1,660 539 068 92e-27 kg, c y e exactas;
NIST Atomic Weights: masas atómicas relativas de 1H (1,00782503223) y 4He
(4,00260325413). Entalpía de combustión del metano (clase C12): -890,3 kJ/mol,
valor DERIVADO de NIST WebBook (C12).
Modelo: balanceo por núcleo de la matriz de átomos con fracciones exactas
(Fraction), sin dependencias externas. Supuestos: la ecuación incluye todas las
especies y su fórmula es correcta; la carga se trata como un elemento más ('q').
Dominio de validez: ecuaciones con una sola solución independiente.
Tolerancia: exacta (aritmética racional); 0,01 MeV en el defecto de masa.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from math import gcd

C = 299_792_458
E = 1.602176634e-19
U_KG = 1.66053906892e-27


def balancear(reactivos: list[dict[str, int]], productos: list[dict[str, int]]) -> list[int]:
    """Coeficientes enteros mínimos; las fórmulas son dicts elemento -> cantidad."""
    especies = reactivos + productos
    elementos = sorted({e for f in especies for e in f})
    n = len(especies)
    filas = [[Fraction(f.get(e, 0)) * (1 if i < len(reactivos) else -1) for i, f in enumerate(especies)]
             for e in elementos]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(filas)) if filas[i][c] != 0), None)
        if p is None:
            continue
        filas[r], filas[p] = filas[p], filas[r]
        filas[r] = [x / filas[r][c] for x in filas[r]]
        for i in range(len(filas)):
            if i != r and filas[i][c] != 0:
                filas[i] = [a - filas[i][c] * b for a, b in zip(filas[i], filas[r])]
        piv.append(c)
        r += 1
    libres = [c for c in range(n) if c not in piv]
    assert len(libres) == 1, "la ecuación no tiene una única solución independiente"
    sol = [Fraction(0)] * n
    sol[libres[0]] = Fraction(1)
    for i, c in enumerate(piv):
        sol[c] = -filas[i][libres[0]]
    den = 1
    for x in sol:
        den = den * x.denominator // gcd(den, x.denominator)
    ent = [int(x * den) for x in sol]
    g = 0
    for x in ent:
        g = gcd(g, abs(x))
    return [x // g for x in ent]


def defecto_masa_mev(m_h1: float = 1.00782503223, m_he4: float = 4.00260325413) -> float:
    """Energía liberada al fusionar 4 átomos de H-1 en He-4 (masas atómicas neutras)."""
    dm_u = 4 * m_h1 - m_he4
    return dm_u * U_KG * C**2 / E / 1e6


def pruebas() -> None:
    assert balancear([{"C": 1, "H": 4}, {"O": 2}], [{"C": 1, "O": 2}, {"H": 2, "O": 1}]) == [1, 2, 1, 2]
    assert balancear([{"C": 1, "O": 2}, {"H": 2}], [{"C": 1, "H": 4}, {"H": 2, "O": 1}]) == [1, 4, 1, 2]
    # con carga: NH3 + HCOOH -> NH4+ + HCOO-
    assert balancear([{"N": 1, "H": 3}, {"H": 2, "C": 1, "O": 2}],
                     [{"N": 1, "H": 4, "q": 1}, {"H": 1, "C": 1, "O": 2, "q": -1}]) == [1, 1, 1, 1]
    # defecto de masa de 4 H -> He: 26,73 MeV (incluye la aniquilación de positrones, cálculo propio)
    assert abs(defecto_masa_mev() - 26.7313) < 0.01, defecto_masa_mev()
    # una combustión química pierde una masa minúscula (E = m c^2)
    assert 890.3e3 / C**2 < 1e-10


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("CH4 + O2 -> CO2 + H2O:", balancear([{"C": 1, "H": 4}, {"O": 2}], [{"C": 1, "O": 2}, {"H": 2, "O": 1}]))
    print("CO2 + H2 -> CH4 + H2O:", balancear([{"C": 1, "O": 2}, {"H": 2}], [{"C": 1, "H": 4}, {"H": 2, "O": 1}]))
    print(f"4 1H -> 4He: {defecto_masa_mev():.3f} MeV por núcleo de He")
    dm = 890.3e3 / C**2
    print(f"Masa perdida en 1 mol de CH4 quemado: {dm:.3e} kg ({dm * 1e3:.3e} g)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
