#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C07: geometria de un sobrevuelo planetario (hiperbola de aproximacion) en la Tierra.

Datos consultados (2026-11-10): masa de la Tierra 5.9722e24 kg y radio medio 6371.000 km, semieje de la orbita 149.598e6 km (ficha NASA/NSSDC);
G = 6.67430e-11 m3/kg/s2 (registro de cambios del JPL). GM_tierra = G M y la masa solar M = GM_sol / G se CALCULAN aqui; GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
SINTETICOS (elegidos para el ejercicio): v_inf = 3.0 km/s y altitudes de periapsis de 200 a 10 000 km.
Modelo: dos cuerpos (nave-Tierra) con esfera de influencia r_SOI = a_T (m_T/M_sol)^(2/5); sin atmosfera, Sol ni Luna.
Pruebas: (1) B = rp sqrt(1 + 2 mu/(rp v_inf^2)) igual a |a| sqrt(e^2 - 1) (tol. 1e-9 relativa); (2) tras el tiempo SOI->periapsis calculado por la ecuacion hiperbolica de Kepler,
la propagacion de Kepler desde el periapsis llega a r_SOI (tol. 1e-3 km); (3) |dv helio| = 2 v_inf sin(delta/2) igual a la diferencia vectorial (tol. 1e-12).
"""
import math, platform
G = 6.67430e-20
MUS = 1.32712440e11
GME = G * 5.9722e24
RE = 6371.0
AE = 149.598e6
MS = MUS / G
RSOI = AE * (5.9722e24 / MS) ** 0.4
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
    print(f"GM_Tierra = {GME:.2f} km3/s2 ; M_sol (de GM_sol/G) = {MS:.4e} kg ; r_SOI = {RSOI:.0f} km ({RSOI/RE:.1f} R_T)")
    vinf = 3.0
    print("v_inf = 3.0 km/s (SINTETICO)")
    print(" alt [km]   rp [km]    e       giro [grados]   v_p [km/s]   B [km]     |dv helio| [km/s]")
    for alt in (200.0, 500.0, 2000.0, 10000.0):
        rp = RE + alt
        e = 1 + rp * vinf**2 / GME
        delta = 2 * math.asin(1 / e)
        vp = math.sqrt(vinf**2 + 2 * GME / rp)
        a = -GME / vinf**2
        B = rp * math.sqrt(1 + 2 * GME / (rp * vinf**2))
        assert abs(B - abs(a) * math.sqrt(e * e - 1)) / B < 1e-9
        dv = 2 * vinf * math.sin(delta / 2)
        vi = [vinf, 0.0]; vo = [vinf * math.cos(delta), vinf * math.sin(delta)]
        assert abs(dv - math.dist(vi, vo)) < 1e-12
        print(f"{alt:8.0f} {rp:9.0f} {e:8.4f} {math.degrees(delta):12.3f} {vp:12.4f} {B:10.0f} {dv:14.4f}")
    rp = RE + 500.0
    e = 1 + rp * vinf**2 / GME; a = GME / vinf**2
    cosh_H = (1 + RSOI / a) / e
    H = math.acosh(cosh_H)
    t_soi = math.sqrt(a**3 / GME) * (e * math.sinh(H) - H)
    vp = math.sqrt(vinf**2 + 2 * GME / rp)
    r, v = kepler_prop([rp, 0, 0], [0, vp, 0], t_soi, GME)
    rn = math.hypot(*r)
    print(f"Altitud 500 km: tiempo del borde de la SOI al periapsis = {t_soi/86400:.3f} d ; por Kepler llega a r = {rn:.3f} km (SOI = {RSOI:.3f} km)")
    assert abs(rn - RSOI) < 1e-3
    print(f"Tiempo total dentro de la SOI = {2*t_soi/86400:.3f} d ; velocidad en el borde = {math.hypot(*v):.4f} km/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
