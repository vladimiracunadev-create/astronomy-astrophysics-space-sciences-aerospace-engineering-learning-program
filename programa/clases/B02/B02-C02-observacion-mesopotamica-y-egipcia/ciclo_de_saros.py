#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B02-C02: por qué el ciclo de Saros "cierra".

Datos PUBLICADOS (NASA, Five Millennium Canon / página «Saros», consultada el
2026-11-05, valores hacia el año 2000): 223 meses sinódicos = 6585,3223 d;
239 anómalos = 6585,5375 d; 242 dracónicos = 6585,3575 d.
Modelo: tres períodos lunares medios casi conmensurables. Supuestos: períodos
medios constantes. Validez: ilustra la regularidad; NO predice eclipses reales
(para eso se necesitan efemérides). Tolerancia: 0,3 d entre los tres múltiplos.
"""

from __future__ import annotations

import sys

SINODICO_223 = 6585.3223
ANOMALO_239 = 6585.5375
DRACONICO_242 = 6585.3575


def pruebas() -> None:
    # Referencia independiente: la página de NASA da "18 años, 11 días y 8 horas" (~6585,33 d).
    assert abs(SINODICO_223 - (18 * 365.2425 + 11 + 8 / 24)) < 1.5      # holgura: 4 o 5 días bisiestos
    # Los tres múltiplos coinciden dentro de 0,3 d:
    assert max(SINODICO_223, ANOMALO_239, DRACONICO_242) - min(SINODICO_223, ANOMALO_239, DRACONICO_242) < 0.3
    # Un Saros de 6585,3223 d es 6585 d enteros más 0,3223 d:
    assert int(SINODICO_223) == 6585


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    fr = SINODICO_223 - int(SINODICO_223)
    print(f"Saros: {SINODICO_223} d = {int(SINODICO_223)} d + {fr * 24:.1f} h")
    print(f"Mes sinódico implícito: {SINODICO_223 / 223:.5f} d")
    print(f"Mes anómalo implícito:  {ANOMALO_239 / 239:.5f} d")
    print(f"Mes dracónico implícito: {DRACONICO_242 / 242:.5f} d")
    print(f"Diferencia anómalo − sinódico: {(ANOMALO_239 - SINODICO_223) * 24:.1f} h")
    print(f"Diferencia dracónico − sinódico: {(DRACONICO_242 - SINODICO_223) * 24:.1f} h")
    corrimiento = fr * 360.0
    print(f"Un Saros: la Tierra gira {corrimiento:.0f}° de más → el eclipse se desplaza ≈{corrimiento:.0f}° en longitud")
    tres = 3 * SINODICO_223
    f3 = tres - round(tres)
    print(f"Tres Saros: {tres:.2f} d (≈{tres / 365.2425:.1f} años); resto {f3:+.3f} d = {f3 * 360:+.0f}° de giro terrestre")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
