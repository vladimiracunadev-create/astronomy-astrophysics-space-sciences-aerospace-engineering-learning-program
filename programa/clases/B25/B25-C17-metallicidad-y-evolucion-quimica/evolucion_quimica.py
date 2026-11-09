#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C17: modelo de caja cerrada y con salida de gas de la evolucion quimica.

Datos: composicion solar de la fotosfera X = 0,7381, Y = 0,2485, Z = 0,0134 (Asplund et al. 2009,
arXiv:0909.0948, texto del PDF consultado 2026-11-09): OBSERVADOS/ESTIMADOS. El rendimiento (yield) efectivo
y = 0,010, las cargas de masa lambda y las fracciones de gas son SINTETICOS/ILUSTRATIVOS.
Modelo: reciclaje instantaneo; cada masa dM_s formada devuelve al gas una masa de metales y dM_s;
(a) caja cerrada: Z = y ln(1/mu), mu = fraccion de gas; (b) con salida de gas lambda dM_s a la
metalicidad del gas: Z = y/(1+lambda) ln(1/mu) con mu = 1 - (1+lambda) s.
Supuestos: mezcla instantanea, sin entrada de gas, rendimiento constante, gas inicial sin metales.
Validez: orden de magnitud cualitativo; las galaxias reales tienen entrada de gas y mezcla finita.
Tolerancias: 1e-9 (RK4 frente a la solucion exacta con 20000 pasos) y 1e-12 (algebra).
"""
from __future__ import annotations
import math
import platform
import sys

Z_SOL = 0.0134
Y_EFF = 0.010


def z_caja(mu, y=Y_EFF):
    return y * math.log(1 / mu)


def z_salida(mu, lam, y=Y_EFF):
    return y / (1 + lam) * math.log(1 / mu)


def rk4_z(s_fin, lam, y=Y_EFF, n=20000):
    """Integra dZ/ds = y / (1 - (1+lam) s) de s = 0 a s_fin con RK4."""
    f = lambda s, z: y / (1 - (1 + lam) * s)
    h = s_fin / n
    s, z = 0.0, 0.0
    for _ in range(n):
        k1 = f(s, z)
        k2 = f(s + h / 2, z + h / 2 * k1)
        k3 = f(s + h / 2, z + h / 2 * k2)
        k4 = f(s + h, z + h * k3)
        z += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        s += h
    return z


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: caja cerrada, RK4 frente a la solucion exacta, para s = 0,7 (mu = 0,3)
    assert abs(rk4_z(0.7, 0.0) / z_caja(0.3) - 1) < 1e-9
    # Prueba 2: con salida (lambda = 1, s = 0,35 -> mu = 0,3)
    assert abs(rk4_z(0.35, 1.0) / z_salida(0.3, 1.0) - 1) < 1e-9
    # Prueba 3: identidad Z_salida(lambda) = Z_caja / (1 + lambda) a igual mu
    for lam in (0.5, 1.0, 3.0):
        assert abs(z_salida(0.3, lam) * (1 + lam) / z_caja(0.3) - 1) < 1e-12
    # Prueba 4: masa de metales conservada en la caja cerrada: Z mu + (metales en estrellas) = y s
    mu = 0.3
    s = 1 - mu
    n = 20000
    h = s / n
    metales_estrellas = sum(z_caja(1 - (i + 0.5) * h) * h for i in range(n))  # int Z ds
    metales_gas = z_caja(mu) * mu
    assert abs((metales_estrellas + metales_gas) / (Y_EFF * s) - 1) < 1e-6
    print(f"Z_sol = {Z_SOL} ; y_eff ilustrativo = {Y_EFF}")
    for mu_ in (0.9, 0.5, 0.3, 0.1, 0.03):
        zc = z_caja(mu_)
        print(f"caja cerrada: mu = {mu_:4.2f} -> Z = {zc:.4f} = {zc / Z_SOL:.2f} Z_sol ; log10(Z/Zsol) = {math.log10(zc / Z_SOL):+.2f}")
    for lam in (0.0, 1.0, 3.0):
        z = z_salida(0.3, lam)
        print(f"salida lambda = {lam:.0f}, mu = 0.30: Z = {z:.4f} = {z / Z_SOL:.2f} Z_sol ; log10 = {math.log10(z / Z_SOL):+.2f}")
    print(f"fraccion de los metales producidos que queda en estrellas (mu = 0.3): {metales_estrellas / (Y_EFF * s):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
