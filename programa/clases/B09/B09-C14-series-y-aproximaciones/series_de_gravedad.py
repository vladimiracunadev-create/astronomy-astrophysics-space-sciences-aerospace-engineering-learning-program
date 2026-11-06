#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C14: series de Taylor y aproximación de la gravedad con la altitud.

Datos: (GM)_E nominal = 3.986004e14 m3/s2 y R_eE nominal = 6.3781e6 m (IAU 2015
B3, arXiv:1510.07674; conversión). Altitudes de ejemplo: SINTÉTICAS.
Modelo: g(h) = GM/(R+h)^2 = g0 (1+x)^-2, x = h/R, con la serie binomial
(1+x)^-2 = sum_{n>=0} (-1)^n (n+1) x^n, válida para |x| < 1; y la serie de
Taylor de sin x con resto de Lagrange |R_n| <= |x|^(n+1)/(n+1)! (DLMF 1.4(vi),
ecs. 1.4.35-1.4.36). Supuestos: Tierra esférica, masa puntual.
Validez: |x| < 1 (h < R). Tolerancias: el error real nunca supera la cota
del resto; el error de orden k decrece al disminuir h.
"""
from __future__ import annotations
import math, platform, sys

GM, R = 3.986004e14, 6.3781e6
G0 = GM / R**2


def serie_g(x, n_terminos):
    return sum((-1) ** n * (n + 1) * x**n for n in range(n_terminos))


def seno_taylor(x, n_terminos):
    return sum((-1) ** k * x ** (2 * k + 1) / math.factorial(2 * k + 1) for k in range(n_terminos))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print(f"g0 = GM/R^2 = {G0:.5f} m/s2")
    print("\n h [km]      x=h/R      g exacta     err.rel orden 1   orden 2    orden 3")
    for h_km in (1, 10, 100, 400, 1000, 3000):
        x = h_km * 1e3 / R
        ex = (1 + x) ** -2
        errs = [abs(serie_g(x, k) - ex) / ex for k in (2, 3, 4)]
        print(f"{h_km:6d}  {x:11.4e}  {G0*ex:10.5f}  {errs[0]:14.3e}  {errs[1]:10.3e}  {errs[2]:10.3e}")
        # el error de orden k decrece con el orden mientras x < ~0.3
        if x < 0.3:
            prueba(errs[0] > errs[1] > errs[2], f"error decrece con el orden (h = {h_km} km)")
    # velocidad circular a 400 km: v = v0 (1+x)^(-1/2) ~ v0 (1 - x/2 + 3x^2/8)
    x = 4.0e5 / R
    v0 = math.sqrt(GM / R)
    v_ex = v0 * (1 + x) ** -0.5
    v1 = v0 * (1 - x / 2)
    v2 = v0 * (1 - x / 2 + 3 * x * x / 8)
    print(f"\nv_circular a 400 km: exacta {v_ex:.2f} m/s; orden 1 {v1:.2f} ({v1/v_ex-1:+.3%}); orden 2 {v2:.2f} ({v2/v_ex-1:+.4%})")
    # divergencia fuera del radio de convergencia
    print("\nSerie de (1+x)^-2 con x = 1.5 (fuera de |x| < 1):")
    for n in (3, 6, 12, 24):
        print(f"  {n:3d} términos: {serie_g(1.5, n): .4e}  (exacto {(1+1.5)**-2:.4f})")
    prueba(abs(serie_g(1.5, 24)) > 1e3, "la serie diverge para x = 1.5")
    # seno: cota del resto de Lagrange
    print("\nsin x en x = 1.0 rad: términos, valor, error real, cota")
    for k in (1, 2, 3, 4, 5, 6):
        v = seno_taylor(1.0, k)
        err = abs(v - math.sin(1.0))
        n = 2 * k  # el siguiente término tiene grado 2k+1: resto ≤ x^(2k+1)/(2k+1)!
        cota = 1.0 ** (2 * k + 1) / math.factorial(2 * k + 1)
        print(f"  {k} términos: {v:.10f}  err = {err:.3e}  cota = {cota:.3e}")
        prueba(err <= cota * (1 + 1e-12), "error ≤ cota de Lagrange")
    x = 10.0
    print(f"\nsin(10) con 3 términos = {seno_taylor(x, 3):.3f}; exacto = {math.sin(x):.6f} (la serie truncada falla lejos del centro)")
    # marea de C04 por serie: g(d-a) - g(d) = g(d) (2a/d + 3a^2/d^2 + ...)
    GM_L, d, a = 4.90e12, 3.844e8, 6.378137e6
    g = lambda r: GM_L / r**2
    ex = g(d - a) - g(d)
    o1 = g(d) * 2 * a / d
    o2 = g(d) * (2 * a / d + 3 * (a / d) ** 2)
    print(f"\nMarea lunar: exacta {ex:.4e}; orden 1 {o1:.4e} ({o1/ex-1:+.2%}); orden 2 {o2:.4e} ({o2/ex-1:+.3%})")
    prueba(abs(o2 / ex - 1) < abs(o1 / ex - 1), "orden 2 mejora al orden 1")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
