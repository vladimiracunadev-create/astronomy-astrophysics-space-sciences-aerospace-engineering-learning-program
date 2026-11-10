#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C06: asistencia gravitacional en Jupiter (conicas empalmadas, plano de la ecliptica).

Datos consultados (2026-11-10): semieje de Jupiter 778.479e6 km, masa 1898.13e24 kg y radio ecuatorial 71 492 km (fichas NASA/NSSDC y JPL SSD); Venus 108.210e6 km, masa 4.8673e24 kg, radio 6051.8 km; Tierra 149.598e6 km;
G = 6.67430e-11 m3/kg/s2 (registro de cambios del JPL); GM_jupiter = G M se CALCULA aqui. GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado en la pagina).
ILUSTRATIVO: la nave llega a Jupiter (y a Venus) por una elipse de Hohmann desde la Tierra; las distancias de periapsis (en radios del planeta, para Venus se anaden 5 % y mas) son elecciones del ejercicio.
Modelo: orbita circular de Jupiter, v_inf conservado en el marco del planeta, giro delta = 2 asin(1/e); sin perturbaciones ni radiacion.
Pruebas: (1) |v_inf| antes y despues iguales (tol. 1e-12 km/s); (2) el giro de la formula iguala el giro entre asintotas obtenido con Kepler a +/-2e4 y 4e4 d y extrapolacion de Richardson (tol. 1e-6 rad);
(3) RK4 y Kepler coinciden en posicion tras 20 d de sobrevuelo (tol. 10 km).
"""
import math, platform
MU = 1.32712440e11
G = 6.67430e-20  # km3/kg/s2
AE, AJ = 149.598e6, 778.479e6
GMJ = G * 1898.13e24
RJ = 71492.0
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



def rot(v, a):
    c, s = math.cos(a), math.sin(a)
    return [c * v[0] - s * v[1], s * v[0] + c * v[1]]


def elementos(r, v):
    rn = math.hypot(*r); v2 = v[0] ** 2 + v[1] ** 2
    eps = 0.5 * v2 - MU / rn
    a = -MU / (2 * eps)
    h = r[0] * v[1] - r[1] * v[0]
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU**2))
    return a, e, a * (1 - e), a * (1 + e), eps


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    AU = 149597870.7
    casos = []
    # Jupiter: la nave (Hohmann desde la Tierra) llega al afelio, mas lenta que el planeta
    at = 0.5 * (AE + AJ)
    casos.append(("Jupiter", AJ, math.sqrt(MU * (2 / AJ - 1 / at)), GMJ, RJ, [2.0, 5.0, 10.0]))
    # Venus: la nave (Hohmann desde la Tierra) llega al perihelio, mas rapida que el planeta
    AV = 108.210e6; GMV = G * 4.8673e24; RV = 6051.8
    atv = 0.5 * (AE + AV)
    casos.append(("Venus", AV, math.sqrt(MU * (2 / AV - 1 / atv)), GMV, RV, [1.05, 1.5, 3.0]))
    print("Planeta  rp [R_p]   e      giro [grados]  |v| antes -> despues [km/s]   dv helio [km/s]   afelio [au]  perihelio [au]")
    for nom, ap, vsc, gm, rpl, ks in casos:
        Vp = math.sqrt(MU / ap)
        vinf = abs(Vp - vsc)
        sg = 1.0 if vsc > Vp else -1.0       # sentido de v_inf respecto a V_planeta
        print(f"{nom}: V_planeta = {Vp:.4f} km/s ; v_nave = {vsc:.4f} km/s ; v_inf = {vinf:.4f} km/s ; GM = {gm:.1f} km3/s2")
        for k in ks:
            rp = k * rpl
            e = 1 + rp * vinf**2 / gm
            delta = 2 * math.asin(1 / e)
            salidas = []
            for signo in (+1, -1):
                vout = rot([0.0, sg * vinf], signo * delta)
                assert abs(math.hypot(*vout) - vinf) < 1e-12
                salidas.append([vout[0], Vp + vout[1]])
            assert abs(math.hypot(*salidas[0]) - math.hypot(*salidas[1])) < 1e-12
            vh = salidas[0]
            a_, e_, q, Q, eps = elementos([ap, 0.0], vh)
            dv = math.hypot(*vh) - vsc
            print(f"{nom:8s} {k:6.2f} {e:8.3f} {math.degrees(delta):11.3f}   {vsc:8.4f} -> {math.hypot(*vh):8.4f} {dv:18.4f} {Q/AU:12.3f} {q/AU:12.3f}")
    # Prueba 2: Kepler hiperbolico a distancia enorme
    vinf = abs(math.sqrt(MU / AJ) - math.sqrt(MU * (2 / AJ - 1 / at)))
    rp = 5 * RJ; e = 1 + rp * vinf**2 / GMJ
    vp = math.sqrt(vinf**2 + 2 * GMJ / rp)
    def giro_T(T):
        rA, vA = kepler_prop([rp, 0, 0], [0, vp, 0], -T, GMJ)
        rB, vB = kepler_prop([rp, 0, 0], [0, vp, 0], +T, GMJ)
        g = math.atan2(vB[1], vB[0]) - math.atan2(vA[1], vA[0])
        return abs((g + math.pi) % (2 * math.pi) - math.pi)
    g1, g2 = giro_T(2e4 * 86400.0), giro_T(4e4 * 86400.0)
    giro = 2 * g2 - g1  # extrapolacion de Richardson a distancia infinita
    delta = 2 * math.asin(1 / e)
    print(f"Prueba 2: giro entre asintotas (Kepler, +/-2e4 y 4e4 d, extrapolado) = {math.degrees(giro):.6f} grados ; formula = {math.degrees(delta):.6f} grados")
    assert abs(giro - delta) < 1e-6
    # Prueba 3: RK4 frente a Kepler
    r4, v4 = rk4_dosc([rp, 0, 0], [0, vp, 0], 20.0, int(20 * 86400 / 20.0), GMJ)
    rk, vk = kepler_prop([rp, 0, 0], [0, vp, 0], 20 * 86400.0, GMJ)
    d = math.dist(r4, rk)
    print(f"Prueba 3: |RK4 - Kepler| tras 20 d = {d:.4f} km")
    assert d < 10.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
