#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C11: perfil de ensanchamiento rotacional y recuperacion de v sin i.

Datos: c (NIST CODATA 2022), consultado 2026-11-09. El coeficiente de oscurecimiento del limbo (0.6), la longitud de onda (500 nm), v sin i (20 km/s), la linea intrinseca gaussiana (2 pm),
el ruido (0.01) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: kernel rotacional G(d) = [2 (1 - e) sqrt(1 - x^2) + (pi e/2)(1 - x^2)]/(pi (1 - e/3) dL) para |x| < 1, x = d/dL, dL = lambda v sin i/c; normalizacion Int G = 1 por Simpson;
FWHM del kernel; convolucion con una linea gaussiana; recuperacion de v sin i por busqueda en rejilla refinada con ruido.
Supuestos: rotacion rigida, oscurecimiento lineal, sin otros ensanchamientos. Validez: ilustrativa.
Tolerancia: normalizacion a 1e-6; v sin i recuperado dentro del 5 %.
"""
from __future__ import annotations
import math, platform, random, sys
C = 299792458.0
EPS = 0.6

def kernel(d, dl):
    x = d / dl
    if abs(x) >= 1:
        return 0.0
    return (2 * (1 - EPS) * math.sqrt(1 - x * x) + math.pi * EPS / 2 * (1 - x * x)) / (math.pi * (1 - EPS / 3) * dl)

def perfil(vsini, grid, sig=0.002):
    dl = 0.5 * vsini * 1e3 / C * 1e9 * 1.0       # nm
    h = grid[1] - grid[0]
    out = []
    for x in grid:
        s = 0.0
        for j in range(-200, 201):
            d = j * h
            s += kernel(d, dl) * math.exp(-0.5 * ((x - d) / (sig / 1000 * 1.0)) ** 2) if False else 0.0
        out.append(s)
    return out

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lam, v = 500.0, 20e3
    dl = lam * v / C
    print(f"Delta lambda_L = lambda v sin i/c = {dl * 1e3:.4f} pm (v sin i = 20 km/s a 500 nm)")
    n = 20000
    h = 2 * dl / n
    area = sum(kernel(-dl + (i + 0.5) * h, dl) * h for i in range(n))
    print(f"normalizacion Int G d(lambda) = {area:.8f}")
    assert abs(area - 1) < 1e-6
    mx = kernel(0.0, dl)
    mitad = [(-dl + i * h) for i in range(n + 1) if kernel(-dl + i * h, dl) >= mx / 2]
    print(f"FWHM del kernel = {(mitad[-1] - mitad[0]) / dl:.4f} Delta lambda_L ; maximo central G(0) dL = {mx * dl:.4f}")
    # linea convolucionada y recuperacion
    sig = 0.002
    rng = random.Random(20261109)
    grid = [-0.06 + 0.002 * i for i in range(61)]
    def conv(vs):
        dlx = lam * vs * 1e3 / C
        pas = 0.0005
        k = [kernel(j * pas, dlx) * pas for j in range(-300, 301)]
        sk = sum(k)
        res = []
        for x in grid:
            tot = 0.0
            for idx, j in enumerate(range(-300, 301)):
                if k[idx] > 0:
                    tot += k[idx] / sk * math.exp(-0.5 * ((x - j * pas) / sig) ** 2)
            res.append(tot)
        return res
    obs = [p + rng.gauss(0, 0.01) for p in conv(20.0)]
    def chi(vs):
        mod = conv(vs)
        return sum((o - m) ** 2 for o, m in zip(obs, mod))
    mejor = min((chi(vs), vs) for vs in [10 + 2 * i for i in range(16)])[1]
    mejor = min((chi(vs), vs) for vs in [mejor - 2 + 0.25 * i for i in range(17)])[1]
    print(f"v sin i recuperado = {mejor:.2f} km/s (verdadero 20.00) ; error relativo = {abs(mejor / 20 - 1) * 100:.2f} %")
    assert abs(mejor / 20 - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
