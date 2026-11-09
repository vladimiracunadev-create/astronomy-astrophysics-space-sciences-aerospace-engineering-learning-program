#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C22: lobulo de Roche por integracion numerica y evolucion del semieje con transferencia de masa.

Datos: GM_sol, R_sol nominales (IAU 2015 B3). Las masas y el semieje de la binaria son valores
SINTETICOS (ilustrativos).
Modelo: potencial de Roche en el sistema que rota con la binaria (unidades: semieje a = 1,
G (M1+M2) = 1, velocidad angular 1): Phi = -m1/r1 - m2/r2 - (1/2)[(x - m2)^2 + y^2], con
m1 = q/(1+q), m2 = 1/(1+q), q = M1/M2; el donante M1 esta en el origen y M2 en x = 1. El
lobulo es la superficie equipotencial que pasa por el punto de Lagrange L1; su radio efectivo
es el de la esfera de igual volumen, obtenido por integracion numerica en angulo solido
(simetria de reflexion respecto de los planos x-y y x-z). Se compara con la aproximacion de Eggleton, R_L/a = 0.49 q^(2/3) /
(0.6 q^(2/3) + ln(1 + q^(1/3))) (aproximacion de la literatura, no consultada aqui: sirve como
referencia independiente del calculo numerico y no como fuente de cifras).
Transferencia conservativa de masa y momento angular: a_f / a_i = (M1i M2i / (M1f M2f))^2.
Supuestos: orbita circular, estrellas esfericas puntuales para el potencial, rotacion sincrona.
Validez: ilustrativa. Tolerancia: 1 % entre numerico y Eggleton; 1e-9 en L1 de q = 1 y en la
conservacion del momento angular.
"""
from __future__ import annotations
import math
import platform
import sys

GM_SOL, R_SOL = 1.3271244e20, 6.957e8


def potencial(x, y, z, m1, m2):
    r1 = math.sqrt(x * x + y * y + z * z)
    r2 = math.sqrt((x - 1.0) ** 2 + y * y + z * z)
    return -m1 / r1 - m2 / r2 - 0.5 * ((x - m2) ** 2 + y * y)     # el eje de rotacion es z


def l1(q):
    m1, m2 = q / (1 + q), 1 / (1 + q)
    f = lambda x: m1 / x ** 2 - m2 / (1 - x) ** 2 - (x - m2)    # dPhi/dx = 0 sobre el eje
    lo, hi = 1e-6, 1 - 1e-6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def radio_roche(q, n_u=120, n_ph=40):
    """Radio de la esfera de igual volumen: V = (1/3) Int r^3 dOmega (simetria de reflexion en y y z)."""
    m1, m2 = q / (1 + q), 1 / (1 + q)
    phi_l1 = potencial(l1(q), 0.0, 0.0, m1, m2)
    suma = 0.0
    for i in range(n_u):
        u = -1 + (i + 0.5) * 2 / n_u                       # cos(theta), theta desde el eje x
        sn = math.sqrt(1 - u * u)
        for j in range(n_ph):
            ph = (j + 0.5) * (math.pi / 2) / n_ph           # cuarto de azimut
            dx, dy, dz = u, sn * math.cos(ph), sn * math.sin(ph)
            paso, r = 0.01, 0.01
            while r < 1.5 and potencial(r * dx, r * dy, r * dz, m1, m2) < phi_l1:
                r += paso
            lo, hi = r - paso, r
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                if potencial(mid * dx, mid * dy, mid * dz, m1, m2) >= phi_l1:
                    hi = mid
                else:
                    lo = mid
            suma += (0.5 * (lo + hi)) ** 3
    omega_total = 4 * math.pi
    vol = (1 / 3) * suma * omega_total / (n_u * n_ph)
    return (3 * vol / (4 * math.pi)) ** (1 / 3)


def eggleton(q):
    q13 = q ** (1 / 3)
    return 0.49 * q13 ** 2 / (0.6 * q13 ** 2 + math.log(1 + q13))


def semieje_final(a_i, m1i, m2i, m1f, m2f):
    return a_i * (m1i * m2i / (m1f * m2f)) ** 2


def momento_angular(a, m1, m2):
    return m1 * m2 * math.sqrt(a / (m1 + m2))     # G = 1


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert abs(l1(1.0) - 0.5) < 1e-9, "L1(q=1) != 0.5"
    print(f"{'q=M1/M2':>8} {'L1/a':>7} {'R_L/a (numerico)':>17} {'Eggleton':>9} {'dif %':>7}")
    for q in (0.1, 0.5, 1.0, 2.0, 10.0):
        rn, re = radio_roche(q), eggleton(q)
        assert abs(rn / re - 1) < 0.01, f"q={q}: numerico y Eggleton difieren > 1 %"
        print(f"{q:8.2f} {l1(q):7.4f} {rn:17.4f} {re:9.4f} {100 * (rn / re - 1):7.2f}")
    # transferencia conservativa: donante 1.5, acretor 1.0, semieje 10 R_sol
    a_i, m1i, m2i = 10.0, 1.5, 1.0
    print("transferencia conservativa (donante 1.5, acretor 1.0, a_i = 10 R_sol):")
    for dm in (0.0, 0.25, 0.5, 0.9, 1.2):
        m1f, m2f = m1i - dm, m2i + dm
        a_f = semieje_final(a_i, m1i, m2i, m1f, m2f)
        j_i, j_f = momento_angular(a_i, m1i, m2i), momento_angular(a_f, m1f, m2f)
        assert abs(j_f / j_i - 1) < 1e-9, "J no se conserva"
        rl = eggleton(m1f / m2f) * a_f if m1f > 0 else 0.0
        print(f"  dM = {dm:4.2f}: M1 = {m1f:4.2f}, M2 = {m2f:4.2f}, a = {a_f:6.2f} R_sol, R_L(donante) = {rl:5.2f} R_sol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
