#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C01: arquitectura en capas para un cálculo orbital.

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal que publica la
documentación de astropy.constants; sin resolución citada en esa página) y
período de rotación sidérea de la Tierra 23.9345 h (NASA NSSDC, Earth Fact
Sheet, actualizada 2024-11-15). Son datos publicados: el resultado es una
ESTIMACIÓN con 5 cifras.
Modelo: dos cuerpos, órbita circular de radio a; T = 2*pi*sqrt(a^3/GM).
Arquitectura: tres capas en un solo archivo para poder leerlas juntas:
  1) núcleo: funciones puras (sin entrada/salida, sin estado global);
  2) adaptador: lee una configuración y valida unidades (km -> m);
  3) orquestación: decide qué se calcula y qué se imprime.
Supuestos: masa del satélite despreciable, sin perturbaciones.
Validez: a > radio terrestre, órbitas casi circulares.
Tolerancia: 1e-12 relativa en la ida y vuelta analítica; 1e-4 relativa
contra el período sidéreo publicado (dato con 6 cifras, modelo ideal).
"""
from __future__ import annotations
import math, platform, sys

GM_TIERRA = 3.986004e14          # m3/s2
PERIODO_SIDEREO_H = 23.9345      # h


# ---- capa 1: núcleo (puro) -------------------------------------------------
def periodo(a_m: float, gm: float) -> float:
    """Período orbital T [s] de una órbita circular de radio a_m [m]."""
    if a_m <= 0 or gm <= 0:
        raise ValueError("a y GM deben ser positivos")
    return 2.0 * math.pi * math.sqrt(a_m**3 / gm)


def radio_para_periodo(t_s: float, gm: float) -> float:
    """Inversa analítica: a [m] tal que el período es t_s [s]."""
    if t_s <= 0 or gm <= 0:
        raise ValueError("T y GM deben ser positivos")
    return (gm * (t_s / (2.0 * math.pi)) ** 2) ** (1.0 / 3.0)


def velocidad_circular(a_m: float, gm: float) -> float:
    return math.sqrt(gm / a_m)


# ---- capa 2: adaptador -----------------------------------------------------
def leer_config(cfg: dict) -> dict:
    """Valida y normaliza a SI. Rechaza unidades desconocidas."""
    factor = {"m": 1.0, "km": 1.0e3}
    if cfg["unidad_a"] not in factor:
        raise ValueError(f"unidad no admitida: {cfg['unidad_a']}")
    return {"a_m": cfg["a"] * factor[cfg["unidad_a"]], "gm": cfg["gm"]}


# ---- capa 3: orquestación ---------------------------------------------------
def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def cerca(a, b, tol):
    return abs(a - b) <= tol * abs(b)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")

    # Prueba 1: ida y vuelta analítica (el núcleo es consistente consigo mismo).
    for t in (5400.0, 43082.0, 86164.0):
        prueba(cerca(periodo(radio_para_periodo(t, GM_TIERRA), GM_TIERRA), t, 1e-12),
               f"ida y vuelta T={t}")
    print("ida y vuelta T -> a -> T: correcta a 1e-12")

    # Prueba 2: tercera ley de Kepler, T^2 / a^3 es constante e igual a 4 pi^2 / GM.
    k = [periodo(a, GM_TIERRA) ** 2 / a**3 for a in (7.0e6, 1.2e7, 4.2e7)]
    prueba(all(cerca(x, 4 * math.pi**2 / GM_TIERRA, 1e-12) for x in k), "tercera ley")
    print(f"T^2/a^3 = {k[0]:.6e} s2/m3 (igual a 4 pi^2/GM = {4*math.pi**2/GM_TIERRA:.6e})")

    # Prueba 3: consistencia con el período sidéreo publicado (a se obtiene de él; se verifica que el modelo reproduzca ese período y que el radio sea el esperado para geosíncrona).
    a_geo = radio_para_periodo(PERIODO_SIDEREO_H * 3600.0, GM_TIERRA)
    t_geo_h = periodo(a_geo, GM_TIERRA) / 3600.0
    print(f"radio geosíncrono a = {a_geo/1e3:.1f} km (altitud sobre 6378.137 km: {a_geo/1e3-6378.137:.1f} km)")
    prueba(40000e3 < a_geo < 44000e3, "radio geosíncrono fuera de rango")
    prueba(cerca(t_geo_h, PERIODO_SIDEREO_H, 1e-4), "período sidéreo")

    # Prueba 4: el adaptador rechaza unidades desconocidas y convierte km -> m.
    n = leer_config({"a": a_geo / 1e3, "unidad_a": "km", "gm": GM_TIERRA})
    prueba(cerca(n["a_m"], a_geo, 1e-12), "conversión km->m")
    try:
        leer_config({"a": 1.0, "unidad_a": "mi", "gm": GM_TIERRA})
        prueba(False, "debía rechazar 'mi'")
    except ValueError as e:
        print(f"adaptador rechaza unidad: {e}")

    # Orquestación: informe.
    v = velocidad_circular(a_geo, GM_TIERRA)
    print(f"velocidad circular a ese radio v = {v:.2f} m/s")
    # Un satélite en LEO a 400 km de altitud sobre 6378.137 km
    a_leo = (6378.137 + 400.0) * 1e3
    print(f"LEO 400 km: T = {periodo(a_leo, GM_TIERRA)/60:.2f} min")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
