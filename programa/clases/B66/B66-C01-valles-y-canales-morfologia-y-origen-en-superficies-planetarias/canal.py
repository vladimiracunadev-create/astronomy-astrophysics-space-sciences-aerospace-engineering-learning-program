#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B66-C01: flujo uniforme en un canal (Darcy-Weisbach) en tres cuerpos.

Datos consultados (2026-11-09): gravedad media de la Tierra (9.820 m/s2) y de Marte (3.73 m/s2), fichas NASA/NSSDC;
Titan: GM = 8978.13710 km3/s2 y radio medio 2574.76 km (JPL SSD, tabla de parametros fisicos de satelites); g = GM/R^2 se CALCULA aqui.
ILUSTRATIVOS (sinteticos, no medidos): geometria del canal (W = 20 m, d = 1.0 m), pendiente S = 0.01, factor de friccion f = 0.05,
densidades del fluido (agua 1000 kg/m3; metano liquido 450 kg/m3 solo como ilustracion, no consultado).
Modelo: flujo uniforme, canal ancho rectangular, u = sqrt(8 g Rh S / f); Q = W d u; Fr = u / sqrt(g d).
Segunda via: Manning con n = Rh^(1/6) sqrt(f/(8 g)). Supuestos: friccion f independiente de g, fondo rigido, fluido newtoniano, sin sedimento.
Tolerancia: Darcy-Weisbach frente a Manning < 1e-9 relativa; Q(Marte)/Q(Tierra) = sqrt(g_M/g_T) con 1e-9.
"""
from __future__ import annotations
import math, platform

CUERPOS = {  # nombre: (g [m/s2], rho [kg/m3])
    "Tierra": (9.820, 1000.0),
    "Marte": (3.73, 1000.0),
    "Titan": (8978.13710e9 / (2574.76e3) ** 2, 450.0),
}
W, D, S, F = 20.0, 1.0, 0.01, 0.05


def rh(w, d):
    return w * d / (w + 2.0 * d)


def velocidad(g, r, s, f):
    return math.sqrt(8.0 * g * r * s / f)


def velocidad_manning(g, r, s, f):
    n = r ** (1.0 / 6.0) * math.sqrt(f / (8.0 * g))
    return r ** (2.0 / 3.0) * math.sqrt(s) / n


def profundidad_para_q(q, w, g, s, f):
    lo, hi = 1e-4, 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        qm = w * mid * velocidad(g, rh(w, mid), s, f)
        if qm < q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Canal ILUSTRATIVO: W = {W} m, d = {D} m, S = {S}, f = {F}; Rh = {rh(W, D):.4f} m")
    print(" cuerpo   g [m/s2]   u [m/s]   Q [m3/s]   Fr     tau [Pa]")
    res = {}
    dmax = 0.0
    for nom, (g, rho) in CUERPOS.items():
        r = rh(W, D)
        u = velocidad(g, r, S, F)
        um = velocidad_manning(g, r, S, F)
        dmax = max(dmax, abs(u - um) / u)
        q = W * D * u
        fr = u / math.sqrt(g * D)
        tau = rho * g * r * S
        res[nom] = (g, u, q, fr)
        print(f"{nom:7s} {g:9.4f} {u:9.4f} {q:10.3f} {fr:6.3f} {tau:9.3f}")
    print(f"Diferencia relativa maxima Darcy-Weisbach frente a Manning = {dmax:.2e}")
    rq = res["Marte"][2] / res["Tierra"][2]
    print(f"Q(Marte)/Q(Tierra) = {rq:.6f} ; sqrt(gM/gT) = {math.sqrt(res['Marte'][0] / res['Tierra'][0]):.6f}")
    print("Profundidad necesaria para Q = 100 m3/s con W = 20 m:")
    ds = {}
    for nom, (g, rho) in CUERPOS.items():
        ds[nom] = profundidad_para_q(100.0, W, g, S, F)
        print(f"  {nom:7s} d = {ds[nom]:.4f} m")
    assert dmax < 1e-9
    assert abs(rq - math.sqrt(res["Marte"][0] / res["Tierra"][0])) < 1e-9
    assert abs(res["Marte"][3] - res["Tierra"][3]) < 1e-9 and abs(res["Titan"][3] - res["Tierra"][3]) < 1e-9
    assert ds["Marte"] > ds["Tierra"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
