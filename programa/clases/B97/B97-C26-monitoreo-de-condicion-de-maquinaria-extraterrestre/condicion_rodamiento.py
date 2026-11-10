#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C26: indicadores de condicion (RMS y curtosis) de un rodamiento sintetico y proyeccion de vida util restante por regresion.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): ruido gaussiano de desviacion 1.0 (unidades arbitrarias), 2048 muestras por ventana, una ventana por dia durante 140 dias,
falla incipiente desde el dia 40 con impulsos periodicos (cada 64 muestras, decaimiento de 4 muestras) de amplitud A(d) = 0.08 exp((d - 40)/14), umbrales ilustrativos de RMS 1.5
y de curtosis 3.6, semilla fija. Ningun dato corresponde a un rodamiento ni a una maquina reales; los umbrales no provienen de ninguna norma (no consultadas).
Modelo: HI(d) = RMS de la ventana; potencia en exceso E(d) = RMS^2 - 1 crece como A^2 (exponencial); la regresion lineal de ln E sobre los ultimos 20 dias hasta el dia de prediccion (96)
se extrapola hasta E = 1.5^2 - 1 = 1.25 (cruce del umbral); vida util restante = dia de cruce - dia de prediccion.
Segunda via: pruebas de los indicadores con casos analiticos (RMS de una senoidal = A/sqrt(2); curtosis de una senoidal = 1.5; curtosis gaussiana ~ 3) y el cruce de referencia
calculado de forma determinista con la potencia esperada (tolerancia de 5 dias en el dia de cruce proyectado frente al de referencia).
Unidades arbitrarias de vibracion y dias. Sin dependencia de la carga, la velocidad ni la temperatura.
"""
from __future__ import annotations
import math, platform, random

SIGMA, NV, NDIAS, D0, T_E, PER, DEC = 1.0, 2048, 140, 40, 14.0, 64, 4                  # SINTETICOS
UMB_RMS, UMB_KURT, DIA_PRED, VENT, SEMILLA = 1.5, 3.6, 96, 20, 20261110


def rms(x):
    return math.sqrt(sum(v * v for v in x) / len(x))


def curtosis(x):
    n = len(x)
    m = sum(x) / n
    m2 = sum((v - m) ** 2 for v in x) / n
    m4 = sum((v - m) ** 4 for v in x) / n
    return m4 / (m2 * m2)


def amplitud(d):
    return 0.08 * math.exp((d - D0) / T_E) if d >= D0 else 0.0


def ventana(rng, d):
    x = [rng.gauss(0, SIGMA) for _ in range(NV)]
    a = amplitud(d)
    if a > 0:
        for i in range(0, NV - DEC, PER):
            for k in range(DEC):
                x[i + k] += a * math.exp(-k)
    return x


def exceso_esperado(d):
    a = amplitud(d)
    pot = sum(math.exp(-2 * k) for k in range(DEC)) * a * a * len(range(0, NV - DEC, PER)) / NV
    return pot


def regresion(xs, ys, ws):
    sw = sum(ws)
    mx = sum(w * x for w, x in zip(ws, xs)) / sw
    my = sum(w * y for w, y in zip(ws, ys)) / sw
    b = sum(w * (x - mx) * (y - my) for w, x, y in zip(ws, xs, ys)) / sum(w * (x - mx) ** 2 for w, x in zip(ws, xs))
    return b, my - b * mx


def calc():
    rng = random.Random(SEMILLA)
    hi, ku = [], []
    for d in range(NDIAS):
        w = ventana(rng, d)
        hi.append(rms(w)); ku.append(curtosis(w))
    dia_rms = next((d for d, v in enumerate(hi) if d >= D0 and v > UMB_RMS), None)
    dia_ku = next((d for d, v in enumerate(ku) if d >= D0 and v > UMB_KURT), None)
    # regresion sobre ln del exceso de potencia en los ultimos VENT dias hasta DIA_PRED
    dias = list(range(DIA_PRED - VENT + 1, DIA_PRED + 1))
    exc = [max(hi[d] ** 2 - SIGMA ** 2, 1e-6) for d in dias]
    b, a = regresion(dias, [math.log(e) for e in exc], [e * e for e in exc])
    objetivo = UMB_RMS ** 2 - SIGMA ** 2
    dia_cruce = (math.log(objetivo) - a) / b
    # referencia determinista: primer dia con exceso esperado >= objetivo
    ref = next(d for d in range(NDIAS * 3) if (d >= D0 and exceso_esperado(d) >= objetivo))
    rul_pred, rul_ref = dia_cruce - DIA_PRED, ref - DIA_PRED
    # pruebas de indicadores
    seno = [math.sin(2 * math.pi * i / 100) * 2.0 for i in range(10000)]
    g = [rng.gauss(0, 1) for _ in range(200000)]
    return dict(hi=hi, ku=ku, dia_rms=dia_rms, dia_ku=dia_ku, pend=b, crec=math.exp(b), dia_cruce=dia_cruce, ref=ref, rul_pred=rul_pred, rul_ref=rul_ref,
                err_rul=abs(rul_pred - rul_ref) / rul_ref, err_dias=abs(dia_cruce - ref), rms_seno=rms(seno), kurt_seno=curtosis(seno), kurt_gauss=curtosis(g), hi_sano=sum(hi[:D0]) / D0,
                ku_sano=sum(ku[:D0]) / D0, hi_90=hi[DIA_PRED], ku_90=ku[DIA_PRED], hi_final=hi[-1], ku_final=ku[-1], adelanto=(dia_rms - dia_ku) if dia_rms and dia_ku else None,
                dias_a_umbral=dia_cruce)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: {NDIAS} dias, ventanas de {NV} muestras; falla incipiente desde el dia {D0}; semilla {SEMILLA}")
    print(f"Pruebas de indicadores: RMS de una senoidal de amplitud 2 = {r['rms_seno']:.4f} (teorico {2/math.sqrt(2):.4f}); curtosis senoidal = {r['kurt_seno']:.4f} (1.5); curtosis gaussiana = {r['kurt_gauss']:.3f} (~3)")
    print(f"Dias sanos: RMS medio = {r['hi_sano']:.4f}; curtosis media = {r['ku_sano']:.3f}")
    print(f"Dia {DIA_PRED}: RMS = {r['hi_90']:.4f}; curtosis = {r['ku_90']:.3f}; dia 139: RMS = {r['hi_final']:.3f}; curtosis = {r['ku_final']:.3f}")
    print(f"Primer dia sobre el umbral: curtosis > {UMB_KURT}: dia {r['dia_ku']}; RMS > {UMB_RMS}: dia {r['dia_rms']} (la curtosis avisa {r['adelanto']} dias antes)")
    print(f"Regresion de ln(exceso de potencia) en los ultimos {VENT} dias hasta el dia {DIA_PRED}: pendiente = {r['pend']:.4f} por dia (factor {r['crec']:.4f}/dia)")
    print(f"Cruce proyectado del umbral de RMS: dia {r['dia_cruce']:.1f} (vida util restante {r['rul_pred']:.1f} d); referencia determinista: dia {r['ref']} ({r['rul_ref']} d); error {r['err_dias']:.1f} d")
    assert abs(r["rms_seno"] - 2 / math.sqrt(2)) < 1e-3 and abs(r["kurt_seno"] - 1.5) < 1e-2 and abs(r["kurt_gauss"] - 3) < 0.05 and r["err_dias"] < 5.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
