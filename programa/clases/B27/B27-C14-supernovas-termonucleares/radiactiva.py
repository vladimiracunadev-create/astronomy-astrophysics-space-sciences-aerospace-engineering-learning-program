#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C14: cadena radiactiva 56Ni -> 56Co -> 56Fe y curva de luz tardia de una supernova termonuclear.

Datos: semividas 56Ni = 6.075 d y 56Co = 77.236 d (tabla de isotopos de Wikipedia, consultada 2026-11-09; no se consulto
la base de datos nuclear original), GM_sol (IAU 2015 B3), G, MeV por julio (NIST CODATA 2022), masa atomica 56 u
(constante de masa atomica NIST). La masa inicial de 56Ni (0.6 Msol) y las energias medias por desintegracion
(1.7 y 3.6 MeV) son ILUSTRATIVAS (sinteticas); no se cita ninguna medicion de una supernova.
Modelo: cadena de Bateman N1' = -l1 N1, N2' = l1 N1 - l2 N2, con solucion
N2 = N0 l1/(l2 - l1) (exp(-l1 t) - exp(-l2 t)); luminosidad L = E1 l1 N1 + E2 l2 N2 (toda la energia se deposita).
Supuestos: deposicion completa (falla en la fase tardia real), sin opacidad, sin otras cadenas. Validez: ilustrativa.
Tolerancia: 1e-8 entre RK4 y Bateman; 1e-4 entre la pendiente tardia y -1/tau_Co.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
U = 1.66053906892e-27
MEV = 1.602176634e-13
T1, T2 = 6.075 * 86400.0, 77.236 * 86400.0
L1, L2 = math.log(2) / T1, math.log(2) / T2
E1, E2 = 1.7 * MEV, 3.6 * MEV


def bateman(t, n0):
    n1 = n0 * math.exp(-L1 * t)
    n2 = max(0.0, n0 * L1 / (L2 - L1) * (math.exp(-L1 * t) - math.exp(-L2 * t)))
    return n1, n2


def rk4(t_fin, n0, n=20000):
    y = [n0, 0.0]
    h = t_fin / n
    f = lambda a: [-L1 * a[0], L1 * a[0] - L2 * a[1]]
    for _ in range(n):
        k1 = f(y)
        k2 = f([y[i] + 0.5 * h * k1[i] for i in range(2)])
        k3 = f([y[i] + 0.5 * h * k2[i] for i in range(2)])
        k4 = f([y[i] + h * k3[i] for i in range(2)])
        y = [y[i] + h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(2)]
    return y


def lum(t, n0):
    n1, n2 = bateman(t, n0)
    return E1 * L1 * n1 + E2 * L2 * n2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n0 = 0.6 * M_SOL / (56 * U)
    print(f"tau(Ni) = {1 / L1 / 86400:.3f} d ; tau(Co) = {1 / L2 / 86400:.3f} d ; N0 = {n0:.4e} nucleos (0.6 Msol de 56Ni)")
    print(f"{'t [d]':>6} {'N_Ni/N0':>10} {'N_Co/N0':>10} {'L [W]':>12} {'L [erg/s]':>11}")
    for td in (0.0, 10.0, 20.0, 50.0, 100.0, 200.0, 300.0):
        t = td * 86400.0
        n1, n2 = bateman(t, n0)
        if td > 0:
            r = rk4(t, n0)
            assert abs(r[0] / n1 - 1) < 1e-8 and abs(r[1] / n2 - 1) < 1e-8, f"RK4 frente a Bateman en {td} d"
        print(f"{td:6.0f} {n1 / n0:10.5f} {n2 / n0:10.5f} {lum(t, n0):12.4e} {lum(t, n0) * 1e7:11.3e}")
    # maximo de N_Co
    t_max = math.log(L1 / L2) / (L1 - L2)
    print(f"maximo de 56Co en t = {t_max / 86400:.2f} d con N_Co/N0 = {bateman(t_max, n0)[1] / n0:.5f}")
    # pendiente tardia
    t = 300 * 86400.0
    h = 0.01 * t
    pend = (math.log(lum(t + h, n0)) - math.log(lum(t - h, n0))) / (2 * h)
    print(f"pendiente tardia d ln L/dt = {pend * 86400:.6f} /d ; -1/tau_Co = {-L2 * 86400:.6f} /d ; caida de 1 magnitud cada {math.log(10 ** 0.4) / (-pend * 86400):.1f} d")
    assert abs(pend / (-L2) - 1) < 1e-4, "pendiente tardia"
    # relacion L(Ni)/L(Co) a t = 0 y 20 d
    n1, n2 = bateman(20 * 86400.0, n0)
    print(f"a 20 d: aporte del Ni = {E1 * L1 * n1 / lum(20 * 86400.0, n0) * 100:.1f} % de L")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
