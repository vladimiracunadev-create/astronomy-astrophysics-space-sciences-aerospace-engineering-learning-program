#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C07: curvatura de una esfera y distancia propia en la metrica de Schwarzschild.

Datos: c exacta y G (NIST CODATA 2022, consultados 2026-11-09); GM_sol, R_sol, GM_E, R_E nominales
(IAU 2015 B3, arXiv:1510.07674, texto del PDF extraido el 2026-11-09). Los radios de la integral son
ILUSTRATIVOS (de R_sol a 2 R_sol).
Modelo: (1) esfera de radio R: elemento de area R^2 sin(theta) dtheta dphi; el triangulo con tres angulos
rectos (octante) tiene exceso angular = K A con K = 1/R^2. (2) Schwarzschild: radio r_s = 2GM/c^2; distancia
propia radial entre r1 y r2: s = Int dr / sqrt(1 - r_s/r), solucion cerrada
s(r) = sqrt(r (r - r_s)) + r_s ln(sqrt(r) + sqrt(r - r_s)).
Supuestos: metrica de vacio estatica y esferica; r > r_s. Validez: fuera del objeto (la formula ignora el interior).
Tolerancia: 1e-6 (relativa) en el exceso angular; 1e-9 entre cuadratura y forma cerrada.
"""
from __future__ import annotations
import math
import platform
import sys

C, G = 299792458.0, 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
GM_E, R_E = 3.986004e14, 6.3781e6


def r_s(gm):
    return 2 * gm / C ** 2


def area_octante(R=1.0, n=1000):
    """Int_0^{pi/2} Int_0^{pi/2} R^2 sin(theta) dtheta dphi por punto medio."""
    d = (math.pi / 2) / n
    s = sum(math.sin((i + 0.5) * d) * d for i in range(n))
    return R * R * s * (math.pi / 2)


def s_cerrada(r, rs):
    return math.sqrt(r * (r - rs)) + rs * math.log(math.sqrt(r) + math.sqrt(r - rs))


def s_numerica(r1, r2, rs, n=20000):
    h = (r2 - r1) / n
    f = lambda r: 1 / math.sqrt(1 - rs / r)
    s = f(r1) + f(r2)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(r1 + i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    A = area_octante()
    exceso = A / 1.0 ** 2
    assert abs(exceso / (math.pi / 2) - 1) < 1e-6, "exceso angular del octante"
    print(f"octante de esfera unidad: area = {A:.6f} (pi/2 = {math.pi / 2:.6f}) ; exceso = {math.degrees(exceso):.4f} grados")
    rs_sol, rs_e = r_s(GM_SOL), r_s(GM_E)
    print(f"r_s(Sol) = {rs_sol:.2f} m ; r_s(Tierra) = {rs_e * 1e3:.3f} mm")
    print(f"compacidad r_s/R: Sol = {rs_sol / R_SOL:.3e} ; Tierra = {rs_e / R_E:.3e}")
    r1, r2 = R_SOL, 2 * R_SOL
    num = s_numerica(r1, r2, rs_sol)
    cer = s_cerrada(r2, rs_sol) - s_cerrada(r1, rs_sol)
    assert abs(num / cer - 1) < 1e-9, "cuadratura != forma cerrada"
    print(f"distancia propia R_sol -> 2 R_sol = {cer:.6e} m ; diferencia coordenada = {cer - (r2 - r1):.3f} m")
    print(f"aproximacion (r_s/2) ln(r2/r1) = {rs_sol / 2 * math.log(2):.3f} m")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
