#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C14: senal atmosferica en transito y numero de transitos necesarios.

Datos: k y la unidad de masa atomica de NIST (CODATA 2022, consultados 2026-11-09); radio
nominal solar 6,957e8 m de la IAU 2015 B3 (texto del PDF consultado el 2026-11-09). NO
CONSULTADOS (ILUSTRATIVOS): radio terrestre 6,371e6 m. Todo lo demas es SINTETICO: una
estrella enana M de 0,12 radios solares, un planeta de 1 radio terrestre, atmosfera de masa
molar 29 g/mol a 250 K con g = 9,8 m/s2, banda de 5 alturas de escala efectivas y ruido de
100 ppm por transito. No es la observacion de ningun sistema.
Modelo: profundidad delta = (Rp/Rs)^2; senal de la atmosfera ~ 2 Rp n H / Rs^2, con
H = k T / (mu m_u g). SNR tras N transitos = (senal/sigma) sqrt(N).
Supuestos: ruido blanco gaussiano, sin manchas ni variabilidad, estrella sin oscurecimiento
al limbo. Validez: orden de magnitud. Tolerancia: area ocultada por cuadratura frente a
(Rp/Rs)^2, 1e-4 relativo; escala 1/sqrt(N) de una simulacion con semilla 2024, 3 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

K = 1.380649e-23
MU_U = 1.66053906892e-27
R_SOL = 6.957e8
R_TIERRA = 6.371e6


def area_ocultada(rp_rs, n=200000):
    """Integra la altura de cuerda de la estrella dentro del disco del planeta (estrella de radio 1,
    planeta centrado en el disco): area = 2 int sqrt(rp^2 - x^2) dx = pi rp^2 por la regla de Simpson."""
    h = 2 * rp_rs / n
    f = lambda x: 2 * math.sqrt(max(rp_rs ** 2 - x * x, 0.0))
    s = f(-rp_rs) + f(rp_rs)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(-rp_rs + i * h)
    return s * h / 3 / math.pi  # fraccion del area estelar (pi * 1^2)


def altura_escala(T, mu, g):
    return K * T / (mu * MU_U * g)


def desviacion_media(sigma, N, intentos=4000, semilla=2024):
    rng = random.Random(semilla)
    medias = [sum(rng.gauss(0, sigma) for _ in range(N)) / N for _ in range(intentos)]
    m = sum(medias) / intentos
    return math.sqrt(sum((x - m) ** 2 for x in medias) / (intentos - 1))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rs, rp = 0.12 * R_SOL, R_TIERRA
    delta = (rp / rs) ** 2
    num = area_ocultada(rp / rs)
    print(f"Profundidad del tránsito = {delta * 1e6:.0f} ppm ; por cuadratura = {num * 1e6:.0f} ppm")
    assert abs(num / delta - 1) < 1e-4
    H = altura_escala(250.0, 29.0, 9.8)
    senal = 2 * rp * 5 * H / rs ** 2
    sigma = 100e-6
    print(f"H = {H / 1e3:.2f} km ; senal atmosferica (5 H) = {senal * 1e6:.1f} ppm")
    for objetivo in (3.0, 5.0):
        N = math.ceil((objetivo * sigma / senal) ** 2)
        print(f"SNR {objetivo:.0f} con ruido {sigma * 1e6:.0f} ppm/transito -> N = {N} transitos")
    d1, d25 = desviacion_media(sigma, 1), desviacion_media(sigma, 25)
    print(f"Desviacion de la media: N=1 -> {d1 * 1e6:.1f} ppm ; N=25 -> {d25 * 1e6:.1f} ppm ; cociente = {d1 / d25:.2f} (esperado 5)")
    assert abs(d1 / d25 - 5) / 5 < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
