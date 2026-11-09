#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C12: curva de luz SINTETICA de una estrella con una mancha y recuperacion del periodo.

Datos: ninguno observado. Estrella, mancha, ruido y periodo son SINTETICOS (ilustrativos).
Modelo: esfera con una mancha circular de radio angular rho y contraste c = (T_m/T_ef)^4
(bolometrico, sin oscurecimiento al limbo). El flujo visible perdido es
dF = (1 - c) * Area_proyectada_de_la_mancha; F0 = pi R^2 (disco completo). La mancha rota con
periodo P, colatitud theta0, inclinacion i. Caso analitico: mancha centrada en el disco
(i = 90 grados, latitud 0, fase de cara): dF/F0 = (1 - c) sin^2(rho).
Periodograma de Lomb-Scargle clasico para recuperar P.
Supuestos: rotacion rigida, mancha estable, sin limbo oscuro ni evolucion. Validez: ilustrativa.
Tolerancia: 1e-3 relativa en el caso analitico; 1 % en el periodo recuperado.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def deficit(t, P, rho_deg, lat_deg, inc_deg, c, nr=40, na=72):
    """Fraccion de flujo perdida en el instante t (cuadratura sobre el casquete de la mancha)."""
    rho = math.radians(rho_deg)
    lat, inc = math.radians(lat_deg), math.radians(inc_deg)
    phi0 = 2 * math.pi * t / P
    # centro de la mancha en ejes del cuerpo -> ejes del observador (eje de rotacion z, inclinacion inc)
    cx, cy, cz = math.cos(lat) * math.cos(phi0), math.cos(lat) * math.sin(phi0), math.sin(lat)
    # base ortonormal del casquete
    ux, uy, uz = -math.sin(phi0), math.cos(phi0), 0.0
    vx, vy, vz = cy * uz - cz * uy, cz * ux - cx * uz, cx * uy - cy * ux
    los = (math.sin(inc), 0.0, math.cos(inc))
    tot = 0.0
    for i in range(nr):
        a = (i + 0.5) * rho / nr           # distancia angular al centro
        da = rho / nr
        for j in range(na):
            b = 2 * math.pi * (j + 0.5) / na
            sa, ca = math.sin(a), math.cos(a)
            px = ca * cx + sa * (math.cos(b) * ux + math.sin(b) * vx)
            py = ca * cy + sa * (math.cos(b) * uy + math.sin(b) * vy)
            pz = ca * cz + sa * (math.cos(b) * uz + math.sin(b) * vz)
            mu = px * los[0] + py * los[1] + pz * los[2]
            if mu > 0:
                tot += mu * sa * da * (2 * math.pi / na)   # area proyectada (R = 1)
    return (1 - c) * tot / math.pi


def lomb_scargle(t, y, periodos):
    n = len(t)
    m = sum(y) / n
    yy = [v - m for v in y]
    mejor, pbest = -1.0, None
    for P in periodos:
        w = 2 * math.pi / P
        s2 = sum(math.sin(2 * w * ti) for ti in t)
        c2 = sum(math.cos(2 * w * ti) for ti in t)
        tau = math.atan2(s2, c2) / (2 * w)
        cs = [math.cos(w * (ti - tau)) for ti in t]
        sn = [math.sin(w * (ti - tau)) for ti in t]
        pc = sum(a * b for a, b in zip(yy, cs)) ** 2 / sum(a * a for a in cs)
        ps = sum(a * b for a, b in zip(yy, sn)) ** 2 / sum(a * a for a in sn)
        p = pc + ps
        if p > mejor:
            mejor, pbest = p, P
    return pbest


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c = (4500.0 / 5772.0) ** 4
    rho = 10.0
    d = deficit(0.0, 10.0, rho, 0.0, 90.0, c, nr=80, na=144)
    esperado = (1 - c) * math.sin(math.radians(rho)) ** 2
    assert abs(d / esperado - 1) < 1e-3, "caso analitico: mancha centrada"
    print(f"contraste c = (4500/5772)^4 = {c:.4f}")
    print(f"mancha centrada (rho=10 grados): numerico = {d:.6f} ; (1-c) sin^2(rho) = {esperado:.6f}")
    rng = random.Random(12)
    P_ver = 10.0
    t = [i * 0.25 for i in range(160)]   # 40 dias, cadencia 0.25 d
    y = [1.0 - deficit(ti, P_ver, rho, 30.0, 60.0, c, nr=12, na=24) + rng.gauss(0, 2e-4) for ti in t]
    amp = max(y) - min(y)
    periodos = [4 + 0.02 * k for k in range(0, 600)]
    p_rec = lomb_scargle(t, y, periodos)
    assert abs(p_rec / P_ver - 1) < 0.01, "periodo no recuperado"
    print(f"curva sintetica (i=60, lat=30, rho=10): amplitud pico a pico = {amp * 1e6:.0f} ppm")
    print(f"periodo verdadero = {P_ver} d ; recuperado = {p_rec:.2f} d")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
