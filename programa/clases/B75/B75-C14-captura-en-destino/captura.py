#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C14: captura en Marte desde una trayectoria hiperbolica segun la excentricidad de la orbita final.

Datos consultados (2026-11-10): masa de Marte 0.64169e24 kg, radio ecuatorial 3396.2 km y dia solar de 24.6597 h (ficha NASA/NSSDC); G = 6.67430e-11 (registro de cambios del JPL); GM_Marte = G M.
v_inf de llegada = 2.6493 km/s: resultado del modelo circular y coplanar de C01 (Hohmann Tierra-Marte). ILUSTRATIVO: altitud de periapsis de 300 km; ajustes de excentricidad elegidos.
Modelo: impulso instantaneo en el periapsis; Delta-v = v_hiperbolica(rp) - v_elipse(rp); sin atmosfera ni perturbaciones.
Pruebas: (1) v_elipse en el periapsis igual a la de una propagacion de Kepler que llega al apoapsis esperado (tol. 1e-6 relativa); (2) el delta-v decrece al aumentar la excentricidad;
(3) el limite parabolico (e -> 1) da v_hip - sqrt(2 mu/rp) (tol. 1e-3 km/s); (4) el periodo de la orbita final de un dia solar marciano da el apoapsis esperado por la 3.a ley.
"""
import math, platform
G = 6.67430e-20
GMM = G * 0.64169e24
RM_ = 3396.2
VINF = 2.6493
SOL = 24.6597 * 3600.0
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
    rp = RM_ + 300.0
    vh = math.sqrt(VINF**2 + 2 * GMM / rp)
    print(f"GM_Marte = {GMM:.2f} km3/s2 ; rp = {rp:.1f} km ; v_inf = {VINF} km/s ; v_hiperbolica en rp = {vh:.4f} km/s")
    print("    e      apoapsis [alt, km]   periodo [h]   dv captura [km/s]   ahorro frente a circular [km/s]")
    dvs = []
    dv_circ = vh - math.sqrt(GMM / rp)
    for e in (0.0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99):
        a = rp / (1 - e); ra = a * (1 + e)
        v = math.sqrt(GMM * (1 + e) / rp)
        dv = vh - v; dvs.append(dv)
        P = 2 * math.pi * math.sqrt(a**3 / GMM) / 3600
        print(f"{e:6.2f} {ra - RM_:20.0f} {P:13.2f} {dv:19.4f} {dv_circ - dv:28.4f}")
    assert all(x > y for x, y in zip(dvs, dvs[1:]))
    # Prueba 1: Kepler hasta el apoapsis
    e = 0.9; a = rp / (1 - e)
    r, v = kepler_prop([rp, 0, 0], [0, math.sqrt(GMM * (1 + e) / rp), 0], math.pi * math.sqrt(a**3 / GMM), GMM)
    print(f"Prueba 1: apoapsis por Kepler = {math.hypot(*r):.3f} km ; esperado a(1+e) = {a*(1+e):.3f} km")
    assert abs(math.hypot(*r) - a * (1 + e)) / (a * (1 + e)) < 1e-6
    # Prueba 3: limite parabolico
    dvp = vh - math.sqrt(2 * GMM / rp)
    print(f"Prueba 3: limite parabolico dv = {dvp:.4f} km/s ; con e = 0.999999: {vh - math.sqrt(GMM*(1.999999)/rp):.4f} km/s")
    assert abs(dvp - (vh - math.sqrt(GMM * (1.999999) / rp))) < 1e-3
    # Prueba 4: orbita de un dia solar
    a_sol = (GMM * (SOL / (2 * math.pi)) ** 2) ** (1 / 3)
    ra = 2 * a_sol - rp; e_sol = (ra - rp) / (ra + rp)
    dv_sol = vh - math.sqrt(GMM * (1 + e_sol) / rp)
    P_chk = 2 * math.pi * math.sqrt(((rp + ra) / 2) ** 3 / GMM)
    print(f"Orbita de un dia solar (24.6597 h): a = {a_sol:.1f} km ; apoapsis altitud = {ra - RM_:.0f} km ; e = {e_sol:.4f} ; dv captura = {dv_sol:.4f} km/s")
    assert abs(P_chk - SOL) < 1e-6
    # sensibilidad a v_inf
    print("Sensibilidad a v_inf (captura circular / dia solar):")
    for vi in (2.0, 2.6493, 3.5, 5.0):
        vh2 = math.sqrt(vi**2 + 2 * GMM / rp)
        print(f"   v_inf = {vi:6.4f} km/s: circular {vh2 - math.sqrt(GMM/rp):.4f} km/s ; dia solar {vh2 - math.sqrt(GMM*(1+e_sol)/rp):.4f} km/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
