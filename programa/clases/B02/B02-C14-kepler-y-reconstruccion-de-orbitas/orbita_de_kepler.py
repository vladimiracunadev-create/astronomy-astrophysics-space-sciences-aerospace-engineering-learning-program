#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C14: reconstruir una órbita con las leyes de Kepler.

Datos PUBLICADOS (NASA NSSDC, razones respecto de la Tierra, act. 18-mar-2025, consultada el
2026-11-05): período y distancia al Sol de Mercurio, Venus, Marte, Júpiter y Saturno. Semieje
mayor de Marte (227,956 millones de km) y período (686,980 d) de la ficha de Marte.
La excentricidad e = 0,2 es SINTÉTICA (ilustra una órbita; no es la de Marte).
Modelo: problema de dos cuerpos kepleriano (ecuación de Kepler M = E - e*sen E).
Supuestos: órbita en un plano, Sol en un foco. Validez: forma y ritmo de la órbita; no son efemérides.
Tolerancias: ecuación de Kepler 1e-12; ley de las áreas 1e-4; tercera ley 2 % con datos de 3 cifras.
"""

from __future__ import annotations

import math
import sys

# NASA, razones respecto de la Tierra: (período, distancia al Sol)
PLANETAS = {
    "Mercurio": (0.241, 0.387),
    "Venus": (0.615, 0.723),
    "Tierra": (1.000, 1.000),
    "Marte": (1.88, 1.52),
    "Júpiter": (11.9, 5.20),
    "Saturno": (29.4, 9.57),
}
A_MARTE = 227.956       # 10^6 km
T_MARTE = 686.980       # d
E_SINT = 0.2            # SINTÉTICA


def resolver_kepler(m: float, e: float) -> float:
    """Resuelve M = E - e*sen E con el método de Newton."""
    x = m if e < 0.8 else math.pi
    for _ in range(50):
        d = (x - e * math.sin(x) - m) / (1.0 - e * math.cos(x))
        x -= d
        if abs(d) < 1e-14:
            break
    return x


def posicion(t: float, periodo: float, a: float, e: float) -> tuple[float, float]:
    """Posición (x, y) respecto del Sol (foco), con el perihelio sobre el eje x."""
    m = 2.0 * math.pi * (t / periodo % 1.0)
    big_e = resolver_kepler(m, e)
    return a * (math.cos(big_e) - e), a * math.sqrt(1.0 - e * e) * math.sin(big_e)


def area_barrida(t0: float, t1: float, periodo: float, a: float, e: float, n: int = 4000) -> float:
    s = 0.0
    prev = posicion(t0, periodo, a, e)
    for i in range(1, n + 1):
        cur = posicion(t0 + (t1 - t0) * i / n, periodo, a, e)
        s += 0.5 * abs(prev[0] * cur[1] - cur[0] * prev[1])
        prev = cur
    return s


def pruebas() -> None:
    for e in (0.0, 0.2, 0.7):
        for m in (0.1, 1.0, 3.0):
            x = resolver_kepler(m, e)
            assert abs(x - e * math.sin(x) - m) < 1e-12
    assert abs(resolver_kepler(1.234, 0.0) - 1.234) < 1e-12                   # órbita circular: E = M
    a1 = area_barrida(0.0, T_MARTE / 10, T_MARTE, A_MARTE, E_SINT)
    a2 = area_barrida(T_MARTE * 0.5, T_MARTE * 0.6, T_MARTE, A_MARTE, E_SINT)
    assert abs(a1 / a2 - 1.0) < 1e-4, (a1, a2)                                # segunda ley
    total = area_barrida(0.0, T_MARTE, T_MARTE, A_MARTE, E_SINT, 20000)
    assert abs(total / (math.pi * A_MARTE**2 * math.sqrt(1 - E_SINT**2)) - 1.0) < 1e-4   # área de la elipse
    for t, a in PLANETAS.values():
        assert abs(t**2 / a**3 - 1.0) < 0.02, (t, a)                          # tercera ley


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Tercera ley con datos de la NASA (T² / a³, unidades de la Tierra):")
    for nombre, (t, a) in PLANETAS.items():
        print(f"  {nombre:9s} T={t:6.3f}  a={a:6.3f}  T²/a³ = {t**2 / a**3:.4f}")
    a, e = A_MARTE, E_SINT
    print(f"Órbita SINTÉTICA con a = {a} millones de km, T = {T_MARTE} d, e = {e}")
    print(f"  perihelio = {a * (1 - e):.1f}; afelio = {a * (1 + e):.1f} millones de km")
    a1 = area_barrida(0.0, T_MARTE / 10, T_MARTE, a, e)
    a2 = area_barrida(T_MARTE * 0.5, T_MARTE * 0.6, T_MARTE, a, e)
    print(f"  área barrida en T/10 desde el perihelio: {a1:.4e}; desde el afelio: {a2:.4e}; razón {a1 / a2:.6f}")
    dt = 0.01

    def rapidez(t: float) -> float:
        p0, p1 = posicion(t - dt, T_MARTE, a, e), posicion(t + dt, T_MARTE, a, e)
        return math.hypot(p1[0] - p0[0], p1[1] - p0[1]) / (2 * dt)

    print(f"  v_perihelio / v_afelio = {rapidez(dt) / rapidez(T_MARTE / 2):.4f} (teoría: {(1 + e) / (1 - e):.4f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
