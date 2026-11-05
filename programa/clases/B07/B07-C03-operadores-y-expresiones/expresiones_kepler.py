#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C03: operadores y expresiones con la tercera ley de Kepler.

Datos PUBLICADOS: NASA NSSDC, fichas individuales de planetas (act. 11-ene-2024 a
19-may-2025), consultadas el 2026-11-05: semieje mayor (1e6 km) y período sidéreo (d).
Modelo: T^2 / a^3 es casi constante si T se mide en años terrestres y a en unidades
de la distancia de la Tierra al Sol (ley de Kepler; la clase la usa como regularidad,
sin derivarla). Supuestos: órbitas casi circulares; «año» = período sidéreo de la Tierra
(365,256 d); a = semieje mayor publicado.
Dominio de validez: planetas del sistema solar con estos datos redondeados.
Tolerancia: la razón T^2/a^3 debe estar a ±2 % de 1 para cada planeta.
"""

from __future__ import annotations

import sys

DATOS = {  # nombre: (semieje mayor en 1e6 km, período sidéreo en días)
    "Mercurio": (57.909, 87.969),
    "Venus": (108.210, 224.701),
    "Tierra": (149.598, 365.256),
    "Marte": (227.956, 686.980),
    "Júpiter": (778.479, 4332.589),
    "Saturno": (1432.041, 10755.699),
    "Urano": (2867.043, 30685.400),
    "Neptuno": (4514.953, 60189.018),
}
A_TIERRA = DATOS["Tierra"][0]
T_TIERRA = DATOS["Tierra"][1]


def razon_kepler(semieje_1e6km: float, periodo_d: float) -> float:
    """Devuelve T^2 / a^3 con T en años terrestres y a en distancias terrestres."""
    t_anios = periodo_d / T_TIERRA
    a_rel = semieje_1e6km / A_TIERRA
    return t_anios ** 2 / a_rel ** 3


def pruebas() -> None:
    assert abs(razon_kepler(A_TIERRA, T_TIERRA) - 1.0) < 1e-12      # la Tierra es la unidad
    assert 2 + 3 * 4 == 14 and (2 + 3) * 4 == 20                    # precedencia
    assert -3 ** 2 == -9 and (-3) ** 2 == 9                         # ** liga más que el signo
    assert 2 ** 3 ** 2 == 512                                       # ** asocia a la derecha
    for nombre, (a, t) in DATOS.items():
        r = razon_kepler(a, t)
        assert abs(r - 1.0) < 0.02, (nombre, r)                     # tolerancia declarada


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"{'planeta':<9}{'a/a_T':>9}{'T (años)':>12}{'T^2/a^3':>10}")
    for nombre, (a, t) in DATOS.items():
        print(f"{nombre:<9}{a / A_TIERRA:>9.3f}{t / T_TIERRA:>12.3f}{razon_kepler(a, t):>10.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
