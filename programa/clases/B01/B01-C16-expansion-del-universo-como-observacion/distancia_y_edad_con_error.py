#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C16: distancia y tiempo de Hubble con incertidumbre; «no hay centro».

Datos: la galaxia de Hα de C01 (λ_obs = 662,9 nm; λ_rep = 656,3 nm; ESTIMADOS/de docencia) y dos valores
PUBLICADOS de H0: Planck 2018, 67,4 ± 0,5 km/s/Mpc (arXiv:1807.06209) y SH0ES, 73,04 ±
1,04 km/s/Mpc (arXiv:2112.04510). 1 Mpc = 3,0856775814913673e19 km (derivado de 1 au y π).
Modelo: v ≈ c z (z << 1); ley de Hubble v = H0 d; t_H = 1/H0; propagación de incertidumbre
relativa δd/d = δH0/H0 (v fija, error de z despreciable). Supuestos: la galaxia sigue la
expansión (no está ligada); incertidumbres independientes en cuadratura. Dominio de
validez: z << 1 (aquí 0,0101); t_H no es la edad del universo (C01). Tolerancias: t_H frente a
977,8/H0 al 0,01 %; igualdad exacta de la ley lineal entre observadores.
"""

from __future__ import annotations

import math
import platform
import sys

C_KMS = 299_792.458
AU_KM = 149_597_870.7
MPC_KM = AU_KM * 648_000 / math.pi * 1e6
S_ANIO = 365.25 * 86_400
Z = (662.9 - 656.3) / 656.3
H0 = {"Planck 2018": (67.4, 0.5), "SH0ES": (73.04, 1.04)}


def t_hubble_gyr(h0: float) -> float:
    return MPC_KM / h0 / S_ANIO / 1e9


def pruebas() -> None:
    assert abs(t_hubble_gyr(70.0) - 977.8 / 70.0) / (977.8 / 70.0) < 1e-4      # atajo de C01
    # «no hay centro»: la ley lineal da la misma H0 desde cualquier observador
    pos = [0.0, 10.0, 25.0, 40.0]                                              # Mpc, red 1D
    h = 70.0
    v = [h * p for p in pos]
    for i, pi in enumerate(pos):
        for j, pj in enumerate(pos):
            assert abs((v[j] - v[i]) - h * (pj - pi)) < 1e-9                   # v relativa = H·d relativa
    # el error relativo de d es el de H0 (v fija)
    d1, d2 = C_KMS * Z / 70.0, C_KMS * Z / 77.0
    assert abs(d1 / d2 - 1.1) < 1e-12


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    v = C_KMS * Z
    v_rel = C_KMS * ((1 + Z) ** 2 - 1) / ((1 + Z) ** 2 + 1)
    print(f"z = {Z:.5f}; v = c z = {v:.0f} km/s; v relativista = {v_rel:.0f} km/s (dif. {(v - v_rel) / v * 100:.2f} %)")
    res = {}
    for nombre, (h, dh) in H0.items():
        d, dd = v / h, v / h * dh / h
        t, dt = t_hubble_gyr(h), t_hubble_gyr(h) * dh / h
        res[nombre] = (h, dh)
        print(f"{nombre}: H0 = {h} ± {dh} -> d = {d:.1f} ± {dd:.1f} Mpc ; t_H = {t:.2f} ± {dt:.2f} Gyr")
    (h1, e1), (h2, e2) = res["Planck 2018"], res["SH0ES"]
    print(f"Tensión: ΔH0 = {h2 - h1:.2f}; σ = {math.hypot(e1, e2):.2f}; ΔH0/σ = {(h2 - h1) / math.hypot(e1, e2):.1f}")
    print(f"1 Mpc = {MPC_KM:.6e} km")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
