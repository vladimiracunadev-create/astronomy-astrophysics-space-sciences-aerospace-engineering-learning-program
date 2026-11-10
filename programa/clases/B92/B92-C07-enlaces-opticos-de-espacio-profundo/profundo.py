#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C07: escalado con la distancia, tiempo de luz y angulo de anticipacion en espacio profundo.

Datos consultados (2026-11-10), paginas de NASA y JPL sobre DSOC: velocidad maxima de 267 Mbps el 11-dic-2023 a mas de
19 millones de millas (31 millones de km); 25 Mbps el 8-abr-2024 a 140 millones de millas; 8.3 Mbps el 24-jun-2024 a
249 millones de millas; 307 millones de millas (494 millones de km) el 3-dic-2024. Las paginas NO entregan la potencia
del laser, las longitudes de onda ni las aperturas de DSOC: no se usan. c = 299792458 m/s y h = 6.62607015e-34 J s (NIST, CODATA 2022).
La milla internacional vale exactamente 1.609344 km (definicion, no consultada en una fuente concreta).
ILUSTRATIVOS (sinteticos, NO es DSOC): potencia media 4 W, longitud de onda 1552.52 nm, cintura 4 cm (theta 12.355 urad),
apertura receptora de 5 m de diametro, velocidades transversales de 1 a 50 km/s.
Modelo: tiempo de luz t = d/c; escalado de tasa a igual margen R ~ P D_t^2 D_r^2 / d^2; potencia recibida
P_rx = P G_t A_r / (4 pi d^2), G_t = 8/theta^2; angulo de anticipacion alpha = v_perp / c.
Segunda via: la razon de tasas entre dos distancias se calcula con la formula cerrada (d0/d1)^2 y con la razon de fotones
recibidos del balance completo; deben coincidir con 1e-12 relativa.
"""
from __future__ import annotations
import math, platform

C = 299792458.0
H = 6.62607015e-34
MILLA_KM = 1.609344
LAM = C / 193.1e12
TH = LAM / (math.pi * 0.04)


def fotones_recibidos(d_m, p=4.0, th=TH, dr=5.0):
    gt = 8.0 / th ** 2
    ar = math.pi * (dr / 2.0) ** 2
    prx = p * gt * ar / (4.0 * math.pi * d_m ** 2)
    return prx, prx / (H * C / LAM)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ref_d, ref_r = 31e6, 267.0
    print(f"Referencia publicada (NASA/JPL): {ref_r:.0f} Mbps a {ref_d / 1e6:.0f} millones de km")
    print("Distancias publicadas y escalado 1/d^2 desde la referencia (a igual margen y configuracion):")
    print("  fecha        d [Mkm]  luz ida [s]  luz ida y vuelta [min]  R escalada [Mbps]  R publicada [Mbps]  cociente  [dB]")
    pub = (("2023-12-11", 31.0, 267.0), ("2024-04-08", 140 * MILLA_KM, 25.0), ("2024-06-24", 249 * MILLA_KM, 8.3), ("2024-12-03", 494.0, None))
    for fecha, dm, rp in pub:
        d = dm * 1e6
        t = d * 1e3 / C
        resc = ref_r * (ref_d / d) ** 2
        if rp is not None:
            print(f"  {fecha}  {dm:8.2f}  {t:10.1f}  {2 * t / 60:20.2f}  {resc:16.3f}  {rp:17.1f}  {rp / resc:8.2f}  {10 * math.log10(rp / resc):5.2f}")
        else:
            print(f"  {fecha}  {dm:8.2f}  {t:10.1f}  {2 * t / 60:20.2f}  {resc:16.3f}  {'no publicada':>17s}")
    print("Balance de fotones de un terminal ILUSTRATIVO (no es DSOC): 4 W, theta = 12.355 urad, receptor de 5 m")
    print("  d [Mkm]   P_rx [W]     fotones/s     fotones por bit a 1 Mbps")
    dd = 0.0
    prev = None
    for dm in (31.0, 225.3, 400.7):
        prx, fps = fotones_recibidos(dm * 1e9)
        print(f"  {dm:7.1f}  {prx:10.3e}  {fps:11.3e}  {fps / 1e6:12.2f}")
        if prev is not None:
            dd = max(dd, abs(prev[1] / fps - (dm / prev[0]) ** 2) / (dm / prev[0]) ** 2)
        prev = (dm, fps)
    print(f"Razon de fotones frente a (d1/d0)^2: diferencia relativa maxima = {dd:.1e}")
    print("Angulo de anticipacion alpha = v_perp / c  (v en km/s):")
    print("  v [km/s]  alpha [urad]  alpha/theta  perdida si no se aplica [dB]")
    for v in (1.0, 10.0, 30.0, 50.0):
        a = v * 1e3 / C
        print(f"  {v:8.1f}  {a * 1e6:11.2f}  {a / TH:11.2f}  {10 * math.log10(math.exp(-2 * (a / TH) ** 2)):14.1f}")
    print(f"Cambio de tasa al duplicar el diametro receptor (R ~ D_r^2): x{2.0 ** 2:.0f} = {10 * math.log10(4.0):.2f} dB")
    assert dd < 1e-12
    assert abs(31e6 * 1e3 / C - 103.4) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
