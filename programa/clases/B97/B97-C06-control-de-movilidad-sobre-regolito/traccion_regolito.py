#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C06: traccion de un rover de seis ruedas sobre un suelo blando (Mohr-Coulomb con deformacion de corte tipo Janosi-Hanamoto).

Datos consultados (2026-11-10): gravedad media de la Tierra 9.820, de Marte 3.73 y de la Luna 1.62 m/s2 (NASA/NSSDC); masa de Perseverance 1025 kg,
seis ruedas de 52.5 cm de diametro (NASA). ILUSTRATIVOS (sinteticos, no medidos): cohesion c = 1.0 kPa, angulo de friccion 35 deg, modulo de deformacion de corte
K = 0.018 m, longitud de contacto L = 0.12 m, ancho b = 0.40 m, resistencia a la rodadura 10 % del peso, deslizamiento 0.20. NO son propiedades de ningun regolito real.
Modelo: tension normal uniforme sigma = W_rueda/(b L); tension de corte tau(x) = (c + sigma tan(phi)) (1 - exp(-s x / K)); empuje H = b integral_0^L tau dx
= (c A + W tan phi)(1 - (K/(s L))(1 - exp(-s L/K))); traccion DP = H - 0.10 W; pendiente maxima aproximada sin(theta) = DP/W.
Segunda via: integracion numerica de tau por Simpson (2000 intervalos), tolerancia relativa 1e-9. Suelo plano, reparto de carga uniforme entre ruedas.
"""
from __future__ import annotations
import math, platform

MASA, NR = 1025.0, 6
C, PHI, K, L, B, CRR, S0 = 1000.0, math.radians(35.0), 0.018, 0.12, 0.40, 0.10, 0.20   # ILUSTRATIVOS
GRAV = {"Tierra": 9.820, "Marte": 3.73, "Luna": 1.62}                                  # NASA/NSSDC


def empuje(w, s):
    a = B * L
    return (C * a + w * math.tan(PHI)) * (1 - (K / (s * L)) * (1 - math.exp(-s * L / K)))


def empuje_num(w, s, n=2000):
    sig = w / (B * L)
    f = lambda x: (C + sig * math.tan(PHI)) * (1 - math.exp(-s * x / K))
    h = L / n
    tot = f(0) + f(L)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(i * h)
    return B * tot * h / 3


def calc():
    res = {}
    for nombre, g in GRAV.items():
        w = MASA * g / NR
        h = empuje(w, S0)
        dp = h - CRR * w
        res[nombre] = dict(w=w, h=h, dp=dp, rel=dp / w, theta=math.degrees(math.asin(min(1.0, dp / w))))
    dif = max(abs(empuje(MASA * g / NR, S0) - empuje_num(MASA * g / NR, S0)) / empuje(MASA * g / NR, S0) for g in GRAV.values())
    barrido = [(s, (empuje(MASA * GRAV["Marte"] / NR, s) - CRR * MASA * GRAV["Marte"] / NR) / (MASA * GRAV["Marte"] / NR)) for s in (0.05, 0.1, 0.2, 0.4, 0.8)]
    return dict(res=res, dif=dif, barrido=barrido, rel_marte=res["Marte"]["rel"], rel_luna=res["Luna"]["rel"], rel_tierra=res["Tierra"]["rel"],
                th_marte=res["Marte"]["theta"], th_luna=res["Luna"]["theta"], th_tierra=res["Tierra"]["theta"],
                dp_marte=res["Marte"]["dp"], dp_tierra=res["Tierra"]["dp"], dp_luna=res["Luna"]["dp"],
                w_marte=res["Marte"]["w"], w_luna=res["Luna"]["w"], w_tierra=res["Tierra"]["w"],
                h_marte=res["Marte"]["h"], razon_luna_tierra=res["Luna"]["rel"] / res["Tierra"]["rel"], s_c=C * B * L)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Rover {MASA:.0f} kg, {NR} ruedas; suelo ILUSTRATIVO c = {C:.0f} Pa, phi = 35 deg, K = {K} m; deslizamiento {S0}")
    print(" cuerpo   W/rueda [N]   empuje [N]   DP [N]   DP/W    pendiente max [deg]")
    for n, d in r["res"].items():
        print(f"{n:7s} {d['w']:12.2f} {d['h']:12.2f} {d['dp']:9.2f} {d['rel']:7.4f} {d['theta']:12.2f}")
    print("DP/W en Marte segun el deslizamiento: " + "; ".join(f"s={s}: {v:.4f}" for s, v in r["barrido"]))
    print(f"Diferencia relativa maxima entre forma cerrada e integral numerica = {r['dif']:.2e}")
    assert r["dif"] < 1e-9 and r["rel_luna"] > r["rel_marte"] > r["rel_tierra"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
