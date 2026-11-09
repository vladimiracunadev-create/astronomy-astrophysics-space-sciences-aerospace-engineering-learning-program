#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C22: ley de Bouguer, grafico de Langley, formulas de masa de aire y coeficiente de color.

Datos: la formula de masa de aire de Kasten y Young (1989) X = 1/[cos z + 0,50572 (96,07995 - z)^-1,6364] (z en grados) se leyo en la pagina Air mass (astronomy) de Wikipedia el 2026-11-09, junto con la
tabla de esa pagina (K-Y 5,59 y sec z 5,76 en z = 80 grados; verificada aqui). El resto es SINTETICO e ILUSTRATIVO (semilla 20261109): k = 0,180 mag/masa de aire para una estrella, 12 masas de aire entre 1,0 y 2,5,
m0 = 12,000 y ruido de 0,010 mag; coeficiente de color k'' = -0,030; escala de Rayleigh k ~ lambda^-4 como aproximacion ilustrativa.
Modelo: m = m0 + k X (Bouguer); ajuste de recta con error formal sigma/sqrt(S_XX); k(color) = k' + k'' (B-V) con dos estrellas.
Supuestos: atmosfera estable y plano-paralela corregida por la formula elegida, ruido gaussiano. Validez: noche fotometrica; las nubes y los aerosoles variables invalidan la recta.
Tolerancia: k recuperado dentro de 3 errores formales; dispersion Monte Carlo frente al error formal a 5 %; K-Y frente a sec z en el cenit a 1e-3.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
K_TRUE, M0, SIG = 0.180, 12.000, 0.010


def ky(zdeg):
    return 1 / (math.cos(math.radians(zdeg)) + 0.50572 * (96.07995 - zdeg) ** -1.6364)


def recta(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx
    m0 = my - k * mx
    res = [b - m0 - k * a for a, b in zip(x, y)]
    return k, m0, sxx, math.sqrt(sum(e * e for e in res) / (n - 2))


def calcular():
    rnd = random.Random(SEMILLA)
    r = {}
    r["tabla"] = [(z, ky(z), 1 / math.cos(math.radians(z))) for z in (0, 30, 60, 70, 80, 85)]
    X = sorted(rnd.uniform(1.0, 2.5) for _ in range(12))
    m = [M0 + K_TRUE * x + rnd.gauss(0, SIG) for x in X]
    k, m0, sxx, rms = recta(X, m)
    r["k"], r["m0"], r["rms"] = k, m0, rms
    r["ek"] = SIG / math.sqrt(sxx)
    mx = sum(X) / len(X)
    r["em0"] = SIG * math.sqrt(1 / len(X) + mx ** 2 / sxx)
    r["X_min"], r["X_max"] = X[0], X[-1]
    ks = []
    for _ in range(4000):
        mm = [M0 + K_TRUE * x + rnd.gauss(0, SIG) for x in X]
        ks.append(recta(X, mm)[0])
    mk = sum(ks) / len(ks)
    r["mc_k"] = math.sqrt(sum((a - mk) ** 2 for a in ks) / (len(ks) - 1))
    r["mc_k_media"] = mk
    # rango de masa de aire pequeno
    Xe = [1.0 + 0.5 * i / 11 for i in range(12)]
    sxx2 = sum((a - sum(Xe) / 12) ** 2 for a in Xe)
    r["ek_estrecho"] = SIG / math.sqrt(sxx2)
    # error por usar sec z en vez de K-Y a z = 80
    r["dX80"] = (1 / math.cos(math.radians(80))) - ky(80)
    r["dm80"] = K_TRUE * r["dX80"]
    # coeficiente de color: dos estrellas, B-V = 0,0 y 1,5
    kp, kpp = 0.180, -0.030
    kc = []
    for bv in (0.0, 1.5):
        kt = kp + kpp * bv
        Xs = sorted(rnd.uniform(1.0, 2.5) for _ in range(12))
        mm = [M0 + kt * x + rnd.gauss(0, SIG) for x in Xs]
        kc.append((bv, kt, recta(Xs, mm)[0], SIG / math.sqrt(sum((a - sum(Xs) / 12) ** 2 for a in Xs))))
    r["color"] = kc
    r["kpp_est"] = (kc[1][2] - kc[0][2]) / 1.5
    r["kpp_err"] = math.sqrt(kc[0][3] ** 2 + kc[1][3] ** 2) / 1.5
    # escala de Rayleigh ilustrativa k ~ lambda^-4 anclada en 0,15 a 550 nm
    r["rayleigh"] = [(l, 0.15 * (550.0 / l) ** 4) for l in (400, 450, 550, 700, 900)]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'z (grados)':>10} {'K-Y':>8} {'sec z':>8}")
    for z, a, b in r["tabla"]:
        print(f"{z:10d} {a:8.4f} {b:8.4f}")
    print(f"Langley: 12 masas de aire entre {r['X_min']:.3f} y {r['X_max']:.3f} ; k = {r['k']:.4f} +- {r['ek']:.4f} (verdadero {K_TRUE}) ; m0 = {r['m0']:.4f} +- {r['em0']:.4f} (verdadero {M0}) ; RMS = {r['rms']:.4f}")
    print(f"Monte Carlo (4000): sigma_k = {r['mc_k']:.5f} (formal {r['ek']:.5f}) ; media {r['mc_k_media']:.5f}")
    print(f"con un rango estrecho de masa de aire (1,0 a 1,5) el error formal sube a {r['ek_estrecho']:.4f} ({r['ek_estrecho']/r['ek']:.2f} veces)")
    print(f"a z = 80 grados sec z - K-Y = {r['dX80']:.3f} masas de aire -> {r['dm80']*1000:.1f} mmag con k = 0,18")
    for bv, kt, ke, e in r["color"]:
        print(f"estrella con B-V = {bv:.1f}: k verdadero {kt:.4f} ; medido {ke:.4f} +- {e:.4f}")
    print(f"k'' estimado = {r['kpp_est']:.4f} +- {r['kpp_err']:.4f} (verdadero -0.030)")
    print("escala ilustrativa k(lambda) = 0,15 (550/lambda)^4:", ", ".join(f"{l} nm -> {k:.3f}" for l, k in r["rayleigh"]))
    assert abs(r["k"] - K_TRUE) < 3 * r["ek"]
    assert abs(r["mc_k"] / r["ek"] - 1) < 0.05
    assert abs(ky(0) - 1.0) < 1e-3
    assert abs(ky(80) - 5.586) < 5e-3
    assert abs(r["kpp_est"] + 0.030) < 3 * r["kpp_err"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
