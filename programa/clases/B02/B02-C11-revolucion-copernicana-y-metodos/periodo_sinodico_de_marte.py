#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C11: el período sinódico de Marte desde el modelo heliocéntrico.

Datos PUBLICADOS (NASA NSSDC Earth y Mars Fact Sheets, consultadas el 2026-11-05):
períodos orbitales sidéreos de la Tierra (365,256 d) y Marte (686,980 d); período
sinódico publicado de Marte: 779,94 d; semiejes mayores 149,598 y 227,956 millones de km.
Modelo: órbitas circulares coplanares con velocidad angular constante (simplificación de
Copérnico). Supuestos: períodos medios. Validez: orden de magnitud del retorno de la
oposición; NO predice fechas reales (las órbitas reales son elípticas).
Tolerancia: 0,05 d frente al valor publicado.
"""

from __future__ import annotations

import sys

T_TIERRA = 365.256      # d
T_MARTE = 686.980       # d
SINODICO_MARTE_PUBLICADO = 779.94   # d
A_TIERRA = 149.598      # 10^6 km
A_MARTE = 227.956       # 10^6 km


def sinodico_exterior(t_interior: float, t_exterior: float) -> float:
    """Planeta exterior visto desde la Tierra: 1/S = 1/T_Tierra − 1/T_exterior."""
    return 1.0 / (1.0 / t_interior - 1.0 / t_exterior)


def pruebas() -> None:
    s = sinodico_exterior(T_TIERRA, T_MARTE)
    assert abs(s - SINODICO_MARTE_PUBLICADO) < 0.05, s                 # referencia publicada
    assert abs(sinodico_exterior(1.0, 2.0) - 2.0) < 1e-12              # caso analítico: T=1 y 2 → S=2
    assert abs((T_MARTE / T_TIERRA) ** (2 / 3) - A_MARTE / A_TIERRA) < 0.01   # tercera ley (C14)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    s = sinodico_exterior(T_TIERRA, T_MARTE)
    print(f"Sinódico calculado: {s:.2f} d = {s / 365.256:.3f} años (publicado: {SINODICO_MARTE_PUBLICADO} d)")
    print(f"Tierra: {360 / T_TIERRA:.4f}°/d; Marte: {360 / T_MARTE:.4f}°/d; la Tierra gana {360 / T_TIERRA - 360 / T_MARTE:.4f}°/d")
    print(f"Distancia mínima aproximada en oposición (órbitas circulares): {(A_MARTE - A_TIERRA):.1f} millones de km")
    print(f"Razón de semiejes publicada: {A_MARTE / A_TIERRA:.3f}; (T_Marte/T_Tierra)^(2/3) = {(T_MARTE / T_TIERRA) ** (2 / 3):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
