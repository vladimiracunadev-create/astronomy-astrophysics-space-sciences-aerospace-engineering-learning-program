#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C08: observacion sintetica de una galaxia de particulas (disco exponencial): proyeccion, PSF, ruido y radio efectivo.

Datos: ninguna constante fisica ni galaxia real. La galaxia (60 000 particulas con perfil exponencial de escala R_d = 3 kpc, luminosidad por particula igual), la inclinacion, la escala de pixel
(0,5 kpc), la PSF gaussiana (FWHM 2 kpc), el cielo y el flujo total son ILUSTRATIVOS (sinteticos) y la semilla es 20261109. No se usa ningun codigo de transferencia radiativa; de SKIRT no se
consulto nada (la referencia no se verifico).
Modelo: la densidad superficial exponencial tiene radio de media luz R_e = 1,67835 R_d (solucion numerica de 1 - (1 + x) e^-x = 0,5); se proyecta con inclinacion i (eje menor comprimido por cos i),
se histograma en 64 x 64 pixeles, se convoluciona con una gaussiana normalizada (separable) y se calcula la senal a ruido por pixel con ruido de Poisson mas fondo (no se genera una imagen ruidosa).
Supuestos: sin polvo, sin extincion, sin lente; el radio efectivo medido es circular sobre el centro verdadero. Validez: ilustrativa.
Tolerancia: R_e medido en la imagen cara-on sin PSF a menos del 3 % del analitico; la PSF conserva el flujo a 1e-4 sobre un campo ampliado (el nucleo se normaliza; la perdida es la que escapa por el borde) y agranda R_e; el cociente de ejes recupera cos i a menos del 5 %.
"""
from __future__ import annotations
import math, platform, random, sys

RD = 3.0
N = 60000
NPIX = 64
ESC = 0.5  # kpc por pixel

def re_analitico():
    # fraccion encerrada 1 - (1 + x) e^-x = 0,5
    lo, hi = 0.1, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if 1 - (1 + mid) * math.exp(-mid) < 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) * RD

def particulas(rng, n):
    pts = []
    for _ in range(n):
        # R de una distribucion Gamma(2, RD): suma de dos exponenciales
        r = -RD * (math.log(rng.random()) + math.log(rng.random()))
        ph = rng.uniform(0, 2 * math.pi)
        pts.append((r * math.cos(ph), r * math.sin(ph)))
    return pts

def proyectar(pts, inc):
    c = math.cos(inc)
    return [(x, y * c) for x, y in pts]

def imagen(pts, npix=NPIX, esc=ESC):
    im = [[0.0] * npix for _ in range(npix)]
    for x, y in pts:
        i = int(math.floor(y / esc + npix / 2))
        j = int(math.floor(x / esc + npix / 2))
        if 0 <= i < npix and 0 <= j < npix:
            im[i][j] += 1.0
    return im

def gauss_kernel(fwhm_kpc, esc):
    sig = fwhm_kpc / 2.354820045 / esc
    half = int(math.ceil(4 * sig))
    k = [math.exp(-0.5 * (d / sig) ** 2) for d in range(-half, half + 1)]
    s = sum(k)
    return [v / s for v in k], half

def convolve(im, fwhm_kpc, esc=ESC):
    k, half = gauss_kernel(fwhm_kpc, esc)
    n = len(im)
    tmp = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for d, kv in enumerate(k):
                jj = j + d - half
                if 0 <= jj < n:
                    s += kv * im[i][jj]
            tmp[i][j] = s
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for d, kv in enumerate(k):
                ii = i + d - half
                if 0 <= ii < n:
                    s += kv * tmp[ii][j]
            out[i][j] = s
    return out

def r_efectivo(im, esc=ESC):
    n = len(im)
    c = n / 2
    pix = []
    for i in range(n):
        for j in range(n):
            r = math.hypot((j + 0.5 - c) * esc, (i + 0.5 - c) * esc)
            pix.append((r, im[i][j]))
    pix.sort()
    tot = sum(f for _, f in pix)
    acc = 0.0
    for k, (r, f) in enumerate(pix):
        acc += f
        if acc >= 0.5 * tot:
            # interpolacion lineal dentro del pixel
            r0 = pix[k - 1][0] if k else 0.0
            return r0 + (r - r0) * (0.5 * tot - (acc - f)) / f if f > 0 else r
    return pix[-1][0]

def flujo(im):
    return sum(sum(f) for f in im)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    re_a = re_analitico()
    print(f"R_e analitico = {re_a:.4f} kpc = {re_a / RD:.5f} R_d")
    assert abs(re_a / RD - 1.67835) < 1e-4
    pts = particulas(rng, N)
    im0 = imagen(proyectar(pts, 0.0))
    re0 = r_efectivo(im0)
    print(f"cara-on sin PSF: flujo en imagen {flujo(im0):.0f} de {N}; R_e medido {re0:.3f} kpc (error {abs(re0 - re_a) / re_a * 100:.2f} %)")
    assert abs(re0 - re_a) / re_a < 0.03
    # PSF: flujo conservado sobre un campo ampliado (128 x 128)
    amplio = imagen(proyectar(pts, 0.0), npix=128)
    conv_a = convolve(amplio, 2.0)
    f0, f1 = flujo(amplio), flujo(conv_a)
    print(f"PSF gaussiana FWHM 2 kpc (campo 128 x 128): flujo antes {f0:.0f}, despues {f1:.6f}, diferencia relativa {abs(f1 - f0) / f0:.1e}")
    assert abs(f1 - f0) / f0 < 1e-4
    conv = convolve(im0, 2.0)
    re_c = r_efectivo(conv)
    print(f"cara-on con PSF: R_e medido {re_c:.3f} kpc (+{(re_c / re0 - 1) * 100:.1f} % sobre {re0:.3f})")
    assert re_c > re0
    # inclinacion: cociente de ejes por momentos de segundo orden
    print(f"{'inc [grados]':>12} {'q medido':>9} {'cos i':>8}")
    for grados in (0, 30, 60, 75):
        inc = math.radians(grados)
        im = imagen(proyectar(pts, inc), npix=128)
        sxx = sxy = syy = f = 0.0
        n = len(im)
        for i in range(n):
            for j in range(n):
                w = im[i][j]
                x, y = (j + 0.5 - n / 2) * ESC, (i + 0.5 - n / 2) * ESC
                sxx += w * x * x; syy += w * y * y; sxy += w * x * y; f += w
        sxx /= f; syy /= f; sxy /= f
        tr, det = sxx + syy, sxx * syy - sxy * sxy
        l1 = tr / 2 + math.sqrt(max(tr * tr / 4 - det, 0)); l2 = tr / 2 - math.sqrt(max(tr * tr / 4 - det, 0))
        q = math.sqrt(l2 / l1)
        print(f"{grados:12d} {q:9.4f} {math.cos(inc):8.4f}")
        assert abs(q - math.cos(inc)) / math.cos(inc) < 0.05
    # ruido: S/N por pixel en el centro y en el borde
    flujo_total = 2.0e5
    cielo = 20.0
    esc_f = flujo_total / N
    cen = conv[32][32] * esc_f
    borde = conv[32][50] * esc_f
    sn_c = cen / math.sqrt(cen + cielo)
    sn_b = borde / math.sqrt(borde + cielo)
    print(f"flujo por pixel: centro {cen:.1f}, a 9 kpc {borde:.1f} (cielo {cielo:.0f}); S/N centro {sn_c:.1f}, borde {sn_b:.2f}")
    assert sn_c > sn_b
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
