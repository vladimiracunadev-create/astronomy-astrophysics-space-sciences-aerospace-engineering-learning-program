#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C04: problema de Lambert (variables universales) para un arco Tierra-Marte del modelo circular y coplanar.

Datos: semiejes de las fichas NASA/NSSDC consultadas el 2026-11-10 (Tierra 149.598e6 km, Marte 227.956e6 km); GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
El estado inicial de la prueba 1 es SINTETICO (generado en el script). Marco heliocentrico plano, km, s, km/s. Solo trayectoria directa de menos de una revolucion.
Pruebas independientes: (1) se propaga un estado conocido con Kepler y Lambert debe recuperar la velocidad inicial (tol. 1e-9 km/s);
(2) se integra numericamente la solucion con RK4 (paso 3600 s) y debe llegar a r2 (tol. 50 km); (3) con un arco casi de 180 grados el delta-v tiende al de Hohmann (tol. 0.01 km/s);
(4) en el TOF de minima energia (formula de Lagrange) el semieje de la solucion iguala s/2 (tol. 1e-6 relativa).
"""
import math, platform
MU = 1.32712440e11
RE, RM = 149.598e6, 227.956e6
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



def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r1 = [RE, 0.0, 0.0]; v1 = [0.4, 1.05 * math.sqrt(MU / RE), 0.3]
    tof = 230 * 86400.0
    r2, v2 = kepler_prop(r1, v1, tof, MU)
    w1, w2 = lambert(r1, r2, tof, MU)
    err = max(abs(a - b) for a, b in zip(w1, v1))
    print(f"Prueba 1 (estado sintetico): |v1_Lambert - v1_verdadera| max = {err:.2e} km/s")
    assert err < 1e-9
    th = math.radians(135.0)
    r1 = [RE, 0.0, 0.0]; r2 = [RM * math.cos(th), RM * math.sin(th), 0.0]
    vcE = math.sqrt(MU / RE); vcM = math.sqrt(MU / RM)
    print("Arco Tierra-Marte de 135 grados: TOF [d]  v_inf_sal [km/s]  v_inf_lleg [km/s]  suma [km/s]")
    for d in (150, 180, 210, 240, 270, 300):
        a, b = lambert(r1, r2, d * 86400.0, MU)
        vs = math.hypot(a[0], a[1] - vcE)
        t2 = [-math.sin(th), math.cos(th), 0.0]
        vl = math.hypot(b[0] - vcM * t2[0], b[1] - vcM * t2[1])
        print(f"                                 {d:7d} {vs:17.3f} {vl:18.3f} {vs+vl:14.3f}")
    a, b = lambert(r1, r2, 210 * 86400.0, MU)
    rf, vf = rk4_dosc(r1, a, 3600.0, 210 * 24, MU)
    dist = math.dist(rf, r2)
    print(f"Prueba 2 (RK4, 210 d): distancia entre la posicion integrada y r2 = {dist:.3f} km")
    assert dist < 50.0
    th = math.radians(179.99); r2 = [RM * math.cos(th), RM * math.sin(th), 0.0]
    at = 0.5 * (RE + RM); tH = math.pi * math.sqrt(at**3 / MU)
    a, b = lambert(r1, r2, tH, MU)
    vs = math.hypot(a[0], a[1] - vcE)
    vH = math.sqrt(MU * (2 / RE - 1 / at)) - vcE
    print(f"Prueba 3 (arco ~180 grados, TOF de Hohmann {tH/86400:.2f} d): v_inf_sal = {vs:.4f} ; Hohmann = {vH:.4f} km/s")
    assert abs(vs - vH) < 0.01
    th = math.radians(135.0); r2 = [RM * math.cos(th), RM * math.sin(th), 0.0]
    c = math.dist(r1, r2); s = 0.5 * (RE + RM + c); amin = s / 2
    tp = math.sqrt(2 / MU) / 3 * (s**1.5 - (s - c) ** 1.5)
    be = 2 * math.asin(math.sqrt((s - c) / s))
    tme = math.sqrt(amin**3 / MU) * (math.pi - (be - math.sin(be)))
    a_, b_ = lambert(r1, r2, tme, MU)
    ael = 1 / (2 / RE - (a_[0] ** 2 + a_[1] ** 2) / MU)
    print(f"Geometria del arco de 135 grados: cuerda c = {c/1e6:.3f}e6 km ; s = {s/1e6:.3f}e6 km ; a_min = {amin/1e6:.3f}e6 km")
    print(f"TOF parabolico (cota inferior elipses) = {tp/86400:.2f} d ; TOF de minima energia = {tme/86400:.2f} d")
    print(f"Prueba 4: semieje de Lambert en el TOF de minima energia = {ael/1e6:.3f}e6 km (esperado {amin/1e6:.3f}e6)")
    assert abs(ael - amin) / amin < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
