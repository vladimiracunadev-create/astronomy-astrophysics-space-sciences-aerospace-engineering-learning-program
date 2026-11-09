#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C19: mantenimiento y vida util, confiabilidad con redundancia, consumibles y degradacion.

Datos: g0 = 9,80665 m/s2 de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). TODO lo demas es ILUSTRATIVO (no son tasas de falla de ningun equipo ni de ninguna mision):
tasas de falla por anio de 0,02 (carga util y estructura), 0,10 (ordenador) y 0,05 (cada rueda de reaccion), ordenador en pareja con respaldo frio e interruptor perfecto,
ruedas 3 de 4, propulsor de 12 kg con Isp 220 s, mantenimiento de orbita de 10 m/s al anio sobre una masa inicial de 150 kg y degradacion de la potencia del 2,5 % anual.
Modelo: (1) R = exp(-lambda t) en serie; respaldo frio R = exp(-lambda t)(1 + lambda t); k de n por suma binomial; (2) Monte Carlo (semilla 20261109, 100000 sistemas) con tiempos
exponenciales frente a la confiabilidad analitica a 5 anios; (3) vida por tiempo hasta R = 0,8 (biseccion); (4) combustible por Tsiolkovsky m_p = m0 (1 - exp(-dv/(Isp g0)));
(5) potencia P(t) = P0 (1 - d)^t y tiempo hasta el 70 % de P0. La vida de la mision es el minimo de las vidas parciales.
Supuestos: fallas independientes, tasa constante (fase de vida util de la curva de la banera), conmutacion perfecta, sin reparacion. Validez: ilustrativa.
Tolerancia: Monte Carlo frente a analitica, 0,005 absoluto; combustible, 1e-9 relativo respecto del calculo inverso.
"""
from __future__ import annotations
import math, platform, random

G0 = 9.80665
L_PL, L_PC, L_RW = 0.02, 0.10, 0.05


def r_serie(t):
    r_pl = math.exp(-L_PL * t)
    r_pc = math.exp(-L_PC * t) * (1 + L_PC * t)
    e = math.exp(-L_RW * t)
    r_rw = 4 * e ** 3 * (1 - e) + e ** 4
    return r_pl, r_pc, r_rw, r_pl * r_pc * r_rw


def simula(t, n, rng):
    ok = 0
    for _ in range(n):
        if rng.expovariate(L_PL) < t:
            continue
        a, b = rng.expovariate(L_PC), rng.expovariate(L_PC)
        if a + b < t:                     # respaldo frio: vida = suma de dos tiempos
            continue
        vivas = sum(1 for _ in range(4) if rng.expovariate(L_RW) >= t)
        if vivas < 3:
            continue
        ok += 1
    return ok / n


def t_para_r(objetivo):
    lo, hi = 0.0, 100.0
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if r_serie(m)[3] > objetivo:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def calc():
    r = {"filas": []}
    for t in (1, 2, 5, 8, 10):
        r["filas"].append((t,) + r_serie(t))
    rng = random.Random(20261109)
    r["mc5"] = simula(5.0, 100000, rng)
    r["an5"] = r_serie(5.0)[3]
    r["t80"] = t_para_r(0.8)
    isp, m0, dv = 220.0, 150.0, 10.0
    mp_ano = m0 * (1 - math.exp(-dv / (isp * G0)))
    r["mp_ano"] = mp_ano
    r["t_prop"] = 12.0 / mp_ano
    r["dv_inverso"] = isp * G0 * math.log(m0 / (m0 - mp_ano))
    r["t_pot"] = math.log(0.70) / math.log(1 - 0.025)
    r["vida"] = min(r["t80"], r["t_prop"], r["t_pot"])
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'t [anios]':>9} {'R carga':>9} {'R ordenador':>12} {'R ruedas 3/4':>13} {'R sistema':>10}")
    for t, a, b, c, d in r["filas"]:
        print(f"{t:9d} {a:9.4f} {b:12.4f} {c:13.4f} {d:10.4f}")
    print(f"R(5 anios): analitica = {r['an5']:.4f} ; Monte Carlo = {r['mc5']:.4f}")
    print(f"tiempo hasta R = 0.8: {r['t80']:.3f} anios")
    print(f"propulsor por anio = {r['mp_ano']:.4f} kg ; vida por propulsor = {r['t_prop']:.2f} anios ; dv inverso = {r['dv_inverso']:.6f} m/s")
    print(f"tiempo hasta 70 % de potencia = {r['t_pot']:.2f} anios")
    print(f"vida de la mision = minimo de las vidas parciales = {r['vida']:.3f} anios")
    assert abs(r["mc5"] - r["an5"]) < 0.005
    assert abs(r["dv_inverso"] - 10.0) / 10.0 < 1e-9
    assert r["vida"] == r["t80"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
