#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C18: cónicas y clasificación de órbitas por excentricidad.

Datos (PUBLICADOS; estimados): NASA/JPL SBDB (consulta 2026-11-05): 1P/Halley (solución del
2025-11-21): e = 0,9679359956953211, a = 17,92863504856923 au, q = 0,5748638313743413 au;
1I/ʻOumuamua (A/2017 U1; solución «Sol. 7c, Micheli et al. 2018», 2018-06-26):
e = 1,201133796102373, a = -1,27234500742808 au, q = 0,2559115812959116 au.
Modelo: r(θ) = p/(1 + e cos θ), con p = q(1 + e) (semilado recto), foco en el origen y
θ desde el periastro; propiedad foco–directriz |PF| = e·dist(P, directriz), directriz x = p/e.
Supuestos: órbita kepleriana plana, 0 <= e. Validez: elipse y círculo para todo θ; hipérbola
solo con 1 + e cos θ > 0, es decir |θ| < arccos(-1/e); la parábola, |θ| < 180°.
Tolerancia de las pruebas: 1e-9.
"""
from __future__ import annotations
import math, platform, sys

CASOS = {
    "Halley (JPL)": dict(e=0.9679359956953211, q=0.5748638313743413, a=17.92863504856923),
    "ʻOumuamua (JPL)": dict(e=1.201133796102373, q=0.2559115812959116, a=-1.27234500742808),
}


def tipo(e):
    if abs(e) < 1e-12:
        return "circunferencia"
    if e < 1 - 1e-12:
        return "elipse"
    if abs(e - 1) <= 1e-12:
        return "parábola"
    return "hipérbola"


def r_conica(theta, p, e):
    d = 1 + e * math.cos(theta)
    return p / d if d > 0 else float("inf")


def pruebas():
    assert [tipo(e) for e in (0, 0.5, 1, 2)] == ["circunferencia", "elipse", "parábola", "hipérbola"]
    for e in (0.0, 0.3, 0.9679359956953211, 1.0, 1.201133796102373, 3.0):
        q = 0.7
        p = q * (1 + e)
        assert abs(r_conica(0.0, p, e) - q) < 1e-12                     # r(0) = q
        # propiedad foco–directriz: |PF| = e · distancia a x = p/e (si e > 0)
        lim = math.acos(-1 / e) if e > 1 else math.pi
        for k in range(-8, 9):
            th = 0.999 * lim * k / 8
            r = r_conica(th, p, e)
            x, y = r * math.cos(th), r * math.sin(th)
            if e > 0:
                assert abs(r - e * abs(p / e - x)) < 1e-9, (e, th)
    # elipse: a = q/(1-e); hipérbola: a < 0 y q = a(1-e)
    h = CASOS["ʻOumuamua (JPL)"]
    assert abs(h["a"] * (1 - h["e"]) - h["q"]) < 1e-12
    h = CASOS["Halley (JPL)"]
    assert abs(h["a"] * (1 - h["e"]) - h["q"]) < 1e-12
    # Parábola: r(180°) infinito; hipérbola: asíntota θ∞ = arccos(-1/e)
    assert r_conica(math.pi, 1.0, 1.0) == float("inf")
    assert abs(math.cos(math.acos(-1 / 1.5)) + 1 / 1.5) < 1e-15


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (clasificación, r(0)=q, foco–directriz, a(1−e)=q, parábola, asíntota)")
    print(f"\n{'Cuerpo':<17}{'e':>9}{'tipo':>13}{'q (au)':>10}{'a (au)':>11}{'p (au)':>10}")
    for n, c in CASOS.items():
        p = c["q"] * (1 + c["e"])
        print(f"{n:<17}{c['e']:9.5f}{tipo(c['e']):>13}{c['q']:10.5f}{c['a']:11.4f}{p:10.5f}")
    c = CASOS["ʻOumuamua (JPL)"]
    e, p = c["e"], c["q"] * (1 + c["e"])
    th_inf = math.degrees(math.acos(-1 / e))
    print(f"\nʻOumuamua: p = q(1+e) = {p:.5f} au; ángulo de la asíntota θ∞ = arccos(−1/e) = {th_inf:.2f}°")
    print(f"  giro total de la dirección de movimiento = 2θ∞ − 180° = {2 * th_inf - 180:.2f}° "
          f"(cálculo propio; coincide con 2·arcsen(1/e) = {2 * math.degrees(math.asin(1 / e)):.2f}°)")
    print("\nr(θ) (au) para distintas excentricidades con el mismo perihelio q = 0,2559 au (θ en °):")
    print(f"{'θ':>5}" + "".join(f"{t:>14}" for t in ("e=0", "e=0,5", "e=1", "e=1,2011")))
    for deg in (0, 30, 60, 90, 120, 140):
        th = math.radians(deg)
        fila = [r_conica(th, 0.2559115812959116 * (1 + ee), ee) for ee in (0.0, 0.5, 1.0, 1.201133796102373)]
        print(f"{deg:5d}" + "".join(f"{v:14.4f}" for v in fila))
    print("\nProp. foco–directriz comprobada para e = 0,5; 1; 1,2011 (ver pruebas).")


if __name__ == "__main__":
    main()
