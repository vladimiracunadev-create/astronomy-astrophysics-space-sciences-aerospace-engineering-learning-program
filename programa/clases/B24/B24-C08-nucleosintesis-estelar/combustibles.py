#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C08: energia de los combustibles estelares y una cadena de quemado de helio.

Datos (NIST CODATA 2022, consultados 2026-11-09): masas de proton, alfa y electron en u;
equivalente en MeV de la u. La masa atomica del carbono-12 es exactamente 12 u por definicion
de la unidad. La masa atomica del He-4 se toma como m_alfa + 2 m_e (se desprecia la energia de
ligadura electronica, ~79 eV). Tasa de reaccion r del triple alfa: valor SINTETICO.
Modelo: (1) Q del triple alfa, 3 He-4 -> C-12, y su fraccion de masa; comparacion con el quemado
de hidrogeno. (2) Abundancia de He bajo el triple alfa: dY/dt = -3 r Y^3, con solucion exacta
Y(t) = Y0 / sqrt(1 + 6 r Y0^2 t), integrada con RK4.
Supuestos: solo triple alfa (sin C12+alfa -> O16); tasa r constante. Validez: ilustrativa.
Tolerancia: 1e-6 entre el Q por kg y por u; 1e-8 en la integracion RK4.
"""
from __future__ import annotations
import platform
import sys

U_MEV = 931.49410372
MP_U, MA_U, ME_U = 1.007276466579, 4.001506179129, 5.485799090e-4
U_KG, EV, C = 1.66053906892e-27, 1.602176634e-19, 299792458.0


def q_triple_alfa_u():
    he4 = MA_U + 2 * ME_U
    return (3 * he4 - 12.0) * U_MEV, (3 * he4 - 12.0) / (3 * he4)


def q_triple_alfa_kg():
    he4 = (MA_U + 2 * ME_U) * U_KG
    dm = 3 * he4 - 12 * U_KG
    return dm * C * C / EV / 1e6


def q_h():
    dm = 4 * MP_U + 4 * ME_U - (MA_U + 2 * ME_U)
    return dm * U_MEV, dm / (4 * MP_U + 4 * ME_U)


def y_exacta(y0, r, t):
    return y0 / (1 + 6 * r * y0 * y0 * t) ** 0.5


def y_rk4(y0, r, t, n=2000):
    f = lambda y: -3 * r * y ** 3
    h, y = t / n, y0
    for _ in range(n):
        k1 = f(y); k2 = f(y + h * k1 / 2); k3 = f(y + h * k2 / 2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    qa, ea = q_triple_alfa_u()
    qb = q_triple_alfa_kg()
    assert abs(qa / qb - 1) < 1e-6, "Q del triple alfa: via u y via kg difieren"
    qh, eh = q_h()
    assert 7.2 < qa < 7.35, "Q triple alfa fuera de rango"
    ratio = eh / ea
    print(f"Q(3 alfa -> C12) = {qa:.4f} MeV (via kg {qb:.4f}) ; fraccion de masa = {ea:.6f}")
    print(f"Q(4 H -> He4)    = {qh:.4f} MeV ; fraccion de masa = {eh:.6f}")
    print(f"energia por unidad de masa: H/He = {ratio:.1f}")
    y0, r, t = 1.0, 1.0e-3, 50.0
    ye, yn = y_exacta(y0, r, t), y_rk4(y0, r, t)
    assert abs(yn / ye - 1) < 1e-8, "RK4 no reproduce la solucion exacta"
    print(f"Y(t=50) exacta = {ye:.8f} ; RK4 = {yn:.8f} (Y0=1, r=1e-3, sinteticos)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
