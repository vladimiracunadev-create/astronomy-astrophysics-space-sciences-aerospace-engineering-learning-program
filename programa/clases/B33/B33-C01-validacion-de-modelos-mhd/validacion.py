#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C01: metricas de validacion de un modelo frente a observaciones (sesgo, RMSE, correlacion, destreza y desfase temporal).

Datos: ninguna constante fisica. La serie de velocidad del viento solar (400 km/s mas dos corrientes rapidas), el modelo (desfase de 6 h, factor 0.9 y ruido de 30 km/s), la persistencia y la semilla
fija son ILUSTRATIVOS (sinteticos); no se valida ningun modelo real ni evento documentado.
Modelo: serie horaria de 30 dias; metricas: sesgo medio, RMSE, coeficiente de correlacion de Pearson, destreza MSSS = 1 - MSE_modelo/MSE_referencia con referencia la climatologia (media) y la
persistencia; desfase optimo por maximizacion de la correlacion cruzada; intervalo de confianza del RMSE por remuestreo (200 repeticiones).
Supuestos: errores independientes entre horas (el remuestreo ignora la autocorrelacion). Validez: ilustrativa.
Tolerancia: desfase recuperado igual al impuesto (6 h); MSSS respecto de climatologia mayor que respecto de persistencia a 24 h del mismo modelo no se asume.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 720
    obs = []
    for t in range(n):
        v = 400.0 + 220 * math.exp(-0.5 * ((t - 200) / 24) ** 2) + 160 * math.exp(-0.5 * ((t - 470) / 30) ** 2) + rng.gauss(0, 15)
        obs.append(v)
    lag = 6
    mod = [0.9 * (obs[t - lag] if t >= lag else obs[0]) + 40 + rng.gauss(0, 30) for t in range(n)]
    pers = [obs[t - 24] if t >= 24 else obs[0] for t in range(n)]
    def mse(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)
    def pearson(a, b):
        ma, mb = sum(a) / len(a), sum(b) / len(b)
        c = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        return c / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    sesgo = sum(m - o for m, o in zip(mod, obs)) / n
    rmse = math.sqrt(mse(mod, obs))
    clim = [sum(obs) / n] * n
    msss_c = 1 - mse(mod, obs) / mse(clim, obs)
    msss_p = 1 - mse(mod, obs) / mse(pers, obs)
    print(f"sesgo = {sesgo:.2f} km/s ; RMSE = {rmse:.2f} km/s ; correlacion = {pearson(mod, obs):.4f} ; MSSS(clim) = {msss_c:.4f} ; MSSS(persistencia 24 h) = {msss_p:.4f}")
    print(f"{'desfase [h]':>11} {'correlacion':>12}")
    mejor = (-2, 0)
    for d in range(-12, 13, 3):
        a = [mod[t + d] if 0 <= t + d < n else mod[t] for t in range(n)]
        c = pearson(a, obs)
        print(f"{d:11d} {c:12.4f}")
    cs = {}
    for d in range(-12, 13):
        a = [mod[t + d] if 0 <= t + d < n else mod[t] for t in range(n)]
        cs[d] = pearson(a, obs)
    d_opt = max(cs, key=cs.get)
    print(f"desfase optimo = {d_opt} h (impuesto: {lag} h)")
    assert d_opt == lag
    rs = []
    for _ in range(200):
        idx = [rng.randrange(n) for _ in range(n)]
        rs.append(math.sqrt(sum((mod[i] - obs[i]) ** 2 for i in idx) / n))
    rs.sort()
    print(f"RMSE por remuestreo: mediana {rs[100]:.2f} ; intervalo 5-95 % [{rs[10]:.2f}, {rs[190]:.2f}] km/s")
    assert rs[10] < rmse < rs[190]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
