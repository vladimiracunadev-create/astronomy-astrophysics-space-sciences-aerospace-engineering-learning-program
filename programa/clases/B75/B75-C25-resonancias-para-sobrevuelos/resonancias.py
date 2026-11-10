#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C25: retornos resonantes k:m a la Tierra (la nave da k vueltas al Sol en m anios terrestres).

Datos consultados (2026-11-10): periodo sideral de la Tierra 365.256 d y semieje 149.598e6 km (ficha NASA/NSSDC). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
ILUSTRATIVO: v_inf de 3.0 km/s en la Tierra (elegido por el ejercicio) y orbitas coplanares con la Tierra en orbita circular.
Modelo: periodo de la nave P = (m/k) P_T; a = (mu (P/2pi)^2)^(1/3); T = 3 - (v_inf/V_T)^2 (Tisserand) y 1 - e^2 = ((T - a_T/a)/2)^2 / (a/a_T) -> e; resonancia viable si q <= a_T <= Q.
Pruebas: (1) tras m periodos terrestres la nave propagada con Kepler vuelve a su posicion inicial (tol. 1e-6 relativa en posicion); (2) la velocidad de la nave en el cruce con la orbita terrestre tiene el v_inf pedido (tol. 1e-9 km/s) y el v_inf minimo por Tisserand iguala |v_tangencial - V_T| (tol. 1e-9 km/s);
(3) el semieje de la resonancia 1:1 es el de la Tierra con el mu estandar y P = 365.256 d (tol. 0.1 % frente a la ficha).
"""
import math, platform
MU = 1.32712440e11
PT = 365.256 * 86400.0
AT_FICHA = 149.598e6
VINF = 3.0
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
    aT = (MU * (PT / (2 * math.pi)) ** 2) ** (1 / 3)
    VT = math.sqrt(MU / aT)
    print(f"a de la Tierra con mu estandar y P = 365.256 d: {aT/1e6:.4f}e6 km (ficha: 149.598e6 km, dif. {100*(aT-AT_FICHA)/AT_FICHA:.3f} %) ; V_T = {VT:.4f} km/s")
    assert abs(aT - AT_FICHA) / AT_FICHA < 1e-3
    T = 3 - (VINF / VT) ** 2
    print(f"v_inf = {VINF} km/s (ILUSTRATIVO) ; T de Tisserand = {T:.5f}")
    print(" k:m (revs nave : anios)  P [anios]  a [au]    e       q [au]   Q [au]   viable   v_inf minimo para que q = 1 [km/s]")
    for k, m in ((1, 1), (1, 2), (2, 3), (3, 2), (1, 3), (2, 1), (3, 4), (4, 3), (1, 4)):
        P = m / k * PT
        a = (MU * (P / (2 * math.pi)) ** 2) ** (1 / 3)
        x = a / aT
        t1 = (T - 1 / x) / 2
        e2 = 1 - t1 * t1 / x
        if e2 < 0 or t1 < 0:
            print(f"   {k}:{m}                {m/k:9.3f} {x:8.4f}   (no existe orbita con este v_inf)")
            continue
        e = math.sqrt(e2); q = a * (1 - e); Q = a * (1 + e)
        viable = q <= aT <= Q
        # prueba 2: velocidad en el cruce r = aT
        v2 = MU * (2 / aT - 1 / a)
        vt = math.sqrt(MU * a * (1 - e2)) / aT
        vr = math.sqrt(max(0.0, v2 - vt * vt))
        vinf_chk = math.hypot(vr, vt - VT)
        assert abs(vinf_chk - VINF) < 1e-9 or not viable, (vinf_chk, k, m)
        # v_inf minimo: la orbita toca la de la Tierra tangencialmente (q = 1 si a >= 1 au; Q = 1 si a < 1 au)
        emin = 1 - 1 / x if x >= 1 else 1 / x - 1
        Tmin = 1 / x + 2 * math.sqrt(x * (1 - emin**2))
        vmin = VT * math.sqrt(3 - Tmin)
        vtan = math.sqrt(MU * (1 + emin) / aT) if x >= 1 else math.sqrt(MU * (1 - emin) / aT)
        assert abs(abs(vtan - VT) - vmin) < 1e-9, (vtan, VT, vmin)
        print(f"   {k}:{m}                {m/k:9.3f} {x:8.4f} {e:8.4f} {q/aT:8.4f} {Q/aT:8.4f}   {'si' if viable else 'no'}      {vmin:8.4f}")
        if viable:
            # prueba 1: propagacion de m periodos terrestres desde el perihelio (cualquier punto)
            r0 = [q, 0.0, 0.0]; v0 = [0.0, math.sqrt(MU * (1 + e) / q), 0.0]
            r, v = kepler_prop(r0, v0, m * PT, MU)
            err = math.dist(r, r0) / q
            assert err < 1e-6, err
    print("Prueba 1: para las resonancias viables, tras m anios terrestres la nave regresa a su posicion inicial (error relativo < 1e-6).")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
