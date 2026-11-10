#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C01: transferencia de Hohmann heliocentrica entre planetas (modelo circular y coplanar).

Datos consultados (2026-11-10): semiejes y velocidades orbitales medias de las fichas NASA/NSSDC (Venus 108.210e6 km, Tierra 149.598e6 km,
Marte 227.956e6 km, Jupiter 778.479e6 km; velocidades 35.02, 29.78, 24.08, 13.06 km/s). GM_sol = 1.32712440e11 km3/s2 (valor estandar, no consultado en la pagina).
Modelo: dos cuerpos, sol-nave; orbitas planetarias circulares y coplanares; marco heliocentrico (ecliptica aproximada), unidades km, s, km/s.
Supuestos: impulsos instantaneos, esfera de influencia de tamano nulo (conicas empalmadas). Dominio: estimacion preliminar, no efemeride.
Pruebas: (1) v circular calculada frente a la velocidad media de la ficha (tol. 0.3 %); (2) tiempo de vuelo por la 3.a ley frente a propagacion de Kepler
(variables universales) hasta el afelio: radio = a_destino y angulo = 180 grados (tol. 1e-6 relativa); (3) conservacion de energia (vis-viva) en ambos extremos.
"""
import math, platform
MU = 1.32712440e11
A = {"Venus": 108.210e6, "Tierra": 149.598e6, "Marte": 227.956e6, "Jupiter": 778.479e6}
VF = {"Venus": 35.02, "Tierra": 29.78, "Marte": 24.08, "Jupiter": 13.06}
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



def hohmann(r1, r2):
    at = 0.5 * (r1 + r2)
    vc1, vc2 = math.sqrt(MU / r1), math.sqrt(MU / r2)
    vp = math.sqrt(MU * (2 / r1 - 1 / at)); va = math.sqrt(MU * (2 / r2 - 1 / at))
    tof = math.pi * math.sqrt(at**3 / MU)
    return at, vc1, vc2, vp, va, tof


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Transferencias de Hohmann desde la Tierra (modelo circular y coplanar):")
    print(" destino   a_t [1e6 km]  v_inf_sal [km/s]  v_inf_lleg [km/s]  dv_total_helio [km/s]  TOF [d]")
    for dest in ("Venus", "Marte", "Jupiter"):
        at, vc1, vc2, vp, va, tof = hohmann(A["Tierra"], A[dest])
        vinf1, vinf2 = abs(vp - vc1), abs(vc2 - va)
        print(f"{dest:8s} {at/1e6:11.3f} {vinf1:15.4f} {vinf2:17.4f} {vinf1+vinf2:20.4f} {tof/86400:9.2f}")
    for p in A:
        v = math.sqrt(MU / A[p]); assert abs(v - VF[p]) / VF[p] < 0.003, (p, v)
    print("v circular calculada frente a la ficha (Tierra / Marte): "
          f"{math.sqrt(MU/A['Tierra']):.3f} frente a {VF['Tierra']} y {math.sqrt(MU/A['Marte']):.3f} frente a {VF['Marte']} km/s")
    r1, r2 = A["Tierra"], A["Marte"]
    at, vc1, vc2, vp, va, tof = hohmann(r1, r2)
    r, v = kepler_prop([r1, 0, 0], [0, vp, 0], tof, MU)
    rn = math.hypot(*r); ang = math.degrees(math.atan2(r[1], r[0])) % 360
    print(f"Propagacion de Kepler hasta el TOF: radio = {rn/1e6:.6f}e6 km (esperado {r2/1e6:.6f}e6), angulo = {ang:.6f} grados")
    assert abs(rn - r2) / r2 < 1e-6 and abs(ang - 180) < 1e-5
    e1 = 0.5 * vp**2 - MU / r1; e2 = 0.5 * va**2 - MU / r2
    print(f"Energia especifica en el perihelio y el afelio: {e1:.6f} y {e2:.6f} km2/s2 ; -mu/(2a_t) = {-MU/(2*at):.6f}")
    assert abs(e1 - e2) < 1e-9 and abs(e1 + MU / (2 * at)) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
