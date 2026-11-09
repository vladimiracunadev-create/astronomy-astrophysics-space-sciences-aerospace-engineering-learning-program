#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C21: magnetografo, desdoblamiento Zeeman, parametro de Stokes V y recuperacion del campo longitudinal.

Datos: magneton de Bohr 9,2740100657e-24 J/T, h y c de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). ILUSTRATIVOS (no son los parametros de ningun instrumento ni de una linea
medida): linea de absorcion gaussiana en 617,33 nm con profundidad 0,6 y sigma 0,04 nm, factor de Lande efectivo 2,5, seis posiciones espectrales a -0,10, -0,06, -0,02, +0,02, +0,06 y +0,10 nm,
ruido de 1e-3 del continuo en V y campos de 100 a 3000 G. Un fragmento de busqueda (no leido) menciona que un magnetografo orbital real usa una linea de Fe I cerca de 6173 angstrom; no se usa ningun valor de ese instrumento.
Modelo: (1) desdoblamiento Delta lambda_B = g mu_B B lambda^2/(h c), contrastado con la constante 4,67e-13 g lambda^2[A] B[G] A; (2) componentes circulares I_pm(lambda) = I(lambda -+ Delta lambda_B)
y V = (I_+ - I_-)/2; (3) aproximacion de campo debil V = -Delta lambda_B dI/dlambda y estimador de minimos cuadrados B = -sum(V dI)/(k sum dI^2) con k = Delta lambda_B por gauss;
(4) Monte Carlo con ruido (semilla 20261109) frente a la dispersion analitica sigma_V/(k sqrt(sum dI^2)).
Supuestos: campo longitudinal uniforme, sin gradientes de velocidad ni ensanchamiento adicional, perfil gaussiano, sin polarizacion lineal. Validez: ilustrativa.
Tolerancia: constante Zeeman a 1e-3 de 4,67e-13; recuperacion en campo debil (100 G) a 1 %; dispersion Monte Carlo a 5 % de la analitica.
"""
from __future__ import annotations
import math, platform, random

MUB = 9.2740100657e-24
H = 6.62607015e-34
C = 299792458.0
LAM0, G, DEPTH, SIG = 617.33e-9, 2.5, 0.6, 0.04e-9
POS = [-0.10e-9, -0.06e-9, -0.02e-9, 0.02e-9, 0.06e-9, 0.10e-9]


def perfil(lam):
    return 1 - DEPTH * math.exp(-(lam - LAM0) ** 2 / (2 * SIG ** 2))


def dperfil(lam):
    return DEPTH * (lam - LAM0) / SIG ** 2 * math.exp(-(lam - LAM0) ** 2 / (2 * SIG ** 2))


def delta_b(b_gauss):
    return G * MUB * (b_gauss * 1e-4) * LAM0 ** 2 / (H * C)


def stokes_v(lam, b_gauss):
    d = delta_b(b_gauss)
    return 0.5 * (perfil(lam - d) - perfil(lam + d))


def estimador(vs, k):
    di = [dperfil(LAM0 + p) for p in POS]
    return -sum(v * x for v, x in zip(vs, di)) / (k * sum(x * x for x in di))


def calc():
    r = {}
    # constante en angstrom por gauss y por angstrom^2 de lambda^2: dlambda[A] = k lambda[A]^2 B[G] g
    k_ang = MUB / (H * C) * 1e-4 * 1e-10        # [1/(m G)] * [m/A]: da A-1 G-1 al multiplicar por g lambda^2 en A^2 se obtiene A por gauss
    r["cte"] = k_ang
    r["dl_1000"] = delta_b(1000.0) * 1e9
    k = delta_b(1.0)                              # metros por gauss
    r["k_pm"] = k * 1e12
    r["rec"] = {}
    for b in (100, 500, 1000, 3000):
        vs = [stokes_v(LAM0 + p, b) for p in POS]
        r["rec"][b] = (estimador(vs, k), vs)
    di = [dperfil(LAM0 + p) for p in POS]
    sv = 1e-3
    r["sigma_an"] = sv / (k * math.sqrt(sum(x * x for x in di)))
    rng = random.Random(20261109)
    est = []
    for _ in range(5000):
        vs = [stokes_v(LAM0 + p, 100.0) + rng.gauss(0, sv) for p in POS]
        est.append(estimador(vs, k))
    m = sum(est) / len(est)
    r["mc_mean"] = m
    r["mc_sd"] = math.sqrt(sum((x - m) ** 2 for x in est) / (len(est) - 1))
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    cte = r["cte"]
    print(f"mu_B/(h c) por gauss = {cte:.4e} A-1 G-1 (referencia 4.67e-13 con g lambda^2 en A^2)")
    print(f"desdoblamiento para B = 1000 G: {r['dl_1000']:.5f} nm ; k = {r['k_pm']:.4f} pm/G")
    print(f"{'B [G]':>6} {'B recuperado [G]':>17} {'error [%]':>10}")
    for b, (e, vs) in r["rec"].items():
        print(f"{b:6d} {e:17.2f} {100*(e-b)/b:10.2f}")
    print(f"Stokes V (B = 1000 G) en las 6 posiciones: " + " ".join(f"{v:+.4f}" for v in r["rec"][1000][1]))
    print(f"ruido 1e-3 en V y B = 100 G: media = {r['mc_mean']:.2f} G ; desviacion MC = {r['mc_sd']:.2f} G ; analitica = {r['sigma_an']:.2f} G")
    assert abs(r["cte"] - 4.67e-13) / 4.67e-13 < 1e-3
    assert abs(r["rec"][100][0] - 100) / 100 < 0.01
    assert abs(r["mc_sd"] - r["sigma_an"]) / r["sigma_an"] < 0.05
    assert abs(r["rec"][3000][0]) < 3000
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
