#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C06: calibracion de parametros libres de un modelo de juguete y masas de una binaria eclipsante sintetica.

Datos: constante G de NIST CODATA 2022, GM_sol nominal de la UAI 2015 B3 (1,3271244e20 m3/s2) y 1 au = 1,495978707e11 m (IERS TN36), consultados el 2026-11-09 (solo resumen de la UAI).
Las respuestas del "modelo" (ln L y ln R en funcion de la abundancia de helio Y y del logaritmo del parametro de longitud de mezcla a), los objetivos, las incertidumbres
(0,2 % en L, 0,1 % en R) y la binaria (M1 = 1,10; M2 = 0,95 masas solares; P = 5,0 d; i = 88 grados; error de 0,5 % en K1 y K2) son ILUSTRATIVOS (sinteticos).
Modelo: f(theta) = (ln L, ln R) con una relacion no lineal de dos parametros; Newton con jacobiano por diferencias finitas; covarianza lineal C = J^-1 S J^-T contrastada con
2000 realizaciones Monte Carlo (semilla 20261109). Binaria: M sin^3 i = P (K1 + K2)^2 K2/(2 pi G) y su gemela; recuperacion de masas desde (K1, K2, P, i).
Supuestos: dos parametros, errores gaussianos independientes, orbita circular. Validez: orientativa.
Tolerancia: Newton recupera theta* a 1e-8; covarianza lineal frente a Monte Carlo dentro de 10 % en las desviaciones; masas recuperadas a 1e-9 sin ruido; Kepler III con la Tierra dentro de 1e-4.
"""
from __future__ import annotations
import math, platform, random, sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
AU = 1.495978707e11
DIA = 86400.0


def f(th):
    dY, da = th[0] - 0.25, th[1] - 0.50
    return (2.6 * dY - 0.9 * da + 3.0 * dY * da, -0.4 * dY - 0.5 * da + 1.2 * da * da)


def jac(th, h=1e-6):
    J = [[0.0, 0.0], [0.0, 0.0]]
    for j in range(2):
        a, b = list(th), list(th)
        a[j] += h
        b[j] -= h
        fa, fb = f(a), f(b)
        for i in range(2):
            J[i][j] = (fa[i] - fb[i]) / (2 * h)
    return J


def inv(J):
    d = J[0][0] * J[1][1] - J[0][1] * J[1][0]
    return [[J[1][1] / d, -J[0][1] / d], [-J[1][0] / d, J[0][0] / d]], d


def newton(obj, th0):
    th = list(th0)
    for it in range(1, 30):
        r = [f(th)[0] - obj[0], f(th)[1] - obj[1]]
        Ji, _ = inv(jac(th))
        d = [Ji[0][0] * r[0] + Ji[0][1] * r[1], Ji[1][0] * r[0] + Ji[1][1] * r[1]]
        th = [th[0] - d[0], th[1] - d[1]]
        if max(abs(d[0]), abs(d[1])) < 1e-9:
            return th, it
    raise RuntimeError("no converge")


def masas(K1, K2, P_s, inc):
    s3 = math.sin(inc) ** 3
    k = P_s / (2 * math.pi * G)
    return k * (K1 + K2) ** 2 * K2 / s3, k * (K1 + K2) ** 2 * K1 / s3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    th_true = [0.268, 0.62]
    obj = f(th_true)
    th, it = newton(obj, [0.25, 0.50])
    print(f"objetivos: ln L = {obj[0]:.6f} ; ln R = {obj[1]:.6f}")
    print(f"Newton: Y = {th[0]:.10f} ; a = ln(alpha/alpha0) = {th[1]:.10f} en {it} iteraciones")
    assert abs(th[0] - th_true[0]) < 1e-8 and abs(th[1] - th_true[1]) < 1e-8
    # covarianza lineal
    sg = (0.002, 0.001)
    Ji, det = inv(jac(th))
    C = [[sum(Ji[i][k] * sg[k] ** 2 * Ji[j][k] for k in range(2)) for j in range(2)] for i in range(2)]
    sY, sa = math.sqrt(C[0][0]), math.sqrt(C[1][1])
    rho = C[0][1] / (sY * sa)
    print(f"covarianza lineal: sigma(Y) = {sY:.5f} ; sigma(a) = {sa:.5f} ; correlacion = {rho:.3f} ; det J = {det:.4f}")
    rng = random.Random(20261109)
    ys, as_ = [], []
    for _ in range(2000):
        o = (obj[0] + rng.gauss(0, sg[0]), obj[1] + rng.gauss(0, sg[1]))
        t, _ = newton(o, th)
        ys.append(t[0])
        as_.append(t[1])
    my, ma = sum(ys) / len(ys), sum(as_) / len(as_)
    sdy = math.sqrt(sum((x - my) ** 2 for x in ys) / (len(ys) - 1))
    sda = math.sqrt(sum((x - ma) ** 2 for x in as_) / (len(as_) - 1))
    print(f"Monte Carlo (2000): sigma(Y) = {sdy:.5f} ; sigma(a) = {sda:.5f}")
    assert abs(sdy / sY - 1) < 0.10 and abs(sda / sa - 1) < 0.10
    # Kepler III
    P = 365.25 * DIA
    a = (GM_SOL * P**2 / (4 * math.pi**2)) ** (1 / 3)
    print(f"Kepler III (GM_sol, P = 365,25 d): a = {a:.6e} m ; 1 au = {AU:.6e} m ; a/au - 1 = {a / AU - 1:.2e}")
    assert abs(a / AU - 1) < 1e-4
    # binaria
    Msol = GM_SOL / G
    M1, M2 = 1.10 * Msol, 0.95 * Msol
    P_s, inc = 5.0 * DIA, math.radians(88.0)
    k = (2 * math.pi * G / P_s) ** (1 / 3) * math.sin(inc) / (M1 + M2) ** (2 / 3)
    K1, K2 = k * M2, k * M1
    print(f"K1 = {K1 / 1e3:.3f} km/s ; K2 = {K2 / 1e3:.3f} km/s")
    m1, m2 = masas(K1, K2, P_s, inc)
    print(f"masas recuperadas: M1 = {m1 / Msol:.9f} ; M2 = {m2 / Msol:.9f} masas solares nominales")
    assert abs(m1 / M1 - 1) < 1e-9 and abs(m2 / M2 - 1) < 1e-9
    ms = []
    for _ in range(2000):
        mm = masas(K1 * (1 + rng.gauss(0, 0.005)), K2 * (1 + rng.gauss(0, 0.005)), P_s, inc)
        ms.append(mm[0] / Msol)
    mu = sum(ms) / len(ms)
    sd = math.sqrt(sum((x - mu) ** 2 for x in ms) / (len(ms) - 1))
    # propagacion lineal: M1 ~ (K1+K2)^2 K2 -> dM/M = sqrt((2K1/(K1+K2)+...)) calculada a mano
    f1 = 2 * K1 / (K1 + K2)
    f2 = 2 * K2 / (K1 + K2) + 1
    lin = math.sqrt((f1 * 0.005) ** 2 + (f2 * 0.005) ** 2)
    print(f"incertidumbre relativa de M1: Monte Carlo = {sd / mu:.5f} ; lineal = {lin:.5f}")
    assert abs(sd / mu / lin - 1) < 0.10
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
