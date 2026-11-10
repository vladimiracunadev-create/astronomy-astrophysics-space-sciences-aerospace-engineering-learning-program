#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C13: incertidumbre de un telemetro laser y de una camara de angulos con datos SINTETICOS.

Datos: c = 299792458 m/s (valor exacto del SI; no consultado en esta sesion). TODO lo demas es ILUSTRATIVO y sintetico, sin sensor real:
jitter de tiempo del telemetro sigma_t = 1 ns (sigma_r = c sigma_t / 2); camara con focal 50 mm, pixel 5 um, objetivo de 4 m de largo,
error de centroide sigma_p = 0.1 px; semilla aleatoria 76013.
Modelo: telemetro r = c t / 2 con ruido gaussiano; camara r = f L / (p * pix) -> sigma_r / r = sigma_p / p con p = f L / (r * pix) (tamano en pixeles).
Fusion de dos medidas independientes por ponderacion de inversa de la varianza. Monte Carlo de 20000 muestras por distancia. La camara solo es valida donde la imagen cabe en el sensor (aqui r >= 100 m: 400 px o menos).
Tolerancias: desviacion estandar de Monte Carlo frente a la teorica < 3 % (20000 muestras).
"""
from __future__ import annotations
import math, os, platform, random, sys

C = 299792458.0
SIG_T = 1e-9
F, PIX, L, SIG_P = 0.050, 5e-6, 4.0, 0.1


def sigma_lidar():
    return C * SIG_T / 2


def sigma_camara(r):
    p = F * L / (r * PIX)          # tamano de la imagen en pixeles
    return r * SIG_P / p, p


def fusion(s1, s2):
    return math.sqrt(1.0 / (1.0 / s1 ** 2 + 1.0 / s2 ** 2))


def monte_carlo(r, n=20000, semilla=76013):
    rng = random.Random(semilla)
    sl = sigma_lidar()
    sc, p = sigma_camara(r)
    ml, mc, mf = [], [], []
    for _ in range(n):
        a = r + rng.gauss(0, sl)
        # camara: el tamano en pixeles tiene ruido; r = f L / (p pix)
        pm = p + rng.gauss(0, SIG_P)
        b = F * L / (pm * PIX)
        w1, w2 = 1 / sl ** 2, 1 / sc ** 2
        ml.append(a); mc.append(b); mf.append((w1 * a + w2 * b) / (w1 + w2))
    def sd(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))
    return sd(ml), sd(mc), sd(mf)


def calcular():
    filas = []
    for r in (100.0, 200.0, 500.0, 1000.0):
        sl = sigma_lidar()
        sc, p = sigma_camara(r)
        sm = monte_carlo(r)
        filas.append(dict(r=r, p=p, sl=sl, sc=sc, sf=fusion(sl, sc), mc=sm))
    cruce = None
    # distancia en la que sigma_camara = sigma_lidar : r^2 sigma_p pix/(f L) = sigma_lidar
    cruce = math.sqrt(sigma_lidar() * F * L / (SIG_P * PIX))
    return dict(filas=filas, cruce=cruce, sl=sigma_lidar())


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar) ; semilla 76013 ; datos SINTETICOS")
    print(f"Telemetro: sigma_r = c*sigma_t/2 = {r['sl']:.4f} m (independiente de la distancia en este modelo)")
    print(" r [m]   tamano [px]  s_lidar[m]  s_camara[m]  s_fusion[m]  MC lidar   MC camara   MC fusion")
    for q in r['filas']:
        print(f"{q['r']:6.0f}  {q['p']:10.1f}  {q['sl']:9.4f}  {q['sc']:10.4f}  {q['sf']:10.4f}  {q['mc'][0]:9.4f}  {q['mc'][1]:10.4f}  {q['mc'][2]:9.4f}")
    print(f"Distancia en que ambos sensores empatan = {r['cruce']:.1f} m")
    for q in r['filas']:
        assert abs(q['mc'][0] - q['sl']) / q['sl'] < 0.03
        assert abs(q['mc'][1] - q['sc']) / q['sc'] < 0.06
        assert abs(q['mc'][2] - q['sf']) / q['sf'] < 0.06
        assert q['sf'] <= min(q['sl'], q['sc']) + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
