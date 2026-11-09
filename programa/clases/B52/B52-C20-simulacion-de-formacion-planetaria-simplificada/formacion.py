#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C20: simulacion simplificada de fusion de embriones con comprobaciones de masa, momento lineal, momento angular y energia.

Datos consultados el 2026-11-09: G de NIST (CODATA 2022); (GM)_sol y (GM)_Tierra nominales de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) y el anio de 365.25 d NO se consultaron: se usan para pasar a unidades ua-anio.
SIMULACION SINTETICA (no observada ni representativa del Sistema Solar): estrella de 1 M_sol; 12 embriones de 0.1 masas terrestres (ilustrativo)
a partir de 0.8 ua con espaciado de 3.5 radios de Hill mutuos, orbitas circulares coplanares con fases aleatorias (semilla 20261109);
densidad 3000 kg/m^3 (ilustrativa); radio de fusion = 100 veces la suma de los radios fisicos (inflado de ensenanza).
Sistema de referencia: baricentrico inercial plano; unidades ua, anio. Integrador leapfrog KDK (h = 0.012 anios) como en B52-C19.
Fusion perfectamente inelastica en el centro de masa del par: se conservan masa y momento lineal; el momento angular orbital del par pasa al ESPIN del cuerpo
fusionado (se contabiliza: L orbital + espin se conserva); la energia NO se conserva por construccion: cambia en -(1/2) mu v_rel^2 (disipacion) + G m_i m_j / d (se elimina la energia
potencial mutua) + la variacion de la energia potencial con los demas cuerpos al reubicar la masa en el centro de masa, y esa variacion predicha se verifica contra la medida.
Tolerancias: masa 1e-14 relativo; momento lineal 1e-12 (M_sol ua/anio); L orbital + espin 1e-9 relativo; variacion de energia en cada fusion frente a la predicha 1e-9 relativo a |E0|.
"""
from __future__ import annotations
import math, platform, random

G = 6.67430e-11
GM_SOL, GM_T = 1.3271244e20, 3.986004e14
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
GMS = GM_SOL * ANIO ** 2 / UA ** 3
M_T = GM_T / GM_SOL           # masa terrestre en M_sol
MSOL_KG = GM_SOL / G
RHO = 3000.0
F_FUSION = 100.0
N, M_EMB, DELTA, A0, T_FIN, H = 12, 0.1 * M_T, 3.5, 0.8, 1500.0, 0.012


def radio_ua(m):
    return (3.0 * m * MSOL_KG / (4.0 * math.pi * RHO)) ** (1.0 / 3.0) / UA


def a_siguiente(a1, m1, m2):
    k = DELTA * ((m1 + m2) / 3.0) ** (1.0 / 3.0) / 2.0
    return a1 * (1.0 + k) / (1.0 - k)


def inicial():
    rng = random.Random(20261109)
    masas, pos, vel = [1.0], [[0.0, 0.0]], [[0.0, 0.0]]
    a = A0
    for i in range(N):
        f = rng.uniform(0, 2 * math.pi)
        masas.append(M_EMB)
        pos.append([a * math.cos(f), a * math.sin(f)])
        v = math.sqrt(GMS / a)
        vel.append([-v * math.sin(f), v * math.cos(f)])
        a = a_siguiente(a, M_EMB, M_EMB)
    mt = sum(masas)
    for k in range(2):
        cp = sum(m * p[k] for m, p in zip(masas, pos)) / mt
        cv = sum(m * v[k] for m, v in zip(masas, vel)) / mt
        for p, v in zip(pos, vel):
            p[k] -= cp
            v[k] -= cv
    return masas, pos, vel


def acel(masas, pos):
    n = len(masas)
    a = [[0.0, 0.0] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
            r3 = (dx * dx + dy * dy) ** 1.5
            fi, fj = GMS * masas[j] / r3, GMS * masas[i] / r3
            a[i][0] += fi * dx
            a[i][1] += fi * dy
            a[j][0] -= fj * dx
            a[j][1] -= fj * dy
    return a


def paso(masas, pos, vel, h):
    a = acel(masas, pos)
    for p, v, ai in zip(pos, vel, a):
        v[0] += 0.5 * h * ai[0]
        v[1] += 0.5 * h * ai[1]
        p[0] += h * v[0]
        p[1] += h * v[1]
    a = acel(masas, pos)
    for v, ai in zip(vel, a):
        v[0] += 0.5 * h * ai[0]
        v[1] += 0.5 * h * ai[1]


def energia(masas, pos, vel):
    e = sum(0.5 * m * (v[0] ** 2 + v[1] ** 2) for m, v in zip(masas, vel))
    for i in range(len(masas)):
        for j in range(i + 1, len(masas)):
            e -= GMS * masas[i] * masas[j] / math.hypot(pos[j][0] - pos[i][0], pos[j][1] - pos[i][1])
    return e


def momentos(masas, pos, vel):
    px = sum(m * v[0] for m, v in zip(masas, vel))
    py = sum(m * v[1] for m, v in zip(masas, vel))
    L = sum(m * (p[0] * v[1] - p[1] * v[0]) for m, p, v in zip(masas, pos, vel))
    return px, py, L


def fusionar(masas, pos, vel):
    """Fusiona el primer par de planetas (indices >= 1) en contacto; devuelve (hubo_fusion, espin_ganado, variacion_de_energia_predicha)."""
    n = len(masas)
    for i in range(1, n):
        for j in range(i + 1, n):
            d = math.hypot(pos[j][0] - pos[i][0], pos[j][1] - pos[i][1])
            if d < F_FUSION * (radio_ua(masas[i]) + radio_ua(masas[j])):
                m = masas[i] + masas[j]
                X = [(masas[i] * pos[i][k] + masas[j] * pos[j][k]) / m for k in range(2)]
                V = [(masas[i] * vel[i][k] + masas[j] * vel[j][k]) / m for k in range(2)]
                espin = sum(mm * ((p[0] - X[0]) * (v[1] - V[1]) - (p[1] - X[1]) * (v[0] - V[0])) for mm, p, v in ((masas[i], pos[i], vel[i]), (masas[j], pos[j], vel[j])))
                mu = masas[i] * masas[j] / m
                vrel2 = (vel[i][0] - vel[j][0]) ** 2 + (vel[i][1] - vel[j][1]) ** 2
                dE_pred = -0.5 * mu * vrel2 + GMS * masas[i] * masas[j] / d
                for kk in range(n):
                    if kk in (i, j):
                        continue
                    rik = math.hypot(pos[i][0] - pos[kk][0], pos[i][1] - pos[kk][1])
                    rjk = math.hypot(pos[j][0] - pos[kk][0], pos[j][1] - pos[kk][1])
                    rXk = math.hypot(X[0] - pos[kk][0], X[1] - pos[kk][1])
                    dE_pred += GMS * masas[kk] * (masas[i] / rik + masas[j] / rjk - m / rXk)
                pos[i] = [(masas[i] * pos[i][k] + masas[j] * pos[j][k]) / m for k in range(2)]
                vel[i] = [(masas[i] * vel[i][k] + masas[j] * vel[j][k]) / m for k in range(2)]
                masas[i] = m
                del masas[j], pos[j], vel[j]
                return True, espin, dE_pred
    return False, 0.0, 0.0


def calcular():
    masas, pos, vel = inicial()
    m0 = sum(masas)
    px0, py0, L0 = momentos(masas, pos, vel)
    a_ini = [math.hypot(*p) for p in pos[1:]]
    E0 = energia(masas, pos, vel)
    fusiones, max_err_E, max_dp, max_dL, dm, espin_tot = [], 0.0, 0.0, 0.0, 0.0, 0.0
    t, pasos = 0.0, int(T_FIN / H)
    for k in range(pasos):
        paso(masas, pos, vel, H)
        t += H
        E_antes = energia(masas, pos, vel)
        while True:
            hubo, esp, dEp = fusionar(masas, pos, vel)
            if not hubo:
                break
            E_desp = energia(masas, pos, vel)
            max_err_E = max(max_err_E, abs((E_desp - E_antes) - dEp) / abs(E0))
            espin_tot += esp
            fusiones.append((t, len(masas) - 1))
            E_antes = E_desp
        if k % 200 == 0 or k == pasos - 1:
            px, py, L = momentos(masas, pos, vel)
            max_dp = max(max_dp, abs(px - px0) + abs(py - py0))
            max_dL = max(max_dL, abs((L + espin_tot) / L0 - 1.0))
            dm = max(dm, abs(sum(masas) / m0 - 1.0))
    a_fin = []
    for m, p, v in zip(masas[1:], pos[1:], vel[1:]):
        r = math.hypot(*p)
        v2 = v[0] ** 2 + v[1] ** 2
        a_fin.append((m, 1.0 / (2.0 / r - v2 / GMS)))
    return dict(a_ini=a_ini, n_ini=N, n_fin=len(masas) - 1, fusiones=fusiones, masas=[m / M_T for m in masas[1:]], a_fin=a_fin, dm=dm, dp=max_dp, dL=max_dL,
                dE_fusion=max_err_E, espin=espin_tot / L0, dE_total=(energia(masas, pos, vel) - E0) / abs(E0), m_embrion_ini=M_EMB / M_T)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Condiciones SINTETICAS: {N} embriones de {r['m_embrion_ini']:.2f} M_Tierra desde {A0} ua con espaciado {DELTA} R_H mutuos ; semilla de fases 20261109 ; radio de fusion = {F_FUSION:.0f} x suma de radios fisicos")
    print("Semiejes iniciales [ua]: " + " ".join(f"{x:.3f}" for x in r["a_ini"]))
    print(f"Tras {T_FIN:.0f} anios: {r['n_fin']} cuerpos ({len(r['fusiones'])} fusiones)")
    print("Masas finales [M_Tierra]: " + " ".join(f"{m:.2f}" for m in r["masas"]))
    print("Semiejes osculadores finales [ua]: " + " ".join(f"{a:.3f}" for _, a in r["a_fin"]))
    print("Primeras fusiones (anio, cuerpos restantes): " + ", ".join(f"({t:.0f}, {n})" for t, n in r["fusiones"][:6]))
    print(f"Conservacion: |d masa total/masa| = {r['dm']:.1e} ; |d momento lineal| = {r['dp']:.1e} M_sol ua/anio ; |d (L+espin)/L| = {r['dL']:.1e} ; espin acumulado / L = {r['espin']:.1e} ; error de la variacion de energia predicha por fusion = {r['dE_fusion']:.1e} ; dE/|E0| total = {r['dE_total']:+.1e}")
    assert r["dm"] < 1e-14
    assert r["dp"] < 1e-12
    assert r["dL"] < 1e-9
    assert r["dE_fusion"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
