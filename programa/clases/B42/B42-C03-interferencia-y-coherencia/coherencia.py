#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C03: visibilidad de franjas de una fuente de espectro gaussiano y longitud de coherencia.

Datos: ninguna constante fisica. Longitud de onda central 600 nm y anchos espectrales 1, 10 y 50 nm son ILUSTRATIVOS.
Modelo: para un espectro gaussiano en numero de onda (media k0, desviacion sk) la intensidad tras una diferencia de camino D es
I(D) = 1 + V(D) cos(k0 D), con V(D) = exp(-sk^2 D^2 / 2). Se integra numericamente el espectro (regla del punto medio, 4001 puntos) y se
contrasta con la formula; la longitud de coherencia se toma como el D en que V = 1/e^(1/2)... aqui V = exp(-1/2) en D = 1/sk.
Supuestos: dos haces de igual intensidad, sin dispersion. Validez: fuentes termicas de banda estrecha.
Tolerancia: visibilidad numerica frente a analitica a 1e-4 ; la fase de la franja central coincide con k0 D.
"""
from __future__ import annotations
import math, platform

L0 = 600e-9

def espectro(fwhm_nm):
    k0 = 2 * math.pi / L0
    dk = 2 * math.pi * (fwhm_nm * 1e-9) / L0 ** 2   # ancho en numero de onda (FWHM)
    sk = dk / (2 * math.sqrt(2 * math.log(2)))
    return k0, sk

def intensidad(d, k0, sk, n=4001):
    ks = [k0 + sk * (-5 + 10 * (i + 0.5) / n) for i in range(n)]
    ws = [math.exp(-0.5 * ((k - k0) / sk) ** 2) for k in ks]
    sw = sum(ws)
    return sum(w * (1 + math.cos(k * d)) for k, w in zip(ks, ws)) / sw

def visibilidad(d, k0, sk):
    # entorno de unas pocas franjas alrededor de d: maximo y minimo locales
    mx, mn = -1e9, 1e9
    paso = L0 / 40
    for j in range(-40, 41):
        i = intensidad(d + j * paso, k0, sk, 801)
        mx, mn = max(mx, i), min(mn, i)
    return (mx - mn) / (mx + mn)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'FWHM [nm]':>10} {'L_coh=1/sk [um]':>16} {'D [um]':>8} {'V integral':>11} {'V teo':>8} {'V franjas':>10}")
    for fw in (1.0, 10.0, 50.0):
        k0, sk = espectro(fw)
        lcoh = 1 / sk
        for fr in (0.5, 1.0, 2.0):
            d = fr * lcoh
            v_teo = math.exp(-0.5 * (sk * d) ** 2)
            # via 1: modulo de la media espectral de exp(i k D) (integral numerica)
            n = 4001
            ks = [k0 + sk * (-6 + 12 * (i + 0.5) / n) for i in range(n)]
            ws = [math.exp(-0.5 * ((k - k0) / sk) ** 2) for k in ks]
            sw = sum(ws)
            v_int = math.hypot(sum(w * math.cos(k * d) for k, w in zip(ks, ws)), sum(w * math.sin(k * d) for k, w in zip(ks, ws))) / sw
            assert abs(v_int - v_teo) < 1e-4, (fw, fr, v_int, v_teo)
            # via 2: contraste medido en las franjas (solo valido si V varia poco en una longitud de onda)
            if fw == 1.0:
                v_fr = visibilidad(d, k0, sk)
                assert abs(v_fr - v_teo) < 2e-3
                txt = f"{v_fr:10.4f}"
            else:
                txt = f"{'-':>10}"
            print(f"{fw:10.1f} {lcoh * 1e6:16.3f} {d * 1e6:8.3f} {v_int:11.4f} {v_teo:8.4f} {txt}")
    k0, sk = espectro(10.0)
    # fase de la franja central: I(D) con D multiplo de lambda0 da maximo
    i_max = intensidad(0.0, k0, sk)
    i_mitad = intensidad(L0 / 2, k0, sk)
    print(f"D = 0: I = {i_max:.6f} (maximo, V=1) ; D = lambda0/2: I = {i_mitad:.6f} (franja oscura)")
    assert abs(i_max - 2) < 1e-6 and i_mitad < 0.01
    # relacion longitud de coherencia ~ lambda^2/dlambda
    fw = 10.0
    l_aprox = L0 ** 2 / (fw * 1e-9)
    print(f"lambda0^2 / dlambda = {l_aprox * 1e6:.2f} um frente a 1/sk = {1 / sk * 1e6:.2f} um (mismo orden; difieren en un factor {l_aprox * sk:.3f})")
    assert 0.5 < l_aprox * sk < 5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
