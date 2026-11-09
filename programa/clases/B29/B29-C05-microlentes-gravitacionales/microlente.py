#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C05: radio de Einstein, magnificacion de una microlente y ajuste de sus parametros.

Datos: G, c (NIST CODATA 2022), GM_sol (IAU 2015 B3) y 1 au (IERS TN36), consultados 2026-11-09; 1 pc = 648000/pi au. Contexto: una microlente ocurre cuando
una estrella de primer plano pasa por la visual de una de fondo y magnifica su luz (Gaudi, arXiv:1002.0332, resumen, consultado 2026-11-09). La masa de la lente
(0.3 Msol), las distancias (4 y 8 kpc), la velocidad relativa, el ruido (2 %) y los parametros del evento (t0 = 100 d, u0 = 0.3, tE = 30 d) son ILUSTRATIVOS.
Modelo: theta_E = sqrt(4 G M/c^2 (D_S - D_L)/(D_L D_S)); u(t) = sqrt(u0^2 + ((t - t0)/tE)^2); A(u) = (u^2 + 2)/(u sqrt(u^2 + 4)); flujo F = F_s A + F_b
(sin mezcla F_b = 0). Ajuste de (t0, u0, tE) minimizando chi^2 con Nelder-Mead; incertidumbre por Monte Carlo (semilla fija). Perturbacion de un planeta:
duracion t_p ~ tE sqrt(q), q = Mp/M.
Supuestos: lente puntual, fuente puntual, sin paralaje ni movimiento orbital. Validez: ilustrativa.
Tolerancia: A(1) = 3/sqrt(5) a 1e-12; parametros recuperados dentro de 3 errores del Monte Carlo.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
AU = 1.49597870700e11
PC = 648000 / math.pi * AU
MAS = math.pi / (180 * 3600 * 1000)


def theta_e(m_kg, dl, ds):
    return math.sqrt(4 * G * m_kg / C ** 2 * (ds - dl) / (dl * ds))


def amp(u):
    return (u * u + 2) / (u * math.sqrt(u * u + 4))


def u_de_t(t, t0, u0, te):
    return math.sqrt(u0 * u0 + ((t - t0) / te) ** 2)


def nelder_mead(f, x0, paso, iters=600):
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


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert abs(amp(1.0) - 3 / math.sqrt(5)) < 1e-12
    print(f"A(u = 1) = {amp(1.0):.6f} (3/sqrt 5 = {3 / math.sqrt(5):.6f}) ; A(0.3) = {amp(0.3):.4f} ; A(0.1) = {amp(0.1):.4f}")
    m = 0.3 * GM_SOL / G
    dl, ds = 4000 * PC, 8000 * PC
    th = theta_e(m, dl, ds)
    re = th * dl
    print(f"M = 0.3 Msol, D_L = 4 kpc, D_S = 8 kpc: theta_E = {th / MAS:.4f} mas ; R_E en la lente = {re / AU:.3f} au")
    v = 200e3     # velocidad relativa ilustrativa 200 km/s
    te_dias = re / v / 86400
    print(f"con velocidad relativa de 200 km/s: tE = {te_dias:.1f} d")
    for q in (1e-3, 1e-4, 3e-6):
        print(f"planeta con q = {q:g}: duracion de la perturbacion ~ tE sqrt(q) = {30 * math.sqrt(q):.3f} d (tE = 30 d)")
    # ajuste
    rng = random.Random(20261109)
    t0, u0, te, sig = 100.0, 0.3, 30.0, 0.02
    ts = [40 + 0.8 * i for i in range(175)]
    verd = (t0, u0, te)
    est = []
    for _ in range(200):
        fl = [amp(u_de_t(t, t0, u0, te)) * (1 + sig * rng.gauss(0, 1)) for t in ts]
        def chi2(p):
            if p[1] <= 1e-3 or p[2] <= 1:
                return 1e30
            return sum(((f - amp(u_de_t(t, p[0], p[1], p[2]))) / (sig * f)) ** 2 for t, f in zip(ts, fl))
        mejor, _ = nelder_mead(chi2, [98.0, 0.4, 25.0], [3.0, 0.1, 5.0])
        est.append(mejor)
    nombres = ["t0 [d]", "u0", "tE [d]"]
    print(f"{'parametro':<8} {'verdadero':>10} {'media':>9} {'desviacion':>11}")
    for i in range(3):
        col = [e[i] for e in est]
        mm, ss = statistics.mean(col), statistics.pstdev(col)
        print(f"{nombres[i]:<8} {verd[i]:10.4f} {mm:9.4f} {ss:11.4f}")
        assert abs(mm - verd[i]) < 3 * ss / math.sqrt(len(est)) * 3 + 1e-3, nombres[i]
    print(f"correlacion u0-tE en las 200 realizaciones: {statistics.correlation([e[1] for e in est], [e[2] for e in est]):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
