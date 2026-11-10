#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C05: transferencia bi-eliptica frente a Hohmann entre orbitas circulares coplanares.

Modelo adimensional: v en unidades de la velocidad circular inicial (r1 = 1, mu = 1); R = r2/r1; rb = radio del apoapsis intermedio.
Datos de aplicacion: semiejes de las fichas NASA/NSSDC consultadas el 2026-11-10 (Tierra 149.598e6 km, Jupiter 778.479e6 km);
GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado). Los cocientes de cruce 11.94 y 15.58 son resultados clasicos que aqui se RECALCULAN, no se citan.
Pruebas: (1) la velocidad en el apoapsis por vis-viva iguala la de una propagacion de Kepler (tol. 1e-9);
(2) la raiz R* (rb -> infinito) y la R** (rb apenas mayor que R) por biseccion, y R* verificada ademas por un barrido de R con paso 1e-3 (tol. 5e-3).
"""
import math, platform
MU1 = 1.32712440e11
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



def dv_hohmann(R):
    return (math.sqrt(2 * R / (1 + R)) - 1) + (math.sqrt(1 / R) - math.sqrt(2 / (R * (1 + R))))


def dv_bielip(R, rb):
    a1 = 0.5 * (1 + rb); a2 = 0.5 * (R + rb)
    d1 = math.sqrt(2 / 1 - 1 / a1) - 1
    d2 = math.sqrt(2 / rb - 1 / a2) - math.sqrt(2 / rb - 1 / a1)
    d3 = math.sqrt(2 / R - 1 / a2) - math.sqrt(1 / R)
    return abs(d1) + abs(d2) + abs(d3)


def bisec(f, lo, hi):
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(lo) * f(m) <= 0: hi = m
        else: lo = m
    return 0.5 * (lo + hi)


def tof_bielip(R, rb):
    a1 = 0.5 * (1 + rb); a2 = 0.5 * (R + rb)
    return math.pi * (math.sqrt(a1**3) + math.sqrt(a2**3))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Delta-v total (unidades de la velocidad circular inicial):")
    print("   R    Hohmann   bi-eliptica rb=20R   bi-eliptica rb=1e6   mejor")
    for R in (5.2, 11.0, 12.0, 15.0, 15.6, 20.0, 50.0):
        h = dv_hohmann(R); b1 = dv_bielip(R, 20 * R); b2 = dv_bielip(R, 1e6)
        mej = "Hohmann" if h <= min(b1, b2) else "bi-eliptica"
        print(f"{R:6.2f} {h:9.5f} {b1:14.5f} {b2:20.5f}   {mej}")
    Rs = bisec(lambda R: dv_hohmann(R) - dv_bielip(R, 1e12), 5.0, 14.0)
    Rb = bisec(lambda R: dv_hohmann(R) - dv_bielip(R, R * (1 + 1e-6)), 13.0, 20.0)
    print(f"Cruce con rb -> infinito (Hohmann = bi-eliptica): R* = {Rs:.4f}")
    print(f"Desde R** toda rb finita mayor que R mejora a Hohmann (rb = R(1+1e-6)): R** = {Rb:.3f}")
    R = 20.0; rb = 100.0
    a1 = 0.5 * (1 + rb)
    r, v = kepler_prop([1.0, 0, 0], [0, math.sqrt(2 - 1 / a1), 0], math.pi * a1**1.5, 1.0)
    vap = math.hypot(*v)
    assert abs(math.hypot(*r) - rb) < 1e-7 and abs(vap - math.sqrt(2 / rb - 1 / a1)) < 1e-9
    print(f"Prueba 1: apoapsis de la 1.a elipse por Kepler r = {math.hypot(*r):.6f} (esperado {rb}), v = {vap:.9f}")
    RE, RJ = 149.598e6, 778.479e6
    R = RJ / RE
    vE = math.sqrt(MU1 / RE)
    print(f"Tierra->Jupiter (R = {R:.3f}): Hohmann = {dv_hohmann(R)*vE:.3f} km/s ; bi-eliptica rb = 20R = {dv_bielip(R, 20*R)*vE:.3f} km/s")
    tH = math.pi * math.sqrt((0.5 * (RE + RJ)) ** 3 / MU1) / 86400
    tB = tof_bielip(R, 20 * R) * math.sqrt(RE**3 / MU1) / 86400
    print(f"Tiempo de vuelo: Hohmann = {tH:.1f} d ; bi-eliptica rb = 20R = {tB/365.256:.1f} anios")
    barr = next(x / 1000 for x in range(5000, 14000) if dv_hohmann(x / 1000) > dv_bielip(x / 1000, 1e12))
    print(f"Barrido independiente de R*: {barr:.3f}")
    assert abs(barr - Rs) < 5e-3
    assert abs(Rs - 11.94) < 5e-3 and abs(Rb - 15.58) < 5e-3
    assert dv_hohmann(5.2) < dv_bielip(5.2, 20 * 5.2)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
