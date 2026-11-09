#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C10: series del hidrogeno con la constante de Rydberg y precision del centroide de una linea.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): R_inf = 10 973 731,568157 1/m, m_e = 9,1093837139e-31 kg, m_p = 1,67262192595e-27 kg, m_d = 3,3435837768e-27 kg.
El indice del aire (formula de Birch-Downs/Edlen) es conocimiento de libro NO consultado; los valores de laboratorio de las lineas (p. ej. H alfa en aire cerca de 656,28 nm) tampoco se consultaron.
La linea sintetica (sigma 0,08 nm, 4000 fotones, pixel de 0,02 nm) es ILUSTRATIVA; semilla 20261109.
Modelo: 1/lambda_vacio = R_M (1/n1^2 - 1/n2^2), R_M = R_inf/(1 + m_e/M); centroide por promedio ponderado en una ventana de 4 sigma; error previsto sigma/sqrt(N).
Supuestos: hidrogeno no relativista sin estructura fina; ruido de fotones. Validez: la estructura fina ensancha H alfa en una fraccion pequena de pm.
Tolerancia: H alfa en aire dentro de 0,02 nm de 656,28; dispersion del centroide por Monte Carlo frente a sigma/sqrt(N) a 10 %.
"""
from __future__ import annotations
import math, platform, random, sys

RINF = 10973731.568157
ME = 9.1093837139e-31
MP = 1.67262192595e-27
MD = 3.3435837768e-27
SEMILLA = 20261109


def lam_vac_nm(n1, n2, M):
    rm = RINF / (1 + ME / M)
    return 1e9 / (rm * (1 / n1 ** 2 - 1 / n2 ** 2))


def n_aire(lam_nm):
    s2 = (1000.0 / lam_nm) ** 2 * 1e-6
    return 1e-8 * (8342.13 + 2406030 / (130 - s2) + 15997 / (38.9 - s2))


def calcular():
    r = {}
    filas = []
    for nombre, n1, n2 in (("Ly alfa", 1, 2), ("Ly beta", 1, 3), ("H alfa", 2, 3), ("H beta", 2, 4), ("H gamma", 2, 5), ("H delta", 2, 6), ("Pa alfa", 3, 4), ("Br alfa", 4, 5)):
        lv = lam_vac_nm(n1, n2, MP)
        la = lv / (1 + n_aire(lv)) if lv > 200 else float("nan")
        filas.append((nombre, lv, la))
    r["filas"] = filas
    r["limite_balmer"] = 1e9 / (RINF / (1 + ME / MP) / 4)
    r["lim_lyman"] = 1e9 / (RINF / (1 + ME / MP))
    r["dh_dd"] = lam_vac_nm(2, 3, MP) - lam_vac_nm(2, 3, MD)
    r["razon_masa"] = 1 / (1 + ME / MP)
    # centroide con ruido de fotones
    rnd = random.Random(SEMILLA)
    sig, N, paso, lam0 = 0.08, 4000, 0.02, 656.0
    xs = [lam0 + (i - 10 * 0) * paso for i in range(-17, 18)]
    xs = [lam0 + k * paso for k in range(-int(4 * sig / paso), int(4 * sig / paso) + 1)]
    mu = [N * paso / (sig * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - lam0) / sig) ** 2) for x in xs]
    cen = []
    flujos = []
    for _ in range(2000):
        c = [max(0.0, rnd.gauss(m, math.sqrt(m))) for m in mu]
        s = sum(c)
        cen.append(sum(x * v for x, v in zip(xs, c)) / s)
        flujos.append(s)
    m = sum(cen) / len(cen)
    r["cen_media"] = m
    r["cen_sd"] = math.sqrt(sum((a - m) ** 2 for a in cen) / (len(cen) - 1))
    r["cen_pred"] = sig / math.sqrt(N)
    mf = sum(flujos) / len(flujos)
    r["flujo_media"] = mf
    r["flujo_sd"] = math.sqrt(sum((a - mf) ** 2 for a in flujos) / (len(flujos) - 1))
    r["ventana_n"] = len(xs)
    r["fwhm"] = sig * math.sqrt(8 * math.log(2))
    r["dv_cen"] = r["cen_sd"] / lam0 * 299792.458
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'linea':>8} {'vacio (nm)':>11} {'aire (nm)':>10}")
    for n, lv, la in r["filas"]:
        print(f"{n:>8} {lv:11.4f} {la:10.4f}")
    print(f"limite de Balmer = {r['limite_balmer']:.3f} nm ; limite de Lyman = {r['lim_lyman']:.3f} nm ; factor de masa reducida (H) = {r['razon_masa']:.8f}")
    print(f"desplazamiento H - D en H alfa = {r['dh_dd']:.4f} nm")
    print(f"centroide: media {r['cen_media']:.5f} nm ; dispersion MC {r['cen_sd']:.5f} nm ; sigma/sqrt(N) = {r['cen_pred']:.5f} nm ; equivale a {r['dv_cen']:.2f} km/s")
    print(f"flujo (cuentas): media {r['flujo_media']:.1f} ; dispersion {r['flujo_sd']:.1f} ; sqrt(N) = {math.sqrt(4000):.1f}")
    ha = dict((n, la) for n, lv, la in r["filas"])["H alfa"]
    assert abs(ha - 656.28) < 0.02
    assert abs(r["cen_sd"] / r["cen_pred"] - 1) < 0.10
    assert abs(r["cen_media"] - 656.0) < 3 * r["cen_sd"] / math.sqrt(2000)
    assert 0.17 < r["dh_dd"] < 0.19
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
