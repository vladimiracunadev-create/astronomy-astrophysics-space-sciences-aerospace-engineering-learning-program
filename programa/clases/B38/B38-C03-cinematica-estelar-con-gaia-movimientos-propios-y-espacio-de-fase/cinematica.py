#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C03: de movimientos propios, paralaje y velocidad radial a velocidades espaciales.

Datos: au = 149 597 870 700 m (definicion exacta de la UAI de 2012, NO consultada en esta sesion) y ano juliano = 365,25 d, de donde k = au/ano = 4,74047 km/s por (mas/ano x kpc) (calculado aqui; sin fuente consultada).
Las dispersiones de velocidad (35, 25, 20 km/s), el movimiento solar (11, 12, 7 km/s), los errores de paralaje y la semilla 20261109 son ILUSTRATIVOS (sinteticos).
No se usa ningun dato de Gaia; de Gaia DR3 solo se consulto el resumen del contenido (2026-11-09).
Modelo: coordenadas galacticas (l, b); v_t = k mu / varpi; U, V, W = proyeccion de (v_r, v_l, v_b) sobre los ejes galacticos; ida y vuelta exacta y propagacion de errores por Monte Carlo.
Supuestos: sin extincion ni correlaciones; paralaje con error gaussiano; distancia = 1/varpi. Validez: ilustrativa.
Tolerancia: ida y vuelta a 1e-9 relativo; dispersiones recuperadas con error de distancia del 1 % a menos del 5 %; el sesgo con 20 % de error debe ser visible.
"""
from __future__ import annotations
import math, platform, random, sys

AU = 149597870700.0
YR = 365.25 * 86400.0

def k_const():
    # 1 mas/ano a 1 kpc = 1e-3 arcsec/ano x 1000 pc = 1 au/ano -> en km/s
    return AU / YR / 1000.0

def base(l, b):
    cl, sl, cb, sb = math.cos(l), math.sin(l), math.cos(b), math.sin(b)
    er = (cb * cl, cb * sl, sb)
    el = (-sl, cl, 0.0)
    eb = (-sb * cl, -sb * sl, cb)
    return er, el, eb

def a_observables(u, v, w, l, b, dpc):
    er, el, eb = base(l, b)
    vr = u * er[0] + v * er[1] + w * er[2]
    vl = u * el[0] + v * el[1] + w * el[2]
    vb = u * eb[0] + v * eb[1] + w * eb[2]
    k = k_const()
    d_kpc = dpc / 1000.0
    mul = vl / (k * d_kpc)
    mub = vb / (k * d_kpc)
    return vr, mul, mub, 1000.0 / dpc

def a_velocidades(vr, mul, mub, varpi_mas, l, b):
    k = k_const()
    d_kpc = 1.0 / varpi_mas
    vl, vb = k * mul * d_kpc, k * mub * d_kpc
    er, el, eb = base(l, b)
    return tuple(vr * er[i] + vl * el[i] + vb * eb[i] for i in range(3))

def disp(xs):
    m = sum(xs) / len(xs)
    return m, math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    k = k_const()
    print(f"k = {k:.5f} km/s por (mas/ano x kpc)")
    assert abs(k - 4.74047) < 1e-5
    # ida y vuelta
    rng = random.Random(20261109)
    peor = 0.0
    for _ in range(1000):
        l, b = rng.uniform(0, 2 * math.pi), rng.uniform(-1.2, 1.2)
        d = rng.uniform(50, 2000)
        u, v, w = rng.gauss(0, 40), rng.gauss(0, 40), rng.gauss(0, 40)
        vr, mul, mub, vp = a_observables(u, v, w, l, b, d)
        u2, v2, w2 = a_velocidades(vr, mul, mub, vp, l, b)
        peor = max(peor, abs(u - u2), abs(v - v2), abs(w - w2))
    print(f"ida y vuelta: error maximo {peor:.2e} km/s")
    assert peor < 1e-9
    # elipsoide de velocidades
    sig = (35.0, 25.0, 20.0)
    sol = (11.0, 12.0, 7.0)
    N = 6000
    pob = []
    for _ in range(N):
        l, b = rng.uniform(0, 2 * math.pi), math.asin(rng.uniform(-1, 1))
        d = rng.uniform(100, 1000)
        pob.append((l, b, d, tuple(rng.gauss(0, s) for s in sig)))
    print(f"{'error de paralaje':>18} {'sigma_U':>8} {'sigma_V':>8} {'sigma_W':>8}")
    res = {}
    for frac in (0.0, 0.01, 0.2):
        us, vs, ws = [], [], []
        for l, b, d, (u, v, w) in pob:
            vr, mul, mub, vp = a_observables(u + sol[0], v + sol[1], w + sol[2], l, b, d)
            vp_obs = vp * (1 + rng.gauss(0, frac)) if frac > 0 else vp
            uu, vv, ww = a_velocidades(vr, mul, mub, vp_obs, l, b)
            us.append(uu - sol[0]); vs.append(vv - sol[1]); ws.append(ww - sol[2])
        res[frac] = (disp(us)[1], disp(vs)[1], disp(ws)[1])
        print(f"{frac * 100:17.0f} % {res[frac][0]:8.2f} {res[frac][1]:8.2f} {res[frac][2]:8.2f}")
    for i, s in enumerate(sig):
        assert abs(res[0.0][i] - s) / s < 0.05
        assert abs(res[0.01][i] - s) / s < 0.05
    assert all(res[0.2][i] > 1.02 * res[0.0][i] for i in range(3))
    # sesgo de 1/varpi con error relativo del 20 %
    m = sum(1 / (5.0 * (1 + rng.gauss(0, 0.2))) for _ in range(20000)) / 20000
    print(f"distancia media con paralaje de 5 mas y error de 20 %: {m * 1000:.1f} pc (verdadera 200,0 pc)")
    assert m > 0.2
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
