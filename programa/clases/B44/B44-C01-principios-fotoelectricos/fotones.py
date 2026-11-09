#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C01: energia del foton, longitud de corte del silicio y estadistica de Poisson.

Datos: h, c y e de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). La energia de banda prohibida del silicio (1,12 eV) es un valor
tipico de texto y es ILUSTRATIVO (no se consulto una fuente); el flujo de 1 pW y el numero de cuadros son sinteticos.
Modelo: E = h c / lambda; lambda_c = h c / E_g; tasa de fotones = P / E; conteos de Poisson con semilla 20261109 (Knuth; para media >= 30, aproximacion normal redondeada).
Supuestos: un foton absorbido libera como maximo un electron; luz monocromatica. Validez: ilustrativa.
Tolerancia: E[eV] por dos vias a 1e-9 relativo; varianza/media de Poisson dentro de 3 % en 4000 muestras.
"""
from __future__ import annotations
import math, platform, random, sys

H = 6.62607015e-34      # J s, exacta
C = 299792458.0         # m/s, exacta
Q = 1.602176634e-19     # C, exacta
H_EV = 4.135667696e-15  # eV s (NIST, valor redondeado de 4.135 667 696...)

def pois(rng, lam):
    if lam >= 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'lambda [nm]':>12} {'E [eV] (h,c,e)':>15} {'E [eV] (h_eV)':>14} {'E [J]':>12}")
    for nm in (400, 550, 700, 900, 1100):
        lam = nm * 1e-9
        e1 = H * C / lam / Q
        e2 = H_EV * C / lam
        print(f"{nm:12d} {e1:15.4f} {e2:14.4f} {H*C/lam:12.4e}")
        assert abs(e1 - e2) / e1 < 1e-9
    eg = 1.12
    lc = H * C / (eg * Q) * 1e9
    print(f"longitud de corte del silicio (E_g = 1.12 eV, ilustrativo): {lc:.1f} nm")
    assert abs(lc - 1107.0) < 1.0
    rate = 1e-12 / (H * C / 550e-9)
    print(f"tasa de fotones de 1 pW a 550 nm: {rate:.4e} fotones/s")
    assert abs(rate / 2.7686e6 - 1) < 1e-3
    rng = random.Random(20261109)
    print(f"{'media':>6} {'media muestral':>15} {'var/media':>10}")
    for lam in (4.0, 20.0, 100.0):
        xs = [pois(rng, lam) for _ in range(4000)]
        m = sum(xs) / len(xs)
        v = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
        print(f"{lam:6.1f} {m:15.3f} {v/m:10.3f}")
        assert abs(m / lam - 1) < 0.03 and abs(v / m - 1) < 0.08
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
