#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C21: paso cercano a Europa en integracion de N cuerpos: paso fijo frente a paso adaptativo y deflexion hiperbolica analitica.

Datos consultados (2026-11-10): GM de Europa 3202.71210 km3/s2 y radio medio 1560.8 km (JPL SSD, JUP365); GM de Jupiter 126.687e6 km3/s2 (NASA/NSSDC, Jupiter Fact Sheet);
semieje medio de Europa 671 100 km (JPL SSD, elementos medios, J2000).
SINTETICO: el cuerpo de prueba (velocidad en el infinito v_inf = 5 km/s, altura de periapsis 100 km sobre la superficie, partida a r0 = 0.5 R_H de Europa);
no es una trayectoria de mision.
Modelo: encuentro en el marco de Europa, solo la gravedad de Europa (se acota la perturbacion de la marea de Jupiter); solucion analitica de la hiperbola
(e = 1 + r_p v_inf^2 / GM, deflexion delta = 2 arcsin(1/e), tiempo de vuelo por la ecuacion de Kepler hiperbolica).
Integradores: leapfrog de paso fijo, RK4 de paso fijo y RK4 con paso adaptativo dt = eta min(r/|v|, sqrt(r^3/GM)).
Segunda via: la propia solucion analitica (estado final en la anomalia verdadera simetrica) y conservacion de la energia.
Tolerancias: RK4 adaptativo con eta = 0.003: error de angulo de salida < 1e-4 grados y de posicion < 1 km; el paso fijo de 60 s debe errar > 100 veces mas que ese caso. La deflexion se compara con el angulo entre las velocidades analiticas en -f0 y +f0 (r0 finito).
"""
from __future__ import annotations
import json, math, platform, sys

GM_E, R_E = 3202.71210, 1560.8
GM_J, A_E = 126.687e6, 671100.0
RH = A_E * (GM_E / (3 * GM_J)) ** (1 / 3)
VINF = 5.0
RP = R_E + 100.0
R0 = 0.5 * RH
EXC = 1 + RP * VINF**2 / GM_E
P = RP * (1 + EXC)
H = math.sqrt(GM_E * P)


def estado(f):
    r = P / (1 + EXC * math.cos(f))
    return [r * math.cos(f), r * math.sin(f), -GM_E / H * math.sin(f), GM_E / H * (EXC + math.cos(f))]


F0 = math.acos((P / R0 - 1) / EXC)


def tiempo_vuelo():
    a = GM_E / VINF**2
    Hh = 2 * math.atanh(math.sqrt((EXC - 1) / (EXC + 1)) * math.tan(F0 / 2))
    M = EXC * math.sinh(Hh) - Hh
    n = math.sqrt(GM_E / a**3)
    return 2 * M / n


def f_der(s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return [vx, vy, -GM_E * x / r3, -GM_E * y / r3]


def rk4(s, h):
    k1 = f_der(s)
    k2 = f_der([a + 0.5 * h * b for a, b in zip(s, k1)])
    k3 = f_der([a + 0.5 * h * b for a, b in zip(s, k2)])
    k4 = f_der([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def leap(s, h):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    vx -= 0.5 * h * GM_E * x / r3
    vy -= 0.5 * h * GM_E * y / r3
    x += h * vx
    y += h * vy
    r3 = (x * x + y * y) ** 1.5
    vx -= 0.5 * h * GM_E * x / r3
    vy -= 0.5 * h * GM_E * y / r3
    return [x, y, vx, vy]


def energia(s):
    return 0.5 * (s[2] ** 2 + s[3] ** 2) - GM_E / math.hypot(s[0], s[1])


def integrar(metodo, dt=None, eta=None):
    s = estado(-F0)
    T = tiempo_vuelo()
    t, n = 0.0, 0
    paso_min = 1e9
    while t < T - 1e-9:
        if eta is not None:
            r = math.hypot(s[0], s[1])
            v = math.hypot(s[2], s[3])
            h = eta * min(r / v, math.sqrt(r**3 / GM_E))
        else:
            h = dt
        h = min(h, T - t)
        if h < paso_min and t + h < T - 1e-9:
            paso_min = h
        s = (rk4 if metodo != "leapfrog" else leap)(s, h)
        t += h
        n += 1
    return s, n, paso_min


def angulo(v1, v2):
    return math.degrees(math.atan2(v1[0] * v2[1] - v1[1] * v2[0], v1[0] * v2[0] + v1[1] * v2[1]))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    T = tiempo_vuelo()
    delta = math.degrees(2 * math.asin(1 / EXC))
    vp = math.sqrt(VINF**2 + 2 * GM_E / RP)
    print(f"Europa: R_H = {RH:,.0f} km ; r0 = {R0:,.0f} km ; r_p = {RP:.1f} km ; e = {EXC:.4f} ; v_p = {vp:.4f} km/s ; deflexion analitica = {delta:.4f} grados ; tiempo de vuelo = {T:.1f} s")
    mar_r0 = 2 * GM_J * R0 / A_E**3 / (GM_E / R0**2)
    mar_rp = 2 * GM_J * RP / A_E**3 / (GM_E / RP**2)
    print(f"Cota de la marea de Jupiter respecto de la gravedad de Europa: a r0 = {mar_r0:.1%} ; en el periapsis = {mar_rp:.2%} (se desprecia en el modelo)")
    out.update(rh=RH, r0=R0, rp=RP, exc=EXC, vp=vp, delta=delta, T=T, mar0=mar_r0, marp=mar_rp)
    sfin = estado(F0)
    d_an = angulo(estado(-F0)[2:], sfin[2:])
    print(f"Angulo entre las velocidades analiticas en -f0 y +f0 (r0 finito) = {d_an:.4f} grados (la deflexion asintotica es {delta:.4f})")
    out['d_an'] = d_an
    e0 = energia(estado(-F0))
    print(" metodo      parametro      pasos   paso minimo [s]   error posicion [km]   error velocidad [m/s]   error deflexion [grados]   error energia")
    res = {}
    casos = [("leapfrog", "dt=60 s", dict(dt=60.0)), ("leapfrog", "dt=20 s", dict(dt=20.0)), ("rk4", "dt=60 s", dict(dt=60.0)), ("rk4", "dt=20 s", dict(dt=20.0)),
             ("rk4", "dt=5 s", dict(dt=5.0)), ("rk4 adaptativo", "eta=0.01", dict(eta=0.01)), ("rk4 adaptativo", "eta=0.003", dict(eta=0.003))]
    for nom, par, kw in casos:
        s, n, hm = integrar("rk4" if "rk4" in nom else "leapfrog", **kw)
        ep = math.hypot(s[0] - sfin[0], s[1] - sfin[1])
        ev = math.hypot(s[2] - sfin[2], s[3] - sfin[3]) * 1000
        v_in = estado(-F0)[2:]
        d_num = angulo(v_in, s[2:])
        ed = abs(d_num - d_an)
        ee = abs(energia(s) / e0 - 1)
        print(f" {nom:14s} {par:10s} {n:7d}   {hm:13.2f}   {ep:17.3e}   {ev:19.3e}   {ed:22.3e}   {ee:11.2e}")
        key = (nom.replace(" ", "_") + "_" + par.replace("=", "").replace(" ", "").replace(".", "p"))
        res[key] = (n, ep, ed)
        out[key + "_n"], out[key + "_ep"], out[key + "_ed"], out[key + "_ee"], out[key + "_hm"] = n, ep, ed, ee, hm
    ad = res["rk4_adaptativo_eta0p003"]
    ad1 = res["rk4_adaptativo_eta0p01"]
    f5 = res["rk4_dt5s"]
    fijo = res["rk4_dt60s"]
    out["ratio"] = fijo[1] / ad[1]
    print(f"RK4 con dt = 60 s frente a RK4 adaptativo (eta = 0.003): error de posicion {fijo[1] / ad[1]:.0f} veces mayor con {fijo[0]} pasos frente a {ad[0]}")
    print(f"A coste similar: RK4 dt = 5 s ({f5[0]} pasos, error {f5[1]:.1e} km) frente a RK4 adaptativo eta = 0.01 ({ad1[0]} pasos, error {ad1[1]:.1e} km): ahorro de pasos = {1 - ad1[0] / f5[0]:.0%}")
    out["ahorro"] = 1 - ad1[0] / f5[0]
    out["n5"], out["e5"], out["na1"], out["ea1"] = f5[0], f5[1], ad1[0], ad1[1]
    assert ad[2] < 1e-4 and ad[1] < 1.0
    assert fijo[1] > 100 * ad[1]
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
