#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C24: plano B y parametro de impacto de un sobrevuelo terrestre (hiperbola en 3D).

Datos consultados (2026-11-10): masa de la Tierra 5.9722e24 kg y radio medio 6371.000 km (ficha NASA/NSSDC); G = 6.67430e-11 (registro del JPL); GM_tierra = G M.
SINTETICOS: v_inf = 3.0 km/s; direccion de aproximacion S con declinacion 20 grados y ascension recta 40 grados (marco inercial generico); puntos de apuntado (B.T, B.R) elegidos para el ejercicio.
Modelo: dos cuerpos; B = S x H^ (de modulo h / v_inf); T = S x k / |S x k| (k = eje z); R = S x T; B.T y B.R son las componentes en el plano B.
Pruebas: (1) |B| = h/v_inf = |a| sqrt(e^2 - 1) (tol. 1e-9); (2) construir el estado en el periapsis desde (B.T, B.R, S) y volver a extraer las componentes del plano B devuelve las de partida (tol. 1e-9 km);
(3) la direccion asintotica S recuperada con Kepler a +/-2e4 y 4e4 d y extrapolacion de Richardson coincide con la de partida (tol. 1e-6 rad).
"""
import math, platform
G = 6.67430e-20
GM = G * 5.9722e24
RE_ = 6371.0
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



def cruz(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def nrm(a):
    n = math.sqrt(dot(a, a)); return [x / n for x in a]


def esc(k, a):
    return [k * x for x in a]


def suma(a, b):
    return [x + y for x, y in zip(a, b)]


def base(S):
    T = nrm(cruz(S, [0.0, 0.0, 1.0])); R = cruz(S, T)
    return T, R


def estado_periapsis(S, BT, BR):
    T, R = base(S)
    B = suma(esc(BT, T), esc(BR, R))
    h = cruz(B, esc(VINF, S))
    hn = math.sqrt(dot(h, h)); hh = esc(1 / hn, h)
    e = math.sqrt(1 + (hn * VINF / GM) ** 2)
    p = suma(esc(1 / e, S), esc(-math.sqrt(e * e - 1) / e, cruz(hh, S)))
    q = cruz(hh, p)
    a = GM / VINF**2
    rp = a * (e - 1)
    vp = math.sqrt(VINF**2 + 2 * GM / rp)
    return esc(rp, p), esc(vp, q), e, hn, rp


def planoB(r, v):
    h = cruz(r, v); hn = math.sqrt(dot(h, h)); hh = esc(1 / hn, h)
    eps = 0.5 * dot(v, v) - GM / math.sqrt(dot(r, r))
    vinf = math.sqrt(2 * eps)
    ev = suma(esc(1 / GM, cruz(v, h)), esc(-1 / math.sqrt(dot(r, r)), r))
    e = math.sqrt(dot(ev, ev)); p = esc(1 / e, ev); q = cruz(hh, p)
    S = esc(1 / e, suma(p, esc(math.sqrt(e * e - 1), q)))
    B = esc(hn / vinf, cruz(S, hh))
    T, R = base(S)
    return S, dot(B, T), dot(B, R), hn / vinf, e


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dec, asc = math.radians(20.0), math.radians(40.0)
    S0 = [math.cos(dec) * math.cos(asc), math.cos(dec) * math.sin(asc), math.sin(dec)]
    T, R = base(S0)
    print(f"GM_Tierra = {GM:.2f} km3/s2 ; v_inf = {VINF} km/s (SINTETICO) ; S = ({S0[0]:.4f}, {S0[1]:.4f}, {S0[2]:.4f})")
    print(f"T = ({T[0]:.4f}, {T[1]:.4f}, {T[2]:.4f}) ; R = ({R[0]:.4f}, {R[1]:.4f}, {R[2]:.4f})")
    print(" B.T [km]  B.R [km]   |B| [km]     e        r_p [km]  altitud [km]   i del plano [grados]   B.T,B.R recuperados [km]")
    for BT, BR in ((20000.0, 10000.0), (25000.0, 0.0), (0.0, 26000.0), (-15000.0, -22000.0), (30000.0, 5000.0)):
        r, v, e, hn, rp = estado_periapsis(S0, BT, BR)
        S, bt, br, B, e2 = planoB(r, v)
        assert abs(B - math.hypot(BT, BR)) < 1e-9 and abs(bt - BT) < 1e-9 and abs(br - BR) < 1e-9
        a = GM / VINF**2
        assert abs(B - a * math.sqrt(e * e - 1)) < 1e-9
        inc = math.degrees(math.acos(max(-1.0, min(1.0, cruz(r, v)[2] / hn))))
        print(f"{BT:9.0f} {BR:9.0f} {B:10.1f} {e:8.4f} {rp:11.1f} {rp-RE_:12.1f} {inc:20.2f}   ({bt:.3f}, {br:.3f}){'  IMPACTA con la superficie' if rp < RE_ else ''}")
    # Prueba 3: S con Kepler
    r, v, e, hn, rp = estado_periapsis(S0, 20000.0, 10000.0)
    def Sdir(Tt):
        r1, v1 = kepler_prop(r, v, -Tt, GM)
        n = math.sqrt(dot(v1, v1)); return esc(1 / n, v1)
    s1 = Sdir(2e4 * 86400.0); s2 = Sdir(4e4 * 86400.0)
    Sext = nrm(suma(esc(2.0, s2), esc(-1.0, s1)))
    ang = math.sqrt(sum((x - y) ** 2 for x, y in zip(Sext, S0)))
    print(f"Prueba 3: distancia entre la direccion asintotica recuperada por Kepler y S de partida = {ang:.2e} rad")
    assert ang < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
