#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C23: fotometria de apertura, fraccion encerrada, S/N frente al radio y estimacion del cielo.

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): estrella gaussiana de sigma 2,0 pixeles (FWHM 4,71) y 8000 e- sobre un cielo de 30 e-/pixel con ruido de lectura de 5 e-, en una imagen de 41 x 41 pixeles;
el ruido de fotones se aproxima por una gaussiana. No es una imagen real.
Modelo: S/N(r) = S f(r) / sqrt(S f(r) + n(r) (B + RN^2)) con f la fraccion encerrada (continuo 1 - exp(-r^2/2 sigma^2) y suma discreta de pixeles); cielo por media y por mediana de un anillo de 12 a 19 pixeles.
Supuestos: PSF conocida y centrada, cielo plano, ruido independiente. Validez: la apertura entera de pixeles se aparta del circulo continuo; la contaminacion del anillo por vecinas no se modela.
Tolerancia: fraccion discreta frente a la continua a 0,08 en valor absoluto (0,005 para r >= 1 FWHM); S/N por Monte Carlo frente a la ecuacion con cielo estimado a 4 %; el radio optimo cae entre 0,5 y 1,5 FWHM.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
L = 41
C0 = 20
SIG = 2.0
F = 8000.0
B = 30.0
RN = 5.0
FWHM = SIG * math.sqrt(8 * math.log(2))


def psf_pix():
    p = [math.exp(-0.5 * (((i % L) - C0) ** 2 + ((i // L) - C0) ** 2) / SIG ** 2) for i in range(L * L)]
    s = sum(p)
    return [v / s for v in p]


def desv(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)), m


def calcular():
    rnd = random.Random(SEMILLA)
    P = psf_pix()
    r = {"fwhm": FWHM}
    rr = lambda i: math.hypot((i % L) - C0, (i // L) - C0)
    anillo = [i for i in range(L * L) if 12 <= rr(i) <= 19]
    r["n_ann"] = len(anillo)
    filas = []
    mejor = None
    for radio in [0.5 * FWHM, 0.75 * FWHM, 1.0 * FWHM, 1.5 * FWHM, 2.0 * FWHM]:
        ap = [i for i in range(L * L) if rr(i) <= radio]
        n = len(ap)
        fd = sum(P[i] for i in ap)
        fc = 1 - math.exp(-radio ** 2 / (2 * SIG ** 2))
        S = F * fd
        sn_ecu = S / math.sqrt(S + n * (B + RN ** 2))
        sn_est = S / math.sqrt(S + n * (B + RN ** 2) * (1 + (math.pi / 2) * n / len(anillo)))
        filas.append([radio / FWHM, radio, n, fd, fc, sn_ecu, sn_est, None])
    # Monte Carlo con media y mediana
    medias = [{"ap": [], "med": []} for _ in filas]
    for _ in range(1500):
        D = [rnd.gauss(F * P[i] + B, math.sqrt(F * P[i] + B + RN ** 2)) for i in range(L * L)]
        v = sorted(D[i] for i in anillo)
        cielo_med = v[len(v) // 2] if len(v) % 2 else 0.5 * (v[len(v) // 2 - 1] + v[len(v) // 2])
        for fila, acc in zip(filas, medias):
            ap = [i for i in range(L * L) if rr(i) <= fila[1]]
            acc["ap"].append(ap)
            acc["med"].append(sum(D[i] - cielo_med for i in ap))
    for fila, acc in zip(filas, medias):
        sd, m = desv(acc["med"])
        fila[7] = (m / sd, m)
        acc["ap"] = None
    r["filas"] = filas
    # optimo por barrido fino (S/N con cielo conocido)
    mejor = max(((rad / 20.0), 0) for rad in range(4, 80))
    best_r, best_sn = None, -1
    for k in range(4, 90):
        radio = k * 0.1
        ap_n = sum(1 for i in range(L * L) if rr(i) <= radio)
        fd = sum(P[i] for i in range(L * L) if rr(i) <= radio)
        S = F * fd
        sn = S / math.sqrt(S + ap_n * (B + RN ** 2))
        if sn > best_sn:
            best_r, best_sn = radio, sn
    r["r_opt"], r["sn_opt"] = best_r, best_sn
    # sesgo si el cielo se estima con un anillo contaminado por la estrella (3 a 6 pixeles)
    an2 = [i for i in range(L * L) if 3 <= rr(i) <= 6]
    cont = sum(P[i] * F for i in an2) / len(an2)
    r["sesgo_cielo"] = cont
    ap = [i for i in range(L * L) if rr(i) <= 1.5 * FWHM]
    r["perdida_flujo"] = cont * len(ap) / (F * sum(P[i] for i in ap))
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"FWHM = {r['fwhm']:.3f} pixeles ; anillo de cielo de {r['n_ann']} pixeles")
    print(f"{'r/FWHM':>7} {'r (px)':>7} {'n':>5} {'f discreta':>11} {'f continua':>11} {'S/N cielo conocido':>19} {'S/N cielo estimado':>19} {'S/N MC':>8}")
    for rf, rad, n, fd, fc, a, b, mc in r["filas"]:
        print(f"{rf:7.2f} {rad:7.3f} {n:5d} {fd:11.5f} {fc:11.5f} {a:19.2f} {b:19.2f} {mc[0]:8.2f}")
    print(f"radio de maximo S/N (cielo conocido) = {r['r_opt']:.1f} pixeles = {r['r_opt']/r['fwhm']:.2f} FWHM ; S/N = {r['sn_opt']:.2f}")
    print(f"anillo de 3 a 6 pixeles contaminado: sobreestimacion del cielo = {r['sesgo_cielo']:.2f} e-/pixel -> perdida de {r['perdida_flujo']*100:.1f} % del flujo en la apertura de 1,5 FWHM")
    for rf, rad, n, fd, fc, a, b, mc in r["filas"]:
        assert abs(fd - fc) < 0.08
        if rf >= 1.0:
            assert abs(fd - fc) < 0.005
        assert abs(mc[0] / b - 1) < 0.04, (rf, mc[0], b)
    assert 0.5 * r["fwhm"] < r["r_opt"] < 1.5 * r["fwhm"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
