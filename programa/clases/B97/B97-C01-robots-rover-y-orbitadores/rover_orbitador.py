#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C01: presupuesto de recorrido de un rover frente a la cobertura de un orbitador.

Datos consultados (2026-11-10): Marte, g media 3.73 m/s2 y radio medio 3389.5 km (NASA/NSSDC); Perseverance: 1025 kg y velocidad maxima
~152 m/h sobre terreno plano y duro (NASA). GM = g R^2 se CALCULA aqui (aproximacion: ignora rotacion y achatamiento).
ILUSTRATIVOS (sinteticos, no medidos): factor de uso de la velocidad 0.5, 4 h de conduccion por dia de operacion, altitud 300 km, franja de la camara 12 km.
Modelo: orbita circular kepleriana, T = 2 pi sqrt(a^3/GM); velocidad sobre el suelo v_g = v_c R / a (sin rotacion del planeta).
Segunda via: integracion numerica de velocidad-Verlet de una orbita; error de cierre < 1e-6 (relativo a a).
Unidades SI; sistema de referencia: inercial centrado en Marte, orbita en un plano.
"""
from __future__ import annotations
import math, platform

G_M, R_M = 3.73, 3389.5e3          # m/s2, m (NASA/NSSDC)
V_MAX = 152.0 / 3600.0              # m/s (NASA, terreno plano y duro)
MASA = 1025.0                       # kg (NASA)
USO, HORAS, ALT, FRANJA = 0.5, 4.0, 300e3, 12e3   # ILUSTRATIVOS
REGION = (100e3, 100e3)             # region a cubrir [m] (ilustrativa)
RUTA = 5e3                          # ruta del rover [m] (ilustrativa)


def verlet(gm, a, n=40000):
    """Integra una orbita circular durante un periodo; devuelve el error de cierre en m."""
    t = 2 * math.pi * math.sqrt(a ** 3 / gm)
    dt = t / n
    x, y, vx, vy = a, 0.0, 0.0, math.sqrt(gm / a)
    ax, ay = -gm * x / a ** 3, -gm * y / a ** 3
    for _ in range(n):
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        r3 = math.hypot(x, y) ** 3
        ax, ay = -gm * x / r3, -gm * y / r3
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
    return math.hypot(x - a, y)


def calc():
    gm = G_M * R_M ** 2
    a = R_M + ALT
    t = 2 * math.pi * math.sqrt(a ** 3 / gm)
    vc = math.sqrt(gm / a)
    vg = vc * R_M / a
    tasa = FRANJA * vg                       # m2/s
    t_img = REGION[0] * REGION[1] / tasa     # s de imagen continua
    dia = V_MAX * USO * HORAS * 3600.0       # m por dia de operacion
    err = verlet(gm, a)
    return dict(gm=gm, a=a, T_min=t / 60.0, vc=vc, vg=vg, tasa_km2s=tasa / 1e6, t_img=t_img, t_img_min=t_img / 60.0,
                dia=dia, dias_ruta=RUTA / dia, peso=MASA * G_M, vmax_mh=V_MAX * 3600, err_rel=err / a,
                razon=(t_img / 86400.0) / (RUTA / dia), a_km=a / 1e3, t500_min=250e3 * 1e6 / tasa / 60.0,
                T600_min=2 * math.pi * math.sqrt((R_M + 600e3) ** 3 / gm) / 60.0)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"GM = g R^2 = {r['gm']:.4e} m3/s2 (derivado, aproximado); a = {r['a']/1e3:.1f} km")
    print(f"Orbitador ILUSTRATIVO a {ALT/1e3:.0f} km: T = {r['T_min']:.2f} min; v_circ = {r['vc']:.1f} m/s; v_suelo = {r['vg']:.1f} m/s")
    print(f"Franja {FRANJA/1e3:.0f} km -> tasa de cobertura = {r['tasa_km2s']:.2f} km2/s; region 100 x 100 km en {r['t_img_min']:.2f} min de imagen continua")
    print(f"Rover (1025 kg, peso en Marte {r['peso']:.1f} N): {r['dia']:.1f} m por dia de operacion con uso {USO}; {RUTA/1e3:.0f} km en {r['dias_ruta']:.2f} dias")
    print(f"Error de cierre de la orbita integrada (Verlet) = {r['err_rel']:.2e} del radio orbital")
    assert r["err_rel"] < 1e-6
    assert abs(r["T_min"] * 60.0 - 2 * math.pi * r["a"] / r["vc"]) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
