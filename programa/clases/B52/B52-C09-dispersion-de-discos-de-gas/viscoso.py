#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C09: evolucion viscosa de un disco y tiempo de dispersion con fotoevaporacion ilustrativa.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol nominal de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): alfa = 1e-3, r1 = 10 ua, M0 = 0.01 M_sol, T = 280 K (r/ua)^-0.5, mu = 2.3;
tasa de fotoevaporacion constante 1e-9 M_sol/anio (valor de ensenanza, sin fuente).
La solucion de semejanza de nu proporcional a r (Sigma = C/(3 pi nu1 r~) T^(-3/2) exp(-r~/T), M = M0 T^(-1/2)) NO se consulto:
se verifica contra la ecuacion de difusion viscosa integrada numericamente.
Sistema de referencia: disco axisimetrico, SI. Ecuacion: dSigma/dt = (3/r) d/dr[ r^(1/2) d/dr( nu Sigma r^(1/2) ) ].
Con nu = nu1 r/r1 y X = sqrt(r/r1), g = Sigma X^3 cumple dg/dt = (3 nu1/(4 r1^2)) d2g/dX2 (ecuacion del calor): se integra con Crank-Nicolson
(solucion tridiagonal) con la solucion de semejanza como condicion de borde en X = 0.1 y X = 6.
Tolerancias: error relativo maximo de Sigma en r/r1 entre 0.1 y 5: 1e-3; cambio de paso (dt y dt/2): 1e-4.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
MSOL = GM / G
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
MU, ALFA, R1_UA, M0_SOL, PE = 2.3, 1e-3, 10.0, 0.01, 1e-9


def similitud_g(X, T):
    """g = Sigma X^3 en unidades adimensionales (r1 = 1, nu1 = 1, C = 1.5)."""
    C = 1.5
    return C / (3 * math.pi) * T ** -1.5 * X * math.exp(-X * X / T)


def thomas(a, b, c, d):
    n = len(d)
    cp, dp = [0.0] * n, [0.0] * n
    cp[0], dp[0] = c[0] / b[0], d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def resolver(dt, t_fin_adim, n=1180, x0=0.1, x1=6.0):
    """Integra dg/dt = (3/4) g_XX (adimensional) con Crank-Nicolson; t adimensional = nu1 t / r1^2."""
    h = (x1 - x0) / n
    X = [x0 + i * h for i in range(n + 1)]
    ts = 1.0 / 3.0
    g = [similitud_g(x, 1.0) for x in X]
    k = 0.75 * dt / h ** 2
    pasos = int(round(t_fin_adim / dt))
    for s in range(pasos):
        t_nuevo = (s + 1) * dt
        T = 1.0 + t_nuevo / ts
        gl, gr = similitud_g(X[0], T), similitud_g(X[-1], T)
        m = n - 1
        a = [-k / 2] * m; b = [1 + k] * m; c = [-k / 2] * m
        d = [g[i] + k / 2 * (g[i - 1] - 2 * g[i] + g[i + 1]) for i in range(1, n)]
        d[0] += k / 2 * gl
        d[-1] += k / 2 * gr
        sol = thomas(a, b, c, d)
        g = [gl] + sol + [gr]
    return X, g


def calcular():
    t_fin = 0.5
    X, g1 = resolver(1e-3, t_fin)
    _, g2 = resolver(5e-4, t_fin)
    T = 1.0 + t_fin / (1.0 / 3.0)
    err = 0.0
    dif = 0.0
    for x, a, b in zip(X, g1, g2):
        r = x * x
        if 0.1 <= r <= 5.0:
            ex = similitud_g(x, T)
            err = max(err, abs(a / ex - 1.0))
            dif = max(dif, abs(a / b - 1.0))
    # masa del disco: M = 2 pi integral Sigma r dr = 4 pi integral g dX / X^... (Sigma r dr = g/X^3 * X^2 * 2X dX = 2 g dX)
    h = X[1] - X[0]
    masa = 4 * math.pi * sum(0.5 * (g1[i] + g1[i + 1]) * h for i in range(len(X) - 1))
    masa_an = T ** -0.5
    # dimensional
    r1 = R1_UA * UA
    cs = math.sqrt(K_B * 280.0 * R1_UA ** -0.5 / (MU * M_P))
    om = math.sqrt(GM / r1 ** 3)
    nu1 = ALFA * cs * cs / om
    t_nu = r1 ** 2 / nu1
    t_s = t_nu / 3.0
    mdot0 = M0_SOL * MSOL / (2.0 * t_s)  # kg/s
    pe = PE * MSOL / ANIO
    # Mdot(t) = Mdot0 T^(-3/2) ; iguala a pe en T = (mdot0/pe)^(2/3)
    Tc = (mdot0 / pe) ** (2.0 / 3.0)
    t_clear = t_s * (Tc - 1.0)
    return dict(err=err, dif=dif, T=T, masa=masa, masa_an=masa_an, nu1=nu1, t_nu=t_nu, t_s=t_s, mdot0=mdot0 * ANIO / MSOL, Tc=Tc, t_clear=t_clear,
                mc=M0_SOL * Tc ** -0.5, cs=cs)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Disco sintetico: alfa = {ALFA}, r1 = {R1_UA} ua, M0 = {M0_SOL} M_sol ; c_s(r1) = {r['cs']:.1f} m/s ; nu1 = {r['nu1']:.3e} m^2/s")
    print(f"Escala viscosa t_nu = r1^2/nu1 = {r['t_nu'] / ANIO:.3e} anios ; t_s = t_nu/3 = {r['t_s'] / ANIO:.3e} anios ; Mdot inicial = {r['mdot0']:.3e} M_sol/anio")
    print(f"Ecuacion de difusion (Crank-Nicolson) a T = 1 + t/t_s = {r['T']:.4f}: error relativo maximo de Sigma (0.1 < r/r1 < 5) = {r['err']:.2e} ; cambio de paso = {r['dif']:.2e}")
    print(f"Masa del disco: numerica = {r['masa']:.5f} M0 ; semejanza T^(-1/2) = {r['masa_an']:.5f} M0 (la diferencia refleja el borde interior en r/r1 = 0.01)")
    print(f"Fotoevaporacion ilustrativa {PE:.0e} M_sol/anio: Mdot viscoso la iguala en T = {r['Tc']:.3f}, t = {r['t_clear'] / ANIO:.3e} anios, con {r['mc'] / M0_SOL:.3f} de la masa inicial")
    assert r["err"] < 1e-3 and r["dif"] < 1e-4
    assert abs(r["masa"] / r["masa_an"] - 1) < 2e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
