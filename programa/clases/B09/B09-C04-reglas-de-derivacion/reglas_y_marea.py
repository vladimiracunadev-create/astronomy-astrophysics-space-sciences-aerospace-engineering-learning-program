#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C04: reglas de derivación y aceleración de marea.

Datos: GM de la Luna = 4.90e3 km3/s2 (NASA, ficha lunar, 3 cifras), distancia
media Tierra-Luna 384 400 km y radio ecuatorial terrestre 6378.137 km (NASA,
fichas de la Tierra y la Luna, actualizadas 2024). Son valores publicados con
pocas cifras: el resultado de marea es una ESTIMACIÓN de orden de magnitud.
Modelo: g(r) = GM/r^2 -> dg/dr = -2 GM/r^3 (regla de la potencia; DLMF 1.4(iii)).
La diferencia entre el lado cercano y el centro es ~ 2 GM R / d^3.
Las reglas del producto, el cociente y la cadena se verifican con números
duales (diferenciación automática de modo directo) frente a derivadas exactas.
Supuestos: Luna puntual, órbita circular, sin rotación. Validez: R << d.
Tolerancia: 1e-12 relativa en las reglas; 5 % entre la derivada y la
diferencia exacta de marea.
"""
from __future__ import annotations
import math, platform, sys


class Dual:
    """Número dual a + b*eps con eps^2 = 0: lleva el valor y su derivada."""
    def __init__(self, a, b=0.0):
        self.a, self.b = a, b
    def _c(o):
        return o if isinstance(o, Dual) else Dual(o)
    def __add__(s, o):
        o = Dual._c(o); return Dual(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o):
        o = Dual._c(o); return Dual(s.a - o.a, s.b - o.b)
    def __rsub__(s, o):
        return Dual._c(o) - s
    def __mul__(s, o):                      # regla del producto
        o = Dual._c(o); return Dual(s.a * o.a, s.b * o.a + s.a * o.b)
    __rmul__ = __mul__
    def __truediv__(s, o):                  # regla del cociente
        o = Dual._c(o); return Dual(s.a / o.a, (s.b * o.a - s.a * o.b) / o.a**2)
    def __rtruediv__(s, o):
        return Dual._c(o) / s
    def __pow__(s, n):                      # regla de la potencia
        return Dual(s.a**n, n * s.a**(n - 1) * s.b)


def dln(x):                                 # cadena: (ln u)' = u'/u
    return Dual(math.log(x.a), x.b / x.a)


def dsin(x):
    return Dual(math.sin(x.a), math.cos(x.a) * x.b)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def cerca(a, b, tol=1e-12):
    return abs(a - b) <= tol * max(1.0, abs(b))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    x = Dual(1.3, 1.0)
    # producto: d/dx [x^2 sin x] = 2x sin x + x^2 cos x
    r = x**2 * dsin(x)
    ex = 2 * 1.3 * math.sin(1.3) + 1.3**2 * math.cos(1.3)
    prueba(cerca(r.b, ex), "producto"); print(f"producto  : {r.b:.12f} (exacto {ex:.12f})")
    # cociente: d/dx [x/(1+x^2)] = (1-x^2)/(1+x^2)^2
    r = x / (1 + x**2)
    ex = (1 - 1.3**2) / (1 + 1.3**2) ** 2
    prueba(cerca(r.b, ex), "cociente"); print(f"cociente  : {r.b:.12f} (exacto {ex:.12f})")
    # cadena: d/dx ln(1+x^2) = 2x/(1+x^2)
    r = dln(1 + x**2)
    ex = 2 * 1.3 / (1 + 1.3**2)
    prueba(cerca(r.b, ex), "cadena"); print(f"cadena    : {r.b:.12f} (exacto {ex:.12f})")

    # Tsiolkovsky: v = ve ln(m0/m); con m(t) = m0 - mdot t, dv/dt = ve mdot/m
    ve, m0, mdot, t = 3000.0, 100_000.0, 500.0, 40.0
    tt = Dual(t, 1.0)
    v = ve * dln(m0 / (m0 - mdot * tt))
    ex = ve * mdot / (m0 - mdot * t)
    prueba(cerca(v.b, ex), "aceleración de Tsiolkovsky")
    print(f"dv/dt (t=40 s) = {v.b:.6f} m/s2 (exacto {ex:.6f}); v = {v.a:.3f} m/s")

    # marea lunar
    GM_L = 4.90e12                          # m3/s2  (4.90e3 km3/s2)
    d, R = 3.844e8, 6.378137e6              # m
    dgdr = -2 * GM_L / d**3                 # derivada de g(r) en r = d
    marea_derivada = abs(dgdr) * R
    g = lambda r_: GM_L / r_**2
    marea_exacta = g(d - R) - g(d)
    marea_g = marea_exacta / 9.80665
    print(f"|dg/dr| = {abs(dgdr):.3e} s-2;  marea ~ |dg/dr| R = {marea_derivada:.4e} m/s2")
    print(f"diferencia exacta g(d-R)-g(d) = {marea_exacta:.4e} m/s2  ({marea_g:.2e} g_n)")
    rel = abs(marea_derivada - marea_exacta) / marea_exacta
    print(f"diferencia relativa derivada vs exacta = {rel:.3%}")
    prueba(rel < 0.05, "derivada ~ diferencia exacta (5 %)")
    prueba(1e-6 < marea_derivada < 1.4e-6, "orden de magnitud de la marea lunar")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
