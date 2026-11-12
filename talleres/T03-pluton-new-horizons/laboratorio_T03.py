# SPDX-License-Identifier: Apache-2.0
"""Laboratorio del taller T03 (Plutón, New Horizons).

Secciones: 1 lanzamiento rápido · 2 tiempo de vuelo con y sin Júpiter · 3 sobrevuelo y resolución · 4 enlace y datos ·
5 generador de radioisótopos · 6 hibernación y fiabilidad · 7 costo.

UNIDADES: km, s, kg, W; UA para distancias heliocéntricas; costos en MUSD.
SISTEMA DE REFERENCIA: heliocéntrico (aproximación radial: se ignora el momento angular); geocéntrico en el lanzamiento.
MODELO: conservación de la energía en el campo del Sol, con un impulso instantáneo en Júpiter. TOLERANCIA: ±30 % en el
tiempo de vuelo (el modelo radial es grosero y subestima el viaje a Júpiter); los demás cálculos, ±5 %. No sirve para diseñar una trayectoria de vuelo.
DATOS: constantes NASA/JPL redondeadas; cifras de la misión de referencia pública, redondeadas (⚠ verificar).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_comun"))
from comun_taller import *  # noqa: E402,F403

C3 = 157.6            # km^2/s^2, referencia pública (⚠)
D_PLUTON_UA = 31.9    # UA al momento del sobrevuelo
D_PLUTON_KM = 4.77e9  # km


def lanzamiento(alt_km: float = 200.0) -> dict:
    r = R_TIERRA + alt_km
    v_inf = math.sqrt(C3)
    v_quema = math.sqrt(C3 + 2 * MU_TIERRA / r)
    v_helio = circular(MU_SOL, UA) + v_inf   # sale en la dirección del movimiento de la Tierra
    v_escape_sol = math.sqrt(2 * MU_SOL / UA)
    exceso = v_helio**2 - v_escape_sol**2
    return {"v_inf": v_inf, "v_quema": v_quema, "v_helio": v_helio, "v_escape_sol": v_escape_sol, "exceso": exceso,
            "dv_leo": v_quema - circular(MU_TIERRA, r)}


def tiempo_de_vuelo(exceso: float, r0_ua: float, r1_ua: float, dv_jupiter: float = 0.0, rj_ua: float = 5.2, n: int = 20000) -> float:
    """Años de vuelo en línea recta con energía conservada y un impulso dv_jupiter (km/s) en rj_ua."""
    r0, r1, rj = r0_ua * UA, r1_ua * UA, rj_ua * UA
    energia = exceso / 2
    t = 0.0
    dr = (r1 - r0) / n
    for i in range(n):
        r = r0 + (i + 0.5) * dr
        if dv_jupiter and r >= rj and energia == exceso / 2:
            v = math.sqrt(2 * (energia + MU_SOL / rj)) + dv_jupiter
            energia = v**2 / 2 - MU_SOL / rj
        v = math.sqrt(2 * (energia + MU_SOL / r))
        t += dr / v
    return t / (365.25 * 86400)


def perfil_velocidad(exceso: float, dv_jupiter: float, hasta_ua: float = 35.0) -> list[tuple[float, float]]:
    pts = []
    energia = exceso / 2
    cambiado = False
    for k in range(20, int(hasta_ua * 10) + 1, 5):
        r_ua = k / 10
        if dv_jupiter and r_ua >= 5.2 and not cambiado:
            v = math.sqrt(2 * (energia + MU_SOL / (5.2 * UA))) + dv_jupiter
            energia = v**2 / 2 - MU_SOL / (5.2 * UA)
            cambiado = True
        pts.append((r_ua, math.sqrt(2 * (energia + MU_SOL / (r_ua * UA)))))
    return pts


def sobrevuelo(d_min_km: float = 12500.0, v_rel: float = 13.8) -> dict:
    ifov = 4.95e-6  # rad por píxel de la cámara de alta resolución (⚠)
    return {"escala_m_px": d_min_km * 1000 * ifov, "tasa_giro_rad_s": v_rel / d_min_km,
            "tasa_giro_grados_s": math.degrees(v_rel / d_min_km), "tiempo_a_1_rp_h": d_min_km * 10 / v_rel / 3600,
            "borroneo_m": v_rel * 1000 * 0.05}


def datos(bits: float = 50e9, velocidad_bps: float = 1000.0) -> dict:
    return {"dias": bits / velocidad_bps / 86400, "luz_h": D_PLUTON_KM / C_LUZ / 3600}


def enlace() -> dict:
    # La potencia recibida cae como 1/d^2: comparación respecto a 5 UA (Júpiter)
    return {"factor": (D_PLUTON_UA / 5.0) ** 2}


def mmrtg_pluton(anios: float) -> float:
    return rtg(245.7, anios, degradacion_anual=0.0127)


def hibernacion(dias: float = 1873.0, p_ciclo: float = 0.9995, ciclos: int = 18) -> float:
    return p_ciclo ** ciclos


def main() -> None:
    print("TALLER T03 - Plutón (New Horizons): laboratorio de diseño preliminar\n")
    l = lanzamiento()
    print("1. LANZAMIENTO RÁPIDO (C3 ≈ 157,6 km²/s²)")
    print(f"   v∞ de salida de la Tierra : {l['v_inf']:.2f} km/s")
    print(f"   velocidad al final de la quema (200 km): {l['v_quema']:.2f} km/s  (la real fue ≈ 16 km/s)")
    print(f"   delta-v desde LEO         : {l['dv_leo']:.2f} km/s")
    print(f"   velocidad heliocéntrica   : {l['v_helio']:.2f} km/s  (escape del Sol a 1 UA: {l['v_escape_sol']:.2f} km/s)")
    print(f"   exceso hiperbólico (v∞ al Sol)²: {l['exceso']:.1f} km²/s²")
    h = hohmann(UA, 39.5 * UA)
    print(f"   (Hohmann Tierra-Plutón: {h['t_vuelo_s'] / 86400 / 365.25:.1f} años: por eso hace falta lanzar tan rápido)")
    print("\n2. TIEMPO DE VUELO (aproximación radial, ±30 %)")
    t_j = tiempo_de_vuelo(l["exceso"], 1.0, 5.2)
    t0 = tiempo_de_vuelo(l["exceso"], 1.0, D_PLUTON_UA)
    t4 = tiempo_de_vuelo(l["exceso"], 1.0, D_PLUTON_UA, dv_jupiter=4.0)
    print(f"   hasta Júpiter (5,2 UA)     : {t_j:.2f} años  (la misión real tardó ≈ 1,1 años)")
    print(f"   hasta Plutón sin Júpiter   : {t0:.1f} años")
    print(f"   hasta Plutón con +4 km/s   : {t4:.1f} años  (real: ≈ 9,5 años)")
    print(f"   ahorro por la asistencia   : {t0 - t4:.1f} años  (la misión reporta ≈ 3 años)")
    s = sobrevuelo()
    print("\n3. SOBREVUELO a 12.500 km y 13,8 km/s")
    print(f"   escala de la cámara        : {s['escala_m_px']:.0f} m/píxel")
    print(f"   velocidad de giro necesaria: {s['tasa_giro_grados_s']:.3f} °/s para seguir el blanco")
    print(f"   desplazamiento en 0,05 s   : {s['borroneo_m']:.0f} m (sin seguimiento, la imagen saldría borrosa)")
    d = datos()
    print("\n4. ENLACE Y DATOS")
    print(f"   retardo de luz Tierra-Plutón: {d['luz_h']:.2f} horas en un sentido")
    print(f"   volumen guardado ≈ 50 Gbit a 1 kbit/s: {d['dias']:.0f} días de transmisión")
    print(f"   la señal es {enlace()['factor']:.0f} veces más débil que a 5 UA (ley 1/d²)")
    print("\n5. GENERADOR DE RADIOISÓTOPOS (245,7 W al lanzamiento, degradación ≈ 1,27 % anual + decaimiento del Pu-238)")
    for a in (0, 5, 9.5, 14, 20):
        print(f"   año {a:>4}: {mmrtg_pluton(a):6.1f} W")
    print("\n6. HIBERNACIÓN: 18 ciclos de encendido y apagado con 0,9995 de éxito cada uno")
    print(f"   probabilidad de que todos salgan bien: {hibernacion():.4f}")
    print("\n7. COSTO (referencia pública ≈ 700 MUSD hasta el sobrevuelo, incluye lanzamiento y operaciones; ⚠ verificar)")
    print(f"   ≈ {700 / 9.5:.0f} MUSD por año de vuelo")


if __name__ == "__main__":
    main()
