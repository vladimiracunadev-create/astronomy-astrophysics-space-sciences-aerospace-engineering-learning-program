#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C05: orbitas periodicas de Lyapunov alrededor de L1 (Tierra-Luna) por correccion diferencial (disparo).

Datos consultados (2026-11-10): GM de la Luna 4902.800 km3/s2, semieje 384 400 km y periodo 27.322 d (JPL SSD).
GM de la Tierra ~ 398 600 km3/s2 (aproximado, deducido de la masa de la tabla de planetas del JPL).
SINTETICO: las amplitudes Ax propuestas (en unidades adimensionales) son parametros de ejemplo; no son ninguna orbita real de mision.
Modelo: CR3BP plano, marco sinodico adimensional (distancia 384 400 km, tiempo 4.348 d). Una orbita simetrica cruza y = 0 con vx = 0.
Metodo: x0 = x_L1 - Ax, y0 = 0, vx0 = 0; se busca vy0 tal que en el siguiente cruce de y = 0 se cumple vx = 0 (biseccion);
el periodo es el doble del tiempo de cruce. Integrador RK4 con dt = 1e-3 y refinamiento del cruce por biseccion del paso.
Segunda via: cierre tras un periodo completo integrado de nuevo, conservacion de Jacobi y periodo lineal 2 pi / b del laboratorio B73-C04.
Tolerancias: cierre < 1e-6 (adimensional); deriva de Jacobi < 1e-8; periodo para Ax = 1e-3 dentro del 0.5 % del lineal.
"""
from __future__ import annotations
import json, math, platform, sys

GM_L, GM_T, A_KM, P_L = 4902.800, 398600.0, 384400.0, 27.322
MU = GM_L / (GM_T + GM_L)
U_D = P_L / (2 * math.pi)


def f(s):
    x, y, vx, vy = s
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    return [vx, vy, 2 * vy + x - (1 - MU) * (x + MU) / r1**3 - MU * (x - 1 + MU) / r2**3,
            -2 * vx + y - (1 - MU) * y / r1**3 - MU * y / r2**3]


def paso(s, h):
    k1 = f(s)
    k2 = f([a + 0.5 * h * b for a, b in zip(s, k1)])
    k3 = f([a + 0.5 * h * b for a, b in zip(s, k2)])
    k4 = f([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def jacobi(s):
    x, y, vx, vy = s
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    return x * x + y * y + 2 * (1 - MU) / r1 + 2 * MU / r2 - vx * vx - vy * vy


def cruce(s0, dt=1e-3, tmax=6.0):
    """Primer cruce de y = 0 despues de salir de y = 0; devuelve (t, estado)."""
    s, t = list(s0), 0.0
    prev_y = s[1]
    # salir del plano
    while abs(s[1]) < 1e-7 and t < 0.05:
        s = paso(s, dt)
        t += dt
    sgn = 1 if s[1] > 0 else -1
    while t < tmax:
        sn = paso(s, dt)
        if sn[1] * sgn <= 0:
            lo, hi = 0.0, dt
            for _ in range(60):
                m = 0.5 * (lo + hi)
                if paso(s, m)[1] * sgn > 0:
                    lo = m
                else:
                    hi = m
            return t + lo, paso(s, lo)
        s, t = sn, t + dt
    raise RuntimeError("sin cruce")


def L1x():
    g = lambda x: x - (1 - MU) * (x + MU) / abs(x + MU) ** 3 - MU * (x - 1 + MU) / abs(x - 1 + MU) ** 3
    a, b = -MU + 1e-9, 1 - MU - 1e-9
    for _ in range(200):
        m = 0.5 * (a + b)
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def corregir(x0):
    res = lambda vy: cruce([x0, 0.0, 0.0, vy])[1][2]
    # barrido para encontrar un cambio de signo en vy0 (ambos sentidos)
    cand = [i * 0.005 for i in range(-80, 81) if i != 0]
    prev = None
    for vy in cand:
        try:
            r = res(vy)
        except RuntimeError:
            prev = None
            continue
        if prev is not None and prev[1] * r < 0 and abs(vy - prev[0]) < 0.0051 and abs(vy) < 0.8:
            a, b, fa = prev[0], vy, prev[1]
            for _ in range(60):
                m = 0.5 * (a + b)
                fm = res(m)
                if fa * fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            return 0.5 * (a + b)
        prev = (vy, r)
    raise RuntimeError("sin raiz")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    xl = L1x()
    # periodo lineal desde el laboratorio de estabilidad (b del par imaginario)
    xx = 1 + (1 - MU) * (3 * (xl + MU) ** 2 / abs(xl + MU) ** 5 - 1 / abs(xl + MU) ** 3) + MU * (3 * (xl - 1 + MU) ** 2 / abs(xl - 1 + MU) ** 5 - 1 / abs(xl - 1 + MU) ** 3)
    yy = 1 + (1 - MU) * (-1 / abs(xl + MU) ** 3) + MU * (-1 / abs(xl - 1 + MU) ** 3)
    B, D = 4 - xx - yy, xx * yy
    s1 = (-B + math.sqrt(B * B - 4 * D)) / 2
    s2 = (-B - math.sqrt(B * B - 4 * D)) / 2
    b = math.sqrt(-s2)
    T_lin = 2 * math.pi / b
    print(f"L1 Tierra-Luna: x = {xl:.8f} ; frecuencia lineal b = {b:.5f} ; periodo lineal = {T_lin:.4f} ({T_lin * U_D:.3f} d)")
    print(" Ax [adim] Ax [km]    vy0         T [adim]   T [d]    C            cierre     deriva C")
    filas = []
    for Ax in (1e-3, 5e-3, 1e-2, 2e-2):
        x0 = xl - Ax
        vy0 = corregir(x0)
        th, sh = cruce([x0, 0.0, 0.0, vy0])
        T = 2 * th
        s, C0, dC = [x0, 0.0, 0.0, vy0], jacobi([x0, 0.0, 0.0, vy0]), 0.0
        n = int(T / 1e-3)
        for _ in range(n):
            s = paso(s, 1e-3)
            dC = max(dC, abs(jacobi(s) - C0))
        s = paso(s, T - n * 1e-3)
        cierre = max(abs(a - b2) for a, b2 in zip(s, [x0, 0.0, 0.0, vy0]))
        filas.append(dict(Ax=Ax, km=Ax * A_KM, vy0=vy0, T=T, Td=T * U_D, C=C0, cierre=cierre, dC=dC))
        print(f" {Ax:8.1e} {Ax * A_KM:9.1f} {vy0:11.6f} {T:10.6f} {T * U_D:8.3f} {C0:11.6f} {cierre:10.2e} {dC:9.2e}")
    dT = abs(filas[0]["T"] - T_lin) / T_lin
    print(f"Periodo con Ax = 1e-3 frente al lineal: diferencia relativa = {dT:.2%}")
    assert all(r["cierre"] < 1e-6 for r in filas) and all(r["dC"] < 1e-8 for r in filas) and dT < 0.005
    print("Pruebas superadas.")
    out = {"python": platform.python_version(), "xl": xl, "b": b, "Tlin": T_lin, "Tlin_d": T_lin * U_D, "dT": dT}
    for i, r in enumerate(filas):
        for k, v in r.items():
            out[f"f{i}_{k}"] = v
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
