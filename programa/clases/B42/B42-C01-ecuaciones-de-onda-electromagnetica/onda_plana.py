#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C01: onda plana electromagnetica, relacion de dispersion y flujo de Poynting.

Datos: constantes CONSULTADAS en NIST CODATA 2022 (tabla allascii.txt, consultada el 2026-11-09): c = 299 792 458 m/s (exacta),
epsilon_0 = 8,854 187 8188e-12 F/m, mu_0 = 1,256 637 061 27e-6 N/A^2. La longitud de onda 550 nm y la amplitud E0 = 1 V/m son ILUSTRATIVAS.
Modelo: E_x(z,t) = E0 cos(k z - w t), B_y = E_x / c; se verifica la ecuacion de onda por diferencias finitas, c = 1/sqrt(eps0 mu0)
y la media temporal del vector de Poynting S = E x B / mu0 contra el resultado analitico eps0 c E0^2 / 2.
Supuestos: vacio, onda plana monocromatica, polarizacion lineal. Validez: ondas libres; no describe medios ni fuentes.
Tolerancia: c por eps0 y mu0 a 1e-9 relativo; ecuacion de onda a 1e-4 relativo (error de segundo orden); <S> a 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

C = 299_792_458.0
EPS0 = 8.8541878188e-12
MU0 = 1.25663706127e-6
LAM = 550e-9
E0 = 1.0

def campo(z, t, k, w):
    return E0 * math.cos(k * z - w * t)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c_derivada = 1.0 / math.sqrt(EPS0 * MU0)
    print(f"c de NIST = {C:.0f} m/s ; 1/sqrt(eps0 mu0) = {c_derivada:.3f} m/s ; error relativo = {abs(c_derivada - C) / C:.2e}")
    assert abs(c_derivada - C) / C < 1e-9
    k = 2 * math.pi / LAM
    w = C * k
    f = w / (2 * math.pi)
    print(f"lambda = {LAM * 1e9:.0f} nm ; k = {k:.6e} rad/m ; f = {f:.6e} Hz ; T = {1 / f:.4e} s")
    # ecuacion de onda por diferencias finitas centradas
    h_z = LAM / 200.0
    h_t = h_z / C
    peor = 0.0
    for iz in range(0, 40):
        z = iz * LAM / 40.0
        t = 0.3 * LAM / C
        d2z = (campo(z + h_z, t, k, w) - 2 * campo(z, t, k, w) + campo(z - h_z, t, k, w)) / h_z ** 2
        d2t = (campo(z, t + h_t, k, w) - 2 * campo(z, t, k, w) + campo(z, t - h_t, k, w)) / h_t ** 2
        escala = k * k * E0
        peor = max(peor, abs(d2z - d2t / C ** 2) / escala)
    print(f"ecuacion de onda: max |d2E/dz2 - (1/c^2) d2E/dt2| / (k^2 E0) = {peor:.2e}")
    assert peor < 1e-4
    # Poynting medio en el tiempo
    n = 20000
    z0 = 0.37 * LAM
    s_sum = 0.0
    T = 2 * math.pi / w
    for i in range(n):
        t = (i + 0.5) * T / n
        e = campo(z0, t, k, w)
        b = e / C
        s_sum += e * b / MU0
    s_med = s_sum / n
    s_teo = 0.5 * EPS0 * C * E0 ** 2
    print(f"<S> numerico = {s_med:.6e} W/m2 ; eps0 c E0^2 / 2 = {s_teo:.6e} W/m2 ; error relativo = {abs(s_med - s_teo) / s_teo:.2e}")
    assert abs(s_med - s_teo) / s_teo < 1e-6
    z_vac = math.sqrt(MU0 / EPS0)
    print(f"impedancia del vacio sqrt(mu0/eps0) = {z_vac:.6f} ohm (NIST: 376.730 313 412)")
    assert abs(z_vac - 376.730313412) < 1e-5
    # relacion energia: densidad electrica media = magnetica media
    u_e = sum(0.5 * EPS0 * campo(z0, (i + 0.5) * T / n, k, w) ** 2 for i in range(n)) / n
    u_b = sum(0.5 * (campo(z0, (i + 0.5) * T / n, k, w) / C) ** 2 / MU0 for i in range(n)) / n
    print(f"<u_E> = {u_e:.6e} J/m3 ; <u_B> = {u_b:.6e} J/m3 ; cociente = {u_e / u_b:.8f}")
    assert abs(u_e / u_b - 1) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
