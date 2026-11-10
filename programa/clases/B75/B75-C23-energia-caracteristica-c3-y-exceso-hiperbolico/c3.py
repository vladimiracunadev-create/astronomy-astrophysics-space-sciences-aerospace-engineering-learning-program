#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C23: energia caracteristica C3 y exceso hiperbolico de salida desde una orbita baja terrestre.

Datos consultados (2026-11-10): masa de la Tierra 5.9722e24 kg, radio medio 6371.000 km y velocidad de escape 11.186 km/s (ficha NASA/NSSDC); semiejes (Venus 108.210e6, Marte 227.956e6, Jupiter 778.479e6 km);
G = 6.67430e-11 (registro del JPL); GM_tierra = G M. GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado). ILUSTRATIVO: orbita de salida circular de 300 km; masa util de ejemplo por una relacion lineal SINTETICA.
Modelo: C3 = v_inf^2 = 2 eps (energia especifica hiperbolica); v_inf de salida de Hohmann (C01) para cada destino; Delta-v desde la orbita baja = sqrt(C3 + 2 mu/r) - sqrt(mu/r).
Pruebas: (1) la velocidad de escape de superficie calculada, sqrt(2 mu / R), coincide con la ficha 11.186 km/s (tol. 0.1 %); (2) tras el impulso, la energia 0.5 v^2 - mu/r de la propagacion de Kepler (1e7 s despues) iguala C3/2 (tol. 1e-9 relativa);
(3) la pendiente numerica d(Delta-v)/d(C3) en C3 = 0 iguala la analitica 1/(2 v_escape local) (tol. 1e-4 relativa).
"""
import math, platform
G = 6.67430e-20
MU = 1.32712440e11
GME = G * 5.9722e24
RE_ = 6371.0
AE_ = 149.598e6
DEST = {"Venus": 108.210e6, "Marte": 227.956e6, "Jupiter": 778.479e6}
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



def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    vesc = math.sqrt(2 * GME / RE_)
    print(f"Velocidad de escape de la superficie = {vesc:.4f} km/s (ficha: 11.186 km/s)")
    assert abs(vesc - 11.186) / 11.186 < 1e-3
    r0 = RE_ + 300.0
    vc = math.sqrt(GME / r0)
    print(f"Orbita de salida: r = {r0:.0f} km ; v_circ = {vc:.4f} km/s ; v_escape local = {math.sqrt(2*GME/r0):.4f} km/s")
    dv_esc = math.sqrt(2 * GME / r0) - vc
    pend = (math.sqrt(1e-6 + 2 * GME / r0) - vc - dv_esc) / 1e-6
    print(f"Pendiente d(dv)/d(C3) en C3 = 0: numerica {pend:.6f} ; analitica 1/(2 v_esc) = {1/(2*math.sqrt(2*GME/r0)):.6f} (s/km)")
    assert abs(pend - 1 / (2 * math.sqrt(2 * GME / r0))) / pend < 1e-4
    print(" destino   v_inf [km/s]   C3 [km2/s2]   dv desde 300 km [km/s]   dv / dv(escape)")
    print(f"escape          0.0000        0.00          {dv_esc:8.4f}               1.000")
    for n, ad in DEST.items():
        at = 0.5 * (AE_ + ad)
        vinf = abs(math.sqrt(MU * (2 / AE_ - 1 / at)) - math.sqrt(MU / AE_))
        c3 = vinf**2
        dv = math.sqrt(c3 + 2 * GME / r0) - vc
        # prueba 2: energia por propagacion
        vp = math.sqrt(c3 + 2 * GME / r0)
        r, v = kepler_prop([r0, 0, 0], [0, vp, 0], 1e7, GME)
        eps = 0.5 * (v[0] ** 2 + v[1] ** 2) - GME / math.hypot(*r)
        assert abs(eps - c3 / 2) / (c3 / 2) < 1e-9
        print(f"{n:8s} {vinf:12.4f} {c3:13.2f} {dv:22.4f} {dv/dv_esc:16.3f}")
    # relacion sintetica de masa util frente a C3 (lineal, ilustrativa)
    print("Masa util SINTETICA m(C3) = 1500 - 14 C3 [kg] (no corresponde a ningun lanzador):")
    for n, ad in DEST.items():
        at = 0.5 * (AE_ + ad)
        c3 = (math.sqrt(MU * (2 / AE_ - 1 / at)) - math.sqrt(MU / AE_)) ** 2
        print(f"   {n:8s} C3 = {c3:7.2f} -> m = {1500 - 14 * c3:8.1f} kg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
