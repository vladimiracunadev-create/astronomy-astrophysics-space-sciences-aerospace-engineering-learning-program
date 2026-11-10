#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C01: entorno de vibracion aleatoria de lanzamiento (niveles del GEVS) y su valor eficaz.

Datos CONSULTADOS (2026-11-10): NASA/GSFC GSFC-STD-7000 (GEVS) Version B, Cambio 0, 2021-04-28:
  Tabla 2.4-3 (componentes en ELV, hasta 22,7 kg): 20 Hz 0,026 g2/Hz (calificacion) / 0,013 (aceptacion); +6 dB/oct hasta 50 Hz;
     meseta 0,16 / 0,08 g2/Hz de 50 a 800 Hz; -6 dB/oct hasta 2000 Hz con 0,026 / 0,013 g2/Hz; totales publicados 14,1 g rms y 10,0 g rms.
  Tabla 2.4-4 (minimo de mano de obra, hasta 45,4 kg): 20 Hz 0,01 g2/Hz; +3 dB/oct hasta 80 Hz; meseta 0,04 g2/Hz hasta 500 Hz;
     -3 dB/oct hasta 2000 Hz con 0,01 g2/Hz; total publicado 6,8 g rms.
  Reduccion de la meseta para W > 22,7 kg (Tabla 2.4-3): ASD = 0,16 * (22,7/W) (calificacion).
Metodo: integral exacta de una ASD lineal a tramos en log-log (6 dB/oct equivale a ASD ~ f^2 y 3 dB/oct a ASD ~ f).
Unidades: f [Hz], ASD [g2/Hz], g rms [g]. Tolerancia: coincidencia con el valor publicado dentro de 0,05 g rms (el estandar da 3 cifras).
Los pesos de ejemplo (35 kg, 59 kg) son ILUSTRATIVOS.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import asd_grms


def tabla_243(meseta, borde):
    """Perfil de la Tabla 2.4-3: pendientes +/-6 dB/oct (ASD ~ f^2). Los extremos 'borde' se recalculan si la meseta se reduce."""
    # 20 Hz -> 50 Hz sube con f^2: valor en 20 Hz = meseta * (20/50)^2 (para 0,16: 0,0256 ~ 0,026 publicado)
    return [(20.0, borde), (50.0, meseta), (800.0, meseta), (2000.0, borde)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    cal = tabla_243(0.16, 0.026)
    ace = tabla_243(0.08, 0.013)
    # Perfil de mano de obra minima (Tabla 2.4-4): +3 dB/oct (ASD ~ f)
    mano = [(20.0, 0.01), (80.0, 0.04), (500.0, 0.04), (2000.0, 0.01)]
    res = {
        "Calificacion (Tabla 2.4-3)": (asd_grms(cal), 14.1),
        "Aceptacion (Tabla 2.4-3)": (asd_grms(ace), 10.0),
        "Mano de obra minima (Tabla 2.4-4)": (asd_grms(mano), 6.8),
    }
    print("Perfil                                  g rms calc   g rms publicado   dif")
    for k, (g, pub) in res.items():
        print(f"{k:38s} {g:9.3f} {pub:15.1f} {g - pub:9.3f}")
    # pendientes reales entre puntos (exponente de f)
    for nombre, perfil in (("Cal", cal), ("Mano", mano)):
        ms = [math.log(b[1] / a[1]) / math.log(b[0] / a[0]) for a, b in zip(perfil, perfil[1:])]
        print(f"Exponentes de f (ASD ~ f^m) {nombre}: " + ", ".join(f"{m:.2f}" for m in ms))
    # Reduccion por masa (Tabla 2.4-3): meseta = 0,16 * 22,7 / W
    print("Reduccion de la meseta de calificacion con la masa (masas ILUSTRATIVAS):")
    for w in (22.7, 35.0, 59.0):
        pl = 0.16 * 22.7 / w
        borde = 0.026 * 22.7 / w
        g = asd_grms(tabla_243(pl, borde))
        print(f"  W = {w:5.1f} kg  meseta = {pl:.4f} g2/Hz  dB de reduccion = {10 * math.log10(w / 22.7):5.2f}  g rms = {g:.2f}")
    # Cada g rms como fuerza equivalente: F = m * 3 sigma * g0 (g0 de NIST: 9,80665 m/s2)
    g0 = 9.80665
    m = 35.0
    grms = res["Calificacion (Tabla 2.4-3)"][0]
    print(f"Fuerza 3-sigma sobre 35 kg con {grms:.2f} g rms (cota de mesa, no carga de diseno): {m * 3 * grms * g0:.0f} N")
    for k, (g, pub) in res.items():
        assert abs(g - pub) < 0.05, k
    assert 1.95 < math.log(0.16 / 0.026) / math.log(50 / 20) < 2.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
