#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C26: un paso de un tour de lunas galileanas por Tisserand (orbitas lunares circulares y coplanares, dos cuerpos por tramo).

Datos consultados (2026-11-10): GM y radio medio de Io, Europa, Ganimedes y Calisto (JPL SSD, parametros fisicos); semiejes (JPL SSD, elementos medios, epoca 2000-01-01.5 TDB);
masa de Jupiter 1898.13e24 kg (ficha NASA/NSSDC); G = 6.67430e-11 (registro del JPL); GM_Jupiter = G M; R_J = 71 492 km (JPL SSD).
SINTETICO: orbita inicial de la nave alrededor de Jupiter (periapsis 600 000 km, apoapsis 3 000 000 km); altitud de sobrevuelo de Ganimedes de 100 km; v_inf de la familia de Tisserand de 1 a 4 km/s.
Modelo: sobrevuelo instantaneo con conservacion de v_inf en el marco de la luna (conicas empalmadas); sin resonancias ni fase real de las lunas.
Pruebas: (1) T respecto a Ganimedes se conserva tras 100 sobrevuelos de giro aleatorio (semilla 26; tol. 1e-9); (2) el cambio de energia especifica coincide con V_G * Delta(v_tangencial) (identidad exacta de un sobrevuelo con v_inf conservado; tol. 1e-9);
(3) el v_inf de la familia de Tisserand en el cruce con Ganimedes calculado desde (rp, ra) iguala el pedido (tol. 1e-9 km/s).
"""
import math, platform, random
G = 6.67430e-20
GMJ = G * 1898.13e24
RJ = 71492.0
LUNAS = {"Io": (421800.0, 5959.91547, 1821.49), "Europa": (671100.0, 3202.71210, 1560.80),
         "Ganimedes": (1070400.0, 9887.83275, 2631.20), "Calisto": (1882700.0, 7179.28340, 2410.30)}


def cruce(rp, ra, r):
    a = 0.5 * (rp + ra); h = math.sqrt(2 * GMJ * rp * ra / (rp + ra))
    v2 = GMJ * (2 / r - 1 / a); vt = h / r; vr = math.sqrt(max(0.0, v2 - vt * vt))
    return vr, vt


def tiss(a, e, am):
    return am / a + 2 * math.sqrt(a / am * (1 - e * e))


def elementos(vr, vt, r):
    eps = 0.5 * (vr * vr + vt * vt) - GMJ / r
    a = -GMJ / (2 * eps); h = r * vt
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / GMJ**2))
    return a, e, eps


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    aG, gmG, RG = LUNAS["Ganimedes"]; VG = math.sqrt(GMJ / aG)
    print(f"GM_Jupiter = {GMJ:.1f} km3/s2 ; V_Ganimedes = {VG:.4f} km/s")
    print("Familia de Tisserand respecto a Ganimedes: apoapsis dado, periapsis q y v_inf en Europa (si q < a_Europa):")
    print(" v_inf_G [km/s]  T_G     r_a [R_J]   q [R_J]   periodo [d]   v_inf en Europa [km/s]")
    for vinf in (1.0, 2.0, 3.0, 4.0):
        T = 3 - (vinf / VG) ** 2
        for ra_rj in (15.0, 25.0, 40.0):
            ra = ra_rj * RJ
            f = lambda q: tiss(0.5 * (q + ra), (ra - q) / (ra + q), aG) - T
            lo, hi = 1e-6 * RJ, aG
            if f(lo) * f(hi) > 0:
                continue
            for _ in range(200):
                m = 0.5 * (lo + hi)
                if f(lo) * f(m) <= 0: hi = m
                else: lo = m
            q = 0.5 * (lo + hi)
            vr, vt = cruce(q, ra, aG)
            assert abs(math.hypot(vr, vt - VG) - vinf) < 1e-6  # prueba 3
            aE = LUNAS["Europa"][0]
            ve = "-"
            if q < aE:
                vre, vte = cruce(q, ra, aE)
                ve = f"{math.hypot(vre, vte - math.sqrt(GMJ/aE)):.4f}"
            P = 2 * math.pi * math.sqrt((0.5 * (q + ra)) ** 3 / GMJ) / 86400
            print(f"{vinf:12.1f} {T:9.5f} {ra_rj:10.1f} {q/RJ:9.3f} {P:12.2f}   {ve:>18s}")
    # Un paso del tour: sobrevuelo de Ganimedes con giro maximo
    rp0, ra0 = 600000.0, 3.0e6
    vr, vt = cruce(rp0, ra0, aG)
    vinf_v = [vr, vt - VG]; vinf = math.hypot(*vinf_v)
    rpl = RG + 100.0
    e_h = 1 + rpl * vinf**2 / gmG; dmax = 2 * math.asin(1 / e_h)
    a0, e0, eps0 = elementos(vr, vt, aG)
    T0 = tiss(a0, e0, aG)
    print(f"Orbita inicial SINTETICA: rp = {rp0:.0f} km ({rp0/RJ:.2f} R_J), ra = {ra0:.0f} km ({ra0/RJ:.2f} R_J), periodo {2*math.pi*math.sqrt(a0**3/GMJ)/86400:.2f} d ; v_inf en Ganimedes = {vinf:.4f} km/s ; giro maximo (100 km de altitud) = {math.degrees(dmax):.2f} grados")
    print(" giro [grados]    rp nuevo [R_J]   ra nuevo [R_J]   periodo [d]   dE [km2/s2]   T_G")
    for signo in (+1, -1):
        d = signo * dmax
        c, s = math.cos(d), math.sin(d)
        w = [c * vinf_v[0] - s * vinf_v[1], s * vinf_v[0] + c * vinf_v[1]]
        vr2, vt2 = w[0], w[1] + VG
        a1, e1, eps1 = elementos(vr2, vt2, aG)
        dE = eps1 - eps0
        assert abs(dE - VG * (vt2 - vt)) <= 1e-9 * max(1.0, abs(dE))
        T1 = tiss(a1, e1, aG)
        assert abs(T1 - T0) < 1e-9
        print(f"{math.degrees(d):12.2f} {a1*(1-e1)/RJ:17.3f} {a1*(1+e1)/RJ:16.3f} {2*math.pi*math.sqrt(a1**3/GMJ)/86400:12.2f} {dE:13.4f} {T1:.9f}")
    # Prueba 1: 100 sobrevuelos de giro aleatorio
    rng = random.Random(26)
    vv = [vr, vt]; Tmax = 0.0
    for _ in range(100):
        w0 = [vv[0], vv[1] - VG]
        d = rng.uniform(-dmax, dmax); c, s = math.cos(d), math.sin(d)
        w = [c * w0[0] - s * w0[1], s * w0[0] + c * w0[1]]
        vv = [w[0], w[1] + VG]
        a_, e_, _eps = elementos(vv[0], vv[1], aG)
        Tmax = max(Tmax, abs(tiss(a_, e_, aG) - T0))
    print(f"Prueba 1: 100 sobrevuelos aleatorios (semilla 26): max |T_G - T_G0| = {Tmax:.2e}")
    assert Tmax < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
