#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca comun de los laboratorios del bloque B83 (ingenieria de sistemas y diseno de misiones).

Constantes consultadas el 2026-11-10 en la ficha de la Tierra de NASA/NSSDC (earthfact): radio ecuatorial 6378.137 km,
GM = 398600 km3/s2 (cinco cifras: es la precision de la ficha), irradiancia solar 1361.0 W/m2, g normal 9.80665 m/s2.
Sistema de referencia de los ejemplos orbitales: inercial geocentrico de EJEMPLO, orbita circular (dos cuerpos, sin J2).
La mision del bloque (ESTRELLA-S, un microsatelite de observacion de 550 km) es SINTETICA: no es una mision real.
Todo numero de los laboratorios es un modelo con datos sinteticos o ilustrativos, nunca una medicion.
"""
from __future__ import annotations
import math
import platform
import sys
import numpy as np

RE_KM = 6378.137          # NASA/NSSDC, radio ecuatorial
GM_KM3S2 = 398600.0       # NASA/NSSDC, GM de la Tierra (5 cifras)
S0_WM2 = 1361.0           # NASA/NSSDC, irradiancia solar
G0 = 9.80665              # m/s2, aceleracion normal de la gravedad (exacta)
H_KM = 550.0              # altura SINTETICA de la mision de ejemplo


def cabecera() -> str:
    return f"Python {platform.python_version()} | numpy {np.__version__}"


def comprobar(cond: bool, msg: str) -> None:
    if not cond:
        print("FALLA:", msg)
        sys.exit(1)


def periodo_s(h_km: float = H_KM) -> float:
    a = RE_KM + h_km
    return 2 * math.pi * math.sqrt(a ** 3 / GM_KM3S2)


def fraccion_eclipse(h_km: float = H_KM, beta_deg: float = 0.0) -> float:
    """Fraccion de la orbita circular en sombra cilindrica para el angulo beta del Sol (0 si no hay eclipse)."""
    a = RE_KM + h_km
    b = math.radians(beta_deg)
    x = math.sqrt(h_km ** 2 + 2 * RE_KM * h_km) / (a * math.cos(b))
    return 0.0 if x >= 1.0 else math.acos(x) / math.pi


def semiangulo_pase(h_km: float, elev_min_deg: float) -> float:
    """Semiangulo central (rad) de la huella de visibilidad sobre una estacion con elevacion minima dada."""
    e = math.radians(elev_min_deg)
    return math.acos(RE_KM * math.cos(e) / (RE_KM + h_km)) - e


def fmt(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}"
