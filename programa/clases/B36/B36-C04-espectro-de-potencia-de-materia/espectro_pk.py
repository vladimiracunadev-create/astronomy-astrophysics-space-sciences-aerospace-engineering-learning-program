#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C04: estimacion del espectro de potencia P(k) en una rejilla 3D y su varianza.

Datos: SINTETICOS. Campo gaussiano en una caja periodica de L = 200 Mpc/h con 32^3 celdas y espectro de ENTRADA de ley de potencias
P(k) = 1000 (k / 0.1)^(-1.5) (Mpc/h)^3, ILUSTRATIVO (no es el espectro de la materia real). Semilla 20261109. No se usa ninguna fuente externa.
Modelo: delta_k = FFT(ruido blanco) * sqrt(N^3 P / V); estimador P_hat(k) = V/N^6 |delta_k|^2 promediado en cascarones de ancho k_f = 2 pi/L.
Segunda via: la FFT propia se comprueba contra una DFT directa y contra el teorema de Parseval; el ruido de Poisson de un muestreo discreto se compara con 1/n.
Supuestos: campo gaussiano, sin asignacion de masa (sin ventana ni aliasing), caja periodica. Validez: k << k_Nyquist.
Tolerancia: bins promediados en 4 realizaciones dentro de 3 sigma de la varianza cosmica gaussiana; Parseval a 1e-9; ruido de Poisson dentro del 3 %.
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
    # f es una lista plana de N^3 complejos, indice (i*N + j)*N + k
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


def pin(k):
    return 1000.0 * (k / 0.1) ** -1.5


def kmodos():
    out = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                n2 = freq(i) ** 2 + freq(j) ** 2 + freq(k) ** 2
                out.append(n2)
    return out


def poisson(rng, lam):
    lim, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= lim:
            return k
        k += 1


def bins(n2, vals):
    """Promedio por cascarones |n| en [m-0.5, m+0.5) con m = 1..15; devuelve (modos, media)."""
    cnt = {}
    sm = {}
    for q, v in zip(n2, vals):
        if q == 0:
            continue
        m = int(math.sqrt(q) + 0.5)
        if m > 15:
            continue
        cnt[m] = cnt.get(m, 0) + 1
        sm[m] = sm.get(m, 0.0) + v
    return {m: (cnt[m], sm[m] / cnt[m]) for m in cnt}


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) FFT frente a DFT directa
    rng = random.Random(20261109)
    x = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(16)]
    dft = [sum(x[n] * cmath.exp(-2j * math.pi * k * n / 16) for n in range(16)) for k in range(16)]
    f = fft1(x)
    e_fft = max(abs(a - b) for a, b in zip(dft, f))
    print(f"FFT frente a DFT directa (n=16): error maximo = {e_fft:.2e}")
    # 2) realizaciones
    n2 = kmodos()
    kk = [KF * math.sqrt(q) for q in n2]
    amp = [0.0 if q == 0 else math.sqrt(N ** 3 * pin(k) / V) for q, k in zip(n2, kk)]
    acum = {}
    parseval = 0.0
    var_x = []
    nreal = 4
    for r in range(nreal):
        w = [complex(rng.gauss(0, 1), 0) for _ in range(N ** 3)]
        wk = fft3(w)
        dk = [a * b for a, b in zip(wk, amp)]
        d = fft3(dk, inv=True)
        d = [z.real / N ** 3 for z in d]
        dk2 = fft3([complex(z) for z in d])
        ph = [V / N ** 6 * abs(z) ** 2 for z in dk2]
        s_x = sum(z * z for z in d) / N ** 3
        s_k = sum(abs(z) ** 2 for z in dk2) / N ** 6
        parseval = max(parseval, abs(s_x - s_k) / s_k)
        var_x.append(s_x)
        for m, (c, mean) in bins(n2, ph).items():
            acum.setdefault(m, []).append((c, mean))
    teo = bins(n2, [pin(k) if q else 0.0 for q, k in zip(n2, kk)])
    print(f"Parseval: error relativo maximo = {parseval:.2e}")
    print(f"{'|n|':>4} {'k [h/Mpc]':>10} {'modos':>6} {'P entrada':>11} {'P estimado':>11} {'sigma teor.':>12} {'pull':>6}")
    pulls = []
    for m in range(1, 16):
        c = acum[m][0][0]
        est = sum(v for _, v in acum[m]) / nreal
        pt = teo[m][1]
        sg = pt * math.sqrt(2.0 / (c * nreal))
        pull = (est - pt) / sg
        pulls.append(pull)
        if m in (1, 2, 3, 5, 8, 12, 15):
            print(f"{m:4d} {m * KF:10.4f} {c:6d} {pt:11.2f} {est:11.2f} {sg:12.2f} {pull:6.2f}")
    chi2 = sum(p * p for p in pulls)
    print(f"chi2 = {chi2:.1f} con 15 bins ; |pull| maximo = {max(abs(p) for p in pulls):.2f}")
    # 3) ruido de Poisson
    lam = 2.0
    cuentas = [poisson(rng, lam) for _ in range(N ** 3)]
    dpo = [c / lam - 1 for c in cuentas]
    dkp = fft3([complex(z) for z in dpo])
    php = [V / N ** 6 * abs(z) ** 2 for z in dkp]
    mp = sum(v for q, v in zip(n2, php) if q) / (N ** 3 - 1)
    nbar = lam / (V / N ** 3)
    print(f"Poisson: P medio = {mp:.2f} (Mpc/h)^3 ; 1/n = {1 / nbar:.2f} (Mpc/h)^3 ; razon = {mp * nbar:.4f}")
    assert e_fft < 1e-12
    assert parseval < 1e-9
    assert all(abs(p) < 3.5 for p in pulls)
    assert abs(mp * nbar - 1) < 0.03
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
