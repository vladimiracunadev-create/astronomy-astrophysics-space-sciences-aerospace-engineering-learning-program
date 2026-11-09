#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C19: edad de un cumulo SINTETICO por su punto de desvio.

Datos: ninguno observado. Cumulo de 3000 estrellas SINTETICAS con funcion inicial de masa
dN/dM ~ M^(-2.3) entre 0.1 y 30 Msol (pendiente ilustrativa) y edad verdadera 0.5 Gyr.
Vida en secuencia principal: t(M) = 7.372 Gyr * f(M) * M / L(M) con la relacion masa-luminosidad
ILUSTRATIVA de B24-C15 (L = 0.23 M^2.3, M^4, 1.4 M^3.5; f = 1 para M < 0.35, 0.1 si no).
Modelo: las estrellas con t(M) < edad ya salieron de la secuencia principal; el punto de desvio
M_TO se obtiene invirtiendo t(M) = edad. La edad estimada se obtiene de la estrella mas
masiva que sigue en la secuencia principal.
Supuestos: todas las estrellas nacen a la vez y con la misma composicion; sin binarias ni
rotacion; vida con luminosidad constante. Validez: ilustrativa.
Tolerancia: 1e-9 en la inversion t(M); 3 sigma en la fraccion de supervivientes; 15 % en la edad.
"""
from __future__ import annotations
import math
import platform
import random
import sys

T_SOL = 7.372
ALFA, M_MIN, M_MAX = 2.3, 0.1, 30.0


def lum(m):
    if m < 0.43:
        return 0.23 * m ** 2.3
    if m < 2.0:
        return m ** 4
    return 1.4 * m ** 3.5


def t_ms(m):
    f = 1.0 if m < 0.35 else 0.1
    return T_SOL * (f / 0.1) * m / lum(m)    # T_SOL ya incluye f = 0.1 para el Sol; f = 1 multiplica por 10


def m_desvio(edad, lo=0.35, hi=M_MAX):
    """Masa cuya vida iguala la edad (t decrece con M para M >= 0.35)."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_ms(mid) > edad:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def muestrear(n, rng):
    a = 1 - ALFA
    out = []
    for _ in range(n):
        u = rng.random()
        out.append((M_MIN ** a + u * (M_MAX ** a - M_MIN ** a)) ** (1 / a))
    return out


def fraccion_teorica(m_corte):
    a = 1 - ALFA
    return (m_corte ** a - M_MIN ** a) / (M_MAX ** a - M_MIN ** a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    edad = 0.5
    m_to = m_desvio(edad)
    assert abs(t_ms(m_to) / edad - 1) < 1e-9, "inversion t(M)"
    rng = random.Random(19)
    masas = muestrear(3000, rng)
    superv = [m for m in masas if t_ms(m) >= edad]
    n_sup, p = len(superv), fraccion_teorica(m_to)
    sigma = math.sqrt(3000 * p * (1 - p))
    assert abs(n_sup - 3000 * p) < 3 * sigma, "fraccion de supervivientes fuera de 3 sigma"
    m_max_sup = max(m for m in superv if m >= 0.35)
    edad_est = t_ms(m_max_sup)
    assert abs(edad_est / edad - 1) < 0.15, "edad estimada fuera del 15 %"
    print(f"edad verdadera = {edad} Gyr -> M_desvio = {m_to:.3f} Msol")
    print(f"supervivientes = {n_sup} de 3000 (esperado {3000 * p:.0f} +/- {sigma:.0f})")
    print(f"estrella mas masiva en la secuencia principal = {m_max_sup:.3f} Msol -> edad estimada = {edad_est:.3f} Gyr "
          f"(error {100 * (edad_est / edad - 1):+.1f} %)")
    for e in (0.01, 0.1, 1.0, 10.0):
        print(f"edad {e:6.2f} Gyr -> M_desvio = {m_desvio(e):.3f} Msol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
