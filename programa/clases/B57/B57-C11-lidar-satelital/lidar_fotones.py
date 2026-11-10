#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C11: LiDAR satelital de fotones: espaciado a lo largo de la traza y busqueda de la superficie.

Datos: tasa de 10 000 pulsos por segundo y 6 haces de ICESat-2 (pagina de NASA, consultada 2026-11-09; el resto de la pagina no traia otros datos).
ILUSTRATIVOS / SINTETICOS: altitud 500 km, GM = 3.986004418e14, R = 6378.137 km (referencia, no consultada), 3 fotones de senal por pulso en
el haz fuerte, dispersion de la superficie 0.15 m, 15 fotones de fondo por pulso repartidos en una ventana de 30 m, segmentos de 100 m.
Modelo: espaciado = v_suelo / tasa; en cada segmento se acumulan fotones, se busca la ventana de +-0.5 m con mas fotones y se toma la mediana.
Semilla fija 57, 200 segmentos por caso. Validez: superficie plana por segmento, sin pendiente ni nubes. Tolerancia: error rms < 3 cm con senal fuerte;
con senal debil (0.05 fotones por pulso) la fraccion de segmentos con error > 1 m debe ser > 10 %.
Requiere numpy.
"""
import math, platform
import numpy as np

GM, RT, H, TASA = 3.986004418e14, 6378137.0, 500e3, 10000.0
SIG, FONDO, VENT, SEG = 0.15, 15.0, 30.0, 100.0


def segmento(rng, lam_senal):
    v = math.sqrt(GM / (RT + H)) * RT / (RT + H)
    n = int(SEG / (v / TASA))
    z0 = rng.uniform(-5, 5)
    ns = rng.poisson(lam_senal * n)
    nb = rng.poisson(FONDO * n)
    z = np.concatenate([z0 + SIG * rng.standard_normal(ns), rng.uniform(-VENT / 2, VENT / 2, nb)])
    z.sort()
    # ventana de +-0.5 m con mas fotones (barrido con searchsorted)
    lo = np.searchsorted(z, z - 0.5)
    hi = np.searchsorted(z, z + 0.5)
    k = int(np.argmax(hi - lo))
    est = float(np.median(z[lo[k]:hi[k]]))
    return est - z0, n


def caso(lam, rng, ens=200):
    e = np.array([segmento(rng, lam)[0] for _ in range(ens)])
    return float(np.sqrt(np.mean(e**2))), float(np.mean(np.abs(e) > 1.0))


def calcular():
    r = {}
    v = math.sqrt(GM / (RT + H)) * RT / (RT + H)
    r["v_suelo"] = v / 1e3
    r["espaciado"] = v / TASA
    r["n_pulsos"] = int(SEG / r["espaciado"])
    rng = np.random.default_rng(57)
    r["rms_fuerte"], r["frac_fuerte"] = caso(3.0, rng)
    r["rms_debil"], r["frac_debil"] = caso(0.05, rng)
    r["rms_fuerte_cm"], r["rms_debil_cm"] = r["rms_fuerte"] * 100, r["rms_debil"] * 100
    r["frac_fuerte_pct"], r["frac_debil_pct"] = r["frac_fuerte"] * 100, r["frac_debil"] * 100
    r["fotones_senal"] = 3.0 * r["n_pulsos"]
    r["fotones_fondo_por_m"] = FONDO * r["n_pulsos"] / VENT
    r["esperado_cm"] = SIG / math.sqrt(3.0 * r["n_pulsos"]) * 100
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Velocidad sobre el suelo = {r['v_suelo']:.3f} km/s ; espaciado entre pulsos a 10 kHz = {r['espaciado']:.3f} m ; pulsos por segmento de 100 m = {r['n_pulsos']}")
    print(f"Fotones de senal por segmento = {r['fotones_senal']:.0f} ; fondo = {r['fotones_fondo_por_m']:.1f} fotones por metro de altura")
    print(f"Error estadistico esperado sigma/sqrt(N) = {r['esperado_cm']:.2f} cm")
    print(f"Senal fuerte: error rms = {r['rms_fuerte']*100:.2f} cm ; segmentos con error > 1 m = {r['frac_fuerte']*100:.1f} %")
    print(f"Senal debil : error rms = {r['rms_debil']*100:.1f} cm ; segmentos con error > 1 m = {r['frac_debil']*100:.1f} %")
    assert r["rms_fuerte"] < 0.03
    assert r["frac_debil"] > 0.10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
