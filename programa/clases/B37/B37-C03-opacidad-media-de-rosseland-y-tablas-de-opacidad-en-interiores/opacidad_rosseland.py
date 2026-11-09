#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C03: media de Rosseland, opacidad de Kramers y uso de una tabla de opacidad interpolada.

Datos: constantes h, k_B, sigma_SB y a_rad de NIST CODATA 2022, consultada el 2026-11-09. La opacidad monocromatica kappa_nu = kappa0 (nu/nu0)^-3 (forma de Kramers), la tabla
kappa(rho, T) y el estado (rho, T, flujo) son ILUSTRATIVOS (sinteticos); no son tablas de opacidad reales.
Modelo: 1/kappa_R = Int (1/kappa_nu)(dB_nu/dT) dnu / Int (dB_nu/dT) dnu. Con u = h nu/(k T): dB/dT ~ u^4 e^u/(e^u - 1)^2 y la integral de u^n e^u/(e^u - 1)^2 vale n! zeta(n).
Para kappa_nu ~ nu^-3 el cociente es analitico: 1/kappa_R = (1/kappa0)(k T/(h nu0))^3 7! zeta(7)/(4! zeta(4)). Se contrasta con la cuadratura numerica (Simpson).
Tabla: kappa = k0 rho T^-3,5/(1 + (T/2e7)^2) (Kramers de juguete con una curvatura anadida) en una malla log-log; interpolacion bilineal en log-log.
Supuestos: sin lineas, sin dispersion electronica; opacidad de juguete. Validez: orientativa.
Tolerancia: cuadratura frente a la forma analitica dentro de 1e-4; interpolacion de la tabla (malla gruesa de 0,5 dex en rho y 0,25 dex en T) dentro del 5 % del valor exacto.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
KB = 1.380649e-23
SB = 5.670374419e-8
C = 299792458.0
A_RAD = 4 * SB / C


def zeta(n):
    return sum(k**-n for k in range(1, 200000)) + 200000 ** (1 - n) / (n - 1)


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def w(u):
    return u**4 * math.exp(u) / (math.exp(u) - 1) ** 2 if u > 1e-9 else 0.0


def rosseland_numerico():
    # 1/kappa_R (en unidades de (kT/(h nu0))^3 / kappa0) = Int u^3 w(u) du / Int w(u) du
    num = simpson(lambda u: u**3 * w(u), 1e-6, 80.0)
    den = simpson(w, 1e-6, 80.0)
    return num / den


def kramers(rho, T, k0=4.0e24):
    return k0 * rho * T**-3.5 / (1.0 + (T / 2.0e7) ** 2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1. identidad de la integral: Int u^n e^u/(e^u-1)^2 du = n! zeta(n)
    for n in (4, 7):
        num = simpson(lambda u: u**n * math.exp(u) / (math.exp(u) - 1) ** 2, 1e-6, 80.0)
        ana = math.factorial(n) * zeta(n)
        print(f"n = {n}: integral numerica = {num:.6f} ; n! zeta(n) = {ana:.6f}")
        assert abs(num / ana - 1) < 1e-4
    # 2. media de Rosseland de kappa_nu ~ nu^-3
    num = rosseland_numerico()
    ana = math.factorial(7) * zeta(7) / (math.factorial(4) * zeta(4))
    print(f"coeficiente 1/kappa_R: cuadratura = {num:.5f} ; analitico 7! zeta(7)/(4! zeta(4)) = {ana:.5f}")
    assert abs(num / ana - 1) < 1e-4
    # 3. caso gris: la media vale kappa
    gris = 1.0 / (simpson(lambda u: w(u) / 3.0, 1e-6, 80.0) / simpson(w, 1e-6, 80.0))
    print(f"kappa gris = 3,0 -> media de Rosseland = {gris:.6f}")
    assert abs(gris - 3.0) < 1e-9
    # 4. valor para una temperatura dada (nu0 = 1e15 Hz, kappa0 = 1 m2/kg, ilustrativo)
    T, nu0, k0 = 1.0e7, 1.0e15, 1.0
    escala = (KB * T / (H * nu0)) ** 3
    kR = k0 / (escala * ana)
    print(f"T = 1e7 K: (kT/(h nu0))^3 = {escala:.3e} ; kappa_R = {kR:.3e} m2/kg")
    # 5. tabla log-log e interpolacion bilineal
    lr = [-1.0 + 0.5 * i for i in range(9)]   # log10 rho [kg/m3], -1 ... 3
    lt = [6.0 + 0.25 * j for j in range(9)]   # log10 T [K], 6 ... 8
    tabla = [[math.log10(kramers(10**a, 10**b)) for b in lt] for a in lr]

    def interp(rho, T):
        a, b = math.log10(rho), math.log10(T)
        i = min(int((a - lr[0]) / 0.5), len(lr) - 2)
        j = min(int((b - lt[0]) / 0.25), len(lt) - 2)
        x = (a - lr[i]) / 0.5
        y = (b - lt[j]) / 0.25
        v = (tabla[i][j] * (1 - x) * (1 - y) + tabla[i + 1][j] * x * (1 - y) + tabla[i][j + 1] * (1 - x) * y + tabla[i + 1][j + 1] * x * y)
        return 10**v

    rho, T = 150.0, 1.3e7
    ex, it = kramers(rho, T), interp(rho, T)
    print(f"tabla en (rho = 150, T = 1,3e7): exacto = {ex:.4e} ; interpolado = {it:.4e} ; error = {abs(it / ex - 1) * 100:.3f} %")
    assert 0 < abs(it / ex - 1) < 0.05
    # 6. gradiente radiativo con ese kappa (flujo L/(4 pi r^2) ilustrativo)
    F, HP, g_ = 4.0e9, 4.0e7, 300.0
    nab = 3 * it * rho * HP * F / (4 * A_RAD * C * T**4)
    print(f"nabla_rad = 3 kappa rho H_P F/(4 a c T^4) = {nab:.4f}")
    assert nab > 0
    # 7. sensibilidad: duplicar kappa duplica nabla_rad
    assert abs(3 * 2 * it * rho * HP * F / (4 * A_RAD * C * T**4) / nab - 2) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
