#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C04: el promedio reduce el error aleatorio, no el sistematico.

Datos: SINTETICOS. Tiempo de llegada de un pulso (verdad 12.500000 ms) medido
con ruido blanco gaussiano sigma = 0.040 ms y un sesgo sistematico de retardo
de cable b = 0.015 ms (constante, desconocido para quien mide).
Modelo: x_i = t + b + e_i, e_i ~ N(0, sigma^2). La media de n lecturas tiene
desviacion sigma/sqrt(n) (GUM 4.2.3) y esperanza t + b.
Se repite el experimento R veces para estimar la dispersion de la media.
Supuestos: ruido independiente y estacionario; sesgo constante.
Validez: n >= 1. Tolerancia: la dispersion simulada de la media coincide con
sigma/sqrt(n) dentro de 8 % (R = 4000); la media de las medias coincide con
t + b dentro de 5 errores tipicos de esa media.
"""
from __future__ import annotations
import math
import platform
import random
import sys

T_VERDAD, SIGMA, SESGO = 12.500000, 0.040, 0.015   # ms
R = 4000


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(7)
    print("   n | sd de la media (sim) | sigma/sqrt(n) | media de medias - t (ms)")
    for n in (1, 4, 16, 64, 256):
        medias = []
        for _ in range(R):
            medias.append(sum(T_VERDAD + SESGO + rng.gauss(0, SIGMA) for _ in range(n)) / n)
        m = sum(medias) / R
        sd = math.sqrt(sum((v - m) ** 2 for v in medias) / (R - 1))
        teor = SIGMA / math.sqrt(n)
        assert abs(sd - teor) / teor < 0.08, (n, sd, teor)
        assert abs(m - (T_VERDAD + SESGO)) < 5 * teor / math.sqrt(R)
        print(f"{n:4d} | {sd:20.5f} | {teor:13.5f} | {m - T_VERDAD:10.5f}")
    # Con n grande el sesgo domina: el error total tiende a SESGO, no a 0
    err_total = math.hypot(SESGO, SIGMA / math.sqrt(256))
    print(f"n=256: error total esperado = {err_total:.5f} ms (sesgo {SESGO} ms)")
    assert err_total > SESGO
    # Una calibracion contra un patron con la verdad conocida estima el sesgo
    lecturas = [T_VERDAD + SESGO + rng.gauss(0, SIGMA) for _ in range(400)]
    b_est = sum(lecturas) / len(lecturas) - T_VERDAD
    print(f"sesgo estimado con patron (n=400) = {b_est:.5f} ms (verdadero {SESGO})")
    assert abs(b_est - SESGO) < 5 * SIGMA / math.sqrt(400)
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una prueba no se cumple")
        sys.exit(1)
