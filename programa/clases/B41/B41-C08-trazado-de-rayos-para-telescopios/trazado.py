#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C08: trazado exacto de rayos meridionales por una lente biconvexa y comparacion con la optica paraxial.

Datos: sin constantes fisicas. Lente de vidrio n = 1,517 (tipico de libro, ILUSTRATIVO), R1 = 200 mm, R2 = -200 mm, espesor 10 mm; alturas de rayo de 1 a 40 mm.
Modelo: interseccion exacta de cada rayo con superficies esfericas y ley de Snell en forma vectorial. Para cada altura h se halla donde el rayo corta el
eje (distancia focal posterior exacta). Segunda via: matrices ABCD paraxiales (C = -1/f). Se ajusta el exponente de la aberracion esferica longitudinal.
Supuestos: rayos meridionales, superficies esfericas, aire, sin absorcion ni dispersion (una longitud de onda). Validez: geometrica; el limite h -> 0 es paraxial.
Tolerancia: h = 0,001 mm frente a matrices 1e-6 mm; exponente de la aberracion 2,0 +- 0,1.
"""
from __future__ import annotations
import math, platform, sys


def interseca(p, d, zv, R):
    """Interseccion del rayo con la esfera de vertice zv y radio R (centro en zv+R). Devuelve t."""
    zc = zv + R
    ox, oz = p[0], p[1] - zc
    b = ox * d[0] + oz * d[1]
    c = ox * ox + oz * oz - R * R
    disc = b * b - c
    s = math.sqrt(disc)
    ts = (-b - s, -b + s)
    # tomar la raiz cuyo punto esta mas cerca del vertice
    best = None
    for t in ts:
        z = p[1] + t * d[1]
        if t > 1e-12 and (best is None or abs(z - zv) < best[1]):
            best = (t, abs(z - zv))
    return best[0]


def refracta(d, N, n1, n2):
    cosi = -(d[0] * N[0] + d[1] * N[1])
    eta = n1 / n2
    k = 1 - eta * eta * (1 - cosi * cosi)
    f = eta * cosi - math.sqrt(k)
    return (eta * d[0] + f * N[0], eta * d[1] + f * N[1])


def traza(h, n, R1, R2, e):
    p = (h, -100.0)
    d = (0.0, 1.0)
    # superficie 1 en z = 0
    t = interseca(p, d, 0.0, R1)
    p = (p[0] + t * d[0], p[1] + t * d[1])
    c1 = (0.0, R1)
    N = ((p[0] - c1[0]) / R1, (p[1] - c1[1]) / R1)
    if N[0] * d[0] + N[1] * d[1] > 0:
        N = (-N[0], -N[1])
    d = refracta(d, N, 1.0, n)
    # superficie 2 en z = e
    t = interseca(p, d, e, R2)
    p = (p[0] + t * d[0], p[1] + t * d[1])
    c2 = (0.0, e + R2)
    N = ((p[0] - c2[0]) / abs(R2), (p[1] - c2[1]) / abs(R2))
    if N[0] * d[0] + N[1] * d[1] > 0:
        N = (-N[0], -N[1])
    d = refracta(d, N, n, 1.0)
    # corte con el eje
    tz = -p[0] / d[0]
    return p[1] + tz * d[1] - e       # distancia focal posterior (vertice 2 al corte)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n, R1, R2, e = 1.517, 200.0, -200.0, 10.0
    # paraxial por matrices
    def mul(a, b):
        return [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]], [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
    m = mul([[1, 0], [-(1.0 - n) / R2, 1]], mul([[1, e / n], [0, 1]], [[1, 0], [-(n - 1) / R1, 1]]))
    f_par = -1 / m[1][0]
    bfd_par = -m[0][0] / m[1][0]
    print(f"paraxial (matrices): f = {f_par:.4f} mm ; distancia focal posterior (vertice) = {bfd_par:.4f} mm")
    hs = (0.001, 5, 10, 20, 30, 40)
    print(f"{'h [mm]':>8} {'bfd exacta [mm]':>16} {'LSA [mm]':>10} {'LSA / h^2 [1e-3/mm]':>20}")
    lsa = {}
    for h in hs:
        b = traza(h, n, R1, R2, e)
        lsa[h] = b - bfd_par
        print(f"{h:8.3f} {b:16.5f} {lsa[h]:10.5f} {(lsa[h]/h**2*1e3 if h > 1 else float('nan')):20.5f}")
    assert abs(traza(0.001, n, R1, R2, e) - bfd_par) < 1e-4
    # exponente por ajuste log-log entre h = 10 y 40
    x = [math.log(h) for h in (10, 20, 30, 40)]
    y = [math.log(abs(lsa[h])) for h in (10, 20, 30, 40)]
    mx, my = sum(x) / 4, sum(y) / 4
    pend = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    print(f"exponente de la aberracion esferica longitudinal (ajuste log-log, h = 10 a 40 mm): {pend:.3f}")
    assert abs(pend - 2.0) < 0.2
    # rayos marginales: luz entre el 70,7 % de la apertura (zona de mejor compromiso)
    print(f"signo de la LSA: {'rayos marginales enfocan mas cerca' if lsa[40] < 0 else 'enfocan mas lejos'} (lente biconvexa)")
    assert lsa[40] < 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
