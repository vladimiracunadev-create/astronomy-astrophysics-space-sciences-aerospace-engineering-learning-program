#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C36: desgaste abrasivo por regolito en un sello deslizante: ley de Archard con regla de dureza relativa.

DATOS ILUSTRATIVOS (ordenes de magnitud, NO consultados): dureza de la superficie H_s: aluminio 6061 1,1 GPa; acero 304 2,0 GPa; aluminio anodizado duro 4,0 GPa;
acero endurecido 7,0 GPa; carburo de volframio 20 GPa. Dureza del abrasivo (granos de regolito, minerales y vidrios) H_a = 6,0 GPa (valor inventado para el ejercicio).
Coeficiente de desgaste de Archard k(r), r = H_a/H_s: k = 1e-6 para r <= 0,8 (regimen de desgaste suave); k = 1e-3 para r >= 1,2 (abrasion severa); log-lineal entre ambos.
Modelo: profundidad de desgaste h = k c p s/H_s con presion de contacto p = 0,2 MPa, fraccion de area con abrasivo c, distancia deslizada s = v t con v = 0,05 m/s.
Gravedad: para un contacto cargado por el peso de una masa m, la presion crece con g; g_Tierra = 9,80665 m/s2 (NIST, consultado 2026-11-10) y g_Luna = 1,62 m/s2 (ILUSTRATIVO, no consultado).
Segunda via: integracion temporal por pasos (h aumenta linealmente) frente a la formula cerrada; linealidad h(2t) = 2 h(t) a 1e-12.
Vida: tiempo para llegar a un desgaste admisible de 50 micrometros.
"""
from __future__ import annotations
import math, platform

HA = 6.0
MAT = {"Aluminio 6061": 1.1, "Acero 304": 2.0, "Aluminio anodizado duro": 4.0, "Acero endurecido": 7.0, "Carburo de volframio": 20.0}
P, V = 0.2e6, 0.05
G_T, G_L = 9.80665, 1.62


def k_archard(r):
    if r <= 0.8:
        return 1e-6
    if r >= 1.2:
        return 1e-3
    t = (r - 0.8) / 0.4
    return 10 ** (-6 + 3 * t)


def profundidad(hs_gpa, c, t, p=P, ha=HA):
    return k_archard(ha / hs_gpa) * c * p * (V * t) / (hs_gpa * 1e9)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Abrasivo ILUSTRATIVO H_a = 6,0 GPa; presion de contacto 0,2 MPa; v = 0,05 m/s; k(r) de la regla de dureza (ilustrativa)")
    t = 1000 * 3600.0
    print(f"{'superficie':26s} {'H_s [GPa]':>9s} {'r=Ha/Hs':>8s} {'k':>9s} {'h(1000 h, c=1) [um]':>20s} {'h(1000 h, c=0,1) [um]':>22s} {'vida a 50 um, c=0,1 [h]':>25s}")
    for n, hs in MAT.items():
        r = HA / hs
        k = k_archard(r)
        h1 = profundidad(hs, 1.0, t) * 1e6
        h01 = profundidad(hs, 0.1, t) * 1e6
        vida = 50.0 / h01 * 1000
        print(f"{n:26s} {hs:9.1f} {r:8.2f} {k:9.2e} {h1:20.4g} {h01:22.4g} {vida:25.4g}")
    # linealidad y segunda via
    hs = 2.0
    n = 1000
    dt = t / n
    h = 0.0
    for _ in range(n):
        h += k_archard(HA / hs) * 1.0 * P * V * dt / (hs * 1e9)
    cerr = profundidad(hs, 1.0, t)
    print(f"Integracion por pasos del acero 304: {h * 1e6:.6f} um ; formula cerrada: {cerr * 1e6:.6f} um ; dif relativa = {abs(h - cerr) / cerr:.1e}")
    lin = abs(profundidad(hs, 1.0, 2 * t) - 2 * profundidad(hs, 1.0, t)) / profundidad(hs, 1.0, 2 * t)
    print(f"Linealidad h(2t) = 2 h(t): dif relativa = {lin:.1e}")
    assert abs(h - cerr) / cerr < 1e-9 and lin < 1e-12
    print("Efecto de la gravedad para un contacto cargado por el peso (p proporcional a g), acero 304, 1000 h, c = 0,1:")
    h_t = profundidad(2.0, 0.1, t, P * 1.0) * 1e6
    h_l = profundidad(2.0, 0.1, t, P * G_L / G_T) * 1e6
    print(f"  Tierra: {h_t:.3f} um ; Luna (g = 1,62): {h_l:.3f} um ; cociente = {h_l / h_t:.4f} = g_L/g_T = {G_L / G_T:.4f}")
    print("Sensibilidad a la dureza del abrasivo (acero 304, c = 0,1, 1000 h):")
    for ha in (2.0, 3.0, 4.0, 6.0, 8.0):
        print(f"  H_a = {ha:3.1f} GPa: r = {ha / 2.0:4.2f}, k = {k_archard(ha / 2.0):.2e}, h = {profundidad(2.0, 0.1, t, ha=ha) * 1e6:9.4g} um")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
