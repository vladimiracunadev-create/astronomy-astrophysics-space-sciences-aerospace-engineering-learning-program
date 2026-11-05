#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C12: ley de Hess con entalpías de formación del NIST WebBook.

Datos PUBLICADOS (medidos y evaluados), en kJ/mol a 298,15 K, estado estándar:
H2O(g) -241,826 +- 0,040 y H2O(l) -285,830 +- 0,040 (Cox, Wagman et al. 1984, CODATA Key
Values); CO2(g) -393,51 +- 0,13 (idem); CH4(g) -74,87 (Chase 1998, NIST-JANAF) o
-74,6 +- 0,3 (Manion 2002). Masas molares: H2O 18,0153 y CH4 16,0425 g/mol (WebBook).
Los elementos en su estado estándar valen 0 por definición.
Modelo: Delta_r H = suma(nu_i Delta_f H_i, productos) - suma(reactivos). Supuestos:
estado estándar, 298 K, incertidumbres independientes sumadas en cuadratura.
Dominio de validez: reacciones completas a 298 K; no da velocidad ni espontaneidad.
Tolerancias: 1e-9 en las pruebas de clausura (aritmética).
"""

from __future__ import annotations

import math
import sys

DFH = {  # kJ/mol : (valor, incertidumbre)
    "H2O(g)": (-241.826, 0.040), "H2O(l)": (-285.830, 0.040),
    "CO2(g)": (-393.51, 0.13), "CH4(g)": (-74.87, 0.0),
    "H2(g)": (0.0, 0.0), "O2(g)": (0.0, 0.0),
}
CH4_ALT = (-74.6, 0.3)       # Manion 2002
M_H2O, M_CH4 = 18.0153e-3, 16.0425e-3   # kg/mol


def delta_r_h(reactivos: dict[str, float], productos: dict[str, float], tabla=DFH) -> tuple[float, float]:
    """Entalpía de reacción y su incertidumbre (cuadratura) para coeficientes dados."""
    h = sum(c * tabla[s][0] for s, c in productos.items()) - sum(c * tabla[s][0] for s, c in reactivos.items())
    u = math.sqrt(sum((c * tabla[s][1]) ** 2 for s, c in {**reactivos, **productos}.items()))
    return h, u


def pruebas() -> None:
    # formación de un compuesto desde sus elementos: Delta_r H = Delta_f H
    h, _ = delta_r_h({"H2(g)": 1, "O2(g)": 0.5}, {"H2O(l)": 1})
    assert abs(h - DFH["H2O(l)"][0]) < 1e-9
    # clausura: (H2O g) - (H2O l) = Delta_vap H = 44,004
    hl, _ = delta_r_h({"CH4(g)": 1, "O2(g)": 2}, {"CO2(g)": 1, "H2O(l)": 2})
    hg, _ = delta_r_h({"CH4(g)": 1, "O2(g)": 2}, {"CO2(g)": 1, "H2O(g)": 2})
    assert abs((hg - hl) - 2 * 44.004) < 1e-9
    # invertir la reacción cambia el signo
    inv, _ = delta_r_h({"CO2(g)": 1, "H2O(l)": 2}, {"CH4(g)": 1, "O2(g)": 2})
    assert abs(inv + hl) < 1e-9
    # multiplicar los coeficientes multiplica la entalpía
    h2, _ = delta_r_h({"CH4(g)": 2, "O2(g)": 4}, {"CO2(g)": 2, "H2O(l)": 4})
    assert abs(h2 - 2 * hl) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    hl, ul = delta_r_h({"CH4(g)": 1, "O2(g)": 2}, {"CO2(g)": 1, "H2O(l)": 2})
    hg, _ = delta_r_h({"CH4(g)": 1, "O2(g)": 2}, {"CO2(g)": 1, "H2O(g)": 2})
    alt = {**DFH, "CH4(g)": CH4_ALT}
    ha, ua = delta_r_h({"CH4(g)": 1, "O2(g)": 2}, {"CO2(g)": 1, "H2O(l)": 2}, alt)
    print(f"CH4 + 2 O2 -> CO2 + 2 H2O(l): {hl:.2f} kJ/mol (+-{ul:.2f} sin incert. de CH4) ; con CH4 = -74.6+-0.3: {ha:.2f} +-{ua:.2f}")
    print(f"CH4 + 2 O2 -> CO2 + 2 H2O(g): {hg:.2f} kJ/mol ; diferencia = {hg - hl:.3f} (= 2 x 44.004)")
    h_met, _ = delta_r_h({"CO2(g)": 1, "H2(g)": 4}, {"CH4(g)": 1, "H2O(g)": 2})
    print(f"CO2 + 4 H2 -> CH4 + 2 H2O(g): {h_met:.2f} kJ/mol")
    print(f"Energía por kg de CH4 (a H2O líquida): {-hl * 1e3 / M_CH4 / 1e6:.2f} MJ/kg")
    h_f, _ = delta_r_h({"H2(g)": 1, "O2(g)": 0.5}, {"H2O(g)": 1})
    print(f"H2 + 1/2 O2 -> H2O(g): {h_f:.3f} kJ/mol = {-h_f * 1e3 / M_H2O / 1e6:.2f} MJ por kg de agua formada")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
