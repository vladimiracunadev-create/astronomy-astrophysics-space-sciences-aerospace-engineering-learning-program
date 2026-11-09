#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C19: integrador de N cuerpos de segundo orden, conservacion y sensibilidad a las condiciones iniciales.

Datos consultados el 2026-11-09: (GM)_sol nominal de la IAU 2015 (Resolucion B3). La unidad astronomica (1.495978707e11 m) y el anio juliano
de 365.25 d NO se consultaron en esta sesion: se usan solo para pasar a unidades ua-anio.
Sistemas SINTETICOS (no observados): estrella de 1 M_sol y tres planetas de 3e-5 M_sol (aprox. 10 masas terrestres, ilustrativo) con espaciados
de 4 y 8 radios de Hill mutuos desde a1 = 1 ua, orbitas circulares coplanares, fases iniciales 0, 2.1 y 4.2 rad.
Sistema de referencia: baricentrico inercial, coordenadas cartesianas planas; unidades ua, anio.
Integrador: leapfrog kick-drift-kick (simpletico de 2o orden), paso h = P1/100.
Pruebas: (1) un planeta excentrico (e = 0.1): error de energia con h y h/2 -> cociente ~4; retorno a la posicion tras un periodo; (2) conservacion del momento angular a 1e-12;
(3) sensibilidad: dos copias con una perturbacion de 1e-9 ua en la posicion del planeta 2; se informa la separacion tras 100 y 1000 orbitas del planeta interno (SIMULACION: resultado de este modelo y esta semilla, sin umbral analitico).
Tolerancias: cociente de errores de energia entre 3 y 5; deriva de fase tras 100 periodos: cociente entre los pasos h y h/2 entre 3 y 5 (error de periodo ~ h^2); momento angular 1e-12 relativo.
"""
from __future__ import annotations
import math, platform

GM_SOL = 1.3271244e20
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
GMS = GM_SOL * ANIO ** 2 / UA ** 3   # ua^3 / anio^2
MU_P = 3e-5                          # masa de planeta en M_sol


def hill_mutuo_a2(a1, delta, m=MU_P):
    """Semieje a2 tal que (a2 - a1) = delta * ((2 m)/(3))^(1/3) (a1 + a2)/2 (estrella de 1 M_sol)."""
    k = delta * (2.0 * m / 3.0) ** (1.0 / 3.0) / 2.0
    return a1 * (1.0 + k) / (1.0 - k)


def sistema(delta, fases=(0.0, 2.1, 4.2)):
    a = [1.0]
    for _ in range(2):
        a.append(hill_mutuo_a2(a[-1], delta))
    masas = [1.0] + [MU_P] * 3
    pos, vel = [[0.0, 0.0]], [[0.0, 0.0]]
    for ai, f in zip(a, fases):
        pos.append([ai * math.cos(f), ai * math.sin(f)])
        v = math.sqrt(GMS / ai)
        vel.append([-v * math.sin(f), v * math.cos(f)])
    return masas, pos, vel, a


def a_baricentro(masas, pos, vel):
    mt = sum(masas)
    for k in range(2):
        cp = sum(m * p[k] for m, p in zip(masas, pos)) / mt
        cv = sum(m * v[k] for m, v in zip(masas, vel)) / mt
        for p, v in zip(pos, vel):
            p[k] -= cp
            v[k] -= cv


def acel(masas, pos):
    n = len(masas)
    a = [[0.0, 0.0] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
            r3 = (dx * dx + dy * dy) ** 1.5
            fi, fj = GMS * masas[j] / r3, GMS * masas[i] / r3
            a[i][0] += fi * dx; a[i][1] += fi * dy
            a[j][0] -= fj * dx; a[j][1] -= fj * dy
    return a


def paso(masas, pos, vel, h):
    a = acel(masas, pos)
    for p, v, ai in zip(pos, vel, a):
        v[0] += 0.5 * h * ai[0]; v[1] += 0.5 * h * ai[1]
        p[0] += h * v[0]; p[1] += h * v[1]
    a = acel(masas, pos)
    for v, ai in zip(vel, a):
        v[0] += 0.5 * h * ai[0]; v[1] += 0.5 * h * ai[1]


def energia(masas, pos, vel):
    e = sum(0.5 * m * (v[0] ** 2 + v[1] ** 2) for m, v in zip(masas, vel))
    for i in range(len(masas)):
        for j in range(i + 1, len(masas)):
            e -= GMS * masas[i] * masas[j] / math.hypot(pos[j][0] - pos[i][0], pos[j][1] - pos[i][1])
    return e


def momento_angular(masas, pos, vel):
    return sum(m * (p[0] * v[1] - p[1] * v[0]) for m, p, v in zip(masas, pos, vel))


def prueba_kepler(n_por_orbita):
    e0 = 0.1
    a = 1.0
    masas, pos, vel = [1.0, 1e-12], [[0.0, 0.0], [a * (1 - e0), 0.0]], [[0.0, 0.0], [0.0, math.sqrt(GMS * (1 + e0) / (a * (1 - e0)))]]
    P = 2 * math.pi * math.sqrt(a ** 3 / GMS)
    h = P / n_por_orbita
    E0 = energia(masas, pos, vel)
    emax, x0 = 0.0, list(pos[1])
    for _ in range(100 * n_por_orbita):
        paso(masas, pos, vel, h)
        emax = max(emax, abs(energia(masas, pos, vel) / E0 - 1.0))
    # retorno tras 100 periodos exactos
    ret = math.hypot(pos[1][0] - x0[0], pos[1][1] - x0[1])
    return emax, ret


def separacion(delta, orbitas, n_por_orbita=100):
    masas, p1, v1, a = sistema(delta)
    a_baricentro(masas, p1, v1)
    p2 = [list(p) for p in p1]; v2 = [list(v) for v in v1]
    p2[2][0] += 1e-9
    P1 = 2 * math.pi * math.sqrt(a[0] ** 3 / GMS)
    h = P1 / n_por_orbita
    E0, L0 = energia(masas, p1, v1), momento_angular(masas, p1, v1)
    marcas, sal, dL, dE = [100, 1000], {}, 0.0, 0.0
    total = orbitas * n_por_orbita
    for k in range(1, total + 1):
        paso(masas, p1, v1, h); paso(masas, p2, v2, h)
        if k % n_por_orbita == 0:
            o = k // n_por_orbita
            dL = max(dL, abs(momento_angular(masas, p1, v1) / L0 - 1.0))
            dE = max(dE, abs(energia(masas, p1, v1) / E0 - 1.0))
            if o in marcas:
                sal[o] = math.hypot(p1[2][0] - p2[2][0], p1[2][1] - p2[2][1])
    return sal, dL, dE, a


def calcular():
    e1, r1 = prueba_kepler(100)
    e2, r2 = prueba_kepler(200)
    res = {}
    for delta in (4.0, 8.0):
        res[delta] = separacion(delta, 1000)
    return dict(e1=e1, e2=e2, r1=r1, r2=r2, res=res)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"GM_sol = {GMS:.6f} ua^3/anio^2 ; planetas SINTETICOS de {MU_P} M_sol")
    print(f"Planeta excentrico (e = 0.1), 100 orbitas: error maximo de energia con 100 pasos/orbita = {r['e1']:.3e} ; con 200 pasos/orbita = {r['e2']:.3e} ; cociente = {r['e1'] / r['e2']:.2f} (esperado ~4)")
    print(f"  distancia a la posicion inicial tras 100 periodos exactos (deriva de fase): {r['r1']:.2e} ua (100 pasos) ; {r['r2']:.2e} ua (200 pasos) ; cociente = {r['r1'] / r['r2']:.2f}")
    for delta, (sal, dL, dE, a) in r["res"].items():
        print(f"Sistema SINTETICO de 3 planetas con espaciado {delta:.0f} R_H mutuos, semiejes {a[0]:.4f} {a[1]:.4f} {a[2]:.4f} ua:")
        print(f"  conservacion en 1000 orbitas: max |dL/L| = {dL:.1e} ; max |dE/E| = {dE:.1e}")
        print(f"  separacion de dos copias (perturbacion inicial 1e-9 ua): {sal[100]:.3e} ua a 100 orbitas ; {sal[1000]:.3e} ua a 1000 orbitas")
    assert 3.0 < r["e1"] / r["e2"] < 5.0
    assert 3.0 < r["r1"] / r["r2"] < 5.0
    for delta, (sal, dL, dE, a) in r["res"].items():
        assert dL < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
