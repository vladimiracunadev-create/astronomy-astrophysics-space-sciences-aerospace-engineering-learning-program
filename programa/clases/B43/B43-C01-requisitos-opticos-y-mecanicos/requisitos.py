#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C01: de la apertura y la tolerancia optica a un cuaderno de requisitos.

Datos: ILUSTRATIVOS todos los parametros del telescopio (D = 200 mm, f/5, lambda = 550 nm, pixel de 3,76 um, seeing de 2 segundos de arco, presupuesto de errores en nm).
No se usan datos de un instrumento real ni constantes externas (1 rad = 206264,806 segundos de arco, definicion).
Modelo: radio de Airy 1,22 lambda/D; limite de Dawes 116/D(mm) segundos de arco (formula empirica); escala de placa 206264,806/F; muestreo de Nyquist lambda N/2.
Strehl de Marechal S = exp(-(2 pi sigma/lambda)^2) frente al calculo numerico de la intensidad central sobre una pupila circular con aberracion esferica primaria (suma sobre una malla 301 x 301).
Supuestos: aberracion pequena, pupila sin obstruccion, monocromatico. Validez: sigma <~ lambda/10.
Tolerancia: Strehl numerico frente a Marechal, 0,02 en valor absoluto; RSS frente a Monte Carlo (semilla 20261109, 200000 muestras), 0,5 % relativo.
"""
from __future__ import annotations
import math, platform, random, sys

D = 0.200; N = 5.0; LAM = 550e-9; PIX = 3.76e-6; SEEING = 2.0
RAD = 206264.806

def strehl_num(sigma_waves, n=301):
    # Z(4,0) normalizado: c*sqrt(5)*(6 r^4 - 6 r^2 + 1) tiene RMS = c
    vals = []
    h = 2.0 / (n - 1)
    sr = si = 0.0; cnt = 0
    for i in range(n):
        x = -1 + i * h
        for j in range(n):
            y = -1 + j * h
            r2 = x * x + y * y
            if r2 <= 1.0:
                w = sigma_waves * math.sqrt(5) * (6 * r2 * r2 - 6 * r2 + 1)
                vals.append(w)
                sr += math.cos(2 * math.pi * w); si += math.sin(2 * math.pi * w); cnt += 1
    mean = sum(vals) / cnt
    rms = math.sqrt(sum((v - mean) ** 2 for v in vals) / cnt)
    pv = max(vals) - min(vals)
    return (sr * sr + si * si) / cnt ** 2, rms, pv

def calc():
    F = D * N
    r = {}
    r["F_mm"] = F * 1e3
    r["airy_arcsec"] = 1.22 * LAM / D * RAD
    r["dawes_arcsec"] = 116.0 / (D * 1e3)
    r["escala_arcsec_mm"] = RAD / (F * 1e3)
    r["pix_arcsec"] = PIX * RAD / F
    r["nyq_um"] = LAM * N / 2 * 1e6
    r["pix_seeing_um"] = SEEING / 2 / RAD * F * 1e6
    s_m = math.exp(-(2 * math.pi / 14) ** 2)
    s_n, rms, pv = strehl_num(1 / 14)
    r["strehl_marechal"] = s_m; r["strehl_num"] = s_n; r["rms_waves"] = rms; r["pv_waves"] = pv; r["pv_sobre_rms"] = pv / rms
    r["sup_rms_nm"] = LAM / 28 * 1e9
    budget = {"figura": 20.0, "soporte": 15.0, "termico": 10.0, "colimacion": 12.0, "montaje": 8.0}
    rss = math.sqrt(sum(v * v for v in budget.values()))
    rng = random.Random(20261109)
    acc = 0.0; n = 200000
    for _ in range(n):
        acc += sum((rng.gauss(0, v)) ** 2 for v in budget.values())
    mc = math.sqrt(acc / n)
    r["rss_nm"] = rss; r["mc_nm"] = mc
    r["strehl_presupuesto"] = math.exp(-(2 * math.pi * rss / (LAM * 1e9)) ** 2)
    r["budget"] = budget
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        if k != "budget":
            print(f"{k} = {v:.6g}")
    assert abs(r["airy_arcsec"] - 0.6918) < 1e-3
    assert abs(r["strehl_num"] - r["strehl_marechal"]) < 0.02
    assert abs(r["rms_waves"] - 1 / 14) < 1e-3
    assert abs(r["mc_nm"] - r["rss_nm"]) / r["rss_nm"] < 0.005
    assert r["strehl_presupuesto"] > 0.8
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
