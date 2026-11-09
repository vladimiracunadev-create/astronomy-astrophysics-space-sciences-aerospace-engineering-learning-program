#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C07: aluminizado: reflectancia, espesor opaco y uniformidad de una evaporacion con fuente puntual.

Datos: ILUSTRATIVOS (indice complejo del aluminio a 550 nm N = 0,96 - 6,69 i, valor tipico de la literatura NO consultado aqui; sustrato de vidrio n = 1,52; evaporador puntual a 400 mm; espejo de 200 mm).
Modelo: reflectancia a incidencia normal R = ((n-1)^2 + k^2)/((n+1)^2 + k^2); pelicula delgada sobre sustrato por matriz de transferencia de una capa; atenuacion aproximada exp(-4 pi k d/lambda).
Uniformidad: espesor proporcional a h/(h^2 + rho^2)^(3/2) (fuente puntual isotropa sobre un plano) frente a una simulacion Monte Carlo de direcciones isotropas (semilla 20261109).
Supuestos: pelicula homogenea y lisa, incidencia normal, un solo evaporador puntual, sin rotacion del sustrato. Validez: ilustrativa.
Tolerancia: R de la capa muy gruesa frente a la formula del metal macizo, 1e-4; T de la matriz de transferencia entre 0,4 y 0,5 veces la atenuacion exponencial para d >= 40 nm (el factor es la transmision de las interfaces); Monte Carlo frente a la integral, 4 %.
"""
from __future__ import annotations
import cmath, math, platform, random

LAM = 550.0
NAL = complex(0.96, -6.69)
NS = 1.52

def capa(d_nm, N=NAL, ns=NS, lam=LAM):
    delta = 2 * math.pi * N * d_nm / lam
    c = cmath.cos(delta); s = cmath.sin(delta)
    B = c + 1j * s / N * ns
    C = 1j * N * s + c * ns
    Y = C / B
    R = abs((1 - Y) / (1 + Y)) ** 2
    T = 4 * 1 * ns / abs(B + C) ** 2
    return R, T

def densidad(rho, h=400.0):
    return h / (h * h + rho * rho) ** 1.5

def integral_media(r0, r1, h=400.0, n=4000):
    # media de densidad en la corona [r0, r1] (ponderada por area)
    num = den = 0.0
    dr = (r1 - r0) / n
    for i in range(n):
        r = r0 + (i + 0.5) * dr
        num += densidad(r, h) * r * dr; den += r * dr
    return num / den

def calc():
    r = {}
    n, k = NAL.real, -NAL.imag
    r["R_macizo"] = ((n - 1) ** 2 + k ** 2) / ((n + 1) ** 2 + k ** 2)
    r["profundidad_nm"] = LAM / (4 * math.pi * k)
    filas = []
    for d in (10, 20, 40, 60, 80, 100, 150):
        R, T = capa(d)
        filas.append((d, R, T, math.exp(-4 * math.pi * k * d / LAM)))
    r["filas"] = filas
    r["R_grueso"] = capa(1000)[0]
    # espesor opaco: T < 0,1 %
    d = 1
    while capa(d)[1] > 1e-3:
        d += 1
    r["d_opaco_nm"] = d
    # uniformidad
    h = 400.0
    r["borde_sobre_centro"] = densidad(100.0, h) / densidad(0.0, h)
    rng = random.Random(20261109)
    cmax = h / math.hypot(h, 100.0)
    ni = no = 0; N = 400000
    for _ in range(N):
        c = rng.uniform(cmax, 1.0)
        rho = h * math.sqrt(1 - c * c) / c
        if rho < 50.0:
            ni += 1
        else:
            no += 1
    # densidad por unidad de area ~ n/area de la corona
    dens_in = ni / (math.pi * 50.0 ** 2); dens_out = no / (math.pi * (100.0 ** 2 - 50.0 ** 2))
    r["mc_cociente"] = dens_out / dens_in
    r["analitico_cociente"] = integral_media(50.0, 100.0, h) / integral_media(0.0, 50.0, h)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("d (nm) | R capa | T capa | exp(-4 pi k d/lambda)")
    for d, R, T, e in r["filas"]:
        print(f"{d} | {R:.4f} | {T:.3e} | {e:.3e}")
    for k in ("R_macizo", "profundidad_nm", "R_grueso", "d_opaco_nm", "borde_sobre_centro", "mc_cociente", "analitico_cociente"):
        print(f"{k} = {r[k]:.6g}")
    assert abs(r["R_grueso"] - r["R_macizo"]) < 1e-4
    for d, R, T, e in r["filas"]:
        if d >= 40:
            assert 0.4 < T / e < 0.5
    assert abs(r["mc_cociente"] - r["analitico_cociente"]) / r["analitico_cociente"] < 0.04
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
