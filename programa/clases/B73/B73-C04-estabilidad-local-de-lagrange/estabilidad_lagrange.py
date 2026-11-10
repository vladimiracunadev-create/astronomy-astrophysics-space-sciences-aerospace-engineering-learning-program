#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C04: estabilidad lineal de los puntos de Lagrange y criterio de Routh.

Datos consultados (2026-11-10): GM del Sol 132 712 x 10^6 km3/s2 (NASA/NSSDC, Sun Fact Sheet); GM de Jupiter 126.687 x 10^6 km3/s2
(NASA/NSSDC, Jupiter Fact Sheet); GM de la Luna 4902.800 km3/s2 (JPL SSD); periodos de la Luna 27.322 d (JPL SSD, elementos medios),
de la Tierra 365.2 d y de Jupiter 4331 d (NASA/NSSDC, Planetary Fact Sheet). GM de la Tierra ~ 398 600 km3/s2 (aproximado, deducido).
Modelo: CR3BP plano, marco sinodico adimensional. Linealizacion: lambda^4 + (4 - Oxx - Oyy) lambda^2 + (Oxx Oyy - Oxy^2) = 0.
Segunda via: (a) segundas derivadas de Omega por diferencias finitas del gradiente; (b) integracion no lineal RK4 (dt = 2e-3) de una
perturbacion SINTETICA de tamano 1e-8 (L1) o 1e-6 (L4) y medida de la tasa de crecimiento. Tolerancias: derivadas < 1e-6;
tasa medida frente a la autovalor real < 1 %; criterio de Routh frente a biseccion del discriminante < 1e-12.
"""
from __future__ import annotations
import json, math, platform, sys

GM = {"Sol": 132712e6, "Jupiter": 126.687e6, "Tierra": 398600.0, "Luna": 4902.800}
SIST = {"Tierra-Luna": (GM["Tierra"], GM["Luna"], 27.322), "Sol-Tierra": (GM["Sol"], GM["Tierra"], 365.2), "Sol-Jupiter": (GM["Sol"], GM["Jupiter"], 4331.0)}


def grad(x, y, mu):
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    return (x - (1 - mu) * (x + mu) / r1**3 - mu * (x - 1 + mu) / r2**3, y - (1 - mu) * y / r1**3 - mu * y / r2**3)


def hess(x, y, mu):
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    xx = 1 + (1 - mu) * (3 * (x + mu) ** 2 / r1**5 - 1 / r1**3) + mu * (3 * (x - 1 + mu) ** 2 / r2**5 - 1 / r2**3)
    yy = 1 + (1 - mu) * (3 * y * y / r1**5 - 1 / r1**3) + mu * (3 * y * y / r2**5 - 1 / r2**3)
    xy = 3 * (1 - mu) * (x + mu) * y / r1**5 + 3 * mu * (x - 1 + mu) * y / r2**5
    return xx, yy, xy


def hess_fd(x, y, mu, h=1e-6):
    gxp, gxm = grad(x + h, y, mu), grad(x - h, y, mu)
    gyp, gym = grad(x, y + h, mu), grad(x, y - h, mu)
    return (gxp[0] - gxm[0]) / (2 * h), (gyp[1] - gym[1]) / (2 * h), (gxp[1] - gxm[1]) / (2 * h)


def raices_s(xx, yy, xy):
    B, D = 4 - xx - yy, xx * yy - xy**2
    disc = B * B - 4 * D
    if disc < 0:
        return None
    r = math.sqrt(disc)
    return ((-B + r) / 2, (-B - r) / 2)


def colineal(mu, a, b):
    g = lambda x: x - (1 - mu) * (x + mu) / abs(x + mu) ** 3 - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3
    for _ in range(200):
        m = 0.5 * (a + b)
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def f(s, mu):
    x, y, vx, vy = s
    gx, gy = grad(x, y, mu)
    return [vx, vy, 2 * vy + gx, -2 * vx + gy]


def rk4(s, mu, dt, n):
    for _ in range(n):
        k1 = f(s, mu)
        k2 = f([a + 0.5 * dt * b for a, b in zip(s, k1)], mu)
        k3 = f([a + 0.5 * dt * b for a, b in zip(s, k2)], mu)
        k4 = f([a + dt * b for a, b in zip(s, k3)], mu)
        s = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]
    return s


def disc_L4(mu):
    return 1 - 27 * mu * (1 - mu)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    dh = 0.0
    tags = {"Tierra-Luna": "tl", "Sol-Tierra": "st", "Sol-Jupiter": "sj"}
    for nom, (g1, g2, P) in SIST.items():
        mu = g2 / (g1 + g2)
        u = P / (2 * math.pi)  # d por unidad de tiempo
        L1 = colineal(mu, -mu + 1e-9, 1 - mu - 1e-9)
        L2 = colineal(mu, 1 - mu + 1e-9, 3.0)
        L3 = colineal(mu, -3.0, -mu - 1e-9)
        pts = {"L1": (L1, 0.0), "L2": (L2, 0.0), "L3": (L3, 0.0), "L4": (0.5 - mu, math.sqrt(3) / 2), "L5": (0.5 - mu, -math.sqrt(3) / 2)}
        print(f"{nom} (mu = {mu:.6e}, unidad de tiempo = {u:.4f} d):")
        for k, (x, y) in pts.items():
            h1, h2 = hess(x, y, mu), hess_fd(x, y, mu)
            dh = max(dh, max(abs(a - b) / max(1.0, abs(a)) for a, b in zip(h1, h2)))
            s = raices_s(*h1)
            if s is None:
                print(f"   {k}: autovalores complejos con parte real -> inestable (espiral)")
                tipo = "inestable (complejo)"
            else:
                s1, s2 = s
                if s1 > 0 and s2 < 0:
                    a, b = math.sqrt(s1), math.sqrt(-s2)
                    print(f"   {k}: lambda = +-{a:.5f} (real) y +-{b:.5f}i  -> silla x centro ; e-folding {u / a:.2f} d")
                    out[f"{tags[nom]}_{k}_a"], out[f"{tags[nom]}_{k}_b"] = a, b
                    out[f"{tags[nom]}_{k}_ef"] = u / a
                elif s1 < 0 and s2 < 0:
                    w1, w2 = math.sqrt(-s1), math.sqrt(-s2)
                    print(f"   {k}: lambda = +-{w1:.5f}i y +-{w2:.5f}i  -> centro x centro (estable linealmente)")
                    out[f"{tags[nom]}_{k}_w1"], out[f"{tags[nom]}_{k}_w2"] = w1, w2
                    out[f"{tags[nom]}_{k}_P1"], out[f"{tags[nom]}_{k}_P2"] = 2 * math.pi * u / w1, 2 * math.pi * u / w2
                else:
                    print(f"   {k}: otro caso")
        out[f"{tags[nom]}_mu"] = mu
        out[f"{tags[nom]}_routh"] = 27 * mu * (1 - mu)
    # criterio de Routh por biseccion
    a, b = 0.0, 0.5
    for _ in range(200):
        m = 0.5 * (a + b)
        if disc_L4(m) > 0:
            a = m
        else:
            b = m
    mu_c = 0.5 * (a + b)
    mu_c_teo = 0.5 * (1 - math.sqrt(23 / 27))
    print(f"mu critico de Routh: biseccion = {mu_c:.10f} ; teoria (1 - sqrt(23/27))/2 = {mu_c_teo:.10f} ; diferencia = {abs(mu_c - mu_c_teo):.1e}")
    # segunda via no lineal: crecimiento en L1 Tierra-Luna
    mu = SIST["Tierra-Luna"][1] / (SIST["Tierra-Luna"][0] + SIST["Tierra-Luna"][1])
    L1 = colineal(mu, -mu + 1e-9, 1 - mu - 1e-9)
    a_teo = out["tl_L1_a"]
    d0 = 1e-8
    s = [L1 + d0, d0, 0.0, 0.0]
    dt = 2e-3
    s = rk4(s, mu, dt, 1500)  # t = 3
    d1 = math.hypot(s[0] - L1, s[1])
    s = rk4(s, mu, dt, 1000)  # t = 5
    d2 = math.hypot(s[0] - L1, s[1])
    # el modo inestable domina: tasa a partir de la razon de la distancia (incluye el modo central pequeno)
    tasa = math.log(d2 / d1) / 2.0
    print(f"No lineal L1 (perturbacion sintetica 1e-8): tasa medida = {tasa:.4f} ; autovalor real = {a_teo:.4f} ; diferencia relativa = {abs(tasa - a_teo) / a_teo:.2%}")
    # L4 Tierra-Luna acotado
    s = [0.5 - mu + 1e-6, math.sqrt(3) / 2 + 1e-6, 0.0, 0.0]
    mx = 0.0
    for _ in range(100):
        s = rk4(s, mu, dt, 500)  # 100 unidades de tiempo en total
        mx = max(mx, math.hypot(s[0] - (0.5 - mu), s[1] - math.sqrt(3) / 2))
    print(f"No lineal L4 Tierra-Luna (1e-6, t = 100 = {100 * SIST['Tierra-Luna'][2] / (2 * math.pi):.0f} d): distancia maxima a L4 = {mx:.2e}")
    assert dh < 1e-6 and abs(mu_c - mu_c_teo) < 1e-12
    assert abs(tasa - a_teo) / a_teo < 0.01
    assert mx < 1e-4
    assert out["tl_routh"] < 1 and out["st_routh"] < 1 and out["sj_routh"] < 1
    print("Pruebas superadas.")
    out.update(tasa_rel=abs(tasa - a_teo) / a_teo, dh=dh, mu_c=mu_c, mu_c_teo=mu_c_teo, tasa=tasa, d1=d1, d2=d2, mx=mx)
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
