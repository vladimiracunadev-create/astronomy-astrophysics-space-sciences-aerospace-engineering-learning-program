#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C03: ajuste por minimos cuadrados de un modelo de apuntado de una antena altazimutal y perdida de ganancia por el error residual.

Datos: c = 299792458 m/s (NIST, CODATA 2022, consultada el 2026-11-09). Los coeficientes verdaderos del modelo, el diametro de 25 m, la frecuencia de 22 GHz, el ruido de 5 segundos de arco y las 150
observaciones de calibradores son SINTETICOS (semilla 20261109); no describen ninguna antena real ni medidas reales.
Modelo: errores de apuntado en azimut y elevacion con siete terminos clasicos: IA y IE (desplazamientos de cero), CA (colimacion), NPAE (no perpendicularidad de ejes), AN y AW (inclinacion del eje
de azimut) y FLEX (flexion gravitatoria, proporcional a cos El). Se observa (dx, dy) = (dAz cos El, dEl): dx = IA cosEl + CA + NPAE sinEl + AN sinAz sinEl - AW cosAz sinEl y
dy = IE + AN cosAz + AW sinAz + FLEX cosEl. Estimacion por ecuaciones normales con eliminacion de Gauss. Perdida de ganancia por error de apuntado radial e = sqrt(2) x RMS por eje: exp(-4 ln2 (e/HPBW)^2), con HPBW = 1,2 lambda/D.
Supuestos: errores pequenos (primer orden), terminos independientes del tiempo y de la temperatura, ruido blanco gaussiano e independiente. Validez: antena rigida; no se modela el viento ni la refraccion.
Tolerancia: cada coeficiente recuperado dentro de 4 desviaciones tipicas de su error formal; RMS residual frente a sigma sqrt((n-p)/n) dentro de 8 %; el RMS posterior debe ser menor que 1/10 del HPBW.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
ARC = math.pi / (180 * 3600)   # radianes por segundo de arco
NOMBRES = ["IA", "IE", "CA", "NPAE", "AN", "AW", "FLEX"]
VERDAD = [30.0, -20.0, 12.0, 8.0, 15.0, -10.0, 25.0]   # segundos de arco, ILUSTRATIVOS


def filas(az, el):
    """Devuelve las dos filas (dx y dy) del diseno para un punto (az, el) en radianes."""
    ce, se, ca, sa = math.cos(el), math.sin(el), math.cos(az), math.sin(az)
    fx = [ce, 0.0, 1.0, se, sa * se, -ca * se, 0.0]
    fy = [0.0, 1.0, 0.0, 0.0, ca, sa, ce]
    return fx, fy


def resolver(a, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[p] = m[p], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            for c in range(i, n + 1):
                m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][c] * x[c] for c in range(i + 1, n))) / m[i][i]
    return x


def inversa(a):
    n = len(a)
    cols = []
    for j in range(n):
        e = [1.0 if i == j else 0.0 for i in range(n)]
        cols.append(resolver(a, e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    sigma = 5.0
    n_src = 150
    dis, obs = [], []
    for _ in range(n_src):
        az = rng.uniform(0, 2 * math.pi)
        el = math.radians(rng.uniform(15, 85))
        fx, fy = filas(az, el)
        for f in (fx, fy):
            y = sum(c * v for c, v in zip(VERDAD, f)) + rng.gauss(0, sigma)
            dis.append(f)
            obs.append(y)
    n = len(obs)
    p = len(VERDAD)
    ata = [[sum(dis[k][i] * dis[k][j] for k in range(n)) for j in range(p)] for i in range(p)]
    atb = [sum(dis[k][i] * obs[k] for k in range(n)) for i in range(p)]
    est = resolver(ata, atb)
    cov = inversa(ata)
    res = [obs[k] - sum(est[i] * dis[k][i] for i in range(p)) for k in range(n)]
    rms_ini = math.sqrt(sum(o * o for o in obs) / n)
    rms_fin = math.sqrt(sum(r * r for r in res) / n)
    print(f"{n_src} calibradores, {n} mediciones, {p} parametros, sigma de ruido = {sigma} segundos de arco")
    print(f"{'termino':>8} {'verdad':>8} {'ajuste':>9} {'error formal':>13} {'(ajuste-verdad)/error':>22}")
    for i, nom in enumerate(NOMBRES):
        s = sigma * math.sqrt(cov[i][i])
        z = (est[i] - VERDAD[i]) / s
        print(f"{nom:>8} {VERDAD[i]:8.2f} {est[i]:9.3f} {s:13.3f} {z:22.2f}")
        assert abs(z) < 4
    esperado = sigma * math.sqrt((n - p) / n)
    print(f"RMS antes del ajuste = {rms_ini:.3f} ; RMS residual = {rms_fin:.3f} ; esperado sigma sqrt((n-p)/n) = {esperado:.3f} segundos de arco")
    assert abs(rms_fin / esperado - 1) < 0.08
    lam = C / 22e9
    hpbw = 1.2 * lam / 25.0 / ARC
    print(f"lambda = {lam * 1000:.4f} mm ; HPBW = 1,2 lambda/D = {hpbw:.2f} segundos de arco con D = 25 m")
    print(f"{'error radial (arcsec)':>21} {'e/HPBW':>8} {'perdida de ganancia (dB)':>26}")
    for e in (math.sqrt(2) * rms_ini, 20.0, 10.0, math.sqrt(2) * rms_fin):
        x = e / hpbw
        pl = 4 * math.log(2) * x * x
        print(f"{e:21.2f} {x:8.4f} {10 * pl / math.log(10):26.4f}")
    assert math.sqrt(2) * rms_fin < hpbw / 10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
