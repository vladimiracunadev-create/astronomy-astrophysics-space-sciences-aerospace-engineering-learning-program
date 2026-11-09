#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C09: respuesta instrumental con una estrella estandar sintetica y campo plano.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, c y k_B exactas. La respuesta (blaze sinc^2 por eficiencia cuantica lineal), la estrella estandar de cuerpo negro de 9000 K y el
blanco de 5000 K son SINTETICOS e ILUSTRATIVOS; los conteos llevan ruido de Poisson aproximado por una gaussiana (semilla 20261109). La ganancia por pixel (2 % RMS) es sintetica.
Modelo: S(l) = cuentas/flujo del estandar suavizada con media movil de 11 bins; el flujo del blanco es cuentas/S; el plano divide la ganancia por pixel.
Supuestos: respuesta estable, cuentas altas (aproximacion gaussiana del Poisson), sin fondo de cielo. Validez: la media movil introduce sesgo donde la respuesta cambia deprisa.
Tolerancia: el RMS del flujo recuperado esta dentro de 2 veces el valor predicho por propagacion de ruido; el plano reduce la dispersion de 2 % a un valor cercano al del ruido de Poisson (menos de 1 %).
"""
from __future__ import annotations
import math, platform, random, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
SEMILLA = 20261109
N = 300
LAM = [400e-9 + i * 1e-9 for i in range(N)]
VENTANA = 11


def planck_fotones(l, T):
    return 2 * C / l ** 4 / math.expm1(H * C / (l * KB * T))


def respuesta(l):
    x = (l - 550e-9) / 120e-9
    blaze = (math.sin(math.pi * x * 1.2) / (math.pi * x * 1.2)) ** 2 if abs(x) > 1e-9 else 1.0
    qe = 0.9 - 0.7 * (l - 400e-9) / 600e-9
    return 0.15 + 0.85 * blaze * qe


def media_movil(v, w):
    h = w // 2
    out = []
    for i in range(len(v)):
        a, b = max(0, i - h), min(len(v), i + h + 1)
        out.append(sum(v[a:b]) / (b - a))
    return out


def calcular():
    rnd = random.Random(SEMILLA)
    r = {}
    f_std = [planck_fotones(l, 9000.0) for l in LAM]
    f_tar = [planck_fotones(l, 5000.0) for l in LAM]
    n0 = 4e6 / max(f_std)                 # estandar: pico de 4e6 cuentas por bin con respuesta 1
    resp = [respuesta(l) for l in LAM]
    r["resp_pico"], r["resp_min"] = max(resp), min(resp)
    n_std_true = [n0 * f * s for f, s in zip(f_std, resp)]
    n0t = 1.0e6 / max(f_tar)              # blanco: 1e6 cuentas
    n_tar_true = [n0t * f * s for f, s in zip(f_tar, resp)]
    est = [rnd.gauss(m, math.sqrt(m)) for m in n_std_true]
    tar = [rnd.gauss(m, math.sqrt(m)) for m in n_tar_true]
    sens_bruta = [e / (n0 * f) for e, f in zip(est, f_std)]
    sens = media_movil(sens_bruta, VENTANA)
    flujo_rec = [t / s for t, s in zip(tar, sens)]
    rel = [(fr / (n0t * f) - 1) for fr, f in zip(flujo_rec, f_tar)]
    sin_cal = [t / (n0t * f) - 1 for t, f in zip(tar, f_tar)]
    r["rms_rel"] = math.sqrt(sum(a * a for a in rel[10:-10]) / len(rel[10:-10]))
    r["rms_sin_cal"] = math.sqrt(sum(a * a for a in sin_cal[10:-10]) / len(sin_cal[10:-10]))
    # prediccion: ruido del blanco 1/sqrt(Nt) combinado con el del estandar suavizado 1/sqrt(Ns*W)
    pred = []
    for i in range(10, N - 10):
        pred.append(1 / n_tar_true[i] + 1 / (n_std_true[i] * VENTANA))
    r["rms_pred"] = math.sqrt(sum(pred) / len(pred))
    r["resp_ratio"] = max(resp) / min(resp)
    # campo plano
    g = [1 + rnd.gauss(0, 0.02) for _ in range(2000)]
    plano = [rnd.gauss(1e5 * a, math.sqrt(1e5 * a)) for a in g]
    cien = [rnd.gauss(2e4 * a, math.sqrt(2e4 * a)) for a in g]
    pm = sum(plano) / len(plano)
    corr = [c / (p / pm) for c, p in zip(cien, plano)]
    def disp(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)) / m
    r["disp_antes"] = disp(cien)
    r["disp_despues"] = disp(corr)
    r["disp_pred"] = math.sqrt(1 / 2e4 + 1 / 1e5)
    r["disp_solo_ruido"] = 1 / math.sqrt(2e4)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"respuesta: maximo {r['resp_pico']:.3f}, minimo {r['resp_min']:.3f}, cociente {r['resp_ratio']:.1f}")
    print(f"flujo del blanco sin calibrar: RMS relativo = {r['rms_sin_cal']*100:.1f} % ; calibrado con el estandar: {r['rms_rel']*100:.3f} % ; predicho: {r['rms_pred']*100:.3f} %")
    print(f"campo plano (ganancia 2 % RMS, 2e4 cuentas): dispersion antes {r['disp_antes']*100:.3f} % ; despues {r['disp_despues']*100:.3f} % ; ruido de Poisson solo {r['disp_solo_ruido']*100:.3f} % ; prediccion con plano ruidoso {r['disp_pred']*100:.3f} %")
    assert r["rms_rel"] < 2 * r["rms_pred"]
    assert r["rms_sin_cal"] > 10 * r["rms_rel"]
    assert r["disp_despues"] < 0.01 and r["disp_antes"] > 0.02
    assert abs(r["disp_despues"] / r["disp_pred"] - 1) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
