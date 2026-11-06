#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C13: áreas y volúmenes por integración.

Datos (PUBLICADOS): radios nominales de la Tierra R_eE = 6.3781e6 m y
R_pE = 6.3568e6 m (IAU 2015 B3, arXiv:1510.07674; la resolución recomienda el
volumen nominal 4 pi R_eE^2 R_pE / 3). Volumen terrestre de la ficha de la
Tierra de la NASA/NSSDC (2024-11-15): 108.321e10 km3 = 1.08321e21 m3.
Excentricidad 0.01671123 y a = 1.00000261 au (NASA/JPL, Approximate Positions).
Espejo parabólico: D = 1.0 m, f = 4.0 m (SINTÉTICO), densidad 2500 kg/m3 (SINTÉTICA).
Modelo: volúmenes de revolución por discos/cascarones y longitud de arco para
la superficie; z(r) = r^2/(4 f). Todo se compara con la fórmula cerrada.
Supuestos: sólidos ideales, sin tolerancias de fabricación. Validez: r <= R.
Tolerancias: Simpson n = 2000 a 1e-9 relativa; volumen terrestre dentro de 1e-3
del valor NASA (las fuentes dan 5-6 cifras y la IAU es nominal).
"""
from __future__ import annotations
import math, platform, sys


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    return s * h / 3


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # 1) esferoide oblato por discos: V = int_{-b}^{b} pi a^2 (1 - z^2/b^2) dz
    a, b = 6.3781e6, 6.3568e6
    V_num = simpson(lambda z: math.pi * a * a * (1 - z * z / (b * b)), -b, b)
    V_ana = 4 * math.pi * a * a * b / 3
    prueba(abs(V_num - V_ana) / V_ana < 1e-9, "esferoide por discos")
    V_nasa = 1.08321e21
    print(f"Esferoide nominal IAU: V_num = {V_num:.5e} m3; 4/3 pi a^2 b = {V_ana:.5e} m3")
    print(f"NASA (108.321e10 km3) = {V_nasa:.5e} m3; dif. relativa = {V_ana/V_nasa-1:+.2e}")
    prueba(abs(V_ana / V_nasa - 1) < 1e-3, "volumen contra NASA")
    esfera = 4 * math.pi * 6.371e6**3 / 3
    print(f"Esfera de radio medio 6371.000 km: {esfera:.5e} m3 ({esfera/V_nasa-1:+.2e} respecto a NASA)")
    # 2) espejo parabólico
    D, f = 1.0, 4.0
    R = D / 2
    sag = R * R / (4 * f)
    V_num = simpson(lambda r: 2 * math.pi * r * (sag - r * r / (4 * f)), 0.0, R)
    V_ana = math.pi * R**4 / (8 * f)
    prueba(abs(V_num - V_ana) / V_ana < 1e-9, "volumen del plato parabólico")
    A_num = simpson(lambda r: 2 * math.pi * r * math.sqrt(1 + (r / (2 * f)) ** 2), 0.0, R)
    A_ana = 8 * math.pi * f * f / 3 * ((1 + R * R / (4 * f * f)) ** 1.5 - 1)
    prueba(abs(A_num - A_ana) / A_ana < 1e-9, "área de la superficie")
    A_ap = math.pi * R * R
    print(f"\nEspejo D = {D} m, f = {f} m: flecha en el borde = {sag*1000:.3f} mm")
    print(f"Volumen retirado (plato) = {V_ana*1e6:.1f} cm3; masa de vidrio (2500 kg/m3, sintética) = {V_ana*2500:.3f} kg")
    print(f"Superficie = {A_ana:.6f} m2; apertura = {A_ap:.6f} m2; razón = {A_ana/A_ap:.6f}")
    # 3) elipse de la órbita terrestre
    e, a_au = 0.01671123, 1.00000261
    b_au = a_au * math.sqrt(1 - e * e)
    A_num = 4 * simpson(lambda x: b_au * math.sqrt(1 - (x / a_au) ** 2), 0.0, a_au, 20000)
    A_ana = math.pi * a_au * b_au
    print(f"\nÁrea de la elipse orbital: numérica {A_num:.8f} au2; pi a b = {A_ana:.8f} au2")
    prueba(abs(A_num - A_ana) / A_ana < 1e-6, "área de la elipse")
    print(f"Semieje menor b = {b_au:.8f} au (b/a = {b_au/a_au:.8f})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
