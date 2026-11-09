#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C08: sesgo de trazadores de la materia (umbral en un campo gaussiano y separacion pico-fondo).

Datos: SINTETICOS. Campo gaussiano en una caja periodica de L = 200 Mpc/h con 32^3 celdas y espectro de entrada P ~ k^-1.5 (ILUSTRATIVO), normalizado a
varianza 1 por celda; trazadores = celdas con delta > nu (nu = 1, 1,5, 2). Semilla 20261109. Para la parte de masa de halos: delta_c = 1,6865 (cerrado, ver C06),
sigma8 = 0,811 y Omega_m = 0,315 (resumen de Planck 2018, arXiv:1807.06209, consultado 2026-11-09), con sigma(M) = sigma8 (M/M8)^-0.27 ILUSTRATIVA y
G = 6,67430e-11 (NIST CODATA 2022, consultada 2026-11-09). No se usa ningun catalogo real.
Modelo: delta_g = 1_{delta>nu}/p - 1. Teorema de Bussgang (campo gaussiano y transformacion local): P_gm(k) = b P_mm(k) con b = E[delta 1]/(p sigma^2) = phi(nu)/p,
SIN dependencia de k. Segunda via: b estimado en la rejilla con el espectro cruzado y con sqrt(P_gg/P_mm). Separacion pico-fondo: b_L = 1 + (nu_h^2 - 1)/delta_c, nu_h = delta_c/sigma(M).
Supuestos: sesgo local determinista, sin muestreo de Poisson ni espacio de redshift. Validez: campo gaussiano; el sesgo de halos reales no es de umbral.
Tolerancia: b del espectro cruzado a baja k dentro del 8 % de phi/p.
"""
from __future__ import annotations
import cmath, math, platform, random

L = 200.0
N = 32
V = L ** 3
KF = 2 * math.pi / L


def fft1(a, inv=False):
    n = len(a)
    if n == 1:
        return a[:]
    par = fft1(a[0::2], inv)
    imp = fft1(a[1::2], inv)
    sg = 1 if inv else -1
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(sg * 2j * math.pi * k / n) * imp[k]
        out[k] = par[k] + t
        out[k + n // 2] = par[k] - t
    return out


def fft3(f, inv=False):
    g = f[:]
    for eje in range(3):
        for a in range(N):
            for b in range(N):
                idx = []
                for c in range(N):
                    if eje == 0:
                        idx.append((c * N + a) * N + b)
                    elif eje == 1:
                        idx.append((a * N + c) * N + b)
                    else:
                        idx.append((a * N + b) * N + c)
                v = fft1([g[i] for i in idx], inv)
                for i, x in zip(idx, v):
                    g[i] = x
    return g


def freq(i):
    return i if i <= N // 2 else i - N


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n2 = [freq(i) ** 2 + freq(j) ** 2 + freq(k) ** 2 for i in range(N) for j in range(N) for k in range(N)]
    amp = [0.0 if q == 0 else (math.sqrt(q)) ** -0.75 for q in n2]  # sqrt(P) ~ k^-0.75
    nus = (1.0, 1.5, 2.0)
    bx = {nu: [] for nu in nus}
    ba = {nu: [] for nu in nus}
    ba_hi = {nu: [] for nu in nus}
    fr = {nu: [] for nu in nus}
    nreal = 6
    for _ in range(nreal):
        w = [complex(rng.gauss(0, 1), 0) for _ in range(N ** 3)]
        d = [z.real for z in fft3([a * b for a, b in zip(fft3(w), amp)], inv=True)]
        m = sum(d) / len(d)
        sd = math.sqrt(sum((z - m) ** 2 for z in d) / len(d))
        d = [(z - m) / sd for z in d]
        dk = fft3([complex(z) for z in d])
        pmm = [abs(z) ** 2 for z in dk]
        for nu in nus:
            sel = [1.0 if z > nu else 0.0 for z in d]
            p = sum(sel) / len(sel)
            fr[nu].append(p)
            g = [s / p - 1 for s in sel]
            gk = fft3([complex(z) for z in g])
            pgm = [(a * b.conjugate()).real for a, b in zip(gk, dk)]
            pgg = [abs(z) ** 2 for z in gk]
            lo = [i for i, q in enumerate(n2) if 0 < q <= 16]
            hi = [i for i, q in enumerate(n2) if 144 < q <= 225]
            bx[nu].append(sum(pgm[i] for i in lo) / sum(pmm[i] for i in lo))
            ba[nu].append(math.sqrt(sum(pgg[i] for i in lo) / sum(pmm[i] for i in lo)))
            ba_hi[nu].append(math.sqrt(sum(pgg[i] for i in hi) / sum(pmm[i] for i in hi)))
    print(f"{'nu':>4} {'p':>8} {'b Bussgang=phi/p':>17} {'b cruzado (k bajo)':>19} {'sqrt(Pgg/Pmm) bajo':>19} {'sqrt(Pgg/Pmm) alto':>19}")
    ok = True
    for nu in nus:
        p = sum(fr[nu]) / nreal
        pt = 0.5 * math.erfc(nu / math.sqrt(2))
        bt = phi(nu) / pt
        mx = sum(bx[nu]) / nreal
        sx = math.sqrt(sum((v - mx) ** 2 for v in bx[nu]) / (nreal - 1) / nreal)
        ma = sum(ba[nu]) / nreal
        mh = sum(ba_hi[nu]) / nreal
        print(f"{nu:4.1f} {p:8.4f} {bt:17.3f} {mx:12.3f} +/-{sx:5.3f} {ma:19.3f} {mh:19.3f}")
        ok = ok and abs(mx - bt) / bt < 0.08
        assert abs(p - pt) < 0.01
    # separacion pico-fondo
    G = 6.67430e-11
    AU = 149597870700.0
    mpc = AU * 648000 / math.pi * 1e6
    rho_c = 3 * (100e3 / mpc) ** 2 / (8 * math.pi * G)
    msun = 1.3271244e20 / G
    rho_m = 0.315 * rho_c / msun * mpc ** 3
    m8 = 4 * math.pi / 3 * rho_m * 8.0 ** 3
    dc = 3.0 / 20.0 * (12 * math.pi) ** (2.0 / 3.0)
    print(f"{'M [Msun/h]':>11} {'nu_h':>7} {'b_L = 1+(nu^2-1)/dc':>20}")
    bl = []
    for lm in (11, 12, 13, 14, 15):
        nu_h = dc / (0.811 * (10.0 ** lm / m8) ** -0.27)
        b = 1 + (nu_h ** 2 - 1) / dc
        bl.append(b)
        print(f"{10.0 ** lm:11.1e} {nu_h:7.3f} {b:20.3f}")
    # consecuencia: amplitud aparente
    print(f"si se ignora un sesgo b = {phi(1.5) / (0.5 * math.erfc(1.5 / math.sqrt(2))):.2f}, el sigma8 aparente de los trazadores seria {0.811 * phi(1.5) / (0.5 * math.erfc(1.5 / math.sqrt(2))):.3f} en lugar de 0.811")
    assert ok
    assert all(bl[i] < bl[i + 1] for i in range(4))
    assert bl[0] < 1 < bl[-1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
