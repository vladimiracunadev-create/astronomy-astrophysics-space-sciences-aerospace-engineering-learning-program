#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C29: malla fecha de salida - fecha de llegada (pork-chop) Tierra-Marte con Lambert, modelo circular y coplanar.

Datos consultados (2026-11-10): semiejes y periodos siderales de las fichas NASA/NSSDC (Tierra 149.598e6 km y 365.256 d; Marte 227.956e6 km y 686.980 d). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
Modelo: dia 0 = fecha ideal de Hohmann del modelo (Marte 44.337 grados por delante de la Tierra, B75-C02); longitudes lambda_T(t) = n_T t y lambda_M(t) = 44.337 + n_M t; Lambert directo de menos de una vuelta.
Las fechas son relativas al dia ideal del modelo (NO son fechas de calendario ni de ninguna misi on real).
Pruebas: (1) el minimo refinado de C3 coincide con el de Hohmann (8.674 km2/s2) dentro del 0.5 % (se excluyen los arcos a menos de 0.05 grados de 180, donde Lambert es singular); (2) el minimo de la malla esta dentro del 3 % del refinado; (3) la forma simetrica: C3(dia +10, TOF 260) y C3(dia -10, TOF 260) difieren menos del 25 %.
"""
import math, platform
MU = 1.32712440e11
AE, AM = 149.598e6, 227.956e6
PE, PM = 365.256, 686.980
nE, nM = 2 * math.pi / PE, 2 * math.pi / PM
VE, VM = math.sqrt(MU / AE), math.sqrt(MU / AM)
PHI0 = math.radians(44.337)
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



def costo(dep, tof):
    tE = nE * dep
    r1 = [AE * math.cos(tE), AE * math.sin(tE), 0.0]
    tM = PHI0 + nM * (dep + tof)
    if abs(((tM - tE) % (2 * math.pi)) - math.pi) < math.radians(0.05):
        return None  # arco de 180 grados: Lambert singular (plano indeterminado)
    r2 = [AM * math.cos(tM), AM * math.sin(tM), 0.0]
    try:
        v1, v2 = lambert(r1, r2, tof * 86400.0, MU)
    except Exception:
        return None
    vt1 = [-math.sin(tE) * VE, math.cos(tE) * VE]
    d1 = math.hypot(v1[0] - vt1[0], v1[1] - vt1[1])
    vt2 = [-math.sin(tM) * VM, math.cos(tM) * VM]
    d2 = math.hypot(v2[0] - vt2[0], v2[1] - vt2[1])
    return d1 ** 2, d2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    at = 0.5 * (AE + AM)
    c3h = (math.sqrt(MU * (2 / AE - 1 / at)) - VE) ** 2
    print(f"Referencia de Hohmann del modelo: C3 = {c3h:.3f} km2/s2 en TOF = {math.pi*math.sqrt(at**3/MU)/86400:.2f} d (dia 0)")
    deps = list(range(-60, 61, 10)); tofs = list(range(180, 341, 20))
    print("C3 [km2/s2] de salida: filas = dia de salida (relativo al ideal), columnas = TOF [d]")
    print("  dia  " + " ".join(f"{t:6d}" for t in tofs))
    mejor = (1e9, None)
    for d in deps:
        fila = []
        for t in tofs:
            r = costo(d, float(t))
            fila.append("   --- " if r is None else f"{r[0]:6.1f}")
            if r and r[0] < mejor[0]: mejor = (r[0], (d, t))
        print(f"{d:5d}  " + " ".join(fila))
    print(f"Minimo de la malla: C3 = {mejor[0]:.2f} km2/s2 en dia {mejor[1][0]:+d}, TOF = {mejor[1][1]} d")
    # mapa de bandas (malla mas fina)
    print("Mapa de bandas de C3 (. < 10 ; o < 12 ; O < 16 ; # < 25 ; espacio = mas) con dia -60..+60 (filas, paso 6 d) y TOF 150..350 (columnas, paso 5 d):")
    for d in range(-60, 61, 6):
        s = ""
        for t in range(150, 351, 5):
            r = costo(d, float(t))
            c = "?" if r is None else "." if r[0] < 10 else "o" if r[0] < 12 else "O" if r[0] < 16 else "#" if r[0] < 25 else " "
            s += c
        print(f"{d:5d} |{s}|")
    # refinamiento por busqueda en malla local
    d0, t0 = mejor[1]; d0 = float(d0); t0 = float(t0)
    paso = 5.0
    while paso > 1e-4:
        cand = [(costo(d0 + a * paso, t0 + b * paso), d0 + a * paso, t0 + b * paso) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        cand = [c for c in cand if c[0] is not None]
        mc = min(cand, key=lambda c: c[0][0])
        if (mc[1], mc[2]) == (d0, t0): paso *= 0.5
        else: d0, t0 = mc[1], mc[2]
    cref = costo(d0, t0)
    print(f"Minimo refinado: C3 = {cref[0]:.4f} km2/s2 ; v_inf llegada = {cref[1]:.4f} km/s ; dia {d0:+.3f}, TOF = {t0:.3f} d")
    assert abs(cref[0] - c3h) / c3h < 0.005
    assert abs(mejor[0] - cref[0]) / cref[0] < 0.03
    a = costo(10, 260.0); b = costo(-10, 260.0)
    print(f"Simetria: C3(+10 d, 260 d) = {a[0]:.2f} ; C3(-10 d, 260 d) = {b[0]:.2f} km2/s2")
    assert abs(a[0] - b[0]) / min(a[0], b[0]) < 0.25
    # ancho de ventana: dias con C3 < 12 con TOF libre (mejor TOF por dia)
    ok = []
    for d in range(-60, 61):
        m = min((costo(float(d), float(t))[0] for t in range(200, 321, 5) if costo(float(d), float(t))), default=None)
        if m is not None and m < 12.0: ok.append(d)
    print(f"Ancho de la ventana con C3 < 12 km2/s2 (mejor TOF para cada dia): de {min(ok):+d} a {max(ok):+d} d ({max(ok)-min(ok)+1} d)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
