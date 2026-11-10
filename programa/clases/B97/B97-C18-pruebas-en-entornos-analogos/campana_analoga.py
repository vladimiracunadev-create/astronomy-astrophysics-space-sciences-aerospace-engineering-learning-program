#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C18: tamano de una campana de pruebas (teorema de ejecucion exitosa) y escalado de Froude para un entorno analogo.

Datos consultados (2026-11-10): gravedad media de la Tierra 9.820, Marte 3.73 y la Luna 1.62 m/s2 (NASA/NSSDC); masa de Perseverance 1025 kg (NASA).
ILUSTRATIVOS (sinteticos): confiabilidades objetivo 0.90, 0.95 y 0.99 con confianza 0.90 y 0.95; longitud caracteristica 1.5 m; velocidad objetivo 0.042 m/s; 200000 campanas simuladas, semilla fija.
Modelo: con 0 fallas en n pruebas independientes, R^n <= 1 - C  =>  n = ceil(ln(1 - C)/ln R). Con c fallas permitidas, n minimo tal que P(X <= c) <= 1 - C con X ~ Bin(n, 1 - R).
Escalado de Froude (semejanza dinamica a igual geometria): v_prueba = v_objetivo sqrt(g_prueba/g_objetivo); fraccion a descargar = 1 - g_objetivo/g_prueba.
Segunda via: suma binomial exacta frente a la formula; simulacion de campanas con confiabilidad igual al objetivo (la tasa de aprobacion debe ser ~ 1 - C, tolerancia 3 sigma).
Unidades SI. Pruebas independientes e identicas; el entorno analogo reproduce solo la gravedad (no el suelo, la temperatura ni el polvo).
"""
from __future__ import annotations
import math, platform, random

G = {"Tierra": 9.820, "Marte": 3.73, "Luna": 1.62}                                     # NASA/NSSDC
MASA, LARGO, V_OBJ = 1025.0, 1.5, 0.042                                                # masa consultada; resto ILUSTRATIVO
NSIM, SEMILLA = 200000, 20261110


def n_cero(r, c):
    return math.ceil(math.log(1 - c) / math.log(r))


def cdf_bin(n, k, q):
    return sum(math.comb(n, i) * q ** i * (1 - q) ** (n - i) for i in range(k + 1))


def n_con_fallas(r, c, k):
    n = k + 1
    while cdf_bin(n, k, 1 - r) > 1 - c:
        n += 1
    return n


def calc():
    tabla = []
    for r in (0.90, 0.95, 0.99):
        for c in (0.90, 0.95):
            n0 = n_cero(r, c)
            tabla.append((r, c, n0, r ** n0, n_con_fallas(r, c, 0), n_con_fallas(r, c, 1), n_con_fallas(r, c, 2)))
    rng = random.Random(SEMILLA)
    n = n_cero(0.95, 0.90)
    aprueba = sum(all(rng.random() < 0.95 for _ in range(n)) for _ in range(NSIM)) / NSIM
    sig = math.sqrt(0.10 * 0.90 / NSIM)
    fr = {}
    for obj in ("Marte", "Luna"):
        fr[obj] = dict(v=V_OBJ * math.sqrt(G["Tierra"] / G[obj]), descarga=1 - G[obj] / G["Tierra"], fuerza=MASA * (G["Tierra"] - G[obj]),
                       fr=V_OBJ / math.sqrt(G[obj] * LARGO))
    # misma semejanza: Fr en la Tierra con la velocidad escalada debe igualar el del objetivo
    fr_t = {o: fr[o]["v"] / math.sqrt(G["Tierra"] * LARGO) for o in fr}
    dif_fr = max(abs(fr_t[o] - fr[o]["fr"]) for o in fr)
    ok_n = all(t[3] <= 1 - t[1] + 1e-12 and t[0] ** (t[2] - 1) > 1 - t[1] for t in tabla)   # n es el minimo
    return dict(tabla=tabla, n45=n, aprueba=aprueba, sig=sig, z=abs(aprueba - 0.10) / sig, fr=fr, dif_fr=dif_fr, ok_n=ok_n,
                n_95_90=n_cero(0.95, 0.90), n_99_90=n_cero(0.99, 0.90), n_99_95=n_cero(0.99, 0.95), n95_1=n_con_fallas(0.95, 0.90, 1), n95_2=n_con_fallas(0.95, 0.90, 2),
                v_marte=fr["Marte"]["v"], d_marte=fr["Marte"]["descarga"], f_marte=fr["Marte"]["fuerza"], v_luna=fr["Luna"]["v"], d_luna=fr["Luna"]["descarga"],
                f_luna=fr["Luna"]["fuerza"], fr_marte=fr["Marte"]["fr"], n_90_90=n_cero(0.90, 0.90))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Campana de pruebas ILUSTRATIVA (pruebas independientes, confiabilidad R, confianza C):")
    print("   R     C    n (0 fallas)  R^n      n (<=0)  n (<=1)  n (<=2)")
    for rr, c, n0, rn, a, b, d in r["tabla"]:
        print(f"{rr:5.2f} {c:5.2f} {n0:10d} {rn:10.5f} {a:8d} {b:8d} {d:8d}")
    print(f"Simulacion de {NSIM} campanas de {r['n45']} pruebas con R = 0.95: tasa de aprobacion = {r['aprueba']:.5f} (esperado 0.10000); desviacion = {r['z']:.2f} sigma")
    print(f"Escalado de Froude (L = {LARGO} m, v objetivo = {V_OBJ} m/s, masa {MASA:.0f} kg):")
    for o, d in r["fr"].items():
        print(f"  {o}: v de prueba en la Tierra = {d['v']:.4f} m/s; fraccion a descargar = {100*d['descarga']:.1f} % ({d['fuerza']:.0f} N); Fr = {d['fr']:.4f}")
    print(f"Diferencia de Froude entre el objetivo y la prueba escalada = {r['dif_fr']:.2e}")
    assert r["ok_n"] and r["z"] < 3 and r["dif_fr"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
