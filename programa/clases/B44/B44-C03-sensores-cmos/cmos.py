#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C03: ruido kTC, muestreo doble correlacionado (CDS) y desplazamiento del obturador rodante en un CMOS.

Datos: k_B y e de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). La capacidad de 10 fF, la temperatura de 300 K, el tiempo por fila y la velocidad son
ILUSTRATIVOS (sinteticos); no describen ningun sensor real.
Modelo: ruido de reset sigma_q = sqrt(k T C) / e (electrones); CDS resta la lectura de reset de la lectura de senal; obturador rodante: desplazamiento = v * N_filas * t_fila.
Supuestos: el ruido de reset es el mismo en las dos lecturas del mismo pixel; ruido de lectura posterior independiente. Validez: ilustrativa.
Tolerancia: sigma kTC simulada dentro de 3 % del valor analitico; tras CDS el residuo es solo el ruido de lectura.
"""
from __future__ import annotations
import math, platform, random, sys

KB = 1.380649e-23
E = 1.602176634e-19

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    T, Cf = 300.0, 10e-15
    sk = math.sqrt(KB * T * Cf) / E
    print(f"ruido kTC (T = 300 K, C = 10 fF): {sk:.2f} e- rms")
    for c in (1e-15, 10e-15, 100e-15):
        print(f"  C = {c*1e15:6.1f} fF -> {math.sqrt(KB*T*c)/E:7.2f} e-")
    assert abs(sk - 40.17) < 0.05
    rng = random.Random(20261109)
    n, rn = 20000, 2.0
    sin_cds, con_cds = [], []
    for _ in range(n):
        reset = rng.gauss(0, sk)            # ruido de reset (se congela en el pixel)
        sig = 100.0
        lect_reset = reset + rng.gauss(0, rn)
        lect_sig = reset + sig + rng.gauss(0, rn)
        sin_cds.append(lect_sig - 100.0)
        con_cds.append(lect_sig - lect_reset - 100.0)
    def sd(xs):
        m = sum(xs) / len(xs)
        return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    s1, s2 = sd(sin_cds), sd(con_cds)
    print(f"sin CDS: {s1:.2f} e-   con CDS: {s2:.2f} e-   (esperado {math.hypot(sk, rn):.2f} y {math.sqrt(2)*rn:.2f})")
    assert abs(s1 / math.hypot(sk, rn) - 1) < 0.03
    assert abs(s2 / (math.sqrt(2) * rn) - 1) < 0.03
    # obturador rodante: barra vertical que se mueve a v px/s, filas leidas cada t_fila
    nfil, tfil, v = 1000, 20e-6, 5000.0
    despl = v * nfil * tfil
    x0 = 100.0
    pos = [x0 + v * i * tfil for i in range(nfil)]
    print(f"desplazamiento entre primera y ultima fila: analitico {despl:.1f} px, simulado {pos[-1]-pos[0]+v*tfil:.1f} px")
    assert abs((pos[-1] - pos[0]) - v * (nfil - 1) * tfil) < 1e-9
    assert abs(despl - 100.0) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
