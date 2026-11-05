#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Módulo B07-C17: funciones matemáticas pequeñas y probables.

Datos: ninguno observado. Los casos de prueba son analíticos (esfera unitaria, raíces
conocidas) y un dato PUBLICADO: período sidéreo de la Tierra 365,256 d y semieje mayor de
Marte 227,956e6 km / Tierra 149,598e6 km (NASA NSSDC, consultado el 2026-11-05).
Modelo: (1) volumen de una esfera; (2) raíces de a x² + b x + c = 0 en reales;
(3) período de Kepler T = a^1,5 (años terrestres, distancias terrestres).
Supuestos: entradas finitas; las raíces complejas se rechazan con ValueError.
Dominio de validez: radio ≥ 0; a > 0 para el período; a ≠ 0 para la cuadrática.
Tolerancia: los tests exigen error relativo ≤ 1e-12 salvo donde se indique.
"""

from __future__ import annotations

import math


def volumen_esfera(radio: float) -> float:
    """Volumen de una esfera (unidades de radio al cubo); radio < 0 lanza ValueError."""
    if radio < 0:
        raise ValueError(f"radio negativo: {radio}")
    return 4.0 / 3.0 * math.pi * radio ** 3


def raices_ingenuas(a: float, b: float, c: float) -> tuple[float, float]:
    """Raíces reales con la fórmula directa (pierde cifras si b² ≫ 4ac). Para comparar."""
    d = _discriminante_raiz(a, b, c)
    return (-b - d) / (2 * a), (-b + d) / (2 * a)


def raices_estables(a: float, b: float, c: float) -> tuple[float, float]:
    """Raíces reales (menor, mayor) evitando la resta de números casi iguales."""
    d = _discriminante_raiz(a, b, c)
    q = -0.5 * (b + math.copysign(d, b))
    r1 = q / a
    r2 = c / q if q != 0 else r1
    return (r1, r2) if r1 <= r2 else (r2, r1)


def _discriminante_raiz(a: float, b: float, c: float) -> float:
    if a == 0:
        raise ValueError("a no puede ser 0")
    disc = b * b - 4 * a * c
    if disc < 0:
        raise ValueError(f"discriminante negativo: {disc}")
    return math.sqrt(disc)


def periodo_kepler_anios(semieje_rel: float) -> float:
    """Período (años terrestres) para un semieje en distancias terrestres: a^1,5."""
    if not semieje_rel > 0:
        raise ValueError(f"el semieje debe ser positivo: {semieje_rel}")
    return semieje_rel ** 1.5
