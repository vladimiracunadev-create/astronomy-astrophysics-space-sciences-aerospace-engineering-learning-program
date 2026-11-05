#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C05: bucles y una simulación sencilla (caída libre, método de Euler).

Datos PUBLICADOS: gravedad en la superficie de la Tierra (9,8 m/s²) y de Marte
(3,7 m/s²), NASA NSSDC, Planetary Fact Sheet (tabla comparativa, act. 18-mar-2025),
consultada el 2026-11-05. Los valores están redondeados a dos cifras.
Modelo: caída desde el reposo sin atmósfera, con gravedad CONSTANTE g. Se avanza en
pasos de tiempo dt con el método de Euler explícito:
    x_{n+1} = x_n + v_n * dt ;  v_{n+1} = v_n + g * dt
Referencia analítica: x(t) = g t² / 2. Euler da exactamente x = (g t² / 2)(1 − dt/t).
Supuestos: sin rozamiento, g constante (solo vale para alturas pequeñas frente al radio).
Dominio de validez: caídas cortas; resultado SIMULADO (numérico), no observado.
Tolerancia: la identidad de Euler se cumple a 1e-9 en valor relativo.
"""

from __future__ import annotations

import math
import sys

G_TIERRA = 9.8   # m/s², publicado
G_MARTE = 3.7    # m/s², publicado


def caida_euler(g: float, t_total: float, dt: float) -> float:
    """Devuelve la distancia caída (m) tras t_total s, con pasos dt (Euler explícito)."""
    n_pasos = round(t_total / dt)
    x = 0.0
    v = 0.0
    for _ in range(n_pasos):
        x = x + v * dt
        v = v + g * dt
    return x


def tiempo_hasta(g: float, altura: float, dt: float) -> float:
    """Devuelve el primer instante (s) en que la distancia caída alcanza la altura."""
    x = 0.0
    v = 0.0
    t = 0.0
    while x < altura:
        x = x + v * dt
        v = v + g * dt
        t = t + dt
    return t


def exacta(g: float, t: float) -> float:
    """Distancia caída exacta con g constante: g t² / 2."""
    return 0.5 * g * t ** 2


def pruebas() -> None:
    # 1) la identidad algebraica de Euler para caída libre
    for dt in (0.1, 0.01):
        esperado = exacta(G_TIERRA, 10.0) * (1.0 - dt / 10.0)
        assert math.isclose(caida_euler(G_TIERRA, 10.0, dt), esperado, rel_tol=1e-9)
    # 2) el error relativo se reduce a la décima parte al reducir dt a la décima parte
    e1 = 1 - caida_euler(G_TIERRA, 10.0, 0.01) / exacta(G_TIERRA, 10.0)
    e2 = 1 - caida_euler(G_TIERRA, 10.0, 0.001) / exacta(G_TIERRA, 10.0)
    assert math.isclose(e1 / e2, 10.0, rel_tol=1e-6)
    # 3) casos borde: tiempo cero y altura cero
    assert caida_euler(G_TIERRA, 0.0, 0.01) == 0.0
    assert tiempo_hasta(G_TIERRA, 0.0, 0.01) == 0.0
    # 4) el tiempo hasta 100 m es cercano al analítico sqrt(2h/g) (tolerancia 2 dt)
    dt = 0.001
    assert abs(tiempo_hasta(G_TIERRA, 100.0, dt) - math.sqrt(2 * 100.0 / G_TIERRA)) < 5 * dt


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Caída en 10 s (Tierra, g = 9.8 m/s²):")
    print(f"  exacta: {exacta(G_TIERRA, 10.0):.3f} m")
    for dt in (0.1, 0.01, 0.001):
        x = caida_euler(G_TIERRA, 10.0, dt)
        print(f"  dt = {dt:<6} Euler: {x:>9.3f} m   error relativo: {1 - x / exacta(G_TIERRA, 10.0):.2e}")
    print("Tiempo para caer 100 m (dt = 0.001 s):")
    print(f"  Tierra: {tiempo_hasta(G_TIERRA, 100.0, 0.001):.3f} s | Marte: {tiempo_hasta(G_MARTE, 100.0, 0.001):.3f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
