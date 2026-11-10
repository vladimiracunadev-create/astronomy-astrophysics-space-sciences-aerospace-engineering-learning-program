#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C07: aceleracion electrostatica de iones de xenon y ley de Child-Langmuir.

Datos CONSULTADOS (2026-11-10): e = 1.602176634e-19 C (exacta), u = 1.66053906892e-27 kg, eps0 = 8.8541878188e-12 F/m, g0 = 9.80665 m/s2 (NIST CODATA);
Dawn (NASA/JPL): empuje maximo 91 mN y xenon ~3.25 mg/s.
NO CONSULTADO (valor de manual): masa atomica relativa del xenon, 131.293.
ILUSTRATIVO (sintetico): tension de haz V = 1100 V (no es un dato publicado de Dawn), separacion entre rejillas d = 0.6 mm, iones Xe+ (carga unica).
Modelo: ve = sqrt(2 e V/m_i); F = mdot_i ve; corriente I = mdot_i e/m_i; limite de carga espacial j = (4 eps0/9) sqrt(2e/m) V^(3/2)/d^2 (1D, sin carga inicial).
Segunda via para Child-Langmuir: integral numerica de x(V) = int dphi/phi'(phi) con la primera integral de la ecuacion de Poisson, y biseccion en j.
Tolerancia: j numerica frente a la formula cerrada < 1e-6 relativa; Isp = ve/g0 a 1e-12.
"""
from __future__ import annotations
import math, platform

E = 1.602176634e-19
U = 1.66053906892e-27
EPS0 = 8.8541878188e-12
G0 = 9.80665
MI = 131.293 * U  # kg, masa del ion Xe+ (se ignora la masa del electron faltante)


def ve_ion(v):
    return math.sqrt(2 * E * v / MI)


def j_cl(v, d):
    return 4 * EPS0 / 9 * math.sqrt(2 * E / MI) * v ** 1.5 / d ** 2


def distancia(j, v, n=20000):
    """x(V) con phi = s^4: integrando 4 s^2 / C, C = 2 sqrt((j/eps0) sqrt(m/(2e))). Regla del punto medio."""
    c = 2 * math.sqrt(j / EPS0 * math.sqrt(MI / (2 * E)))
    s_max = v ** 0.25
    h = s_max / n
    return sum(4 * ((k + 0.5) * h) ** 2 / c for k in range(n)) * h


def j_numerica(v, d):
    lo, hi = 1e-3, 1e5
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if distancia(mid, v) > d:
            lo = mid  # mayor j acorta la distancia; si x > d hace falta mas j
        else:
            hi = mid
    return math.sqrt(lo * hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Masa del ion Xe+ = {MI:.4e} kg (131.293 u, valor de manual NO consultado)")
    v, d = 1100.0, 0.6e-3
    ve = ve_ion(v)
    print(f"V = {v:.0f} V (ILUSTRATIVA): Ve = {ve:.0f} m/s ; Isp = {ve/G0:.1f} s")
    assert abs(ve / G0 - math.sqrt(2 * E * v / MI) / G0) < 1e-9
    f, md = 0.091, 3.25e-6
    md_ion = f / ve
    i_haz = md_ion * E / MI
    print(f"Dawn (F y mdot consultados): mdot de iones = F/Ve = {md_ion*1e6:.3f} mg/s ; corriente de haz = {i_haz:.3f} A ; utilizacion de masa = {md_ion/md:.3f}")
    print(f"Velocidad equivalente consultada (F/mdot) = {f/md:.0f} m/s ; Ve_ion*utilizacion = {ve*md_ion/md:.0f} m/s")
    assert abs(ve * md_ion / md - f / md) < 1e-6
    jc = j_cl(v, d)
    jn = j_numerica(v, d)
    print(f"Child-Langmuir (d = {d*1e3:.1f} mm): j = {jc:.2f} A/m2 ; numerica = {jn:.2f} A/m2 ; diferencia relativa = {abs(jc-jn)/jc:.1e}")
    assert abs(jc - jn) / jc < 1e-6
    print("  V [V]   Ve [m/s]   Isp [s]   j_max [A/m2]")
    for vv in (500.0, 1100.0, 2000.0, 3000.0):
        print(f" {vv:>6.0f} {ve_ion(vv):>10.0f} {ve_ion(vv)/G0:>9.1f} {j_cl(vv, d):>13.1f}")
    a = ve_ion(2000.0) / ve_ion(500.0)
    assert abs(a - 2.0) < 1e-12
    print(f"Ve(2000 V)/Ve(500 V) = {a:.6f} (esperado 2 por Ve ~ V^(1/2)); j escala como V^(3/2): j(2000)/j(500) = {j_cl(2000.0,d)/j_cl(500.0,d):.4f}")
    area = f / (jc * math.sqrt(2 * MI * v / E))
    print(f"Area de rejilla minima para 91 mN con j_max: A = F/(j sqrt(2 m V/e)) = {area*1e4:.1f} cm2 (diametro equivalente {2*math.sqrt(area/math.pi)*100:.1f} cm)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
