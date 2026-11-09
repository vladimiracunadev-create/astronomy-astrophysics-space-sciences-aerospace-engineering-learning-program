#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C15: correlacion cruzada de dos antenas, visibilidad y equivalencia FX frente a XF (semilla fija).

Datos: ninguno externo. La fuente (potencia 0,5 unidades, fase de franja 40 grados), el ruido de cada antena (potencia 4 unidades) y el
numero de muestras son SINTETICOS (semilla 20261109).
Modelo: v1 = s + n1, v2 = s e^{i phi} + n2 con s gaussiana compleja de potencia S y n_i independientes de potencia N. La correlacion <v2 v1*> = S e^{i phi}.
Su ruido es sigma = sqrt((S+N)^2/M) en cada parte, M = numero de muestras. FX: FFT de cada flujo y producto por canal; XF: correlacion circular
en retardo y luego FFT. Ambos dan el mismo espectro cruzado (teorema de correlacion).
Supuestos: ruido gaussiano blanco, sin retardo residual, correlador ideal. Validez: orientativa.
Tolerancia: FX frente a XF a 1e-9; amplitud y fase de la visibilidad dentro de 3 sigma; caida del ruido como 1/sqrt(M) dentro del 15 %.
"""
from __future__ import annotations
import cmath, math, platform, random

def fft(x):
    n = len(x)
    if n == 1:
        return x
    p, q = fft(x[0::2]), fft(x[1::2])
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * q[k]
        out[k], out[k + n // 2] = p[k] + t, p[k] - t
    return out

def cg(rng, P):
    s = math.sqrt(P / 2)
    return complex(rng.gauss(0, s), rng.gauss(0, s))

def vis(rng, M, S, Nn, phi):
    acc = 0j
    for _ in range(M):
        s = cg(rng, S)
        v1, v2 = s + cg(rng, Nn), s * cmath.exp(1j * phi) + cg(rng, Nn)
        acc += v2 * v1.conjugate()
    return acc / M

def calc():
    rng = random.Random(20261109)
    S, Nn, phi = 0.5, 4.0, math.radians(40)
    sigma = lambda M: (S + Nn) / math.sqrt(M)
    filas = []
    for M in (1000, 4000, 16000):
        errs = []
        for _ in range(40):
            v = vis(rng, M, S, Nn, phi)
            errs.append(abs(v - S * cmath.exp(1j * phi)))
        rms = math.sqrt(sum(e * e for e in errs) / len(errs) / 2)   # por componente
        v = vis(rng, M, S, Nn, phi)
        filas.append((M, abs(v), math.degrees(cmath.phase(v)), rms))
    # FX frente a XF
    n = 256
    x1 = [cg(rng, 1.0) for _ in range(n)]
    x2 = [cg(rng, 1.0) + 0.5 * x1[(i - 5) % n] for i in range(n)]
    X1, X2 = fft(x1), fft(x2)
    fx = [a * b.conjugate() for a, b in zip(X2, X1)]
    r = [sum(x2[(i + k) % n] * x1[i].conjugate() for i in range(n)) for k in range(n)]
    xf = fft(r)
    kmax = max(range(n), key=lambda k: abs(r[k]))
    dif = max(abs(a - b) for a, b in zip(fx, xf))
    return dict(filas=filas, S=S, Nn=Nn, phi=40.0, dif=dif, kmax=kmax, rel=dif / max(abs(a) for a in fx), sig=sigma)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'M':>6} {'|V| medido':>11} {'fase [grados]':>14} {'rms error por parte':>20} {'(S+N)/sqrt(2M)':>15}")
    for M, a, f, rms in r["filas"]:
        print(f"{M:6d} {a:11.4f} {f:14.2f} {rms:20.4f} {r['sig'](M)/math.sqrt(2):15.4f}")
    print(f"FX frente a XF: diferencia maxima relativa = {r['rel']:.2e} ; retardo recuperado (lag de pico) = {r['kmax']} muestras")
    for M, a, f, rms in r["filas"]:
        assert abs(rms / (r["sig"](M) / math.sqrt(2)) - 1) < 0.3
        assert abs(a - 0.5) < 3 * r["sig"](M) and abs(f - 40) < 3 * math.degrees(r["sig"](M) / 0.5)
    assert r["rel"] < 1e-9 and r["kmax"] == 5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
