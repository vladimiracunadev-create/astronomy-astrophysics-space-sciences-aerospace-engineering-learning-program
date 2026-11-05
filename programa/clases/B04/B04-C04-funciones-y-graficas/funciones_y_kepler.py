#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C04: una función periodo(distancia) con datos planetarios.

Datos (PUBLICADOS; estimados): NASA NSSDC Planetary Fact Sheet - Metric
(actualizada 2025-03-18; consulta 2026-11-05), columnas «Distance from Sun»
(10^6 km) y «Orbital period» (días) de Venus, Tierra, Marte y Júpiter.
Modelo: P = k a^(3/2) (tercera ley de Kepler como función de potencia), con k
ajustada con el punto de la Tierra. Supuestos: órbitas casi circulares, a =
distancia media al Sol; Sol dominante. Validez: planetas del sistema solar
interior y Júpiter; no sirve para cuerpos con otro cuerpo central.
Tolerancia de las pruebas: 1e-9 (identidades algebraicas); 2 % en la comparación
con datos (los datos tienen 3-4 cifras).
"""
from __future__ import annotations
import math, platform, sys

DATOS = {  # a en 10^6 km, P en días: valores publicados
    "Venus": (108.2, 224.7),
    "Tierra": (149.6, 365.2),
    "Marte": (228.0, 687.0),
    "Júpiter": (778.5, 4331.0),
}


def potencia(a, k):
    return k * a ** 1.5


def inversa(P, k):
    return (P / k) ** (2.0 / 3.0)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a_t, P_t = DATOS["Tierra"]
    k = P_t / a_t ** 1.5
    # --- pruebas ---
    for a in (50.0, 149.6, 778.5, 5000.0):
        assert abs(inversa(potencia(a, k), k) - a) < 1e-9 * a          # f^-1(f(x)) = x
    assert abs(potencia(4 * 149.6, k) / P_t - 8.0) < 1e-12             # a x4 -> P x8
    assert all(potencia(a2, k) > potencia(a1, k) for a1, a2 in ((10, 20), (20, 300)))  # creciente
    assert abs(potencia(0.0, k)) == 0.0                                 # f(0)=0
    for nombre, (a, P) in DATOS.items():
        assert abs(potencia(a, k) / P - 1) < 0.02, nombre              # datos vs modelo
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (inversa, escala x4->x8, crecimiento, f(0)=0, datos dentro del 2 %)")
    print(f"\nk = P/a^1.5 (con la Tierra) = {k:.6e} días/(10^6 km)^1.5")
    print(f"{'Planeta':<9}{'a (10^6 km)':>12}{'P obs (d)':>11}{'P modelo (d)':>14}{'dif. %':>8}")
    for nombre, (a, P) in DATOS.items():
        Pm = potencia(a, k)
        print(f"{nombre:<9}{a:12.1f}{P:11.1f}{Pm:14.1f}{(Pm/P-1)*100:8.2f}")
    print("\nCociente P/a^1.5 por planeta (constante si la ley vale):")
    for nombre, (a, P) in DATOS.items():
        print(f"  {nombre:<8}{P / a**1.5:.5f}")
    # gráfica de texto de P(a) (accesible)
    print("\nGráfica de texto: P en miles de días frente a a (10^6 km)")
    for a in range(100, 801, 100):
        barra = "#" * round(potencia(a, k) / 100)
        print(f"a={a:4d} | {barra} {potencia(a, k):7.0f} d")
    # log-log: pendiente
    (a1, P1), (a2, P2) = DATOS["Venus"], DATOS["Júpiter"]
    pend = (math.log10(P2) - math.log10(P1)) / (math.log10(a2) - math.log10(a1))
    print(f"\nPendiente log-log entre Venus y Júpiter = {pend:.4f} (esperada 1,5)")


if __name__ == "__main__":
    main()
