#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C25: carga util educativa en un CubeSat de 3U, resolucion en tierra, balance de potencia, datos, masa y matriz de verificacion de requisitos.

Datos: S_sol = 1361 W/m2, GM_Tierra = 3,986004e14 m3/s2 y R_ecuatorial = 6,3781e6 m de la UAI B3 de 2015 (arXiv:1510.07674, consultada el 2026-11-09). TODO lo demas es ILUSTRATIVO y es un
ejemplo docente, no una mision ni un requisito de ninguna convocatoria (no se consulto ningun estandar de CubeSat): orbita circular a 500 km, camara con pixel de 3,45 micrometros, 2048 x 1536 pixeles de 12 bit,
focal de 0,10 m y apertura de 0,03 m, celdas del 28 % que cubren el 60 % de cada cara, cargas medias de 2 W (carga util, ciclo 20 %), 3 W (servicio) y 4 W (comunicaciones, ciclo 10 %), bateria de 20 Wh,
enlace de 100 kbit/s y compresion 2,2 (como C16, sintetica), presupuesto de masa con incertidumbre del 10 % por partida.
Modelo: (1) GSD = h p/f, ancho de franja N GSD y parametro de muestreo Q = lambda F/p; (2) area proyectada media de un cuerpo convexo = S/4 (teorema de Cauchy) contrastada con un Monte Carlo de orientaciones
aleatorias (semilla 20261109) sobre las seis caras de un 3U; potencia generada media = eta cobertura S_sol A_media (1 - f_eclipse); (3) energia de bateria en eclipse y profundidad de descarga;
(4) volumen por paso = velocidad * duracion (geometrica, elevacion 10 grados); (5) masa con margen del 20 % y probabilidad de superar el limite por Monte Carlo; (6) matriz de verificacion.
Supuestos: orientacion aleatoria (caso peor sin control de actitud), orbita sin precesion, eclipse beta = 0, sin degradacion. Validez: ilustrativa.
Tolerancia: area proyectada media frente a S/4, 1 %; resultado de la matriz reproducible.
"""
from __future__ import annotations
import math, platform, random

S0 = 1361.0
GM = 3.986004e14
RE = 6.3781e6
H = 500e3
A = RE + H
PIX, FOC, DIAM, NX, NY, BITS, LAM = 3.45e-6, 0.10, 0.03, 2048, 1536, 12, 550e-9
ETA, COB = 0.28, 0.60
CARAS = [((1, 0, 0), 0.03), ((-1, 0, 0), 0.03), ((0, 1, 0), 0.03), ((0, -1, 0), 0.03), ((0, 0, 1), 0.01), ((0, 0, -1), 0.01)]
MASAS = {"estructura": 0.85, "paneles y bateria": 0.55, "ordenador y radio": 0.45, "actitud": 0.35, "camara": 0.60, "otros": 0.30}


def proyectada(s):
    return sum(a * max(0.0, n[0] * s[0] + n[1] * s[1] + n[2] * s[2]) for n, a in CARAS)


def vec_aleatorio(rng):
    z = rng.uniform(-1, 1)
    f = rng.uniform(0, 2 * math.pi)
    r = math.sqrt(1 - z * z)
    return (r * math.cos(f), r * math.sin(f), z)


def calc():
    r = {}
    r["gsd"] = H * PIX / FOC
    r["franja_km"] = NX * r["gsd"] / 1e3
    r["Q"] = LAM * (FOC / DIAM) / PIX
    r["airy_um"] = 2.44 * LAM * (FOC / DIAM) * 1e6
    sup = sum(a for _, a in CARAS)
    r["sup"] = sup
    r["media_teor"] = sup / 4
    rng = random.Random(20261109)
    n = 200000
    r["media_mc"] = sum(proyectada(vec_aleatorio(rng)) for _ in range(n)) / n
    rho = math.asin(RE / A)
    r["f_ecl"] = rho / math.pi
    per = 2 * math.pi * math.sqrt(A ** 3 / GM)
    r["per_min"] = per / 60
    r["t_ecl_min"] = r["f_ecl"] * per / 60
    r["p_gen"] = ETA * COB * S0 * r["media_teor"] * (1 - r["f_ecl"])
    r["p_carga"] = 2 * 0.2 + 3 + 4 * 0.1
    r["balance"] = r["p_gen"] - r["p_carga"]
    e_ecl = r["p_carga"] * r["t_ecl_min"] / 60
    r["e_ecl"] = e_ecl
    r["dod"] = e_ecl / 20.0
    lc = math.acos(RE * math.cos(math.radians(10)) / A) - math.radians(10)
    r["paso_s"] = 2 * lc / (2 * math.pi) * per
    r["vol_MB"] = 100e3 * r["paso_s"] / 8 / 1e6
    r["img_MB"] = NX * NY * BITS / 8 / 1e6 / 2.2
    r["img_paso"] = r["vol_MB"] / r["img_MB"]
    r["m_nom"] = sum(MASAS.values())
    r["m_marg"] = r["m_nom"] * 1.2
    exc = 0
    for _ in range(50000):
        m = sum(v * (1 + 0.10 * rng.gauss(0, 1)) for v in MASAS.values())
        if m * 1.2 > 4.0:
            exc += 1
    r["p_exceso"] = exc / 50000
    r["mat"] = [
        ("R1 GSD <= 20 m", r["gsd"], r["gsd"] <= 20),
        ("R2 masa con margen <= 4 kg", r["m_marg"], r["m_marg"] <= 4.0),
        ("R3 profundidad de descarga <= 30 %", r["dod"] * 100, r["dod"] <= 0.30),
        ("R4 balance de potencia > 0 W", r["balance"], r["balance"] > 0),
        ("R5 imagenes por paso >= 2", r["img_paso"], r["img_paso"] >= 2),
    ]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"GSD = {r['gsd']:.3f} m ; franja = {r['franja_km']:.2f} km ; Q = lambda F/p = {r['Q']:.3f} ; disco de Airy (2.44 lambda F) = {r['airy_um']:.2f} um")
    print(f"superficie del 3U = {r['sup']:.3f} m2 ; area proyectada media: teoria S/4 = {r['media_teor']:.5f} ; Monte Carlo = {r['media_mc']:.5f} m2")
    print(f"periodo = {r['per_min']:.3f} min ; eclipse = {r['t_ecl_min']:.2f} min ({r['f_ecl']*100:.2f} %)")
    print(f"potencia generada media = {r['p_gen']:.3f} W ; carga media = {r['p_carga']:.3f} W ; balance = {r['balance']:+.3f} W")
    print(f"energia en eclipse = {r['e_ecl']:.3f} Wh ; profundidad de descarga = {r['dod']*100:.2f} %")
    print(f"paso a 10 grados = {r['paso_s']:.1f} s ; volumen = {r['vol_MB']:.3f} MB ; imagen comprimida = {r['img_MB']:.3f} MB ; imagenes por paso = {r['img_paso']:.2f}")
    print(f"masa nominal = {r['m_nom']:.2f} kg ; con margen 20 % = {r['m_marg']:.3f} kg ; P(masa con margen > 4 kg) = {r['p_exceso']:.4f}")
    for nombre, v, ok in r["mat"]:
        print(f"  {nombre:38s} valor = {v:9.3f}  {'CUMPLE' if ok else 'NO CUMPLE'}")
    assert abs(r["media_mc"] - r["media_teor"]) / r["media_teor"] < 0.01
    assert r["gsd"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
