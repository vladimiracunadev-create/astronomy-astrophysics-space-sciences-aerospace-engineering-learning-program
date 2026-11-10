#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C25: comportamiento no lineal: plasticidad 1D con endurecimiento isotropo (retorno radial) y contacto con holgura (Newton-Raphson).

DATOS ILUSTRATIVOS (no consultados): E = 69 000 MPa, sigma_y = 275 MPa, modulo plastico de endurecimiento isotropo H = 3000 MPa (sigma_y(ep) = sigma_y + H ep).
Camino de deformacion impuesta (ciclo): 0 -> +0,8 % -> 0 -> -0,4 % -> 0, en 400 pasos por tramo.
Algoritmo (retorno 1D): prueba elastica s_tr = E(eps - ep_n); si |s_tr| > sigma_y + H alpha_n, retorno: dgamma = (|s_tr| - sigma_y - H alpha_n)/(E + H).
Solucion analitica de la carga monotona: s1 = sigma_y + E_t (eps1 - sigma_y/E) con E_t = E H/(E + H); deformacion plastica al descargar a tension cero: ep = eps1 - s1/E.
Contacto: resorte k1 = 1,0e6 N/m en serie con una holgura g = 1,0 mm y un segundo resorte k2 = 4,0e6 N/m que actua solo cuando u > g; fuerza interna
f(u) = k1 u + k2 max(0, u - g); se resuelve f(u) = P con Newton y tangente k1 + k2 H(u - g). Analitica: u = P/k1 si P <= k1 g; u = (P + k2 g)/(k1 + k2) si no.
Tolerancias: sigma al final de la carga monotona frente a analitica < 1e-9 relativa; Newton: residuo < 1e-9 N.
"""
from __future__ import annotations
import math, platform

E, SY, H = 69000.0, 275.0, 3000.0
K1, K2, GAP = 1.0e6, 4.0e6, 1.0e-3


def paso(eps, ep, alpha):
    s_tr = E * (eps - ep)
    f = abs(s_tr) - (SY + H * alpha)
    if f <= 0:
        return s_tr, ep, alpha
    dg = f / (E + H)
    sg = 1.0 if s_tr > 0 else -1.0
    ep_n = ep + dg * sg
    al_n = alpha + dg
    return E * (eps - ep_n), ep_n, al_n


def newton_contacto(P):
    u = 0.0
    it = 0
    while True:
        f = K1 * u + K2 * max(0.0, u - GAP) - P
        if abs(f) < 1e-9:
            return u, it
        t = K1 + (K2 if u > GAP else 0.0)
        u -= f / t
        it += 1
        if it > 50:
            raise RuntimeError("Newton no converge")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Material ILUSTRATIVO: E = 69 000 MPa, sigma_y = 275 MPa, H = 3000 MPa (endurecimiento isotropo)")
    tramos = ((0.0, 0.008), (0.008, 0.0), (0.0, -0.004), (-0.004, 0.0))
    ep, al = 0.0, 0.0
    W = 0.0
    prev_eps, prev_s = 0.0, 0.0
    marcas = []
    for k, (a, b) in enumerate(tramos):
        for i in range(1, 401):
            eps = a + (b - a) * i / 400
            s, ep, al = paso(eps, ep, al)
            W += 0.5 * (s + prev_s) * (eps - prev_eps)
            prev_eps, prev_s = eps, s
        marcas.append((b, s, ep, al))
    names = ("fin de la carga a +0,8 %", "fin de la descarga a 0 de deformacion", "fin de la carga inversa a -0,4 %", "cierre del ciclo a 0")
    for nm, (e, s, p, a) in zip(names, marcas):
        print(f"  {nm:40s} eps = {e * 100:+6.2f} %  sigma = {s:9.3f} MPa  eps_p = {p * 100:+8.4f} %  alfa = {a * 100:7.4f} %")
    Et = E * H / (E + H)
    s1 = SY + Et * (0.008 - SY / E)
    ep1 = 0.008 - s1 / E
    print(f"Analitica de la carga monotona: E_t = {Et:.3f} MPa ; sigma(0,8 %) = {s1:.6f} MPa ; eps_p = {ep1 * 100:.6f} %")
    # se recalcula solo la rampa monotona para compararla con la analitica
    ep_m, al_m = 0.0, 0.0
    for i in range(1, 401):
        s_m, ep_m, al_m = paso(0.008 * i / 400, ep_m, al_m)
    print(f"Numerica: sigma = {s_m:.6f} MPa ; eps_p = {ep_m * 100:.6f} % ; dif relativa sigma = {abs(s_m - s1) / s1:.1e}")
    assert abs(s_m - s1) / s1 < 1e-9
    print(f"Energia disipada en el ciclo (integral de sigma d eps) = {W:.4f} MJ/m3")
    print(f"Tension de fluencia actual tras el ciclo = sigma_y + H alfa = {SY + H * marcas[-1][3]:.2f} MPa (endurecimiento acumulado)")
    # Contacto
    print("Contacto con holgura (k1 = 1e6 N/m, g = 1 mm, k2 = 4e6 N/m): Newton frente a analitica")
    for P in (500.0, 1000.0, 2000.0, 5000.0):
        u, it = newton_contacto(P)
        ua = P / K1 if P <= K1 * GAP else (P + K2 * GAP) / (K1 + K2)
        assert abs(u - ua) < 1e-12
        print(f"  P = {P:6.0f} N  u = {u * 1e3:7.4f} mm  (analitica {ua * 1e3:7.4f}) iteraciones = {it}  {'con contacto' if u > GAP else 'sin contacto'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
