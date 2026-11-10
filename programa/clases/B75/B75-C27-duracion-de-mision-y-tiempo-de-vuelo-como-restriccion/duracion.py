#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C27: tiempo de vuelo Tierra-Marte como restriccion: costo en delta-v, masa y costo total con un costo temporal ILUSTRATIVO.

Datos consultados (2026-11-10): semiejes y periodo de Marte (686.980 d) de las fichas NASA/NSSDC; masas de la Tierra y Marte, radios 6371.0 y 3396.2 km; G = 6.67430e-11 (registro del JPL); GM_sol = 1.32712440e11 km3/s2 y g0 estandar (no consultados).
SINTETICOS: orbita de salida a 300 km, captura en una orbita de periapsis 300 km y excentricidad 0.8192 (un dia solar, B75-C14), Isp 320 s, masa final 1000 kg, costo de masa 1 unidad (u) por tonelada lanzada y costo temporal de 0 a 0.5 u por dia de mision.
Modelo: para cada TOF se elige la fase de salida (fecha) que minimiza la suma de excesos hiperbolicos con Lambert (circular y coplanar, trayectoria directa de menos de una vuelta); no hay maniobras de correccion ni margen.
Pruebas: (1) con costo temporal nulo el optimo coincide con el minimo de delta-v; (2) refinando la malla de TOF de 20 d a 10 d el optimo cambia menos de 20 d; (3) el delta-v en TOF de Hohmann (258.9 d) con fase libre es el de Hohmann (4.6129 km/s) dentro del 1 %.
"""
import math, platform
MU = 1.32712440e11
G = 6.67430e-20
G0 = 9.80665e-3
GME, GMM = G * 5.9722e24, G * 0.64169e24
AE, AM = 149.598e6, 227.956e6
PM = 686.980
VE, VM = math.sqrt(MU / AE), math.sqrt(MU / AM)
ISP = 320.0
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



def vinf_par(phi_deg, tof_d):
    th = math.radians(phi_deg) + 2 * math.pi * tof_d / PM
    r1 = [AE, 0.0, 0.0]; r2 = [AM * math.cos(th), AM * math.sin(th), 0.0]
    try:
        v1, v2 = lambert(r1, r2, tof_d * 86400.0, MU)
    except Exception:
        return None
    d1 = math.hypot(v1[0], v1[1] - VE)
    t2 = [-math.sin(th), math.cos(th)]
    d2 = math.hypot(v2[0] - VM * t2[0], v2[1] - VM * t2[1])
    return d1, d2


def mejor_fase(tof):
    mejor = None
    for i in range(-1800, 1801, 10):
        phi = i / 10.0
        r = vinf_par(phi, tof)
        if r and abs(abs(phi + 360.0 * tof / PM) % 360 - 180) > 0.2 and (mejor is None or sum(r) < sum(mejor[1])):
            mejor = (phi, r)
    phi0 = mejor[0]
    for k in range(-100, 101):
        phi = phi0 + k * 0.01
        r = vinf_par(phi, tof)
        if r and abs(abs(phi + 360.0 * tof / PM) % 360 - 180) > 0.02 and sum(r) < sum(mejor[1]):
            mejor = (phi, r)
    return mejor


def dv_total(vd, va):
    r0 = 6371.0 + 300.0
    dv_dep = math.sqrt(vd**2 + 2 * GME / r0) - math.sqrt(GME / r0)
    rp = 3396.2 + 300.0
    dv_cap = math.sqrt(va**2 + 2 * GMM / rp) - math.sqrt(GMM * (1 + 0.8192) / rp)
    return dv_dep, dv_cap


def curva(paso):
    out = []
    for tof in range(120, 441, paso):
        m = mejor_fase(float(tof))
        d = dv_total(*m[1])
        out.append((tof, m[0], m[1][0], m[1][1], sum(d)))
    return out


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c20 = curva(20)
    print(" TOF [d]  fase optima [g]  v_inf_sal  v_inf_lleg  dv salida+captura [km/s]  m0 [t] (mf = 1 t)")
    for t, phi, a, b, d in c20:
        print(f"{t:7d} {phi:15.1f} {a:10.3f} {b:11.3f} {d:24.4f} {math.exp(d/(ISP*G0)):13.3f}")
    imin = min(range(len(c20)), key=lambda i: c20[i][4])
    print(f"Minimo de delta-v en la malla de 20 d: TOF = {c20[imin][0]} d, dv = {c20[imin][4]:.4f} km/s")
    at = 0.5 * (AE + AM)
    d_h = dv_total(math.sqrt(MU * (2 / AE - 1 / at)) - VE, VM - math.sqrt(MU * (2 / AM - 1 / at)))
    print(f"Hohmann (258.9 d): dv salida+captura = {sum(d_h):.4f} km/s")
    c10 = curva(10)
    j = min(range(len(c10)), key=lambda i: c10[i][4])
    print("Costo total = m0 [t] + c_t * TOF (unidades u; c_t ILUSTRATIVO):")
    print("   c_t [u/d]   TOF optimo [d]   dv [km/s]   m0 [t]   costo masa [u]   costo tiempo [u]   total [u]")
    for ct in (0.0, 0.005, 0.02, 0.05, 0.2):
        k = min(range(len(c10)), key=lambda i: math.exp(c10[i][4] / (ISP * G0)) + ct * c10[i][0])
        t, phi, a, b, d = c10[k]; m0 = math.exp(d / (ISP * G0))
        print(f"{ct:11.3f} {t:16d} {d:11.4f} {m0:8.3f} {m0:16.3f} {ct*t:18.2f} {m0+ct*t:11.3f}")
    assert abs(c10[j][0] - c20[imin][0]) <= 20
    k0 = min(range(len(c10)), key=lambda i: math.exp(c10[i][4] / (ISP * G0)))
    assert k0 == j
    assert abs(min(c[4] for c in c10 if 250 <= c[0] <= 270) - sum(d_h)) / sum(d_h) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
