#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C22: capturas temporales y cuasi-satelites: clasificacion de orbitas coorbitales en el CR3BP Sol-Tierra.

Datos consultados (2026-11-10): GM del Sol 132 712 x 10^6 km3/s2 (NASA/NSSDC, Sun Fact Sheet, 2024-05-09); distancia Sol-Tierra 149.6 x 10^6 km (NASA/NSSDC, Planetary Fact Sheet, 2025-03-18).
GM de la Tierra ~ 398 600 km3/s2: deducido de la masa de la tabla de planetas del JPL (aproximado). mu = GM_T / (GM_S + GM_T).
SINTETICAS: todas las condiciones iniciales (radio, fase, factor de velocidad) y las partículas de prueba; ningun asteroide real.
Modelo: CR3BP plano Sol-Tierra en el marco sinodico adimensional; RK4 con dt = 0.01 (clasificacion, 200 anos = 1257 unidades) o 0.002 (capturas).
Clasificacion con el angulo theta = angulo heliocentrico respecto de la Tierra (sin envolver): tadpole si theta queda en (0, pi) o (-pi, 0) sin cruzar 0 ni pi;
herradura si theta cubre pi sin cruzar 0 ni 2 pi (rango < 2 pi); cuasi-satelite si theta cruza 0 con rango < pi/2 y la distancia maxima a la Tierra < 15 R_H; otro caso: circulante o dispersada.
Capturas temporales: particulas a 0.5 R_H de la Tierra con velocidad circular (respecto de la Tierra) multiplicada por un factor, progradas y retrogradas; escape si d > 2 R_H.
Segunda via: deriva de la constante de Jacobi en cada simulacion y conteo de cruces del angulo.
Tolerancias: deriva de Jacobi < 1e-7 en las clasificaciones que no pasan cerca de la Tierra (d_min > 1 R_H).
"""
from __future__ import annotations
import json, math, platform, sys

GM_S, GM_E, AU = 132712e6, 398600.0, 149.6e6
MU = GM_E / (GM_S + GM_E)
RH = (MU / 3) ** (1 / 3)


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


def inicial(rho, th, k):
    x, y = -MU + rho * math.cos(th), rho * math.sin(th)
    vin = k * math.sqrt((1 - MU) / rho)
    return [x, y, -vin * math.sin(th) + y, vin * math.cos(th) - x]


def clasificar(rho, th, k, T=1257.0, h=0.01):
    s = inicial(rho, th, k)
    C0 = jacobi(s)
    n = int(T / h)
    unw, prev = None, None
    tmin, tmax = 9e9, -9e9
    dmin, dmax, dC, cruces, last = 9.0, 0.0, 0.0, 0, None
    for i in range(1, n + 1):
        s = rk4(s, h)
        ang = math.atan2(s[1], s[0] + MU)
        if prev is None:
            unw = ang
        else:
            d = ang - prev
            if d > math.pi:
                d -= 2 * math.pi
            if d < -math.pi:
                d += 2 * math.pi
            unw += d
        prev = ang
        tmin, tmax = min(tmin, unw), max(tmax, unw)
        dd = math.hypot(s[0] - 1 + MU, s[1])
        dmin, dmax = min(dmin, dd), max(dmax, dd)
        sg = 1 if unw > 0 else -1
        if last is not None and sg != last:
            cruces += 1
        last = sg
        if i % 1000 == 0:
            dC = max(dC, abs(jacobi(s) - C0))
    rango = tmax - tmin
    if tmin > 0 and tmax < math.pi or tmax < 0 and tmin > -math.pi:
        tipo = "tadpole"
    elif tmin > 0 and math.pi < tmax < 2 * math.pi:
        tipo = "herradura"
    elif tmin < 0 < tmax and rango < math.pi / 2 and dmax < 15 * RH:
        tipo = "cuasi-satelite"
    else:
        tipo = "circulante/dispersada"
    return tipo, math.degrees(tmin), math.degrees(tmax), dmin / RH, dmax / RH, cruces, dC


def captura(factor, signo, T=63.0, dt=0.002):
    r_rel = 0.5 * RH
    vc = signo * factor * math.sqrt(MU / r_rel)
    x, y = 1 - MU + r_rel, 0.0
    s = [x, y, 0.0, vc - r_rel]  # v_giratoria = v_rel_inercial - (-y_rel, x_rel) = (0, vc - r_rel)
    n = int(T / dt)
    for i in range(1, n + 1):
        s = rk4(s, dt)
        if math.hypot(s[0] - 1 + MU, s[1]) > 2 * RH:
            return i * dt / (2 * math.pi)
    return None


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    print(f"mu = {MU:.6e} ; R_H = {RH:.5f} UA = {RH * AU:,.0f} km")
    out.update(mu=MU, rh=RH, rh_km=RH * AU)
    print("Clasificacion de orbitas coorbitales (particulas SINTETICAS; 200 anos):")
    print(" caso                                 rho      theta0  k       tipo                 theta en [grados]           d/R_H min..max    cruces de 0   deriva C")
    casos = [("tadpole (L4)", 1.0, 50.0, 1.0, "tad"), ("herradura delta=0.002", 1.002, 20.0, 1.0, "h1"), ("herradura delta=0.004", 1.004, 20.0, 1.0, "h2"),
             ("herradura delta=0.01", 1.01, 20.0, 1.0, "h3"), ("cuasi-satelite e=0.05", 0.95, 0.0001, math.sqrt(1.05), "q5"), ("e=0.02 (encuentros con la Tierra)", 0.98, 0.0001, math.sqrt(1.02), "q2")]
    dCmax_ok = 0.0
    for nom, rho, th, k, tag in casos:
        tipo, a, b, d1, d2, cr, dC = clasificar(rho, math.radians(th), k)
        print(f" {nom:36s} {rho:6.3f}  {th:7.4f} {k:6.4f}  {tipo:20s} [{a:9.1f}, {b:10.1f}]   {d1:6.2f}..{d2:7.2f}   {cr:9d}   {dC:9.1e}")
        out[f"{tag}_tipo"], out[f"{tag}_tmin"], out[f"{tag}_tmax"], out[f"{tag}_dmin"], out[f"{tag}_dmax"], out[f"{tag}_cr"], out[f"{tag}_dC"] = tipo, a, b, d1, d2, cr, dC
        if d1 > 1.0:
            dCmax_ok = max(dCmax_ok, dC)
    out["dCmax"] = dCmax_ok
    print("Capturas temporales: particulas SINTETICAS a 0.5 R_H de la Tierra, velocidad circular geocentrica x factor; escape si d > 2 R_H (anos hasta el escape; '>10' = no escapa en 10 anos):")
    print("  factor      prograda   retrograda")
    caps = {}
    for fac in (0.6, 0.8, 1.0, 1.2, 1.4):
        tp, tr = captura(fac, +1), captura(fac, -1)
        fm = lambda t: ">10" if t is None else f"{t:.2f}"
        print(f"  {fac:5.1f}   {fm(tp):>10s}   {fm(tr):>10s}")
        caps[fac] = (tp, tr)
        out[f"cp_{int(fac * 10)}"], out[f"cr_{int(fac * 10)}"] = (tp if tp is not None else -1.0), (tr if tr is not None else -1.0)
    assert out["tad_tipo"] == "tadpole" and out["h1_tipo"] == out["h2_tipo"] == out["h3_tipo"] == "herradura" and out["q5_tipo"] == "cuasi-satelite"
    assert dCmax_ok < 1e-7
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
