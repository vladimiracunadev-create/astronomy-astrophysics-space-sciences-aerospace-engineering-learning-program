#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C15: deteccion robusta de pixeles calientes y muertos, reemplazo por mediana y mascara.

Datos: ninguna constante fisica. El nivel de 1000 ADU, el ruido de 10 ADU, los 30 pixeles calientes (+300 ADU), los 20 muertos (valor 0) y el cuadro de 64 x 64 son
ILUSTRATIVOS (sinteticos); no describen una camara real.
Modelo: sigma robusta = 1,4826 MAD; un pixel se marca si |x - mediana| > 5 sigma_robusta; la media y la desviacion habituales se sesgan por los defectos. Reemplazo por la mediana de los 8 vecinos.
Falsos positivos esperados: N P(|z| > 5) = N erfc(5/sqrt(2)). Semilla 20261109.
Supuestos: ruido gaussiano, defectos aislados. Validez: ilustrativa.
Tolerancia: deteccion del 100 % de los defectos inyectados; falsos positivos menores que 3 (esperados ~0,005).
"""
from __future__ import annotations
import math, platform, random, sys

W = 64
N = W * W

def med(v):
    v = sorted(v); n = len(v)
    return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    img = [rng.gauss(1000, 10) for _ in range(N)]
    idx = rng.sample(range(N), 50)
    hot, dead = idx[:30], idx[30:]
    for i in hot:
        img[i] += 300
    for i in dead:
        img[i] = 0.0
    m = med(img)
    mad = med([abs(x - m) for x in img])
    sig = 1.4826 * mad
    media = sum(img) / N
    sd = math.sqrt(sum((x - media) ** 2 for x in img) / (N - 1))
    print(f"mediana {m:.2f}, sigma robusta {sig:.2f} (verdadera 10.00) ; media {media:.2f}, desviacion habitual {sd:.2f}")
    assert abs(sig / 10 - 1) < 0.05 and sd > 3 * sig
    marc = [i for i in range(N) if abs(img[i] - m) > 5 * sig]
    verd = set(idx)
    tp = len(verd & set(marc))
    fp = len(set(marc) - verd)
    esp = N * math.erfc(5 / math.sqrt(2))
    print(f"defectos inyectados {len(verd)} ; detectados {tp} ; falsos positivos {fp} (esperados {esp:.4f})")
    assert tp == 50 and fp < 3
    # reemplazo por mediana de vecinos (8-conexa) sobre los marcados
    marcset = set(marc)
    rep = img[:]
    for i in marc:
        y, x = divmod(i, W)
        vec = [img[(y + dy) * W + (x + dx)] for dy in (-1, 0, 1) for dx in (-1, 0, 1)
               if (dy or dx) and 0 <= y + dy < W and 0 <= x + dx < W and ((y + dy) * W + x + dx) not in marcset]
        rep[i] = med(vec)
    err = [abs(rep[i] - 1000) for i in marc]
    print(f"error medio tras el reemplazo: {sum(err)/len(err):.2f} ADU ; maximo {max(err):.2f}")
    media2 = sum(rep) / N
    print(f"media de la imagen antes {media:.2f} -> despues {media2:.2f} ADU")
    assert media2 > media + 2 and abs(media2 - 1000) < 1.5
    print(f"fraccion de pixeles enmascarados: {len(marc)/N:.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
