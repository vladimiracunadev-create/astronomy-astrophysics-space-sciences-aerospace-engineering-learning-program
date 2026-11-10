#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C21: interseccion de dos conicas con foco comun (elipse de transferencia y orbita real de Marte).

Datos consultados (2026-11-10): elementos de la tabla de posiciones aproximadas del JPL (J2000): Marte a = 1.52371034 au, e = 0.09339410, longitud del perihelio 336.05637041 grados (-23.94362959);
baricentro Tierra-Luna a = 1.00000261 au, e = 0.01671123, longitud del perihelio 102.93768193 grados; 1 au = 149 597 870.7 km y GM_sol = 1.32712440e11 km3/s2 (estandar, no consultados).
ILUSTRATIVO: la elipse de transferencia sale tangente a la orbita de la Tierra (circular de 1 au) en el perihelio con longitud de salida lambda_d elegida y apoapsis 1.8, 2.2 o 3.0 au.
Modelo: dos cuerpos heliocentricos coplanares; interseccion por la ecuacion p_A/(1 + e_A cos th) = p_B/(1 + e_B cos(th - dw)) -> A cos th + B sin th = C.
Pruebas: (1) en cada interseccion los radios de las dos conicas coinciden (tol. 1e-9 relativa); (2) la propagacion de Kepler de la elipse de transferencia desde el perihelio, durante el TOF calculado, llega al radio de la interseccion (tol. 1e-6 relativa).
"""
import math, platform
MU = 1.32712440e11
AU = 149597870.7
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



def interseca(pA, eA, wA, pB, eB, wB):
    """Verdaderas anomalias (respecto a la conica A) de las intersecciones; w = longitud del perihelio."""
    dw = wB - wA
    A = pA * eB * math.cos(dw) - pB * eA
    B = pA * eB * math.sin(dw)
    C = pB - pA
    R = math.hypot(A, B)
    if abs(C) > R: return []
    base = math.atan2(B, A); d = math.acos(C / R)
    return [base + d, base - d]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    aM, eM, wM = 1.52371034 * AU, 0.09339410, math.radians(-23.94362959)
    pM = aM * (1 - eM**2)
    print(f"Marte (JPL, J2000): a = {aM/AU:.5f} au, e = {eM:.5f}, longitud del perihelio = {math.degrees(wM)%360:.3f} grados ; perihelio {aM*(1-eM)/AU:.4f} au, afelio {aM*(1+eM)/AU:.4f} au")
    print(" lambda_d [g]  apoapsis [au]   1.a interseccion (saliente): longitud [g]  r [au]  TOF [d]   Dv_sal [km/s]   (2.a, entrante: longitud [g], r [au], TOF [d])")
    VE = math.sqrt(MU / AU)
    for lam in (60.0, 100.0, 140.0):
        for ra_au in (1.8, 2.2, 3.0):
            ra = ra_au * AU
            a = 0.5 * (AU + ra); e = (ra - AU) / (ra + AU); p = a * (1 - e**2)
            w = math.radians(lam)
            sols = interseca(p, e, w, pM, eM, wM)
            filas = []
            for th in sols:
                th = th % (2 * math.pi)
                rA = p / (1 + e * math.cos(th)); rB = pM / (1 + eM * math.cos(th + w - wM))
                assert abs(rA - rB) / rA < 1e-9
                # Prueba 2: Kepler desde el perihelio
                vp = math.sqrt(MU * (1 + e) / (a * (1 - e)))
                E = 2 * math.atan(math.sqrt((1 - e) / (1 + e)) * math.tan(th / 2)) % (2 * math.pi)
                tof = math.sqrt(a**3 / MU) * (E - e * math.sin(E))
                r, v = kepler_prop([AU, 0.0, 0.0], [0.0, vp, 0.0], tof, MU)
                assert abs(math.hypot(*r) - rA) / rA < 1e-6
                filas.append((math.degrees(th + w) % 360, rA / AU, tof / 86400))
            dvs = math.sqrt(MU * (1 + e) / (AU)) - VE
            filas.sort(key=lambda x: x[2])
            f0 = filas[0]; f1 = filas[1] if len(filas) > 1 else None
            s = f"{lam:10.1f} {ra_au:13.1f} {f0[0]:24.2f} {f0[1]:9.4f} {f0[2]:9.2f} {dvs:14.4f}"
            if f1: s += f"   ({f1[0]:.2f}, {f1[1]:.4f}, {f1[2]:.2f})"
            print(s)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
