#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C06: trabajo, energía cinética y energía potencial gravitatoria.

Datos: GM = 3,9860e14 m³/s² y R = 6 378 137 m (NASA NSSDC, Earth Fact Sheet);
masa del satélite 1000 kg (SINTÉTICA). Modelo: gravedad puntual; trabajo de una fuerza
central por integración numérica (regla del trapecio) frente a la fórmula cerrada
W = -(Ep2 - Ep1). Supuestos: sin rotación terrestre, sin atmósfera.
Dominio de validez: r > R. Tolerancia: 1e-6 relativa.
"""
from __future__ import annotations
import math
import sys

GM = 3.9860e14
R = 6_378_137.0
M = 1000.0

def ep(r: float) -> float:
    return -GM * M / r

def trabajo_gravedad_numerico(r1: float, r2: float, n: int = 100_000) -> float:
    """Trabajo de la gravedad al ir de r1 a r2 en línea radial: integral de -GMm/r² dr."""
    h = (r2 - r1) / n
    f = [-GM * M / (r1 + i * h) ** 2 for i in range(n + 1)]
    return h * (sum(f) - 0.5 * (f[0] + f[-1]))

def main() -> int:
    r2 = R + 400_000.0
    w_num = trabajo_gravedad_numerico(R, r2)
    w_ana = -(ep(r2) - ep(R))
    assert abs(w_num - w_ana) / abs(w_ana) < 1e-6, (w_num, w_ana)
    # teorema trabajo-energía: Ec2 = Ec1 + W
    v0 = 3000.0
    v2 = math.sqrt(v0**2 + 2 * w_ana / M)
    assert abs(0.5 * M * v2**2 - (0.5 * M * v0**2 + w_ana)) < 1e-3
    v = math.sqrt(GM / r2)
    ec, e_pot = 0.5 * M * v**2, ep(r2)
    e_tot = ec + e_pot
    assert abs(e_tot + ec) < 1e-9 * ec          # en órbita circular E = -Ec
    e_sup = ep(R)                                 # reposo en R (sin rotación)
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Trabajo de la gravedad de R a R+400 km: {w_num:.4e} J (analítico {w_ana:.4e} J)")
    print(f"Órbita 400 km: Ec = {ec:.4e} J; Ep = {e_pot:.4e} J; E = {e_tot:.4e} J")
    print(f"Energía necesaria desde reposo en la superficie: {e_tot - e_sup:.4e} J ({(e_tot - e_sup)/M/1e6:.2f} MJ/kg)")
    print(f"  para subir (Ep): {e_pot - e_sup:.4e} J; para la rapidez orbital (Ec): {ec:.4e} J")
    print(f"Con g_n y h constante (aproximación): m g h = {M*9.80665*400_000:.4e} J")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
