#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C02: marcos rotatorios sinodicos (inercial <-> giratorio), Coriolis, centrifuga y periodos sinodicos.

Datos consultados (2026-11-10): semieje mayor 384 400 km y periodo 27.322 d de la Luna; periodos de Io, Europa, Ganymede y Callisto
1.762732, 3.525463, 7.155588 y 16.690440 d (JPL SSD, tabla de elementos, epoca J2000); GM de la Luna 4902.800 km3/s2 (JPL SSD).
GM de la Tierra ~ 398 600 km3/s2: deducido de la masa de la tabla de planetas del JPL (aproximado).
SINTETICO: satelite en orbita circular inercial alrededor de la Tierra a 38 440 km (0.1 unidades); 2000 estados aleatorios con semilla 73.
Marco sinodico baricentrico: omega = n = 2 pi / P_Luna, ejes giratorios con los primarios en (-mu, 0) y (1-mu, 0); sentido antihorario.
Segunda via: derivacion numerica (diferencias centrales) de la posicion giratoria frente a la formula v_rot = R^T v_in - omega x r.
Tolerancias: ida y vuelta < 1e-12 ; velocidad por diferencias centrales frente a la formula < 1e-8 (adimensional).
"""
from __future__ import annotations
import json, math, platform, random, sys

P_LUNA, A_KM = 27.322, 384400.0
GM_L, GM_T = 4902.800, 398600.0
MU = GM_L / (GM_T + GM_L)
N_RAD_S = 2 * math.pi / (P_LUNA * 86400.0)
U_VEL = A_KM * N_RAD_S  # km/s
P_GAL = {"Io": 1.762732, "Europa": 3.525463, "Ganymede": 7.155588, "Callisto": 16.690440}


def a_rot(s, t):
    x, y, vx, vy = s
    c, sn = math.cos(t), math.sin(t)
    return [x * c - y * sn, x * sn + y * c, (vx - y) * c - (vy + x) * sn, (vx - y) * sn + (vy + x) * c]


def a_giratorio(s, t):
    X, Y, VX, VY = s
    c, sn = math.cos(t), math.sin(t)
    x, y = X * c + Y * sn, -X * sn + Y * c
    ux, uy = VX * c + VY * sn, -VX * sn + VY * c
    return [x, y, ux + y, uy - x]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"mu = {MU:.8f} ; n = {N_RAD_S:.6e} rad/s ; unidad de velocidad = {U_VEL:.5f} km/s")
    rnd = random.Random(73)
    emax = 0.0
    for _ in range(2000):
        s = [rnd.uniform(-1.5, 1.5) for _ in range(4)]
        t = rnd.uniform(0, 50)
        r = a_giratorio(a_rot(s, t), t)
        emax = max(emax, max(abs(a - b) for a, b in zip(s, r)))
    print(f"Ida y vuelta (2000 estados, semilla 73): error maximo = {emax:.2e}")
    # la Luna en el marco giratorio: fija; en el inercial: velocidad (1-mu) en unidades
    v_luna = (1 - MU) * U_VEL
    print(f"Luna: fija en (1-mu, 0) = ({1 - MU:.6f}, 0); en el marco inercial se mueve a {v_luna:.4f} km/s (baricentrico)")
    # satelite circular inercial alrededor de la Tierra
    rho = 0.1
    w = math.sqrt((1 - MU) / rho**3)  # velocidad angular inercial (solo la Tierra)
    def estado_in(t):
        ang = w * t
        # Tierra en el baricentro: posicion de la Tierra = (-mu cos t, -mu sin t)
        ex, ey = -MU * math.cos(t), -MU * math.sin(t)
        return [ex + rho * math.cos(ang), ey + rho * math.sin(ang), -MU * 0 - rho * w * math.sin(ang) + MU * math.sin(t), rho * w * math.cos(ang) - MU * math.cos(t)]
    t0, h = 1.3, 1e-6
    pos = lambda t: a_giratorio(estado_in(t), t)[:2]
    p_mas, p_menos = pos(t0 + h), pos(t0 - h)
    v_num = [(a - b) / (2 * h) for a, b in zip(p_mas, p_menos)]
    v_formula = a_giratorio(estado_in(t0), t0)[2:]
    dv = max(abs(a - b) for a, b in zip(v_num, v_formula))
    print(f"Velocidad giratoria: diferencias centrales {v_num[0]:.8f}, {v_num[1]:.8f} ; formula {v_formula[0]:.8f}, {v_formula[1]:.8f} ; diferencia = {dv:.2e}")
    x, y, vx, vy = a_giratorio(estado_in(t0), t0)
    v_in = math.hypot(*estado_in(t0)[2:])
    v_rot = math.hypot(vx, vy)
    acor = 2 * v_rot * U_VEL * N_RAD_S * 1e3  # m/s2
    acen = math.hypot(x, y) * A_KM * N_RAD_S**2 * 1e3
    print(f"Satelite sintetico a 38 440 km de la Tierra: |v_inercial| = {v_in * U_VEL:.4f} km/s ; |v_giratoria| = {v_rot * U_VEL:.4f} km/s")
    print(f"Aceleraciones aparentes (m/s2): Coriolis = {acor:.3e} ; centrifuga = {acen:.3e}")
    # periodos sinodicos de pares galileanos
    print("Periodos sinodicos (d), 1/Psin = |1/P1 - 1/P2| :")
    names = list(P_GAL)
    sin = {}
    for a, b in zip(names, names[1:]):
        ps = 1.0 / abs(1 / P_GAL[a] - 1 / P_GAL[b])
        sin[f"{a}-{b}"] = ps
        print(f"  {a}-{b}: {ps:.4f} d")
    assert emax < 1e-12 and dv < 1e-8
    assert abs(sin["Io-Europa"] - P_GAL["Europa"]) < 5e-3
    print("Pruebas superadas.")
    return {"python": platform.python_version(), "mu": MU, "n": N_RAD_S, "uvel": U_VEL, "emax": emax, "vluna": v_luna, "dv": dv,
            "vin": v_in * U_VEL, "vrot": v_rot * U_VEL, "acor": acor, "acen": acen, "s_ie": sin["Io-Europa"], "s_eg": sin["Europa-Ganymede"],
            "s_gc": sin["Ganymede-Callisto"]}


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
