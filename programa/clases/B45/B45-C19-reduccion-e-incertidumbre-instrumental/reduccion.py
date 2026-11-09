#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C19: reduccion de un CCD sintetico, curva de transferencia de fotones y ecuacion de S/N.

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): detector de 64 x 64 pixeles con ganancia 2,0 e-/ADU, ruido de lectura 6,0 e-, nivel de bias 500 ADU, oscuro 0,1 e-/s/pixel y
planos con ganancia de pixel de 2 % RMS. No se uso un detector real.
Modelo: curva de transferencia de fotones var(ADU) = mean(ADU)/g + RN^2/g^2 por parejas de planos; S/N de un punto: S = F t / sqrt(F t + n (B t + D t + RN^2)).
Supuestos: ruido de Poisson aproximado por una gaussiana, respuesta lineal, ruido de lectura gaussiano. Validez: sin no linealidad, sin carga de arrastre y sin ruido de patron fijo distinto de la ganancia por pixel.
Tolerancia: ganancia estimada a 3 % de la verdadera; ruido de lectura a 5 %; S/N por Monte Carlo frente a la ecuacion con el cielo estimado por mediana (factor pi/2) a 5 %; la ordenada de la curva de transferencia queda mal determinada y no se usa para el ruido de lectura.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
L = 64
GAIN = 2.0
RN = 6.0
BIAS = 500.0
OSCURO = 0.1


def estadisticos(a):
    m = sum(a) / len(a)
    v = sum((x - m) ** 2 for x in a) / (len(a) - 1)
    return m, v


def cuadro(rnd, e_por_pix, ganancias):
    """Imagen en ADU: bias + (Poisson(e)*g_pix + lectura)/GAIN."""
    out = []
    for gp, e in zip(ganancias, e_por_pix):
        m = e * gp
        electrones = rnd.gauss(m, math.sqrt(max(m, 0.0))) + rnd.gauss(0, RN)
        out.append(BIAS + electrones / GAIN)
    return out


