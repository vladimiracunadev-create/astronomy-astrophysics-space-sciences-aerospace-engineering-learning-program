#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C27: deteccion de cambios en series de imagenes: diferencia con umbral y quiebre en una serie temporal.

Datos: SINTETICOS. Dos imagenes de 200 x 200 pixeles con ruido gaussiano de 0.02 en cada una y un parche de 20 x 20 pixeles con un cambio de +0.15.
Serie temporal de un pixel: 8 anios de datos cada 16 dias, ciclo anual de amplitud 0.2 sobre 0.5, ruido de 0.03, y un quiebre de -0.25 desde el anio 6 (sintetico). Semilla 57.
Modelo: diferencia d = I2 - I1 con sigma_d = sqrt(2) sigma ; umbral k sigma_d ; probabilidad de falsa alarma por pixel = 2 (1 - Phi(k)) ; deteccion de un cambio D:
1 - Phi(k - D/sigma_d) (aprox.); serie: ajuste armonico a los primeros 3 anios, residuos estandarizados, alarma si 3 consecutivos superan 3 sigma.
Validez: ruido gaussiano independiente; sin registro defectuoso ni atmosfera. Tolerancia: falsa alarma simulada frente a la analitica < 10 % relativo (k = 3);
la deteccion en la serie debe ocurrir despues del quiebre y antes de 3 meses.
Requiere numpy.
"""
import math, platform
import numpy as np

N, SIG, D = 200, 0.02, 0.15


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def calcular():
    r = {}
    rng = np.random.default_rng(57)
    sd = math.sqrt(2) * SIG
    I1 = 0.4 + SIG * rng.standard_normal((N, N))
    I2 = 0.4 + SIG * rng.standard_normal((N, N))
    I2[90:110, 90:110] += D
    d = I2 - I1
    for k in (2, 3):
        mask = np.abs(d) > k * sd
        fuera = mask.copy(); fuera[90:110, 90:110] = False
        dentro = mask[90:110, 90:110]
        r[f"fa_sim_{k}"] = float(fuera.sum() / (N * N - 400))
        r[f"fa_teo_{k}"] = 2 * (1 - phi(k))
        r[f"det_sim_{k}"] = float(dentro.mean())
        r[f"det_teo_{k}"] = 1 - phi(k - D / sd) + phi(-k - D / sd)
    # serie temporal
    t = np.arange(0, 8, 16 / 365.25)
    y = 0.5 + 0.2 * np.sin(2 * math.pi * t) + 0.03 * rng.standard_normal(t.size)
    y[t >= 6.0] -= 0.25
    ent = t < 3
    A = np.column_stack([np.ones_like(t), np.sin(2 * math.pi * t), np.cos(2 * math.pi * t)])
    c = np.linalg.lstsq(A[ent], y[ent], rcond=None)[0]
    res = y - A @ c
    s = res[ent].std(ddof=3)
    z = res / s
    alarma = None
    for i in range(len(t) - 2):
        if t[i] > 3 and all(abs(z[i + j]) > 3 for j in range(3)):
            alarma = t[i + 2]
            break
    r["s_serie"] = float(s)
    r["alarma_t"] = float(alarma) if alarma is not None else float("nan")
    r["retraso_meses"] = (r["alarma_t"] - 6.0) * 12
    falsas = 0
    for i in range(len(t) - 2):
        if 3 < t[i] < 5.9 and all(abs(z[i + j]) > 3 for j in range(3)):
            falsas += 1
    r["falsas_serie"] = falsas
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    for k in (2, 3):
        print(f"k = {k}: falsa alarma simulada = {r[f'fa_sim_{k}']*100:.3f} % ; analitica = {r[f'fa_teo_{k}']*100:.3f} % ; deteccion del cambio de +0.15: simulada = {r[f'det_sim_{k}']*100:.1f} % ; analitica = {r[f'det_teo_{k}']*100:.1f} %")
    print(f"Serie: sigma de los residuos del ajuste de 3 anios = {r['s_serie']:.4f} ; alarma en t = {r['alarma_t']:.3f} anios (quiebre en 6.000) ; retraso = {r['retraso_meses']:.1f} meses ; falsas alarmas antes del quiebre = {r['falsas_serie']}")
    assert abs(r["fa_sim_3"] / r["fa_teo_3"] - 1) < 0.25
    assert abs(r["fa_sim_2"] / r["fa_teo_2"] - 1) < 0.10
    assert 6.0 <= r["alarma_t"] < 6.25
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
