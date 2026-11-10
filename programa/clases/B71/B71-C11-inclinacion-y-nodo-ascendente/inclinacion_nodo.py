#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C11: inclinacion y nodo ascendente desde el vector de estado, con el cuadrante correcto.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 (IAU 2015 B3).
DATOS SINTETICOS (semilla 71, random de la biblioteca estandar): 1000 estados con a en [7000, 42000] km, e en [0, 0.7], i en [0.1, 179.9] grados,
RAAN en [0, 360), omega en [0, 360), nu en [0, 360). Sistema: marco inercial geocentrico ECI idealizado (eje z = polo), SI. Dos cuerpos.
Modelo: h = r x v ; n = z x h ; i = acos(h_z/|h|) ; RAAN = atan2(n_y, n_x) mod 2 pi (cuadrante por atan2, no por acos).
Segunda via: elementos -> estado (matriz de rotacion 3-1-3 aplicada al sistema perifocal) -> elementos; se compara con los valores de partida.
Tolerancias: error angular de i y RAAN < 1e-9 rad para i en [0.1, 179.9] grados; latitud maxima = i (prograda) o 180 - i (retrograda) dentro de 1e-3 grados (muestreo de 3600 puntos).
"""
from __future__ import annotations
import math, platform, random

MU = 3.986004e14


def rot313(raan, inc, w):
    cO, sO, ci, si, cw, sw = math.cos(raan), math.sin(raan), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    return [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
            [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
            [sw * si, cw * si, ci]]


def mv(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def estado(a, e, inc, raan, w, nu):
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    rp_ = (r * math.cos(nu), r * math.sin(nu), 0.0)
    f = math.sqrt(MU / p)
    vp_ = (-f * math.sin(nu), f * (e + math.cos(nu)), 0.0)
    m = rot313(raan, inc, w)
    return mv(m, rp_), mv(m, vp_)


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def elementos_i_raan(r, v):
    h = cruz(r, v)
    hn = math.sqrt(sum(x * x for x in h))
    inc = math.acos(h[2] / hn)
    n = (-h[1], h[0], 0.0)  # z x h
    raan = math.atan2(n[1], n[0]) % (2 * math.pi)
    return inc, raan, h, n


def dang(a, b):
    d = abs(a - b) % (2 * math.pi)
    return min(d, 2 * math.pi - d)


def calcular():
    R = {}
    rnd = random.Random(71)
    emax_i = emax_O = 0.0
    n_casos = 1000
    cuad = [0, 0, 0, 0]
    retro = 0
    for _ in range(n_casos):
        a = rnd.uniform(7000e3, 42000e3)
        e = rnd.uniform(0.0, 0.7)
        inc = math.radians(rnd.uniform(0.1, 179.9))
        raan = math.radians(rnd.uniform(0.0, 360.0))
        w = math.radians(rnd.uniform(0.0, 360.0))
        nu = math.radians(rnd.uniform(0.0, 360.0))
        r, v = estado(a, e, inc, raan, w, nu)
        i2, O2, h, n = elementos_i_raan(r, v)
        emax_i = max(emax_i, abs(i2 - inc))
        emax_O = max(emax_O, dang(O2, raan))
        cuad[int(raan // (math.pi / 2)) % 4] += 1
        retro += inc > math.pi / 2
    R.update(n_casos=n_casos, emax_i=emax_i, emax_O=emax_O, cuad=cuad, retro=retro)
    # ejemplos concretos de cuadrante
    ej = []
    for ODeg in (30.0, 120.0, 210.0, 300.0):
        r, v = estado(7000e3, 0.01, math.radians(51.6), math.radians(ODeg), math.radians(40.0), math.radians(10.0))
        i2, O2, h, n = elementos_i_raan(r, v)
        ej.append((ODeg, math.degrees(O2), math.degrees(i2)))
    R["ej"] = ej
    R["ej_err"] = max(abs(x[0] - x[1]) for x in ej)
    # latitud maxima
    for nom, idg in (("pro", 51.6), ("sso", 97.8), ("ecu", 0.0)):
        inc = math.radians(idg)
        mx = 0.0
        for k in range(3600):
            u = 2 * math.pi * k / 3600
            mx = max(mx, abs(math.asin(math.sin(inc) * math.sin(u))))
        R[f"lat_{nom}"] = math.degrees(mx)
    R["lat_pro_dif"] = abs(R["lat_pro"] - 51.6)
    R["lat_sso_dif"] = abs(R["lat_sso"] - (180 - 97.8))
    # caso degenerado: i = 0 -> nodo indeterminado
    r, v = estado(7000e3, 0.01, 0.0, math.radians(123.0), math.radians(40.0), math.radians(10.0))
    h = cruz(r, v)
    R["n_norma_i0"] = math.hypot(-h[1], h[0]) / math.sqrt(sum(x * x for x in h))
    R["h_normal_dir"] = h[2] / math.sqrt(sum(x * x for x in h))
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"{R['n_casos']} estados SINTETICOS (semilla 71); retrogradas (i > 90): {R['retro']}")
    print(f"  error maximo de i = {R['emax_i']:.2e} rad ; error angular maximo de RAAN = {R['emax_O']:.2e} rad")
    print(f"  RAAN por cuadrante (0-90, 90-180, 180-270, 270-360): {R['cuad']}")
    print("Cuadrante de RAAN con atan2 (i = 51.6 grados ilustrativo): RAAN de partida -> recuperada [grados]")
    for a, b, c in R["ej"]:
        print(f"  {a:6.1f} -> {b:8.4f}   (i recuperada = {c:.4f})")
    print(f"  error maximo = {R['ej_err']:.1e} grados")
    print("Latitud geocentrica maxima alcanzada (muestreo de 3600 puntos):")
    print(f"  i = 51.6 -> {R['lat_pro']:.4f} grados ; i = 97.8 -> {R['lat_sso']:.4f} grados (= 180 - i) ; i = 0 -> {R['lat_ecu']:.4f}")
    print(f"Caso i = 0: |n|/|h| = {R['n_norma_i0']:.1e} (nodo indeterminado) ; h_z/|h| = {R['h_normal_dir']:.6f}")
    assert R["emax_i"] < 1e-9 and R["emax_O"] < 1e-9
    assert R["ej_err"] < 1e-9
    assert R["lat_pro_dif"] < 1e-3 and R["lat_sso_dif"] < 1e-3
    assert R["n_norma_i0"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
