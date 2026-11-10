#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C14: exponentes de Lyapunov del mapa estandar por dos metodos y su relacion con K.

Datos: TODOS SINTETICOS (adimensionales). Mapa p' = p + K sin(theta), theta' = theta + p' (modulo 2 pi).
Para cada K se usan 8 condiciones iniciales aleatorias (semilla 73) y N = 40 000 iteraciones (tras 100 de transitorio).
Metodo A: vector tangente con la jacobiana [[1 + K cos(theta), 1], [K cos(theta), 1]] y renormalizacion en cada paso (Benettin).
Metodo B: dos trayectorias separadas 1e-9, renormalizando la separacion en cada paso.
Tambien: suma de los dos exponentes (mapa que conserva area) por ortonormalizacion de Gram-Schmidt de dos vectores tangentes.
Escala ILUSTRATIVA: si una iteracion equivale a un periodo de Io (1.769138 d, NASA/NSSDC, Jovian Satellite Fact Sheet, 2023-12-06),
el tiempo de Lyapunov 1/lambda se expresa en dias; no es la dinamica de Io.
Tolerancias: metodo A frente a B dentro del 5 % para K >= 2 ; suma de exponentes < 1e-10 ; K = 0.5 -> |lambda| < 0.02.
"""
from __future__ import annotations
import json, math, platform, random, sys

TWO_PI = 2 * math.pi
N = 40000
P_IO = 1.769138


def mapa(th, p, K):
    p = (p + K * math.sin(th)) % TWO_PI
    th = (th + p) % TWO_PI
    return th, p


def metodo_A(th, p, K, n=N):
    for _ in range(100):
        th, p = mapa(th, p, K)
    vx, vy = 1.0, 0.0
    s = 0.0
    # tambien segundo vector para Gram-Schmidt
    wx, wy = 0.0, 1.0
    s1 = s2 = 0.0
    for _ in range(n):
        c = K * math.cos(th)
        # jacobiana aplicada en el punto actual
        vx, vy = (1 + c) * vx + vy, c * vx + vy
        wx, wy = (1 + c) * wx + wy, c * wx + wy
        th, p = mapa(th, p, K)
        nv = math.hypot(vx, vy)
        s1 += math.log(nv)
        vx, vy = vx / nv, vy / nv
        # Gram-Schmidt
        dot = wx * vx + wy * vy
        wx, wy = wx - dot * vx, wy - dot * vy
        nw = math.hypot(wx, wy)
        s2 += math.log(nw)
        wx, wy = wx / nw, wy / nw
    return s1 / n, s2 / n


def metodo_B(th, p, K, n=N, d0=1e-9):
    for _ in range(100):
        th, p = mapa(th, p, K)
    th2, p2 = th + d0, p
    s = 0.0
    for _ in range(n):
        th, p = mapa(th, p, K)
        th2, p2 = mapa(th2, p2, K)
        dth = (th2 - th + math.pi) % TWO_PI - math.pi
        dp = (p2 - p + math.pi) % TWO_PI - math.pi
        d = math.hypot(dth, dp)
        s += math.log(d / d0)
        th2 = th + dth * d0 / d
        p2 = p + dp * d0 / d
    return s / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    rnd = random.Random(73)
    ics = [(rnd.uniform(0, TWO_PI), rnd.uniform(0, TWO_PI)) for _ in range(8)]
    print(f"{len(ics)} condiciones iniciales sinteticas (semilla 73), N = {N} iteraciones por trayectoria")
    print("    K    <lambda_A>  min..max (A)     <lambda_B>   dif A-B   lambda1+lambda2   ln(K/2)   t_Lyap [iter]   t_Lyap [d, escala Io]")
    sumamax = 0.0
    for K, tag in ((0.5, "k05"), (1.0, "k10"), (2.0, "k20"), (5.0, "k50"), (10.0, "k100")):
        A = [metodo_A(th, p, K) for th, p in ics]
        B = [metodo_B(th, p, K) for th, p in ics]
        lA = [a[0] for a in A]
        sumas = [a[0] + a[1] for a in A]
        mA, mB = sum(lA) / len(lA), sum(B) / len(B)
        sumamax = max(sumamax, max(abs(s) for s in sumas))
        dif = abs(mA - mB) / max(mA, 1e-9)
        asin = math.log(K / 2) if K > 2 else float("nan")
        tl = 1 / mA if mA > 0.02 else float("inf")
        print(f" {K:5.1f}   {mA:9.4f}   {min(lA):7.4f}..{max(lA):7.4f}   {mB:9.4f}   {dif:7.2%}   {max(abs(s) for s in sumas):12.1e}   {asin:8.4f}   {tl:12.2f}   {tl * P_IO:14.2f}")
        out[f"mA_{tag}"], out[f"mB_{tag}"], out[f"dif_{tag}"], out[f"min_{tag}"], out[f"max_{tag}"] = mA, mB, dif, min(lA), max(lA)
        out[f"tl_{tag}"] = tl
        out[f"tld_{tag}"] = tl * P_IO
        if K >= 2:
            assert dif < 0.05, (K, dif)
    assert sumamax < 1e-10
    assert out["mA_k05"] < 0.02
    print("Pruebas superadas.")
    out["sumamax"] = sumamax
    out["asin5"] = math.log(5 / 2)
    out["asin10"] = math.log(10 / 2)
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
