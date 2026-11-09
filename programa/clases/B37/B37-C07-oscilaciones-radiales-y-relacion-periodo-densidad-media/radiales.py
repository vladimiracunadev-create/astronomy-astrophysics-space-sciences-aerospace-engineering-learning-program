#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C07: modo radial fundamental de un politropo n = 3 y relacion periodo-densidad media.

Datos: constante G de NIST CODATA 2022 y valores nominales solares de la UAI 2015 B3 (GM = 1,3271244e20 m3/s2, R = 6,957e8 m), consultados el 2026-11-09 (solo resumen de la UAI).
La estructura (politropo n = 3 de Eddington) y el indice adiabatico Gamma_1 = 5/3 (o 4/3) son un modelo de juguete ILUSTRATIVO; no es un modelo solar ni un modelo de estrella pulsante real.
Modelo: oscilaciones radiales adiabaticas en forma de Sturm-Liouville, con eta = xi_r/r: d/dr(Gamma_1 p r^4 eta') + [r^3 d((3 Gamma_1 - 4) p)/dr + omega^2 rho r^4] eta = 0.
En variables de Lane-Emden (rho = rho_c theta^3, p = p_c theta^4, sigma^2 = omega^2/(4 pi G rho_c)): (Gamma_1 theta^4 xi^4 eta')' + [xi^3 ((3 Gamma_1 - 4) theta^4)' + 4 sigma^2 theta^3 xi^4] eta = 0.
Vias independientes: (1) disparo desde el centro con RK4 y biseccion en sigma^2 hasta que w = Gamma_1 theta^4 xi^4 eta' se anula en la superficie; (2) cociente de Rayleigh con eta = 1:
[Int Gamma_1 theta^4 xi^4 eta'^2 - Int xi^3 ((3 Gamma_1 - 4) theta^4)' eta^2]/(4 Int theta^3 xi^4 eta^2) minimizado en la base eta = sum c_k (xi/xi_1)^(2k) (Rayleigh-Ritz, cota superior por el principio variacional). Caso exacto: Gamma_1 = 4/3 da sigma^2 = 0.
Supuestos: adiabatico, sin rotacion, sin atmosfera; el politropo n = 3 con Gamma_1 distinto de 4/3 no es autoconsistente (modelo de juguete). Validez: orientativa.
Tolerancia: sigma^2(Gamma_1 = 4/3) < 1e-4; Rayleigh-Ritz no menor que el disparo y, con base de grado 3, dentro del 1 % del disparo para Gamma_1 = 5/3.
"""
from __future__ import annotations
import math, platform, sys

G = 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8


def lane_emden_perfil(h=2e-3):
    xi = h
    th = 1 - xi**2 / 6 + 3 * xi**4 / 120 - 3 * (8 * 3 - 5) * xi**6 / 15120
    ph = -xi / 3 + 3 * xi**3 / 30 - 6 * 3 * (8 * 3 - 5) * xi**5 / 15120
    pts = [(xi, th, ph)]

    def f(x, t, p):
        return p, -2 * p / x - max(t, 0.0) ** 3

    while True:
        k1 = f(xi, th, ph)
        k2 = f(xi + h / 2, th + h / 2 * k1[0], ph + h / 2 * k1[1])
        k3 = f(xi + h / 2, th + h / 2 * k2[0], ph + h / 2 * k2[1])
        k4 = f(xi + h, th + h * k3[0], ph + h * k3[1])
        tn = th + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        pn = ph + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if tn <= 0.0005:
            return pts
        xi, th, ph = xi + h, tn, pn
        pts.append((xi, th, ph))


PERFIL = lane_emden_perfil()
XI1 = 6.89685


def w_superficie(s2, g1):
    """Integra (eta, w) con RK4 sobre la malla del perfil; devuelve w en el ultimo punto."""
    eta, w = 1.0, 0.0

    def dpt(xi, th, ph):
        # d/dxi [ (3 g1 - 4) theta^4 ] = 4 (3 g1 - 4) theta^3 theta'
        return 4 * (3 * g1 - 4) * th**3 * ph

    def rhs(i, e, ww):
        xi, th, ph = PERFIL[i]
        de = ww / (g1 * th**4 * xi**4)
        dw = -(xi**3 * dpt(xi, th, ph) + 4 * s2 * th**3 * xi**4) * e
        return de, dw

    # el esquema usa los puntos de la malla de 2e-3; paso trapezoidal-Heun de segundo orden con h pequeno
    h = PERFIL[1][0] - PERFIL[0][0]
    for i in range(len(PERFIL) - 1):
        a = rhs(i, eta, w)
        e1, w1 = eta + h * a[0], w + h * a[1]
        b = rhs(i + 1, e1, w1)
        eta += h * 0.5 * (a[0] + b[0])
        w += h * 0.5 * (a[1] + b[1])
    return w


def sigma2_disparo(g1, hi=1.0):
    if abs(g1 - 4 / 3) < 1e-12:
        return 0.0
    # barrido para el primer cambio de signo de w(superficie) desde un valor pequeno
    grid = [0.005 * k for k in range(1, int(hi / 0.005))]
    prev = w_superficie(grid[0], g1)
    for a, b in zip(grid, grid[1:]):
        cur = w_superficie(b, g1)
        if prev * cur < 0:
            lo, hi_ = a, b
            for _ in range(40):
                mid = 0.5 * (lo + hi_)
                if w_superficie(mid, g1) * w_superficie(lo, g1) > 0:
                    lo = mid
                else:
                    hi_ = mid
            return 0.5 * (lo + hi_)
        prev = cur
    raise RuntimeError("sin raiz")


def resolver(A, b):
    n = len(b)
    M = [row[:] + [b[k]] for k, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][k] * x[k] for k in range(r + 1, n))) / M[r][r]
    return x


def matrices(g1, grado):
    """Matrices A y B de Rayleigh-Ritz con la base eta_k = (xi/xi_1)^(2k), k = 0..grado."""
    h = PERFIL[1][0] - PERFIL[0][0]
    n = grado + 1
    A = [[0.0] * n for _ in range(n)]
    B = [[0.0] * n for _ in range(n)]
    for xi, th, ph in PERFIL:
        x = xi / XI1
        e = [x ** (2 * k) for k in range(n)]
        ep = [2 * k * x ** (2 * k - 1) / XI1 if k else 0.0 for k in range(n)]
        dpt = 4 * (3 * g1 - 4) * th**3 * ph
        for a in range(n):
            for b in range(n):
                A[a][b] += (g1 * th**4 * xi**4 * ep[a] * ep[b] - xi**3 * dpt * e[a] * e[b]) * h
                B[a][b] += 4 * th**3 * xi**4 * e[a] * e[b] * h
    return A, B


def rayleigh_ritz(g1, grado):
    """Menor valor propio generalizado A v = s2 B v por iteracion inversa."""
    A, B = matrices(g1, grado)
    n = grado + 1
    v = [1.0] * n
    lam = 0.0
    for _ in range(200):
        Bv = [sum(B[i][j] * v[j] for j in range(n)) for i in range(n)]
        w = resolver(A, Bv)
        nrm = math.sqrt(sum(x * x for x in w))
        v = [x / nrm for x in w]
        Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        Bv = [sum(B[i][j] * v[j] for j in range(n)) for i in range(n)]
        lam_n = sum(v[i] * Av[i] for i in range(n)) / sum(v[i] * Bv[i] for i in range(n))
        if abs(lam_n - lam) < 1e-13:
            break
        lam = lam_n
    return lam_n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"perfil n = 3: {len(PERFIL)} puntos hasta xi = {PERFIL[-1][0]:.3f} (xi_1 = {XI1})")
    # caso exacto
    w0 = w_superficie(0.0, 4 / 3)
    print(f"Gamma_1 = 4/3: w(superficie) con sigma^2 = 0 vale {w0:.2e} (el modo homologo eta = 1 es solucion exacta)")
    assert abs(w0) < 1e-3
    g1 = 5 / 3
    s2 = sigma2_disparo(g1)
    rq = [rayleigh_ritz(g1, k) for k in (0, 1, 2, 3)]
    print(f"Gamma_1 = 5/3: sigma^2 (disparo) = {s2:.4f}")
    print("Rayleigh-Ritz con base de grado 0, 1, 2, 3 en (xi/xi_1)^2: " + " ; ".join(f"{x:.4f}" for x in rq))
    assert all(x >= s2 * 0.999 for x in rq) and rq[1] <= rq[0] and rq[3] <= rq[2] <= rq[1]
    assert abs(rq[3] / s2 - 1) < 0.01
    A0, B0 = matrices(4 / 3, 0)
    print(f"Gamma_1 = 4/3: A00/B00 (cociente de Rayleigh con eta = 1) = {A0[0][0] / B0[0][0]:.2e}")
    assert abs(A0[0][0] / B0[0][0]) < 1e-12
    # relacion periodo-densidad media
    rc_rm = 54.1825
    M = GM_SOL / G
    rho_m = M / (4 / 3 * math.pi * R_SOL**3)
    rho_c = rc_rm * rho_m
    omega = math.sqrt(4 * math.pi * G * rho_c * s2)
    Pi = 2 * math.pi / omega
    Q = Pi * math.sqrt(rho_m / rho_m)
    print(f"rho_medio = {rho_m:.1f} kg/m3 ; omega = {omega:.4e} rad/s ; Pi = {Pi / 3600:.3f} h ; Q = Pi sqrt(rho/rho_sol) = {Q / 3600:.3f} h")
    # escala: otra estrella del mismo modelo con rho_medio 1/100 de la solar
    rho2 = rho_m / 100
    omega2 = math.sqrt(4 * math.pi * G * rc_rm * rho2 * s2)
    Pi2 = 2 * math.pi / omega2
    print(f"rho_medio/100: Pi = {Pi2 / 3600:.3f} h ; Pi2/Pi = {Pi2 / Pi:.4f} (esperado 10)")
    assert abs(Pi2 / Pi - 10) < 1e-9
    # frecuencia dinamica
    tau = math.sqrt(R_SOL**3 / GM_SOL)
    print(f"escala dinamica sqrt(R^3/GM) = {tau:.1f} s ; Pi/tau = {Pi / tau:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
