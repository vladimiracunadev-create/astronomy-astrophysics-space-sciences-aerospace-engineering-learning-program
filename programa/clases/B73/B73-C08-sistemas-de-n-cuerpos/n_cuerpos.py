#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C08: problema de N cuerpos por suma directa y leapfrog en un sistema joviano de cinco cuerpos.

Datos consultados (2026-11-10): GM de Io, Europa, Ganymede y Callisto = 5959.91547, 3202.71210, 9887.83275, 7179.28340 km3/s2 (JPL SSD, JUP365);
GM de Jupiter = 126.687 x 10^6 km3/s2 (NASA/NSSDC, Jupiter Fact Sheet, 2024-10-02); semiejes medios 421 800, 671 100, 1 070 400, 1 882 700 km
y periodos 1.762732, 3.525463, 7.155588, 16.690440 d (JPL SSD, tabla de elementos, J2000, plano de Laplace); periodo de Io 1.769138 d (NASA/NSSDC, Jovian Satellite Fact Sheet, 2023-12-06).
SINTETICO: condiciones iniciales = orbitas circulares coplanares con esos semiejes y fases 0, 90, 180 y 270 grados; no son el estado real del sistema.
Modelo: cinco masas puntuales (masa proporcional a GM), solo gravedad newtoniana mutua; marco del baricentro; sin J2 ni mareas.
Integrador: leapfrog (kick-drift-kick), orden 2, simplectico, paso fijo. Segunda via: (a) problema de dos cuerpos Jupiter-Io con periodo analitico;
(b) reduccion del paso a la mitad: el error de energia debe bajar ~4 veces; (c) conservacion de momento y momento angular.
Tolerancias: error relativo de energia < 1e-6 ; cociente de errores 3-5 ; momento angular < 1e-10 relativo.
"""
from __future__ import annotations
import json, math, platform, sys

GM = [126.687e6, 5959.91547, 3202.71210, 9887.83275, 7179.28340]  # Jupiter, Io, Europa, Ganymede, Callisto
NOM = ["Jupiter", "Io", "Europa", "Ganymede", "Callisto"]
A = [0.0, 421800.0, 671100.0, 1070400.0, 1882700.0]
P_JPL = [None, 1.762732, 3.525463, 7.155588, 16.690440]
N = len(GM)


def inicial():
    r, v = [[0.0, 0.0]], [[0.0, 0.0]]
    for i in range(1, N):
        ang = math.radians(90.0 * (i - 1))
        vc = math.sqrt((GM[0] + GM[i]) / A[i])
        r.append([A[i] * math.cos(ang), A[i] * math.sin(ang)])
        v.append([-vc * math.sin(ang), vc * math.cos(ang)])
    # baricentro
    M = sum(GM)
    for arr in (r, v):
        cx = sum(GM[i] * arr[i][0] for i in range(N)) / M
        cy = sum(GM[i] * arr[i][1] for i in range(N)) / M
        for i in range(N):
            arr[i][0] -= cx
            arr[i][1] -= cy
    return r, v


def acel(r, n=N):
    a = [[0.0, 0.0] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = r[j][0] - r[i][0], r[j][1] - r[i][1]
            d3 = (dx * dx + dy * dy) ** 1.5
            a[i][0] += GM[j] * dx / d3
            a[i][1] += GM[j] * dy / d3
            a[j][0] -= GM[i] * dx / d3
            a[j][1] -= GM[i] * dy / d3
    return a


def energia(r, v, n=N):
    e = 0.0
    for i in range(n):
        e += 0.5 * GM[i] * (v[i][0] ** 2 + v[i][1] ** 2)
        for j in range(i + 1, n):
            e -= GM[i] * GM[j] / math.hypot(r[i][0] - r[j][0], r[i][1] - r[j][1])
    return e


def momento_ang(r, v, n=N):
    return sum(GM[i] * (r[i][0] * v[i][1] - r[i][1] * v[i][0]) for i in range(n))


def momento(v, n=N):
    return math.hypot(sum(GM[i] * v[i][0] for i in range(n)), sum(GM[i] * v[i][1] for i in range(n)))


def leapfrog(r, v, dt, pasos, n=N):
    a = acel(r, n)
    emax = 0.0
    e0 = energia(r, v, n)
    for k in range(pasos):
        for i in range(n):
            v[i][0] += 0.5 * dt * a[i][0]
            v[i][1] += 0.5 * dt * a[i][1]
            r[i][0] += dt * v[i][0]
            r[i][1] += dt * v[i][1]
        a = acel(r, n)
        for i in range(n):
            v[i][0] += 0.5 * dt * a[i][0]
            v[i][1] += 0.5 * dt * a[i][1]
        if k % 200 == 0:
            emax = max(emax, abs(energia(r, v, n) / e0 - 1))
    return max(emax, abs(energia(r, v, n) / e0 - 1))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Cuerpos: {', '.join(NOM)} ; pares por evaluacion de la fuerza = N(N-1)/2 = {N * (N - 1) // 2}")
    T = 16.690440 * 86400.0  # una orbita de Callisto
    res = {}
    for dt in (400.0, 200.0):
        r, v = inicial()
        e0, L0 = energia(r, v), momento_ang(r, v)
        em = leapfrog(r, v, dt, int(T / dt))
        dL = abs(momento_ang(r, v) / L0 - 1)
        pm = momento(v) / sum(GM[i] * math.hypot(*v[i]) for i in range(N))
        res[dt] = (em, dL, pm)
        print(f"dt = {dt:5.0f} s, T = {T / 86400:.2f} d ({int(T / dt)} pasos): error relativo maximo de energia = {em:.2e} ; |dL/L| = {dL:.2e} ; |P|/sum|p| = {pm:.1e}")
    ratio = res[400.0][0] / res[200.0][0]
    print(f"Cociente de errores de energia al reducir el paso a la mitad = {ratio:.2f} (orden 2 -> 4)")
    # dos cuerpos Jupiter-Io: periodo
    mu = GM[0] + GM[1]
    P_kep = 2 * math.pi * math.sqrt(A[1] ** 3 / mu)
    P_NASA = 1.769138
    print(f"Jupiter-Io: periodo kepleriano de una orbita circular de a = 421 800 km = {P_kep / 86400:.5f} d ; ficha NASA/NSSDC = {P_NASA} d (dif. {abs(P_kep / 86400 - P_NASA) / P_NASA:.2%}) ; tabla JPL = {P_JPL[1]} d (dif. {abs(P_kep / 86400 - P_JPL[1]) / P_JPL[1]:.2%})")
    # integracion de dos cuerpos: vuelve al punto de partida tras P_kep?
    GM2 = GM[:]
    r = [[0.0, 0.0], [A[1], 0.0]]
    vc = math.sqrt(mu / A[1])
    v = [[0.0, 0.0], [0.0, vc]]
    M2 = GM[0] + GM[1]
    cx = GM[1] * r[1][0] / M2
    cy = 0.0
    vx_cm, vy_cm = 0.0, GM[1] * vc / M2
    for i in range(2):
        r[i][0] -= cx
        v[i][1] -= vy_cm
    dt = 50.0
    pasos = int(round(P_kep / dt))
    dt = P_kep / pasos
    leapfrog(r, v, dt, pasos, 2)
    cierre = math.hypot(r[1][0] - r[0][0] - A[1], r[1][1] - r[0][1]) / A[1]
    print(f"Dos cuerpos: tras un periodo kepleriano la separacion vuelve al inicio con error relativo = {cierre:.2e} ({pasos} pasos)")
    # movimientos medios de Callisto, Ganymede, Europa, Io tras T
    assert res[200.0][0] < 1e-6 and 3.0 < ratio < 5.0 and res[200.0][1] < 1e-10 and cierre < 1e-5
    assert abs(P_kep / 86400 - P_NASA) / P_NASA < 0.002
    print("Pruebas superadas.")
    return {"python": platform.python_version(), "pares": N * (N - 1) // 2, "e400": res[400.0][0], "e200": res[200.0][0], "dL": res[200.0][1], "pm": res[200.0][2],
            "ratio": ratio, "Pkep": P_kep / 86400, "dP": abs(P_kep / 86400 - P_JPL[1]) / P_JPL[1], "dPn": abs(P_kep / 86400 - P_NASA) / P_NASA, "cierre": cierre, "T": T / 86400, "pasos": int(T / 200.0)}


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
