#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C21: transformacion al sistema estandar con estrellas estandar sinteticas (punto cero y termino de color).

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): 30 estandares con V entre 11 y 15 y B-V entre -0,2 y 1,6; el instrumento obedece v = V + zp + c (B-V) con zp = -3,200 y c = +0,045 mag y
ruido de 0,015 mag por estrella; dos estandares reciben un valor atipico de 0,25 mag. No son estandares de Landolt ni de ningun catalogo. La conversion AB/Jy (3631 Jy para m_AB = 0) es conocimiento de libro NO consultado.
Modelo: minimos cuadrados lineales de v - V = zp + c (B-V) (ecuaciones normales 2x2); covarianza sigma^2 (A^T A)^-1; rechazo iterativo a 3 sigma; comparacion con la covarianza por Monte Carlo.
Supuestos: ruido gaussiano independiente, sin dependencia de la masa de aire (ya corregida), termino de color lineal. Validez: no incluye terminos de segundo orden ni la zona de saturacion.
Tolerancia: parametros ajustados dentro de 3 errores formales de los verdaderos; dispersion Monte Carlo frente al error formal a 10 %; los atipicos se detectan.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
ZP, CC, SIG = -3.200, 0.045, 0.015


def ajustar(col, y, mascara=None):
    idx = [i for i in range(len(y)) if mascara is None or mascara[i]]
    n = len(idx)
    sx = sum(col[i] for i in idx)
    sxx = sum(col[i] ** 2 for i in idx)
    sy = sum(y[i] for i in idx)
    sxy = sum(col[i] * y[i] for i in idx)
    det = n * sxx - sx * sx
    zp = (sxx * sy - sx * sxy) / det
    c = (n * sxy - sx * sy) / det
    res = [y[i] - zp - c * col[i] for i in idx]
    return zp, c, res, (sxx / det, -sx / det, n / det), n


def calcular():
    rnd = random.Random(SEMILLA)
    N = 30
    V = [rnd.uniform(11, 15) for _ in range(N)]
    bv = [rnd.uniform(-0.2, 1.6) for _ in range(N)]
    y = [ZP + CC * b + rnd.gauss(0, SIG) for b in bv]
    r = {"N": N}
    zp, c, res, (a00, a01, a11), n = ajustar(bv, y)
    r["limpio"] = (zp, c, math.sqrt(a00) * SIG, math.sqrt(a11) * SIG, math.sqrt(sum(x * x for x in res) / (n - 2)))
    # atipicos
    y2 = y[:]
    y2[3] += 0.25
    y2[17] -= 0.25
    zp2, c2, res2, cov2, n2 = ajustar(bv, y2)
    r["sucio"] = (zp2, c2)
    mask = [True] * N
    for _ in range(5):
        zp3, c3, res3, cov3, n3 = ajustar(bv, y2, mask)
        s = math.sqrt(sum(x * x for x in res3) / (n3 - 2))
        mask = [abs(y2[i] - zp3 - c3 * bv[i]) < 3 * s for i in range(N)]
    r["recortado"] = (zp3, c3, N - sum(mask), [i for i in range(N) if not mask[i]], s)
    # objetivo: instrumental v = 17,654 con B-V = 0,80 -> V
    v_obj, bv_obj = 17.654, 0.80
    r["V_obj"] = v_obj - zp - c * bv_obj
    r["V_obj_sin_color"] = v_obj - zp
    var_pred = SIG ** 2 * (a00 + 2 * a01 * bv_obj + a11 * bv_obj ** 2)
    r["sig_V_pred"] = math.sqrt(var_pred + SIG ** 2)
    # Monte Carlo de la covarianza
    zps, cs = [], []
    for _ in range(3000):
        yy = [ZP + CC * b + rnd.gauss(0, SIG) for b in bv]
        z_, c_, _, _, _ = ajustar(bv, yy)
        zps.append(z_)
        cs.append(c_)
    def sd(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)), m
    r["mc_zp"] = sd(zps)
    r["mc_c"] = sd(cs)
    r["formal_zp"] = math.sqrt(a00) * SIG
    r["formal_c"] = math.sqrt(a11) * SIG
    r["corr"] = a01 / math.sqrt(a00 * a11)
    r["bv_media"] = sum(bv) / N
    # conversion: m_AB = -2,5 log10(f_nu / 3631 Jy)
    r["jy_ab"] = [(jy, -2.5 * math.log10(jy / 3631.0)) for jy in (3631.0, 363.1, 1.0, 0.001)]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    zp, c, ezp, ec, rms = r["limpio"]
    print(f"{r['N']} estandares: zp = {zp:.4f} +- {ezp:.4f} (verdadero {ZP}) ; c = {c:.4f} +- {ec:.4f} (verdadero {CC}) ; RMS de los residuos = {rms:.4f} mag ; correlacion zp-c = {r['corr']:.3f}")
    print(f"con dos atipicos de +-0,25: zp = {r['sucio'][0]:.4f}, c = {r['sucio'][1]:.4f}")
    zp3, c3, nrej, quienes, s = r["recortado"]
    print(f"recorte a 3 sigma: descarta {nrej} estrellas {quienes} ; zp = {zp3:.4f}, c = {c3:.4f}, sigma residual {s:.4f}")
    print(f"objetivo v = 17,654 con B-V = 0,80: V = {r['V_obj']:.3f} (sin termino de color {r['V_obj_sin_color']:.3f}) ; error previsto = {r['sig_V_pred']:.4f} mag")
    print(f"Monte Carlo (3000 repeticiones): sigma_zp = {r['mc_zp'][0]:.4f} (formal {r['formal_zp']:.4f}) ; sigma_c = {r['mc_c'][0]:.4f} (formal {r['formal_c']:.4f})")
    print("m_AB = -2,5 log10(f/3631 Jy):", ", ".join(f"{jy:g} Jy -> {m:.3f}" for jy, m in r["jy_ab"]))
    assert abs(zp - ZP) < 3 * ezp and abs(c - CC) < 3 * ec
    assert abs(r["mc_zp"][0] / r["formal_zp"] - 1) < 0.10 and abs(r["mc_c"][0] / r["formal_c"] - 1) < 0.10
    assert set(quienes) == {3, 17}
    assert abs(zp3 - ZP) < 3 * ezp * 1.2
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
