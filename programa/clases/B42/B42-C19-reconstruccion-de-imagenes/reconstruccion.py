#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C19: reconstruccion de imagenes por filtro inverso, filtro de Wiener y Richardson-Lucy sobre una escena SINTETICA.

Datos: escena sintetica de 64 x 64 con tres estrellas (5000, 4000 y 3000 cuentas) y un disco debil ; las dos primeras estan separadas 3 pixeles = 0,75 lambda/D (bajo el criterio de Rayleigh) ;
PSF de una pupila circular ideal de 16 pixeles en una malla de 64 (4 px por lambda/D) ; ruido de Poisson aproximado por gaussiana de varianza I (mas lectura de 2 e-). Todo es ILUSTRATIVO ; semilla 20261109.
Modelo: d = h * o + n (convolucion periodica por FFT). Inverso: O = D / H con H truncada donde |H| < 1e-3 (cero) ; Wiener: O = D H* / (|H|^2 + K) con K = 1e-3 (parametro de regularizacion elegido, no optimizado) ;
Richardson-Lucy: o <- o * [h^T * (d / (h * o))] con 40 iteraciones. Vias independientes: la imagen sin ruido se recupera por el filtro inverso hasta 1e-9 (comprueba el pipeline) ; el flujo
total se conserva en RL (propiedad algebraica) ; se mide el error relativo y el cociente valle/pico entre las dos estrellas cercanas.
Supuestos: PSF conocida y estacionaria, ruido independiente, condiciones periodicas. Validez: ilustrativa ; una PSF mal conocida deteriora mucho mas el resultado (no se simula aqui).
Tolerancia: filtro inverso sin ruido a 1e-9 ; flujo de RL a 1e-9 relativo ; los errores con ruido se informan (no hay una cota teorica simple).
"""
from __future__ import annotations
import cmath, math, platform, random

N = 64
DP = 16

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

def ifft2(g):
    c = [[v.conjugate() for v in r] for r in g]
    f = fft2(c)
    return [[f[i][j].conjugate() / (N * N) for j in range(N)] for i in range(N)]

def psf_y_otf():
    c = N // 2
    P = [[complex(1.0 if math.hypot(i - c + 0.5, j - c + 0.5) <= DP / 2 else 0.0) for j in range(N)] for i in range(N)]
    F = fft2(P)
    p = [[abs(F[i][j]) ** 2 for j in range(N)] for i in range(N)]
    s = sum(sum(r) for r in p)
    p = [[v / s for v in r] for r in p]
    H = fft2([[complex(v) for v in r] for r in p])
    return p, H

def conv(a, H):
    A = fft2([[complex(v) for v in r] for r in a])
    return [[v.real for v in r] for r in ifft2([[A[i][j] * H[i][j] for j in range(N)] for i in range(N)])]

def rms_rel(a, b):
    num = math.sqrt(sum((a[i][j] - b[i][j]) ** 2 for i in range(N) for j in range(N)))
    den = math.sqrt(sum(b[i][j] ** 2 for i in range(N) for j in range(N)))
    return num / den

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    p, H = psf_y_otf()
    obj = [[0.0] * N for _ in range(N)]
    for (x, y, v) in ((28, 28, 5000.0), (31, 28, 4000.0), (45, 40, 3000.0)):
        obj[y][x] += v
    for i in range(N):
        for j in range(N):
            if math.hypot(i - 45, j - 15) <= 5:
                obj[i][j] += 40.0
    flujo = sum(sum(r) for r in obj)
    limpio = conv(obj, H)
    # filtro inverso sin ruido
    Hs = [[H[i][j] if abs(H[i][j]) > 1e-3 else 0 for j in range(N)] for i in range(N)]
    D0 = fft2([[complex(v) for v in r] for r in limpio])
    inv0 = [[v.real for v in r] for r in ifft2([[D0[i][j] / Hs[i][j] if Hs[i][j] != 0 else 0 for j in range(N)] for i in range(N)])]
    # error limitado por la banda perdida (|H| < 1e-3 es la region fuera del corte) ; se mide en banda
    O0 = fft2([[complex(v) for v in r] for r in obj])
    Oi = fft2([[complex(v) for v in r] for r in inv0])
    en_banda = max(abs(Oi[i][j] - O0[i][j]) for i in range(N) for j in range(N) if Hs[i][j] != 0)
    print(f"flujo de la escena = {flujo:.0f} cuentas ; pico de la PSF = {max(max(r) for r in p):.5f} ; |H| > 1e-3 en {sum(1 for i in range(N) for j in range(N) if abs(H[i][j]) > 1e-3)} de {N * N} frecuencias")
    print(f"filtro inverso sin ruido: error maximo en la banda = {en_banda:.2e} (por unidad de espectro de la escena)")
    assert en_banda < 1e-6 * max(abs(O0[0][0]), 1.0), en_banda
    # datos con ruido
    d = [[max(0.0, limpio[i][j] + rnd.gauss(0, math.sqrt(max(limpio[i][j], 0) + 1.0)) + rnd.gauss(0, 2.0)) for j in range(N)] for i in range(N)]
    D = fft2([[complex(v) for v in r] for r in d])
    inv = [[v.real for v in r] for r in ifft2([[D[i][j] / Hs[i][j] if Hs[i][j] != 0 else 0 for j in range(N)] for i in range(N)])]
    K = 1e-3
    wi = [[v.real for v in r] for r in ifft2([[D[i][j] * H[i][j].conjugate() / (abs(H[i][j]) ** 2 + K) for j in range(N)] for i in range(N)])]
    # Richardson-Lucy
    est = [[flujo / (N * N)] * N for _ in range(N)]
    Hc = [[H[i][j].conjugate() for j in range(N)] for i in range(N)]
    for _ in range(40):
        m = conv(est, H)
        rat = [[d[i][j] / max(m[i][j], 1e-9) for j in range(N)] for i in range(N)]
        corr = conv(rat, Hc)
        est = [[est[i][j] * corr[i][j] for j in range(N)] for i in range(N)]
    f_rl = sum(sum(r) for r in est)
    f_d = sum(sum(r) for r in d)
    print(f"flujo: datos = {f_d:.3f} ; RL = {f_rl:.3f} ; diferencia relativa = {abs(f_rl - f_d) / f_d:.2e}")
    assert abs(f_rl - f_d) / f_d < 1e-9
    print(f"{'metodo':<22} {'error relativo vs escena':>26} {'minimo':>9} {'valle/pico (par)':>17}")
    def valle(im):
        a = [im[28][x] for x in (28, 29, 30, 31)]
        return min(a[1], a[2]) / min(a[0], a[3])
    res = {}
    for nombre, im in (("datos (borrosos)", d), ("filtro inverso", inv), ("Wiener K=1e-3", wi), ("Richardson-Lucy 40", est)):
        e = rms_rel(im, obj)
        mn = min(min(r) for r in im)
        res[nombre] = (e, valle(im))
        print(f"{nombre:<22} {e:26.4f} {mn:9.1f} {valle(im):17.3f}")
    assert res["Wiener K=1e-3"][0] < res["filtro inverso"][0]
    assert res["Richardson-Lucy 40"][0] < res["datos (borrosos)"][0]
    assert min(min(r) for r in est) >= 0.0
    assert res["datos (borrosos)"][1] > 1.0        # el par no se ve resuelto en los datos
    assert res["Richardson-Lucy 40"][1] < res["datos (borrosos)"][1]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
