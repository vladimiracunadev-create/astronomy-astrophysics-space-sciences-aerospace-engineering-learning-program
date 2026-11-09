#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C02: ley de Snell, angulo critico, angulo de Brewster y reflectancia de Fresnel.

Datos: sin constantes fisicas. Los indices (aire 1,0003 y vidrio 1,517) son ILUSTRATIVOS, tipicos de libro, no consultados.
Modelo: n1 sen t1 = n2 sen t2; angulo critico asin(n2/n1) si n1 > n2; angulo de Brewster atan(n2/n1); reflectancias de Fresnel Rs y Rp para luz
no absorbida. Segunda via: la reflectancia en incidencia normal se compara con ((n1-n2)/(n1+n2))^2 y la conservacion de energia R + T = 1 se comprueba
integrando el flujo con la proyeccion del haz (T se calcula por separado con los coeficientes de transmision).
Supuestos: interfaz plana entre dielectricos transparentes, onda plana. Validez: optica geometrica mas coeficientes de Fresnel.
Tolerancia: R + T = 1 a 1e-12; Rp(Brewster) < 1e-20; normal frente a la formula cerrada a 1e-12.
"""
from __future__ import annotations
import math, platform, sys


def snell(n1, n2, t1):
    s = n1 * math.sin(t1) / n2
    return None if abs(s) > 1 else math.asin(s)


def fresnel(n1, n2, t1):
    t2 = snell(n1, n2, t1)
    if t2 is None:
        return 1.0, 1.0, 0.0, 0.0
    c1, c2 = math.cos(t1), math.cos(t2)
    rs = (n1 * c1 - n2 * c2) / (n1 * c1 + n2 * c2)
    rp = (n2 * c1 - n1 * c2) / (n2 * c1 + n1 * c2)
    ts = 2 * n1 * c1 / (n1 * c1 + n2 * c2)
    tp = 2 * n1 * c1 / (n2 * c1 + n1 * c2)
    f = n2 * c2 / (n1 * c1)           # cociente de flujos transmitidos
    return rs * rs, rp * rp, f * ts * ts, f * tp * tp


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n1, n2 = 1.0003, 1.517
    print("aire -> vidrio (indices ilustrativos)")
    print(f"{'t1 [deg]':>9} {'t2 [deg]':>9} {'Rs':>9} {'Rp':>9} {'R media':>9}")
    for g in (0, 20, 40, 56.6, 60, 80):
        t1 = math.radians(g)
        t2 = snell(n1, n2, t1)
        rs, rp, ts, tp = fresnel(n1, n2, t1)
        print(f"{g:9.1f} {math.degrees(t2):9.3f} {rs:9.5f} {rp:9.5f} {(rs+rp)/2:9.5f}")
        assert abs(rs + ts - 1) < 1e-12 and abs(rp + tp - 1) < 1e-12
    rs0, rp0, _, _ = fresnel(n1, n2, 0.0)
    cerrada = ((n1 - n2) / (n1 + n2)) ** 2
    print(f"incidencia normal: R = {rs0:.6f} ; formula cerrada = {cerrada:.6f}")
    assert abs(rs0 - cerrada) < 1e-12 and abs(rp0 - cerrada) < 1e-12
    tb = math.atan(n2 / n1)
    rsb, rpb, _, _ = fresnel(n1, n2, tb)
    print(f"angulo de Brewster = {math.degrees(tb):.4f} deg ; Rp = {rpb:.2e} ; Rs = {rsb:.5f}")
    assert rpb < 1e-20
    # reflexion total vidrio -> aire
    tc = math.asin(n1 / n2)
    print(f"vidrio -> aire: angulo critico = {math.degrees(tc):.4f} deg")
    for g in (tc - 0.001, tc + 0.001):
        rs, rp, ts, tp = fresnel(n2, n1, g)
        print(f"  t1 = {math.degrees(g):.4f} deg : Rs = {rs:.5f} Rp = {rp:.5f}")
    assert snell(n2, n1, tc + 0.001) is None
    # pila de capas: n sen t se conserva (invariante de Snell)
    capas = [1.0003, 1.333, 1.517, 1.333, 1.0003]
    t = math.radians(35.0)
    inv = capas[0] * math.sin(t)
    th = t
    for k in range(1, len(capas)):
        th = snell(capas[k - 1], capas[k], th)
        assert abs(capas[k] * math.sin(th) - inv) < 1e-12
    print(f"pila de 5 medios: invariante n sen t = {inv:.6f} ; angulo final = {math.degrees(th):.4f} deg (igual al inicial por simetria)")
    assert abs(math.degrees(th) - 35.0) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
