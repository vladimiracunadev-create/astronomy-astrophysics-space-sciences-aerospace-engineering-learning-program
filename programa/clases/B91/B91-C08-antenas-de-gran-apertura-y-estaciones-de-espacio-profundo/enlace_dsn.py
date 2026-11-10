#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C08: G/T, perdida por apuntamiento y presupuesto de enlace de una antena de espacio profundo de 70 m.

Datos consultados (2026-11-10), NASA/JPL DSN 810-005 modulo 101 rev. D (2011), antena de 70 m (DSS-14):
  Tabla 1 (tx): ganancia X 7145 MHz = 73.23 dBi (dicroico retraido); perdida de guia de onda X = 0.45 dB (transmisor de 20 kW); EIRP X = 145.8 dBm; HPBW tx = 0.038 deg.
  Tabla 2 (rx): ganancia X 8420 MHz = 74.55 dBi (DSS-14, solo X); HPBW rx = 0.032 deg; Tabla 4: T_op = 16.69 K en zenit (X-only, RCP, CD = 25 %).
  Tabla 3: reduccion de ganancia por viento en X: 0.1 dB (32 km/h), 0.3 dB (48 km/h), 1.5 dB (72 km/h).
  Ecuacion A9: Delta G = 10 log10 exp(-2.773 theta^2 / HPBW^2) [dB] (aproximacion gaussiana; el modulo advierte que subestima la perdida lejos del eje).
Constantes: k_B = 1.380649e-23 J/K (SI exacto); 1 ua = 149 597 870 700 m (UAI 2012); c = 299 792 458 m/s.
SINTETICO (satelite): P_tx = 20 W, antena de 3.0 m con eta = 0.55, distancia 2.0 ua, perdida de polarizacion 0.1 dB, atmosfera 0.1 dB,
  perdida de apuntamiento de la sonda 0.3 dB, Eb/N0 requerido 2.0 dB + margen 3.0 dB. La antena de 34 m se ESCALA por area (no es un valor publicado).
Comprobaciones: (a) EIRP = P_tx - L_guia + G reproduce 145.8 dBm; (b) Delta G(HPBW/2) = -3.01 dB; (c) G/T por dos vias; (d) velocidad por dos vias.
Tolerancias: (a) 0.05 dB; (b) 0.01 dB.
"""
from __future__ import annotations
import math, platform

KB = 1.380649e-23
UA = 149_597_870_700.0
C = 299_792_458.0


def db(x):
    return 10 * math.log10(x)


def dg_apunt(theta, hpbw):
    return 10 * math.log10(math.exp(-2.773 * theta * theta / (hpbw * hpbw)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # (a) EIRP
    p_dbm = db(20e3 * 1e3)
    eirp = p_dbm - 0.45 + 73.23
    print(f"(a) EIRP X = 10 log(20 kW en mW) - 0.45 dB + 73.23 dBi = {p_dbm:.2f} - 0.45 + 73.23 = {eirp:.2f} dBm (publicado 145.8 dBm, diferencia {eirp-145.8:+.2f} dB)")
    assert abs(eirp - 145.8) < 0.05
    # (b) apuntamiento
    hp = 0.032
    print(f"(b) Apuntamiento rx (HPBW {hp} deg): Delta G(HPBW/2) = {dg_apunt(hp/2, hp):.3f} dB")
    assert abs(dg_apunt(hp / 2, hp) + 3.01) < 0.01
    print("   error theta [mdeg]   theta/HPBW   perdida [dB]")
    for t in (2, 4, 8, 16, 24):
        print(f"      {t:6.1f}             {t*1e-3/hp:6.3f}      {dg_apunt(t*1e-3, hp):8.3f}")
    print("   Viento (Tabla 3, X): 32 km/h -> -0.1 dB ; 48 km/h -> -0.3 dB ; 72 km/h -> -1.5 dB")
    # (c) G/T
    g_rx, t_op = 74.55, 16.69
    gt = g_rx - db(t_op)
    print(f"(c) G/T = {g_rx} dBi - 10 log({t_op} K) = {gt:.2f} dB/K ; via lineal (G/T en cociente): {db(10**(g_rx/10)/t_op):.2f} dB/K")
    assert abs(gt - db(10 ** (g_rx / 10) / t_op)) < 1e-9
    # 34 m escalado
    g34 = g_rx + db((34.0 / 70.0) ** 2)
    print(f"    Antena de 34 m ESCALADA por area desde 70 m (misma eficiencia y T_op, NO publicado): G = {g34:.2f} dBi, G/T = {g34-db(t_op):.2f} dB/K")
    for n in (2, 4):
        gta = g34 + db(n) - db(t_op)
        print(f"    Arreglo ideal de {n} x 34 m (combinacion coherente sin perdidas): G/T = {gta:.2f} dB/K  (70 m: {gt:.2f})")
    # Presupuesto de enlace sintetico
    f = 8.42e9
    lam = C / f
    d = 2.0 * UA
    fspl = 20 * math.log10(4 * math.pi * d / lam)
    g_sc = db(0.55 * (math.pi * 3.0 / lam) ** 2)
    eirp_sc = db(20.0) + g_sc  # dBW
    print(f"Enlace SINTETICO de bajada: f = 8.42 GHz, d = 2.0 ua = {d/1e9:.1f} Gm; perdida de espacio libre = {fspl:.2f} dB")
    print(f"    G satelite = {g_sc:.2f} dBi ; EIRP satelite = {eirp_sc:.2f} dBW")
    perdidas = {"polarizacion": 0.1, "atmosfera (cielo claro, ILUSTRATIVO)": 0.1, "apuntamiento satelite": 0.3, "apuntamiento estacion (4 mdeg)": -dg_apunt(4e-3, hp)}
    for k, v in perdidas.items():
        print(f"    {k:40s} {v:6.3f} dB")
    cn0 = eirp_sc - fspl + gt - sum(perdidas.values()) - db(KB)
    cn0_ref = eirp_sc - fspl + (g_rx - db(t_op)) - sum(perdidas.values()) + 228.6
    print(f"    C/N0 = {cn0:.2f} dB-Hz (con k_B exacto) ; con -228.6 dBW/Hz/K redondeado: {cn0_ref:.2f}")
    assert abs(cn0 - cn0_ref) < 0.01
    req = 2.0 + 3.0
    r_db = cn0 - req
    print(f"    Eb/N0 requerido 2.0 dB + margen 3.0 dB -> velocidad soportable R = 10^({r_db:.2f}/10) = {10**(r_db/10)/1e3:.1f} kbit/s")
    print("    Velocidad soportable segun la antena de la estacion (mismo satelite):")
    for nom, gtx in (("70 m (publicado)", gt), ("34 m escalada", g34 - db(t_op)), ("4 x 34 m escalado", g34 + db(4) - db(t_op))):
        c = eirp_sc - fspl + gtx - sum(perdidas.values()) - db(KB)
        print(f"      {nom:20s} C/N0 = {c:6.2f} dB-Hz ; R = {10**((c-req)/10)/1e3:8.1f} kbit/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
