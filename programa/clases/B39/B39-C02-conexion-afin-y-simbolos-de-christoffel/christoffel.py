#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C02: simbolos de Christoffel por diferencias finitas, compatibilidad metrica y geodesicas.

Datos: ninguna constante fisica ni dato observado. Las metricas (2-esfera unitaria y Schwarzschild con M = 1 en unidades geometrizadas G = c = 1), los puntos de evaluacion y las condiciones iniciales de la geodesica son
ILUSTRATIVOS; las comparaciones usan formulas cerradas.
Modelo: Gamma^d_ab = 1/2 g^de (d_a g_eb + d_b g_ea - d_e g_ab) con derivadas centrales de paso h = 1e-5; compatibilidad d_c g_ab - Gamma^d_ca g_db - Gamma^d_cb g_ad = 0; geodesica d2x^a/ds2 = -Gamma^a_bc dx^b/ds dx^c/ds integrada con Runge-Kutta de orden 4.
Supuestos: conexion de Levi-Civita (sin torsion y compatible con la metrica). Validez: ilustrativa.
Tolerancia: Christoffel frente a la formula cerrada a 1e-8; compatibilidad a 1e-8; geodesica frente al gran circulo a 1e-8.
"""
from __future__ import annotations
import math, platform

def inv(m):
    n = len(m)
    a = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[p] = a[p], a[i]
        d = a[i][i]
        a[i] = [v / d for v in a[i]]
        for r in range(n):
            if r != i:
                f = a[r][i]
                a[r] = [vr - f * vi for vr, vi in zip(a[r], a[i])]
    return [row[n:] for row in a]

def dmetric(g, x, h=1e-5):
    n = len(x)
    out = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h; xm[c] -= h
        gp, gm = g(xp), g(xm)
        out.append([[(gp[a][b] - gm[a][b]) / (2 * h) for b in range(n)] for a in range(n)])
    return out  # out[c][a][b] = d_c g_ab

def christoffel(g, x, h=1e-5):
    n = len(x)
    gi = inv(g(x)); dg = dmetric(g, x, h)
    return [[[0.5 * sum(gi[d][e] * (dg[a][e][b] + dg[b][e][a] - dg[e][a][b]) for e in range(n)) for b in range(n)] for a in range(n)] for d in range(n)]

def sph(x):
    return [[1.0, 0.0], [0.0, math.sin(x[0]) ** 2]]

M = 1.0
def schw(x):  # coordenadas (t, r, theta, phi)
    t, r, th, ph = x
    f = 1 - 2 * M / r
    return [[-f, 0, 0, 0], [0, 1 / f, 0, 0], [0, 0, r * r, 0], [0, 0, 0, r * r * math.sin(th) ** 2]]

def geodesica(G, x, v, s_fin, n):
    def f(y):
        x, v = y[:2], y[2:]
        Gm = G(x)
        acc = [-sum(Gm[a][b][c] * v[b] * v[c] for b in range(2) for c in range(2)) for a in range(2)]
        return v + acc
    y = x + v; h = s_fin / n
    for _ in range(n):
        k1 = f(y); k2 = f([yi + 0.5 * h * ki for yi, ki in zip(y, k1)])
        k3 = f([yi + 0.5 * h * ki for yi, ki in zip(y, k2)]); k4 = f([yi + h * ki for yi, ki in zip(y, k3)])
        y = [yi + h / 6 * (a + 2 * b + 2 * c + d) for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]
    return y

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    th = 0.9
    G = christoffel(sph, [th, 0.4])
    ex_tpp, ex_ptp = -math.sin(th) * math.cos(th), math.cos(th) / math.sin(th)
    print(f"2-esfera  Gamma^th_phph numerico {G[0][1][1]:.9f}  cerrado {ex_tpp:.9f}")
    print(f"2-esfera  Gamma^ph_thph numerico {G[1][0][1]:.9f}  cerrado {ex_ptp:.9f}")
    asim = max(abs(G[d][a][b] - G[d][b][a]) for d in range(2) for a in range(2) for b in range(2))
    print(f"asimetria maxima en los indices inferiores: {asim:.2e}")
    # compatibilidad metrica
    dg = dmetric(sph, [th, 0.4])
    comp = max(abs(dg[c][a][b] - sum(G[d][c][a] * sph([th, 0.4])[d][b] + G[d][c][b] * sph([th, 0.4])[a][d] for d in range(2)))
               for c in range(2) for a in range(2) for b in range(2))
    print(f"violacion maxima de la compatibilidad metrica: {comp:.2e}")
    # Schwarzschild
    r = 6.0
    Gs = christoffel(schw, [0.0, r, math.pi / 2, 0.0])
    f = 1 - 2 * M / r
    ex = {"Gamma^r_tt": M / r ** 2 * f, "Gamma^t_tr": M / (r * r * f), "Gamma^r_rr": -M / (r * r * f), "Gamma^r_thth": -r * f, "Gamma^th_rth": 1 / r}
    num = {"Gamma^r_tt": Gs[1][0][0], "Gamma^t_tr": Gs[0][0][1], "Gamma^r_rr": Gs[1][1][1], "Gamma^r_thth": Gs[1][2][2], "Gamma^th_rth": Gs[2][1][2]}
    print(f"{'simbolo (r = 6 M)':20s} {'numerico':>14s} {'cerrado':>14s}")
    for k in ex:
        print(f"{k:20s} {num[k]:14.9f} {ex[k]:14.9f}")
    # geodesica en la 2-esfera: gran circulo
    th0 = math.pi / 2 - 0.3; ph0 = 0.0
    ang = math.radians(35.0)
    v0 = [math.cos(ang), math.sin(ang) / math.sin(th0)]
    s_fin = 2.0
    y = geodesica(lambda x: christoffel(sph, x), [th0, ph0], v0, s_fin, 400)
    # trayectoria exacta: gran circulo en R^3
    P = lambda t, p: (math.sin(t) * math.cos(p), math.sin(t) * math.sin(p), math.cos(t))
    p0 = P(th0, ph0)
    e_th = (math.cos(th0) * math.cos(ph0), math.cos(th0) * math.sin(ph0), -math.sin(th0))
    e_ph = (-math.sin(ph0), math.cos(ph0), 0.0)
    t_vec = tuple(math.cos(ang) * e_th[i] + math.sin(ang) * e_ph[i] for i in range(3))
    pf = tuple(math.cos(s_fin) * p0[i] + math.sin(s_fin) * t_vec[i] for i in range(3))
    pn = P(y[0], y[1])
    err = max(abs(pn[i] - pf[i]) for i in range(3))
    print(f"geodesica (longitud {s_fin}): error frente al gran circulo = {err:.2e}")
    norma = y[2] ** 2 + math.sin(y[0]) ** 2 * y[3] ** 2
    print(f"norma conservada de la velocidad: {norma:.10f}")
    assert abs(G[0][1][1] - ex_tpp) < 1e-8 and abs(G[1][0][1] - ex_ptp) < 1e-8
    assert asim < 1e-12 and comp < 1e-8
    for k in ex:
        assert abs(num[k] - ex[k]) < 1e-8, k
    assert err < 1e-8 and abs(norma - 1.0) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
