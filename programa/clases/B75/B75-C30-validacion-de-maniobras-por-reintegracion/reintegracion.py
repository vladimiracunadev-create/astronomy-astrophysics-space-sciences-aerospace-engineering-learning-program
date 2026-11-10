#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C30: validacion de una maniobra impulsiva por reintegracion (salida heliocentrica Tierra-Marte del modelo circular y coplanar).

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Tierra 149.598e6 km, Marte 227.956e6 km). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
SINTETICA / ILUSTRATIVA: perturbacion radial a = a0 (1 au / r)^2 con a0 = 2e-9 km/s2 (valor inventado; NO se consulto ningun valor de presion de radiacion solar ni de otra perturbacion real); el impulso es tangencial de 2.9452 km/s.
Metodo: (1) salto de energia en el impulso comparado con v-.dv + |dv|^2/2; (2) reintegracion con RK4 hacia delante y luego hacia atras (reversibilidad); (3) convergencia con el paso (43200, 21600, 10800 s);
(4) escala de la dispersion por la perturbacion con a0 (a0 y 2 a0); (5) sin perturbacion RK4 debe igualar la propagacion de Kepler.
Pruebas: (1) salto de energia numerico igual al analitico (tol. 1e-9); (2) sin perturbacion |RK4 - Kepler| < 1 km tras el TOF; (3) ida y vuelta con perturbacion regresa dentro de 10 km; (4) el cociente de diferencias de paso (43200-21600 frente a 21600-10800 s) esta entre 12 y 20 (orden 4);
(5) la desviacion con 2 a0 es el doble que con a0 dentro del 5 %.
"""
import math, platform
MU = 1.32712440e11
AE, AM = 149.598e6, 227.956e6
A0 = 2e-9
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



def acel(r, a0):
    rn = math.hypot(*r)
    f = a0 * (AE / rn) ** 2 / rn
    return [-MU * r[0] / rn**3 + f * r[0], -MU * r[1] / rn**3 + f * r[1]]


def integrar(r, v, T, dt, a0):
    n = int(round(abs(T) / dt)); h = T / n
    r = list(r); v = list(v)
    for _ in range(n):
        k1v = acel(r, a0); k1r = v
        r2 = [x + 0.5 * h * y for x, y in zip(r, k1r)]; v2 = [x + 0.5 * h * y for x, y in zip(v, k1v)]
        k2v = acel(r2, a0); k2r = v2
        r3 = [x + 0.5 * h * y for x, y in zip(r, k2r)]; v3 = [x + 0.5 * h * y for x, y in zip(v, k2v)]
        k3v = acel(r3, a0); k3r = v3
        r4 = [x + h * y for x, y in zip(r, k3r)]; v4 = [x + h * y for x, y in zip(v, k3v)]
        k4v = acel(r4, a0); k4r = v4
        r = [x + h / 6 * (p + 2 * q + 2 * s + w) for x, p, q, s, w in zip(r, k1r, k2r, k3r, k4r)]
        v = [x + h / 6 * (p + 2 * q + 2 * s + w) for x, p, q, s, w in zip(v, k1v, k2v, k3v, k4v)]
    return r, v


def energia(r, v):
    return 0.5 * (v[0] ** 2 + v[1] ** 2) - MU / math.hypot(*r)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    VE = math.sqrt(MU / AE)
    at = 0.5 * (AE + AM)
    dv = math.sqrt(MU * (2 / AE - 1 / at)) - VE
    tof = math.pi * math.sqrt(at**3 / MU)
    rm = [AE, 0.0]; vm = [0.0, VE]
    vp = [vm[0], vm[1] + dv]
    de_num = energia(rm, vp) - energia(rm, vm)
    de_ana = vm[1] * dv + 0.5 * dv * dv
    print(f"Impulso tangencial dv = {dv:.4f} km/s ; TOF = {tof/86400:.2f} d")
    print(f"Salto de energia: numerico = {de_num:.9f} km2/s2 ; analitico v-.dv + dv^2/2 = {de_ana:.9f} km2/s2")
    assert abs(de_num - de_ana) < 1e-9
    r_k, v_k = kepler_prop(rm + [0.0], vp + [0.0], tof, MU)
    r0, v0 = integrar(rm, vp, tof, 3600.0, 0.0)
    e0 = math.dist(r0, r_k[:2])
    print(f"Sin perturbacion: |RK4 - Kepler| tras el TOF = {e0:.4f} km")
    assert e0 < 1.0
    # convergencia
    sol = {}
    for dt in (43200.0, 21600.0, 10800.0):
        sol[dt] = integrar(rm, vp, tof, dt, A0)[0]
    d1 = math.dist(sol[43200.0], sol[21600.0]); d2 = math.dist(sol[21600.0], sol[10800.0])
    print(f"Con perturbacion a0 = {A0:.1e} km/s2 (SINTETICA): diferencia entre pasos de 43200 y 21600 s = {d1:.4f} km ; entre 21600 y 10800 s = {d2:.4f} km ; cociente = {d1/d2:.2f} (orden 4: 16)")
    assert 12.0 < d1 / d2 < 20.0
    # ida y vuelta
    rf, vf = integrar(rm, vp, tof, 3600.0, A0)
    rb, vb = integrar(rf, [-vf[0], -vf[1]], tof, 3600.0, A0)
    print(f"Ida y vuelta (con la velocidad invertida): distancia a la posicion inicial = {math.dist(rb, rm):.5f} km")
    assert math.dist(rb, rm) < 10.0
    # efecto de la perturbacion y escala
    dev1 = math.dist(sol[21600.0], r0)
    r2, _ = integrar(rm, vp, tof, 3600.0, 2 * A0)
    dev2 = math.dist(r2, r0)
    print(f"Desplazamiento de la llegada por la perturbacion: a0 -> {dev1:.1f} km ; 2 a0 -> {dev2:.1f} km ; cociente = {dev2/dev1:.3f}")
    assert abs(dev2 / dev1 - 2.0) < 0.1
    print(f"Radio de llegada con perturbacion = {math.hypot(*sol[21600.0])/1e6:.4f}e6 km (sin ella {math.hypot(*r0)/1e6:.4f}e6 km)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
