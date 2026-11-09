#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C14: condiciones de Rankine-Hugoniot y espectro de la aceleracion difusiva en choques (Monte Carlo).

Datos: ninguna constante fisica. El indice adiabatico (5/3), los numeros de Mach (1.5, 2, 3, 5, 10, 20), la razon u1/c = 0.01 y el numero de particulas (40 000) son ILUSTRATIVOS
(sinteticos).
Modelo: (1) choque plano de gas ideal: razon de compresion r = (g + 1) M^2/((g - 1) M^2 + 2) y salto de presion y de velocidad, con comprobacion de las tres leyes de conservacion
(masa, momento y energia) aguas arriba y abajo; (2) aceleracion difusiva de particulas de prueba (Bell): en cada ciclo la particula gana una fraccion xi = (4/3) beta (r - 1)/r de energia
(beta = u1/c) y escapa con probabilidad P = 4 beta/r; se simula la energia final de cada particula, se ajusta la pendiente de la distribucion integral N(>E) en escala logaritmica y se
compara con s = 3/(r - 1) (indice diferencial (r + 2)/(r - 1)).
Supuestos: choque plano y fuerte o debil estacionario, particulas relativistas sin retroceso del choque, difusion isotropa. Validez: orientativa.
Tolerancia: leyes de conservacion a 1e-12; pendiente simulada dentro del 5 % de s = 3/(r - 1) para r > 2.
"""
from __future__ import annotations
import math
import platform
import random
import sys

G = 5.0 / 3.0


def rh(m, g=G):
    r = (g + 1) * m * m / ((g - 1) * m * m + 2)
    p_rel = (2 * g * m * m - (g - 1)) / (g + 1)
    return r, p_rel


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'M':>5} {'r = rho2/rho1':>14} {'p2/p1':>8} {'u2/u1':>8} {'residuo masa':>13} {'residuo momento':>16} {'residuo energia':>16}")
    for m in (1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0):
        r, pr = rh(m)
        rho1, p1 = 1.0, 1.0
        c1 = math.sqrt(G * p1 / rho1)
        u1 = m * c1
        u2 = u1 / r
        rho2, p2 = r * rho1, pr * p1
        masa = rho1 * u1 - rho2 * u2
        mom = rho1 * u1 ** 2 + p1 - (rho2 * u2 ** 2 + p2)
        en = u1 * (0.5 * rho1 * u1 ** 2 + G / (G - 1) * p1) - u2 * (0.5 * rho2 * u2 ** 2 + G / (G - 1) * p2)
        esc = max(rho1 * u1, rho1 * u1 ** 2, abs(u1 * 0.5 * rho1 * u1 ** 2)) + 1e-300
        assert abs(masa) < 1e-12 * esc and abs(mom) < 1e-12 * esc * u1 + 1e-12 and abs(en) < 1e-12 * (esc * u1 ** 2 + 1), f"conservacion M={m}"
        print(f"{m:5.1f} {r:14.4f} {pr:8.3f} {1 / r:8.4f} {masa:13.1e} {mom:16.1e} {en:16.1e}")
    assert abs(rh(1.0)[0] - 1) < 1e-12 and abs(rh(1e6)[0] - 4) < 1e-6
    # aceleracion difusiva
    beta, n = 0.01, 40000
    rng = random.Random(20261109)
    print(f"{'M':>5} {'r':>7} {'xi':>9} {'P_esc':>8} {'s teorico 3/(r-1)':>18} {'s simulado':>11} {'dif':>7}")
    for m in (2.0, 3.0, 20.0):
        r, _ = rh(m)
        xi = 4.0 / 3.0 * beta * (r - 1) / r
        pesc = 4 * beta / r
        ciclos = []
        for _ in range(n):
            k = 0
            while rng.random() > pesc:
                k += 1
            ciclos.append(k)
        # distribucion integral en escala logaritmica: N(>E)/N con E = (1 + xi)^k
        kmax = max(ciclos)
        pts = []
        paso = max(1, int(1.0 / pesc / 8))
        for k in range(paso, int(4.0 / pesc), paso):
            frac = sum(1 for c in ciclos if c > k) / n
            if frac > 5 / n:
                pts.append((k * math.log(1 + xi), math.log(frac)))
        xs_, ys_ = zip(*pts)
        mx, my = sum(xs_) / len(xs_), sum(ys_) / len(ys_)
        pend = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x in xs_)
        s_sim = -pend
        s_teo = 3 / (r - 1)
        print(f"{m:5.1f} {r:7.3f} {xi:9.5f} {pesc:8.5f} {s_teo:18.3f} {s_sim:11.3f} {abs(s_sim / s_teo - 1):7.2%}")
        assert abs(s_sim / s_teo - 1) < 0.05, f"pendiente M={m}"
    print("indice diferencial (r + 2)/(r - 1): " + ", ".join(f"r = {rh(m)[0]:.3f} -> {(rh(m)[0] + 2) / (rh(m)[0] - 1):.3f}" for m in (2.0, 3.0, 20.0)))
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
