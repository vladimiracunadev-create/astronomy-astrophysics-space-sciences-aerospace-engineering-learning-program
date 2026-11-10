#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C07: constante de Jacobi, curvas de velocidad cero y regiones prohibidas (Tierra-Luna y Sol-Tierra).

Datos consultados (2026-11-10): GM de la Luna 4902.800 km3/s2 (JPL SSD); GM del Sol 132 712 x 10^6 km3/s2 (NASA/NSSDC, Sun Fact Sheet).
GM de la Tierra ~ 398 600 km3/s2 (aproximado, deducido de la masa de la tabla de planetas del JPL).
SINTETICO: 20 estados iniciales aleatorios (semilla 73) en el plano, con velocidad tal que C cae en la ventana elegida.
Modelo: CR3BP plano, marco sinodico adimensional. C = 2 Omega - v^2; region permitida: 2 Omega >= C.
C en los puntos de Lagrange: C(Li) = 2 Omega(Li); C4 = C5 = 3 - mu (1 - mu).
Segunda via: (a) conectividad por relleno de una rejilla de 0.01 frente a la teoria de umbrales C1 > C2 > C3 > C4;
(b) 20 integraciones RK4 (dt = 1e-3, T <= 10; se detienen a menos de 0.1 de un primario) que no deben entrar nunca en la region prohibida (2 Omega - C >= -1e-6) y conservan C (< 1e-5).
"""
from __future__ import annotations
import json, math, platform, random, sys
from collections import deque

GM = {"Sol": 132712e6, "Tierra": 398600.0, "Luna": 4902.800}


def omega2(x, y, mu):
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    return x * x + y * y + 2 * (1 - mu) / r1 + 2 * mu / r2


def colineal(mu, a, b):
    g = lambda x: x - (1 - mu) * (x + mu) / abs(x + mu) ** 3 - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3
    for _ in range(200):
        m = 0.5 * (a + b)
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def umbrales(mu):
    L1 = colineal(mu, -mu + 1e-9, 1 - mu - 1e-9)
    L2 = colineal(mu, 1 - mu + 1e-9, 3.0)
    L3 = colineal(mu, -3.0, -mu - 1e-9)
    return [omega2(L1, 0, mu), omega2(L2, 0, mu), omega2(L3, 0, mu), 3 - mu * (1 - mu)]


def conectividad(mu, C, h=0.01, L=2.0):
    n = int(2 * L / h) + 1
    ok = [[omega2(-L + i * h, -L + j * h, mu) >= C for j in range(n)] for i in range(n)]
    idx = lambda v: int(round((v + L) / h))
    def region(x0, y0):
        i0, j0 = idx(x0), idx(y0)
        if not ok[i0][j0]:
            return None
        vis = {(i0, j0)}
        q = deque([(i0, j0)])
        while q:
            i, j = q.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                if 0 <= a < n and 0 <= b < n and (a, b) not in vis and ok[a][b]:
                    vis.add((a, b))
                    q.append((a, b))
        return vis
    R = region(-mu, 0.1)
    tierra_luna = R is not None and (idx(1 - mu - 0.08), idx(0.0)) in R
    tierra_ext = R is not None and (idx(-1.9), idx(0.0)) in R or (R is not None and (idx(1.9), idx(0.0)) in R)
    return tierra_luna, tierra_ext, ok, h, L


def mapa(mu, C):
    filas = []
    for j in range(12, -13, -1):
        y = j * 0.1
        fila = ""
        for i in range(-32, 33):
            x = i * 0.05
            if abs(y) < 1e-9 and abs(x + mu) < 0.026:
                fila += "T"
            elif abs(y) < 1e-9 and abs(x - 1 + mu) < 0.026:
                fila += "L"
            else:
                fila += "." if omega2(x, y, mu) >= C else "#"
        filas.append(fila)
    return filas


def f(s, mu):
    x, y, vx, vy = s
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    return [vx, vy, 2 * vy + x - (1 - mu) * (x + mu) / r1**3 - mu * (x - 1 + mu) / r2**3, -2 * vx + y - (1 - mu) * y / r1**3 - mu * y / r2**3]


def rk4(s, mu, h):
    k1 = f(s, mu)
    k2 = f([a + 0.5 * h * b for a, b in zip(s, k1)], mu)
    k3 = f([a + 0.5 * h * b for a, b in zip(s, k2)], mu)
    k4 = f([a + h * b for a, b in zip(s, k3)], mu)
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    for nom, tag, (g1, g2) in (("Tierra-Luna", "tl", (GM["Tierra"], GM["Luna"])), ("Sol-Tierra", "st", (GM["Sol"], GM["Tierra"]))):
        mu = g2 / (g1 + g2)
        c = umbrales(mu)
        print(f"{nom} (mu = {mu:.6e}): C1 = {c[0]:.6f} ; C2 = {c[1]:.6f} ; C3 = {c[2]:.6f} ; C4 = C5 = {c[3]:.6f}")
        assert c[0] > c[1] > c[2] > c[3]
        for i, v in enumerate(c, 1):
            out[f"{tag}_C{i}"] = v
        out[f"{tag}_mu"] = mu
    mu = out["tl_mu"]
    c = [out[f"tl_C{i}"] for i in range(1, 5)]
    ventanas = [("C > C1", c[0] + 0.05, (False, False)), ("C2 < C < C1", 0.5 * (c[0] + c[1]), (True, False)),
                ("C3 < C < C2", 0.5 * (c[1] + c[2]), (True, True)), ("C4 < C < C3", 0.5 * (c[2] + c[3]), (True, True))]
    print("Conectividad de la region permitida desde la Tierra (rejilla 0.01) frente a la teoria:")
    for k, (nom, C, esp) in enumerate(ventanas):
        tl, te, ok, h, L = conectividad(mu, C)
        print(f"  {nom:12s} C = {C:.4f}: llega a la Luna = {tl} ; llega al exterior = {te} ; esperado = {esp}")
        assert (tl, te) == esp, nom
        out[f"v{k}_C"] = C
        if k == 1:
            print("  Mapa (# prohibido, . permitido, T Tierra, L Luna; x de -1.6 a 1.6 paso 0.05, y de 1.2 a -1.2 paso 0.1):")
            for fila in mapa(mu, C):
                print("    " + fila)
    rnd = random.Random(73)
    C_obj = 0.5 * (c[0] + c[1])
    dCmax, viol_min, n_ok = 0.0, 1e9, 0
    for _ in range(20):
        while True:
            x, y = rnd.uniform(-1.3, 1.3), rnd.uniform(-1.0, 1.0)
            v2 = omega2(x, y, mu) - C_obj
            if v2 > 0.02 and math.hypot(x + mu, y) > 0.3 and math.hypot(x - 1 + mu, y) > 0.3:
                break
        ang = rnd.uniform(0, 2 * math.pi)
        v = math.sqrt(v2)
        s = [x, y, v * math.cos(ang), v * math.sin(ang)]
        for _ in range(10000):
            s = rk4(s, mu, 1e-3)
            if math.hypot(s[0] + mu, s[1]) < 0.1 or math.hypot(s[0] - 1 + mu, s[1]) < 0.1:
                break
            C = omega2(s[0], s[1], mu) - (s[2] ** 2 + s[3] ** 2)
            dCmax = max(dCmax, abs(C - C_obj))
            viol_min = min(viol_min, omega2(s[0], s[1], mu) - C_obj)
        n_ok += 1
    print(f"20 trayectorias sinteticas (semilla 73) con C = {C_obj:.4f}: deriva maxima de C = {dCmax:.1e} ; minimo de (2 Omega - C) = {viol_min:.1e} (>= 0 si nunca entran en la region prohibida)")
    assert dCmax < 1e-5 and viol_min > -1e-6
    print("Pruebas superadas.")
    out.update(st_dC12=out['st_C1'] - out['st_C2'], tl_dC12=out['tl_C1'] - out['tl_C2'], dCmax=dCmax, viol_min=viol_min, C_obj=C_obj)
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
