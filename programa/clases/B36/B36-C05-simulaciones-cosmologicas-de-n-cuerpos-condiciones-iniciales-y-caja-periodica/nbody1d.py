#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C05: simulacion de N cuerpos en una caja periodica (laminas 1D) con condiciones iniciales de Zel'dovich.

Datos: SINTETICOS. 256 laminas de masa igual en una caja periodica de longitud L = 1 (unidades de la caja) en un universo de Einstein-de Sitter (4 pi G rho_b = 1.5 H^2).
Desplazamiento inicial x = q - D (eps/k) sin(k q), k = 2 pi / L, con eps = 1 (la primera interseccion de laminas ocurre en a = 1/eps = 1). Sin fuente externa.
Modelo: x'' + (3/2a) x' = (3/2) a^-2 (x - q) en la variable a, con q la posicion lagrangiana del rango (la fuerza de 1D es EXACTA aun tras cruzarse las laminas);
integrador salto de rana (kick-drift-kick) con los factores exactos de a: Int a^-1/2 da y Int a^-3/2 da.
Segunda via: la solucion analitica de Zel'dovich x(a) = q + a s(q), exacta en 1D hasta el cruce de laminas.
Supuestos: 1D plano, EdS, sin suavizado. Validez: la comparacion con Zel'dovich solo antes del cruce (a < 1/eps).
Tolerancia: error en a = 0.81 inferior a 0,01 del espaciado medio con el paso fino; orden de convergencia entre 1.7 y 2.3.
"""
from __future__ import annotations
import math, platform

N = 256
EPS = 1.0
K = 2 * math.pi


def inicial(a):
    q = [(i + 0.5) / N for i in range(N)]
    s = [-(EPS / K) * math.sin(K * x) for x in q]
    x = [qi + a * si for qi, si in zip(q, s)]
    p = [a ** 1.5 * si for si in s]  # p = a^1.5 dx/da, con dx/da = s
    return q, s, x, p


def evolucionar(a0, a1, da):
    q, s, x, p = inicial(a0)
    n = int(round((a1 - a0) / da))
    a = a0
    for _ in range(n):
        am = a + da / 2
        an = a + da
        # kick de medio paso, drift de paso completo, kick de medio paso
        orden = sorted(range(N), key=lambda i: x[i])
        fk = 1.5 * 2 * (math.sqrt(am) - math.sqrt(a))
        for r, i in enumerate(orden):
            p[i] += fk * (x[i] - q[r])
        fd = -2 * (an ** -0.5 - a ** -0.5)
        for i in range(N):
            x[i] += p[i] * fd
        orden = sorted(range(N), key=lambda i: x[i])
        fk2 = 1.5 * 2 * (math.sqrt(an) - math.sqrt(am))
        for r, i in enumerate(orden):
            p[i] += fk2 * (x[i] - q[r])
        a = an
    return q, s, x, p


def zel(q, s, a):
    return [qi + a * si for qi, si in zip(q, s)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    esp = 1.0 / N
    print(f"{'da':>8} {'pasos':>6} {'error max en a=0.81 [espaciados]':>34}")
    err = {}
    for da in (0.004, 0.002, 0.001):
        q, s, x, p = evolucionar(0.01, 0.81, da)
        z = zel(q, s, 0.81)
        err[da] = max(abs(xi - zi) for xi, zi in zip(x, z)) / esp
        print(f"{da:8.4f} {int(round(0.80 / da)):6d} {err[da]:34.3e}")
    orden = math.log(err[0.004] / err[0.002]) / math.log(2), math.log(err[0.002] / err[0.001]) / math.log(2)
    print(f"orden de convergencia observado: {orden[0]:.2f} y {orden[1]:.2f}")
    # densidad en el centro del pico: sobredensidad en q = 0 entre las laminas N-1 y 0
    q, s, x, p = evolucionar(0.01, 0.81, 0.001)
    dx = x[0] + 1 - x[N - 1]
    rho_num = esp / dx
    rho_zel = 1.0 / (1 - 0.81 * EPS)
    print(f"densidad en q = 0 en a = 0.81: simulacion = {rho_num:.3f} ; Zel'dovich 1/(1 - a eps) = {rho_zel:.3f}")
    print(f"momento total = {sum(p):.2e} (debe ser ~0)")
    # despues del cruce
    q2, s2, x2, p2 = evolucionar(0.01, 1.51, 0.001)
    z2 = zel(q2, s2, 1.51)
    dz = max(abs(xi - zi) for xi, zi in zip(x2, z2)) / esp
    desord = sum(1 for i in range(N - 1) if x2[i] > x2[i + 1])
    print(f"a = 1.51 (tras el cruce): desviacion maxima respecto a Zel'dovich = {dz:.1f} espaciados ; pares de laminas fuera de orden = {desord}")
    assert err[0.001] < 1e-2
    assert 1.7 < orden[0] < 2.3 and 1.7 < orden[1] < 2.3
    assert abs(rho_num - rho_zel) / rho_zel < 0.02
    assert abs(sum(p)) < 1e-9
    assert dz > 2 and desord > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
