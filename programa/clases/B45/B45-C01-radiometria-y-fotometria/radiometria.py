#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C01: radiancia de Planck, exitancia, irradiancia, fotones y eficacia luminosa.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, c, k_B y sigma (todas exactas) en la tabla local allascii.txt.
T = 5772 K y R = 6,957e8 m son valores nominales propuestos para el ejemplo (no consultados aqui); 1 au = 149 597 870 700 m (exacta, definicion). La curva V(lambda) es una
gaussiana ILUSTRATIVA (maximo en 555 nm, sigma 42,5 nm), no la funcion CIE; 683 lm/W a 540 THz es la definicion SI de la candela.
Modelo: cuerpo negro de Planck; la exitancia se integra en x = hc/(lambda k T) y se compara con sigma T^4; ley del inverso del cuadrado.
Supuestos: emision isotropa y lambertiana, sin atmosfera. Validez: orden de magnitud de la eficacia luminosa solo para la forma gaussiana elegida.
Tolerancia: integral de Planck frente a pi^4/15 a 1e-6; sigma calculada frente a NIST a 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
SIGMA_NIST = 5.670374419e-8
AU = 149597870700.0
T_SUN = 5772.0
R_SUN = 6.957e8


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def planck_lambda(lam, T):
    """Radiancia espectral B_lambda en W m^-3 sr^-1."""
    x = H * C / (lam * KB * T)
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(x)


def calcular():
    r = {}
    integral = simpson(lambda x: x ** 3 / math.expm1(x), 1e-6, 60.0)
    r["integral"] = integral
    r["integral_ref"] = math.pi ** 4 / 15
    sigma_calc = 2 * math.pi ** 5 * KB ** 4 / (15 * H ** 3 * C ** 2)
    r["sigma_calc"] = sigma_calc
    r["m_exit"] = sigma_calc * T_SUN ** 4
    m_num = 2 * math.pi * KB ** 4 * T_SUN ** 4 / (H ** 3 * C ** 2) * integral
    r["m_num"] = m_num
    r["L"] = 4 * math.pi * R_SUN ** 2 * r["m_exit"]
    r["E1"] = (R_SUN / AU) ** 2 * r["m_exit"]
    r["E2"] = r["E1"] / 4
    r["Lrad"] = r["m_exit"] / math.pi
    # fotones por segundo en 1 W a 550 nm
    r["N_ph"] = 1.0 * 550e-9 / (H * C)
    # eficacia luminosa con V gaussiana ilustrativa (integral en lambda)
    def V(l):
        return math.exp(-0.5 * ((l - 555e-9) / 42.5e-9) ** 2)
    num = simpson(lambda l: V(l) * planck_lambda(l, T_SUN), 300e-9, 900e-9, 3000)
    # potencia total en 100 nm - 100 um en escala log(lambda)
    den = simpson(lambda u: planck_lambda(math.exp(u), T_SUN) * math.exp(u), math.log(50e-9), math.log(2e-4), 6000)
    r["eficacia"] = 683.0 * num / den
    r["nu_683"] = 540e12
    r["lam_683"] = C / 540e12
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"integral x^3/(e^x-1) = {r['integral']:.6f} ; pi^4/15 = {r['integral_ref']:.6f}")
    print(f"sigma calculada = {r['sigma_calc']:.9e} W m^-2 K^-4 ; NIST = {SIGMA_NIST:.9e}")
    print(f"M(5772 K) = {r['m_exit']:.6e} W/m^2 ; por integral = {r['m_num']:.6e}")
    print(f"L = {r['L']:.4e} W ; E(1 au) = {r['E1']:.2f} W/m^2 ; E(2 au) = {r['E2']:.2f} W/m^2")
    print(f"radiancia lambertiana L = M/pi = {r['Lrad']:.4e} W m^-2 sr^-1")
    print(f"fotones por segundo en 1 W a 550 nm = {r['N_ph']:.4e}")
    print(f"eficacia luminosa (V gaussiana ilustrativa) = {r['eficacia']:.1f} lm/W ; lambda(540 THz) = {r['lam_683']*1e9:.3f} nm")
    assert abs(r["integral"] - r["integral_ref"]) < 1e-6
    assert abs(r["sigma_calc"] / SIGMA_NIST - 1) < 1e-9
    assert abs(r["m_num"] / r["m_exit"] - 1) < 1e-6
    assert 1340 < r["E1"] < 1380
    assert abs(r["E2"] / r["E1"] - 0.25) < 1e-12
    assert 60 < r["eficacia"] < 110
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
