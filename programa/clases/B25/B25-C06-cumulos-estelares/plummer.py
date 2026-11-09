#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C06: cumulo de Plummer, ecuacion de Jeans y teorema del virial.

Datos: G = 6.67430e-11 m3 kg-1 s-2 (NIST, CODATA 2022, 2026-11-09); GM_sol (IAU 2015 B3);
1 pc = 3,0856776e16 m (conversion). El cumulo (M = 2e4 Msol, a = 1,5 pc, masa media 0,5 Msol) es
SINTETICO: no es un cumulo observado.
Modelo: esfera de Plummer, rho(r) = 3 M a^2 / (4 pi (r^2 + a^2)^(5/2)), M(<r) = M r^3/(r^2+a^2)^(3/2),
dispersion isotropa sigma^2(r) = G M / (6 sqrt(r^2 + a^2)); radio de media masa r_h = a/sqrt(2^(2/3)-1).
Supuestos: equilibrio, isotropia, masas iguales, sin gas, sin marea externa.
Validez: ilustrativa; los cumulos reales tienen espectro de masas, segregacion y marea.
Tolerancias: 1e-8 (masa), 1e-6 (Jeans por diferencias finitas), 1e-6 (virial por Simpson).
El tiempo de relajacion t_rh ~ 0,138 (N / ln(0,4 N)) t_din es una estimacion estandar de orden de
magnitud que NO se verifica contra fuente en esta clase.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
M_SOL = 1.3271244e20 / G
PC = 3.0856776e16
MYR = 3.15576e13


def m_dentro(r, M, a):
    return M * r ** 3 / (r * r + a * a) ** 1.5


def rho(r, M, a):
    return 3 * M * a * a / (4 * math.pi * (r * r + a * a) ** 2.5)


def sigma2(r, M, a):
    return G * M / (6 * math.sqrt(r * r + a * a))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def r_media_masa(M, a):
    lo, hi = 0.0, 100 * a
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if m_dentro(mid, M, a) < 0.5 * M:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    M, a = 2e4 * M_SOL, 1.5 * PC
    # Prueba 1: masa por cuadratura frente a la forma cerrada, hasta R = 50 a
    R = 50 * a
    num = simpson(lambda r: 4 * math.pi * r * r * rho(r, M, a), 0.0, R)
    assert abs(num / m_dentro(R, M, a) - 1) < 1e-8, "masa de Plummer"
    # Prueba 2: radio de media masa
    rh = r_media_masa(M, a)
    assert abs(rh / a - 1 / math.sqrt(2 ** (2 / 3) - 1)) < 1e-9
    # Prueba 3: ecuacion de Jeans d(rho sigma^2)/dr = -rho G M(<r)/r^2
    for r in (0.5 * a, a, 3 * a):
        h = 1e-4 * r
        lhs = (rho(r + h, M, a) * sigma2(r + h, M, a) - rho(r - h, M, a) * sigma2(r - h, M, a)) / (2 * h)
        rhs = -rho(r, M, a) * G * m_dentro(r, M, a) / r ** 2
        assert abs(lhs / rhs - 1) < 1e-6, "ecuacion de Jeans"
    # Prueba 4: virial 2K = -W, con 2K = 3 int rho sigma^2 dV y W = -3 pi G M^2/(32 a)
    dos_k = 3 * simpson(lambda r: 4 * math.pi * r * r * rho(r, M, a) * sigma2(r, M, a), 0.0, 400 * a, 200000)
    w = -3 * math.pi * G * M * M / (32 * a)
    assert abs(dos_k / (-w) - 1) < 1e-6, "virial"
    t_din = math.sqrt(rh ** 3 / (G * M))
    n_est = 2e4 / 0.5
    t_rh = 0.138 * n_est / math.log(0.4 * n_est) * t_din
    print(f"r_h = {rh / PC:.3f} pc ({rh / a:.4f} a) ; sigma(0) = {math.sqrt(sigma2(0.0, M, a)) / 1e3:.2f} km/s")
    print(f"masa por cuadratura / cerrada = {num / m_dentro(R, M, a):.10f}")
    print(f"2K/|W| = {dos_k / (-w):.8f}")
    print(f"t_din = {t_din / MYR:.2f} Myr ; N = {n_est:.0f} ; t_rh = {t_rh / MYR:.0f} Myr (orden de magnitud)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
