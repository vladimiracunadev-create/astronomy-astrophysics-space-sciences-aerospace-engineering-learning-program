#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C20: mision robotica integrada simulada (traslado de un rover con energia, ruta, planificacion diaria y anomalias).

Datos consultados (2026-11-10): velocidad maxima de Perseverance ~152 m/h sobre terreno plano y duro (NASA). El factor de ruta 1.274 viene del laboratorio de C08 (mapa SINTETICO).
ILUSTRATIVOS (sinteticos): distancia a la meta 3000 m en linea recta, factor de uso de la velocidad 0.5, 4 h de conduccion permitidas por dia, bateria util diaria 1.2 kWh,
potencia de conduccion 0.4 kW, probabilidad de anomalia con dia perdido 5 %, 20000 misiones simuladas, semilla fija. NO es una mision real ni la de Perseverance.
Modelo: horas efectivas h = min(4, E/P); distancia diaria d = v uso h; dias nominales N = ceil(D f_ruta / d); cada dia sale bien con probabilidad 1 - p; los dias hasta N exitos
siguen una binomial negativa con media N/(1 - p).
Segunda via: simulacion Monte Carlo de la mision (media y desviacion tipica) frente a la media y la varianza analiticas (tolerancia 3 sigma de la media; 5 % en la desviacion).
Unidades SI y dias. Sin pendientes, sin ventanas de comunicacion, sin degradacion de la bateria.
"""
from __future__ import annotations
import math, platform, random, statistics

V_MAX = 152.0 / 3600.0               # m/s (NASA)
D, F_RUTA, USO, H_MAX, E_DIA, P_COND, P_ANOM = 3000.0, 1.274, 0.5, 4.0, 1.2, 0.4, 0.05   # ILUSTRATIVOS (F_RUTA de C08)
NSIM, SEMILLA = 20000, 20261110


def dias_nominales(d=D, f=F_RUTA, uso=USO, h_max=H_MAX, e=E_DIA, p=P_COND):
    h = min(h_max, e / p)
    dist = V_MAX * uso * h * 3600.0
    return math.ceil(d * f / dist), dist, h


def simular(rng, n, p_anom):
    dias, hechos = 0, 0
    while hechos < n:
        dias += 1
        if rng.random() >= p_anom:
            hechos += 1
    return dias


def calc():
    n, dist, h = dias_nominales()
    rng = random.Random(SEMILLA)
    muestras = [simular(rng, n, P_ANOM) for _ in range(NSIM)]
    media, desv = statistics.mean(muestras), statistics.pstdev(muestras)
    media_a = n / (1 - P_ANOM)
    var_a = n * P_ANOM / (1 - P_ANOM) ** 2
    z = abs(media - media_a) / (math.sqrt(var_a) / math.sqrt(NSIM))
    p95 = sorted(muestras)[int(0.95 * NSIM) - 1]
    sens = {}
    for nombre, kw in {"uso +20 %": dict(uso=USO * 1.2), "uso -20 %": dict(uso=USO * 0.8), "ruta +20 %": dict(f=F_RUTA * 1.2), "bateria +20 %": dict(e=E_DIA * 1.2),
                       "bateria -20 %": dict(e=E_DIA * 0.8), "distancia +20 %": dict(d=D * 1.2)}.items():
        sens[nombre] = dias_nominales(**kw)[0]
    return dict(n=n, dist=dist, h=h, media=media, desv=desv, media_a=media_a, desv_a=math.sqrt(var_a), z=z, p95=p95, sens=sens, vmax_mh=V_MAX * 3600,
                dif_desv=abs(desv - math.sqrt(var_a)) / math.sqrt(var_a), s_uso_mas=sens["uso +20 %"], s_uso_menos=sens["uso -20 %"], s_ruta_mas=sens["ruta +20 %"],
                s_bat_mas=sens["bateria +20 %"], s_bat_menos=sens["bateria -20 %"], s_dist_mas=sens["distancia +20 %"], lim=("energia" if E_DIA / P_COND < H_MAX else "tiempo"), min_=min(muestras), max_=max(muestras))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Mision SINTETICA: meta a {D:.0f} m (en linea recta), factor de ruta {F_RUTA}; v max {r['vmax_mh']:.0f} m/h (consultada), uso {USO}")
    print(f"Horas de conduccion por dia = {r['h']:.2f} h (limitadas por {r['lim']}); distancia diaria = {r['dist']:.1f} m; dias nominales = {r['n']}")
    print(f"Con anomalias (p = {P_ANOM}) el tiempo esperado es {r['media_a']:.2f} d (simulado {r['media']:.2f} d); desviacion tipica analitica {r['desv_a']:.3f} d, simulada {r['desv']:.3f} d")
    print(f"Percentil 95 de la duracion = {r['p95']} d; minimo {r['min_']} d; maximo {r['max_']} d; diferencia de la media = {r['z']:.2f} sigma")
    print("Sensibilidad de los dias nominales:")
    for k, v in r["sens"].items():
        print(f"  {k:16s} -> {v} d ({v - r['n']:+d})")
    assert r["z"] < 3 and r["dif_desv"] < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
