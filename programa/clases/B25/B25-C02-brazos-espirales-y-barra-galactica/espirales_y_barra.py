#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C02: espiral logaritmica, problema del enrollamiento y geometria de la barra.

Datos: R0 = 8.2 kpc, Theta0 = 238 km/s, angulo de la barra 27 grados y semilongitud de la barra
larga 5,0 kpc (Bland-Hawthorn y Gerhard 2016, arXiv:1602.07702, texto del PDF consultado
2026-11-09); angulo de paso medio de los brazos mayores ~10 grados (Reid et al. 2019,
arXiv:1910.03357, texto del PDF consultado 2026-11-09). Son valores OBSERVADOS/ESTIMADOS.
1 km/s = 1.0227 pc/Myr se CALCULA aqui con 1 pc = 648000/pi ua (conversion de unidades).
Modelo: (a) espiral logaritmica ln(R/Rk) = -(beta - beta_k) tan(psi); (b) brazo material que
gira con curva plana, con angulo de paso tan(psi) = R/(Theta t); (c) barra como segmento recto
de semilongitud a con angulo phi respecto de la linea Sol-centro.
Supuestos: plano galactico, curva de rotacion plana, brazo material inicialmente radial.
Validez: ilustrativa; los brazos reales se ajustan por tramos. Tolerancias: 1e-6 (derivada
numerica frente a la forma cerrada) y 1e-9 (identidades).
"""
from __future__ import annotations
import math
import platform
import sys

AU = 149_597_870_700.0
PC = 648000.0 / math.pi * AU
KMS_A_PC_MYR = 1e3 * 3.15576e13 / PC  # 1 km/s en pc/Myr
R0, THETA0, A_BARRA, PHI_BARRA = 8.2, 238.0, 5.0, 27.0


def radio_espiral(beta, rk, psi_deg):
    return rk * math.exp(-beta * math.tan(math.radians(psi_deg)))


def psi_numerico(rk, psi_deg, beta=0.7, h=1e-5):
    """Angulo entre la tangente y la circunferencia: tan(psi) = |dR/dbeta| / R."""
    dr = (radio_espiral(beta + h, rk, psi_deg) - radio_espiral(beta - h, rk, psi_deg)) / (2 * h)
    return math.degrees(math.atan(abs(dr) / radio_espiral(beta, rk, psi_deg)))


def razon_por_vuelta(psi_deg):
    return math.exp(2 * math.pi * math.tan(math.radians(psi_deg)))


def psi_enrollado(r_kpc, t_gyr, theta=THETA0):
    """Angulo de paso (grados) de un brazo material tras t, con curva plana."""
    recorrido_kpc = theta * KMS_A_PC_MYR * t_gyr * 1e3 / 1e3  # km/s -> kpc/Gyr = pc/Myr
    return math.degrees(math.atan(r_kpc / recorrido_kpc))


def psi_enrollado_numerico(r, t, theta=THETA0, h=1e-4):
    """Derivando el angulo acumulado phi(R) = theta t / R: tan(psi) = 1/|R dphi/dR|."""
    phi = lambda x: theta * KMS_A_PC_MYR * t * 1e3 / 1e3 / x
    dphi = (phi(r + h) - phi(r - h)) / (2 * h)
    return math.degrees(math.atan(1.0 / abs(r * dphi)))


def longitud_extremo(a, phi_deg, r0=R0):
    """Longitud galactica (grados) del extremo cercano de una barra de semilongitud a."""
    p = math.radians(phi_deg)
    return math.degrees(math.atan2(a * math.sin(p), r0 - a * math.cos(p)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for psi in (5.0, 10.0, 20.0):
        assert abs(psi_numerico(5.0, psi) - psi) < 1e-6, "angulo de paso numerico distinto"
    assert abs(razon_por_vuelta(0.0) - 1.0) < 1e-12
    for t in (0.2, 1.0, 5.0):
        assert abs(psi_enrollado(R0, t) - psi_enrollado_numerico(R0, t)) < 1e-6
    # extremos de la barra: a = 0 -> 0 grados; phi = 90 -> atan(a/R0)
    assert abs(longitud_extremo(0.0, 27.0)) < 1e-12
    assert abs(longitud_extremo(5.0, 90.0) - math.degrees(math.atan(5.0 / R0))) < 1e-9
    print(f"1 km/s = {KMS_A_PC_MYR:.4f} pc/Myr")
    for psi in (5.0, 10.0, 20.0):
        print(f"psi = {psi:4.1f} grados -> R crece x{razon_por_vuelta(psi):.3f} por vuelta")
    for t in (0.2, 1.0, 5.0):
        print(f"brazo material en R0 tras {t:3.1f} Gyr: psi = {psi_enrollado(R0, t):.2f} grados")
    print(f"extremo cercano de la barra: l = {longitud_extremo(A_BARRA, PHI_BARRA):.1f} grados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
