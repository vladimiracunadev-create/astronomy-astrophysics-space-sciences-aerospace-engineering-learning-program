#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C03: matrices de Pauli, regla de Born, relacion de incertidumbre de Robertson y oscilacion de Rabi de un sistema de dos niveles.

Datos: ninguna constante fisica (se trabaja con hbar = 1). Las frecuencias de Rabi (1.0) y de detuning (0.0 y 0.8), los estados aleatorios (semilla fija) y el numero de disparos (100 000)
son ILUSTRATIVOS (sinteticos).
Modelo: sigma_x, sigma_y, sigma_z como matrices complejas 2x2; conmutador [sigma_x, sigma_y] = 2 i sigma_z; estado |psi> = cos(theta/2)|0> + e^(i phi) sin(theta/2)|1> y probabilidad de medir
sigma_z = +1 igual a cos^2(theta/2); desigualdad de Robertson Delta A Delta B >= |<[A, B]>|/2 sobre 1000 estados aleatorios; evolucion con H = (Omega sigma_x + Delta sigma_z)/2 integrada con RK4 y
comparada con P(t) = Omega^2/(Omega^2 + Delta^2) sen^2(sqrt(Omega^2 + Delta^2) t/2).
Supuestos: sistema cerrado de dos niveles, medicion proyectiva ideal. Validez: exacta para el modelo.
Tolerancia: norma conservada a 1e-9 en RK4; RK4 frente a la formula a 1e-8; frecuencia empirica de la medicion dentro de 4 errores estandar.
"""
from __future__ import annotations
import cmath
import math
import platform
import random
import sys

SX = [[0, 1], [1, 0]]
SY = [[0, -1j], [1j, 0]]
SZ = [[1, 0], [0, -1]]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mv(a, v):
    return [a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1]]


def esp(a, v):
    w = mv(a, v)
    return (v[0].conjugate() * w[0] + v[1].conjugate() * w[1]).real


def estado(theta, phi):
    return [math.cos(theta / 2) + 0j, cmath.exp(1j * phi) * math.sin(theta / 2)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c = [[mm(SX, SY)[i][j] - mm(SY, SX)[i][j] for j in range(2)] for i in range(2)]
    ok = all(abs(c[i][j] - 2j * SZ[i][j]) < 1e-12 for i in range(2) for j in range(2))
    print(f"[sigma_x, sigma_y] = 2 i sigma_z: {ok} ; sigma_x^2 = identidad: {mm(SX, SX) == [[1, 0], [0, 1]]}")
    assert ok
    # Born
    print(f"{'theta [deg]':>11} {'P(+z) = cos^2(theta/2)':>24} {'<sigma_z>':>10} {'<sigma_x>':>10} {'<sigma_y>':>10}")
    for th in (0, 30, 60, 90, 120, 180):
        psi = estado(math.radians(th), math.radians(40))
        pz = abs(psi[0]) ** 2
        assert abs(pz - math.cos(math.radians(th) / 2) ** 2) < 1e-12
        print(f"{th:11d} {pz:24.6f} {esp(SZ, psi):10.4f} {esp(SX, psi):10.4f} {esp(SY, psi):10.4f}")
    rng = random.Random(20261109)
    th = math.radians(60)
    p = math.cos(th / 2) ** 2
    n = 100000
    k = sum(1 for _ in range(n) if rng.random() < p)
    err = math.sqrt(p * (1 - p) / n)
    print(f"{n} medidas con theta = 60 deg: frecuencia = {k / n:.5f} ; P = {p:.5f} ; error estandar = {err:.5f} ; desviacion = {abs(k / n - p) / err:.2f} errores")
    assert abs(k / n - p) < 4 * err
    # Robertson
    peor = 1e9
    for _ in range(1000):
        psi = estado(math.acos(1 - 2 * rng.random()), 2 * math.pi * rng.random())
        dx = math.sqrt(max(0.0, 1 - esp(SX, psi) ** 2))
        dy = math.sqrt(max(0.0, 1 - esp(SY, psi) ** 2))
        cota = abs(esp(SZ, psi))        # |<[sx, sy]>|/2 = |<sz>|
        peor = min(peor, dx * dy - cota)
    print(f"desigualdad de Robertson Delta sigma_x Delta sigma_y >= |<sigma_z>| en 1000 estados: minimo de (producto - cota) = {peor:.3e}")
    assert peor > -1e-12
    # Rabi
    print(f"{'Omega':>6} {'Delta':>6} {'t':>6} {'P_RK4':>10} {'P_formula':>10} {'|norma - 1|':>12}")
    for om, de in ((1.0, 0.0), (1.0, 0.8)):
        w = math.sqrt(om * om + de * de)
        psi = [1 + 0j, 0j]
        h = lambda v: [0.5 * (om * v[1] + de * v[0]), 0.5 * (om * v[0] - de * v[1])]
        t, dt = 0.0, 1e-3
        marcas = {1.0: None, 2.0: None, 3.14159: None}
        for paso in range(1, 6285):
            f = lambda v: [-1j * x for x in h(v)]
            k1 = f(psi)
            k2 = f([psi[i] + 0.5 * dt * k1[i] for i in range(2)])
            k3 = f([psi[i] + 0.5 * dt * k2[i] for i in range(2)])
            k4 = f([psi[i] + dt * k3[i] for i in range(2)])
            psi = [psi[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(2)]
            t = paso * dt
            for m in marcas:
                if marcas[m] is None and abs(t - m) < dt / 2 + 1e-12:
                    marcas[m] = (t, abs(psi[1]) ** 2, abs(psi[0]) ** 2 + abs(psi[1]) ** 2)
        for m, (tt, pr, nm) in marcas.items():
            pf = om * om / (w * w) * math.sin(w * tt / 2) ** 2
            print(f"{om:6.1f} {de:6.1f} {tt:6.3f} {pr:10.6f} {pf:10.6f} {abs(nm - 1):12.2e}")
            assert abs(pr - pf) < 1e-8 and abs(nm - 1) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
