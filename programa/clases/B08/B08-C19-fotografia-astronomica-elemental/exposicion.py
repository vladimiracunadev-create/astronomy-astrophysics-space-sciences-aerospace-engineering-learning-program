#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C19: cuánto puedes exponer sin que las estrellas dejen estela.

Datos PUBLICADOS: rotación sidérea 23,9345 h (NASA Earth Fact Sheet, act. 15-nov-2024, consultada 2026-11-05) y
diámetro angular de la Luna 1762-2009 arcsec en 2025 (NASA SVS 5415, tabla de 2025, consultada 2026-11-05). Cámaras y objetivos:
valores de EJEMPLO. Modelo (SIMULADO): escala de placa = 206265 * pixel/focal (arcsec/px); estela = Omega cos(dec) t / escala;
tiempo máximo sin seguimiento para una estela de k píxeles = k * escala / (Omega cos dec). La «regla de 500» (t = 500/f) es una regla
práctica popular NO verificada en una fuente: aquí solo se evalúa qué estela implica. Dominio: estrellas, óptica sin distorsión.
Tolerancias: exactitud analítica 1e-9.
Prueba independiente: escala de placa de 1000 mm y píxel de 5 µm = 1,0313 arcsec/px (cálculo a mano); una estrella en el ecuador
recorre 15,041 arcsec/s; campo del sensor por la fórmula 2 atan(w/2f) contra la aproximación w/f.
"""
from __future__ import annotations

import math
import sys

OMEGA = 360.0 * 3600.0 / (23.9345 * 3600.0)       # arcsec/s
ARCSEC_RAD = 206264.806


def escala_placa(pixel_um: float, focal_mm: float) -> float:
    return ARCSEC_RAD * pixel_um * 1e-3 / focal_mm


def estela_px(t_s: float, dec: float, pixel_um: float, focal_mm: float) -> float:
    return OMEGA * math.cos(math.radians(dec)) * t_s / escala_placa(pixel_um, focal_mm)


def t_max_s(k_px: float, dec: float, pixel_um: float, focal_mm: float) -> float:
    return k_px * escala_placa(pixel_um, focal_mm) / (OMEGA * math.cos(math.radians(dec)))


def campo_deg(sensor_mm: float, focal_mm: float) -> float:
    return math.degrees(2.0 * math.atan(sensor_mm / (2.0 * focal_mm)))


def luna_px(diam_arcsec: float, pixel_um: float, focal_mm: float) -> float:
    return diam_arcsec / escala_placa(pixel_um, focal_mm)


def pruebas() -> None:
    assert abs(escala_placa(5.0, 1000.0) - 1.0313) < 0.0002, escala_placa(5.0, 1000.0)
    assert abs(OMEGA - 15.041) < 0.001
    assert abs(estela_px(1.0, 0.0, 5.0, 1000.0) - 15.041 / 1.0313) < 0.01
    assert abs(campo_deg(36.0, 50.0) - 39.6) < 0.1                      # sensor de 36 mm con 50 mm de focal
    assert abs(t_max_s(1.0, 0.0, 5.0, 1000.0) * OMEGA - escala_placa(5.0, 1000.0)) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Configuraciones de EJEMPLO (SIMULADO). Omega = %.3f arcsec/s" % OMEGA)
    for nombre, f, px, sensor in [("gran angular 24 mm", 24.0, 4.3, 36.0), ("normal 50 mm", 50.0, 4.3, 36.0),
                                  ("tele 200 mm", 200.0, 4.3, 36.0), ("telescopio 1000 mm", 1000.0, 5.0, 23.5)]:
        esc = escala_placa(px, f)
        t1 = t_max_s(1.0, 0.0, px, f)
        t1s = t_max_s(1.0, -60.0, px, f)
        print(f"{nombre}: escala {esc:5.2f} arcsec/px | campo {campo_deg(sensor, f):5.1f} grados | t_max(1 px) ecuador {t1:5.1f} s, dec -60 {t1s:5.1f} s"
              f" | estela con 500/f = {500.0 / f:5.1f} s: {estela_px(500.0 / f, 0.0, px, f):5.1f} px")
    for f in (200.0, 1000.0):
        print(f"La Luna (1762-2009 arcsec) con f = {f:.0f} mm y pixel 4,3 um: {luna_px(1762.3, 4.3, f):.0f} a {luna_px(2008.6, 4.3, f):.0f} px de diametro")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
