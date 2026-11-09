#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C22: energia del dipolo terrestre, relacion de Dessler-Parker-Sckopke y corriente del anillo.

Datos: mu_0 y m_p (NIST CODATA 2022); R_E ecuatorial (IAU 2015 B3), consultados 2026-11-09. El campo ecuatorial superficial B_0 = 3.12e-5 T, las perturbaciones (-30, -100, -300 nT),
la energia media de los iones (100 keV) y el radio del anillo (4 R_E) son ILUSTRATIVOS (sinteticos); las perturbaciones no corresponden a ninguna clasificacion de tormentas.
Modelo: energia magnetica del dipolo fuera de la Tierra W = (4 pi/(3 mu_0)) B_0^2 R_E^3, verificada con integracion numerica 2D; relacion de Dessler-Parker-Sckopke
Delta B/B_0 = -(2/3) E_RC/W_dip; numero de iones N = E_RC/<E> y masa; corriente de un anillo circular de radio a que da Delta B en su centro: I = 2 a Delta B/mu_0.
Supuestos: dipolo centrado, anillo simetrico, energia cinetica de las particulas igual a la del anillo. Validez: orientativa.
Tolerancia: integracion numerica (regla del punto medio, 400 x 400) frente a la forma cerrada dentro de 1e-5; relacion inversa E_RC -> Delta B a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

MU0, MP, Q = 1.25663706127e-6, 1.67262192595e-27, 1.602176634e-19
R_E, B0 = 6.3781e6, 3.12e-5


def w_dip():
    return 4 * math.pi / (3 * MU0) * B0 ** 2 * R_E ** 3


def w_dip_numerica(nu=400, nth=400):
    # u = R/r en (0, 1], theta en (0, pi): integrando B^2/(2 mu_0) r^2 sen(theta) dr dtheta dphi con B = B0 u^3 sqrt(1 + 3 cos^2 theta)
    s = 0.0
    hu, ht = 1.0 / nu, math.pi / nth
    for i in range(nu):
        u = (i + 0.5) * hu
        for j in range(nth):
            th = (j + 0.5) * ht
            s += B0 ** 2 * u ** 2 * (1 + 3 * math.cos(th) ** 2) * math.sin(th) * hu * ht
    return 2 * math.pi * R_E ** 3 * s / (2 * MU0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    w = w_dip()
    wn = w_dip_numerica()
    print(f"energia del dipolo fuera de la Tierra: forma cerrada = {w:.4e} J ; integracion numerica 2D = {wn:.4e} J ; cociente = {wn / w:.8f}")
    assert abs(wn / w - 1) < 1e-5
    print(f"{'Delta B [nT]':>12} {'E_RC [J]':>12} {'E_RC/W_dip':>11} {'N (100 keV)':>13} {'masa [kg]':>10} {'I (a = 4 R_E) [MA]':>19}")
    for db in (-30e-9, -100e-9, -300e-9):
        e_rc = -1.5 * w * db / B0
        back = -(2 / 3) * e_rc / w * B0
        assert abs(back / db - 1) < 1e-12
        n = e_rc / (100e3 * Q)
        masa = n * MP
        i_a = 2 * 4 * R_E * abs(db) / MU0
        print(f"{db * 1e9:12.0f} {e_rc:12.3e} {e_rc / w:11.3%} {n:13.3e} {masa:10.1f} {i_a / 1e6:19.2f}")
    print(f"B_0 = {B0 * 1e9:.0f} nT: una perturbacion de -100 nT equivale a {100e-9 / B0:.3%} del campo ecuatorial")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
