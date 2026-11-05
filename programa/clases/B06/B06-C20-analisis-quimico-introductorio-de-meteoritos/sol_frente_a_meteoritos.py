#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C20: fotosfera solar frente a condritas CI y comparación con Bennu.

Datos PUBLICADOS (observados): Asplund, Grevesse, Sauval y Scott 2009, Ann. Rev.
Astron. Astrophys. 47, 481, Tabla 1: A(X) de la fotosfera y de las condritas CI
(media de Lodders, Palme y Gail 2009, normalizada a la misma escala fijando Si);
Glavin et al. 2025: Bennu C = 4,5-4,7 % y N = 0,23-0,25 % en masa. Los valores de
los gases nobles de la fotosfera (He, Ne, Ar) vienen entre corchetes en la fuente:
son estimaciones indirectas. Pesos atómicos NIST (puntos medios de intervalos).
Modelo: Delta = A_fot - A_met en dex; fracción en masa de la «CI media» calculada con
los 29 elementos de la tabla (el resto, Z > 30, aporta una fracción pequeña: ESTIMADO).
Supuestos: los valores meteoríticos representan CI; Bennu no es CI estricta.
Dominio de validez: comparación de abundancias de elementos entre H y Zn.
Tolerancias: media de Delta en no volátiles dentro de 0,02 dex de 0 y dispersión
entre 0,03 y 0,07 dex (la fuente informa 0,00 +- 0,05 para 45 elementos).
"""

from __future__ import annotations

import statistics as st
import sys

FOT = {"H": 12.00, "He": 10.93, "Li": 1.05, "Be": 1.38, "B": 2.70, "C": 8.43, "N": 7.83, "O": 8.69,
       "F": 4.56, "Ne": 7.93, "Na": 6.24, "Mg": 7.60, "Al": 6.45, "Si": 7.51, "P": 5.41, "S": 7.12,
       "Cl": 5.50, "Ar": 6.40, "K": 5.03, "Ca": 6.34, "Ti": 4.95, "V": 3.93, "Cr": 5.64, "Mn": 5.43,
       "Fe": 7.50, "Co": 4.99, "Ni": 6.22, "Cu": 4.19, "Zn": 4.56}
MET = {"H": 8.22, "He": 1.29, "Li": 3.26, "Be": 1.30, "B": 2.79, "C": 7.39, "N": 6.26, "O": 8.40,
       "F": 4.42, "Ne": -1.12, "Na": 6.27, "Mg": 7.53, "Al": 6.43, "Si": 7.51, "P": 5.43, "S": 7.15,
       "Cl": 5.23, "Ar": -0.50, "K": 5.08, "Ca": 6.29, "Ti": 4.91, "V": 3.96, "Cr": 5.64, "Mn": 5.48,
       "Fe": 7.45, "Co": 4.87, "Ni": 6.20, "Cu": 4.25, "Zn": 4.63}
PESO = {"H": 1.007975, "He": 4.002602, "Li": 6.9675, "Be": 9.0121831, "B": 10.8135, "C": 12.0106,
        "N": 14.006855, "O": 15.9994, "F": 18.998403163, "Ne": 20.1797, "Na": 22.98976928,
        "Mg": 24.3055, "Al": 26.9815385, "Si": 28.085, "P": 30.973761998, "S": 32.0675,
        "Cl": 35.4515, "Ar": 39.948, "K": 39.0983, "Ca": 40.078, "Ti": 47.867, "V": 50.9415,
        "Cr": 51.9961, "Mn": 54.938044, "Fe": 55.845, "Co": 58.933194, "Ni": 58.6934,
        "Cu": 63.546, "Zn": 65.38}
NO_VOLATILES = ["Na", "Mg", "Al", "Si", "P", "S", "K", "Ca", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
VOLATILES = ["H", "C", "N", "O"]
NOBLES = ["He", "Ne", "Ar"]


def delta(el: str) -> float:
    return FOT[el] - MET[el]


def masa_ci(el: str) -> float:
    """Fracción en masa (%) de la «CI media» con los 29 elementos de la tabla, sin gases nobles."""
    m = {k: 10 ** (MET[k] - 12) * PESO[k] for k in MET if k not in NOBLES}
    return 100 * m[el] / sum(m.values())


def pruebas() -> None:
    assert delta("Si") == 0.0                                  # normalización a Si
    d = [delta(k) for k in NO_VOLATILES]
    assert abs(st.mean(d)) < 0.02 and 0.03 < st.stdev(d) < 0.07, (st.mean(d), st.stdev(d))
    assert all(delta(k) > 0.25 for k in VOLATILES)             # los volátiles están empobrecidos en CI
    assert delta("Li") < -2.0                                  # Li empobrecido en el Sol
    total = sum(masa_ci(k) for k in MET if k not in NOBLES)
    assert abs(total - 100) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    d = [delta(k) for k in NO_VOLATILES]
    print(f"No volátiles (17 elementos): media de Delta = {st.mean(d):+.3f} dex ; desviación = {st.stdev(d):.3f} dex")
    print("Elemento | A fot | A met | Delta [dex] | factor 10^Delta")
    for k in VOLATILES + ["Li"] + NOBLES:
        print(f"  {k:2s}  {FOT[k]:6.2f}  {MET[k]:6.2f}  {delta(k):+7.2f}  {10 ** delta(k):.3g}")
    print("«CI media» calculada (% en masa, 26 elementos sin gases nobles): "
          + ", ".join(f"{k} {masa_ci(k):.2f}" for k in ("O", "Fe", "Si", "Mg", "S", "C", "H", "N")))
    c = masa_ci("C")
    n = masa_ci("N")
    print(f"Bennu C = 4.5-4.7 % -> {4.5 / c:.2f}-{4.7 / c:.2f} veces el valor calculado; "
          f"N = 0.23-0.25 % -> {0.23 / n:.2f}-{0.25 / n:.2f} veces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