def calcular():
    rnd = random.Random(SEMILLA)
    n = L * L
    gp = [1 + rnd.gauss(0, 0.02) for _ in range(n)]
    uno = [1.0] * n
    r = {}
    # bias: par de tramas
    b1, b2 = cuadro(rnd, [0.0] * n, uno), cuadro(rnd, [0.0] * n, uno)
    dif = [x - y for x, y in zip(b1, b2)]
    _, vd = estadisticos(dif)
    r["rn_est"] = math.sqrt(vd / 2) * GAIN
    r["bias_med"] = estadisticos(b1)[0]
    # curva de transferencia con planos de 10 niveles
    niveles = [200, 500, 1000, 2000, 4000, 8000, 12000, 16000, 20000, 25000]   # electrones por pixel
    xs, ys = [], []
    for e in niveles:
        p1 = cuadro(rnd, [float(e)] * n, uno)
        p2 = cuadro(rnd, [float(e)] * n, uno)
        m1, m2 = estadisticos(p1)[0], estadisticos(p2)[0]
        d = [a - b for a, b in zip(p1, p2)]
        v = estadisticos(d)[1] / 2
        xs.append(0.5 * (m1 + m2) - r["bias_med"])
        ys.append(v)
    k = len(xs)
    mx, my = sum(xs) / k, sum(ys) / k
    pend = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    inter = my - pend * mx
    r["g_est"] = 1 / pend
    r["rn_ptc"] = math.sqrt(max(inter, 0.0)) * r["g_est"]
    r["ptc"] = list(zip(niveles, xs, ys))
    # reduccion: ciencia = estrella gaussiana sobre cielo; bias maestro, oscuro, plano
    t = 100.0
    F, B, sig = 400.0, 25.0, 1.8                   # e-/s de la estrella; cielo e-/s/pixel; sigma PSF
    cx = cy = 32
    star = [F * t * math.exp(-0.5 * (((i % L) - cx) ** 2 + ((i // L) - cy) ** 2) / sig ** 2) / (2 * math.pi * sig ** 2) for i in range(n)]
    S_ver = sum(s for s in star)
    ap_r = 4.5
    en_ap = [i for i in range(n) if ((i % L) - cx) ** 2 + ((i // L) - cy) ** 2 <= ap_r ** 2]
    npix = len(en_ap)
    frac = sum(star[i] for i in en_ap) / S_ver
    res_ap = []
    for _ in range(300):
        cien = cuadro(rnd, [(OSCURO * t + B * t + star[i]) for i in range(n)], gp)
        # bias maestro de 20 tramas sin ruido de lectura residual notable: se resta el nivel medio, plano ideal conocido
        corr = [(cien[i] - BIAS) * GAIN / gp[i] for i in range(n)]
        # cielo estimado como mediana de un anillo
        anillo = sorted(corr[i] for i in range(n) if 10 <= math.hypot((i % L) - cx, (i // L) - cy) <= 18)
        cielo = anillo[len(anillo) // 2]
        res_ap.append(sum(corr[i] - cielo for i in en_ap))
    m, v = estadisticos(res_ap)
    r["S_ap_esperada"] = S_ver * frac
    r["S_ap_media"] = m
    r["sd_mc"] = math.sqrt(v)
    S = S_ver * frac
    r["sn_mc"] = m / math.sqrt(v)
    r["sn_ecu"] = S / math.sqrt(S + npix * (B * t + OSCURO * t + RN ** 2))
    n_ann = sum(1 for i in range(n) if 10 <= math.hypot((i % L) - cx, (i // L) - cy) <= 18)
    r["n_ann"] = n_ann
    r["sn_ecu_cielo"] = S / math.sqrt(S + npix * (B * t + OSCURO * t + RN ** 2) * (1 + (math.pi / 2) * npix / n_ann))
    r["npix"] = npix
    r["frac"] = frac
    r["S_total"] = S_ver
    # dominio del ruido
    r["terminos"] = (S, npix * B * t, npix * OSCURO * t, npix * RN ** 2)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"bias maestro = {r['bias_med']:.2f} ADU ; ruido de lectura desde el par de bias = {r['rn_est']:.3f} e- (verdadero {RN})")
    print(f"{'e-/pixel':>9} {'media ADU':>10} {'varianza ADU^2':>15}")
    for e, mx, v in r["ptc"]:
        print(f"{e:9d} {mx:10.2f} {v:15.3f}")
    print(f"curva de transferencia: ganancia = {r['g_est']:.4f} e-/ADU (verdadera {GAIN}) ; ruido de lectura de la ordenada = {r['rn_ptc']:.2f} e-")
    S, Bt, Dt, Rt = r["terminos"]
    print(f"apertura de {r['npix']} pixeles encierra {r['frac']*100:.2f} % del flujo ; senal esperada {r['S_ap_esperada']:.0f} e- ; recuperada {r['S_ap_media']:.0f} e- (sigma MC {r['sd_mc']:.0f})")
    print(f"terminos de varianza (e-^2): senal {S:.0f}, cielo {Bt:.0f}, oscuro {Dt:.0f}, lectura {Rt:.0f}")
    print(f"S/N: Monte Carlo {r['sn_mc']:.2f} ; ecuacion del CCD con cielo conocido {r['sn_ecu']:.2f} ; con cielo estimado por mediana de {r['n_ann']} pixeles {r['sn_ecu_cielo']:.2f}")
    assert abs(r["g_est"] / GAIN - 1) < 0.03
    assert abs(r["rn_est"] / RN - 1) < 0.05
    assert abs(r["sn_mc"] / r["sn_ecu_cielo"] - 1) < 0.05
    assert r["sn_mc"] < r["sn_ecu"]
    assert abs(r["S_ap_media"] / r["S_ap_esperada"] - 1) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
