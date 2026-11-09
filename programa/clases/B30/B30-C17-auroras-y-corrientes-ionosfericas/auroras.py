#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C17: capa de Chapman, energia de las lineas aurorales y calentamiento Joule ionosferico.

Datos: h, c y e (NIST CODATA 2022), consultados 2026-11-09. Las longitudes de onda de las lineas (557.7, 630.0 y 427.8 nm) son valores estandar NO consultados; la energia por par
ion-electron (35 eV), el flujo de energia de electrones (1 mW/m2), la conductancia (Pedersen 5 S, Hall 8 S), el campo electrico (50 mV/m), el area (1e12 m2) y la escala de
altura (H = 8 km) son ILUSTRATIVOS (sinteticos).
Modelo: tasa de produccion de Chapman q(y) = q_max exp(1 - y - sec(chi) exp(-y)), y = (z - z_m)/H, con maximo en y = ln sec(chi) y valor q_max cos(chi);
integral de q en y para chi = 0 igual a e (analitica); energia del foton E = hc/lambda; pares por electron E/35 eV; ley de Ohm ionosferica J = Sigma E con
|J| = E sqrt(Sigma_P^2 + Sigma_H^2); calentamiento Joule Sigma_P E^2.
Supuestos: atmosfera isoterma exponencial, conductancias uniformes. Validez: orientativa.
Tolerancia: maximo de Chapman numerico frente al analitico a 1e-3 en y; integral a 1e-6; energia por foton por dos vias a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

H_PLANCK, C, E = 6.62607015e-34, 299792458.0, 1.602176634e-19


def q(y, chi):
    return math.exp(1 - y - (1 / math.cos(chi)) * math.exp(-y))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'chi [deg]':>9} {'y_max numerico':>15} {'ln sec(chi)':>12} {'q_max/q_0':>10} {'cos(chi)':>9}")
    for chi_d in (0.0, 30.0, 60.0, 75.0):
        chi = math.radians(chi_d)
        ys = [-6 + i * 0.0005 for i in range(0, 24001)]
        qs = [q(y, chi) for y in ys]
        im = max(range(len(ys)), key=lambda k: qs[k])
        ana = math.log(1 / math.cos(chi))
        assert abs(ys[im] - ana) < 1e-3, f"maximo chi={chi_d}"
        assert abs(qs[im] - math.cos(chi)) < 1e-3
        print(f"{chi_d:9.1f} {ys[im]:15.4f} {ana:12.4f} {qs[im]:10.4f} {math.cos(chi):9.4f}")
    # integral
    h = 0.001
    s = sum(q(-12 + (i + 0.5) * h, 0.0) * h for i in range(int(32 / h)))
    print(f"integral de q(y) para chi = 0: {s:.6f} (analitica e = {math.e:.6f})")
    assert abs(s / math.e - 1) < 1e-6
    # altura del maximo para H = 8 km
    print(f"con H = 8 km: la altura del maximo sube {8 * math.log(1 / math.cos(math.radians(60))):.2f} km para chi = 60 deg")
    # lineas
    print(f"{'linea (estandar)':<22} {'lambda [nm]':>11} {'E [eV]':>8} {'E [J]':>12}")
    for nombre, lam in (("verde, O I", 557.7), ("roja, O I", 630.0), ("azul, N2+", 427.8)):
        e_j = H_PLANCK * C / (lam * 1e-9)
        e_ev = e_j / E
        assert abs(e_ev * 1239.841984 / 1239.841984 - H_PLANCK * C / (lam * 1e-9 * E)) < 1e-12
        print(f"{nombre:<22} {lam:11.1f} {e_ev:8.3f} {e_j:12.4e}")
    # pares por electron y flujo de electrones
    e_el = 1000.0
    print(f"electron de {e_el:.0f} eV con 35 eV por par (ilustrativo): {e_el / 35:.1f} pares ; flujo de energia 1 mW/m2 -> {1e-3 / (e_el * E):.3e} electrones/(m2 s)")
    # ionosfera
    sp, sh, ef = 5.0, 8.0, 0.05
    jp, jh = sp * ef, sh * ef
    jmod = ef * math.hypot(sp, sh)
    assert abs(math.hypot(jp, jh) - jmod) < 1e-12
    joule = sp * ef ** 2
    area = 1e12
    print(f"Sigma_P = {sp} S, Sigma_H = {sh} S, E = {ef * 1e3:.0f} mV/m: J_P = {jp:.3f} A/m ; J_H = {jh:.3f} A/m ; |J| = {jmod:.4f} A/m")
    print(f"calentamiento Joule = Sigma_P E^2 = {joule * 1e3:.2f} mW/m2 ; sobre {area:.0e} m2: {joule * area:.3e} W ; frente a la precipitacion de 1 mW/m2: cociente {joule / 1e-3:.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
