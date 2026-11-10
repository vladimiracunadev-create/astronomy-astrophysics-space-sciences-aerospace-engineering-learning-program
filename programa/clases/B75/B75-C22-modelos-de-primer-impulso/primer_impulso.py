#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C22: modelos de primer impulso: delta-v de salida y tiempo de vuelo para alcanzar un radio heliocentrico (modelo circular y coplanar).

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Venus 108.210e6, Tierra 149.598e6, Marte 227.956e6, Jupiter 778.479e6 km). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
Modelo: la nave parte de la orbita circular de la Tierra con un impulso heliocentrico de modulo dv y direccion phi medida desde la velocidad (0 = tangencial, positivo hacia afuera); se calculan energia, momento, apoapsis y tiempo hasta el apoapsis.
Pruebas: (1) para cada radio objetivo, el dv minimo por biseccion con phi = 0 iguala al de Hohmann (tol. 1e-9); (2) un barrido de phi de -90 a 90 grados con paso 0.05 muestra que, para un dv dado, el apoapsis maximo ocurre en phi = 0 (tol. 0.1 grado);
(3) el tiempo hasta el apoapsis por la ecuacion de Kepler iguala el de la propagacion universal (tol. 1e-6 relativa).
"""
import math, platform
MU = 1.32712440e11
A = {"Venus": 108.210e6, "Tierra": 149.598e6, "Marte": 227.956e6, "Jupiter": 778.479e6}
RE_ = A["Tierra"]; VE = math.sqrt(MU / RE_)
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



def apoapsis(dv, phi):
    vx = dv * math.sin(phi); vy = VE + dv * math.cos(phi)
    v2 = vx * vx + vy * vy
    eps = 0.5 * v2 - MU / RE_
    if eps >= 0: return float("inf"), None
    a = -MU / (2 * eps)
    h = RE_ * vy
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU**2))
    return a * (1 + e), (a, e)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(" destino   dv Hohmann [km/s]   dv minimo (biseccion) [km/s]   phi optimo [grados]   TOF a apoapsis [d]")
    for dest in ("Venus", "Marte", "Jupiter"):
        rt = A[dest]
        at = 0.5 * (RE_ + rt)
        dvh = math.sqrt(MU * (2 / RE_ - 1 / at)) - VE
        if rt > RE_:
            lo, hi = 0.0, 20.0
            for _ in range(200):
                m = 0.5 * (lo + hi)
                if apoapsis(m, 0.0)[0] < rt: lo = m
                else: hi = m
            dvmin = 0.5 * (lo + hi)
            assert abs(dvmin - dvh) < 1e-9
            # Prueba 2: barrido de phi
            mejor = max(((apoapsis(dvh, math.radians(p / 20.0))[0], p / 20.0) for p in range(-1800, 1801)), key=lambda x: x[0])
            assert abs(mejor[1]) < 0.1
            tof = math.pi * math.sqrt(at**3 / MU) / 86400
            print(f"{dest:8s} {dvh:15.4f} {dvmin:27.4f} {mejor[1]:19.2f} {tof:18.2f}")
        else:
            print(f"{dest:8s} {dvh:15.4f}   (destino interior: impulso retrogrado, dv negativo; |dv| = {abs(dvh):.4f})")
    print("Familia tangencial: dv, apoapsis y tiempo hasta el apoapsis")
    print("  dv [km/s]   apoapsis [au]   TOF a apoapsis [d]   excentricidad")
    for dv in (1.0, 2.0, 2.9452, 4.0, 6.0, 8.0, 8.7933):
        ra, el = apoapsis(dv, 0.0)
        a, e = el
        E = math.pi
        tof = math.sqrt(a**3 / MU) * math.pi
        r, v = kepler_prop([RE_, 0, 0], [0, VE + dv, 0], tof, MU)
        assert abs(math.hypot(*r) - ra) / ra < 1e-6
        print(f"{dv:9.4f} {ra/149597870.7:14.3f} {tof/86400:20.1f} {e:14.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
