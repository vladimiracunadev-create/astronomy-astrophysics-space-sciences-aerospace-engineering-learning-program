#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C16: cobertura uv, haz sucio y sintesis de rotacion de un conjunto este-oeste.

Datos: ninguno externo. Las posiciones de las 6 antenas (0, 60, 150, 270, 420, 600 m sobre una linea este-oeste), la longitud de onda (0,21 m),
la declinacion (+40 grados) y el intervalo horario (-6 a +6 h) son ILUSTRATIVOS; no describen un conjunto real.
Modelo: haz sucio b(l, m) = (1/N) suma cos(2 pi (u l + v m)) sobre las muestras uv y sus conjugadas. Comprobacion analitica: para muestras
uniformes u = k d (k = -M..M) en una dimension, b(l) = sin((2M+1) pi d l)/((2M+1) sin(pi d l)) (nucleo de Dirichlet).
Supuestos: plano del cielo (w ignorado), ancho de banda cero, ponderacion uniforme. Validez: orientativa.
Tolerancia: haz directo frente a Dirichlet a 1e-12; cociente de anchuras del haz frente a 1/sen(declinacion) dentro del 15 %.
"""
from __future__ import annotations
import math, platform

LAM, DEC = 0.21, math.radians(40.0)
POS = [0.0, 60.0, 150.0, 270.0, 420.0, 600.0]
ARC = math.pi / 180 / 3600

def muestras(h_ini, h_fin, paso_min):
    uv = []
    n = int((h_fin - h_ini) * 60 / paso_min) + 1
    for t in range(n):
        H = math.radians(15 * (h_ini + t * paso_min / 60))
        for i in range(len(POS)):
            for j in range(i + 1, len(POS)):
                B = (POS[j] - POS[i]) / LAM
                u, v = B * math.cos(H), B * math.sin(DEC) * math.sin(H)
                uv.append((u, v))
                uv.append((-u, -v))
    return uv

def haz(uv, l, m):
    return sum(math.cos(2 * math.pi * (u * l + v * m)) for u, v in uv) / len(uv)

def ancho(uv, eje):
    paso = 0.25 * ARC
    k = 0
    while True:
        k += 1
        x = k * paso
        b = haz(uv, x, 0.0) if eje == "l" else haz(uv, 0.0, x)
        if b < 0.5:
            b0 = haz(uv, (k - 1) * paso, 0.0) if eje == "l" else haz(uv, 0.0, (k - 1) * paso)
            xm = (k - 1) * paso + (b0 - 0.5) / (b0 - b) * paso
            return 2 * xm / ARC

def celdas(uv, c=40.0):
    return len({(round(u / c), round(v / c)) for u, v in uv})

def calc():
    # Dirichlet
    M, d = 5, 0.8
    mx = 0.0
    for q in range(1, 200):
        l = q * 0.0053
        directo = (1 + 2 * sum(math.cos(2 * math.pi * k * d * l) for k in range(1, M + 1))) / (2 * M + 1)
        cerrado = math.sin((2 * M + 1) * math.pi * d * l) / ((2 * M + 1) * math.sin(math.pi * d * l))
        mx = max(mx, abs(directo - cerrado))
    inst = muestras(0.0, 0.0, 1)
    full = muestras(-6.0, 6.0, 10)
    wl, wm = ancho(full, "l"), ancho(full, "m")
    lobulo = max(abs(haz(full, k * 2 * ARC, 0.0)) for k in range(40, 400))
    return dict(dir_dif=mx, n_inst=len(inst), n_full=len(full), c_inst=celdas(inst), c_full=celdas(full), wl=wl, wm=wm,
                razon=wm / wl, esp=1 / math.sin(DEC), lob=lobulo, umax=max(abs(u) for u, v in full), nbl=len(POS) * (len(POS) - 1) // 2,
                lam_B=LAM / POS[-1] / ARC)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"nucleo de Dirichlet: diferencia maxima haz directo - forma cerrada = {r['dir_dif']:.2e}")
    print(f"{r['nbl']} lineas de base ; muestras uv (con conjugadas): instantanea {r['n_inst']}, 12 h {r['n_full']}")
    print(f"celdas uv de 40 lambda ocupadas: instantanea {r['c_inst']}, 12 h {r['c_full']} ; u_max = {r['umax']:.1f} lambda")
    print(f"FWHM del haz sucio: en l {r['wl']:.2f} arcsec, en m {r['wm']:.2f} arcsec ; cociente {r['razon']:.3f} (1/sen delta = {r['esp']:.3f})")
    print(f"lambda/B_max = {r['lam_B']:.1f} arcsec ; lobulo lateral maximo (eje l, 80-800 arcsec) = {r['lob']:.3f}")
    assert r["dir_dif"] < 1e-12
    assert r["c_full"] > 5 * r["c_inst"]
    assert abs(r["razon"] / r["esp"] - 1) < 0.15
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
