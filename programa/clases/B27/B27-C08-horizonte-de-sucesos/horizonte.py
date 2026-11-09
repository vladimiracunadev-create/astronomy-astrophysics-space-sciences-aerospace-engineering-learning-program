#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C08: caida libre radial hacia un horizonte de Schwarzschild, tiempo propio y tiempo coordenado.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Masas de 10 Msol y 6.5e9 Msol
(esta ultima de M87*, EHT arXiv:1906.11238, resumen) y el radio de partida 10 r_s: valores ILUSTRATIVOS.
Modelo: caida radial desde el reposo en r0 en Schwarzschild. Tiempo propio hasta r = 0:
tau = (pi/2) sqrt(r0^3/(2GM)) (identico al newtoniano). Tiempo coordenado hasta r = r_s (1 + delta):
t = Int dr / [(1 - r_s/r) sqrt(r_s/r - r_s/r0)] c^-1 ... (se integra numericamente) y crece como (r_s/c) ln(1/delta)/sqrt(1 - r_s/r0).
Aceleracion de marea a lo largo del radio entre dos puntos separados L en r = r_s: a = 2 G M L/r_s^3.
Supuestos: agujero negro de Schwarzschild, cuerpo de prueba puntual. Validez: r > 0.
Tolerancia: 1e-8 entre tau numerico y analitico; 1 % en la pendiente de t(ln 1/delta) frente a 1/sqrt(1 - r_s/r0).
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20


def tau_numerico(r0, gm, n=200000):
    """tau = Int_0^r0 dr / sqrt(2GM (1/r - 1/r0)); con r = r0 sin^2(phi) el integrando es suave."""
    h = (math.pi / 2) / n
    f = lambda p: 2 * r0 ** 1.5 * math.sin(p) ** 2 / math.sqrt(2 * gm)
    s = f(0) + f(math.pi / 2)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return s * h / 3


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def t_coordenado(r0, rs, delta, n=40000):
    """t(r_s(1+delta)) en unidades de r_s/c: dt = dr / [c (1 - rs/r) sqrt(rs/r - rs/r0)].
    Tramo cercano al horizonte: r = rs + exp(s); tramo exterior: r = r0 - w^2 (quita la singularidad en r0)."""
    r_med = 0.5 * (rs + r0)
    f_a = lambda sv: (lambda r: r / math.sqrt(rs / r - rs / r0))(rs + math.exp(sv))   # dr = (r - rs) ds
    parte_a = simpson(f_a, math.log(rs * delta), math.log(r_med - rs), n)

    def f_b(w):
        r = r0 - w * w
        return 2 * w / ((1 - rs / r) * math.sqrt(rs * (r0 - r) / (r * r0))) if w > 0 else 2 / ((1 - rs / r0) * math.sqrt(rs / (r0 * r0)))
    parte_b = simpson(f_b, 0.0, math.sqrt(r0 - r_med), n)
    return (parte_a + parte_b) / rs


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for m_sol in (10.0, 6.5e9):
        gm = m_sol * GM_SOL
        rs = 2 * gm / C ** 2
        r0 = 10 * rs
        tn = tau_numerico(r0, gm)
        ta = math.pi / 2 * math.sqrt(r0 ** 3 / (2 * gm))
        assert abs(tn / ta - 1) < 1e-8, "tau numerico != analitico"
        print(f"M = {m_sol:.1e} Msol: r_s = {rs:.4g} m ; r0 = 10 r_s ; tau hasta r = 0: {ta:.4g} s (numerico {tn:.4g}) = {ta / (rs / C):.2f} r_s/c")
        marea = 2 * gm * 2.0 / rs ** 3
        print(f"   aceleracion de marea entre dos puntos separados 2 m en r_s: {marea:.3e} m/s2")
    # tiempo coordenado: crece logaritmicamente
    rs = 1.0
    r0 = 10.0
    t = {d: t_coordenado(r0, rs, d) for d in (1e-2, 1e-3, 1e-4, 1e-5)}
    pend = (t[1e-5] - t[1e-3]) / (math.log(1e5) - math.log(1e3))
    for d, v in t.items():
        print(f"delta = {d:.0e}: t (en r_s/c) = {v:.3f}")
    esp = 1 / math.sqrt(1 - rs / r0)
    print(f"pendiente dt/d(ln 1/delta) = {pend:.4f} r_s/c (esperado 1/sqrt(1 - r_s/r0) = {esp:.4f})")
    assert abs(pend / esp - 1) < 0.01, "divergencia logaritmica del tiempo coordenado"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
