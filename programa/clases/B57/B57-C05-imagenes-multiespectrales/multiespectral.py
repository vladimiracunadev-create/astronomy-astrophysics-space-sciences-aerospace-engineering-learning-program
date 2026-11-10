#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C05: imagenes multiespectrales: razones de bandas y fusion con la pancromatica.

Datos: SINTETICOS. Escena de 64 x 64 pixeles con cuatro cubiertas (agua, suelo, vegetacion, urbano) y reflectancias ILUSTRATIVAS en
cuatro bandas (azul, verde, rojo, infrarrojo cercano; los limites de banda de Landsat 8 vienen de USGS, consultada 2026-11-09). Una textura
multiplicativa comun a todas las bandas representa el detalle fino; la pancromatica es el promedio de las cuatro bandas de alta resolucion.
Modelo: multiespectral a baja resolucion = promedio 2 x 2; fusion de Brovey: B_f = B_up * Pan / Pan_up, con Pan_up el promedio de las bandas
sobremuestreadas; referencia: sobremuestreo por vecino mas cercano. Semilla fija 57.
Validez: la fusion de Brovey asume que el detalle fino es comun a todas las bandas. Tolerancia: la razon entre bandas se conserva a 1e-9 y el
RMSE de Brovey es < 50 % del de vecino mas cercano.
Requiere numpy.
"""
import platform
import numpy as np

ESPECTROS = {  # reflectancia en azul, verde, rojo, NIR (ILUSTRATIVA)
    "agua": (0.06, 0.05, 0.03, 0.01),
    "suelo": (0.10, 0.15, 0.22, 0.28),
    "vegetacion": (0.04, 0.09, 0.05, 0.45),
    "urbano": (0.18, 0.20, 0.22, 0.24),
}
NOMBRES = list(ESPECTROS)


def escena(n=64, seed=57):
    rng = np.random.default_rng(seed)
    clase = np.zeros((n, n), int)
    clase[:, n // 2:] = 1
    clase[n // 2:, : n // 2] = 2
    clase[n // 2:, n // 2:] = 3
    textura = 1.0 + 0.25 * np.sign(np.sin(np.arange(n)[:, None] * 1.3) * np.sin(np.arange(n)[None, :] * 1.7))
    textura *= 1.0 + 0.02 * rng.standard_normal((n, n))
    espec = np.array([ESPECTROS[NOMBRES[c]] for c in clase.ravel()]).reshape(n, n, 4)
    espec = espec * textura[:, :, None]
    # detalle propio del infrarrojo cercano en la vegetacion (no comun a todas las bandas) y ruido independiente por banda
    tex_nir = np.sign(np.sin(np.arange(n)[:, None] * 0.9) * np.sin(np.arange(n)[None, :] * 1.1))
    espec[:, :, 3] *= 1.0 + 0.15 * tex_nir * (clase == 2)
    espec *= 1.0 + 0.01 * rng.standard_normal(espec.shape)
    return clase, espec


def baja(x):
    return x.reshape(x.shape[0] // 2, 2, x.shape[1] // 2, 2, *x.shape[2:]).mean(axis=(1, 3))


def sube(x):
    return np.repeat(np.repeat(x, 2, axis=0), 2, axis=1)


def rmse(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


def calcular():
    r = {}
    clase, verdad = escena()
    pan = verdad.mean(axis=2)
    ms = baja(verdad)
    up = sube(ms)
    pan_up = up.mean(axis=2)
    brovey = up * (pan / pan_up)[:, :, None]
    r["rmse_vecino"] = rmse(up, verdad)
    r["rmse_brovey"] = rmse(brovey, verdad)
    razon_up = up[:, :, 3] / up[:, :, 2]
    razon_b = brovey[:, :, 3] / brovey[:, :, 2]
    r["err_razon"] = float(np.max(np.abs(razon_up - razon_b)))
    # razon NIR/rojo por clase (ilustrativa): valores medios de la verdad
    for i, nom in enumerate(NOMBRES):
        m = clase == i
        r["nir_rojo_" + nom] = float(verdad[m][:, 3].mean() / verdad[m][:, 2].mean())
    r["mejora"] = r["rmse_vecino"] / r["rmse_brovey"]
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print("Razon NIR/rojo por cubierta (sintetica):")
    for nom in NOMBRES:
        print(f"  {nom:11s} {r['nir_rojo_'+nom]:7.2f}")
    print(f"RMSE vecino mas cercano = {r['rmse_vecino']:.5f} ; RMSE Brovey = {r['rmse_brovey']:.5f} ; mejora = {r['mejora']:.1f}x")
    print(f"Maxima diferencia de la razon NIR/rojo tras la fusion = {r['err_razon']:.2e}")
    assert r["err_razon"] < 1e-9
    assert r["rmse_brovey"] < 0.5 * r["rmse_vecino"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
