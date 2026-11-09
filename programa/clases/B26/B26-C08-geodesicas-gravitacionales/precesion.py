#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C08: precesion del perihelio por integracion numerica de la orbita relativista.

Datos: c (NIST CODATA 2022, consultado 2026-11-09) y GM_sol (IAU 2015 B3, arXiv:1510.07674). Elementos
orbitales (a = 5.79e10 m, e = 0.2056): valores ILUSTRATIVOS (no consultados en esta clase).
Modelo: ecuacion de la orbita de Schwarzschild para u = 1/r: u'' + u = GM/h^2 + 3 GM u^2/c^2, con
h el momento angular especifico (h^2 = GM a (1 - e^2)). Un giro de perihelio a perihelio mide
2 pi + delta; la prediccion de primer orden es delta = 6 pi GM / (c^2 a (1 - e^2)).
Supuestos: particula de prueba, campo de Schwarzschild, sin otros planetas. Validez: GM/(c^2 r) << 1.
Tolerancia: 0.5 % entre el desplazamiento numerico y la prediccion.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
GM = 1.3271244e20
A, E = 5.79e10, 0.2056


def rhs(u, du, h2, cc):
    return du, GM / h2 + 3 * GM * u * u / cc ** 2 - u


def integra(h2, u0, cc=C, dphi=2e-4):
    """Integra desde un perihelio (du = 0) hasta el siguiente: devuelve el angulo recorrido."""
    u, du, phi = u0, 0.0, 0.0
    def paso(u, du):
        k1 = rhs(u, du, h2, cc)
        k2 = rhs(u + dphi / 2 * k1[0], du + dphi / 2 * k1[1], h2, cc)
        k3 = rhs(u + dphi / 2 * k2[0], du + dphi / 2 * k2[1], h2, cc)
        k4 = rhs(u + dphi * k3[0], du + dphi * k3[1], h2, cc)
        return (u + dphi * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6,
                du + dphi * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)
    # salir del perihelio inicial (du pasa a negativo), luego buscar du = 0 con du < 0 -> > 0 (afelio) y de nuevo
    estado = 0
    while True:
        un, dun = paso(u, du)
        phin = phi + dphi
        if estado == 0 and dun < 0:
            estado = 1
        elif estado == 1 and dun > 0:
            estado = 2                              # pasado el afelio
        elif estado == 2 and dun < 0 <= du:
            # perihelio: interpola el cero de du
            frac = du / (du - dun)
            return phi + frac * dphi
        u, du, phi = un, dun, phin


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h2 = GM * A * (1 - E * E)
    u0 = 1 / (A * (1 - E))
    pred = 6 * math.pi * GM / (C ** 2 * A * (1 - E * E))
    total = integra(h2, u0)
    delta = total - 2 * math.pi
    print(f"prediccion 6 pi GM / (c^2 a (1-e^2)) = {pred:.6e} rad por orbita ({math.degrees(pred) * 3600:.5f} arcsec)")
    print(f"integracion numerica: delta = {delta:.6e} rad por orbita ({math.degrees(delta) * 3600:.5f} arcsec)")
    assert abs(delta / pred - 1) < 5e-3, "precesion fuera del 0.5 %"
    periodo = 2 * math.pi * math.sqrt(A ** 3 / GM)
    n_siglo = 100 * 365.25 * 86400.0 / periodo
    print(f"periodo kepleriano = {periodo / 86400:.2f} d ; orbitas por siglo = {n_siglo:.1f} ; "
          f"precesion = {math.degrees(delta) * 3600 * n_siglo:.2f} arcsec por siglo")
    # sin el termino relativista no hay precesion
    d0 = integra(h2, u0, cc=1e30) - 2 * math.pi
    assert abs(d0) < 1e-8, "el caso newtoniano no debe precesar"
    print(f"caso newtoniano (c -> infinito): delta = {d0:.2e} rad")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
