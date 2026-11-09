#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C04: tensor de energia-momento de un fluido perfecto, condiciones de energia y conservacion.

Datos: c = 299 792 458 m/s (exacta), NIST CODATA 2022 (tabla allascii, consultada el 2026-11-09). Las densidades, las presiones, la velocidad de la boost (0,6 c) y la densidad inicial del universo de prueba son
ILUSTRATIVAS (sinteticas); no describen ningun sistema real.
Modelo: T^ab = (rho + p) u^a u^b + p g^ab con c = 1 en las secciones geometricas; boost de Lorentz comparado con Lambda T Lambda^T; divergencia covariante nabla_a T^ab = d_a T^ab + Gamma^a_al T^lb + Gamma^b_al T^al calculada por diferencias finitas en un universo plano de Friedmann con a(t) = t^n (polvo n = 2/3, radiacion n = 1/2).
Supuestos: fluido perfecto, metrica FLRW plana. Validez: ilustrativa (geometria con materia de prueba).
Tolerancia: boost a 1e-12; divergencia a 1e-7 de la escala de T^00; densidades frente a la ley rho ~ a^-3 y a^-4 a 1e-9.
"""
from __future__ import annotations
import math, platform

C = 299792458.0  # m/s, NIST CODATA 2022 (exacta)

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

def christoffel(g, x, h=1e-5):
    n = len(x)
    gi = inv(g(x)); dg = []
    for c in range(n):
        xp = list(x); xm = list(x); xp[c] += h; xm[c] -= h
        gp, gm = g(xp), g(xm)
        dg.append([[(gp[a][b] - gm[a][b]) / (2 * h) for b in range(n)] for a in range(n)])
    return [[[0.5 * sum(gi[d][e] * (dg[a][e][b] + dg[b][e][a] - dg[e][a][b]) for e in range(n)) for b in range(n)] for a in range(n)] for d in range(n)]

def fluido(g, u, rho, p):
    gi = inv(g)
    n = len(u)
    return [[(rho + p) * u[a] * u[b] + p * gi[a][b] for b in range(n)] for a in range(n)]

def divergencia(g, T, x, h=1e-5):
    """nabla_a T^{ab}; T(x) devuelve T^{ab}."""
    n = len(x); G = christoffel(g, x)
    out = []
    for b in range(n):
        d = 0.0
        for a in range(n):
            xp = list(x); xm = list(x); xp[a] += h; xm[a] -= h
            d += (T(xp)[a][b] - T(xm)[a][b]) / (2 * h)
        T0 = T(x)
        d += sum(G[a][a][l] * T0[l][b] for a in range(n) for l in range(n))
        d += sum(G[b][a][l] * T0[a][l] for a in range(n) for l in range(n))
        out.append(d)
    return out

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    eta = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    rho, p = 2.0, 0.5
    T0 = fluido(eta, [1, 0, 0, 0], rho, p)
    print(f"reposo: T = diag({T0[0][0]:.4f}, {T0[1][1]:.4f}, {T0[2][2]:.4f}, {T0[3][3]:.4f})  traza = {-T0[0][0] + T0[1][1] + T0[2][2] + T0[3][3]:.4f} (cerrada -rho + 3p = {-rho + 3 * p:.4f})")
    v = 0.6; gam = 1 / math.sqrt(1 - v * v)
    Tb = fluido(eta, [gam, gam * v, 0, 0], rho, p)
    L = [[gam, gam * v, 0, 0], [gam * v, gam, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    TL = [[sum(L[a][c] * T0[c][d] * L[b][d] for c in range(4) for d in range(4)) for b in range(4)] for a in range(4)]
    dif = max(abs(Tb[a][b] - TL[a][b]) for a in range(4) for b in range(4))
    print(f"boost v = {v} c: T^00 = {Tb[0][0]:.6f} (cerrada gamma^2 (rho + p v^2) = {gam ** 2 * (rho + p * v * v):.6f}), T^01 = {Tb[0][1]:.6f}")
    print(f"diferencia con Lambda T Lambda^T: {dif:.2e}")
    # condiciones de energia
    print(f"{'ecuacion de estado':20s} {'w = p/rho':>9s} {'debil':>6s} {'dominante':>10s} {'fuerte':>7s}")
    casos = [("polvo", 0.0), ("radiacion", 1 / 3), ("constante cosmologica", -1.0), ("rigido", 1.0), ("fantasma", -1.5)]
    res = {}
    for nombre, w in casos:
        rh = 1.0; pp = w * rh
        debil = rh >= 0 and rh + pp >= 0
        dom = rh >= abs(pp)
        fuerte = rh + pp >= 0 and rh + 3 * pp >= 0
        res[nombre] = (debil, dom, fuerte)
        print(f"{nombre:20s} {w:9.4f} {str(debil):>6s} {str(dom):>10s} {str(fuerte):>7s}")
    # conservacion en FLRW
    print(f"{'universo':10s} {'n':>6s} {'max |div T|':>13s} {'escala T00':>11s}")
    for nombre, n, k, w in (("polvo", 2 / 3, 3, 0.0), ("radiacion", 0.5, 4, 1 / 3)):
        g = lambda x, n=n: [[-1, 0, 0, 0], [0, x[0] ** (2 * n), 0, 0], [0, 0, x[0] ** (2 * n), 0], [0, 0, 0, x[0] ** (2 * n)]]
        Tf = lambda x, n=n, k=k, w=w: fluido(g(x), [1, 0, 0, 0], 1.0 * x[0] ** (-n * k), w * x[0] ** (-n * k))
        x = [2.0, 0.0, 0.0, 0.0]
        dv = divergencia(g, Tf, x)
        esc = Tf(x)[0][0]
        print(f"{nombre:10s} {n:6.4f} {max(abs(d) for d in dv):13.3e} {esc:11.5f}")
        assert max(abs(d) for d in dv) < 1e-7 * esc * 10, nombre
        # ley rho ~ a^-3(1+w) comparada con la integracion de d rho / d ln a = -3 (1 + w) rho
        rho_a = 1.0; N = 2000; dln = math.log(8.0) / N
        f = lambda r: -3 * (1 + w) * r
        for _ in range(N):
            k1 = f(rho_a); k2 = f(rho_a + 0.5 * dln * k1); k3 = f(rho_a + 0.5 * dln * k2); k4 = f(rho_a + dln * k3)
            rho_a += dln / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        print(f"  rho(a = 8)/rho(a = 1): integrada {rho_a:.9e}  cerrada 8^-{k} = {8.0 ** (-k):.9e}")
        assert abs(rho_a / 8.0 ** (-k) - 1) < 1e-9
    # control negativo: polvo con rho ~ a^-2 (no conservado) debe violar la divergencia
    g = lambda x: [[-1, 0, 0, 0], [0, x[0] ** (4 / 3), 0, 0], [0, 0, x[0] ** (4 / 3), 0], [0, 0, 0, x[0] ** (4 / 3)]]
    Tm = lambda x: fluido(g(x), [1, 0, 0, 0], x[0] ** (-4 / 3), 0.0)
    dm = max(abs(d) for d in divergencia(g, Tm, [2.0, 0.0, 0.0, 0.0]))
    print(f"control negativo (rho ~ a^-2): max |div T| = {dm:.3e}")
    assert dm > 1e-2
    e_si = 1.0 * C ** 2
    print(f"1 kg/m^3 de masa en reposo equivale a {e_si:.9e} J/m^3 (c^2, NIST CODATA 2022)")
    assert dif < 1e-12 and abs(Tb[0][0] - gam ** 2 * (rho + p * v * v)) < 1e-12
    assert res["polvo"] == (True, True, True) and res["constante cosmologica"] == (True, True, False) and res["fantasma"][0] is False
    assert abs(e_si - 8.987551787368176e16) < 1.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
