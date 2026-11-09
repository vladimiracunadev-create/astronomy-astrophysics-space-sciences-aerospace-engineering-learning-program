#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C12: cuadro maestro de bias y propagacion de ruido.

Datos: ninguna constante fisica. Nivel de bias (800 ADU), patron de columnas (sigma 2 ADU), ruido de lectura (4 ADU), cuadros de 48 x 48 pixeles y 25 cuadros por maestro
son ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: cuadro = bias + patron fijo por columna + ruido gaussiano; maestro = media (y mediana) de N cuadros; ruido del maestro = RN/sqrt(N) (media), ~1,2533 RN/sqrt(N) (mediana);
al restar el maestro de un cuadro nuevo el ruido es RN sqrt(1 + 1/N). Semilla 20261109.
Supuestos: patron fijo estable, ruido independiente entre cuadros. Validez: ilustrativa.
Tolerancia: ruido del maestro y del resultado dentro de 4 % del analitico.
"""
from __future__ import annotations
import math, platform, random, sys

W = 48
N = W * W

def std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    b0, rn, nf = 800.0, 4.0, 25
    col = [rng.gauss(0, 2.0) for _ in range(W)]
    base = [b0 + col[i % W] for i in range(N)]
    cuadros = [[base[i] + rng.gauss(0, rn) for i in range(N)] for _ in range(nf)]
    media = [sum(c[i] for c in cuadros) / nf for i in range(N)]
    def med(v):
        v = sorted(v); n = len(v)
        return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])
    mediana = [med([c[i] for c in cuadros]) for i in range(N)]
    r_media = [m - b for m, b in zip(media, base)]
    r_med = [m - b for m, b in zip(mediana, base)]
    s_media, s_med = std(r_media), std(r_med)
    print(f"ruido del maestro (media):   {s_media:.4f} ADU ; analitico {rn/math.sqrt(nf):.4f}")
    print(f"ruido del maestro (mediana): {s_med:.4f} ADU ; analitico {rn*math.sqrt(math.pi/2)/math.sqrt(nf):.4f}")
    assert abs(s_media / (rn / math.sqrt(nf)) - 1) < 0.04
    assert abs(s_med / (rn * math.sqrt(math.pi / 2) / math.sqrt(nf)) - 1) < 0.04
    nuevo = [base[i] + rng.gauss(0, rn) for i in range(N)]
    res = [a - m for a, m in zip(nuevo, media)]
    esp = rn * math.sqrt(1 + 1 / nf)
    print(f"cuadro nuevo - maestro: std {std(res):.4f} ADU ; analitico {esp:.4f} ; media {sum(res)/N:+.4f}")
    assert abs(std(res) / esp - 1) < 0.04
    sin = [a - b0 for a in nuevo]
    print(f"cuadro nuevo - nivel medio (sin maestro): std {std(sin):.4f} ADU (incluye el patron de columnas)")
    assert std(sin) > std(res)
    print(f"{'N cuadros':>10} {'ruido maestro [ADU]':>20}")
    for n in (1, 5, 25, 100):
        print(f"{n:10d} {rn/math.sqrt(n):20.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
