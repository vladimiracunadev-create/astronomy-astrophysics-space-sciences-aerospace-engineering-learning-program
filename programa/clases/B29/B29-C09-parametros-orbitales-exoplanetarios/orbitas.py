#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C09: parametros orbitales de un exoplaneta: densidad estelar desde el tránsito y ajuste kepleriano de velocidad radial.

Datos: G (NIST CODATA 2022), GM_sol y R_sol (IAU 2015 B3), 1 au (IERS TN36), consultados 2026-11-09. Los parametros del planeta sintetico (P = 30 d, K = 20 m/s,
e = 0.4, omega = 1.0 rad), el ruido (1 m/s) y el numero de medidas (50) son ILUSTRATIVOS.
Modelo: (1) densidad estelar desde el tránsito: rho_* = 3 pi (a/Rs)^3/(G P^2) (con Mp << Ms); comprobacion con el Sol y la Tierra a partir de GM y R nominales;
(2) ajuste kepleriano de la curva de velocidad radial con parametros (K, h = sqrt(e) cos(omega), k = sqrt(e) sen(omega), M0) mediante Nelder-Mead con varios inicios
(el periodo se supone conocido); error por Monte Carlo (semilla fija).
Supuestos: un solo planeta, periodo conocido. Validez: ilustrativa.
Tolerancia: la densidad solar a partir de a/Rs debe coincidir con 3 GM/(4 pi G Rs^3) a 1e-3; e recuperada con sesgo menor que 3 errores de la media.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

G = 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
AU = 1.49597870700e11
DIA = 86400.0


def kepler(m_anom, e):
    ea = m_anom if e < 0.8 else math.pi
    for _ in range(100):
        d = (ea - e * math.sin(ea) - m_anom) / (1 - e * math.cos(ea))
        ea -= d
        if abs(d) < 1e-14:
            break
    return ea


def vr(t, p, k, e, om, m0):
    m = (2 * math.pi * t / p + m0) % (2 * math.pi)
    ea = kepler(m, e)
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(ea / 2), math.sqrt(1 - e) * math.cos(ea / 2))
    return k * (math.cos(nu + om) + e * math.cos(om))


def nelder_mead(f, x0, paso, iters=500):
    n = len(x0)
    pts = [list(x0)] + [[x0[j] + (paso[j] if j == i else 0) for j in range(n)] for i in range(n)]
    vals = [f(p) for p in pts]
    for _ in range(iters):
        orden = sorted(range(n + 1), key=lambda i: vals[i])
        pts, vals = [pts[i] for i in orden], [vals[i] for i in orden]
        c = [sum(pts[i][j] for i in range(n)) / n for j in range(n)]
        xr = [c[j] + (c[j] - pts[-1][j]) for j in range(n)]
        fr = f(xr)
        if fr < vals[0]:
            xe = [c[j] + 2 * (c[j] - pts[-1][j]) for j in range(n)]
            fe = f(xe)
            pts[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = [c[j] + 0.5 * (pts[-1][j] - c[j]) for j in range(n)]
            fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n + 1):
                    pts[i] = [pts[0][j] + 0.5 * (pts[i][j] - pts[0][j]) for j in range(n)]
                    vals[i] = f(pts[i])
    i = min(range(n + 1), key=lambda i: vals[i])
    return pts[i], vals[i]


def ajustar(ts, vs, p, rng):
    def chi2(q):
        k, h, kk, m0 = q
        e = h * h + kk * kk
        if k <= 0 or e >= 0.95:
            return 1e30
        om = math.atan2(kk, h)
        return sum((v - vr(t, p, k, e, om, m0)) ** 2 for t, v in zip(ts, vs))
    mejor = (1e31, None)
    amp = (max(vs) - min(vs)) / 2
    for _ in range(6):
        x0 = [amp, rng.uniform(-0.6, 0.6), rng.uniform(-0.6, 0.6), rng.uniform(0, 2 * math.pi)]
        q, v = nelder_mead(chi2, x0, [amp * 0.2, 0.2, 0.2, 0.8])
        if v < mejor[0]:
            mejor = (v, q)
    k, h, kk, m0 = mejor[1]
    return k, h * h + kk * kk, math.atan2(kk, h)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    gm_t = 3.986004e14
    rho_sol = 3 * GM_SOL / (4 * math.pi * G * R_SOL ** 3)
    # densidad estelar desde a/Rs y P para la Tierra (a de la tercera ley)
    p_t = 365.25 * DIA
    a_t = (GM_SOL * (p_t / (2 * math.pi)) ** 2) ** (1 / 3)
    rho_tr = 3 * math.pi * (a_t / R_SOL) ** 3 / (G * p_t ** 2)
    print(f"a de la Tierra (tercera ley) = {a_t / AU:.6f} au ; a/Rs = {a_t / R_SOL:.3f}")
    print(f"densidad solar: 3 GM/(4 pi G Rs^3) = {rho_sol:.2f} kg/m3 ; desde a/Rs y P = {rho_tr:.2f} kg/m3 ; cociente = {rho_tr / rho_sol:.6f}")
    assert abs(rho_tr / rho_sol - 1) < 1e-3, "densidad estelar desde el transito"
    print(f"{'a/Rs':>7} {'P [d]':>8} {'rho_* [kg/m3]':>14} {'rho_*/rho_sol':>14}")
    for ars, pd in ((215.0, 365.25), (10.0, 3.0), (5.0, 1.0), (30.0, 20.0)):
        p = pd * DIA
        rho = 3 * math.pi * ars ** 3 / (G * p * p)
        print(f"{ars:7.1f} {pd:8.2f} {rho:14.2f} {rho / rho_sol:14.3f}")
    # ajuste kepleriano
    rng = random.Random(20261109)
    p, k0, e0, om0, sig, n = 30 * DIA, 20.0, 0.4, 1.0, 1.0, 50
    ts = [rng.uniform(0, 4 * p) for _ in range(n)]
    res = []
    for _ in range(40):
        vs = [vr(t, p, k0, e0, om0, 0.7) + rng.gauss(0, sig) for t in ts]
        res.append(ajustar(ts, vs, p, rng))
    nombres = ["K [m/s]", "e", "omega [rad]"]
    verd = [k0, e0, om0]
    print(f"{'parametro':<12} {'verdadero':>10} {'media':>9} {'desviacion':>11}")
    for i in range(3):
        col = [r[i] for r in res]
        mm, ss = statistics.mean(col), statistics.pstdev(col)
        print(f"{nombres[i]:<12} {verd[i]:10.4f} {mm:9.4f} {ss:11.4f}")
        assert abs(mm - verd[i]) < 3 * ss / math.sqrt(len(res)) * 3 + 0.02, nombres[i]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
