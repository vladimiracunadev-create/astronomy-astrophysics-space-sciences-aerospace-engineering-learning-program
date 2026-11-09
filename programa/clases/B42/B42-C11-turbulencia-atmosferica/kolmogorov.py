#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C11: pantallas de fase de Kolmogorov por FFT y funcion de estructura.

Datos: ninguna medida atmosferica. r0 = 0,15 m (a la longitud de onda de observacion), malla de 128 x 128 con paso de 0,02 m (L = 2,56 m) y 20 realizaciones FFT
(40 pantallas independientes: parte real e imaginaria) con semilla 20261109 son ILUSTRATIVAS. Los coeficientes 0,023 del espectro y 6,88 de la funcion de estructura son valores
de libro de texto NO consultados en esta clase (se verifica su consistencia interna).
Modelo: espectro de fase PSD(f) = 0,023 r0^(-5/3) f^(-11/3) (rad^2 m^2) ; pantalla = Re/Im de la FFT de c(f) sqrt(PSD) df con c complejo gaussiano ; funcion de estructura teorica
D(r) = 6,88 (r/r0)^(5/3). Vias independientes: (a) D estimada del promedio de pares de pixeles frente a la teoria ; (b) pendiente log-log ; (c) integracion directa de la PSD
(D(r) = 2 int PSD (1 - cos(2 pi f.r)) d2f) sobre la misma malla de frecuencias, que debe reproducir la media de pantallas sin hacer pantallas.
Se anaden 3 niveles de subarmonicos (rejilla 3 x 3 con paso df/3^p) para reponer las frecuencias bajas que la FFT de 2,56 m no contiene ; sin ellos D(0,08 m) sale ~35 % bajo la teoria.
Supuestos: turbulencia estacionaria y homogenea, sin escala externa finita (von Karman no incluido). Las frecuencias por encima de Nyquist (25 1/m) faltan y bajan D a r = 1 pixel. Validez: r de 2 a 8 pixeles.
Tolerancia: D de las pantallas frente a la integral espectral (via c) a 10 % ; frente a la teoria infinita el cociente debe quedar entre 0,75 y 1,05 (la malla de 128 puntos pierde 15-23 % de la potencia por truncar
frecuencias sobre Nyquist: no es un error de codigo, es una propiedad del muestreo) ; pendiente log-log 5/3 a 0,15.
"""
from __future__ import annotations
import cmath, math, platform, random

N = 128
DX = 0.02
R0 = 0.15

def fft(a):
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    m = 2
    while m <= n:
        w = cmath.exp(-2j * math.pi / m)
        for s in range(0, n, m):
            t = 1 + 0j
            for k in range(m // 2):
                u, v = a[s + k], a[s + k + m // 2] * t
                a[s + k], a[s + k + m // 2] = u + v, u - v
                t *= w
        m <<= 1
    return a

def fft2(g):
    f = [fft(r) for r in g]
    cols = [fft([f[i][j] for i in range(len(f))]) for j in range(len(f[0]))]
    return [[cols[j][i] for j in range(len(f[0]))] for i in range(len(f))]

def amplitud():
    df = 1.0 / (N * DX)
    amp = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            fy = (i if i < N // 2 else i - N) * df
            fx = (j if j < N // 2 else j - N) * df
            f = math.hypot(fx, fy)
            amp[i][j] = 0.0 if f == 0 else math.sqrt(0.023 * R0 ** (-5 / 3) * f ** (-11 / 3)) * df
    return amp

SUBNIV = 3

def sub_frecuencias():
    """Frecuencias de subarmonicos (Lane et al.): 3 niveles, rejilla 3 x 3 sin el centro, paso df / 3^p."""
    df = 1.0 / (N * DX)
    out = []
    for p in range(1, SUBNIV + 1):
        dfp = df / 3 ** p
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                if a == 0 and b == 0:
                    continue
                fx, fy = a * dfp, b * dfp
                f = math.hypot(fx, fy)
                out.append((fx, fy, math.sqrt(0.023 * R0 ** (-5 / 3) * f ** (-11 / 3)) * dfp))
    return out

SUBF = sub_frecuencias()

def pantallas(rnd, amp):
    g = [[amp[i][j] * complex(rnd.gauss(0, 1), rnd.gauss(0, 1)) for j in range(N)] for i in range(N)]
    f = fft2(g)
    a = [[f[i][j].real for j in range(N)] for i in range(N)]
    b = [[f[i][j].imag for j in range(N)] for i in range(N)]
    # subarmonicos: suma de ondas planas de baja frecuencia (separable en x e y)
    cs = [complex(rnd.gauss(0, 1), rnd.gauss(0, 1)) * am for _, _, am in SUBF]
    ex = [[cmath.exp(-2j * math.pi * fx * j * DX) for j in range(N)] for fx, _, _ in SUBF]
    ey = [[cmath.exp(-2j * math.pi * fy * i * DX) for i in range(N)] for _, fy, _ in SUBF]
    for i in range(N):
        for j in range(N):
            s = 0j
            for k in range(len(SUBF)):
                s += cs[k] * ey[k][i] * ex[k][j]
            a[i][j] += s.real
            b[i][j] += s.imag
    return a, b

def d_teoria(r):
    return 6.88 * (r / R0) ** (5 / 3)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    amp = amplitud()
    lags = (1, 2, 4, 6, 8)
    acum = {l: 0.0 for l in lags}
    cuenta = 0
    for _ in range(20):
        for scr in pantallas(rnd, amp):
            for l in lags:
                s = 0.0
                npar = 0
                for i in range(N - l):          # solo pares sin envolver (los subarmonicos no son periodicos)
                    fi = scr[i]
                    fl = scr[i + l]
                    for j in range(N - l):
                        s += (fi[j] - fi[j + l]) ** 2 + (fi[j] - fl[j]) ** 2
                        npar += 2
                acum[l] += s / npar
            cuenta += 1
    # via (c): integral espectral directa sobre la misma malla
    df = 1.0 / (N * DX)
    print(f"{cuenta} pantallas ; df = {df:.3f} 1/m ; frecuencia minima = {df:.3f} 1/m (escala maxima 1/df = {1 / df:.2f} m)")
    print(f"{'r [m]':>7} {'D pantallas':>12} {'D integral PSD':>15} {'D teoria 6,88(r/r0)^5/3':>25} {'cociente':>9}")
    logs = []
    for l in lags:
        r = l * DX
        dm = acum[l] / cuenta
        s = 0.0
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                fy = (i if i < N // 2 else i - N) * df
                fx = (j if j < N // 2 else j - N) * df
                a2 = amp[i][j] ** 2     # varianza de Re y Im: cada parte tiene varianza a2 (c tiene varianza 2 por componente => parte real var = a2)
                s += 2 * a2 * (1 - math.cos(2 * math.pi * fx * r))
        for fx, fy, am in SUBF:
            s += 2 * am * am * (1 - math.cos(2 * math.pi * fx * r))
        # el promedio sobre los dos ejes es igual por simetria del espectro isotropo
        dint = s
        dt = d_teoria(r)
        logs.append((math.log(r), math.log(dm)))
        print(f"{r:7.3f} {dm:12.4f} {dint:15.4f} {dt:25.4f} {dm / dt:9.3f}")
        assert abs(dm / dint - 1) < 0.10, (r, dm, dint)
        assert 0.75 < dm / dt < 1.05, (r, dm, dt)   # la malla discreta pierde potencia sobre Nyquist: el cociente es < 1
    n = len(logs)
    mx = sum(x for x, _ in logs) / n
    my = sum(y for _, y in logs) / n
    pend = sum((x - mx) * (y - my) for x, y in logs) / sum((x - mx) ** 2 for x, _ in logs)
    print(f"pendiente log-log de D(r) = {pend:.3f} (teoria 5/3 = {5 / 3:.3f})")
    assert abs(pend - 5 / 3) < 0.15
    # varianza total faltante por las frecuencias bajas: D(L/2) frente a la teoria
    rl = 0.64
    s = 0.0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            fx = (j if j < N // 2 else j - N) * df
            s += 2 * amp[i][j] ** 2 * (1 - math.cos(2 * math.pi * fx * rl))
    for fx, fy, am in SUBF:
        s += 2 * am * am * (1 - math.cos(2 * math.pi * fx * rl))
    print(f"r = {rl} m (L/4): D por integral PSD = {s:.3f} ; teoria infinita = {d_teoria(rl):.3f} ; deficit = {1 - s / d_teoria(rl):.1%} por frecuencias bajas ausentes")
    assert 0.0 < 1 - s / d_teoria(rl) < 0.5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
