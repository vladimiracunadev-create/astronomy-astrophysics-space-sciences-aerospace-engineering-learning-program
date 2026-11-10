#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C24: carga util de observacion terrestre: de los requisitos al presupuesto de datos y a la apertura.

Datos: requisitos tomados de Sentinel-2 como PUNTO DE PARTIDA (altitud 786 km, barrido 290 km, pixeles de 10 m en 4 bandas, 12 bits; SentiWiki, consultada 2026-11-09).
ILUSTRATIVOS (no son los de ninguna mision): paso de pixel 7.5 um, lambda 0.665 um, apertura 0.15 m, fraccion de la orbita en que se adquiere 50 %, compresion 2:1,
enlace de bajada 520 Mbit/s con 10 minutos de contacto por orbita. GM y R de referencia, no consultados.
Modelo: pixeles por linea = barrido/GSD ; velocidad sobre el suelo = v_orb R/(R+H) ; tasa de lineas = v_suelo/GSD ; tasa de bits = lineas x pixeles x bandas x bits ;
focal f = p H/GSD ; campo de vision 2 atan(barrido/2/H) (Tierra plana) ; apertura minima por Rayleigh 1.22 lambda H/GSD ; datos por orbita frente a capacidad del enlace.
Validez: aproximada y de primer orden; no es un diseno de instrumento. Tolerancia: tasa de lineas x GSD = velocidad sobre el suelo a 1e-9; el presupuesto debe cerrar o declarar el deficit.
"""
import math, platform

GM, RT = 3.986004418e14, 6378137.0
H, SWATH, GSD, BANDAS, BITS = 786e3, 290e3, 10.0, 4, 12
PITCH, LAM, D = 7.5e-6, 0.665e-6, 0.15
FRAC, COMP, ENLACE, CONTACTO = 0.5, 2.0, 520e6, 600.0


def calcular():
    r = {}
    r["px_linea"] = SWATH / GSD
    v = math.sqrt(GM / (RT + H))
    vg = v * RT / (RT + H)
    r["v_suelo"] = vg / 1e3
    r["lineas_s"] = vg / GSD
    r["err_lineas"] = abs(r["lineas_s"] * GSD - vg)
    r["px_s"] = r["lineas_s"] * r["px_linea"]
    r["tasa_Gbit"] = r["px_s"] * BANDAS * BITS / 1e9
    r["f"] = PITCH * H / GSD
    r["fov"] = math.degrees(2 * math.atan(SWATH / 2 / H))
    r["ancho_focal_mm"] = r["px_linea"] * PITCH * 1e3
    r["D_min_mm"] = 1.22 * LAM * H / GSD * 1e3
    r["Fnum"] = r["f"] / D
    T = 2 * math.pi * math.sqrt((RT + H) ** 3 / GM)
    r["T_min"] = T / 60
    r["Gbit_orbita"] = r["tasa_Gbit"] * T * FRAC / COMP
    r["cap_enlace_Gbit"] = ENLACE * CONTACTO / 1e9
    r["razon"] = r["Gbit_orbita"] / r["cap_enlace_Gbit"]
    r["contacto_necesario_min"] = r["Gbit_orbita"] * 1e9 / ENLACE / 60
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Pixeles por linea = {r['px_linea']:.0f} ; velocidad sobre el suelo = {r['v_suelo']:.3f} km/s ; tasa de lineas = {r['lineas_s']:.1f} /s")
    print(f"Tasa de pixeles = {r['px_s']/1e6:.1f} Mpx/s ; tasa de bits sin comprimir = {r['tasa_Gbit']:.2f} Gbit/s")
    print(f"Focal con paso 7.5 um = {r['f']:.3f} m ; campo de vision = {r['fov']:.2f} grados ; ancho de la linea focal = {r['ancho_focal_mm']:.0f} mm")
    print(f"Apertura minima por difraccion = {r['D_min_mm']:.1f} mm ; con D = 0.15 m, F/# = {r['Fnum']:.2f}")
    print(f"Periodo orbital = {r['T_min']:.2f} min ; datos por orbita (50 % de adquisicion, compresion 2:1) = {r['Gbit_orbita']:.0f} Gbit")
    print(f"Capacidad del enlace por orbita (520 Mbit/s x 600 s) = {r['cap_enlace_Gbit']:.0f} Gbit ; razon datos/capacidad = {r['razon']:.2f} ; contacto necesario = {r['contacto_necesario_min']:.1f} min")
    assert r["err_lineas"] < 1e-9
    assert r["D_min_mm"] < 150
    print("Pruebas superadas." if r["razon"] <= 1 else "Pruebas superadas (el presupuesto NO cierra: se declara el deficit).")


if __name__ == "__main__":
    main()
