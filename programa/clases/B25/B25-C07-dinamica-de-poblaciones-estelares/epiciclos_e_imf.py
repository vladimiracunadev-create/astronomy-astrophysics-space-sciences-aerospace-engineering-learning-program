#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C07: epiciclos en una curva plana y momentos de una funcion de masa inicial.

Datos: Theta0 = 238 km/s y R0 = 8,2 kpc (Bland-Hawthorn y Gerhard 2016, arXiv:1602.07702, texto
del PDF consultado 2026-11-09; OBSERVADOS). Definiciones de las constantes de Oort A y B del mismo
texto: A - B = Theta0/R0, A + B = -dTheta/dR. Funcion de masa: ley de potencias rota con ruptura en
0,5 Msol (Kroupa 2001, arXiv:astro-ph/0009005, resumen consultado 2026-11-09); las pendientes
1,3 y 2,3 y el limite 0,08-100 Msol son ILUSTRATIVOS (no consultados). Orbitas SINTETICAS.
Modelo: (a) potencial logaritmico plano Phi = Theta^2 ln R en el plano; integracion RK4;
(b) IMF dN/dm ~ m^-alpha por tramos, continua en la ruptura.
Supuestos: orbitas en el plano, sin brazos ni barra, sin dispersion de edades.
Validez: amplitudes pequenas frente al radio guia (epiciclo). Tolerancias: 1e-3 (periodo),
1e-2 (cociente de dispersiones), 1e-8 (cuadratura de la IMF).
Unidades: kpc, km/s; 1 kpc/(km/s) = 0,9778 Gyr (se calcula aqui).
"""
from __future__ import annotations
import math
import platform
import sys

THETA, R0 = 238.0, 8.2
KPC_KMS_GYR = 3.0856776e19 / 1e3 / 3.15576e16  # Gyr


def oort(theta, r, dtheta_dr=0.0):
    return 0.5 * (theta / r - dtheta_dr), -0.5 * (theta / r + dtheta_dr)


def kappa(theta, r):
    """Frecuencia epiciclica en curva plana: kappa^2 = -4 B (A - B)."""
    a, b = oort(theta, r)
    return math.sqrt(-4 * b * (a - b))


def deriv(s):
    x, y, vx, vy = s
    r2 = x * x + y * y
    f = -THETA ** 2 / r2
    return (vx, vy, f * x, f * y)


def rk4(s, h):
    k1 = deriv(s)
    k2 = deriv(tuple(si + 0.5 * h * ki for si, ki in zip(s, k1)))
    k3 = deriv(tuple(si + 0.5 * h * ki for si, ki in zip(s, k2)))
    k4 = deriv(tuple(si + h * ki for si, ki in zip(s, k3)))
    return tuple(si + h / 6 * (a + 2 * b + 2 * c + d) for si, a, b, c, d in zip(s, k1, k2, k3, k4))


def orbita(rg, delta, n_per=6, h=2e-4):
    """Parte del apocentro r = rg + delta con L = Theta rg; devuelve periodo radial y <vphi'^2>/<vR^2>."""
    s = (rg + delta, 0.0, 0.0, THETA * rg / (rg + delta))
    t, tiempos_min = 0.0, []
    prev_r = math.hypot(s[0], s[1])
    prev_vr = 0.0
    sum_vr2 = sum_vp2 = 0.0
    cnt = 0
    while len(tiempos_min) < n_per + 1:
        s2 = rk4(s, h)
        r2 = math.hypot(s2[0], s2[1])
        vr = (s2[0] * s2[2] + s2[1] * s2[3]) / r2
        vp = (s2[0] * s2[3] - s2[1] * s2[2]) / r2
        if prev_vr < 0 <= vr:
            tiempos_min.append(t + h * (-prev_vr) / (vr - prev_vr))
        sum_vr2 += vr * vr
        sum_vp2 += (vp - THETA) ** 2
        cnt += 1
        prev_vr = vr
        s, t = s2, t + h
    per = (tiempos_min[-1] - tiempos_min[0]) / n_per
    return per, sum_vp2 / sum_vr2


def imf_integral(f, alpha1=1.3, alpha2=2.3, m0=0.08, mb=0.5, m1=100.0, n=20000):
    """int f(m) xi(m) dm con xi continua en mb, en escala logaritmica (Simpson)."""
    c2 = 1.0
    c1 = c2 * mb ** (alpha1 - alpha2)

    def xi(m):
        return c1 * m ** -alpha1 if m < mb else c2 * m ** -alpha2

    def tramo(lo, hi):
        a, b = math.log(lo), math.log(hi)
        h = (b - a) / n
        g = lambda u: f(math.exp(u)) * xi(math.exp(u)) * math.exp(u)
        s = g(a) + g(b)
        for i in range(1, n):
            s += (4 if i % 2 else 2) * g(a + i * h)
        return s * h / 3

    return tramo(m0, mb) + tramo(mb, m1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    A, B = oort(THETA, R0)
    assert abs((A - B) - THETA / R0) < 1e-12 and abs(A + B) < 1e-12
    k = kappa(THETA, R0)
    assert abs(k / (math.sqrt(2) * THETA / R0) - 1) < 1e-12
    per, razon = orbita(R0, 0.05)
    t_kappa = 2 * math.pi / k
    assert abs(per / t_kappa - 1) < 1e-3, "periodo radial distinto del epiciclico"
    assert abs(razon / 0.5 - 1) < 1e-2, "cociente de dispersiones distinto de kappa^2/(4 Omega^2)"
    # IMF: cuadratura frente a forma cerrada del numero total en un tramo de ley de potencias
    alpha1, alpha2 = 1.3, 2.3
    c1 = 0.5 ** (alpha1 - alpha2)
    cerrado = c1 * (0.08 ** (1 - alpha1) - 0.5 ** (1 - alpha1)) / (alpha1 - 1) + (0.5 ** (1 - alpha2) - 100 ** (1 - alpha2)) / (alpha2 - 1)
    num = imf_integral(lambda m: 1.0)
    assert abs(num / cerrado - 1) < 1e-8
    masa = imf_integral(lambda m: m)
    n_masivas = imf_integral(lambda m: 1.0 if m >= 8 else 0.0)
    m_masivas = imf_integral(lambda m: m if m >= 8 else 0.0)
    print(f"A = {A:.2f}, B = {B:.2f} km/s/kpc ; A - B = {A - B:.2f} ; kappa = {k:.1f} km/s/kpc")
    print(f"T_epiciclo (2 pi/kappa) = {t_kappa * KPC_KMS_GYR * 1e3:.1f} Myr ; periodo orbital 2 pi/Omega = {2 * math.pi / (THETA / R0) * KPC_KMS_GYR * 1e3:.1f} Myr")
    print(f"periodo radial numerico = {per * KPC_KMS_GYR * 1e3:.2f} Myr (cociente con 2 pi/kappa = {per / t_kappa:.5f})")
    print(f"<vphi'^2>/<vR^2> = {razon:.4f} (teoria 0.5)")
    print(f"IMF: masa media = {masa / num:.3f} Msol ; fraccion en numero de estrellas >= 8 Msol = {n_masivas / num:.5f}")
    print(f"fraccion de la masa en estrellas >= 8 Msol = {m_masivas / masa:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
