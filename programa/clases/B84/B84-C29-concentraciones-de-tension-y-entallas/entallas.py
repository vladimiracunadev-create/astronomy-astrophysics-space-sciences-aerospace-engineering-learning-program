#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C29: concentracion de tension en un agujero (solucion de Kirsch), factor de entalla a fatiga y efecto del ancho finito.

DATOS ILUSTRATIVOS (no consultados): placa de aluminio con agujero circular de radio a = 5 mm sometida a tension remota sigma = 100 MPa en la direccion x;
constante de sensibilidad a la entalla ILUSTRATIVA a_p = 0,5 mm (q = 1/(1 + a_p/r)); curva de Basquin ILUSTRATIVA S_f' = 900 MPa, b = -0,10.
Solucion de Kirsch (placa infinita): sigma_tt(r, th) = sigma/2 [(1 + a^2/r^2) - (1 + 3 a^4/r^4) cos 2th], th medido desde el eje de carga. En el borde (r = a):
sigma_tt = sigma (1 - 2 cos 2th): maximo 3 sigma en th = 90 grados, y -sigma en th = 0.
Ancho finito: formula empirica de la forma Kt = 3 - 3,14 x + 3,667 x^2 - 1,527 x^3 con x = d/w (diametro/ancho; formula de la literatura recordada, NO consultada: se rotula
como aproximacion ilustrativa) respecto de la tension neta.
Segunda via: equilibrio de fuerzas en la seccion x = 0: la integral numerica int_a^inf (sigma_tt(r, 90 grados) - sigma) dr debe igualar sigma a (la fuerza que el agujero desvia);
tolerancia relativa 1e-6 (integral por Simpson con cambio de variable t = a/r).
"""
from __future__ import annotations
import math, platform

A, SIG = 5e-3, 100.0
AP = 0.5e-3
SF, B = 900.0, -0.10


def stt(r, th, a=A, s=SIG):
    return s / 2 * ((1 + a * a / (r * r)) - (1 + 3 * a ** 4 / r ** 4) * math.cos(2 * th))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Placa con agujero de radio a = {A * 1e3:.0f} mm y tension remota {SIG:.0f} MPa (ILUSTRATIVO)")
    print("Tension circunferencial en el borde del agujero (Kirsch):")
    for deg in (0, 30, 60, 90):
        print(f"  theta = {deg:2d} grados: sigma_tt = {stt(A, math.radians(deg)):8.3f} MPa  (Kt local = {stt(A, math.radians(deg)) / SIG:5.2f})")
    print("Decaimiento a lo largo del eje y (theta = 90 grados): sigma_tt(r)/sigma")
    for rr in (1.0, 1.25, 1.5, 2.0, 3.0, 5.0):
        print(f"  r/a = {rr:4.2f}: {stt(rr * A, math.pi / 2) / SIG:6.3f}")
    # Integral de equilibrio con el cambio de variable t = a/r (dr = a/t^2 dt): integrando (sigma_tt - sigma) a/t^2, limite sigma a/2 en t = 0
    n = 200000
    h = 1.0 / n

    def g(t):
        return SIG * A / 2 if t == 0.0 else (stt(A / t, math.pi / 2) - SIG) * A / (t * t)

    s = g(0.0) + g(1.0)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(i * h)
    integral = s * h / 3
    print(f"Equilibrio: int_a^inf (sigma_tt - sigma) dr = {integral:.6e} MPa m ; sigma a = {SIG * A:.6e} ; dif relativa = {abs(integral - SIG * A) / (SIG * A):.1e}")
    assert abs(integral - SIG * A) / (SIG * A) < 1e-6
    print("Ancho finito (aproximacion empirica NO consultada) Kt respecto de la tension neta frente a d/w:")
    for x in (0.0, 0.1, 0.2, 0.3, 0.5):
        kt = 3 - 3.14 * x + 3.667 * x ** 2 - 1.527 * x ** 3
        print(f"  d/w = {x:.1f}: Kt_neto = {kt:.3f} ; sigma_max = Kt (sigma_bruta/(1 - d/w)) -> factor sobre la tension bruta = {kt / (1 - x):.3f}")
    print("Factor de entalla a fatiga: Kf = 1 + q (Kt - 1), q = 1/(1 + a_p/r) con a_p = 0,5 mm (ILUSTRATIVO):")
    for r in (1e-3, 2e-3, 5e-3, 10e-3):
        q = 1 / (1 + AP / r)
        kf = 1 + q * (3.0 - 1)
        print(f"  radio de entalla r = {r * 1e3:4.1f} mm: q = {q:.3f}  Kf = {kf:.3f}")
    q = 1 / (1 + AP / A)
    kf = 1 + q * 2
    print(f"Agujero de 5 mm: q = {q:.3f}, Kf = {kf:.3f}")
    print("Vida con Basquin (S_a nominal 60 MPa, R = -1): sin entalla frente a con entalla")
    for kfv in (1.0, kf):
        sa = 60.0 * kfv
        N = 0.5 * (sa / SF) ** (1 / B)
        print(f"  Kf = {kfv:.3f}: S_a local = {sa:7.2f} MPa -> N = {N:.3e} ciclos")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
