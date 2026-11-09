#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C04: perfil de Voigt por integracion numerica y anchos Doppler.

Datos: k_B, m_p, c (NIST CODATA 2022), consultados 2026-11-09. La longitud de onda (656.28 nm), la temperatura (5772 K, UAI 2015 B3) y los parametros de amortiguamiento (a = 0, 0.01, 0.1, 1) son ILUSTRATIVOS.
Modelo: H(a, v) = (a/pi) Int exp(-y^2)/((v - y)^2 + a^2) dy por Simpson; limites: H(0, v) = exp(-v^2), H(a, 0) = exp(a^2) erfc(a), alas H ~ a/(sqrt(pi) v^2) para v grande;
normalizacion Int H dv = sqrt(pi); ancho Doppler Delta lambda_D = (lambda/c) sqrt(2 k T/m).
Supuestos: perfil de un solo absorbedor, sin gradientes. Validez: ideal.
Tolerancia: H(0,v) a 1e-9; H(a, 0) frente a exp(a^2) erfc(a) a 1e-6; normalizacion a 5e-3; alas a 1e-2.
"""
from __future__ import annotations
import math, platform, sys
KB, MP, C = 1.380649e-23, 1.67262192595e-27, 299792458.0

def voigt(a, v, ymax=40.0, n=40000):
    if a == 0:
        return math.exp(-v * v)
    h = 2 * ymax / n
    f = lambda y: math.exp(-y * y) / ((v - y) ** 2 + a * a)
    s = f(-ymax) + f(ymax)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(-ymax + i * h)
    return a / math.pi * s * h / 3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    vth = math.sqrt(2 * KB * 5772 / MP)
    print(f"velocidad termica del hidrogeno a 5772 K = {vth / 1e3:.3f} km/s ; Delta lambda_D (656.28 nm) = {656.28e-9 / C * vth * 1e9:.5f} nm")
    print(f"{'v':>5} " + "".join(f"{'a = ' + str(a):>12}" for a in (0, 0.01, 0.1, 1)))
    for v in (0.0, 1.0, 3.0, 10.0):
        print(f"{v:5.1f} " + "".join(f"{voigt(a, v):12.6f}" for a in (0, 0.01, 0.1, 1)))
    assert abs(voigt(0, 2.0) - math.exp(-4)) < 1e-9
    for a in (0.01, 0.1, 1.0):
        ana = math.exp(a * a) * math.erfc(a)
        assert abs(voigt(a, 0.0) / ana - 1) < 1e-6, a
    print(f"H(a, 0) frente a exp(a^2) erfc(a): a = 0.1 -> {voigt(0.1, 0.0):.6f} vs {math.exp(0.01) * math.erfc(0.1):.6f}")
    tot = sum(voigt(0.1, -30 + (i + 0.5) * 0.1, n=4000) * 0.1 for i in range(600))
    print(f"normalizacion Int H dv (a = 0.1, |v| < 30) = {tot:.5f} ; sqrt(pi) = {math.sqrt(math.pi):.5f}")
    assert abs(tot / math.sqrt(math.pi) - 1) < 5e-3
    v = 30.0
    print(f"ala en v = 30: H = {voigt(0.1, v):.4e} ; a/(sqrt(pi) v^2) = {0.1 / (math.sqrt(math.pi) * v * v):.4e}")
    assert abs(voigt(0.1, v) / (0.1 / (math.sqrt(math.pi) * v * v)) - 1) < 1e-2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
