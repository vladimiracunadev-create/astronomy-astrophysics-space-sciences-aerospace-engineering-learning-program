#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B93-C01: pista de una placa por corriente, caida de tension, y microtira (impedancia y retardo).

Datos consultados (2026-11-10): notas de curso UCSB ECE 145A (Long, 2007): para microtira con W = h sobre epoxi-vidrio,
er = 4.8, er_eff = 3.4, v = 0.54 c, Z0 = 68 ohm (se usa SOLO para contrastar el calculo).
NO CONSULTADOS (relaciones estandar o de resultados de busqueda, la norma no se leyo): formula empirica de corriente de la
IPC-2221, I = k dT^0.44 A^0.725 (A en mil^2, dT en K, k = 0.048 externa y 0.024 interna); resistividad del cobre
1.68e-8 ohm m a 20 C y coeficiente 0.00393 /K; aproximacion de Hammerstad para la microtira.
SINTETICOS / ILUSTRATIVOS: corrientes, longitudes, cobre de 35 um (1 oz = 1.378 mil), h = 0.2 mm, er = 4.8.
Tolerancias: Z0 frente al valor publicado dentro de 1 ohm; er_eff dentro de 0.05; inversion ancho<->corriente con 1e-9 relativa.
"""
from __future__ import annotations
import math, platform

C = 299792458.0  # m/s, definicion SI
MIL = 25.4e-6  # m
T_CU = 35e-6  # m (1 oz, ILUSTRATIVO)
RHO20, ALFA = 1.68e-8, 0.00393


def area_mil2(i, dt, k):
    return (i / (k * dt ** 0.44)) ** (1.0 / 0.725)


def ancho_mm(i, dt, k, t=T_CU):
    return area_mil2(i, dt, k) * MIL ** 2 / t * 1e3


def corriente(w_mm, dt, k, t=T_CU):
    a = (w_mm * 1e-3 * t) / MIL ** 2
    return k * dt ** 0.44 * a ** 0.725


def resistencia(l_m, w_mm, t_c, t=T_CU):
    rho = RHO20 * (1 + ALFA * (t_c - 20.0))
    return rho * l_m / (w_mm * 1e-3 * t)


def eps_eff(er, w_h):
    return (er + 1) / 2 + (er - 1) / 2 * (1 + 12.0 / w_h) ** -0.5


def z0(er, w_h):
    ee = eps_eff(er, w_h)
    if w_h <= 1:
        return 60 / math.sqrt(ee) * math.log(8 / w_h + w_h / 4)
    return 120 * math.pi / (math.sqrt(ee) * (w_h + 1.393 + 0.667 * math.log(w_h + 1.444)))


def w_h_para(er, objetivo):
    lo, hi = 0.05, 10.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if z0(er, m) > objetivo:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Cobre ILUSTRATIVO de 35 um; dT = 10 K sobre el ambiente")
    print(" I [A]   ancho externa [mm]   ancho interna [mm]")
    for i in (0.5, 1.0, 2.0, 3.0):
        print(f"{i:5.1f}   {ancho_mm(i, 10, 0.048):12.3f}   {ancho_mm(i, 10, 0.024):14.3f}")
    w = ancho_mm(2.0, 10, 0.048)
    assert abs(corriente(w, 10, 0.048) / 2.0 - 1) < 1e-9
    r20, r85 = resistencia(0.100, w, 20), resistencia(0.100, w, 85)
    print(f"Pista de 100 mm y {w:.3f} mm: R(20 C) = {r20*1e3:.2f} mohm, R(85 C) = {r85*1e3:.2f} mohm; caida a 2 A (85 C) = {2*r85*1e3:.1f} mV")
    ee, zz = eps_eff(4.8, 1.0), z0(4.8, 1.0)
    print(f"Microtira W = h, er = 4.8: er_eff = {ee:.3f} (publicado 3.4), Z0 = {zz:.1f} ohm (publicado 68), v = {1/math.sqrt(ee):.3f} c (publicado 0.54 c)")
    assert abs(ee - 3.4) < 0.05 and abs(zz - 68.0) < 1.0
    wh = w_h_para(4.8, 50.0)
    h = 0.2
    print(f"Para Z0 = 50 ohm: W/h = {wh:.3f}; con h = {h} mm, W = {wh*h:.3f} mm; er_eff = {eps_eff(4.8, wh):.3f}")
    ee50 = eps_eff(4.8, wh)
    ret = math.sqrt(ee50) / C * 1e12 * 1e-3
    print(f"Retardo = {ret:.2f} ps/mm; una pista de 100 mm tarda {ret*100/1000:.3f} ns")
    assert abs(z0(4.8, wh) - 50.0) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
