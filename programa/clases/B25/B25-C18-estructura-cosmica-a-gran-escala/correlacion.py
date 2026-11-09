#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C18: funcion de correlacion de dos puntos de catalogos sinteticos.

Datos: ninguno observado. Todo SINTETICO con semilla fija (random.Random): (a) catalogo de Poisson
(sin estructura) y (b) catalogo agrupado de Neyman-Scott: padres de Poisson, cada uno con un numero de
miembros de Poisson desplazados con una gaussiana de desviacion s por coordenada. Caja periodica de lado
L = 100 Mpc (unidades ILUSTRATIVAS), N ~ 2000 puntos.
Modelo: estimador natural xi(r) = DD(r)/RR(r) - 1, con RR esperado analiticamente en una caja periodica.
Solucion analitica del proceso de Neyman-Scott: xi(r) = exp(-r^2/(4 s^2)) / (n_p (4 pi s^2)^(3/2)),
con n_p la densidad de padres.
Supuestos: caja periodica, sin distorsiones en el espacio de corrimientos al rojo, sin mascara.
Validez: comprobacion del estimador; los catalogos reales requieren catalogo aleatorio y mascara.
Tolerancias: |xi| <= 4 sigma_Poisson para el catalogo aleatorio (sigma = 1/sqrt(DD esperado)) y 30 % para el
agrupado en los primeros contenedores (ruido de cuenta de pares, calculado de antemano).
"""
from __future__ import annotations
import math
import platform
import random
import sys

L = 100.0


def poisson(rng, lam):
    if lam > 50:
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    k, p, t = 0, 1.0, math.exp(-lam)
    while True:
        p *= rng.random()
        if p <= t:
            return k
        k += 1


def catalogo_poisson(n, rng):
    return [(rng.random() * L, rng.random() * L, rng.random() * L) for _ in range(n)]


def catalogo_agrupado(n_padres, miembros, s, rng):
    pts = []
    for _ in range(n_padres):
        c = (rng.random() * L, rng.random() * L, rng.random() * L)
        for _ in range(poisson(rng, miembros)):
            pts.append(tuple((c[k] + rng.gauss(0, s)) % L for k in range(3)))
    return pts


def pares(pts, bordes):
    cnt = [0] * (len(bordes) - 1)
    rmax2 = bordes[-1] ** 2
    n = len(pts)
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i + 1, n):
            dx = abs(xi - pts[j][0]); dx = min(dx, L - dx)
            if dx > bordes[-1]:
                continue
            dy = abs(yi - pts[j][1]); dy = min(dy, L - dy)
            if dy > bordes[-1]:
                continue
            dz = abs(zi - pts[j][2]); dz = min(dz, L - dz)
            d2 = dx * dx + dy * dy + dz * dz
            if d2 < rmax2:
                r = math.sqrt(d2)
                for b in range(len(cnt)):
                    if bordes[b] <= r < bordes[b + 1]:
                        cnt[b] += 1
                        break
    return cnt


def xi_estimado(pts, bordes):
    n = len(pts)
    dd = pares(pts, bordes)
    out = []
    for b, c in enumerate(dd):
        vol = 4 / 3 * math.pi * (bordes[b + 1] ** 3 - bordes[b] ** 3)
        rr = n * (n - 1) / 2 * vol / L ** 3
        out.append((c / rr - 1, rr, c))
    return out


def xi_teoria(r, n_padres, s):
    n_p = n_padres / L ** 3
    return math.exp(-r * r / (4 * s * s)) / (n_p * (4 * math.pi * s * s) ** 1.5)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    bordes = [0.0, 2.0, 4.0, 6.0, 10.0, 15.0]
    rng = random.Random(20261109)
    # Prueba 1: catalogo de Poisson, xi compatible con 0 dentro de 4 sigma
    pts_p = catalogo_poisson(2000, rng)
    for (xi, rr, c), a, b in zip(xi_estimado(pts_p, bordes), bordes, bordes[1:]):
        assert abs(xi) <= 4 / math.sqrt(rr), f"Poisson: xi={xi:.3f} en [{a},{b}]"
    # Prueba 2: catalogo agrupado frente a la solucion analitica
    n_padres, miembros, s = 100, 20.0, 3.0
    pts_c = catalogo_agrupado(n_padres, miembros, s, rng)
    est = xi_estimado(pts_c, bordes)
    print(f"Poisson: N = {len(pts_p)} ; agrupado: N = {len(pts_c)} (100 padres x ~20 miembros, s = 3 Mpc)")
    def teo_bin(a, b, n=400):
        num = den = 0.0
        for k in range(n):
            r = a + (b - a) * (k + 0.5) / n
            num += xi_teoria(r, n_padres, s) * r * r
            den += r * r
        return num / den

    print("contenedor (Mpc) | xi estimado | xi teorico (promedio en el contenedor) | pares")
    for (xi, rr, c), a, b in zip(est, bordes, bordes[1:]):
        print(f"  {a:4.1f}-{b:4.1f}        {xi:8.2f}      {teo_bin(a, b):8.2f}                          {c}")
    for (xi, rr, c), a, b in list(zip(est, bordes, bordes[1:]))[:2]:
        assert abs(xi / teo_bin(a, b) - 1) < 0.30, f"agrupado: xi={xi:.2f} frente a {teo_bin(a, b):.2f}"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
