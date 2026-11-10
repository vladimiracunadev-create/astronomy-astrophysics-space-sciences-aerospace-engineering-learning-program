# SPDX-License-Identifier: Apache-2.0
"""B85-C27: márgenes y correlación térmica: ajuste de una conductancia a datos de ensayo sintéticos y margen por Monte Carlo.

Todo SINTÉTICO e ILUSTRATIVO (semilla fija); el criterio de correlación de ±3 K y la política de margen no están consultados.
Modelo: cadena de 3 nodos (fuente, caja, radiador) con una conductancia desconocida G_c entre caja y radiador.
Segunda vía: ajuste por sección áurea frente a búsqueda en malla; margen por Monte Carlo frente a la propagación lineal de varianzas.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

SEMILLA = 20261110
EA_RAD = 0.85 * 0.4
Q_CASOS = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]       # W de disipacion en la caja (6 casos de ensayo)
G_VERD = 1.8                                          # W/K verdadero (sintetico)
G_MODELO = 1.2                                        # W/K supuesto inicial (sintetico)
G_FIJA = 3.0                                          # W/K entre fuente y caja
LIMITE = 330.0                                        # K (ilustrativo)


def t_caja(q, g_c, g_f=G_FIJA):
    t_rad = (q / (SIGMA * EA_RAD)) ** 0.25
    return t_rad + q / g_c


def t_fuente(q, g_c, g_f=G_FIJA):
    return t_caja(q, g_c) + q / g_f


def datos():
    rng = random.Random(SEMILLA)
    return [t_caja(q, G_VERD) + rng.gauss(0.0, 0.6) for q in Q_CASOS]


def rms(g_c, medidas):
    return math.sqrt(sum((t_caja(q, g_c) - m) ** 2 for q, m in zip(Q_CASOS, medidas)) / len(medidas))


def aurea(f, a, b, it=80):
    gr = (math.sqrt(5) - 1) / 2
    c1, d1 = b - gr * (b - a), a + gr * (b - a)
    for _ in range(it):
        if f(c1) < f(d1):
            b = d1
        else:
            a = c1
        c1, d1 = b - gr * (b - a), a + gr * (b - a)
    return 0.5 * (a + b)


def calcular():
    r = {}
    med = datos()
    r["med"] = med
    r["res0"] = [t_caja(q, G_MODELO) - m for q, m in zip(Q_CASOS, med)]
    r["bias0"] = sum(r["res0"]) / len(med)
    r["rms0"] = rms(G_MODELO, med)
    r["max0"] = max(abs(x) for x in r["res0"])
    r["g_aj"] = aurea(lambda g: rms(g, med), 0.5, 5.0)
    r["g_malla"] = min((0.5 + 0.0005 * k for k in range(0, 9001)), key=lambda g: rms(g, med))
    r["rms1"] = rms(r["g_aj"], med)
    r["res1"] = [t_caja(q, r["g_aj"]) - m for q, m in zip(Q_CASOS, med)]
    r["max1"] = max(abs(x) for x in r["res1"])
    r["cumple0"] = r["max0"] <= 3.0
    r["cumple1"] = r["max1"] <= 3.0
    # margen: incertidumbre de G (+-15 % 1 sigma), Q (+-5 %), eps (+-3 %) en el caso de 60 W
    rng = random.Random(SEMILLA + 1)
    q0, g0, e0 = 60.0, r["g_aj"], EA_RAD
    muestras = []
    for _ in range(20000):
        g = g0 * (1 + rng.gauss(0, 0.15))
        q = q0 * (1 + rng.gauss(0, 0.05))
        ea = e0 * (1 + rng.gauss(0, 0.03))
        muestras.append((q / (SIGMA * ea)) ** 0.25 + q / g)
    mu = sum(muestras) / len(muestras)
    sd = math.sqrt(sum((x - mu) ** 2 for x in muestras) / (len(muestras) - 1))
    r["mu"], r["sd"] = mu, sd
    r["t_nom"] = t_caja(q0, g0)
    # propagacion lineal de varianzas
    d_g = -q0 / g0 ** 2 * g0 * 0.15
    d_q = (0.25 * (q0 / (SIGMA * e0)) ** 0.25 + q0 / g0) * 0.05
    d_e = -0.25 * (q0 / (SIGMA * e0)) ** 0.25 * 0.03
    r["sd_lin"] = math.sqrt(d_g ** 2 + d_q ** 2 + d_e ** 2)
    r["margen_3sd"] = LIMITE - (r["t_nom"] + 3 * sd)
    r["margen_nominal"] = LIMITE - r["t_nom"]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Datos de ensayo SINTETICOS: T_caja = T_rad(Q) + Q/G con G verdadero = {G_VERD} W/K, ruido 0.6 K, semilla {SEMILLA}; modelo inicial G = {G_MODELO} W/K")
    print("Q [W]   T medida [K]   residuo inicial [K]   residuo ajustado [K]")
    for q, m, a, b in zip(Q_CASOS, r["med"], r["res0"], r["res1"]):
        print(f"{q:5.0f}   {m:12.2f}   {a:+19.2f}   {b:+20.2f}")
    print(f"Inicial: sesgo = {r['bias0']:+.2f} K ; RMS = {r['rms0']:.2f} K ; maximo = {r['max0']:.2f} K ; cumple +-3 K: {'si' if r['cumple0'] else 'no'}")
    print(f"Ajuste: G = {r['g_aj']:.4f} W/K (seccion aurea) ; {r['g_malla']:.4f} W/K (malla) ; RMS = {r['rms1']:.2f} K ; maximo = {r['max1']:.2f} K ; cumple +-3 K: {'si' if r['cumple1'] else 'no'}")
    print(f"Margen en el caso de 60 W (limite {LIMITE:.0f} K): T nominal = {r['t_nom']:.2f} K ; Monte Carlo: media = {r['mu']:.2f} K, sigma = {r['sd']:.2f} K (lineal {r['sd_lin']:.2f} K)")
    print(f"Margen nominal = {r['margen_nominal']:.2f} K ; margen tras 3 sigma = {r['margen_3sd']:.2f} K")
    comprobar(abs(r["g_aj"] - r["g_malla"]) < 1e-3, "aurea frente a malla")
    comprobar(abs(r["sd"] - r["sd_lin"]) / r["sd_lin"] < 0.08, "Monte Carlo frente a lineal")
    comprobar(not r["cumple0"] and r["cumple1"], "el ajuste mejora la correlacion")
    fin()


if __name__ == "__main__":
    main()
