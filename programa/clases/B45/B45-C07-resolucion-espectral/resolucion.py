#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C07: perfil instrumental gaussiano, R, doblete y conservacion del ancho equivalente.

Datos: c = 299792458 m/s (NIST CODATA 2022, exacta, consultada el 2026-11-09). El doblete de 589,0 y 589,6 nm es SINTETICO e ILUSTRATIVO (lineas de absorcion gaussianas de profundidad 0,5
y ancho intrinseco despreciable); no se consultaron longitudes de onda de laboratorio. Semilla 20261109.
Modelo: FWHM = lambda/R = sqrt(8 ln 2) sigma; valle = profundidad en el punto medio dividida por la profundidad en el centro de una linea (menor que 1 si hay valle); sigma por momentos con peso signado en una ventana de 4 sigma, con ruido.
Supuestos: perfil instrumental gaussiano e invariante; muestreo de 0,02 nm. Validez: un perfil real tiene alas y varia con la longitud de onda.
Tolerancia: valle frente a la formula analitica a 1e-3; ancho equivalente conservado a 1e-3; sigma recuperada con ruido dentro de 3 errores estandar.
"""
from __future__ import annotations
import math, platform, random, sys

C_KMS = 299792.458
K = math.sqrt(8 * math.log(2))
SEMILLA = 20261109


def valle_analitico(sep, sigma):
    return 2 * math.exp(-(sep / 2) ** 2 / (2 * sigma ** 2)) / (1 + math.exp(-sep ** 2 / (2 * sigma ** 2)))


def perfil_doblete(R, lam1=589.0, lam2=589.6, paso=0.02):
    """Espectro normalizado 1 - 0,5 G1 - 0,5 G2 con G de area unidad en pico 1 (pico = 1)."""
    lam_c = 0.5 * (lam1 + lam2)
    sig = lam_c / R / K
    xs = [lam1 - 6 + i * paso for i in range(int((lam2 - lam1 + 12) / paso) + 1)]
    f = [1 - 0.5 * math.exp(-0.5 * ((x - lam1) / sig) ** 2) - 0.5 * math.exp(-0.5 * ((x - lam2) / sig) ** 2) for x in xs]
    return xs, f, sig


def calcular():
    r = {}
    lam = 589.3
    r["filas"] = []
    for R in (500, 1000, 1500, 3000, 10000):
        xs, f, sig = perfil_doblete(R)
        # punto medio
        i_med = min(range(len(xs)), key=lambda i: abs(xs[i] - 589.3))
        prof_med = 1 - f[i_med]
        i_l1 = min(range(len(xs)), key=lambda i: abs(xs[i] - 589.0))
        prof_pico = 1 - f[i_l1]
        r["filas"].append((R, lam / R, sig, prof_med / prof_pico, valle_analitico(0.6, sig), C_KMS / R))
    # ancho equivalente conservado bajo convolucion (linea de EW 0,05 nm y profundidad variable)
    ew_int = 0.05
    for R in (1000, 10000):
        sig = 589.3 / R / K
        # linea intrinseca delta: tras convolucion gaussiana de area ew_int
        paso = 0.002
        xs = [589.3 - 8 * sig + i * paso for i in range(int(16 * sig / paso) + 1)]
        ew_num = sum(ew_int / (sig * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - 589.3) / sig) ** 2) * paso for x in xs)
        r[f"ew_{R}"] = ew_num
    # recuperar sigma de una linea con ruido por momentos (S/N 50 en el continuo)
    rnd = random.Random(SEMILLA)
    R = 3000
    sig = 589.3 / R / K
    paso = 0.01
    xs = [589.3 + (i - 33) * paso for i in range(67)]
    estim = []
    for _ in range(300):
        d = [0.5 * math.exp(-0.5 * ((x - 589.3) / sig) ** 2) + rnd.gauss(0, 1 / 50) for x in xs]
        w = d
        s0 = sum(w)
        mu = sum(x * v for x, v in zip(xs, w)) / s0
        var = sum(v * (x - mu) ** 2 for x, v in zip(xs, w)) / s0
        estim.append(math.sqrt(var))
    m = sum(estim) / len(estim)
    sd = math.sqrt(sum((e - m) ** 2 for e in estim) / (len(estim) - 1))
    r["sig_true"] = sig
    r["sig_med"] = m
    r["sig_sd"] = sd
    r["sig_err"] = sd / math.sqrt(len(estim))
    r["R_req"] = 589.3 / 0.6
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'R':>6} {'FWHM (nm)':>10} {'sigma (nm)':>11} {'valle/linea num':>15} {'analitico':>10} {'dv (km/s)':>10}")
    for R, fw, sg, vn, va, dv in r["filas"]:
        print(f"{R:6d} {fw:10.4f} {sg:11.5f} {vn:15.4f} {va:10.4f} {dv:10.2f}")
    print(f"R minimo para separar el doblete (R = lambda/delta lambda) = {r['R_req']:.0f}")
    print(f"ancho equivalente tras convolucion (EW intrinseco 0,05 nm): R=1000 {r['ew_1000']:.5f} ; R=10000 {r['ew_10000']:.5f}")
    print(f"sigma verdadera {r['sig_true']:.5f} nm ; media por momentos {r['sig_med']:.5f} nm ; dispersion {r['sig_sd']:.5f} ; error estandar de la media {r['sig_err']:.5f}")
    for R, fw, sg, vn, va, dv in r["filas"]:
        assert abs(vn - va) < 2e-3, (R, vn, va)
    assert abs(r["ew_1000"] / 0.05 - 1) < 1e-3 and abs(r["ew_10000"] / 0.05 - 1) < 1e-3
    assert abs(r["sig_med"] - r["sig_true"]) < 0.2 * r["sig_true"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
