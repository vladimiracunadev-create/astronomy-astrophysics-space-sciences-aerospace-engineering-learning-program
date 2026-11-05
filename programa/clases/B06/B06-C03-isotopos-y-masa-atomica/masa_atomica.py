#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C03: masa atómica media a partir de isótopos.

Datos PUBLICADOS: NIST, «Atomic Weights and Isotopic Compositions for All
Elements» (masas atómicas relativas y composiciones isotópicas terrestres;
consulta del 2026-11-05) y, para la razón 12C/13C solar, Asplund et al. 2009
(12C/13C = 86,8 ± 3,8, estimación a partir de medidas en el Sol).
Modelo: masa media = suma(abundancia_i * masa_i). Supuesto: composición
isotópica terrestre normal. Dominio de validez: materiales terrestres; otros
cuerpos (meteoritos, Sol) pueden diferir. Tolerancia: el valor calculado debe
caer dentro del intervalo estándar de la NIST (o a +-3 incertidumbres del valor).
"""

from __future__ import annotations

import sys

# elemento: [(masa relativa, abundancia)], NIST
ISOTOPOS = {
    "H": [(1.00782503223, 0.999885), (2.01410177812, 0.000115)],
    "He": [(3.0160293201, 0.00000134), (4.00260325413, 0.99999866)],
    "C": [(12.0, 0.9893), (13.00335483507, 0.0107)],
    "N": [(14.00307400443, 0.99636), (15.00010889888, 0.00364)],
    "O": [(15.99491461957, 0.99757), (16.99913175650, 0.00038), (17.99915961286, 0.00205)],
    "Ne": [(19.9924401762, 0.9048), (20.993846685, 0.0027), (21.991385114, 0.0925)],
    "Mg": [(23.985041697, 0.7899), (24.985836976, 0.1000), (25.982592968, 0.1101)],
    "Si": [(27.97692653465, 0.92223), (28.97649466490, 0.04685), (29.973770136, 0.03092)],
    "S": [(31.9720711744, 0.9499), (32.9714589098, 0.0075), (33.967867004, 0.0425), (35.96708071, 0.0001)],
    "Cl": [(34.968852682, 0.7576), (36.965902602, 0.2424)],
    "Ar": [(35.967545105, 0.003336), (37.96273211, 0.000629), (39.9623831237, 0.996035)],
    "Fe": [(53.93960899, 0.05845), (55.93493633, 0.91754), (56.93539284, 0.02119), (57.93327443, 0.00282)],
}
# Peso atómico estándar NIST: (mínimo, máximo); para valores con incertidumbre, valor +- 3 u
ESTANDAR = {
    "H": (1.00784, 1.00811), "He": (4.002602 - 6e-6, 4.002602 + 6e-6), "C": (12.0096, 12.0116),
    "N": (14.00643, 14.00728), "O": (15.99903, 15.99977), "Ne": (20.1797 - 18e-4, 20.1797 + 18e-4),
    "Mg": (24.304, 24.307), "Si": (28.084, 28.086), "S": (32.059, 32.076),
    "Cl": (35.446, 35.457), "Ar": (39.948 - 3e-3, 39.948 + 3e-3), "Fe": (55.845 - 6e-3, 55.845 + 6e-3),
}


def masa_media(simbolo: str) -> float:
    return sum(m * x for m, x in ISOTOPOS[simbolo])


def abundancia_desde_peso(peso: float, m_ligero: float, m_pesado: float) -> float:
    """Abundancia del isótopo pesado en un elemento de dos isótopos."""
    return (peso - m_ligero) / (m_pesado - m_ligero)


def pruebas() -> None:
    for s, lista in ISOTOPOS.items():
        assert abs(sum(x for _, x in lista) - 1) < 2e-4, s       # abundancias suman 1
        lo, hi = ESTANDAR[s]
        assert lo <= masa_media(s) <= hi, (s, masa_media(s))     # cae en el valor estándar NIST
    # Caso analítico: un único isótopo da su propia masa
    assert abs(sum(m * x for m, x in [(12.0, 1.0)]) - 12.0) < 1e-15
    # Caso analítico: invertir la media recupera la abundancia del 13C (0,0107) a 1e-4
    x13 = abundancia_desde_peso(masa_media("C"), 12.0, 13.00335483507)
    assert abs(x13 - 0.0107) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Elemento | masa media calculada | estándar NIST")
    for s in ISOTOPOS:
        lo, hi = ESTANDAR[s]
        print(f"  {s:2s}  {masa_media(s):10.4f}   [{lo:.4f}, {hi:.4f}]")
    d_h = ISOTOPOS["H"][1][1] / ISOTOPOS["H"][0][1]
    c_t = ISOTOPOS["C"][0][1] / ISOTOPOS["C"][1][1]
    print(f"D/H terrestre = {d_h:.3e}")
    print(f"12C/13C terrestre = {c_t:.1f} ; Sol (Asplund 2009) = 86.8 +- 3.8 ; diferencia = {(c_t - 86.8) / 3.8:.2f} sigma")
    r15 = ISOTOPOS["N"][1][1] / ISOTOPOS["N"][0][1]
    print(f"15N/14N (tabla NIST) = {r15:.4e} ; con delta15N = +180 permil -> {r15 * 1.18:.4e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
