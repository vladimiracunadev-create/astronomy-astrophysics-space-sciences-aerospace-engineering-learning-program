#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C01: polinomios, esquema de Horner y factorización.

Datos: coeficientes de la oblicuidad media de la eclíptica ε_A(t) de la
precesión IAU 2006, tal como los reproducen las IERS Conventions (2010),
Nota Técnica 36, ec. (5.40) (datos PUBLICADOS, modelo). Elementos orbitales del
cometa 1P/Halley: NASA/JPL SBDB (consulta 2026-11-05; estimados).
Modelo: ε_A(t) = ε0 + c1 t + c2 t² + c3 t³ + c4 t⁴ + c5 t⁵, en segundos de arco,
con t en siglos julianos TT desde J2000,0.
Supuestos: se usa solo la parte polinómica; sin nutación; no hay incertidumbre
propagada. Validez de la clase: |t| ≤ 1 siglo (límite conservador de la clase).
Tolerancia de las pruebas: 1e-9 en valores exactos con enteros; 1e-12 relativa
entre Horner y evaluación directa.
"""
from __future__ import annotations
import platform, sys
from fractions import Fraction

EPS0 = 84381.406                 # arcsec, IERS TN36 (IAU 2006), t = 0
COEF = [EPS0, -46.836769, -0.0001831, 0.00200340, -0.000000576, -0.0000000434]  # grado 0..5


def horner(coef, x):
    """Evalúa c0 + c1 x + ... con una multiplicación y una suma por término."""
    r = 0.0
    for c in reversed(coef):
        r = r * x + c
    return r


def directo(coef, x):
    return sum(c * x**k for k, c in enumerate(coef))


def division_sintetica(coef_alto_a_bajo, r):
    """Divide p(x) por (x - r). Devuelve (cociente, resto)."""
    out = []
    acc = 0
    for c in coef_alto_a_bajo:
        acc = acc * r + c
        out.append(acc)
    return out[:-1], out[-1]


def pruebas():
    # 1) Horner = evaluación directa
    for t in (-1.0, -0.37, 0.0, 0.5, 1.0):
        a, b = horner(COEF, t), directo(COEF, t)
        assert abs(a - b) <= 1e-12 * abs(b), (t, a, b)
    # 2) ε_A(0) es el valor de referencia de la fuente
    assert horner(COEF, 0.0) == EPS0
    # 3) factorización exacta: x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
    p = [1, -6, 11, -6]
    for raiz in (1, 2, 3):
        q, resto = division_sintetica(p, raiz)
        assert resto == 0
    q, _ = division_sintetica(p, 1)
    q, _ = division_sintetica(q, 2)
    q, resto = division_sintetica(q, 3)
    assert q == [1] and resto == 0, (q, resto)
    # 4) diferencia de cuadrados con fracciones exactas: Q^2 - q^2 = (Q-q)(Q+q)
    Q, qv = Fraction(35, 1), Fraction(1, 2)
    assert Q**2 - qv**2 == (Q - qv) * (Q + qv)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (Horner = directo; factorización exacta; diferencia de cuadrados)")
    print("\nε_A(t) en grados, polinomio IAU 2006 (t en siglos desde J2000):")
    for t in (-1.0, 0.0, 1.0):
        e = horner(COEF, t)
        print(f"  t = {t:+.0f}  ->  {e:12.6f}\"  =  {e/3600:.6f}°")
    print("\nAporte de cada término en t = 1 siglo (segundos de arco):")
    for k, c in enumerate(COEF[1:], start=1):
        print(f"  grado {k}: {c:+.10f}")
    d = horner(COEF, 1.0) - EPS0
    print(f"  suma de cambios: {d:+.6f}\" por siglo  ({d/3600*1e3:+.3f} milésimas de grado)")
    # Halley: Q^2 - q^2 = 4 a^2 e
    a, e = 17.92863504856923, 0.9679359956953211
    q, Q = a * (1 - e), a * (1 + e)
    print(f"\nHalley: q = a(1-e) = {q:.6f} au (JPL: 0.574864); Q = a(1+e) = {Q:.5f} au (JPL: 35.28241)")
    print(f"  Q^2 - q^2 = {Q**2 - q**2:.4f}   (Q-q)(Q+q) = {(Q-q)*(Q+q):.4f}   4 a^2 e = {4*a*a*e:.4f}")
    # Kepler 3: P^2 = a^3 -> a^3 - P^2 con P = 8 yr es a^3 - 64 = (a-4)(a^2+4a+16)
    print("\nKepler (au, años): a^3 - 64 = (a - 4)(a^2 + 4a + 16); a = 4 au da P = 8 años:",
          4**3 == 8**2)


if __name__ == "__main__":
    main()
