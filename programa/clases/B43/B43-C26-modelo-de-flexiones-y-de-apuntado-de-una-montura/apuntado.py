#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C26: modelo de flexiones y de apuntado de una montura altacimutal ajustado por minimos cuadrados.

Datos: SINTETICOS. 60 estrellas ficticias con acimut uniforme en 0-360 grados y altura uniforme en 25-80 grados (semilla 20261109); parametros verdaderos ILUSTRATIVOS (segundos de arco):
IA = 120, IE = -80, CA = 45, NPAE = 20, AN = 30, AW = -25, TF = 15; ruido gaussiano de 1" por medida. No son medidas de ninguna montura.
Modelo (simplificado, de la familia de los modelos de apuntado; no reproduce al pie de la letra ninguna implementacion concreta): para angulos pequenos
  dx = dAz cos(h) = IA cos(h) + CA + NPAE sin(h) + (AN sin(A) - AW cos(A)) sin(h)
  dh = IE + AN cos(A) + AW sin(A) + TF cos(h)
Ajuste lineal por minimos cuadrados (ecuaciones normales, eliminacion de Gauss) de los 7 parametros con 120 ecuaciones; errores formales sigma sqrt(diag((A^T A)^-1)).
Verificacion independiente: parametros recuperados frente a los verdaderos (cada error menor que 4 sigma formales) y RMS residual frente al ruido inyectado.
Supuestos: angulos pequenos, errores independientes, sin termino periodico ni histeresis. Validez: modelo de primer orden.
Tolerancia: |error| < 4 sigma formal para cada parametro; RMS residual dentro del 10 % del RMS realmente inyectado (que con esta semilla resulta mayor que 1" por azar de muestreo).
"""
from __future__ import annotations
import math, platform, random

NOMBRES = ["IA", "IE", "CA", "NPAE", "AN", "AW", "TF"]
VERD = [120.0, -80.0, 45.0, 20.0, 30.0, -25.0, 15.0]

def filas(A, h):
    ca, sa, ch, sh = math.cos(A), math.sin(A), math.cos(h), math.sin(h)
    fx = [ch, 0.0, 1.0, sh, sa * sh, -ca * sh, 0.0]
    fh = [0.0, 1.0, 0.0, 0.0, ca, sa, ch]
    return fx, fh

def inversa(M):
    n = len(M)
    A = [M[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i])); A[i], A[p] = A[p], A[i]
        d = A[i][i]
        A[i] = [x / d for x in A[i]]
        for r in range(n):
            if r != i:
                f = A[r][i]
                A[r] = [A[r][c] - f * A[i][c] for c in range(2 * n)]
    return [row[n:] for row in A]

def calc():
    rng = random.Random(20261109)
    obs = []; ruido = []
    for _ in range(60):
        A = rng.uniform(0, 2 * math.pi); h = math.radians(rng.uniform(25, 80))
        fx, fh = filas(A, h)
        nx = rng.gauss(0, 1.0); nh = rng.gauss(0, 1.0); ruido += [nx, nh]
        yx = sum(p * f for p, f in zip(VERD, fx)) + nx
        yh = sum(p * f for p, f in zip(VERD, fh)) + nh
        obs.append((fx, yx)); obs.append((fh, yh))
    n = 7
    N = [[sum(f[i] * f[j] for f, _ in obs) for j in range(n)] for i in range(n)]
    b = [sum(f[i] * y for f, y in obs) for i in range(n)]
    inv = inversa(N)
    est = [sum(inv[i][j] * b[j] for j in range(n)) for i in range(n)]
    res = [y - sum(p * q for p, q in zip(est, f)) for f, y in obs]
    rms_res = math.sqrt(sum(v * v for v in res) / (len(obs) - n))
    crudo = math.sqrt(sum(y * y for _, y in obs) / len(obs))
    sig = [math.sqrt(inv[i][i]) * 1.0 for i in range(n)]
    r = dict(ruido_real=math.sqrt(sum(v * v for v in ruido) / len(ruido)), est=est, sig=sig, rms_res=rms_res, rms_antes=crudo, n_ecuaciones=len(obs))
    r["razon"] = [(est[i] - VERD[i]) / sig[i] for i in range(n)]
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("parametro | verdadero (\") | ajustado (\") | sigma formal (\") | error/sigma")
    for i, nm in enumerate(NOMBRES):
        print(f"{nm} | {VERD[i]:.1f} | {r['est'][i]:.2f} | {r['sig'][i]:.2f} | {r['razon'][i]:+.2f}")
    print(f"n_ecuaciones = {r['n_ecuaciones']}")
    print(f"rms_antes = {r['rms_antes']:.4f}")
    print(f"rms_ruido_inyectado = {r['ruido_real']:.4f}")
    print(f"rms_residual = {r['rms_res']:.4f}")
    assert all(abs(q) < 4 for q in r["razon"])
    assert abs(r["rms_res"] - r["ruido_real"]) < 0.1 * r["ruido_real"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
