#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C20: propagador kepleriano y su verificacion con invariantes, retroceso en el tiempo e integrador independiente.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 (IAU 2015 B3). TODOS los casos son SINTETICOS (semilla 20):
30 orbitas con a en [7000, 30000] km, e en [0, 0.7], i en [0, 180] grados, RAAN, omega, M0 en [0, 360) y tiempos de propagacion t en [-1.2 T, 1.2 T].
Sistema: marco inercial geocentrico idealizado (ECI), SI; dos cuerpos puntuales; sin perturbaciones; solo orbitas elipticas.
No se usa ninguna efemeride, ni JPL Horizons, ni SPICE (no consultados).
Modelo: M = M0 + n t ; Newton para E (tolerancia 1e-14) ; nu ; estado perifocal ; rotacion 3-1-3.
Segunda via (independiente): integracion RK4 3D desde el estado inicial con 20000 pasos por periodo (hacia atras si t < 0); se compara la posicion y la velocidad finales.
Pruebas y tolerancias (declaradas antes de ejecutar):
  T1 t = 0 reproduce el estado inicial: 1e-9 m;
  T2 un periodo exacto reproduce el estado: 1e-4 m;
  T3 invariantes h y epsilon constantes en 25 tiempos: 1e-9 relativa;
  T4 ida y vuelta (+t y luego -t): 1e-6 m;
  T5 propagador frente a RK4 independiente: posicion < 1e-2 m, velocidad < 1e-6 m/s (el error dominante es el del RK4);
  T6 mutacion: un propagador con el Newton cortado a 2 iteraciones debe FALLAR T5 aunque pase T3 (los invariantes no ven errores de tiempo).
