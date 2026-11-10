# SPDX-License-Identifier: Apache-2.0
"""B85-C29: degradación acumulada de un radiador en órbita (UV + oxígeno atómico + contaminación) con incertidumbre.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC); NASA SST-SoA: los coatings se oscurecen y se usa el fin de vida para el caso caliente.
SINTÉTICO e ILUSTRATIVO (semilla fija): leyes y parámetros de C13, C14 y C16, distribuciones lognormales, límite de temperatura.
Segunda vía: media del Monte Carlo frente a la evaluación determinista y cota analítica de la sensibilidad.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

SEMILLA = 20261110
ALFA0, EPS = 0.20, 0.90
DA, E0 = 0.18, 1500.0            # UV (sintetico, como C14)
ESH_ANIO = 5000.0
ESP_COAT, RE_COAT = 100e-9, 3.0e-34       # capa protectora (C13, ilustrativa)
FLUJO_AO = 7.67e18                         # m-2 s-1 (C13, 400 km, ilustrativo)
ALFA_SIN_CAPA = 0.12                       # aumento de alfa cuando la capa protectora se pierde (sintetico)
D_CONT = 0.01                              # aumento de alfa por contaminacion en toda la vida (sintetico)
LIMITE = 345.0                             # K (ilustrativo)
Q_ABS = 1.0                                # placa de 1 m2, una cara al sol (como C14)


def alfa_t(t_anios, e0=E0, da=DA, flujo=FLUJO_AO, re=RE_COAT, d_cont=D_CONT):
    esh = ESH_ANIO * t_anios
    a = ALFA0 + da * (1 - math.exp(-esh / e0))
    perdida = re * flujo * t_anios * YEAR
    if perdida >= ESP_COAT:
        a += ALFA_SIN_CAPA
    a += d_cont * min(1.0, t_anios / 2.0)
    return a


def temperatura(a):
    return (a * S0 / (EPS * SIGMA)) ** 0.25


def lognormal(rng, mediana, sigma_ln):
    return mediana * math.exp(rng.gauss(0.0, sigma_ln))


def mc(t_anios, n=20000):
    rng = random.Random(SEMILLA)
    ts = []
    sobre = 0
    for _ in range(n):
        a = alfa_t(t_anios, e0=lognormal(rng, E0, 0.2), da=lognormal(rng, DA, 0.1),
                   flujo=lognormal(rng, FLUJO_AO, 0.5), re=lognormal(rng, RE_COAT, 0.4), d_cont=lognormal(rng, D_CONT, 0.5))
        t = temperatura(a)
        ts.append(t)
        sobre += t > LIMITE
    mu = sum(ts) / n
    sd = math.sqrt(sum((x - mu) ** 2 for x in ts) / (n - 1))
    ts.sort()
    return mu, sd, ts[int(0.95 * n)], sobre / n


def calcular():
    r = {"filas": []}
    for t in (0.0, 1.0, 2.0, 5.0, 10.0, 15.0):
        a = alfa_t(t)
        r["filas"].append((t, a, temperatura(a)))
    r["t_perdida_capa"] = ESP_COAT / (RE_COAT * FLUJO_AO) / YEAR
    r["mc5"] = mc(5.0)
    r["mc10"] = mc(10.0)
    r["det5"] = temperatura(alfa_t(5.0))
    r["det10"] = temperatura(alfa_t(10.0))
    # anio en que el valor determinista cruza el limite
    r["anio_limite"] = next((t / 10.0 for t in range(0, 301) if temperatura(alfa_t(t / 10.0)) > LIMITE), None)
    # sensibilidad de T a alfa
    a5 = alfa_t(5.0)
    r["dT_dalfa"] = temperatura(a5) / (4 * a5)
    r["sd_solo_alfa"] = r["dT_dalfa"] * 0.02
    # sin la perdida de la capa (flujo muy bajo): alfa a 10 anios
    r["T10_sin_ao"] = temperatura(alfa_t(10.0, flujo=1e15))
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Radiador SINTETICO: alfa0 = {ALFA0}, eps = {EPS}; UV: +{DA} con E0 = {E0:.0f} ESH ({ESH_ANIO:.0f} ESH/anio); capa de {ESP_COAT*1e9:.0f} nm que dura {r['t_perdida_capa']:.2f} anios con flujo de O {FLUJO_AO:.2e} m-2 s-1; limite {LIMITE:.0f} K")
    print("Anios   alfa     T [K]  (determinista)")
    for t, a, tt in r["filas"]:
        print(f"{t:5.1f}   {a:.4f}   {tt:.2f}")
    print(f"Cruce del limite (determinista): {r['anio_limite']} anios")
    for t, m in ((5, r["mc5"]), (10, r["mc10"])):
        print(f"Monte Carlo a {t} anios: media = {m[0]:.2f} K ; sigma = {m[1]:.2f} K ; percentil 95 = {m[2]:.2f} K ; P(T > {LIMITE:.0f} K) = {m[3]*100:.1f} %")
    print(f"Determinista a 5 y 10 anios: {r['det5']:.2f} K y {r['det10']:.2f} K ; dT/dalfa a 5 anios = {r['dT_dalfa']:.1f} K")
    print(f"Sin erosion de la capa (flujo de O 1e15): T a 10 anios = {r['T10_sin_ao']:.2f} K")
    comprobar(abs(r["mc5"][0] - r["det5"]) < 2.0 * r["mc5"][1], "media MC cercana a la determinista")
    comprobar(r["det10"] >= r["det5"], "T creciente")
    fin()


if __name__ == "__main__":
    main()
