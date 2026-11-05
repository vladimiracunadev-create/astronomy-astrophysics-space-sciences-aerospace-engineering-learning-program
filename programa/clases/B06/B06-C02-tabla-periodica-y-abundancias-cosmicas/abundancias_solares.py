#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C02: de abundancias logarítmicas a fracciones en número y masa.

Datos PUBLICADOS (observados e inferidos): Asplund, Grevesse, Sauval & Scott 2009,
Ann. Rev. Astron. Astrophys. 47, 481, Tabla 1 (fotosfera solar; el helio entre
corchetes procede de la heliosismología, no de la fotosfera) y Tabla 4 (X, Y, Z).
Pesos atómicos: NIST, punto medio del intervalo estándar cuando es un intervalo.
Modelo: A(X) = log10(N_X/N_H) + 12. Supuestos: se usan los 29 elementos de la
lista de abajo (H a Zn salvo Sc); el resto aporta menos de 0,1 % de la masa.
Dominio de validez: composición fotosférica actual del Sol, no la del universo.
Tolerancias: X, Y y Z dentro de 0,002; Z/X dentro de 1 % del valor publicado.
"""

from __future__ import annotations

import sys

A = {  # A(X) = log10(N_X/N_H) + 12 ; Asplund et al. 2009, Tabla 1
    "H": 12.00, "He": 10.93, "Li": 1.05, "Be": 1.38, "B": 2.70, "C": 8.43,
    "N": 7.83, "O": 8.69, "F": 4.56, "Ne": 7.93, "Na": 6.24, "Mg": 7.60,
    "Al": 6.45, "Si": 7.51, "P": 5.41, "S": 7.12, "Cl": 5.50, "Ar": 6.40,
    "K": 5.03, "Ca": 6.34, "Ti": 4.95, "V": 3.93, "Cr": 5.64, "Mn": 5.43,
    "Fe": 7.50, "Co": 4.99, "Ni": 6.22, "Cu": 4.19, "Zn": 4.56,
}
W = {  # pesos atómicos [g/mol]; NIST (punto medio de los intervalos)
    "H": 1.007975, "He": 4.002602, "Li": 6.9675, "Be": 9.0121831, "B": 10.8135,
    "C": 12.0106, "N": 14.006855, "O": 15.9994, "F": 18.998403163, "Ne": 20.1797,
    "Na": 22.98976928, "Mg": 24.3055, "Al": 26.9815385, "Si": 28.085,
    "P": 30.973761998, "S": 32.0675, "Cl": 35.4515, "Ar": 39.948, "K": 39.0983,
    "Ca": 40.078, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938044,
    "Fe": 55.845, "Co": 58.933194, "Ni": 58.6934, "Cu": 63.546, "Zn": 65.38,
}
# Asplund et al. 2009, Tabla 4, «Present work», fotosfera actual
X_PUB, Y_PUB, Z_PUB, ZX_PUB = 0.7381, 0.2485, 0.0134, 0.0181


def n_rel_h(simbolo: str) -> float:
    """N_X/N_H a partir de A(X)."""
    return 10 ** (A[simbolo] - 12.0)


def fracciones() -> tuple[dict[str, float], dict[str, float]]:
    n_total = sum(n_rel_h(s) for s in A)
    en_numero = {s: n_rel_h(s) / n_total for s in A}
    m = {s: n_rel_h(s) * W[s] for s in A}
    m_total = sum(m.values())
    return en_numero, {s: m[s] / m_total for s in A}


def pruebas() -> None:
    assert abs(n_rel_h("H") - 1.0) < 1e-12          # definición de la escala
    assert abs(n_rel_h("O") - 10 ** -3.31) < 1e-12  # 8,69 - 12
    num, masa = fracciones()
    assert abs(sum(num.values()) - 1) < 1e-12 and abs(sum(masa.values()) - 1) < 1e-12
    x, y = masa["H"], masa["He"]
    z = 1 - x - y
    assert abs(x - X_PUB) < 0.002, x
    assert abs(y - Y_PUB) < 0.002, y
    assert abs(z - Z_PUB) < 0.002, z
    assert abs(z / x - ZX_PUB) / ZX_PUB < 0.01, z / x


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    num, masa = fracciones()
    x, y = masa["H"], masa["He"]
    z = 1 - x - y
    print(f"X = {x:.4f} (pub. {X_PUB}) | Y = {y:.4f} (pub. {Y_PUB}) | Z = {z:.4f} (pub. {Z_PUB}) | Z/X = {z / x:.4f} (pub. {ZX_PUB})")
    print("Elemento | N/N_H | fracción en número | fracción en masa")
    for s in sorted(A, key=lambda k: -A[k])[:9]:
        print(f"  {s:2s}  {n_rel_h(s):10.3e}  {num[s]:10.4%}  {masa[s]:10.4%}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