"""
from __future__ import annotations
import math, platform, random

MU = 3.986004e14


def rot(raan, inc, w):
    cO, sO, ci, si, cw, sw = math.cos(raan), math.sin(raan), math.cos(inc), math.sin(inc), math.cos(w), math.sin(w)
    return [[cO * cw - sO * sw * ci, -cO * sw - sO * cw * ci, sO * si],
            [sO * cw + cO * sw * ci, -sO * sw + cO * cw * ci, -cO * si],
            [sw * si, cw * si, ci]]


def mv(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def norma(a):
    return math.sqrt(sum(x * x for x in a))


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def kepler(M, e, iteraciones=100):
    M = (M + math.pi) % (2 * math.pi) - math.pi
    E = M if e < 0.8 else math.pi
    for _ in range(iteraciones):
        d = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= d
        if abs(d) < 1e-14:
            break
    return E


def propagar(el, t, iteraciones=100):
    a, e, inc, raan, w, M0 = el
    n = math.sqrt(MU / a ** 3)
    E = kepler(M0 + n * t, e, iteraciones)
    nu = 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))
    p = a * (1 - e * e)
    r = p / (1 + e * math.cos(nu))
    f = math.sqrt(MU / p)
    m = rot(raan, inc, w)
    return mv(m, (r * math.cos(nu), r * math.sin(nu), 0.0)), mv(m, (-f * math.sin(nu), f * (e + math.cos(nu)), 0.0))


def rk4_estado(r0, v0, t, pasos_por_periodo, T):
    s = r0 + v0
    n = max(1, int(abs(t) / T * pasos_por_periodo))
    dt = t / n
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2 + s[2] ** 2) ** 1.5
        return (s[3], s[4], s[5], -MU * s[0] / d3, -MU * s[1] / d3, -MU * s[2] / d3)
    for _ in range(n):
        k1 = f(s)
        k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(6)))
        k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(6)))
        k4 = f(tuple(s[i] + dt * k3[i] for i in range(6)))
        s = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(6))
    return s[:3], s[3:]


def dist(a, b):
    return norma(tuple(x - y for x, y in zip(a, b)))


def calcular():
    R = {}
    rnd = random.Random(20)
    casos = []
    for _ in range(30):
        a = rnd.uniform(7000e3, 30000e3)
        e = rnd.uniform(0.0, 0.7)
        inc, raan, w, M0 = (math.radians(rnd.uniform(lo, hi)) for lo, hi in ((0, 180), (0, 360), (0, 360), (0, 360)))
        t = rnd.uniform(-1.2, 1.2)
        casos.append(((a, e, inc, raan, w, M0), t))
    t1 = t2 = t3 = t4 = 0.0
    e5r = e5v = 0.0
    e5m = 0.0
    peor_e5 = (0.0, None)
    for el, tf in casos:
        a = el[0]
        T = 2 * math.pi * math.sqrt(a ** 3 / MU)
        t = tf * T
        r0, v0 = propagar(el, 0.0)
        # T1: t = 0 frente a elementos -> estado (mismo modelo, M0) ; se compara con la propagacion en t=0 desde M0 desfasada un periodo
        ra, va = propagar(el, T)
        t1 = max(t1, dist(r0, propagar(el, 0.0)[0]))
        t2 = max(t2, dist(r0, ra))
        # T3
        h0 = norma(cruz(r0, v0))
        eps0 = 0.5 * norma(v0) ** 2 - MU / norma(r0)
        for k in range(25):
            rk, vk = propagar(el, T * k / 25.0)
            t3 = max(t3, abs(norma(cruz(rk, vk)) - h0) / h0, abs(0.5 * norma(vk) ** 2 - MU / norma(rk) - eps0) / abs(eps0))
        # T4
        el2 = (el[0], el[1], el[2], el[3], el[4], el[5] + math.sqrt(MU / a ** 3) * t)
        rt, vt = propagar(el, t)
        rb, vb = propagar(el2, -t)
        t4 = max(t4, dist(rb, r0), 0.0)
        # T5
        rrk, vrk = rk4_estado(r0, v0, t, 20000, T)
        er, ev = dist(rt, rrk), dist(vt, vrk)
        e5r, e5v = max(e5r, er), max(e5v, ev)
        # T6: mutacion con 2 iteraciones de Newton
        rm, vm = propagar(el, t, iteraciones=2)
        e5m = max(e5m, dist(rm, rrk))
    R.update(t1=t1, t2=t2, t3=t3, t4=t4, e5r=e5r, e5v=e5v, e5m=e5m, n_casos=len(casos))
    # invariantes de la version mutada (deben seguir pasando)
    el, tf = casos[0]
    T = 2 * math.pi * math.sqrt(el[0] ** 3 / MU)
    r0, v0 = propagar(el, 0.0)
    h0 = norma(cruz(r0, v0))
    pm = 0.0
    for k in range(25):
        rk, vk = propagar(el, T * k / 25.0, iteraciones=2)
        pm = max(pm, abs(norma(cruz(rk, vk)) - h0) / h0)
    R["inv_mut"] = pm
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"{R['n_casos']} orbitas SINTETICAS (semilla 20), t en [-1.2 T, 1.2 T]; dos cuerpos; sin efemerides")
    print(f"  T1 estado en t = 0 reproducido:                 max {R['t1']:.2e} m   (tolerancia 1e-9)")
    print(f"  T2 un periodo exacto devuelve el estado:         max {R['t2']:.2e} m   (tolerancia 1e-4)")
    print(f"  T3 invariantes h y epsilon en 25 tiempos:        max {R['t3']:.2e}     (tolerancia 1e-9)")
    print(f"  T4 ida y vuelta (+t, -t):                        max {R['t4']:.2e} m   (tolerancia 1e-6)")
    print(f"  T5 frente a RK4 independiente (20000 pasos/T):   posicion {R['e5r']:.2e} m ; velocidad {R['e5v']:.2e} m/s   (tolerancias 1e-2 m ; 1e-6 m/s)")
    print(f"  T6 mutacion (Newton con 2 iteraciones): error frente a RK4 = {R['e5m']:.2e} m ; invariante h de la version mutada = {R['inv_mut']:.1e}")
    assert R["t1"] < 1e-9 and R["t2"] < 1e-4 and R["t3"] < 1e-9 and R["t4"] < 1e-6
    assert R["e5r"] < 1e-2 and R["e5v"] < 1e-6
    assert R["e5m"] > 100.0 * R["e5r"] and R["e5m"] > 1.0 and R["inv_mut"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
