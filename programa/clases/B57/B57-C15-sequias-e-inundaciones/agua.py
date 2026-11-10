#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C15: sequias e inundaciones: mascara de agua con Otsu, cambio de area y anomalia de lluvia.

Datos: SINTETICOS. Imagen de 200 x 200 pixeles con tierra (indice de agua -0.4 +- 0.10) y agua (+0.5 +- 0.10) y un lago circular cuyo radio
crece de 30 a 45 pixeles (inundacion). NDWI = (verde - NIR)/(verde + NIR) (formula conocida, NO CONSULTADA). Lluvia anual sintetica
normal de media 600 mm y desviacion 150 mm durante 40 anios; semilla fija 57. Pixel de 30 m (ejemplo).
Modelo: umbral de Otsu (maximiza la varianza entre clases) frente al punto medio analitico entre dos gaussianas de igual varianza y peso;
area inundada = pixeles de agua * area del pixel; anomalia estandarizada z = (x - media)/sigma y fraccion de anios con z < -1 frente a 15.87 %.
Validez: dos clases separables, sin nubes ni sombras. Tolerancia: Otsu frente al punto medio < 0.02; area medida frente a la verdadera < 2 %.
Requiere numpy.
"""
import math, platform
import numpy as np

N, PX = 200, 30.0


def imagen(radio, rng):
    y, x = np.mgrid[:N, :N]
    agua = (x - 100) ** 2 + (y - 100) ** 2 <= radio**2
    v = np.where(agua, 0.5, -0.4) + 0.10 * rng.standard_normal((N, N))
    return v, agua


def otsu(v, bins=256):
    h, e = np.histogram(v, bins=bins)
    c = 0.5 * (e[:-1] + e[1:])
    w0 = np.cumsum(h)
    w1 = h.sum() - w0
    m0 = np.cumsum(h * c) / np.maximum(w0, 1)
    m1 = (np.sum(h * c) - np.cumsum(h * c)) / np.maximum(w1, 1)
    var = w0 * w1 * (m0 - m1) ** 2
    # la varianza entre clases tiene una meseta entre las dos modas: se toma el centro de la meseta (>= 99.9 % del maximo)
    return float(np.mean(c[var >= var.max() * 0.999]))


def calcular():
    rng = np.random.default_rng(57)
    r = {}
    v0, a0 = imagen(30, rng)
    v1, a1 = imagen(45, rng)
    for k, (v, a) in (("antes", (v0, a0)), ("despues", (v1, a1))):
        t = otsu(v)
        est = v > t
        r[f"umbral_{k}"] = t
        r[f"area_est_{k}"] = float(est.sum() * PX * PX / 1e6)
        r[f"area_ver_{k}"] = float(a.sum() * PX * PX / 1e6)
        r[f"err_{k}"] = abs(r[f"area_est_{k}"] / r[f"area_ver_{k}"] - 1)
    r["dif_area"] = r["area_est_despues"] - r["area_est_antes"]
    r["dif_ver"] = r["area_ver_despues"] - r["area_ver_antes"]
    r["punto_medio"] = (0.5 + (-0.4)) / 2
    mitad = np.where(np.arange(N)[None, :] < N // 2, 0.5, -0.4) + 0.10 * np.random.default_rng(57).standard_normal((N, N))
    r["umbral_equilibrado"] = otsu(mitad)
    rng2 = np.random.default_rng(57)
    lluvia = rng2.normal(600, 150, 200000)
    z = (lluvia - lluvia.mean()) / lluvia.std()
    r["frac_seca"] = float(np.mean(z < -1)) * 100
    r["frac_teo"] = 15.8655
    s = np.random.default_rng(57).normal(600, 150, 40)
    r["z_min_40"] = float(((s - s.mean()) / s.std()).min())
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Umbral de Otsu: antes = {r['umbral_antes']:.3f} ; despues = {r['umbral_despues']:.3f} ; imagen mitad agua mitad tierra = {r['umbral_equilibrado']:.3f} ; punto medio analitico = {r['punto_medio']:.3f}")
    print(f"Area de agua antes: estimada = {r['area_est_antes']:.3f} km2 ; verdadera = {r['area_ver_antes']:.3f} km2")
    print(f"Area de agua despues: estimada = {r['area_est_despues']:.3f} km2 ; verdadera = {r['area_ver_despues']:.3f} km2")
    print(f"Inundacion (aumento de area): estimado = {r['dif_area']:.3f} km2 ; verdadero = {r['dif_ver']:.3f} km2")
    print(f"Anios con z < -1 en 200000 anios sinteticos = {r['frac_seca']:.2f} % (normal: {r['frac_teo']:.2f} %) ; z minimo en 40 anios = {r['z_min_40']:.2f}")
    assert abs(r["umbral_equilibrado"] - r["punto_medio"]) < 0.02
    assert -0.4 < r["umbral_antes"] < 0.5 and -0.4 < r["umbral_despues"] < 0.5
    assert r["err_antes"] < 0.02 and r["err_despues"] < 0.02
    assert abs(r["frac_seca"] - r["frac_teo"]) < 0.3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
