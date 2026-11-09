#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C01: criterios de Schwarzschild y Ledoux y convección de longitud de mezcla simplificada en una capa.

Datos: constantes G, c, k_B, sigma_SB (a_rad = 4 sigma/c), m_u de NIST CODATA 2022, consultada el 2026-11-09. Las condiciones de la capa (rho, T, kappa, c_p, g, H_P, L) y la
longitud de mezcla alpha = 1,8 son ILUSTRATIVAS (sinteticas); no son un modelo solar.
Modelo: flujo total F = F_rad(nabla) + F_conv(nabla). F_rad = 4 a c T^3 T nabla/(3 kappa rho H_P); F_conv = rho c_p T sqrt(g delta) l^2 /(4 sqrt2) H_P^(-3/2) (nabla - nabla_e)^(3/2).
La eficiencia de la burbuja (nabla_e - nabla_ad) = (nabla - nabla_ad)/(1 + B), con B = c_p rho^2 kappa l v/(6 a c T^3) y v^2 = g delta l^2 (nabla - nabla_e)/(8 H_P).
Forma simplificada de la teoria de longitud de mezcla, con coeficientes de orden unidad NO calibrados. Se resuelve nabla por biseccion.
Supuestos: gas ideal (delta = 1, nabla_ad = 0,4), capa local y estacionaria. Validez: orientativa.
Tolerancia: conservacion del flujo en la raiz dentro de 1e-9 relativo; nabla entre nabla_ad y nabla_rad.
"""
from __future__ import annotations
import math, platform, sys

G = 6.67430e-11
C = 299792458.0
SB = 5.670374419e-8
A_RAD = 4 * SB / C
NAD = 0.4


def flujos(nab, rho, T, kappa, cp, g, HP, alpha):
    l = alpha * HP
    f_rad = 4 * A_RAD * C * T**4 * nab / (3 * kappa * rho * HP)
    y = max(nab - NAD, 0.0)
    # v depende de y = nabla - nabla_e, y y de B (que depende de v): punto fijo por biseccion en y
    lo, hi = 0.0, y
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        v = math.sqrt(g * l * l * mid / (8 * HP))
        B = cp * rho**2 * kappa * l * v / (6 * A_RAD * C * T**3)
        y_nuevo = (nab - NAD) * B / (1 + B)
        if y_nuevo > mid:
            lo = mid
        else:
            hi = mid
    y = 0.5 * (lo + hi)
    v = math.sqrt(g * l * l * y / (8 * HP))
    f_conv = rho * cp * T * math.sqrt(g) * l * l / (4 * math.sqrt(2)) * HP**-1.5 * y**1.5
    return f_rad, f_conv, y, v


def resolver(rho, T, kappa, cp, g, HP, F, alpha):
    nab_rad = 3 * kappa * rho * HP * F / (4 * A_RAD * C * T**4)
    if nab_rad <= NAD:
        return nab_rad, nab_rad, 0.0, 0.0, 0.0
    lo, hi = NAD, nab_rad
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fr, fc, y, v = flujos(mid, rho, T, kappa, cp, g, HP, alpha)
        if fr + fc > F:
            hi = mid
        else:
            lo = mid
    nab = 0.5 * (lo + hi)
    fr, fc, y, v = flujos(nab, rho, T, kappa, cp, g, HP, alpha)
    return nab_rad, nab, fc / F, v, fr + fc - F


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mu = 0.6
    cp = 2.5 * 1.380649e-23 / (mu * 1.66053906892e-27)
    T, g, HP = 1.0e6, 500.0, 2.0e7
    F = 1.0e9
    print(f"cp = {cp:.4e} J/(kg K) ; nabla_ad = {NAD}")
    print(f"{'rho [kg/m3]':>12} {'kappa [m2/kg]':>14} {'nabla_rad':>10} {'nabla-nad':>11} {'F_conv/F':>9} {'v [m/s]':>10}")
    filas = []
    for rho, kappa in ((5.0, 1.0), (10.0, 1.0), (30.0, 3.0), (300.0, 3.0)):
        nr, n, fc, v, res = resolver(rho, T, kappa, cp, g, HP, F, 1.8)
        filas.append((rho, nr, n, fc))
        print(f"{rho:12.1e} {kappa:14.1f} {nr:10.4f} {max(n - NAD, 0.0):11.3e} {fc:9.4f} {v:10.2f}")
        assert abs(res) < 1e-9 * F
        assert n == nr if nr <= NAD else NAD - 1e-12 <= n <= nr + 1e-12
    # capa radiativa: nabla_rad < nabla_ad -> sin conveccion
    nr, n, fc, v, res = resolver(1e-2, T, 1.0, cp, g, HP, 1e5, 1.8)
    print(f"capa estable: nabla_rad = {nr:.4f} < nabla_ad ; F_conv/F = {fc:.1f}")
    assert nr < NAD and fc == 0.0
    # limite eficiente: nabla -> nabla_ad conforme crece la densidad
    assert filas[-1][2] - NAD < filas[1][2] - NAD
    assert filas[-1][2] - NAD < 1e-3
    # dependencia de alpha: mayor alpha -> conveccion mas eficiente -> nabla menor
    ns = [resolver(10.0, T, 1.0, cp, g, HP, F, a)[1] for a in (1.0, 1.8, 2.5)]
    print("nabla - nabla_ad para alpha = 1,0 ; 1,8 ; 2,5: " + " ; ".join(f"{x - NAD:.3e}" for x in ns))
    assert ns[0] > ns[1] > ns[2] > NAD
    # Ledoux: estable si nabla_rad < nabla_ad + (phi/delta) nabla_mu
    nabla_mu, phi = 0.15, 1.0
    for nr_ in (0.45, 0.6, 0.7):
        schw = nr_ > NAD
        led = nr_ > NAD + phi * nabla_mu
        print(f"nabla_rad = {nr_:.2f}: Schwarzschild {'inestable' if schw else 'estable'} ; Ledoux (nabla_mu = {nabla_mu}) {'inestable' if led else 'estable'}")
    assert (0.45 > NAD) and not (0.45 > NAD + nabla_mu) and (0.6 > NAD + nabla_mu)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
