#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C03: Navier-Stokes 1D (flujo de Couette-Poiseuille entre placas) - analitico, tridiagonal y avance en el tiempo.

Consultado (2026-11-10): NASA Glenn, Navier-Stokes = Euler + terminos viscosos (difusion).
ILUSTRATIVOS (sinteticos, no medidos): h = 0.010 m, rho = 900 kg/m3, mu = 0.050 Pa s (aceite ilustrativo), U = 0.5 m/s (placa superior),
gradiente de presion G = -dp/dx = 2000 Pa/m, flujo unidireccional estacionario o en evolucion.
Ecuacion: rho du/dt = G + mu d2u/dy2, u(0) = 0, u(h) = U.
Solucion analitica: u = U y/h + G y (h - y)/(2 mu).
Via 2: sistema tridiagonal (Thomas) de la ecuacion estacionaria con 100 celdas.
Via 3: avance explicito en el tiempo (FTCS) desde u = 0 hasta el estacionario.
Tolerancias: error maximo de las vias numericas respecto a la analitica < 1e-6 (Thomas) y < 1e-4 (FTCS), relativos a U.
"""
import math, platform

H, RHO, MU, U, G = 0.010, 900.0, 0.050, 0.5, 2000.0
N = 100


def analitica(y):
    return U * y / H + G * y * (H - y) / (2 * MU)


def thomas(n):
    dy = H / n
    a = [1.0] * (n - 1)
    b = [-2.0] * (n - 1)
    c = [1.0] * (n - 1)
    d = [-G * dy * dy / MU] * (n - 1)
    d[-1] -= U
    for i in range(1, n - 1):
        w = a[i] / b[i - 1]
        b[i] -= w * c[i - 1]
        d[i] -= w * d[i - 1]
    x = [0.0] * (n - 1)
    x[-1] = d[-1] / b[-1]
    for i in range(n - 3, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    return [0.0] + x + [U]


def ftcs(n):
    dy = H / n
    nu = MU / RHO
    dt = 0.4 * dy * dy / nu
    u = [0.0] * (n + 1)
    u[-1] = U
    t = 0.0
    while t < 5.0:
        nuevo = u[:]
        for i in range(1, n):
            nuevo[i] = u[i] + dt * (G / RHO + nu * (u[i + 1] - 2 * u[i] + u[i - 1]) / (dy * dy))
        u = nuevo
        t += dt
    return u, t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nu = MU / RHO
    print(f"Datos ILUSTRATIVOS: h = {H} m, mu = {MU} Pa s, nu = {nu:.4e} m2/s, U = {U} m/s, G = {G} Pa/m")
    ut = thomas(N)
    uf, t = ftcs(50)
    ys = [i * H / N for i in range(N + 1)]
    e_t = max(abs(ut[i] - analitica(ys[i])) for i in range(N + 1)) / U
    ys50 = [i * H / 50 for i in range(51)]
    e_f = max(abs(uf[i] - analitica(ys50[i])) for i in range(51)) / U
    print(" y/h    u analitica [m/s]   u tridiagonal [m/s]   u FTCS [m/s]")
    for k in (0, 10, 20, 50, 80, 90, 100):
        yk = k / 100
        i50 = k // 2
        print(f" {yk:.2f}   {analitica(yk * H):12.6f}      {ut[k]:12.6f}      {uf[i50]:12.6f}")
    print(f"Error maximo / U: tridiagonal = {e_t:.2e} ; FTCS (t = {t:.2f} s) = {e_f:.2e}")
    tau0 = MU * (U / H + G * H / (2 * MU))
    tauh = MU * (U / H - G * H / (2 * MU))
    q = U * H / 2 + G * H ** 3 / (12 * MU)
    print(f"Tension en la pared inferior = {tau0:.3f} Pa ; en la superior = {tauh:.3f} Pa")
    print(f"Caudal por unidad de ancho q = {q:.6f} m2/s ; velocidad media = {q / H:.6f} m/s")
    # verificacion de q por trapecio sobre la solucion analitica
    qt = sum(0.5 * (analitica(ys[i]) + analitica(ys[i + 1])) * H / N for i in range(N))
    print(f"q por trapecio = {qt:.6f} m2/s")
    assert e_t < 1e-6 and e_f < 1e-4
    assert abs(qt - q) / q < 1e-4
    print("Pruebas superadas.")


main()
