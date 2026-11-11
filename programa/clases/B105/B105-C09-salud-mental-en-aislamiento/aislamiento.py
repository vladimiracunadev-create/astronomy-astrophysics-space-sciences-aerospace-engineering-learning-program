#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C09: seguimiento de una escala de animo en aislamiento con CUSUM y tasa de falsas alarmas (datos SINTETICOS).

Serie diaria sintetica de una escala de animo (puntuacion z, sin unidades): AR(1) x_t = phi x_{t-1} + e_t con phi = 0.4, varianza estacionaria 1.
Linea base personal: media y DE de los primeros 30 dias. Cambio: salto de +/-1.0 DE a partir del dia 90 (ILUSTRATIVO). CUSUM unilateral inferior que se inicia en S = 0 al comenzar la ventana de vigilancia (dia 90, 90 dias de vigilancia):
S_t = max(0, S_{t-1} - z_t - k) con k = 0.5; alarma si S_t > h. 180 dias; 5000 series; semilla 105. No se consulto ninguna escala validada; es un
ejercicio de deteccion de cambios y NO una herramienta de evaluacion psicologica. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

PHI, K = 0.4, 0.5


def serie(rng, n, dias, cambio_dia=None, salto=0.0):
    e = rng.normal(0, np.sqrt(1 - PHI ** 2), (n, dias))
    x = np.zeros((n, dias))
    x[:, 0] = rng.normal(0, 1, n)
    for t in range(1, dias):
        x[:, t] = PHI * x[:, t - 1] + e[:, t]
    if cambio_dia is not None:
        x[:, cambio_dia:] += salto
    return x


def alarma(x, h, base=30, inicio=90):
    mu = x[:, :base].mean(axis=1, keepdims=True)
    sd = x[:, :base].std(axis=1, ddof=1, keepdims=True)
    z = (x - mu) / sd
    s = np.zeros(x.shape[0]); primer = np.full(x.shape[0], -1)
    for t in range(inicio, x.shape[1]):
        s = np.maximum(0, s - z[:, t] - K)
        nuevo = (s > h) & (primer < 0)
        primer[nuevo] = t
    return primer


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): AR(1) con phi = 0.4; salto de -1 DE desde el dia 90 en la serie con cambio; sin escalas reales")
    rng = np.random.default_rng(105)
    n = 5000
    base = serie(rng, n, 180)
    cambio = serie(rng, n, 180, cambio_dia=90, salto=-1.0)
    print("umbral h | falsas alarmas en 90 d de vigilancia (sin cambio) | detecciones (con cambio) | retraso mediano [dias]")
    res = {}
    for h in (3.0, 4.0, 5.0, 6.0, 8.0):
        fa = np.mean(alarma(base, h) >= 0)
        p = alarma(cambio, h)
        det = np.mean(p >= 90)
        pre = 0.0
        retraso = np.median(p[p >= 90] - 90) if np.any(p >= 90) else float("nan")
        res[h] = (fa, det)
        print(f"   {h:3.1f}   |        {fa:.3f}                           |   {det:.3f}               |   {retraso:5.1f}")
    # intervalo de confianza de la tasa de falsas alarmas (h = 4)
    fa4 = res[4.0][0]
    se = np.sqrt(fa4 * (1 - fa4) / n)
    print(f"Con h = 4: falsas alarmas (90 d) = {fa4:.3f} +- {1.96 * se:.3f} (95 %, n = {n} series)")
    print(f"Con una tripulacion de 6 personas, P(al menos una falsa alarma en la mision) con h = 4 = {1 - (1 - fa4) ** 6:.3f}")
    assert res[3.0][0] > res[4.0][0] > res[8.0][0]
    assert res[3.0][1] >= res[8.0][1]
    assert res[4.0][1] > 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
