#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B06-C15: pH, ácidos y bases débiles, y balance NH3 / ácido fórmico de Bennu.

Datos PUBLICADOS (medidos en laboratorio): Glavin et al. 2025 (Nature Astronomy),
extracto en agua caliente de Bennu: amoníaco libre ~13,6 umol/g y ácido fórmico
4,106 umol/g (4106 nmol/g). K_w = 1,0e-14 (25 grados C), K_a = 1,8e-4 y K_b = 1,8e-5
son VALORES DE TRABAJO DE LA CLASE (sintéticos/ilustrativos; no consultados en una
fuente). Concentraciones usadas como aproximación de las actividades.
Modelo: pH = -log10[H+]; equilibrio del ácido o base débil resuelto con la
cuadrática exacta y con la aproximación x = sqrt(K c). Supuestos: disolución diluida
ideal, 25 grados C. Dominio de validez: ácidos y bases monopróticos en agua.
Tolerancias: 1e-9 en la verificación K = x^2/(c - x); 0,01 unidades de pH en la
comparación con las soluciones de referencia calculadas a mano.
"""

from __future__ import annotations

import math
import sys

KW = 1.0e-14
KA, KB = 1.8e-4, 1.8e-5


def ph(h: float) -> float:
    return -math.log10(h)


def h_acido_fuerte(c: float) -> float:
    """[H+] de un ácido fuerte monoprótico incluyendo la autoprotólisis del agua."""
    return (c + math.sqrt(c * c + 4 * KW)) / 2


def x_debil_exacta(k: float, c: float) -> float:
    """x = [H+] (ácido) o [OH-] (base) de un electrolito débil de concentración c."""
    return (-k + math.sqrt(k * k + 4 * k * c)) / 2


def x_debil_aprox(k: float, c: float) -> float:
    return math.sqrt(k * c)


def pruebas() -> None:
    assert abs(ph(h_acido_fuerte(1e-3)) - 3.0) < 1e-4            # HCl 1e-3 M -> pH 3
    assert abs(ph(math.sqrt(KW)) - 7.0) < 1e-12                   # agua pura: pH 7
    p = ph(h_acido_fuerte(1e-8))
    assert 6.9 < p < 7.0, p                                       # muy diluido: no 8
    x = x_debil_exacta(KA, 0.010)
    assert abs(x * x / (0.010 - x) - KA) < 1e-12                  # K = x^2/(c-x)
    assert abs(ph(x_debil_exacta(KA, 0.010)) - 2.90) < 0.01
    assert abs(14 + math.log10(x_debil_exacta(KB, 0.10)) - 11.12) < 0.01   # pH de la base: 14 - pOH


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"HCl 1e-3 M: pH = {ph(h_acido_fuerte(1e-3)):.3f} ; 1e-8 M: pH = {ph(h_acido_fuerte(1e-8)):.3f} (no 8)")
    for c in (0.010, 0.0001):
        xe, xa = x_debil_exacta(KA, c), x_debil_aprox(KA, c)
        print(f"Ácido débil Ka = {KA:.1e}, c = {c}: pH exacto = {ph(xe):.3f} ; aproximado = {ph(xa):.3f} ; "
              f"ionización = {100 * xe / c:.1f} %")
    xb = x_debil_exacta(KB, 0.10)
    print(f"Base débil Kb = {KB:.1e}, c = 0.10: pOH = {ph(xb):.3f} ; pH = {14 - ph(xb):.3f}")
    nh3, hcooh = 13.6, 4.106       # umol/g (Glavin et al. 2025)
    print(f"Bennu (extracto): NH3 = {nh3} umol/g ; HCOOH = {hcooh} umol/g ; razón NH3/HCOOH = {nh3 / hcooh:.2f}")
    print(f"Si todo el ácido fórmico reaccionara con NH3: NH4+ HCOO- = {hcooh:.3f} umol/g ; NH3 sobrante = {nh3 - hcooh:.3f} umol/g")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
