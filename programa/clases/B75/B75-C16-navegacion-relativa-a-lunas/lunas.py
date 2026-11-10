#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C16: escalas de un sistema de lunas (lunas galileanas) y navegacion relativa a una luna.

Datos consultados (2026-11-10): GM y radio medio de Io, Europa, Ganimedes y Calisto (JPL SSD, parametros fisicos de satelites); semiejes y periodos siderales (JPL SSD, elementos medios, epoca 2000-01-01.5 TDB);
masa de Jupiter 1898.13e24 kg (ficha NASA/NSSDC); G = 6.67430e-11 (registro de cambios del JPL); GM_Jupiter = G M se CALCULA aqui.
SINTETICO: la orbita de la nave alrededor de Jupiter (periapsis 5 R_J = 357 460 km, apoapsis 3 000 000 km) y el instante del encuentro; R_J = 71 492 km (JPL SSD).
Modelo: orbitas lunares circulares y coplanares (elementos medios, no para efemerides); la nave cruza cada orbita lunar con la velocidad de su elipse; sin perturbaciones.
Pruebas: (1) el periodo de Kepler con GM_Jupiter calculado reproduce el periodo de la tabla de cada luna (tol. 1 %; la diferencia es de unas decimas por ciento, atribuible a que dos cuerpos con a medio ignora el achatamiento de Jupiter: causa no verificada aqui); (2) la ida y vuelta al marco giratorio de la luna recupera el vector (tol. 1e-9 km);
(3) el radio de Hill de cada luna respecto a Jupiter es mayor que su radio medio.
"""
import math, platform
G = 6.67430e-20
GMJ = G * 1898.13e24
RJ = 71492.0
# nombre: (a [km], P [d], GM [km3/s2], R [km])
LUNAS = {
    "Io": (421800.0, 1.762732, 5959.91547, 1821.49),
    "Europa": (671100.0, 3.525463, 3202.71210, 1560.80),
    "Ganimedes": (1070400.0, 7.155588, 9887.83275, 2631.20),
    "Calisto": (1882700.0, 16.690440, 7179.28340, 2410.30),
}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"GM_Jupiter = G M = {GMJ:.1f} km3/s2")
    print(" luna       a [R_J]  v_orb [km/s]  P Kepler [d]  P tabla [d]  dif [%]   r_Hill [km]  r_Hill/R   v_esc sup. [km/s]")
    for n, (a, P, gm, R) in LUNAS.items():
        v = math.sqrt(GMJ / a)
        Pk = 2 * math.pi * math.sqrt(a**3 / GMJ) / 86400
        rh = a * (gm / (3 * GMJ)) ** (1 / 3)
        dif = 100 * (Pk - P) / P
        assert abs(dif) < 1.0 and rh > R
        print(f"{n:9s} {a/RJ:8.2f} {v:12.4f} {Pk:13.6f} {P:12.6f} {dif:8.3f} {rh:12.0f} {rh/R:9.2f} {math.sqrt(2*gm/R):14.4f}")
    # nave en una elipse jupiteriana sintetica
    rp, ra = 5 * RJ, 3.0e6
    a_o = 0.5 * (rp + ra); h = math.sqrt(2 * GMJ * rp * ra / (rp + ra))
    print(f"Orbita SINTETICA de la nave: rp = {rp:.0f} km, ra = {ra:.0f} km, P = {2*math.pi*math.sqrt(a_o**3/GMJ)/86400:.2f} d")
    print(" luna       v_nave [km/s]  v_radial  v_tangencial  v_luna   v_inf respecto a la luna [km/s]")
    for n, (a, P, gm, R) in LUNAS.items():
        v2 = GMJ * (2 / a - 1 / a_o); vt = h / a; assert rp <= a <= ra; vr = math.sqrt(v2 - vt * vt); vm = math.sqrt(GMJ / a)
        vinf = math.hypot(vr, vt - vm)
        print(f"{n:9s} {math.sqrt(v2):13.4f} {vr:9.4f} {vt:13.4f} {vm:8.4f} {vinf:26.4f}")
    # marco giratorio de Europa (sincrono: omega = 2 pi / P)
    a, P, gm, R = LUNAS["Europa"]
    w = 2 * math.pi / (P * 86400)
    t = 3.0 * 86400
    r_nave = [900000.0, 250000.0]
    ang = w * t
    pm = [a * math.cos(ang), a * math.sin(ang)]
    rel = [r_nave[0] - pm[0], r_nave[1] - pm[1]]
    c, s = math.cos(-ang), math.sin(-ang)
    rot = [c * rel[0] - s * rel[1], s * rel[0] + c * rel[1]]
    c2, s2 = math.cos(ang), math.sin(ang)
    back = [c2 * rot[0] - s2 * rot[1], s2 * rot[0] + c2 * rot[1]]
    err = math.dist(back, rel)
    print(f"Marco giratorio de Europa (omega = {w:.4e} rad/s) a t = 3 d: posicion relativa inercial ({rel[0]:.1f}, {rel[1]:.1f}) km -> giratorio ({rot[0]:.1f}, {rot[1]:.1f}) km ; ida y vuelta: error {err:.2e} km")
    assert err < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
