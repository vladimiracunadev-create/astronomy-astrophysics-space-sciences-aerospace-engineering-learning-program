#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Módulo B07-C06: funciones reutilizables para comprobar la regularidad de Kepler.

Datos PUBLICADOS: NASA NSSDC, fichas individuales de planetas (act. 11-ene-2024 a
19-may-2025), consultadas el 2026-11-05: semieje mayor (1e6 km) y período sidéreo (d).
Modelo: con T en años terrestres y a en distancias terrestres, T^2/a^3 ≈ 1 y T ≈ a^1,5
(regularidad empírica de Kepler usada sin derivarla).
Supuestos: órbitas casi circulares; los dos datos son del mismo planeta.
Dominio de validez: planetas del sistema solar; a > 0 y T > 0.
Tolerancia: la prueba exige que todas las razones estén a ±2 % de 1.
"""

from __future__ import annotations

import sys

A_TIERRA_1E6KM = 149.598   # semieje mayor de la Tierra
T_TIERRA_D = 365.256       # período sidéreo de la Tierra

DATOS = {  # nombre: (semieje mayor en 1e6 km, período sidéreo en d)
    "Mercurio": (57.909, 87.969), "Venus": (108.210, 224.701), "Tierra": (149.598, 365.256),
    "Marte": (227.956, 686.980), "Júpiter": (778.479, 4332.589), "Saturno": (1432.041, 10755.699),
    "Urano": (2867.043, 30685.400), "Neptuno": (4514.953, 60189.018),
}


def normalizar(valor: float, referencia: float) -> float:
    """Devuelve valor / referencia (adimensional)."""
    return valor / referencia


def razon_kepler(a_rel: float, t_anios: float) -> float:
    """Devuelve T^2 / a^3 con T en años terrestres y a en distancias terrestres."""
    return t_anios ** 2 / a_rel ** 3


def periodo_predicho(a_rel: float, exponente: float = 1.5) -> float:
    """Devuelve el período (años terrestres) predicho: a_rel elevado a `exponente`."""
    return a_rel ** exponente


def desviacion_porcentual(medido: float, esperado: float) -> float:
    """Devuelve 100 * (medido - esperado) / esperado."""
    return 100.0 * (medido - esperado) / esperado


def planeta_a_razon(nombre: str) -> float:
    """Devuelve la razón de Kepler del planeta `nombre` (clave de DATOS)."""
    a, t = DATOS[nombre]
    return razon_kepler(normalizar(a, A_TIERRA_1E6KM), normalizar(t, T_TIERRA_D))


def pruebas() -> None:
    assert normalizar(10.0, 5.0) == 2.0
    assert razon_kepler(1.0, 1.0) == 1.0
    assert periodo_predicho(4.0) == 8.0                     # 4 ** 1,5
    assert periodo_predicho(4.0, exponente=2) == 16.0       # argumento por nombre
    assert desviacion_porcentual(110.0, 100.0) == 10.0
    assert abs(planeta_a_razon("Tierra") - 1.0) < 1e-12
    for nombre in DATOS:
        assert abs(planeta_a_razon(nombre) - 1.0) < 0.02, nombre


if __name__ == "__main__":
    pruebas()
    print(f"python {sys.version.split()[0]} | kepler.py: pruebas OK")
