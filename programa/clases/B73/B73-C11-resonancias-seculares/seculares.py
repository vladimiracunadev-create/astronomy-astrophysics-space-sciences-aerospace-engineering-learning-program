#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C11: teoria secular de Laplace-Lagrange para Jupiter y Saturno (dos planetas, orden bajo en e e I).

Datos consultados (2026-11-10): GM del Sol 132 712 x 10^6 km3/s2 (NASA/NSSDC, Sun Fact Sheet); GM de Jupiter 126.687 x 10^6 km3/s2
(Jupiter Fact Sheet); masa de Saturno 568.32 x 10^24 kg (Saturn Fact Sheet) y G = 6.67430e-11 (CODATA 2018, citada en el registro de cambios del JPL) -> GM_Saturno ~ 3.793e7 km3/s2;
distancias al Sol 778.5 x 10^6 km y 1432.0 x 10^6 km, excentricidades 0.049 (Jupiter, 0.0487 en su ficha) y 0.052 (Saturno) (NASA/NSSDC, Planetary Fact Sheet, 2025-03-18).
SINTETICO: longitudes del perihelio iniciales (0 y 90 grados) y excentricidades iniciales tomadas de las fichas como punto de partida; no es el estado real de ninguna epoca.
Modelo: teoria lineal de Laplace-Lagrange (coeficientes de Laplace b_{3/2}^{(1)}, b_{3/2}^{(2)} por integracion numerica); no consultada en su fuente: se verifica
con (a) simetria de la matriz con pesos, (b) conservacion del deficit de momento angular sum m (1+m) sqrt(a) e^2 y (c) integracion numerica RK4 del sistema lineal frente a la solucion por modos.
Particula de prueba: g(a) = n(a)/4 sum m_k alpha_k^2 b1(alpha_k), resonancia donde g(a) = g1 (biseccion frente a secante).
Tolerancias: simetria < 1e-12 relativo; deficit de momento angular < 1e-9; modos frente a RK4 < 1e-6.
"""
from __future__ import annotations
import json, math, platform, sys

GM_S, GM_J = 132712e6, 126.687e6
GM_SAT = 6.67430e-11 * 568.32e24 / 1e9  # km3/s2
A_J, A_SAT = 778.5e6, 1432.0e6
E0 = [0.049, 0.052]
SEG_AO = 365.25 * 86400.0
ARC = 180.0 / math.pi * 3600.0


def laplace_b(s, j, alpha, n=20000):
    t = 0.0
    for k in range(n):
        psi = 2 * math.pi * (k + 0.5) / n
        t += math.cos(j * psi) / (1 - 2 * alpha * math.cos(psi) + alpha * alpha) ** s
    return 2 * t / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a = [A_J, A_SAT]
    gm = [GM_J, GM_SAT]
    m = [g / GM_S for g in gm]
    n = [math.sqrt(GM_S / ai**3) for ai in a]  # rad/s
    al = a[0] / a[1]
    b1, b2 = laplace_b(1.5, 1, al), laplace_b(1.5, 2, al)
    print(f"alpha = a_J/a_S = {al:.5f} ; b_(3/2)^(1) = {b1:.5f} ; b_(3/2)^(2) = {b2:.5f}")
    print(f"GM_Saturno (deducido) = {GM_SAT:.4e} km3/s2 ; m_J/M = {m[0]:.5e} ; m_S/M = {m[1]:.5e} ; n_J = {n[0] * SEG_AO * 180 / math.pi:.3f} grados/ano ; n_S = {n[1] * SEG_AO * 180 / math.pi:.3f} grados/ano")
    # matrices A (excentricidades) y B (inclinaciones), en rad/s
    A = [[0.0, 0.0], [0.0, 0.0]]
    B = [[0.0, 0.0], [0.0, 0.0]]
    # j = 0 interior (alpha_jk = alpha, alpha_bar = alpha); j = 1 exterior (alpha_jk = alpha, alpha_bar = 1)
    c0 = n[0] / 4 * m[1] / (1 + m[0]) * al * al
    c1 = n[1] / 4 * m[0] / (1 + m[1]) * al * 1.0
    A[0][0], A[0][1] = c0 * b1, -c0 * b2
    A[1][1], A[1][0] = c1 * b1, -c1 * b2
    B[0][0], B[0][1] = -c0 * b1, c0 * b1
    B[1][1], B[1][0] = -c1 * b1, c1 * b1
    # simetria con pesos w_j = m_j (1 + m_j) sqrt(a_j) : w_0 A01 = w_1 A10
    w = [m[i] * (1 + m[i]) * math.sqrt(a[i]) for i in range(2)]
    sim = abs(w[0] * A[0][1] - w[1] * A[1][0]) / abs(w[0] * A[0][1])
    simB = abs(w[0] * B[0][1] - w[1] * B[1][0]) / abs(w[0] * B[0][1])
    print(f"Simetria con pesos m(1+m) sqrt(a): A {sim:.1e} ; B {simB:.1e}")

    def autoval(M):
        tr, det = M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]
        d = math.sqrt(tr * tr / 4 - det)
        return tr / 2 + d, tr / 2 - d
    g = autoval(A)
    f = autoval(B)
    conv = SEG_AO * ARC  # rad/s -> arcsec/ano
    print(f"Frecuencias propias de excentricidad: g1 = {g[0] * conv:.3f} \"/ano (periodo {360 * 3600 / (g[0] * conv):,.0f} anos) ; g2 = {g[1] * conv:.3f} \"/ano (periodo {360 * 3600 / (g[1] * conv):,.0f} anos)")
    print(f"Frecuencias propias de inclinacion: f1 = {f[0] * conv:.3f} \"/ano ; f2 = {f[1] * conv:.3f} \"/ano (el modo nulo es el plano invariable)")
    # evolucion de z_j = e_j exp(i varpi_j): dz/dt = i A z ; RK4 frente a modos
    z0 = [E0[0] * complex(1, 0), E0[1] * complex(0, 1)]  # varpi_J = 0, varpi_S = 90 grados (sinteticos)
    dt = 10.0 * SEG_AO
    T = 200000.0 * SEG_AO
    def deriv(z):
        return [1j * (A[0][0] * z[0] + A[0][1] * z[1]), 1j * (A[1][0] * z[0] + A[1][1] * z[1])]
    z = list(z0)
    amd0 = sum(w[i] * abs(z[i]) ** 2 for i in range(2))
    emin, emax, damd = [9.0, 9.0], [0.0, 0.0], 0.0
    for k in range(int(T / dt)):
        k1 = deriv(z)
        k2 = deriv([z[i] + 0.5 * dt * k1[i] for i in range(2)])
        k3 = deriv([z[i] + 0.5 * dt * k2[i] for i in range(2)])
        k4 = deriv([z[i] + dt * k3[i] for i in range(2)])
        z = [z[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(2)]
        if k % 100 == 0:
            for i in range(2):
                emin[i], emax[i] = min(emin[i], abs(z[i])), max(emax[i], abs(z[i]))
            damd = max(damd, abs(sum(w[i] * abs(z[i]) ** 2 for i in range(2)) / amd0 - 1))
    # solucion por modos
    vec = []
    for gk in g:
        # (A - gk I) v = 0 -> v = (A01, gk - A00)
        v = [A[0][1], gk - A[0][0]]
        nrm = math.hypot(*v)
        vec.append([v[0] / nrm, v[1] / nrm])
    # resolver z0 = c0 v0 + c1 v1 (reales en la base)
    det = vec[0][0] * vec[1][1] - vec[0][1] * vec[1][0]
    c = [(z0[0] * vec[1][1] - z0[1] * vec[1][0]) / det, (vec[0][0] * z0[1] - vec[0][1] * z0[0]) / det]
    zT = [sum(c[k] * vec[k][i] * complex(math.cos(g[k] * T), math.sin(g[k] * T)) for k in range(2)) for i in range(2)]
    dmod = max(abs(zT[i] - z[i]) for i in range(2)) / max(abs(zT[i]) for i in range(2))
    print(f"Deficit de momento angular (m(1+m) sqrt(a) e^2): variacion relativa maxima en 200 000 anos = {damd:.1e}")
    print(f"Modos frente a RK4 en t = 200 000 anos: diferencia relativa = {dmod:.1e}")
    print(f"Rango de e (condiciones sinteticas, modelo lineal): Jupiter {emin[0]:.4f}-{emax[0]:.4f} ; Saturno {emin[1]:.4f}-{emax[1]:.4f}")
    # particula de prueba interior: g(a) = n(a)/4 sum_k m_k alpha_k^2 b1(alpha_k); donde g(a) = g_i hay resonancia secular
    AU = 149.6e6
    def g_test(a_km):
        nn = math.sqrt(GM_S / a_km**3)
        tot = 0.0
        for k in range(2):
            alk = a_km / a[k]
            tot += m[k] * alk * alk * laplace_b(1.5, 1, alk, 4000)
        return nn / 4 * tot * conv
    print("Precesion de una particula de prueba interior (Jupiter y Saturno, modelo lineal): a [UA] -> g [\"/ano]")
    tab = {}
    for au in (1.5, 2.0, 2.5, 3.0, 3.5):
        tab[au] = g_test(au * AU)
        print(f"  {au:.1f} -> {tab[au]:.3f}")
    def resolver(objetivo):
        lo, hi = 1.5 * AU, 3.5 * AU
        if (g_test(lo) - objetivo) * (g_test(hi) - objetivo) > 0:
            return None
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if (g_test(lo) - objetivo) * (g_test(mid) - objetivo) <= 0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi) / AU
    ares = resolver(g[0] * conv)
    # segunda via: secante
    x0, x1 = 2.0 * AU, 2.5 * AU
    for _ in range(40):
        f0, f1 = g_test(x0) - g[0] * conv, g_test(x1) - g[0] * conv
        if abs(f1 - f0) < 1e-15:
            break
        x0, x1 = x1, x1 - f1 * (x1 - x0) / (f1 - f0)
    asec = x1 / AU
    print(f"Resonancia g(a) = g1 = {g[0] * conv:.3f} \"/ano: a = {ares:.4f} UA (biseccion) ; {asec:.4f} UA (secante) ; diferencia = {abs(ares - asec):.1e} UA")
    assert abs(ares - asec) < 1e-6
    assert sim < 1e-12 and simB < 1e-12 and damd < 1e-9 and dmod < 1e-6 and abs(f[0]) < 1e-12 * conv
    print("Pruebas superadas.")
    out = {"python": platform.python_version(), "al": al, "b1": b1, "b2": b2, "gmsat": GM_SAT, "g1": g[0] * conv, "g2": g[1] * conv,
           "P1": 360 * 3600 / (g[0] * conv), "P2": 360 * 3600 / (g[1] * conv), "f2": f[1] * conv, "f1": f[0] * conv, "sim": sim, "simB": simB, "damd": damd, "dmod": dmod,
           "ejmin": emin[0], "ejmax": emax[0], "esmin": emin[1], "esmax": emax[1], "mj": m[0], "ms": m[1],
           "ares": ares, "asec": asec, "g15": tab[1.5], "g20": tab[2.0], "g25": tab[2.5], "g30": tab[3.0], "g35": tab[3.5], "nj": n[0] * SEG_AO * 180 / math.pi, "ns": n[1] * SEG_AO * 180 / math.pi}
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
