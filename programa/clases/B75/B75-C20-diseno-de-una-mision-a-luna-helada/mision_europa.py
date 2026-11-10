#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C20: esbozo preliminar de una mision Tierra -> Jupiter -> orbita de Europa (conicas empalmadas, circular y coplanar).

Datos consultados (2026-11-10): masas de la Tierra (5.9722e24 kg) y de Jupiter (1898.13e24 kg), semiejes (Tierra 149.598e6 km, Jupiter 778.479e6 km), radio medio de la Tierra 6371.0 km (fichas NASA/NSSDC);
radio ecuatorial de Jupiter 71 492 km y G = 6.67430e-11 (JPL SSD); GM y radio medio de Europa (3202.71210 km3/s2 y 1560.80 km, JPL SSD). GM_sol = 1.32712440e11 km3/s2 y g0 = 9.80665 m/s2 (estandar, no consultados).
Pagina NASA de Europa Clipper (consultada): lanzamiento el 14-10-2024, llegada a Jupiter en abril de 2030 y 49 sobrevuelos de Europa (no se reproduce ninguna trayectoria).
SINTETICOS / ILUSTRATIVOS: orbita de salida a 300 km; captura joviana con periapsis 9.5 R_J y periodo de 60 d; v_inf en Europa al final del tour 1.5 km/s (una cifra de diseno sin respaldo); orbita final circular de 100 km;
correcciones y tour 0.30 km/s en total; margen 10 %; Isp = 320 s; masa final 1000 kg.
Modelo: tres arcos de dos cuerpos con impulsos instantaneos; el tour de lunas NO se calcula (C26), solo se le asigna un delta-v sintetico.
Pruebas: (1) masa inicial por producto de razones por fase = por suma de delta-v (tol. 1e-12 relativa); (2) la elipse de captura de 60 d tiene el apoapsis esperado al propagarla medio periodo con Kepler (tol. 1e-6 relativa);
(3) el periodo de la orbita circular final de Europa por Kepler es 2 pi sqrt(r^3/GM) (tol. 1e-9).
"""
import math, platform
G = 6.67430e-20
MU = 1.32712440e11
G0 = 9.80665e-3
GME, GMJ = G * 5.9722e24, G * 1898.13e24
GMEu, REu = 3202.71210, 1560.80
RT, RJ = 6371.0, 71492.0
AE, AJ = 149.598e6, 778.479e6
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



def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    at = 0.5 * (AE + AJ)
    vinf_d = math.sqrt(MU * (2 / AE - 1 / at)) - math.sqrt(MU / AE)
    vinf_a = math.sqrt(MU / AJ) - math.sqrt(MU * (2 / AJ - 1 / at))
    tof = math.pi * math.sqrt(at**3 / MU) / 86400
    r0 = RT + 300.0
    dv_dep = math.sqrt(vinf_d**2 + 2 * GME / r0) - math.sqrt(GME / r0)
    rp = 9.5 * RJ
    a_c = (GMJ * (60 * 86400.0 / (2 * math.pi)) ** 2) ** (1 / 3)
    ra = 2 * a_c - rp
    dv_joi = math.sqrt(vinf_a**2 + 2 * GMJ / rp) - math.sqrt(GMJ * (2 / rp - 1 / a_c))
    r_eu = REu + 100.0
    vinf_e = 1.5
    dv_eoi = math.sqrt(vinf_e**2 + 2 * GMEu / r_eu) - math.sqrt(GMEu / r_eu)
    print(f"Hohmann Tierra-Jupiter: TOF = {tof:.1f} d ({tof/365.256:.2f} anios) ; v_inf salida = {vinf_d:.4f} km/s (C3 = {vinf_d**2:.2f} km2/s2) ; v_inf llegada = {vinf_a:.4f} km/s")
    print(f"Captura joviana: rp = {rp:.0f} km (9.5 R_J) ; periodo 60 d -> a = {a_c:.0f} km, ra = {ra:.0f} km ({ra/RJ:.1f} R_J)")
    print(f"Europa: v_inf = {vinf_e} km/s (SINTETICO) ; orbita circular de 100 km: v_c = {math.sqrt(GMEu/r_eu):.4f} km/s")
    fases_orb = [("Salida desde 300 km", dv_dep), ("Correcciones y tour (sintetico)", 0.30), ("Captura en Jupiter (60 d)", dv_joi), ("Insercion en orbita de Europa (100 km)", dv_eoi)]
    fases_fly = [("Salida desde 300 km", dv_dep), ("Correcciones y tour (sintetico)", 0.30), ("Captura en Jupiter (60 d)", dv_joi)]
    res = {}
    for nom, fases in (("Orbitador de Europa", fases_orb), ("Misiones de sobrevuelos (sin insercion en Europa)", fases_fly)):
        print(f"\n{nom}:")
        for n, d in fases: print(f"   {n:42s} {d:8.4f} km/s")
        det = sum(d for _, d in fases); tot = det * 1.10
        m = 1000.0; prod = 1.0
        for _, d in reversed(fases):
            rm = math.exp(d * 1.10 / (ISP * G0)); m *= rm; prod *= rm
        ms = 1000.0 * math.exp(tot / (ISP * G0))
        assert abs(m - ms) / ms < 1e-12
        res[nom] = (det, tot, m)
        print(f"   determinista = {det:.4f} km/s ; con margen 10 % = {tot:.4f} km/s ; masa inicial (m_f = 1000 kg, Isp = 320 s) = {m:.0f} kg ; razon m0/mf = {m/1000:.1f}")
    print("\nComparacion con la pagina de Europa Clipper (consultada): lanzamiento 2024-10-14, llegada a Jupiter en abril de 2030 (unos 5.5 anios), 49 sobrevuelos de Europa.")
    print(f"El Hohmann del modelo dura {tof/365.256:.2f} anios: la ruta real es mas larga (usa asistencias gravitacionales; su detalle no se consulto).")
    # Prueba 2
    r, v = kepler_prop([rp, 0, 0], [0, math.sqrt(GMJ * (2 / rp - 1 / a_c)), 0], 30 * 86400.0, GMJ)
    print(f"Prueba 2: apoapsis de la elipse de 60 d por Kepler (medio periodo) = {math.hypot(*r):.1f} km ; esperado {ra:.1f} km")
    assert abs(math.hypot(*r) - ra) / ra < 1e-6
    # Prueba 3
    P = 2 * math.pi * math.sqrt(r_eu**3 / GMEu)
    rr, vv = kepler_prop([r_eu, 0, 0], [0, math.sqrt(GMEu / r_eu), 0], P, GMEu)
    print(f"Prueba 3: periodo de la orbita circular de Europa de 100 km = {P/60:.2f} min ; tras un periodo la nave vuelve a ({rr[0]:.6f}, {rr[1]:.6f}) km")
    assert math.dist(rr[:2], [r_eu, 0.0]) < 1e-5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
