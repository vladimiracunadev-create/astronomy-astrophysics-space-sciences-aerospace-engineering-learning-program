#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C03: funcion de correlacion de dos puntos con los estimadores natural y de Landy-Szalay.

Datos: SINTETICOS. Un proceso de Thomas (cumulos gaussianos) en una caja periodica de L = 100 Mpc/h: 100 centros uniformes, cada uno con un numero de miembros
de Poisson (media 10) desplazados con sigma = 2 Mpc/h por eje. No es un catalogo de galaxias ni se usa ninguna fuente externa; semilla 20261109.
Modelo: 1 + xi(r) = RR-normalizado; analitico para el proceso de Thomas en 3D: xi(r) = exp(-r^2/(4 sigma^2)) / [(4 pi sigma^2)^(3/2) n_c], con n_c la densidad de centros.
Estimadores: natural DD/RR - 1 con RR analitico (caja periodica) y Landy-Szalay (DD - 2DR + RR)/RR con un catalogo aleatorio de 4000 puntos.
Supuestos: isotropia, caja periodica sin geometria de encuesta, sin distorsiones de redshift. Validez: r << L/2.
Tolerancia: el valor medio de 8 maquetas frente al analitico, dentro de 3 errores estandar de la media (y 15 % en los bins de r < 4).
"""
from __future__ import annotations
import math, platform, random

L = 100.0
NC = 100
MEDIA = 10
SIG = 2.0
RB = [0.5 + 1.0 * i for i in range(13)]  # bordes 0.5 .. 12.5
NB = len(RB) - 1


def poisson(rng, lam):
    lim, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= lim:
            return k
        k += 1


def mock(rng):
    pts = []
    for _ in range(NC):
        c = (rng.random() * L, rng.random() * L, rng.random() * L)
        for _ in range(poisson(rng, MEDIA)):
            pts.append(tuple((c[j] + rng.gauss(0, SIG)) % L for j in range(3)))
    return pts


def conteo(A, B, mismo):
    """Pares (A,B) por bin de r en caja periodica; si mismo, cuenta cada par una vez."""
    cnt = [0] * NB
    r0, r1 = RB[0] ** 2, RB[-1] ** 2
    inv = 1.0 / (RB[1] - RB[0])
    h = L / 2
    for i, (x, y, z) in enumerate(A):
        for (u, v, w) in (A[i + 1:] if mismo else B):
            dx = abs(x - u)
            if dx > h:
                dx = L - dx
            dy = abs(y - v)
            if dy > h:
                dy = L - dy
            dz = abs(z - w)
            if dz > h:
                dz = L - dz
            s = dx * dx + dy * dy + dz * dz
            if r0 <= s < r1:
                cnt[int((math.sqrt(s) - RB[0]) * inv)] += 1
    return cnt


def vol(i):
    return 4 * math.pi / 3 * (RB[i + 1] ** 3 - RB[i] ** 3)


def xi_teo(i):
    # promedio ponderado por volumen del bin (Simpson en r con peso r^2)
    n = 200
    a, b = RB[i], RB[i + 1]
    nc = NC / L ** 3
    f = lambda r: math.exp(-r * r / (4 * SIG ** 2)) / ((4 * math.pi * SIG ** 2) ** 1.5 * nc) * r * r
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if k % 2 else 2) * f(a + k * h) for k in range(1, n))
    return s * h / 3 / ((b ** 3 - a ** 3) / 3)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    xis = []
    ns = []
    dd0 = None
    for m in range(8):
        P = mock(rng)
        n = len(P)
        ns.append(n)
        dd = conteo(P, P, True)
        if m == 0:
            dd0, P0 = dd, P
        rr = [0.5 * n * (n - 1) * vol(i) / L ** 3 for i in range(NB)]
        xis.append([dd[i] / rr[i] - 1 for i in range(NB)])
    mean = [sum(x[i] for x in xis) / 8 for i in range(NB)]
    err = [math.sqrt(sum((x[i] - mean[i]) ** 2 for x in xis) / 7 / 8) for i in range(NB)]
    # Landy-Szalay con aleatorios en la primera maqueta
    R = [(rng.random() * L, rng.random() * L, rng.random() * L) for _ in range(4000)]
    n, nr = len(P0), len(R)
    dr = conteo(P0, R, False)
    rrc = conteo(R, R, True)
    ls = []
    for i in range(NB):
        DD = dd0[i] / (n * (n - 1) / 2)
        DR = dr[i] / (n * nr)
        RRn = rrc[i] / (nr * (nr - 1) / 2)
        ls.append((DD - 2 * DR + RRn) / RRn)
    nat0 = xis[0]
    print(f"maquetas: N = {ns} ; media = {sum(ns) / 8:.1f}")
    print(f"{'r [Mpc/h]':>10} {'xi teorico':>11} {'media 8 maq.':>13} {'error media':>12} {'natural(1)':>11} {'LS(1)':>9} {'pull':>6}")
    pulls = []
    for i in range(NB):
        t = xi_teo(i)
        pull = (mean[i] - t) / err[i] if err[i] > 0 else 0.0
        pulls.append(pull)
        print(f"{(RB[i] + RB[i + 1]) / 2:10.1f} {t:11.4f} {mean[i]:13.4f} {err[i]:12.4f} {nat0[i]:11.4f} {ls[i]:9.4f} {pull:6.2f}")
    chi2 = sum(p * p for p in pulls)
    print(f"chi2 de la media frente al analitico = {chi2:.1f} con {NB} bins")
    dif = max(abs(ls[i] - nat0[i]) for i in range(NB))
    print(f"maxima diferencia |LS - natural| en la maqueta 1 = {dif:.3f}")
    # correlacion integrada: Int xi dV en r<12.5 frente al teorico
    teo_int = sum(xi_teo(i) * vol(i) for i in range(NB))
    est_int = sum(mean[i] * vol(i) for i in range(NB))
    print(f"integral de xi dV: estimada = {est_int:.1f} ; teorica = {teo_int:.1f} (Mpc/h)^3")
    assert all(abs(p) < 3.5 for p in pulls)
    for i in range(4):
        assert abs(mean[i] - xi_teo(i)) < 0.15 * xi_teo(i) + 3 * err[i]
    assert dif < 0.5 * max(1.0, max(ls))
    assert abs(est_int - teo_int) / teo_int < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
