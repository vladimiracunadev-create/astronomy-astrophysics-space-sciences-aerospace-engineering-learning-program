#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C13: marcado de interferencia en un espectro dinamico con umbrales robustos (MAD) y SumThreshold simplificado.

Datos: ninguna constante fisica. El espectro dinamico (64 canales x 128 tiempos de ruido gaussiano), los canales interferentes y la interferencia debil son SINTETICOS e ILUSTRATIVOS
(semilla 20261109). La idea de SumThreshold (umbrales sobre sumas de M muestras vecinas con umbral decreciente) se tomo del resumen de Offringa et al., arXiv:1002.1957, consultado el
2026-11-09; el factor rho = 1,5 y la implementacion unidimensional son una version DIDACTICA propia, no el algoritmo publicado ni sus cifras.
Modelo: sigma robusta = 1,4826 MAD; marca |x - mediana| > chi sigma; SumThreshold: para M = 1, 2, 4, 8, 16, umbral chi_M = chi_1 / rho^(log2 M) sobre la media de M muestras consecutivas en el tiempo.
Segunda via: la tasa de falsas marcas gaussiana 2 Q(chi) = erfc(chi / sqrt 2) frente a un Monte Carlo sin interferencia; la deteccion de la interferencia debil con y sin SumThreshold.
Supuestos: ruido gaussiano estacionario y de media cero tras restar la mediana; interferencia aditiva. Validez: ilustrativa.
Tolerancia: tasa de falsas marcas dentro de 3 errores estandar de la gaussiana; la interferencia fuerte se marca por completo; SumThreshold detecta mas de la interferencia debil que el umbral simple.
"""
from __future__ import annotations
import math, platform, random, statistics, sys

def mad_sigma(v):
    m = statistics.median(v)
    return 1.4826 * statistics.median([abs(x - m) for x in v]), m

def flag_simple(data, chi):
    flat = [x for row in data for x in row]
    s, m = mad_sigma(flat)
    return [[abs(x - m) > chi * s for x in row] for row in data], s, m

def sumthreshold(data, chi1=4.0, rho=1.5, s=None, m=None):
    nrow, ncol = len(data), len(data[0])
    flag = [[False] * ncol for _ in range(nrow)]
    for lvl in range(5):
        M = 2 ** lvl
        chi = chi1 / rho ** lvl
        for i in range(nrow):
            for j in range(ncol - M + 1):
                vals = [(0.0 if flag[i][j + k] else data[i][j + k] - m) for k in range(M)]
                if abs(sum(vals) / M) > chi * s:
                    for k in range(M):
                        flag[i][j + k] = True
    return flag

def compute():
    rng = random.Random(20261109)
    nch, nt = 64, 128
    R = dict(nch=nch, nt=nt)
    # solo ruido
    chi = 3.5
    cnt = tot = 0
    ntr = 100
    for _ in range(ntr):
        d = [[rng.gauss(0, 1) for _ in range(nt)] for _ in range(nch)]
        f, s, m = flag_simple(d, chi)
        cnt += sum(sum(r) for r in f); tot += nch * nt
    R.update(chi=chi, fp_obs=cnt / tot, fp_th=math.erfc(chi / math.sqrt(2)), tot=tot)
    # con interferencia
    d = [[rng.gauss(0, 1) for _ in range(nt)] for _ in range(nch)]
    strong = {5, 17, 40}
    truth = [[False] * nt for _ in range(nch)]
    for c in strong:
        for t in range(nt):
            d[c][t] += 20.0; truth[c][t] = True
    burst = range(60, 64)
    for c in range(nch):
        for t in burst:
            d[c][t] += 15.0; truth[c][t] = True
    weak_ch, w0, wl, wa = 25, 30, 16, 1.5
    for t in range(w0, w0 + wl):
        d[weak_ch][t] += wa; truth[weak_ch][t] = True
    f1, s, m = flag_simple(d, 5.0)
    f2 = sumthreshold(d, 4.0, 1.5, s, m)
    def stats(f):
        det = sum(1 for c in strong for t in range(nt) if f[c][t]) / (len(strong) * nt)
        wk = sum(1 for t in range(w0, w0 + wl) if f[weak_ch][t]) / wl
        fp = sum(1 for i in range(nch) for j in range(nt) if f[i][j] and not truth[i][j]) / sum(1 for i in range(nch) for j in range(nt) if not truth[i][j])
        return det, wk, fp
    R["simple"] = stats(f1); R["sum"] = stats(f2)
    R["sigma_rob"] = s; R["med"] = m
    R["flag_frac_simple"] = sum(sum(r) for r in f1) / (nch * nt)
    R["flag_frac_sum"] = sum(sum(r) for r in f2) / (nch * nt)
    R["truth_frac"] = sum(sum(r) for r in truth) / (nch * nt)
    R["thr"] = [(2 ** l, 4.0 / 1.5 ** l) for l in range(5)]
    # sin la interferencia fuerte la sigma ingenua (desv. tipica) esta inflada
    flat = [x for r in d for x in r]
    R["sd_naive"] = statistics.pstdev(flat)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    se = math.sqrt(R["fp_th"] * (1 - R["fp_th"]) / R["tot"])
    print(f"solo ruido, umbral {R['chi']} sigma robusta ({R['tot']} muestras): falsas marcas observadas = {R['fp_obs']:.5f} ; gaussiana 2Q = {R['fp_th']:.5f}")
    assert abs(R["fp_obs"] - R["fp_th"]) < 3 * se + 2e-4
    print(f"con interferencia: sigma robusta = {R['sigma_rob']:.4f} (mediana {R['med']:+.4f}) ; desviacion tipica ingenua = {R['sd_naive']:.3f} ; fraccion interferida real = {R['truth_frac']:.4f}")
    print("umbrales SumThreshold (M muestras, umbral en sigma):", ", ".join(f"{M}:{c:.2f}" for M, c in R["thr"]))
    print("                      canales fuertes marcados   interferencia debil marcada   falsas marcas sobre limpios")
    for name, k, ff in (("umbral simple 5 sigma", "simple", R["flag_frac_simple"]), ("SumThreshold", "sum", R["flag_frac_sum"])):
        a, b, c = R[k]
        print(f"{name:>22} {a:22.3f} {b:29.3f} {c:30.5f}")
    assert R["simple"][0] == 1.0 and R["sum"][0] == 1.0
    assert R["sum"][1] > R["simple"][1] and R["sum"][2] < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
