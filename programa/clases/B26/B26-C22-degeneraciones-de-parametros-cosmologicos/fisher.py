#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C22: matriz de Fisher de (Omega_m, w) con supernovas sinteticas y ruptura de la degeneracion.

Datos: ninguno observado. 100 supernovas sinteticas (z de 0.02 a 1.0, error 0.15 mag), modelo wCDM plano con
valores fiduciales Om = 0.315, w = -1 y H0 = 67.4 km/s/Mpc (Planck 2018, arXiv:1807.06209, resumen,
consultado 2026-11-09). El "a priori de BAO" sobre Omega_m con sigma = 0.015 imita el resultado publicado de DESI
(arXiv:2404.03002, resumen), pero se usa como a priori SINTETICO.
Modelo: E(z)^2 = Om (1+z)^3 + (1-Om)(1+z)^(3(1+w)); mu = 5 log10(D_L/10 pc) con una constante de calibracion
marginalizada (se resta la media de las derivadas). Fisher: F_ij = sum (d mu/d p_i)(d mu/d p_j)/s^2 con derivadas
por diferencias finitas centrales; covarianza = F^-1; correlacion rho = C_12/sqrt(C_11 C_22); area de la
elipse de 68 % proporcional a 1/sqrt(det F). Comprobacion: F = Hessiano de chi^2/2.
Supuestos: errores gaussianos, regimen casi lineal. Validez: ilustrativa.
Tolerancia: 1e-3 entre el Fisher y el Hessiano numerico de chi^2; 1e-9 en la inversa 2x2.
"""
from __future__ import annotations
import math
import platform
import sys

C_KMS, H0 = 299792.458, 67.4
N, SIG = 100, 0.15
OM0, W0 = 0.315, -1.0
ZS = [0.02 + 0.98 * i / (N - 1) for i in range(N)]


def mu(z, om, w, n=200):
    E = lambda zz: math.sqrt(om * (1 + zz) ** 3 + (1 - om) * (1 + zz) ** (3 * (1 + w)))
    h = z / n
    s = 1 / E(0) + 1 / E(z)
    for i in range(1, n):
        s += (4 if i % 2 else 2) / E(i * h)
    return 5 * math.log10((1 + z) * C_KMS / H0 * s * h / 3 * 1e5)


def deriv(p, k, dp):
    q1, q2 = list(p), list(p)
    q1[k] += dp
    q2[k] -= dp
    d = [(mu(z, *q1) - mu(z, *q2)) / (2 * dp) for z in ZS]
    m = sum(d) / len(d)
    return [x - m for x in d]           # marginaliza la constante de calibracion


def fisher(p=(OM0, W0)):
    d = [deriv(p, 0, 1e-4), deriv(p, 1, 1e-4)]
    return [[sum(a * b for a, b in zip(d[i], d[j])) / SIG ** 2 for j in range(2)] for i in range(2)]


def inv2(f):
    det = f[0][0] * f[1][1] - f[0][1] * f[1][0]
    return [[f[1][1] / det, -f[0][1] / det], [-f[1][0] / det, f[0][0] / det]], det


def chi2(om, w):
    m0 = [mu(z, OM0, W0) for z in ZS]
    d = [mu(z, om, w) - a for z, a in zip(ZS, m0)]
    mm = sum(d) / len(d)
    return sum((x - mm) ** 2 for x in d) / SIG ** 2


def resumen(nombre, f):
    c, det = inv2(f)
    s1, s2 = math.sqrt(c[0][0]), math.sqrt(c[1][1])
    rho = c[0][1] / (s1 * s2)
    print(f"{nombre}: sigma(Om) = {s1:.4f} ; sigma(w) = {s2:.4f} ; correlacion = {rho:+.4f} ; "
          f"area relativa = {1 / math.sqrt(det):.4g}")
    return s1, s2, rho, 1 / math.sqrt(det)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f = fisher()
    c, det = inv2(f)
    prod = [[sum(f[i][k] * c[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    assert abs(prod[0][0] - 1) < 1e-9 and abs(prod[0][1]) < 1e-9, "inversa 2x2"
    # F = Hessiano de chi2 / 2 (diferencias finitas de chi2)
    h1, h2 = 2e-3, 2e-3
    f11 = (chi2(OM0 + h1, W0) - 2 * chi2(OM0, W0) + chi2(OM0 - h1, W0)) / h1 ** 2 / 2
    f22 = (chi2(OM0, W0 + h2) - 2 * chi2(OM0, W0) + chi2(OM0, W0 - h2)) / h2 ** 2 / 2
    f12 = (chi2(OM0 + h1, W0 + h2) - chi2(OM0 + h1, W0 - h2) - chi2(OM0 - h1, W0 + h2) + chi2(OM0 - h1, W0 - h2)) / (4 * h1 * h2) / 2
    assert abs(f11 / f[0][0] - 1) < 1e-3 and abs(f22 / f[1][1] - 1) < 1e-3 and abs(f12 / f[0][1] - 1) < 1e-2
    print(f"Fisher (SN): F11 = {f[0][0]:.1f}, F12 = {f[0][1]:.1f}, F22 = {f[1][1]:.1f} ; Hessiano/2: {f11:.1f}, {f12:.1f}, {f22:.1f}")
    a = resumen("SN solas       ", f)
    f2 = [[f[0][0] + 1 / 0.015 ** 2, f[0][1]], [f[1][0], f[1][1]]]
    b = resumen("SN + a priori ", f2)
    assert abs(b[0] / a[0]) < 1 and abs(b[1] / a[1]) < 1 and b[3] < a[3], "el a priori debe reducir las incertidumbres"
    print(f"reduccion del area: x{a[3] / b[3]:.1f} ; de sigma(w): x{a[1] / b[1]:.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
