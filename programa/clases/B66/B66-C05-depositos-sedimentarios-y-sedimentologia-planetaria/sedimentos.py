#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B66-C05: velocidad de caida, numero de Rouse, progradacion de un delta y facies sinteticas.

Datos consultados (2026-11-09, NASA/NSSDC): g de la Tierra = 9.820 m/s2 y de Marte = 3.73 m/s2.
ILUSTRATIVOS (sinteticos, no consultados): agua de 1000 kg/m3 y viscosidad dinamica 1.0e-3 Pa s para ambos mundos; densidad de grano 2650 kg/m3;
correlacion de arrastre de esfera Cd = 24/Re (1 + 0.15 Re^0.687) (Schiller-Naumann, estandar, no consultada); kappa = 0.41; umbrales de Rouse 2.5 y 0.8;
canal W = 20 m, S = 0.01, f = 0.05; porosidad 0.4; Cs = 1e-3; ancho del frente deltaico 2000 m y altura del frente 10 m; semilla 20261109.
Modelo: ws por balance de arrastre y peso (biseccion); Stokes ws = (rho_p - rho) g D^2 /(18 mu) como segunda via; Rouse P = ws /(kappa u*), u* = sqrt(g d S);
avance del delta = Cs Q /(ancho altura (1 - porosidad)). Supuestos: granos esfericos, agua pura y fria, flujo uniforme. Tolerancia: ws frente a Stokes < 1 % para D = 20 micras.
"""
from __future__ import annotations
import math, platform, random

RHO, MU, RHO_P, KAPPA = 1000.0, 1.0e-3, 2650.0, 0.41
W, S, F, POR, CS = 20.0, 0.01, 0.05, 0.4, 1e-3
G = {"Tierra": 9.820, "Marte": 3.73}


def ws(d, g):
    lo, hi = 1e-9, 10.0
    for _ in range(200):
        v = 0.5 * (lo + hi)
        re = RHO * v * d / MU
        cd = 24.0 / re * (1.0 + 0.15 * re ** 0.687)
        # velocidad que resultaria del balance con este Cd
        v_bal = math.sqrt(4.0 * (RHO_P - RHO) * g * d / (3.0 * RHO * cd))
        if v_bal > v:
            lo = v
        else:
            hi = v
    return 0.5 * (lo + hi)


def stokes(d, g):
    return (RHO_P - RHO) * g * d * d / (18.0 * MU)


def facies(p):
    return "carga de fondo" if p > 2.5 else ("suspension mixta" if p > 0.8 else "suspension")


def prof(q, g):
    lo, hi = 1e-4, 100.0
    for _ in range(200):
        d = 0.5 * (lo + hi)
        rh = W * d / (W + 2 * d)
        qm = W * d * math.sqrt(8 * g * rh * S / F)
        lo, hi = (d, hi) if qm < q else (lo, d)
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Velocidad de caida ws [m/s] (agua ILUSTRATIVA, esfera):")
    print(" D [mm]   Tierra      Marte    Marte/Tierra")
    prev = 0.0
    for d_mm in (0.02, 0.1, 0.5, 2.0):
        d = d_mm * 1e-3
        wt, wm = ws(d, G["Tierra"]), ws(d, G["Marte"])
        assert wt > prev
        prev = wt
        print(f"{d_mm:6.2f} {wt:10.5f} {wm:10.5f} {wm / wt:8.4f}")
    d = 20e-6
    dif = abs(ws(d, G["Tierra"]) - stokes(d, G["Tierra"])) / stokes(d, G["Tierra"])
    print(f"Contraste con Stokes (D = 20 micras, Tierra): diferencia relativa = {dif:.2e}")
    assert dif < 0.01
    print("Numero de Rouse para arena de 0.5 mm en el canal ILUSTRATIVO con Q = 100 m3/s:")
    for nom, g in G.items():
        dd = prof(100.0, g)
        u = math.sqrt(g * dd * S)
        p = ws(0.5e-3, g) / (KAPPA * u)
        print(f"  {nom:6s} d = {dd:.3f} m ; u* = {u:.4f} m/s ; P = {p:.3f} -> {facies(p)}")
    q_hist = [100.0 * math.exp(random.Random(20261109 + k).gauss(0.0, 0.7)) for k in range(12)]
    print("Estratigrafia SINTETICA de 12 crecidas en Marte (grava fina de 2 mm; Rouse de la fraccion de 2 mm):")
    cuenta = {}
    espesor = 0.0
    for k, q in enumerate(q_hist):
        dd = prof(q, G["Marte"])
        u = math.sqrt(G["Marte"] * dd * S)
        p = ws(2.0e-3, G["Marte"]) / (KAPPA * u)
        f_ = facies(p)
        cuenta[f_] = cuenta.get(f_, 0) + 1
        dep = CS * q * 86400.0 / (2000.0 * 2000.0 * (1.0 - POR))  # espesor por dia sobre 2000 m x 2000 m
        espesor += dep
        print(f"  crecida {k + 1:2d}: Q = {q:7.1f} m3/s ; P = {p:5.2f} ; {f_:16s} ; espesor/dia = {dep * 1000:.3f} mm")
    print(f"Conteo de facies: {cuenta} ; espesor acumulado (1 dia por crecida) = {espesor * 1000:.2f} mm")
    avance = CS * 100.0 / (2000.0 * 10.0 * (1.0 - POR))
    print(f"Avance del frente del delta con Q = 100 m3/s: {avance:.3e} m/s = {avance * 86400:.3f} m/dia")
    assert sum(cuenta.values()) == 12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
