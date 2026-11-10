#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C04: estatica plana de una suspension rocker-bogie y escalon maximo.

Datos consultados (2026-11-10): gravedad media de Marte 3.73 m/s2 y de la Luna 1.62 m/s2 (fichas NASA/NSSDC); Tierra g_n = 9.80665 m/s2
(NIST, CODATA 2022). De la pagina «Rover Components» de Mars 2020 (NASA, science.nasa.gov): seis ruedas, rocker-bogie con pivote diferencial,
rueda de 52.5 cm de diametro, masa 1025 kg; el rover puede cruzar obstaculos del tamano de una rueda. ILUSTRATIVOS (sinteticos, no la
geometria real de ningun rover): masa 1000 kg; posiciones x [m] (adelante positivo): rueda delantera +0.60, pivote rocker-bogie -0.20,
ruedas del bogie -0.20 +/- 0.35; pivote del cuerpo (diferencial) en la posicion de cargas iguales o desplazado a +0.20; coeficiente
de traccion disponible mu = 0.40.
Modelo: estatica plana de un lado (carga F = M g / 2 en el pivote del cuerpo); equilibrio de fuerzas y momentos del balancin y del bogie;
subida de un escalon h por la rueda delantera: F_h = N1 tan(alpha), cos(alpha) = (r - h)/r, empuje disponible mu (N2 + N3).
Sistema: marco del cuerpo, terreno plano. Supuestos: sin masa de la suspension, rueda rigida, sin traccion propia en la arista del escalon.
Tolerancias: suma de cargas = F y momento nulo < 1e-9 relativo; solucion de Gauss frente a formula cerrada < 1e-9.
"""
from __future__ import annotations
import math, platform

M = 1000.0
X1, XB, XBF, XBR = 0.60, -0.20, -0.20 + 0.35, -0.20 - 0.35
RADIO, MU = 0.2625, 0.40
GRAV = {"Tierra": 9.80665, "Marte": 3.73, "Luna": 1.62}


def gauss(a, b):
    n = len(b)
    a = [fila[:] + [b[i]] for i, fila in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            a[r] = [a[r][c] - f * a[i][c] for c in range(n + 1)]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (a[i][n] - sum(a[i][c] * x[c] for c in range(i + 1, n))) / a[i][i]
    return x


def cargas(f, xp):
    """Incognitas N1 (delantera), N2 (media), N3 (trasera). Ecuaciones: sum Fz, momento respecto al pivote del cuerpo, momento del bogie respecto a su pivote."""
    a = [[1, 1, 1],
         [X1 - xp, XBF - xp, XBR - xp],
         [0, XBF - XB, XBR - XB]]
    return gauss(a, [f, 0.0, 0.0])


def cargas_cerrada(f, xp):
    n1 = f * (xp - XB) / (X1 - XB)
    rb = f - n1
    n2 = rb * (XB - XBR) / (XBF - XBR)
    return [n1, n2, rb - n2]


def escalon_max(n1, n23):
    # F_h = N1 tan(alpha) <= mu (N2 + N3)
    ta = MU * n23 / n1
    alpha = math.atan(ta)
    return alpha, RADIO * (1.0 - math.cos(alpha))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xp_eq = (X1 + 2 * XB) / 3.0
    print(f"Geometria ILUSTRATIVA: rueda delantera {X1:+.2f} m, pivote rocker-bogie {XB:+.2f} m, bogie {XBF:+.2f} / {XBR:+.2f} m; pivote del cuerpo para cargas iguales = {xp_eq:+.4f} m")
    dmax = 0.0
    print(" cuerpo   g [m/s2]  F lado [N]  pivote [m]   N1 [N]   N2 [N]   N3 [N]  N1/F")
    for nom, g in GRAV.items():
        f = M * g / 2.0
        for xp in (xp_eq, 0.20):
            n = cargas(f, xp)
            c = cargas_cerrada(f, xp)
            dmax = max(dmax, max(abs(a - b) for a, b in zip(n, c)) / f)
            mom = sum(n[i] * (x - xp) for i, x in enumerate((X1, XBF, XBR))) / f
            assert abs(sum(n) - f) / f < 1e-9 and abs(mom) < 1e-9
            print(f"{nom:7s} {g:9.5f} {f:11.2f} {xp:+10.4f} {n[0]:9.2f} {n[1]:9.2f} {n[2]:9.2f} {n[0] / f:6.3f}")
    print(f"Gauss frente a formula cerrada: diferencia relativa maxima = {dmax:.2e}")
    print("Escalon maximo de la rueda delantera (mu = 0.40, r = 0.2625 m):")
    print(" pivote [m]  alpha [deg]  h_max [cm]  h_max/r  h_max/diametro")
    res = {}
    for xp in (xp_eq, 0.20):
        g_h = {}
        for nom, g in GRAV.items():
            n = cargas(M * g / 2.0, xp)
            al, h = escalon_max(n[0], n[1] + n[2])
            g_h[nom] = (al, h)
        res[xp] = g_h
        al, h = g_h["Marte"]
        print(f"{xp:+10.4f} {math.degrees(al):11.3f} {h * 100:11.3f} {h / RADIO:8.4f} {h / (2 * RADIO):10.4f}")
        assert max(abs(g_h[k][1] - g_h["Tierra"][1]) for k in g_h) < 1e-12
    print("El escalon maximo es el mismo en Tierra, Marte y Luna (las cargas y el empuje escalan con g).")
    print("Efecto del diferencial: la rueda delantera de un lado sube h; angulo de balancin y cabeceo del cuerpo (promedio de ambos lados)")
    print("    h [m]  balancin [deg]  cabeceo cuerpo [deg]  subida del cuerpo [cm]")
    for h in (0.05, 0.10, 0.20, 0.30):
        th = math.asin(h / (X1 - XB))
        zp = (xp_eq - XB) * math.sin(th)
        print(f"{h:9.2f} {math.degrees(th):15.3f} {math.degrees(th) / 2:21.3f} {zp / 2 * 100:22.3f}")
    n_eq = cargas(M * GRAV["Marte"] / 2.0, xp_eq)
    assert max(abs(x - M * GRAV["Marte"] / 6.0) for x in n_eq) < 1e-9
    print("Con el pivote en la posicion de cargas iguales, cada rueda lleva M g / 6: comprobado.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
