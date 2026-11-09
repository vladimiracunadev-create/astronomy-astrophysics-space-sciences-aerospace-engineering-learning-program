#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C11: rotacion interna de dos zonas a partir del desdoblamiento rotacional de modos dipolares.

Datos: ninguna constante fisica externa. Todo es SINTETICO (ilustrativo): las rotaciones de nucleo y envoltura (Omega_c/2pi = 0,60 uHz; Omega_e/2pi = 0,06 uHz), la fraccion de
inercia en el nucleo zeta de cada modo (de 0,1 a 0,9) y el ruido (0,01 uHz) con semilla 20261109. La relacion de desdoblamiento de dos zonas es la forma estandar de promedio ponderado por
la energia de cada zona, adoptada aqui como modelo de juguete sin haberse consultado una fuente para esta clase.
Modelo: delta nu_m = m [zeta Omega_c + (1 - zeta) Omega_e]/(2 pi) con m = -1, 0, +1 (dipolo); ajuste por minimos cuadrados ponderados de Omega_c y Omega_e a partir de delta nu/m de 12 modos;
covarianza analitica (A^T W A)^-1 contrastada con Monte Carlo (2000 realizaciones). Caso de cuerpo rigido (Omega_c = Omega_e) y conversion a periodo de rotacion P = 1/(delta nu).
Para modos de presion en una estrella de rotacion solida, el coeficiente de Ledoux C_nl ~ 0 y para modos g de dipolo C = 1/(l(l+1)) = 1/2 (identidad algebraica, verificada).
Supuestos: rotacion lenta (primer orden), dos zonas, sin campo magnetico. Validez: orientativa.
Tolerancia: parametros recuperados dentro de 3 sigma; covarianza analitica frente a Monte Carlo dentro de 10 % en las desviaciones; cuerpo rigido recupera Omega_c = Omega_e.
"""
from __future__ import annotations
import math, platform, random, sys


def ajustar(zetas, y, sg):
    # y_i = zeta_i a + (1 - zeta_i) b ; matriz normal 2x2 ponderada
    w = 1.0 / sg**2
    saa = sum(w * z * z for z in zetas)
    sab = sum(w * z * (1 - z) for z in zetas)
    sbb = sum(w * (1 - z) ** 2 for z in zetas)
    ta = sum(w * z * v for z, v in zip(zetas, y))
    tb = sum(w * (1 - z) * v for z, v in zip(zetas, y))
    det = saa * sbb - sab * sab
    a = (sbb * ta - sab * tb) / det
    b = (saa * tb - sab * ta) / det
    cov = [[sbb / det, -sab / det], [-sab / det, saa / det]]
    return a, b, cov


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a0, b0, sg = 0.60, 0.06, 0.01
    zetas = [0.1 + 0.8 * k / 11 for k in range(12)]
    rng = random.Random(20261109)
    y_sin = [z * a0 + (1 - z) * b0 for z in zetas]
    y = [v + rng.gauss(0, sg) for v in y_sin]
    a, b, cov = ajustar(zetas, y, sg)
    sa, sb = math.sqrt(cov[0][0]), math.sqrt(cov[1][1])
    rho = cov[0][1] / (sa * sb)
    print(f"{'zeta':>6} {'delta nu/m [uHz]':>17}")
    for z, v in list(zip(zetas, y))[::3]:
        print(f"{z:6.3f} {v:17.4f}")
    print(f"ajuste: Omega_c/2pi = {a:.4f} +/- {sa:.4f} uHz (verdadero {a0}) ; Omega_e/2pi = {b:.4f} +/- {sb:.4f} uHz (verdadero {b0}) ; correlacion = {rho:.3f}")
    assert abs(a - a0) < 3 * sa and abs(b - b0) < 3 * sb
    print(f"cociente de rotacion nucleo/envoltura = {a / b:.2f} (verdadero {a0 / b0:.2f})")
    # Monte Carlo
    As, Bs = [], []
    for _ in range(2000):
        yy = [v + rng.gauss(0, sg) for v in y_sin]
        r = ajustar(zetas, yy, sg)
        As.append(r[0])
        Bs.append(r[1])
    ma, mb = sum(As) / 2000, sum(Bs) / 2000
    sda = math.sqrt(sum((x - ma) ** 2 for x in As) / 1999)
    sdb = math.sqrt(sum((x - mb) ** 2 for x in Bs) / 1999)
    print(f"Monte Carlo (2000): sigma(Omega_c) = {sda:.4f} ; sigma(Omega_e) = {sdb:.4f} uHz")
    assert abs(sda / sa - 1) < 0.10 and abs(sdb / sb - 1) < 0.10
    # cuerpo rigido
    yr = [0.25 for _ in zetas]
    ar, br, _ = ajustar(zetas, yr, sg)
    print(f"cuerpo rigido (0,25 uHz en todos los modos): Omega_c = {ar:.6f} ; Omega_e = {br:.6f}")
    assert abs(ar - 0.25) < 1e-9 and abs(br - 0.25) < 1e-9
    # periodo de rotacion
    P_c = 1.0 / (a * 1e-6) / 86400.0
    P_e = 1.0 / (b * 1e-6) / 86400.0
    print(f"periodo de rotacion: nucleo = {P_c:.2f} d ; envoltura = {P_e:.1f} d")
    # coeficiente de Ledoux de dipolo en el limite g
    print(f"C = 1/(l(l+1)) para l = 1: {1 / (1 * 2):.3f} ; para l = 2: {1 / (2 * 3):.4f}")
    assert abs(1 / (1 * 2) - 0.5) < 1e-15
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
