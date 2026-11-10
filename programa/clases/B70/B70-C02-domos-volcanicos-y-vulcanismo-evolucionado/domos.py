#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C02: perfil de un domo con resistencia a la fluencia (modelo plastico de Nye).

Datos: gravedades NASA/NSSDC (consultada 2026-11-09): Luna 1,62, Marte 3,73, Venus 8,87; Tierra 9,80665 m/s^2 (valor normal).
Densidad (2400 kg/m^3), resistencia a la fluencia (1,0e5 Pa), radio del domo y volumen: ILUSTRATIVOS (sinteticos).
Modelo: equilibrio de fuerzas en un material perfectamente plastico, dh/dr = -tau/(rho g h), con h(R) = 0. Solucion h^2 = 2 tau (R - r)/(rho g).
Altura central H = sqrt(2 tau R/(rho g)); volumen V = (8 pi/15) sqrt(2 tau/(rho g)) R^(5/2).
Se integra numericamente la ecuacion diferencial con Runge-Kutta 4 en la variable u = h^2 (du/dr = -2 tau/(rho g)) desde la orilla,
y el volumen con Simpson, y se compara con la solucion cerrada. Tambien se invierte V -> R por biseccion.
Supuestos: material plastico ideal, base plana, simetria axial, sin termica ni cristalizacion. Validez: ilustrativa.
Tolerancia: 1e-9 relativo en la altura, 1e-6 en el volumen, 1e-9 en la inversion.
"""
from __future__ import annotations
import math, platform

RHO, TAU = 2400.0, 1.0e5
G_TAB = {"Luna": 1.62, "Marte": 3.73, "Venus": 8.87, "Tierra": 9.80665}

def altura_central_rk4(R, g, n=4000):
    """Integra du/dr = -2 tau/(rho g) desde r = R (u = 0) hasta r = 0; devuelve H = sqrt(u(0))."""
    f = lambda r, u: -2 * TAU / (RHO * g)
    h = -R / n
    r, u = R, 0.0
    for _ in range(n):
        k1 = f(r, u); k2 = f(r + h / 2, u + h * k1 / 2); k3 = f(r + h / 2, u + h * k2 / 2); k4 = f(r + h, u + h * k3)
        u += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        r += h
    return math.sqrt(u)

def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def volumen_analitico(R, g):
    return 8 * math.pi / 15 * math.sqrt(2 * TAU / (RHO * g)) * R ** 2.5

def volumen_numerico(R, g):
    # sustitucion r = R - s^2 elimina la raiz en el extremo: dV = 2 pi (R - s^2) sqrt(2 tau/(rho g)) s * 2 s ds
    c = math.sqrt(2 * TAU / (RHO * g))
    return simpson(lambda s: 2 * math.pi * (R - s * s) * c * s * 2 * s, 0.0, math.sqrt(R))

def radio_para_volumen(V, g):
    lo, hi = 1.0, 1e6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if volumen_analitico(mid, g) < V:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    R = 1500.0
    print(f"Domo con R = {R:.0f} m, rho = {RHO:.0f} kg/m^3, tau = {TAU:.1e} Pa (ilustrativos)")
    for nombre, g in G_TAB.items():
        Ha = math.sqrt(2 * TAU * R / (RHO * g))
        Hn = altura_central_rk4(R, g)
        assert abs(Ha - Hn) / Ha < 1e-9, "altura RK4 no coincide"
        Va, Vn = volumen_analitico(R, g), volumen_numerico(R, g)
        assert abs(Va - Vn) / Va < 1e-6, "volumen no coincide"
        print(f"  {nombre:7s} g = {g:7.5f}: H = {Ha:7.1f} m (RK4 {Hn:7.1f}) ; V = {Va/1e9:.4f} km^3 (Simpson {Vn/1e9:.4f}) ; H/R = {Ha/R:.3f}")
    Ht = math.sqrt(2 * TAU * R / (RHO * 9.80665))
    Hm = math.sqrt(2 * TAU * R / (RHO * 3.73))
    print(f"Cociente H(Marte)/H(Tierra) = {Hm/Ht:.4f} ; sqrt(g_T/g_M) = {math.sqrt(9.80665/3.73):.4f}")
    assert abs(Hm / Ht - math.sqrt(9.80665 / 3.73)) < 1e-12
    V = 1.0e9  # 1 km^3
    print("Radio de un domo de 1 km^3 (resistencia fija):")
    for nombre, g in G_TAB.items():
        Rv = radio_para_volumen(V, g)
        assert abs(volumen_analitico(Rv, g) - V) / V < 1e-9
        Hv = math.sqrt(2 * TAU * Rv / (RHO * g))
        print(f"  {nombre:7s}: R = {Rv:7.1f} m ; H = {Hv:6.1f} m")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
