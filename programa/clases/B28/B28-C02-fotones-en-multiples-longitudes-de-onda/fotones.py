#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C02: fotones de radio a gamma: conversiones, ley de Planck y desplazamiento de Wien.

Datos: h, c, k_B, sigma_SB, constantes de desplazamiento de Wien y e (NIST CODATA 2022), consultados 2026-11-09;
temperatura efectiva solar nominal 5772 K (IAU 2015 B3, consultada 2026-11-09). Las energias de las bandas son
ILUSTRATIVAS (valores representativos, no limites oficiales).
Modelo: B_nu(T) = 2 h nu^3/c^2 /(exp(h nu/kT) - 1); B_lambda = 2 h c^2/lambda^5 /(exp(hc/lambda kT) - 1).
Integral total Int B_nu dnu = sigma T^4/pi; maximos de B_nu y B_lambda por razon aurea, comparados con las constantes de Wien.
Supuestos: cuerpo negro ideal. Validez: equilibrio termico.
Tolerancia: 1e-9 en la integral de Planck; 1e-6 en los maximos de Wien (el maximo es plano).
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB, SIG, E = 6.62607015e-34, 299792458.0, 1.380649e-23, 5.670374419e-8, 1.602176634e-19
WIEN_NU, WIEN_L = 5.878925757e10, 2.897771955e-3
T_SUN = 5772.0


def b_nu(nu, t):
    return 2 * H * nu ** 3 / C ** 2 / math.expm1(H * nu / (KB * t))


def b_lam(lam, t):
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(H * C / (lam * KB * t))


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def maximo(f, a, b):
    g = (math.sqrt(5) - 1) / 2
    c_, d_ = b - g * (b - a), a + g * (b - a)
    for _ in range(300):
        if f(c_) > f(d_):
            b = d_
        else:
            a = c_
        c_, d_ = b - g * (b - a), a + g * (b - a)
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'banda':<14} {'nu [Hz]':>11} {'lambda [m]':>12} {'E [eV]':>12} {'E/k_B [K]':>12}")
    for nombre, nu in (("radio 1 GHz", 1e9), ("mm 300 GHz", 3e11), ("IR 10 um", C / 10e-6), ("optico 550 nm", C / 550e-9),
                       ("UV 100 nm", C / 100e-9), ("X 1 keV", 1e3 * E / H), ("gamma 1 MeV", 1e6 * E / H), ("gamma 1 TeV", 1e12 * E / H)):
        e_ev = H * nu / E
        print(f"{nombre:<14} {nu:11.3e} {C / nu:12.3e} {e_ev:12.4e} {H * nu / KB:12.4e}")
    t = T_SUN
    x_max = 60.0
    f = lambda x: x ** 3 / math.expm1(x) if x > 0 else 0.0
    integral = simpson(f, 1e-12, x_max, 200000) * (KB * t / H) ** 4 * 2 * H / C ** 2
    esperado = SIG * t ** 4 / math.pi
    assert abs(integral / esperado - 1) < 1e-9, "integral de Planck"
    print(f"T = {t} K: Int B_nu dnu = {integral:.6e} W m-2 sr-1 ; sigma T^4/pi = {esperado:.6e} ; flujo sigma T^4 = {SIG * t ** 4:.4e} W/m2")
    nu_p = maximo(lambda nu: b_nu(nu, t), 1e12, 2e15)
    lam_p = maximo(lambda lam: b_lam(lam, t), 1e-7, 5e-6)
    assert abs(nu_p / (WIEN_NU * t) - 1) < 1e-6 and abs(lam_p * t / WIEN_L - 1) < 1e-6, "constantes de Wien"
    print(f"maximo de B_nu: nu = {nu_p:.4e} Hz (Wien: {WIEN_NU * t:.4e}) ; maximo de B_lambda: lambda = {lam_p * 1e9:.2f} nm (Wien: {WIEN_L / t * 1e9:.2f})")
    print(f"los dos maximos no coinciden: c/nu_max = {C / nu_p * 1e9:.1f} nm frente a lambda_max = {lam_p * 1e9:.1f} nm")
    print(f"{'T [K]':>9} {'lambda_max':>12} {'banda del maximo':>18}")
    for tt in (2.7255, 300.0, 5772.0, 1e4, 1e7, 1e9):
        lm = WIEN_L / tt
        banda = "radio-mm" if lm > 1e-4 else "IR" if lm > 7.5e-7 else "optico" if lm > 4e-7 else "UV" if lm > 1e-8 else "X" if lm > 1e-11 else "gamma"
        print(f"{tt:9.4g} {lm:12.3e} {banda:>18}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
