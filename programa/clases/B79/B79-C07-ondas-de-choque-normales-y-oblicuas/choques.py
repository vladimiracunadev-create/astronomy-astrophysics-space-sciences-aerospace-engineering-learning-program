#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C07: ondas de choque normales y oblicuas en aire ideal.

Consultado (2026-11-10): NASA Glenn, relaciones del choque normal (p2/p1, rho2/rho1, T2/T1, M2) y descripcion del choque oblicuo
(solucion debil/fuerte, Tt constante, pt cae). Las ecuaciones del choque oblicuo (NACA Report 1135) NO se leyeron.
ESTANDAR (no consultado): relacion theta-beta-M tan(theta) = 2 cot(beta) (M^2 sin^2 beta - 1) / (M^2 (g + cos 2 beta) + 2);
presion total tras el choque normal; cambio de entropia ds = cp ln(T2/T1) - R ln(p2/p1).
ILUSTRATIVOS: gamma = 1.4, R = 287.05 J/(kg K), T1 = 250 K, p1 = 50000 Pa, M1 = 2 y 3, deflexion de 10 grados.
Via 2 (normal): residuos de los balances de masa, momento y energia total con las propiedades de ambos lados.
Via 2 (oblicuo): se construye el vector velocidad aguas abajo conservando la componente tangencial y se comprueba que gira theta.
Tolerancias: residuos < 1e-12 relativos; angulo de giro reconstruido frente al dato < 1e-9 grados.
"""
import math, platform

G, R, T1, P1 = 1.4, 287.05, 250.0, 50000.0
CP = G * R / (G - 1)


def normal(M):
    p = (2 * G * M * M - (G - 1)) / (G + 1)
    r = (G + 1) * M * M / ((G - 1) * M * M + 2)
    t = p / r
    m2 = math.sqrt(((G - 1) * M * M + 2) / (2 * G * M * M - (G - 1)))
    return p, r, t, m2


def pt_ratio(M):
    p, r, t, m2 = normal(M)
    f = lambda m: 1 + 0.5 * (G - 1) * m * m
    return p * (f(m2) / f(M)) ** (G / (G - 1))


def theta_de_beta(M, b):
    return math.atan(2 / math.tan(b) * (M * M * math.sin(b) ** 2 - 1) / (M * M * (G + math.cos(2 * b)) + 2))


def beta_debil(M, theta):
    b0 = math.asin(1 / M)
    # maximo de theta(beta): barrido fino
    mejor, bmax = -1.0, b0
    n = 20000
    for i in range(n + 1):
        b = b0 + (math.pi / 2 - b0) * i / n
        th = theta_de_beta(M, b)
        if th > mejor:
            mejor, bmax = th, b
    if theta > mejor:
        raise ValueError("deflexion mayor que la maxima")
    lo, hi = b0, bmax
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if theta_de_beta(M, mid) < theta:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), math.degrees(mejor)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Aire ILUSTRATIVO: gamma = {G}, T1 = {T1} K, p1 = {P1:.0f} Pa")
    print("Choque normal")
    print("  M1    p2/p1   rho2/rho1   T2/T1     M2     pt2/pt1    ds [J/(kg K)]  residuo")
    peor = 0.0
    for M in (1.5, 2.0, 3.0):
        p, r, t, m2 = normal(M)
        a1 = math.sqrt(G * R * T1)
        u1 = M * a1
        rho1 = P1 / (R * T1)
        t2, p2, rho2 = T1 * t, P1 * p, rho1 * r
        u2 = m2 * math.sqrt(G * R * t2)
        res = max(abs(rho2 * u2 - rho1 * u1) / (rho1 * u1),
                  abs((p2 + rho2 * u2 ** 2) - (P1 + rho1 * u1 ** 2)) / (P1 + rho1 * u1 ** 2),
                  abs((CP * t2 + 0.5 * u2 ** 2) - (CP * T1 + 0.5 * u1 ** 2)) / (CP * T1 + 0.5 * u1 ** 2))
        peor = max(peor, res)
        ds = CP * math.log(t) - R * math.log(p)
        print(f" {M:4.1f}   {p:6.4f}   {r:7.4f}    {t:7.4f}  {m2:.4f}   {pt_ratio(M):.4f}     {ds:8.3f}      {res:.1e}")
    print(f"Residuo maximo de masa, momento y energia = {peor:.2e}")
    print("Choque oblicuo, deflexion theta = 10 grados")
    print("  M1   beta debil [gr]  Mn1     M2      p2/p1    pt2/pt1   theta reconstruido [gr]  theta_max [gr]")
    th = math.radians(10.0)
    err_th = 0.0
    for M in (2.0, 3.0):
        b, thmax = beta_debil(M, th)
        mn1 = M * math.sin(b)
        p, r, t, mn2 = normal(mn1)
        m2 = mn2 / math.sin(b - th)
        # reconstruccion del giro: componente tangencial conservada
        a1 = math.sqrt(G * R * T1)
        u1 = M * a1
        ut = u1 * math.cos(b)
        un1 = u1 * math.sin(b)
        un2 = un1 / r
        giro = b - math.atan2(un2, ut)
        err_th = max(err_th, abs(math.degrees(giro) - 10.0))
        pt = pt_ratio(mn1)
        print(f" {M:4.1f}   {math.degrees(b):9.4f}    {mn1:.4f}  {m2:.4f}  {p:.4f}   {pt:.4f}      {math.degrees(giro):10.6f}          {thmax:7.3f}")
    print(f"Error maximo del giro reconstruido = {err_th:.2e} grados")
    try:
        beta_debil(2.0, math.radians(30.0))
    except ValueError:
        print("Deflexion de 30 grados a M1 = 2: sin solucion oblicua adjunta (choque desprendido)")
    assert peor < 1e-12 and err_th < 1e-9
    assert abs(normal(2.0)[0] - 4.5) < 1e-12
    print("Pruebas superadas.")


main()
