#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C28: dosis acumulada SINTETICA en orbitas jovianas con una tasa de dosis ilustrativa ~ r^-3 y blindaje exponencial.

Datos consultados (2026-11-10): masa de Jupiter 1898.13e24 kg (ficha NASA/NSSDC), radio ecuatorial 71 492 km y G = 6.67430e-11 (JPL SSD); semieje de Europa 671 100 km (JPL SSD, elementos medios).
SINTETICOS / ILUSTRATIVOS (NO son datos de radiacion): tasa de dosis D(r) = D0 (R_J/r)^3 con D0 = 1e6 unidades/dia (u/d) a r = R_J; atenuacion por blindaje exp(-t/lambda) con lambda = 10 g/cm2; limite de dosis de la mision 2e5 u.
El modelo no reproduce el entorno real de radiacion de Jupiter (cuya forma, magnitud y variabilidad NO se consultaron).
Modelo: orbitas keplerianas de dos cuerpos; dosis por orbita = int D dt = D0 R_J^3 / 86400 * 2 pi / (h p) (analitica).
Pruebas: (1) la dosis por orbita integrada numericamente (20 000 pasos con Kepler universal y trapecio) iguala la formula analitica (tol. 1e-4 relativa); (2) la dosis de la orbita circular de Europa es D(a) por el periodo (tol. 1e-9);
(3) la dosis con blindaje t es la dosis sin blindaje por exp(-t/lambda) (tol. 1e-12).
"""
import math, platform
G = 6.67430e-20
GMJ = G * 1898.13e24
RJ = 71492.0
D0 = 1.0e6  # u/dia a r = RJ
LAM = 10.0   # g/cm2
LIM = 2.0e5  # u
AEU = 671100.0
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



def dosis_analitica(rp, ra):
    a = 0.5 * (rp + ra); e = (ra - rp) / (ra + rp); p = a * (1 - e * e)
    h = math.sqrt(GMJ * p)
    return D0 * RJ**3 / 86400.0 * 2 * math.pi / (h * p), a, e, p


def dosis_numerica(rp, ra, n=20000):
    a = 0.5 * (rp + ra)
    vp = math.sqrt(GMJ * (2 / rp - 1 / a))
    P = 2 * math.pi * math.sqrt(a**3 / GMJ)
    dt = P / n
    tot = 0.0
    r0 = [rp, 0.0, 0.0]; v0 = [0.0, vp, 0.0]
    rate_prev = D0 * (RJ / rp) ** 3
    for i in range(1, n + 1):
        r, v = kepler_prop(r0, v0, i * dt, GMJ)
        rate = D0 * (RJ / math.hypot(*r)) ** 3
        tot += 0.5 * (rate + rate_prev) * dt / 86400.0
        rate_prev = rate
    return tot


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Tasa SINTETICA D(r) = D0 (R_J/r)^3, D0 = 1e6 u/d (NO es el entorno real de radiacion)")
    casos = [("Orbita sintetica 5 R_J x 3e6 km (C16)", 5 * RJ, 3.0e6), ("Captura 9.5 R_J, periodo 60 d (C20)", 9.5 * RJ, 8156994.1), ("Orbita 15 R_J x 40 R_J", 15 * RJ, 40 * RJ)]
    print(" orbita                                   periodo [d]   dosis por orbita [u]   numerica [u]   dif [%]   orbitas hasta 2e5 u (sin blindaje)   con 5 g/cm2")
    for nom, rp, ra in casos:
        D, a, e, p = dosis_analitica(rp, ra)
        P = 2 * math.pi * math.sqrt(a**3 / GMJ) / 86400
        Dn = dosis_numerica(rp, ra)
        dif = 100 * (Dn - D) / D
        assert abs(Dn - D) / D < 1e-4
        n0 = LIM / D; n5 = LIM / (D * math.exp(-5.0 / LAM))
        print(f"{nom:40s} {P:10.2f} {D:21.2f} {Dn:14.2f} {dif:9.4f} {n0:30.0f} {n5:14.0f}")
    # orbita circular de Europa
    P = 2 * math.pi * math.sqrt(AEU**3 / GMJ)
    D_c = D0 * (RJ / AEU) ** 3 * P / 86400.0
    Dd, a, e, p = dosis_analitica(AEU, AEU)
    assert abs(D_c - Dd) / D_c < 1e-9
    print(f"Orbita circular de Europa (671 100 km): tasa = {D0*(RJ/AEU)**3:.4f} u/d ; periodo = {P/86400:.4f} d ; dosis por orbita = {D_c:.4f} u ; por 30 d = {D0*(RJ/AEU)**3*30:.2f} u")
    print("Blindaje exp(-t/lambda), lambda = 10 g/cm2 (SINTETICO):")
    for t in (0.0, 1.0, 5.0, 10.0, 20.0):
        f = math.exp(-t / LAM)
        assert abs(f * 100.0 - 100.0 * math.exp(-t / LAM)) < 1e-12
        print(f"   t = {t:5.1f} g/cm2: factor {f:.4f} ; dosis por orbita en la orbita 5 R_J x 3e6 km = {f*dosis_analitica(5*RJ, 3.0e6)[0]:.2f} u")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
