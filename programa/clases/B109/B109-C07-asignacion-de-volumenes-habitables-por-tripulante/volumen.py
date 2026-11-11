#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C07: volumen neto habitable (NHV) por tripulante a partir del volumen bruto y de los descuentos.

Datos consultados (2026-11-10): Burke, Howard y Kessler (2022): el recinto del Surface Habitat da ~127 m3 de volumen habitable (casi 64 m3 por tripulante para dos), altura estandar 2.4 m,
areas recomendadas 14.6 m2 y de trazado 42.63 m2 (Tabla 4), nucleo de 3.3 m de diametro, cubierta metalica de 4.4 m x 2.6 m, parte inflable de 6.5 m x 5.2 m; informe de consenso HRP (2014):
NHV = volumen que queda para la tripulacion tras descontar equipo desplegado, almacenamiento, basura y huecos; recomendacion de 25 m3 por persona para una mision de 30 meses a Marte (Mars DRM 5.0).
ILUSTRATIVOS (no son mediciones): fracciones de descuento (equipo 25 %, almacenamiento 12 %, huecos 10 %, basura 2 %) y sus rangos de incertidumbre uniformes
(equipo 15-35 %, almacenamiento 5-20 %, huecos 5-15 %, basura 1-3 %). Los 25 m3 NO son un requisito de un habitat lunar de 30 dias.
Modelo: NHV = V_bruto (1 - suma de fracciones). Incertidumbre: sorteos uniformes independientes (semilla 109007, 20000).
Segunda via: la suma de volumenes descontados mas el NHV debe ser el volumen bruto (1e-9); el descuento multiplicativo (1-f1)(1-f2)... difiere del aditivo y se muestra la diferencia.
Unidades: volumen [m3], area [m2], altura [m].
"""
from __future__ import annotations
import math, platform, random

V_BRUTO = 127.0  # m3, Burke et al. 2022 (aprox.)
H = 2.4
DESC = {"equipo desplegado": (0.25, 0.15, 0.35), "almacenamiento": (0.12, 0.05, 0.20), "huecos y estructura": (0.10, 0.05, 0.15), "basura": (0.02, 0.01, 0.03)}
REF_HRP = 25.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Descuentos ILUSTRATIVOS; volumen bruto y areas de Burke et al. (2022); 25 m3/persona del informe HRP solo como comparacion (mision de 30 meses a Marte)")
    centro = sum(v[0] for v in DESC.values())
    nhv = V_BRUTO * (1 - centro)
    print(f"Volumen bruto = {V_BRUTO:.1f} m3 ({V_BRUTO / 2:.1f} m3 por tripulante con 2)")
    desc_vol = 0.0
    for k, (f, lo, hi) in DESC.items():
        print(f"   descuento {k:20s} {f * 100:5.1f} % = {V_BRUTO * f:6.2f} m3")
        desc_vol += V_BRUTO * f
    assert abs(desc_vol + nhv - V_BRUTO) < 1e-9
    mult = V_BRUTO
    for f, _, _ in DESC.values():
        mult *= 1 - f
    print(f"NHV (descuento aditivo) = {nhv:.2f} m3 ; NHV (descuento multiplicativo) = {mult:.2f} m3 ; diferencia = {mult - nhv:.2f} m3")
    for n in (2, 4):
        print(f"   NHV por tripulante con {n} = {nhv / n:.2f} m3  (referencia HRP {REF_HRP:.0f} m3: {'por encima' if nhv / n >= REF_HRP else 'por debajo'})")
    rng = random.Random(109007)
    N = 20000
    vals = []
    for _ in range(N):
        t = sum(rng.uniform(lo, hi) for _, lo, hi in DESC.values())
        vals.append(V_BRUTO * (1 - t) / 2)
    vals.sort()
    p_ok = sum(1 for v in vals if v >= REF_HRP) / N
    print(f"Monte Carlo (2 tripulantes): NHV/trip P5 = {vals[int(0.05 * N)]:.2f} ; P50 = {vals[N // 2]:.2f} ; P95 = {vals[int(0.95 * N)]:.2f} m3 ; P(>= 25) = {p_ok:.4f}")
    print(f"Volumen funcional (area x 2.4 m): minimo recomendado {14.6 * H:.1f} m3 ({14.6 * H / 2:.1f} por trip.) ; trazado {42.63 * H:.1f} m3 ({42.63 * H / 2:.1f} por trip.)")
    geo_metal = math.pi / 4 * 4.4 ** 2 * 2.6
    geo_inf = math.pi / 4 * (6.5 ** 2 - 3.3 ** 2) * 5.2
    print(f"Geometria publicada (cilindros): metalica {geo_metal:.1f} m3 ; inflable sin nucleo {geo_inf:.1f} m3 ; suma {geo_metal + geo_inf:.1f} m3 (el articulo da ~127 m3 de 'volumen habitable': su desglose no se consulto)")
    assert 0 < nhv < V_BRUTO
    assert abs(mult - nhv) < 0.1 * V_BRUTO
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
