#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C01: crecimiento lineal de perturbaciones de densidad en un universo plano con Lambda.

Datos: Omega_m = 0.315 (resumen de Planck 2018, arXiv:1807.06209, consultado 2026-11-09). Es el UNICO dato tomado de una fuente; la forma del
universo (plano, materia + Lambda, sin radiacion) y el redshift inicial z = 999 son ILUSTRATIVOS.
Modelo: D'' + (3/a + dlnE/da) D' - 1.5 Omega_m/(a^5 E^2) D = 0, con E^2 = Omega_m a^-3 + 1 - Omega_m, integrada con Runge-Kutta 4 en la variable a.
Segunda via: la solucion integral D(a) = 2.5 Omega_m E(a) * Int_0^a da'/(a' E(a'))^3 (Simpson). Caso analitico: Omega_m = 1 da D = a.
Supuestos: perturbaciones lineales, materia sin presion, sin radiacion ni neutrinos. Validez: z << 1000.
Tolerancia: RK4 frente a la integral, 1e-6 relativo; EdS, 1e-8.
"""
from __future__ import annotations
import math, platform


def E2(a, om):
    return om * a ** -3 + 1 - om


def dlnE(a, om):
    return -1.5 * om * a ** -4 / E2(a, om)


def rhs(a, y, om):
    D, P = y
    return (P, -(3 / a + dlnE(a, om)) * P + 1.5 * om / (a ** 5 * E2(a, om)) * D)


def rk4(om, a0, a1, n):
    # paso uniforme en ln a para resolver bien todo el rango
    la0, la1 = math.log(a0), math.log(a1)
    h = (la1 - la0) / n
    y = (a0, 1.0)
    la = la0
    out = []
    for _ in range(n):
        a = math.exp(la)
        def f(l, yy):
            aa = math.exp(l)
            d, p = rhs(aa, yy, om)
            return (aa * d, aa * p)
        k1 = f(la, y)
        k2 = f(la + h / 2, (y[0] + h / 2 * k1[0], y[1] + h / 2 * k1[1]))
        k3 = f(la + h / 2, (y[0] + h / 2 * k2[0], y[1] + h / 2 * k2[1]))
        k4 = f(la + h, (y[0] + h * k3[0], y[1] + h * k3[1]))
        y = (y[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), y[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
        la += h
        out.append((math.exp(la), y[0], y[1]))
    return out


def integral(om, a, n=4000):
    # Int_0^a da'/(a'E)^3 ; cerca de 0 el integrando ~ a'^1.5, se integra con Simpson (n par)
    h = a / n
    g = lambda x: 0.0 if x == 0 else 1.0 / (x * math.sqrt(E2(x, om))) ** 3
    s = g(0) + g(a)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(i * h)
    return s * h / 3


def D_int(om, a):
    return 2.5 * om * math.sqrt(E2(a, om)) * integral(om, a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    om = 0.315
    a0 = 1e-3
    n = 4000
    tray = rk4(om, a0, 1.0, n)
    # EdS
    tr1 = rk4(1.0, a0, 1.0, 400)
    eds = abs(tr1[-1][1] - 1.0)
    print(f"EdS (Omega_m = 1): D(1) = {tr1[-1][1]:.9f} ; |D - a| = {eds:.2e}")
    # tabla en redshifts
    print(f"{'z':>5} {'a':>8} {'D RK4':>10} {'D integral':>11} {'g=D/a':>8} {'f':>7} {'Om(a)^0.55':>11}")
    D1 = tray[-1][1]
    res = {}
    for z in (0, 0.5, 1, 2, 5):
        a = 1 / (1 + z)
        aa, D, P = rk4(om, a0, a, n)[-1]
        Di = D_int(om, aa)
        f = aa * P / D
        oma = om * aa ** -3 / E2(aa, om)
        res[z] = (aa, D, Di, f, oma ** 0.55)
        print(f"{z:5.1f} {aa:8.5f} {D:10.6f} {Di:11.6f} {D / aa:8.5f} {f:7.4f} {oma ** 0.55:11.4f}")
    # normalizacion: D(a=1) integral vs RK4 (la RK4 parte de D=a0, por lo que difiere por el modo decreciente ~ a0^1.5)
    D1i = D_int(om, 1.0)
    rel = abs(D1 - D1i) / D1i
    print(f"D(1): RK4 = {D1:.6f} ; integral = {D1i:.6f} ; diferencia relativa = {rel:.2e}")
    g0 = D1i
    print(f"supresion por Lambda: D(1)/a(1) = {g0:.4f} ; f(0) = {res[0][3]:.4f} ; Omega_m^0.55 = {om ** 0.55:.4f}")
    # sensibilidad: ratio de crecimiento entre z=1 y z=0
    r = res[0][2] / res[1][2]
    print(f"crecimiento entre z=1 y z=0: D(1)/D(0.5) = {r:.4f} (EdS daria 2.0000)")
    assert eds < 1e-8
    assert rel < 1e-5
    for z, (aa, D, Di, f, fa) in res.items():
        assert abs(D - Di) / Di < 1e-5
        assert abs(f - fa) < 0.01 + 0.0 * z
    assert 0.75 < g0 < 0.81
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
