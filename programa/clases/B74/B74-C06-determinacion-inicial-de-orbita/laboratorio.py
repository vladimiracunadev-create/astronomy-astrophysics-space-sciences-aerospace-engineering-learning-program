#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C06: determinacion inicial de orbita con Gibbs y Lambert (variables universales).

Todo SINTETICO: orbita kepleriana de dos cuerpos alrededor de la Tierra (a = 8000 km, e = 0.1, i = 50 deg, RAAN 40 deg,
argumento del perigeo 30 deg, anomalia media inicial 20 deg); tres posiciones en marco inercial. mu = 3.986004e14 m3/s2 (valor
nominal tipo IAU 2015, NO consultado en esta sesion; ilustrativo). Metodos: Gibbs (tres vectores coplanares) y Lambert por
variables universales con biseccion en z (algoritmo estandar, no consultado en una fuente concreta). Verificacion: Lambert
reproduce la velocidad verdadera del primer punto; Gibbs reproduce la del punto central. Ruido de posicion 10 m (semilla 17).
Tolerancia: error de velocidad sin ruido < 1e-6 m/s para Lambert y para Gibbs (Gibbs es exacto para tres puntos coplanares de una conica).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

MU = 3.986004e14


def stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z)
        return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z)
        return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def kepler_estado(r0, v0, dt):
    """Propaga con variables universales (Newton para chi)."""
    r0n, vr0 = np.linalg.norm(r0), np.dot(r0, v0) / np.linalg.norm(r0)
    alpha = 2 / r0n - np.dot(v0, v0) / MU
    chi = math.sqrt(MU) * abs(alpha) * dt
    for _ in range(100):
        z = alpha * chi**2
        C, S = stumpff(z)
        F = r0n * vr0 / math.sqrt(MU) * chi**2 * C + (1 - alpha * r0n) * chi**3 * S + r0n * chi - math.sqrt(MU) * dt
        dF = r0n * vr0 / math.sqrt(MU) * chi * (1 - z * S) + (1 - alpha * r0n) * chi**2 * C + r0n
        d = F / dF
        chi -= d
        if abs(d) < 1e-9:
            break
    z = alpha * chi**2
    C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C
    g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0
    rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi
    gd = 1 - chi**2 / rn * C
    return r, fd * r0 + gd * v0


def elementos_a_rv(a, e, i, raan, w, M):
    E = M
    for _ in range(50):
        E = E - (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    p = a * (1 - e**2)
    r = p / (1 + e * math.cos(nu))
    rp = r * np.array([math.cos(nu), math.sin(nu), 0])
    vp = math.sqrt(MU / p) * np.array([-math.sin(nu), e + math.cos(nu), 0])
    def R3(x):
        c, s = math.cos(x), math.sin(x)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    def R1(x):
        c, s = math.cos(x), math.sin(x)
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    Q = R3(raan) @ R1(i) @ R3(w)
    return Q @ rp, Q @ vp


def gibbs(r1, r2, r3):
    n1, n2, n3 = map(np.linalg.norm, (r1, r2, r3))
    N = n1 * np.cross(r2, r3) + n2 * np.cross(r3, r1) + n3 * np.cross(r1, r2)
    D = np.cross(r1, r2) + np.cross(r2, r3) + np.cross(r3, r1)
    S = r1 * (n2 - n3) + r2 * (n3 - n1) + r3 * (n1 - n2)
    return math.sqrt(MU / (np.linalg.norm(N) * np.linalg.norm(D))) * (np.cross(D, r2) / n2 + S)


def lambert(r1, r2, dt):
    n1, n2 = np.linalg.norm(r1), np.linalg.norm(r2)
    dnu = math.acos(np.clip(np.dot(r1, r2) / (n1 * n2), -1, 1))
    if np.cross(r1, r2)[2] < 0:
        dnu = 2 * math.pi - dnu
    A = math.sin(dnu) * math.sqrt(n1 * n2 / (1 - math.cos(dnu)))
    def y(z):
        C, S = stumpff(z)
        return n1 + n2 + A * (z * S - 1) / math.sqrt(C)
    def F(z):
        C, S = stumpff(z)
        yy = y(z)
        return (yy / C) ** 1.5 * S + A * math.sqrt(yy) - math.sqrt(MU) * dt
    lo, hi = -50.0, 4 * math.pi**2 - 1e-3
    while y(lo) < 0:
        lo += 0.1
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(mid) < 0:
            lo = mid
        else:
            hi = mid
    z = 0.5 * (lo + hi)
    C, S = stumpff(z)
    yy = y(z)
    f = 1 - yy / n1
    g = A * math.sqrt(yy / MU)
    gd = 1 - yy / n2
    return (r2 - f * r1) / g, (gd * r2 - r1) / g


def main():
    rng = np.random.default_rng(17)
    a, e = 8.0e6, 0.1
    rad = math.radians
    r0, v0 = elementos_a_rv(a, e, rad(50), rad(40), rad(30), rad(20))
    T = 2 * math.pi * math.sqrt(a**3 / MU)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita SINTETICA, semilla 17)",
           f"Periodo = {T/60:.3f} min ; |r0| = {np.linalg.norm(r0)/1e3:.3f} km ; |v0| = {np.linalg.norm(v0):.3f} m/s"]
    res = {"T_min": T / 60}
    # Lambert sin ruido: 25 min
    dt = 25 * 60.0
    r2, v2 = kepler_estado(r0, v0, dt)
    v1_l, v2_l = lambert(r0, r2, dt)
    el = np.linalg.norm(v1_l - v0)
    out.append(f"Lambert (dt = 25 min, sin ruido): error de v1 = {el:.3e} m/s")
    res["lambert_err"] = el
    # Gibbs con separaciones distintas
    out.append("Gibbs (tres posiciones separadas dt cada una):")
    out.append("  dt [s]   sep. angular [deg]   error v2 sin ruido [m/s]   error v2 con ruido 10 m [m/s]")
    okg = True
    for dts in (30.0, 120.0, 300.0):
        r1_, v1_ = kepler_estado(r0, v0, -dts)
        r3_, _ = kepler_estado(r0, v0, dts)
        v_est = gibbs(r1_, r0, r3_)
        e0 = np.linalg.norm(v_est - v0)
        sep = math.degrees(math.acos(np.dot(r1_, r0) / (np.linalg.norm(r1_) * np.linalg.norm(r0))))
        en = []
        for _ in range(500):
            v_n = gibbs(r1_ + rng.normal(0, 10, 3), r0 + rng.normal(0, 10, 3), r3_ + rng.normal(0, 10, 3))
            en.append(np.linalg.norm(v_n - v0))
        rmsn = float(np.sqrt(np.mean(np.square(en))))
        out.append(f"  {dts:6.0f}   {sep:12.3f}   {e0:22.3e}   {rmsn:24.4f}")
        res[f"g{int(dts)}"] = rmsn
        res[f"g0_{int(dts)}"] = e0
        res[f"sep{int(dts)}"] = sep
        if dts == 300.0:
            okg = e0 < 1e-6
    # el vector de posicion 3D en la solucion Lambert con ruido
    en = []
    for _ in range(500):
        v1n, _ = lambert(r0 + rng.normal(0, 10, 3), r2 + rng.normal(0, 10, 3), dt)
        en.append(np.linalg.norm(v1n - v0))
    rms_l = float(np.sqrt(np.mean(np.square(en))))
    out.append(f"Lambert (dt = 25 min) con ruido de 10 m por eje en ambas posiciones: rms del error de v1 = {rms_l:.4f} m/s")
    res["lambert_ruido"] = rms_l
    ok = el < 1e-6 and okg
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
