#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C18: satelites irregulares de Jupiter y Saturno: fraccion de la esfera de Hill, inclinacion y estabilidad prograda/retrograda.

Datos consultados (2026-11-10): semieje, excentricidad e inclinacion de Himalia (11 461 000 km; 0.162; 27.50), Elara (11 741 000; 0.217; 26.63),
Leda (11 165 000; 0.164; 27.46), Lysithea (11 717 000; 0.112; 28.30), Ananke (21 276 000; 0.244; 148.9), Carme (23 404 000; 0.253; 164.9),
Pasiphae (23 624 000; 0.409; 151.4) y Sinope (23 939 000; 0.250; 158.1) (NASA/NSSDC, Jovian Satellite Fact Sheet, 2023-12-06); Phoebe: 12 944 000 km,
e = 0.164, i = 174.8 (NASA/NSSDC, Saturnian Satellite Fact Sheet, 2025-07-22); GM de Jupiter 126.687e6 km3/s2, semieje 778.479e6 km (Jupiter Fact Sheet, 2024-10-02);
GM del Sol 132 712e6 km3/s2 (Sun Fact Sheet, 2024-05-09). Radio ecuatorial de Jupiter 71 492 km (Jupiter Fact Sheet).
SINTETICO: las particulas de prueba de la simulacion (orbitas circulares iniciales a distintas fracciones del radio de Hill, fase 0).
Modelo: radio de Hill R_H = a_J (GM_J / (3 GM_S))^(1/3). Simulacion: problema restringido de tres cuerpos circular plano Sol-Jupiter (mu = GM_J/(GM_S+GM_J)),
marco sinodico, RK4 dt = 2e-3, 40 anos de Jupiter (251 unidades); la particula parte a f R_H de Jupiter con velocidad circular kepleriana respecto de Jupiter,
prograda (+) o retrograda (-); escapa si su distancia a Jupiter supera 1.5 R_H. Inclinacion critica de Kozai arccos(sqrt(3/5)) (formula clasica, no consultada).
Segunda via: (a) R_H frente a la distancia a L1 resuelta numericamente; (b) conservacion de la constante de Jacobi en la simulacion.
Tolerancias: |R_H - L1| / R_H < 5 % ; Jacobi < 1e-6 (solo en las trayectorias que no escapan: tras un encuentro cercano o la salida, RK4 de paso fijo pierde exactitud).
"""
from __future__ import annotations
import json, math, platform, sys

GM_J, GM_S, A_J = 126.687e6, 132712e6, 778.479e6
MU = GM_J / (GM_S + GM_J)
RH_ADIM = (GM_J / (3 * GM_S)) ** (1 / 3)
RH_KM = A_J * RH_ADIM
R_JUP = 71492.0
LUNAS = [("Leda", 11165e3, 0.164, 27.46), ("Himalia", 11461e3, 0.162, 27.50), ("Lysithea", 11717e3, 0.112, 28.30), ("Elara", 11741e3, 0.217, 26.63),
         ("Ananke", 21276e3, 0.244, 148.9), ("Carme", 23404e3, 0.253, 164.9), ("Pasiphae", 23624e3, 0.409, 151.4), ("Sinope", 23939e3, 0.250, 158.1),
         ("Phoebe (Saturno)", 12944e3, 0.164, 174.8)]


def f(s):
    x, y, vx, vy = s
    r1 = math.hypot(x + MU, y)
    r2 = math.hypot(x - 1 + MU, y)
    return [vx, vy, 2 * vy + x - (1 - MU) * (x + MU) / r1**3 - MU * (x - 1 + MU) / r2**3, -2 * vx + y - (1 - MU) * y / r1**3 - MU * y / r2**3]


def rk4(s, h):
    k1 = f(s)
    k2 = f([a + 0.5 * h * b for a, b in zip(s, k1)])
    k3 = f([a + 0.5 * h * b for a, b in zip(s, k2)])
    k4 = f([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


def jacobi(s):
    x, y, vx, vy = s
    return x * x + y * y + 2 * (1 - MU) / math.hypot(x + MU, y) + 2 * MU / math.hypot(x - 1 + MU, y) - vx * vx - vy * vy


def L1():
    g = lambda x: x - (1 - MU) * (x + MU) / abs(x + MU) ** 3 - MU * (x - 1 + MU) / abs(x - 1 + MU) ** 3
    a, b = -MU + 1e-9, 1 - MU - 1e-9
    for _ in range(200):
        m = 0.5 * (a + b)
        if g(a) * g(m) <= 0:
            b = m
        else:
            a = m
    return 0.5 * (a + b)


def simular(fr, signo, T=251.0, dt=2e-3):
    a = fr * RH_ADIM
    # posicion: sobre el eje x alejandose del Sol; velocidad circular respecto de Jupiter en el marco inercial
    x, y = 1 - MU + a, 0.0
    vrel = signo * math.sqrt(MU / a)  # tangencial (en +y para prograda)
    # velocidad en el marco giratorio: v_in - omega x r = (0, vrel + (1 - MU)) ... para el punto del eje: (vx, vy) = (0, v_in_y - x)
    vy = (vrel + (1 - MU)) - x
    s = [x, y, 0.0, vy]
    C0 = jacobi(s)
    dC = 0.0
    n = int(T / dt)
    for i in range(1, n + 1):
        s = rk4(s, dt)
        d = math.hypot(s[0] - (1 - MU), s[1])
        if d > 1.5 * RH_ADIM:
            return i * dt, dC
        if i % 500 == 0:
            dC = max(dC, abs(jacobi(s) - C0))
    return None, dC


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print(f"R_H = a_J (GM_J / 3 GM_S)^(1/3) = {RH_KM:,.0f} km ({RH_ADIM:.5f} a_J) ; radio de Jupiter = {R_JUP:.0f} km")
    l1 = (1 - MU - L1())
    print(f"Segunda via: distancia de L1 a Jupiter (CR3BP) = {l1:.5f} a_J = {l1 * A_J:,.0f} km ; diferencia con R_H = {abs(l1 - RH_ADIM) / RH_ADIM:.2%}")
    out.update(rh=RH_KM, rh_adim=RH_ADIM, l1=l1 * A_J, l1dif=abs(l1 - RH_ADIM) / RH_ADIM, mu=MU)
    kozai = math.degrees(math.acos(math.sqrt(3 / 5)))
    print(f"Inclinacion critica de Kozai: {kozai:.2f} y {180 - kozai:.2f} grados")
    out["kozai"] = kozai
    print(" satelite              a [km]      a/R_H   (1+e)a/R_H   i [grados]  sentido      en (Kozai, 180-Kozai)?")
    for nom, a, e, inc in LUNAS:
        rh = RH_KM if "Saturno" not in nom else None
        sentido = "retrogrado" if inc > 90 else "prógrado"
        if rh:
            print(f" {nom:20s} {a:11,.0f}   {a / rh:6.3f}   {(1 + e) * a / rh:9.3f}   {inc:9.2f}   {sentido:10s}   {'si' if kozai < inc < 180 - kozai else 'no'}")
        else:
            print(f" {nom:20s} {a:11,.0f}   (el R_H de Saturno no se calcula aqui)        {inc:9.2f}   {sentido:10s}   {'si' if kozai < inc < 180 - kozai else 'no'}")
    dentro = [n for n, a, e, inc in LUNAS if kozai < inc < 180 - kozai]
    out["dentro"] = len(dentro)
    out["amax_ra"] = max((1 + e) * a / RH_KM for n, a, e, inc in LUNAS if "Saturno" not in n)
    out["pas"] = 23624e3 / RH_KM
    out["him"] = 11461e3 / RH_KM
    print(f"Satelites de la lista con inclinacion entre {kozai:.1f} y {180 - kozai:.1f}: {len(dentro)}")
    print("Simulacion CR3BP Sol-Jupiter (particulas SINTETICAS circulares, 40 anos de Jupiter; escape si d > 1.5 R_H):")
    print("   f = a/R_H   prograda: escape en [anos]   retrograda: escape en [anos]   dC prograda  dC retrograda")
    dCmax = 0.0
    res = {}
    for fr in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        tp, dcp = simular(fr, +1)
        tr, dcr = simular(fr, -1)
        if tp is None:
            dCmax = max(dCmax, dcp)
        if tr is None:
            dCmax = max(dCmax, dcr)
        fmt = lambda t: "no escapa" if t is None else f"{t / (2 * math.pi):.2f}"
        print(f"   {fr:6.2f}       {fmt(tp):>18s}            {fmt(tr):>18s}          {dcp:9.1e}   {dcr:9.1e}")
        res[fr] = (tp, tr)
    out["dCmax"] = dCmax
    fp = next((fr for fr in sorted(res) if res[fr][0] is not None), None)
    fr_ = next((fr for fr in sorted(res) if res[fr][1] is not None), None)
    out["fp"], out["fr"] = fp if fp else 0.0, fr_ if fr_ else 0.0
    print(f"Primera fraccion de R_H con escape: prograda = {fp} ; retrograda = {fr_}")
    assert out["l1dif"] < 0.05 and dCmax < 1e-6
    assert fp is not None and (fr_ is None or fr_ > fp)
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
