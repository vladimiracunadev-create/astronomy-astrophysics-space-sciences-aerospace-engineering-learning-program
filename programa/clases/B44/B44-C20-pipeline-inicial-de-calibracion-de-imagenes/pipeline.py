#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C20: pipeline inicial bias - dark - flat - mascara - fotometria de apertura sobre un campo sintetico.

Datos: ninguna constante fisica. Todo es SINTETICO: cuadros de 64 x 64 pixeles, bias de 500 e- con patron de columnas, ruido de lectura de 5 e-, corriente oscura de 0,05 e-/s con 4 pixeles calientes,
respuesta con PRNU de 1 % y vineteo del 10 %, una estrella gaussiana (FWHM de 3 pixeles) con 40 000 e- inyectados, cielo de 20 e-/s en 100 s y 6 rayos cosmicos. No es una observacion.
El orden de los pasos (sustraer bias, sustraer dark, dividir por flat) coincide con el descrito en la documentacion de ccdproc consultada el 2026-11-09 (docs.astropy.org); no se uso esa biblioteca.
Modelo: ciencia = bias + dark t + flat x (cielo t + estrella) + ruido; maestro bias (15 cuadros, mediana), maestro dark (7 cuadros de 100 s, bias restado), maestro flat (15 cuadros, mediana normalizada);
mascara de pixeles calientes y rayos cosmicos por sigma robusta; fotometria de apertura de radio 6 pix con anillo de cielo 10-14 pix. Semilla 20261109.
Supuestos: ruido gaussiano, un solo filtro, sin no linealidad. Validez: ilustrativa.
Tolerancia: flujo recuperado dentro de 1 % del inyectado por la respuesta media del campo (el flat se normaliza a su media; la apertura de radio 6 contiene casi todo el flujo) y dentro de 4 sigma de la incertidumbre esperada.
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
    rn, b0, tsci = 5.0, 500.0, 100.0
    col = [rng.gauss(0, 2.0) for _ in range(W)]
    bias_v = [b0 + col[i % W] for i in range(N)]
    tasa = [0.05 for _ in range(N)]
    calientes = (300, 1500, 2500, 3500)
    for i in calientes:
        tasa[i] = 3.0
    resp = []
    for y in range(W):
        for x in range(W):
            rho2 = ((x - 31.5) ** 2 + (y - 31.5) ** 2) / (2 * 31.5 ** 2)
            resp.append((1 + rng.gauss(0, 0.01)) * (1 - 0.10 * rho2))
    sky = 20.0
    sg = 3.0 / 2.3548200450309493
    cx, cy, F = 40.3, 22.6, 40000.0
    star = [F * (math.erf((x + 0.5 - cx) / (sg * math.sqrt(2))) - math.erf((x - 0.5 - cx) / (sg * math.sqrt(2)))) / 2 *
            (math.erf((y + 0.5 - cy) / (sg * math.sqrt(2))) - math.erf((y - 0.5 - cy) / (sg * math.sqrt(2)))) / 2
            for y in range(W) for x in range(W)]
    def g(mu):
        return rng.gauss(mu, math.sqrt(max(mu, 0.0))) if mu > 0 else 0.0
    def cuadro(t, luz):
        return [bias_v[i] + g(tasa[i] * t) + g(resp[i] * luz(i) * 1.0) + rng.gauss(0, rn) for i in range(N)]
    bias_f = [cuadro(0, lambda i: 0.0) for _ in range(15)]
    mbias = [med([f[i] for f in bias_f]) for i in range(N)]
    dark_f = [cuadro(100.0, lambda i: 0.0) for _ in range(7)]
    mdark = [med([f[i] - mbias[i] for f in dark_f]) for i in range(N)]      # e- en 100 s
    flat_f = [cuadro(5.0, lambda i: 20000.0) for _ in range(15)]
    mf = [med([(f[i] - mbias[i] - mdark[i] * 5.0 / 100.0) for f in flat_f]) for i in range(N)]
    mn = sum(mf) / N
    mflat = [x / mn for x in mf]
    ciencia = cuadro(tsci, lambda i: sky * tsci + star[i])
    # cinco rayos cosmicos + uno adicional
    rc = rng.sample([i for i in range(N) if i not in calientes], 6)
    for i in rc:
        ciencia[i] += 800.0
    # pasos
    p1 = [ciencia[i] - mbias[i] for i in range(N)]
    p2 = [p1[i] - mdark[i] for i in range(N)]
    p3 = [p2[i] / mflat[i] for i in range(N)]
    # mascara
    m = med(p3)
    sigr = 1.4826 * med([abs(x - m) for x in p3])
    mask = {i for i in range(N) if abs(p3[i] - m) > 5 * sigr and not (abs((i % W) - cx) < 8 and abs((i // W) - cy) < 8)} | set(calientes)
    print(f"mascara: {len(mask)} pixeles ({len(set(rc) & mask)} de 6 rayos cosmicos, {len(set(calientes) & mask)} de 4 calientes) ; sigma robusta {sigr:.2f} e-")
    assert set(rc) <= mask
    img = p3[:]
    for i in mask:
        y, x = divmod(i, W)
        vec = [p3[(y + dy) * W + x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1)
               if (dy or dx) and 0 <= y + dy < W and 0 <= x + dx < W and ((y + dy) * W + x + dx) not in mask]
        img[i] = med(vec)
    def foto(im):
        ap = [i for i in range(N) if math.hypot(i % W - cx, i // W - cy) <= 6.0]
        an = [i for i in range(N) if 10.0 <= math.hypot(i % W - cx, i // W - cy) <= 14.0]
        cielo = med([im[i] for i in an])
        flujo = sum(im[i] - cielo for i in ap)
        return flujo, cielo, len(ap), len(an)
    f_cal, c_cal, nap, nan_ = foto(img)
    rm = sum(resp) / N
    Fref = F * rm       # el flat se normaliza a su media: el flujo queda en unidades de un pixel de respuesta media
    # sin calibrar: solo restar la mediana de un anillo (sin mascara)
    f_raw, c_raw, _, _ = foto(ciencia)
    var = F + nap * (sky * tsci + 0.05 * tsci + rn ** 2 + 1.0) * (1 + 1.0 / nan_)
    sig_esp = math.sqrt(var)
    print(f"{'caso':<26} {'flujo [e-]':>12} {'error [e-]':>11} {'error [%]':>10}")
    print(f"respuesta media del campo {rm:.4f} ; flujo de referencia tras normalizar el flat: {Fref:.1f} e-")
    for nombre, f in (("sin calibrar", f_raw), ("pipeline completo", f_cal)):
        print(f"{nombre:<26} {f:12.1f} {f-Fref:11.1f} {100*(f-Fref)/Fref:10.3f}")
    print(f"incertidumbre esperada (fotones + cielo + lectura): {sig_esp:.1f} e- ({100*sig_esp/F:.2f} %) ; apertura {nap} pix, anillo {nan_} pix")
    assert abs(f_cal - Fref) < 4 * sig_esp
    assert abs(f_cal - Fref) / Fref < 0.01 and abs(f_raw - Fref) > abs(f_cal - Fref)
    # estructura residual del cielo tras el pipeline
    zona = [img[i] for i in range(N) if math.hypot(i % W - cx, i // W - cy) > 14 and i not in mask]
    mz = sum(zona) / len(zona)
    sz = math.sqrt(sum((x - mz) ** 2 for x in zona) / (len(zona) - 1))
    zr = [ciencia[i] for i in range(N) if math.hypot(i % W - cx, i // W - cy) > 14]
    mr = sum(zr) / len(zr)
    sr = math.sqrt(sum((x - mr) ** 2 for x in zr) / (len(zr) - 1))
    print(f"cielo: nivel {mz:.1f} e- (esperado {sky*tsci*rm:.1f} = cielo x respuesta media) ; dispersion {sz:.1f} e- tras el pipeline frente a {sr:.1f} e- sin calibrar")
    assert abs(mz - sky * tsci * rm) < 10 and sr > sz
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
