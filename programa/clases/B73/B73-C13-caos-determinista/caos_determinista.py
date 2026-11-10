#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C13: caos determinista en el mapa estandar de Chirikov (regimen regular K = 0.5 y caotico K = 5).

Datos: TODOS SINTETICOS (adimensionales). Mapa: p' = p + K sin(theta) ; theta' = theta + p' (ambos modulo 2 pi).
Condiciones iniciales sinteticas: (theta0, p0) = (1.0, 0.5) y una copia desplazada en 1e-10 en theta.
Verificaciones: (a) separacion de dos trayectorias vecinas frente al numero de iteraciones; (b) pendiente de ln(separacion) frente a n
(candidata a exponente de Lyapunov; se calcula con rigor en B73-C14) y horizonte de prediccion n_h = ln(delta_f/delta_0)/pendiente;
(c) reversibilidad: n iteraciones adelante y n atras con el mapa inverso exacto, error de ida y vuelta en doble precision;
(d) segunda via: la misma trayectoria con aritmetica decimal de 60 digitos; iteracion en que la de doble precision se separa mas de 1e-3.
Tolerancias: pendiente del regimen regular (n 10-60) < 0.1 ; caotico > 0.5 ; el horizonte medido dentro del 30 % del estimado por la pendiente.
"""
from __future__ import annotations
import json, math, platform, sys
from decimal import Decimal, getcontext

TWO_PI = 2 * math.pi
getcontext().prec = 60
PI_D = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
TWO_PI_D = 2 * PI_D


def mapa(th, p, K):
    p = (p + K * math.sin(th)) % TWO_PI
    th = (th + p) % TWO_PI
    return th, p


def inverso(th, p, K):
    th = (th - p) % TWO_PI
    p = (p - K * math.sin(th)) % TWO_PI
    return th, p


def sin_d(x):
    x = x % TWO_PI_D
    if x > PI_D:
        x -= TWO_PI_D
    t, s, n = x, x, 1
    x2 = x * x
    while abs(t) > Decimal(10) ** -62:
        t = -t * x2 / ((2 * n) * (2 * n + 1))
        s += t
        n += 1
    return s


def mapa_d(th, p, K):
    p = (p + Decimal(str(K)) * sin_d(th)) % TWO_PI_D
    th = (th + p) % TWO_PI_D
    return th, p


def dist(a, b):
    d = [abs(a[0] - b[0]), abs(a[1] - b[1])]
    d = [min(x, TWO_PI - x) for x in d]
    return math.hypot(*d)


def correr(K, n=60, delta0=1e-10):
    a, b = (1.0, 0.5), (1.0 + delta0, 0.5)
    ds = [dist(a, b)]
    for _ in range(n):
        a, b = mapa(*a, K), mapa(*b, K)
        ds.append(dist(a, b))
    return ds


def pendiente(ds, n1, n2):
    xs = list(range(n1, n2 + 1))
    ys = [math.log(ds[i]) for i in xs]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar) ; decimal de {getcontext().prec} digitos")
    out = {"python": platform.python_version()}
    print("(a)-(b) Separacion de dos trayectorias que parten a 1e-10 en theta (datos sinteticos):")
    print("   n      d(K=0.5)      d(K=5)")
    d_reg, d_cao = correr(0.5), correr(5.0)
    for i in (0, 5, 10, 15, 20, 25, 30, 40, 60):
        print(f" {i:3d}   {d_reg[i]:.3e}   {d_cao[i]:.3e}")
    s_reg = pendiente(d_reg, 10, 60)
    s_cao = pendiente(d_cao, 0, 20)
    print(f"Pendiente de ln(d) frente a n: regular (n 10-60) = {s_reg:.3f} ; caotico (n 0-20) = {s_cao:.3f}")
    n_h = math.log(1e-2 / 1e-10) / s_cao
    n_med = next(i for i, d in enumerate(d_cao) if d >= 1e-2)
    print(f"Horizonte para pasar de 1e-10 a 1e-2 (caotico): estimado = {n_h:.1f} iteraciones ; medido = {n_med}")
    out.update(s_reg=s_reg, s_cao=s_cao, n_h=n_h, n_med=n_med, d40_reg=d_reg[40], d20_cao=d_cao[20], d30_cao=d_cao[30])
    # (c) reversibilidad
    print("(c) Reversibilidad: n iteraciones adelante y n atras (mapa inverso exacto):")
    for K in (0.5, 5.0):
        th, p = 1.0, 0.5
        for _ in range(60):
            th, p = mapa(th, p, K)
        for _ in range(60):
            th, p = inverso(th, p, K)
        e = dist((th, p), (1.0, 0.5))
        print(f"   K = {K}: error de ida y vuelta tras 60 pasos = {e:.2e}")
        out["rev_reg" if K == 0.5 else "rev_cao"] = e
    # (d) doble precision frente a 60 digitos
    print("(d) Doble precision frente a aritmetica de 60 digitos (misma condicion inicial):")
    for K in (0.5, 5.0):
        th, p = 1.0, 0.5
        thd, pd = Decimal(1), Decimal("0.5")
        n_sep = None
        for i in range(1, 201):
            th, p = mapa(th, p, K)
            thd, pd = mapa_d(thd, pd, K)
            dd = dist((th, p), (float(thd), float(pd)))
            if n_sep is None and dd > 1e-3:
                n_sep = i
        print(f"   K = {K}: separacion mayor que 1e-3 en la iteracion {n_sep if n_sep else '> 200'} ; separacion a n = 200: {dd:.2e}")
        out["nsep_reg" if K == 0.5 else "nsep_cao"] = n_sep if n_sep else 0
        out["d200_reg" if K == 0.5 else "d200_cao"] = dd
    assert abs(s_reg) < 0.1 and s_cao > 0.5
    assert abs(n_med - n_h) / n_h < 0.3
    assert out["nsep_cao"] and out["nsep_cao"] < 100
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
