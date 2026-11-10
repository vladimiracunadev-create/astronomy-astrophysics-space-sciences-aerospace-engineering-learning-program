#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C12: optimizacion del tiempo de vuelo Tierra-Marte con Lambert (modelo circular y coplanar).

Datos consultados (2026-11-10): semiejes y periodo sideral de Marte (686.980 d) de las fichas NASA/NSSDC (Tierra 149.598e6 km, Marte 227.956e6 km). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
ILUSTRATIVO: la fase de Marte a la salida (adelanto sobre la Tierra) se elige entre 20 y 70 grados; la Tierra sale del angulo 0.
Funcion de costo: suma de excesos hiperbolicos (v_inf de salida + v_inf de llegada) en km/s, sin las maniobras de salida y captura planetocentricas (C09).
Metodo: barrido de TOF de 100 a 420 d con paso de 1 d y refinamiento por seccion aurea +/- 1 d. Solo trayectoria directa de menos de una revolucion.
Pruebas: (1) con fase 44.0 grados el costo minimo difiere menos de 3 % de la suma de Hohmann (5.5944 km/s); (2) el refinamiento no empeora el barrido (tol. 1e-12);
(3) para cada fase el optimo es un minimo local del barrido (los dos vecinos de 1 d cuestan mas o igual).
"""
import math, platform
MU = 1.32712440e11
RE_, RM_ = 149.598e6, 227.956e6
PM = 686.980
VE, VM = math.sqrt(MU / RE_), math.sqrt(MU / RM_)
# --- Utilidades de dos cuerpos (todas en km, s, km/s) ---
def _stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def kepler_prop(r0, v0, dt, mu):
    """Propaga (r0, v0) durante dt con variables universales (Curtis, alg. 3.4); r0, v0 listas de 3."""
    r0n = math.sqrt(sum(x * x for x in r0)); vr0 = sum(a * b for a, b in zip(r0, v0)) / r0n
    alpha = 2 / r0n - sum(x * x for x in v0) / mu
    sm = math.sqrt(mu)
    if alpha > 0: x = sm * alpha * dt
    elif alpha < 0:
        a_ = 1 / alpha; sg = 1.0 if dt >= 0 else -1.0
        rv = sum(p * q for p, q in zip(r0, v0))
        x = sg * math.sqrt(-a_) * math.log((-2 * mu * alpha * dt) / (rv + sg * math.sqrt(-mu * a_) * (1 - r0n * alpha)))
    else: x = sm * dt / r0n
    for _ in range(200):
        z = alpha * x * x; C, S = _stumpff(z)
        F = r0n * vr0 / sm * x * x * C + (1 - alpha * r0n) * x**3 * S + r0n * x - sm * dt
        dF = r0n * vr0 / sm * x * (1 - z * S) + (1 - alpha * r0n) * x * x * C + r0n
        dx = F / dF; x -= dx
        if abs(dx) < 1e-12 * max(1.0, abs(x)): break
    z = alpha * x * x; C, S = _stumpff(z)
    f = 1 - x * x / r0n * C; g = dt - x**3 / sm * S
    r = [f * a + g * b for a, b in zip(r0, v0)]; rn = math.sqrt(sum(q * q for q in r))
    fd = sm / (rn * r0n) * (z * S - 1) * x; gd = 1 - x * x / rn * C
    v = [fd * a + gd * b for a, b in zip(r0, v0)]
    return r, v


def rk4_dosc(r, v, dt, n, mu):
    """Integra el problema de dos cuerpos con RK4 de paso fijo (n pasos de dt)."""
    def acc(p):
        d = math.sqrt(sum(q * q for q in p)); return [-mu * q / d**3 for q in p]
    r = list(r); v = list(v)
    for _ in range(n):
        k1v = acc(r); k1r = v
        r2 = [a + 0.5 * dt * b for a, b in zip(r, k1r)]; v2 = [a + 0.5 * dt * b for a, b in zip(v, k1v)]
        k2v = acc(r2); k2r = v2
        r3 = [a + 0.5 * dt * b for a, b in zip(r, k2r)]; v3 = [a + 0.5 * dt * b for a, b in zip(v, k2v)]
        k3v = acc(r3); k3r = v3
        r4 = [a + dt * b for a, b in zip(r, k3r)]; v4 = [a + dt * b for a, b in zip(v, k3v)]
        k4v = acc(r4); k4r = v4
        r = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(r, k1r, k2r, k3r, k4r)]
        v = [a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(v, k1v, k2v, k3v, k4v)]
    return r, v

def lambert(r1, r2, tof, mu, prograde=True):
    """Problema de Lambert por variables universales (Curtis, alg. 5.2). r1, r2 en km; tof en s. Devuelve (v1, v2) en km/s."""
    n1 = math.sqrt(sum(x * x for x in r1)); n2 = math.sqrt(sum(x * x for x in r2))
    cosd = sum(a * b for a, b in zip(r1, r2)) / (n1 * n2)
    cz = r1[0] * r2[1] - r1[1] * r2[0]
    d = math.acos(max(-1.0, min(1.0, cosd)))
    if prograde: d = d if cz >= 0 else 2 * math.pi - d
    else: d = d if cz < 0 else 2 * math.pi - d
    A = math.sin(d) * math.sqrt(n1 * n2 / (1 - math.cos(d)))
    def y(z):
        C, S = _stumpff(z); return n1 + n2 + A * (z * S - 1) / math.sqrt(C)
    def F(z):
        C, S = _stumpff(z); yy = y(z)
        return (yy / C) ** 1.5 * S + A * math.sqrt(yy) - math.sqrt(mu) * tof
    lo, hi = -4 * math.pi**2 + 1e-6, 4 * math.pi**2 - 1e-6
    while y(lo) < 0 or (not math.isfinite(F(lo))): lo += 0.1
    if F(lo) > 0: raise ValueError("tof demasiado corto para este arco")
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if y(mid) < 0 or F(mid) < 0: lo = mid
        else: hi = mid
    z = 0.5 * (lo + hi); yy = y(z)
    f = 1 - yy / n1; g = A * math.sqrt(yy / mu); gd = 1 - yy / n2
    v1 = [(b - f * a) / g for a, b in zip(r1, r2)]
    v2 = [(gd * b - a) / g for a, b in zip(r1, r2)]
    return v1, v2



def costo(phi_deg, tof_d):
    th = math.radians(phi_deg) + 2 * math.pi * tof_d / PM
    r1 = [RE_, 0.0, 0.0]; r2 = [RM_ * math.cos(th), RM_ * math.sin(th), 0.0]
    try:
        v1, v2 = lambert(r1, r2, tof_d * 86400.0, MU)
    except Exception:
        return 1e9
    d1 = math.hypot(v1[0], v1[1] - VE)
    t2 = [-math.sin(th), math.cos(th)]
    d2 = math.hypot(v2[0] - VM * t2[0], v2[1] - VM * t2[1])
    return d1 + d2


def optimiza(phi):
    mejor = min(((costo(phi, t), t) for t in range(100, 421)), key=lambda x: x[0])
    lo, hi = mejor[1] - 1.0, mejor[1] + 1.0
    g = (math.sqrt(5) - 1) / 2
    for _ in range(60):
        c = hi - g * (hi - lo); d = lo + g * (hi - lo)
        if costo(phi, c) < costo(phi, d): hi = d
        else: lo = c
    t = 0.5 * (lo + hi)
    return mejor, (costo(phi, t), t)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    at = 0.5 * (RE_ + RM_)
    hoh = (math.sqrt(MU * (2 / RE_ - 1 / at)) - VE) + (VM - math.sqrt(MU * (2 / RM_ - 1 / at)))
    tH = math.pi * math.sqrt(at**3 / MU) / 86400
    print(f"Referencia de Hohmann: suma de excesos = {hoh:.4f} km/s ; TOF = {tH:.2f} d")
    print(" fase [grados]   TOF optimo [d]   suma optima [km/s]   suma con TOF de Hohmann [km/s]   exceso sobre Hohmann [%]")
    res = {}
    for phi in (20.0, 30.0, 40.0, 44.0, 50.0, 60.0, 70.0):
        mejor, (c, t) = optimiza(phi)
        assert c <= mejor[0] + 1e-12
        assert costo(phi, round(mejor[1]) - 1) >= mejor[0] and costo(phi, round(mejor[1]) + 1) >= mejor[0]
        ch = costo(phi, tH)
        res[phi] = c
        print(f"{phi:10.1f} {t:16.2f} {c:20.4f} {ch:26.4f} {100*(c-hoh)/hoh:24.2f}")
    assert abs(res[44.0] - hoh) / hoh < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
